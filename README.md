# ⚡ News Traffic Engine (NTE)
### Autonomous AI Agent Framework for Newsroom Traffic, Instant Google News Indexing, Generative Engine Optimization (GEO) & Google Discover Growth

[![CI](https://github.com/tmolavi/news-traffic-engine/actions/workflows/ci.yml/badge.svg)](https://github.com/tmolavi/news-traffic-engine/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![GEO Ready](https://img.shields.io/badge/GEO-ChatGPT%20%7C%20Perplexity%20%7C%20AI%20Overviews-brightgreen)](https://github.com/tmolavi/news-traffic-engine)

> **Languages:** [English](README.md) · [فارسی](README.fa.md) · [العربية](README.ar.md) · [Türkçe](README.tr.md) · [Español](README.es.md)

---

## 📌 Executive Summary

The **News Traffic Engine (NTE)** is a production-grade, open-source AI agent system designed for newsrooms, digital journalists, and high-volume media publishers operating in the AI-search era. 

While legacy news SEO focused exclusively on keyword placement and traditional SERP rankings, modern news traffic depends on three critical pillars:
1. **Sub-15-Minute Search Indexing:** Direct API submission to Google Indexing API and IndexNow protocol to secure placements in **Google News** and **Top Stories** while events are unfolding.
2. **Generative Engine Optimization (GEO):** Structuring editorial copy into modular, fact-dense passage chunks (130–175 words) with immediate answers in the first 45 words, guaranteeing citations in **ChatGPT Search**, **Perplexity AI**, and **Google AI Overviews**.
3. **Omnichannel Viral Distribution & Web Push:** Instantaneous multi-platform syndication via [n8n](https://n8n.io) to Telegram, Eitaa, Bale, X (Twitter), LinkedIn, paired with VAPID Web Push alerts that re-engage returning audiences with 10–25% CTR.

Created by **[Taghi Molavi](https://molavi.pro)** (AI Architect & Creator of [GEO-Scope](https://github.com/tmolavi/geo-scope) and [SAGE](https://github.com/tmolavi/sage-audit)) in strategic collaboration with **[Inten](https://inten.asia)** (Enterprise Digital Transformation & High-Traffic Infrastructure Leader).

---

## 🏗️ Architecture Overview

```
+-----------------------------------------------------------------------------------+
|                            NEWS TRAFFIC ENGINE (NTE)                              |
+-----------------------------------------------------------------------------------+
        |                                   |                                   |
        v                                   v                                   v
[ 1. INSTANT DISCOVERY ]            [ 2. GEO & CITABILITY ]             [ 3. SYNDICATION ]
- Google Indexing API               - 40-Word Direct Answer Lead        - n8n Omnichannel Flow
- IndexNow Batch Protocol           - 130-175 Word Passage Chunker      - Telegram / Eitaa / Bale
- Google News XML Sitemap           - llms.txt & llms-full.txt          - X / LinkedIn / Web Push
- Robots.txt AI Bot Policies        - NewsArticle JSON-LD Graph         - Discover Vitals Audit
        |                                   |                                   |
        +-----------------------------------+-----------------------------------+
                                            |
                                            v
                    [ RESULT: 3X-5X COMPOUND TRAFFIC SURGE ]
               Google News · Google Discover · Perplexity · ChatGPT
```

---

## 🚀 Key Modules & Capabilities

### 1. Instant Search Indexing (`engine.indexing`)
- **Google Indexing API Client:** Eliminates crawler delays by dispatching fresh article URLs straight into Google's batch indexing pipeline for inclusion in under 15 minutes.
- **IndexNow Engine:** Broadcasts instant publish notifications to Microsoft Bing, Yahoo, Yandex, and Seznam.
- **Google News XML Sitemap Builder:** Automatically generates compliant XML feeds filtering articles strictly within the 48-hour freshness window with `<news:news>` namespace elements.

### 2. Generative Engine Optimization (`engine.geo`)
- **News Citability Analyzer:** Evaluates article text against empirical citation patterns, grading lead-answer clarity, quote density, numerical data points, and passage boundary quality (0–100 Citability Score).
- **`/llms.txt` & RAG Generator:** Creates clean Markdown summaries and structured chunks for LLM consumption.
- **Robots.txt Engine:** Grants crawl permission to legitimate AI answer engines (`GPTBot`, `PerplexityBot`, `ClaudeBot`, `Applebot-Extended`) while protecting proprietary feeds.
- **Interoperability Bridge:** Connects seamlessly with [GEO-Scope](https://github.com/tmolavi/geo-scope) and [SAGE Audit](https://github.com/tmolavi/sage-audit).

### 3. Structured Data & E-E-A-T (`engine.schema`)
- **NewsArticle & LiveBlogPosting JSON-LD:** Constructs Google-compliant graphs with authoritative author grounding (`sameAs` links to Wikidata, Wikipedia, LinkedIn).
- **AnalysisNewsArticle & FactCheck:** Rich snippet generation for analytical and fact-checking desks.

### 4. Omnichannel Syndication & Audience Retention (`engine.syndication`)
- **n8n Production Workflow (`n8n_news_syndication_workflow.json`):** Plug-and-play workflow receiving CMS webhooks and broadcasting formatted news cards with rich media to Telegram, Eitaa, Bale, X (Twitter), and LinkedIn.
- **Web Push Dispatcher:** Standards-compliant VAPID payload generator for breaking news browser alerts.

### 5. Google Discover Readiness (`engine.performance`)
- **Discover Vitals Checker:** Enforces `max-image-preview:large`, validates 1200px+ lead images, and verifies mobile Core Web Vitals (LCP < 1.5s, CLS < 0.05).

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

## 🧪 Running the Test Suite

```bash
python3 -m unittest discover tests
```

---

## 👥 Authors & Strategic Partners

### Lead Architect
* **[Taghi Molavi](https://molavi.pro)** — AI Systems Architect, pioneer in Generative Engine Optimization (GEO), and author of [GEO-Scope](https://github.com/tmolavi/geo-scope) and [SAGE](https://github.com/tmolavi/sage-audit).
  - Website: [https://molavi.pro](https://molavi.pro)
  - Contact: `contact@molavi.pro`

### Enterprise Technology Partner
* **[Inten](https://inten.asia)** — Leading Enterprise Digital Transformation & High-Traffic Infrastructure Provider. Specializes in autonomous AI workflows, large-scale newsroom automation, and multi-tenant performance engineering across Asia.
  - Website: [https://inten.asia](https://inten.asia)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
