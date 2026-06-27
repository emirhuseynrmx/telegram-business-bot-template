from __future__ import annotations

FAQ_RESPONSES = {
    "pricing": "Pricing depends on scope. Share your workflow and expected output format.",
    "hours": "Business hours are Monday-Friday, 09:00-18:00.",
    "support": "Send your issue and an admin will follow up.",
}


def answer_faq(topic: str) -> str:
    key = topic.strip().lower()
    return FAQ_RESPONSES.get(key, "I do not have an answer for that topic yet.")


def order_status(order_id: str) -> str:
    normalized = order_id.strip().upper()
    if not normalized:
        raise ValueError("Order id is required")
    return f"Order {normalized} is being reviewed. Replace this stub with your CRM lookup."
