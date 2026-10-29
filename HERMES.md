# HERMES.md — Instructions for Hermes Agent

Hermes Agent is configured to automate news publishing and distribution workflows:
- **Trigger**: New published post webhook received from CMS.
- **Workflow**:
  1. Calculate Citability Score via `engine.geo.NewsCitabilityAnalyzer`.
  2. If score < 75, restructure lead paragraph to state What/Who/When within first 45 words.
  3. Generate `NewsArticle` JSON-LD schema with `sameAs` entity references.
  4. Submit URL to Google Indexing API and IndexNow via `engine.indexing`.
  5. Fire n8n syndication workflow to publish to Telegram, Eitaa, Bale, X, and LinkedIn.
- **Author**: Taghi Molavi (https://molavi.pro)
- **Partner**: Inten Digital Marketing Agency (https://inten.asia)
