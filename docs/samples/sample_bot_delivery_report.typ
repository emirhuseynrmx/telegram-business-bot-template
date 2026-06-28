#set page(margin: 42pt)
#set text(font: "Arial", size: 10pt)
#set heading(numbering: none)

#let accent = rgb("#1457d9")
#let good = rgb("#11845b")
#let muted = rgb("#667085")
#let panel = rgb("#f6f8fb")

#let stat(label, value, color: accent) = block[
  #rect(fill: panel, radius: 5pt, inset: 10pt, width: 100%)[
    #text(size: 8pt, fill: muted, weight: "bold")[#upper(label)]
    #linebreak()
    #text(size: 18pt, fill: color, weight: "bold")[#value]
  ]
]

= Telegram Business Bot Delivery Report

#text(fill: muted)[
  Sample delivery report for a small-business Telegram bot. The template covers
  lead capture, FAQs, status replies, alerts, and admin export.
]

#grid(columns: (1fr, 1fr, 1fr, 1fr), gutter: 8pt)[
  #stat("Commands", "5")
][
  #stat("Lead export", "CSV")
][
  #stat("Validation", "Pydantic")
][
  #stat("Network tests", "0", color: good)
]

== Bot Commands

#table(
  columns: (1fr, 2fr),
  inset: 5pt,
  stroke: rgb("#d0d5dd"),
  [*Command*], [*Purpose*],
  [`/start`], [Onboarding and quick help],
  [`/lead`], [Capture name, email, and message],
  [`/faq`], [Answer common business questions],
  [`/status`], [Return order or request status],
  [`/export_leads`], [Admin-only lead CSV export],
)

== Handoff Checklist

- `.env.example` included for bot token and admin configuration
- Lead validation rejects bad email and empty messages
- Service tests run without calling Telegram
- CSV export is simple enough for Google Sheets or CRM import

== Scope Notes

- Uses user-owned Telegram Bot API credentials.
- Does not automate spam, scraping, or unsolicited outreach.
