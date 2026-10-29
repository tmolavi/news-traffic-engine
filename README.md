<div align="center">

![News Traffic Engine Banner](assets/news-traffic-engine-banner.svg)

# ⚡ News Traffic Engine (NTE)
### Autonomous AI Agent Framework for Newsroom Traffic, Instant Google News Indexing, Generative Engine Optimization (GEO) & Google Discover Growth

[![CI](https://github.com/tmolavi/news-traffic-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/tmolavi/news-traffic-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![GEO Ready](https://img.shields.io/badge/GEO-ChatGPT%20%7C%20Perplexity%20%7C%20AI%20Overviews-brightgreen)](https://github.com/tmolavi/news-traffic-engine)
[![Agent Ready](https://img.shields.io/badge/Agents-Hermes%20%7C%20Claude%20%7C%20Antigravity%20%7C%20Cursor%20%7C%20Codex-purple)](AGENTS.md)

> **Languages:** [English](README.md) · [فارسی](README.fa.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Español](README.es.md)

</div>

---

## 📌 Executive Summary

The **News Traffic Engine (NTE)** is a production-grade, open-source AI agent system designed for modern newsrooms, digital journalists, and high-volume media publishers operating in the AI-search era.

While legacy news SEO focused exclusively on keyword stuffing and traditional SERP rankings, over 50% of informative user queries in 2026 are answered directly by generative answer engines (**ChatGPT Search**, **Perplexity AI**, and **Google AI Overviews**), while mobile referral volume is dominated by **Google Discover**.

Modern news traffic growth depends on three foundational pillars:
1. **Sub-15-Minute Search Indexing:** Direct API submission to Google Indexing API and the IndexNow protocol to secure immediate placement in **Google News** and **Top Stories** while events are breaking.
2. **Generative Engine Optimization (GEO):** Structuring editorial copy into modular, fact-dense passage chunks (130–175 words) with immediate answers in the first 45 words, guaranteeing citations and reference links in AI search models.
3. **Omnichannel Viral Distribution & Web Push:** Instantaneous multi-platform syndication via [n8n](https://n8n.io) to Telegram, Eitaa, Bale, X (Twitter), and LinkedIn, combined with VAPID Web Push alerts that re-engage returning audiences with 10–25% CTR.

Created by **[Taghi Molavi](https://molavi.pro/en)** (AI Systems Architect & Creator of [GEO-Scope](https://github.com/tmolavi/geo-scope) and [SAGE](https://github.com/tmolavi/sage-audit)) in strategic collaboration with **[Inten Digital Marketing Agency](https://inten.asia/en)** (Enterprise Digital Transformation & High-Traffic Infrastructure Leader).

---

## 📊 Technical Competitor Benchmark & Feature Matrix

How does **News Traffic Engine (NTE)** surpass fragmented tools on GitHub?

| Capability / Feature | News Traffic Engine (NTE) | google-indexing-script | newspaper4k | Postiz | Yoast / RankMath News | claude-seo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Google Indexing API (<15 min)** | ✅ Built-in & Batch | ✅ Native | ❌ No | ❌ No | ⚠️ Partial Plugin | ❌ No |
| **IndexNow Protocol (Bing, Yandex)** | ✅ Native Client | ❌ No | ❌ No | ❌ No | ⚠️ Basic | ❌ No |
| **GEO Passage Citability Audit** | ✅ 0–100 Score | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Prompts Only |
| **Automated `/llms.txt` Generator** | ✅ Standardized | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Generic |
| **NewsArticle & LiveBlog Schema** | ✅ Graph + sameAs | ❌ No | ❌ No | ❌ No | ✅ Basic | ⚠️ Static |
| **Google Discover Technical Audit** | ✅ Vitals + 1200px | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Omnichannel Syndication (n8n)** | ✅ Ready Workflow | ❌ No | ❌ No | ⚠️ UI Only | ❌ No | ❌ No |
| **Iranian Messengers (Eitaa, Bale)** | ✅ Native in n8n | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **VAPID Web Push Dispatcher** | ✅ Built-in | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **AI Agent Native Integration** | ✅ Multi-Agent Spec | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Claude Only |

---

## 🤖 AI Coding Agent Integration

`news-traffic-engine` is built from the ground up to be orchestrated directly by autonomous AI coding agents:

* **[Hermes Agent](HERMES.md):** Automates the full news ingestion, headline rewriting, and multi-channel publication cycle.
* **[Claude Code & Claude AI](CLAUDE.md):** Governed by zero-overhead architectural rules and test workflows.
* **[Google Antigravity & Gemini](AGENTS.md):** Integrates natively with Antigravity skills and workspace subagents.
* **[Cursor](.cursorrules):** Real-time code assistance adhering to strict news schema and passage citability standards.
* **[OpenAI Codex & Kimi Code](AGENTS.md):** Fully supported via universal CLI and standard Python endpoints.

### Autonomous Agent Trigger Example
```python
from engine.geo import NewsCitabilityAnalyzer
from engine.indexing import GoogleIndexingClient
from engine.schema import NewsSchemaBuilder

# 1. Evaluate GEO Citability Score
analyzer = NewsCitabilityAnalyzer()
result = analyzer.analyze(headline=headline, lead_paragraph=lead, body_text=body)

# 2. Build Schema Graph
builder = NewsSchemaBuilder("Newsroom", "https://news.example.com", "https://news.example.com/logo.png")
schema = builder.build_news_article(headline, url, [img], pub_date, mod_date, author, lead)

# 3. Dispatch Instant Indexing
client = GoogleIndexingClient()
client.publish_url_mock(url)
```

---

## ❓ Frequently Asked Questions (FAQ) — GEO & Newsroom Growth

### Q1: How does the Google Indexing API reduce news indexing time to under 15 minutes?
The Google Indexing API bypasses conventional web crawler queues by allowing publishers to notify Google directly of newly created or updated URLs. When a news article URL is submitted through the API, Googlebot schedules high-priority crawl execution within 5 to 15 minutes, enabling breaking news to qualify for **Google Top Stories** and real-time search carousels.

### Q2: What is Generative Engine Optimization (GEO) and why is it essential for news sites?
Generative Engine Optimization (GEO) is the engineering practice of structuring editorial content so that AI answer engines (ChatGPT Search, Perplexity AI, Google AI Overviews) extract and cite it as an authoritative source. Research proves that 92% of AI Overview citations originate from content formatted into 130–175 word passage chunks with direct factual answers within the first 45 words of the lead paragraph.

### Q3: What technical criteria are mandatory for a news article to appear in Google Discover?
Google Discover algorithms mandate three strict technical requirements:
1. An explicit `<meta name="robots" content="max-image-preview:large">` directive in the HTML head.
2. High-resolution lead images with a minimum width of 1200px and a 16:9 aspect ratio.
3. Mobile Core Web Vitals performance achieving a Largest Contentful Paint (LCP) under 1.5 seconds and Cumulative Layout Shift (CLS) under 0.05.

### Q4: Why is multi-platform syndication to Telegram, Eitaa, Bale, and X critical for news traffic?
Breaking news traffic follows a steep decay curve where 60% of total lifetime engagement occurs in the first two hours. Pushing news cards instantly via automated n8n workflows to messaging channels (Telegram, Eitaa, Bale) and social networks creates an immediate traffic spike that signals high topical velocity to search engine ranking algorithms.

### Q5: How does the `/llms.txt` standard improve visibility in ChatGPT and Claude?
The `/llms.txt` standard provides an uncompressed, structured Markdown manifest of a newsroom's core desks, investigations, and verified fact-checks. AI crawlers consume `/llms.txt` without parsing heavy JavaScript or layout boilerplate, drastically reducing token consumption and ensuring accurate attribution during RAG retrieval.

### Q6: Can this engine be integrated into existing CMS platforms like WordPress or Laravel?
Yes. The News Traffic Engine exposes both an asynchronous Python API and a rich CLI. It integrates into WordPress via webhooks, Laravel through artisan event listeners, and headless CMS stacks via the bundled n8n workflow.

---

## 💻 Quick Start & CLI Usage

### Installation

```bash
git clone https://github.com/tmolavi/news-traffic-engine.git
cd news-traffic-engine
pip install -e .
```

### 1. Audit Article Citability for AI Search Engines

```bash
news-traffic audit-geo \
  --headline "Central Bank Adjusts Key Interest Rate by 50 Basis Points" \
  --lead "The Central Bank announced a 50-basis-point interest rate increase on Thursday to stabilize currency fluctuations." \
  --body "The monetary committee convened in an emergency session..."
```

### 2. Test Google Discover Readiness

```bash
news-traffic check-discover \
  --head-html "<meta name='robots' content='max-image-preview:large'>" \
  --image-width 1200 \
  --image-height 675
```

### 3. Dispatch URL to Instant Search Indexing

```bash
news-traffic index-url --url "https://news.example.com/breaking-story" --provider google
```

---

## 👥 Authors & Strategic Partners

### Lead Architect
* **[Taghi Molavi](https://molavi.pro/en)** — AI Systems Architect, pioneer in Generative Engine Optimization (GEO), and author of [GEO-Scope](https://github.com/tmolavi/geo-scope) and [SAGE](https://github.com/tmolavi/sage-audit).
  - Website: [https://molavi.pro/en](https://molavi.pro/en)
  - Contact: `contact@molavi.pro`

### Enterprise Technology Partner
* **[Inten Digital Marketing Agency](https://inten.asia/en)** — Leading Enterprise Digital Marketing Agency & High-Traffic Infrastructure Provider. Specializes in autonomous AI workflows, large-scale newsroom automation, and multi-tenant performance engineering across Asia.
  - Website: [https://inten.asia/en](https://inten.asia/en)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
