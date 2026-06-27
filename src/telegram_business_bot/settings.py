from __future__ import annotations

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    telegram_bot_token: str = Field(default="replace-me")
    admin_user_ids: str = ""
    leads_csv_path: Path = Path("data/leads.csv")
    business_name: str = "Acme Services"

    @property
    def admin_ids(self) -> set[int]:
        return {
            int(value.strip())
            for value in self.admin_user_ids.split(",")
            if value.strip().isdigit()
        }
