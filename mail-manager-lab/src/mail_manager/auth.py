from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import unicodedata
from typing import Any

import yaml


CANONICAL_ACTIONS = {
    "list_headers",
    "preview_body",
    "create_draft",
    "move_to_review",
    "send_email",
    "open_attachment",
    "follow_link",
    "delete_email",
}


LEGACY_ACTION_ALIASES = {
    "read_headers": "list_headers",
    "preview_safe": "preview_body",
    "draft_reply": "create_draft",
    "send_reply": "send_email",
    "move_to_review_trash": "move_to_review",
    "open_attachments": "open_attachment",
    "follow_links": "follow_link",
}


SENSITIVE_ACTIONS = {
    "create_draft",
    "move_to_review",
    "send_email",
    "open_attachment",
    "follow_link",
    "delete_email",
}


NATURAL_MAILBOX_ALIASES = {
    "administracion": "administracion-vielha",
    "administración": "administracion-vielha",
    "admin": "administracion-vielha",
    "reservas": "reservas-tossa",
    "reserva": "reservas-tossa",
    "direccion": "direccion-tossa",
    "dirección": "direccion-tossa",
    "info": "vielhacomputer",
    "principal": "vielhacomputer",
}


@dataclass(frozen=True)
class MailAuthResult:
    allowed: bool
    reason: str
    safe_message: str
    requires_confirmation: bool = False
    user_key: str | None = None
    mailbox: str | None = None
    action: str | None = None


def normalize_text(value: str) -> str:
    return unicodedata.normalize("NFKC", str(value).strip().lower())


def normalize_action(action: str) -> str:
    normalized = normalize_text(action)
    return LEGACY_ACTION_ALIASES.get(normalized, normalized)


def resolve_mailbox_phrase(phrase_or_mailbox: str) -> str | None:
    key = normalize_text(phrase_or_mailbox)
    if not key:
        return None

    return NATURAL_MAILBOX_ALIASES.get(key, key)


def load_policy(config_path: str | Path) -> dict[str, Any]:
    try:
        path = Path(config_path)
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}

    if not isinstance(data, dict):
        return {}

    return data


def find_user_by_telegram_id(
    policy: dict[str, Any],
    telegram_user_id: str,
) -> tuple[str | None, dict[str, Any] | None]:
    users = policy.get("users") or {}
    if not isinstance(users, dict):
        return None, None

    wanted = str(telegram_user_id).strip()

    for user_key, user_cfg in users.items():
        if not isinstance(user_cfg, dict):
            continue

        current = str(user_cfg.get("telegram_user_id", "")).strip()
        if current == wanted:
            return str(user_key), user_cfg

    return None, None


def user_allowed_mailboxes(user_cfg: dict[str, Any]) -> set[str]:
    raw = user_cfg.get("allowed_mailboxes") or user_cfg.get("mailboxes") or []
    if not isinstance(raw, list):
        return set()

    return {str(item).strip() for item in raw if str(item).strip()}


def user_allowed_actions(
    user_cfg: dict[str, Any],
    role_cfg: dict[str, Any] | None = None,
) -> set[str]:
    raw = user_cfg.get("allowed_actions") or user_cfg.get("permissions") or []

    role_raw: list[Any] = []
    if role_cfg:
        role_raw = (
            role_cfg.get("default_actions")
            or role_cfg.get("default_permissions")
            or []
        )

    merged = list(role_raw or []) + list(raw or [])

    return {
        normalize_action(str(item))
        for item in merged
        if str(item).strip()
    }


def authorize_mail_action(
    telegram_user_id: str,
    mailbox: str,
    action: str,
    *,
    config_path: str | Path,
) -> MailAuthResult:
    policy = load_policy(config_path)
    if not policy:
        return MailAuthResult(
            allowed=False,
            reason="policy_unavailable",
            safe_message="Ahora mismo no puedo validar permisos para esta acción.",
        )

    user_key, user_cfg = find_user_by_telegram_id(policy, telegram_user_id)
    if not user_cfg:
        return MailAuthResult(
            allowed=False,
            reason="user_not_found",
            safe_message="Ahora mismo no puedo atender esta solicitud desde este Telegram.",
        )

    status = str(user_cfg.get("status", "")).strip().lower()
    if status != "active":
        return MailAuthResult(
            allowed=False,
            reason="user_inactive",
            safe_message="Ahora mismo no puedo atender esta solicitud desde este Telegram.",
            user_key=user_key,
        )

    resolved_mailbox = resolve_mailbox_phrase(mailbox)
    if not resolved_mailbox:
        return MailAuthResult(
            allowed=False,
            reason="mailbox_unresolved",
            safe_message="No puedo identificar el buzón solicitado de forma segura.",
            user_key=user_key,
        )

    configured_mailboxes = policy.get("mailboxes") or {}
    if isinstance(configured_mailboxes, dict) and configured_mailboxes:
        if resolved_mailbox not in configured_mailboxes:
            return MailAuthResult(
                allowed=False,
                reason="mailbox_unknown",
                safe_message="Este usuario no tiene permiso para acceder a ese buzón.",
                user_key=user_key,
            )

    allowed_mailboxes = user_allowed_mailboxes(user_cfg)
    if resolved_mailbox not in allowed_mailboxes:
        return MailAuthResult(
            allowed=False,
            reason="mailbox_not_allowed",
            safe_message=(
                "Este usuario no tiene permiso para acceder a ese buzón.\n\n"
                "El administrador puede ampliar los permisos si corresponde."
            ),
            user_key=user_key,
        )

    normalized_action = normalize_action(action)
    if normalized_action not in CANONICAL_ACTIONS:
        return MailAuthResult(
            allowed=False,
            reason="unknown_action",
            safe_message="Este usuario no tiene permiso para realizar esa acción.",
            user_key=user_key,
            mailbox=resolved_mailbox,
        )

    roles = policy.get("roles") or {}
    role_name = str(user_cfg.get("role", "")).strip()
    role_cfg = roles.get(role_name) if isinstance(roles, dict) else None

    allowed_actions = user_allowed_actions(user_cfg, role_cfg)

    if normalized_action not in allowed_actions:
        return MailAuthResult(
            allowed=False,
            reason="action_not_allowed",
            safe_message=(
                "Este usuario no tiene permiso para realizar esa acción.\n\n"
                "Puedo continuar solo con acciones autorizadas."
            ),
            user_key=user_key,
            mailbox=resolved_mailbox,
            action=normalized_action,
        )

    requires_confirmation = normalized_action in SENSITIVE_ACTIONS

    return MailAuthResult(
        allowed=True,
        reason="allowed",
        safe_message="Acción autorizada.",
        requires_confirmation=requires_confirmation,
        user_key=user_key,
        mailbox=resolved_mailbox,
        action=normalized_action,
    )
