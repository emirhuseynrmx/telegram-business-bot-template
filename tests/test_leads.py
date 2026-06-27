from __future__ import annotations

from telegram_business_bot.leads import LeadStore, parse_lead_command


def test_parse_lead_command() -> None:
    lead = parse_lead_command("/lead Alice | alice@example.com | Need a quote")

    assert lead.name == "Alice"
    assert lead.email == "alice@example.com"
    assert lead.message == "Need a quote"


def test_lead_store_appends_and_reads_rows(tmp_path) -> None:
    store = LeadStore(tmp_path / "leads.csv")
    lead = parse_lead_command("/lead Alice | alice@example.com | Need a quote")

    store.append(lead)
    rows = store.read_all()

    assert rows[0]["name"] == "Alice"
    assert rows[0]["email"] == "alice@example.com"
