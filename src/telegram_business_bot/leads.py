from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

from pydantic import BaseModel, ConfigDict, EmailStr


class Lead(BaseModel):
    model_config = ConfigDict(frozen=True, str_strip_whitespace=True)

    name: str
    email: EmailStr
    message: str
    created_at: datetime

    def to_row(self) -> dict[str, str]:
        return {
            "name": self.name,
            "email": self.email,
            "message": self.message,
            "created_at": self.created_at.isoformat(),
        }


class LeadStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def append(self, lead: Lead) -> Path:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        exists = self.path.exists()
        with self.path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "email", "message", "created_at"])
            if not exists:
                writer.writeheader()
            writer.writerow(lead.to_row())
        return self.path

    def read_all(self) -> list[dict[str, str]]:
        if not self.path.exists():
            return []
        with self.path.open(newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))


def parse_lead_command(text: str) -> Lead:
    raw = text.removeprefix("/lead").strip()
    parts = [part.strip() for part in raw.split("|")]
    if len(parts) != 3:
        raise ValueError("Use: /lead name | email | message")
    return Lead(
        name=parts[0],
        email=parts[1],
        message=parts[2],
        created_at=datetime.now(timezone.utc),
    )
