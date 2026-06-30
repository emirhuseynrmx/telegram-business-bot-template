from __future__ import annotations

FAQ_RESPONSES = {
    "pricing": (
        "Fiyatlandırma kapsama göre değişir:\n"
        "- Starter (1.500-3.000 EUR): tek pipeline veya rapor, 5 iş günü\n"
        "- Growth (3.000-8.000 EUR): ETL + ML model + API, 10-15 iş günü\n"
        "- Enterprise (8.000+ EUR): uçtan uca veri platformu + ekip eğitimi\n"
        "- Saatlik danışmanlık: 95 EUR/saat (min 2 saat)\n"
        "24 saat içinde özel teklif için: contact@dataflow-analytics.io"
    ),
    "hours": (
        "Çalışma saatleri: Pazartesi-Cuma, 09:00-18:00 CET.\n"
        "Standart destek: 24 iş saati içinde yanıt.\n"
        "Öncelikli destek (Enterprise): 4 iş saati içinde yanıt.\n"
        "Kritik hatalar (pipeline çökmesi): 2 iş saati içinde yanıt."
    ),
    "support": (
        "Destek talebi açmak için support@dataflow-analytics.io adresine şunları gönderin:\n"
        "1. Proje referans numaranız (format: DF-YYYY-NNNN)\n"
        "2. Sorunun açıklaması ve yeniden üretme adımları\n"
        "3. Hata mesajları veya ekran görüntüleri\n"
        "Teslimat sonrası 30 gün içindeki kritik hatalar ücretsiz giderilir."
    ),
    "refund": (
        "İade politikası:\n"
        "- Teslimattan 7 gün içinde: spesifikasyon uyumsuzluğunda tam iade\n"
        "- 8-14. günler: önemli hata tespit edilirse %50 iade\n"
        "- 14 günden sonra: iade yok, ancak 30 gün kritik hata desteği ücretsiz\n"
        "Saatlik danışmanlık seansları iade kapsamı dışındadır."
    ),
    "timeline": (
        "Tipik proje süreleri:\n"
        "- Starter: 3-5 iş günü\n"
        "- Growth: 10-15 iş günü\n"
        "- Enterprise: 4-12 hafta (kapsama göre)\n"
        "Kesin tarihler iş başlamadan önce imzalanan iş tanımında belirtilir."
    ),
    "formats": (
        "Kabul edilen veri formatları: CSV, Excel, JSON, Parquet, PostgreSQL, MySQL, "
        "Google Sheets, REST API.\n"
        "Teslimat formatları: CSV, Excel, Parquet, JSON Lines, PDF rapor, "
        "HTML dashboard, REST API, PostgreSQL dump, ONNX/Joblib model."
    ),
    "payment": (
        "Ödeme koşulları:\n"
        "- Sabit kapsam projeler: %50 başlangıç, %50 teslimatta\n"
        "- Retainer: ayın 1'inde aylık peşin\n"
        "- Saatlik: haftalık fatura, 7 gün vade\n"
        "Kabul edilen yöntemler: SEPA, Stripe (Visa/MC/AMEX), Wise. Para birimi: EUR."
    ),
    "privacy": (
        "Gizlilik politikası:\n"
        "- Tüm müşteri verileri yalnızca proje kapsamında kullanılır\n"
        "- Proje tamamlanmasından 30 gün sonra veriler silinir\n"
        "- Veriler AB'de şifreli sunucularda saklanır (Hetzner Cloud, Frankfurt)\n"
        "- NDA ücretsiz imzalanır, talep üzerine"
    ),
    "integrations": (
        "Entegre ettiğimiz araçlar: Zapier, n8n, Google Workspace, Notion, Airtable, "
        "Telegram, Slack, HubSpot, Pipedrive, Salesforce.\n"
        "Farklı bir araçla entegrasyon için bizimle iletişime geçin."
    ),
    "consultation": (
        "Evet — 30 dakikalık keşif görüşmesi ücretsiz ve bağlayıcı değildir.\n"
        "Rezervasyon: contact@dataflow-analytics.io adresine projenizin kısa "
        "açıklamasıyla yazın."
    ),
}


def answer_faq(topic: str) -> str:
    key = topic.strip().lower()
    fallback = (
        "Bu konu için henüz bir yanıtım yok. "
        "Lütfen contact@dataflow-analytics.io adresine yazın."
    )
    return FAQ_RESPONSES.get(key, fallback)


def order_status(order_id: str) -> str:
    normalized = order_id.strip().upper()
    if not normalized:
        raise ValueError("Proje referans numarası gereklidir")
    if not normalized.startswith("DF-"):
        return (
            f"'{normalized}' tanınan bir format değil. "
            "Lütfen DF-YYYY-NNNN formatındaki proje numaranızı kullanın."
        )
    return (
        f"Proje {normalized} için durum: aktif takip altında. "
        "Detaylı güncelleme için support@dataflow-analytics.io adresine yazın."
    )
