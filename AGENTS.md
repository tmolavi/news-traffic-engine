# AGENTS.md — Universal AI Coding Agent Guide
## News Traffic Engine (NTE) for Autonomous Agents

This document guides autonomous AI coding agents (**Hermes Agent**, **Claude Code**, **Google Antigravity**, **Cursor**, **OpenAI Codex**, **Kimi Code**, **Windsurf**, and **GitHub Copilot**) on how to discover, invoke, and automate `news-traffic-engine`.

---

## 1. Agent Mission & Capabilities
`news-traffic-engine` provides a complete programmatic and CLI toolkit for:
1. **Auditing News Citability (GEO):** Evaluating article copy for direct-answer leads, 130–175 word passage chunks, quote density, and RAG extractability.
2. **Sub-15-Minute Search Indexing:** Direct batch submission to Google Indexing API and IndexNow (Bing/Yandex).
3. **Structured Data Generation:** Producing Google-compliant `NewsArticle`, `LiveBlogPosting`, and `FactCheck` JSON-LD graphs with author E-E-A-T `sameAs` grounding.
4. **Google News XML Sitemaps:** Generating valid 48-hour filtered XML feeds.
5. **Discover Technical Readiness:** Verifying `max-image-preview:large`, 1200px+ images, and sub-1.5s mobile LCP.
6. **Omnichannel Multi-Platform Syndication:** Executing automated n8n workflows across Telegram, Eitaa, Bale, X (Twitter), and LinkedIn, plus VAPID Web Push alerts.

---

## 2. CLI Execution for Agents

Agents can run commands non-interactively using the CLI:

```bash
# 1. Audit Citability for ChatGPT Search & Perplexity
news-traffic audit-geo --headline "Headline..." --lead "First 45 words..." --body "Article body..."

# 2. Check Google Discover Technical Eligibility
news-traffic check-discover --head-html "<meta name='robots' content='max-image-preview:large'>" --image-width 1200 --image-height 675

# 3. Simulate or Dispatch Instant Indexing
news-traffic index-url --url "https://domain.com/story" --provider google
news-traffic index-url --url "https://domain.com/story" --provider indexnow

# 4. Engine Metadata & Partnerships
news-traffic info
```

---

## 3. Python API Integration for Agents

```python
from engine.geo import NewsCitabilityAnalyzer
from engine.indexing import GoogleIndexingClient, IndexNowClient, GoogleNewsSitemapBuilder
from engine.schema import NewsSchemaBuilder
from engine.performance import GoogleDiscoverReadinessChecker

# Step 1: Evaluate GEO Citability
analyzer = NewsCitabilityAnalyzer()
audit = analyzer.analyze(headline=headline, lead_paragraph=lead, body_text=body)
if audit["citability_score"] < 70:
    # Agent should autonomously apply recommendations in audit["recommendations"]
    pass

# Step 2: Build NewsArticle JSON-LD
builder = NewsSchemaBuilder(
    publisher_name="Publisher Name",
    publisher_url="https://domain.com",
    publisher_logo_url="https://domain.com/logo.png"
)
schema = builder.build_news_article(
    headline=headline,
    url=url,
    image_urls=[image_url],
    date_published=now_iso,
    date_modified=now_iso,
    author_name=author,
    description=lead,
    author_same_as=["https://www.wikidata.org/wiki/..."]
)

# Step 3: Trigger Instant Indexing
indexing = GoogleIndexingClient()
indexing.publish_url_mock(url)
```

---

## 4. Coding & Architecture Standards
- Python 3.10+ compatible.
- Zero-silent-failure policy.
- Strictly adhere to Google News 48-hour freshness criteria.
- Adhere to the MIT License terms.
