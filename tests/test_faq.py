from __future__ import annotations

import pytest

from telegram_business_bot.faq import answer_faq, order_status


def test_answer_faq_known_topic() -> None:
    assert "scope" in answer_faq("pricing")


def test_answer_faq_unknown_topic() -> None:
    assert "not have an answer" in answer_faq("unknown")


def test_order_status_requires_id() -> None:
    with pytest.raises(ValueError, match="Order id is required"):
        order_status("")


def test_order_status_returns_stub_message() -> None:
    assert "ABC123" in order_status("abc123")
