from __future__ import annotations

import pytest

from telegram_business_bot.faq import answer_faq, order_status


def test_answer_faq_known_topic() -> None:
    assert "EUR" in answer_faq("pricing")


def test_answer_faq_unknown_topic() -> None:
    assert "contact" in answer_faq("unknown").lower()


def test_order_status_requires_id() -> None:
    with pytest.raises(ValueError, match="gereklidir"):
        order_status("")


def test_order_status_returns_project_reference() -> None:
    result = order_status("DF-2025-0042")
    assert "DF-2025-0042" in result
