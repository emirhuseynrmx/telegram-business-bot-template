from __future__ import annotations

from telegram_business_bot.settings import Settings


def test_settings_parses_admin_ids() -> None:
    settings = Settings(admin_user_ids="123, abc, 456")

    assert settings.admin_ids == {123, 456}
