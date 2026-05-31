from pathlib import Path
import textwrap

from mail_manager.auth import authorize_mail_action, resolve_mailbox_phrase


def write_policy(tmp_path: Path, content: str) -> Path:
    cfg = tmp_path / "telegram-users.yaml"
    cfg.write_text(textwrap.dedent(content), encoding="utf-8")
    return cfg


def test_resolve_mailbox_aliases():
    assert resolve_mailbox_phrase("administración") == "administracion-vielha"
    assert resolve_mailbox_phrase("administracion") == "administracion-vielha"
    assert resolve_mailbox_phrase("admin") == "administracion-vielha"
    assert resolve_mailbox_phrase("reservas") == "reservas-tossa"
    assert resolve_mailbox_phrase("dirección") == "direccion-tossa"
    assert resolve_mailbox_phrase("direccion") == "direccion-tossa"
    assert resolve_mailbox_phrase("info") == "vielhacomputer"


def test_owner_can_list_headers(tmp_path):
    cfg = write_policy(
        tmp_path,
        """
        version: 1
        mailboxes:
          administracion-vielha: {}
        roles:
          owner:
            default_actions:
              - list_headers
              - preview_body
              - send_email
        users:
          grover:
            telegram_user_id: 5703152430
            status: active
            role: owner
            allowed_mailboxes:
              - administracion-vielha
        """,
    )

    result = authorize_mail_action(
        "5703152430",
        "administración",
        "list_headers",
        config_path=cfg,
    )

    assert result.allowed is True
    assert result.reason == "allowed"
    assert result.mailbox == "administracion-vielha"
    assert result.action == "list_headers"
    assert result.requires_confirmation is False


def test_owner_send_email_requires_confirmation(tmp_path):
    cfg = write_policy(
        tmp_path,
        """
        version: 1
        mailboxes:
          administracion-vielha: {}
        roles:
          owner:
            default_actions:
              - send_email
        users:
          grover:
            telegram_user_id: 5703152430
            status: active
            role: owner
            allowed_mailboxes:
              - administracion-vielha
        """,
    )

    result = authorize_mail_action(
        "5703152430",
        "administracion-vielha",
        "send_email",
        config_path=cfg,
    )

    assert result.allowed is True
    assert result.requires_confirmation is True


def test_operator_can_list_allowed_mailbox(tmp_path):
    cfg = write_policy(
        tmp_path,
        """
        version: 1
        mailboxes:
          administracion-vielha: {}
          reservas-tossa: {}
        roles:
          operator:
            default_actions:
              - list_headers
              - preview_body
        users:
          sharon:
            telegram_user_id: 1336773370
            status: active
            role: operator
            allowed_mailboxes:
              - administracion-vielha
        """,
    )

    result = authorize_mail_action(
        "1336773370",
        "administración",
        "list_headers",
        config_path=cfg,
    )

    assert result.allowed is True
    assert result.mailbox == "administracion-vielha"


def test_operator_cannot_access_denied_mailbox(tmp_path):
    cfg = write_policy(
        tmp_path,
        """
        version: 1
        mailboxes:
          administracion-vielha: {}
          reservas-tossa: {}
        roles:
          operator:
            default_actions:
              - list_headers
        users:
          sharon:
            telegram_user_id: 1336773370
            status: active
            role: operator
            allowed_mailboxes:
              - administracion-vielha
        """,
    )

    result = authorize_mail_action(
        "1336773370",
        "reservas",
        "list_headers",
        config_path=cfg,
    )

    assert result.allowed is False
    assert result.reason == "mailbox_not_allowed"
    assert "reservas-tossa" not in result.safe_message


def test_operator_cannot_send_without_permission(tmp_path):
    cfg = write_policy(
        tmp_path,
        """
        version: 1
        mailboxes:
          administracion-vielha: {}
        roles:
          operator:
            default_actions:
              - list_headers
        users:
          sharon:
            telegram_user_id: 1336773370
            status: active
            role: operator
            allowed_mailboxes:
              - administracion-vielha
        """,
    )

    result = authorize_mail_action(
        "1336773370",
        "administración",
        "send_email",
        config_path=cfg,
    )

    assert result.allowed is False
    assert result.reason == "action_not_allowed"


def test_inactive_user_denied(tmp_path):
    cfg = write_policy(
        tmp_path,
        """
        version: 1
        mailboxes:
          administracion-vielha: {}
        roles:
          operator:
            default_actions:
              - list_headers
        users:
          sharon:
            telegram_user_id: 1336773370
            status: inactive
            role: operator
            allowed_mailboxes:
              - administracion-vielha
        """,
    )

    result = authorize_mail_action(
        "1336773370",
        "administración",
        "list_headers",
        config_path=cfg,
    )

    assert result.allowed is False
    assert result.reason == "user_inactive"


def test_unknown_user_denied(tmp_path):
    cfg = write_policy(
        tmp_path,
        """
        version: 1
        mailboxes:
          administracion-vielha: {}
        users:
          grover:
            telegram_user_id: 5703152430
            status: active
            role: owner
            allowed_mailboxes:
              - administracion-vielha
            allowed_actions:
              - list_headers
        """,
    )

    result = authorize_mail_action(
        "999999999",
        "administración",
        "list_headers",
        config_path=cfg,
    )

    assert result.allowed is False
    assert result.reason == "user_not_found"


def test_missing_policy_fails_closed():
    result = authorize_mail_action(
        "5703152430",
        "administración",
        "list_headers",
        config_path="C:/no/existe/telegram-users.yaml",
    )

    assert result.allowed is False
    assert result.reason == "policy_unavailable"
