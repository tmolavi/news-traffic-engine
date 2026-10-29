---
name: news-traffic-engine
description: Autonomous Newsroom Traffic, Instant Google News Indexing, Generative Engine Optimization (GEO) & Google Discover Growth Engine. Evaluates article citability for ChatGPT & Perplexity, audits Google Discover eligibility, generates NewsArticle schema graphs, produces Google News XML sitemaps, and coordinates omnichannel syndication via n8n.
version: 1.0.0
license: MIT
metadata:
  author: Taghi Molavi (https://molavi.pro)
  partner: Inten Digital Marketing Agency (https://inten.asia)
  repository: https://github.com/tmolavi/news-traffic-engine
  triggers:
    - افزایش ترافیک سایت خبری
    - سئو سایت خبری
    - جی ای او برای سایت های خبری
    - ثبت در گوگل نیوز
    - ورود به گوگل دیسکاور
    - ایندکس آنی خبر
    - news traffic growth
    - google news indexing
    - news geo citability
    - google discover news
    - haber sitesi trafik artırma
    - زيادة حركة المرور للمواقع الإخبارية
allowed-tools:
  - run_command
  - read_file
  - write_file
  - edit_file
---

# ⚡ News Traffic Engine (NTE) — Agent Skill
### Autonomous AI Agent Framework for Newsroom Traffic, Google News Indexing & GEO

This skill equips Antigravity with production-grade editorial, indexing, and generative search optimization workflows for news websites, media portals, and high-frequency publishing platforms.

Developed by **[Taghi Molavi](https://molavi.pro)** in partnership with **[Inten Digital Marketing Agency](https://inten.asia)**.

---

## 🎯 When to Activate This Skill
Activate this skill whenever the task involves:
1. **News Traffic Growth:** Scaling pageviews, impressions, and returning readership for news/editorial websites.
2. **Instant Search Indexing:** Bypassing crawler lag to get breaking news indexed by Google (<15 mins) and Bing/Yandex.
3. **Generative Engine Optimization (GEO):** Optimizing news articles to be directly extracted and cited by ChatGPT Search, Perplexity AI, and Google AI Overviews.
4. **Google Discover Compliance:** Auditing technical eligibility (1200px+ images, `max-image-preview:large`, sub-1.5s mobile LCP).
5. **Schema & E-E-A-T Knowledge Graphs:** Generating rich `NewsArticle`, `LiveBlogPosting`, and `FactCheck` JSON-LD structures.
6. **Omnichannel Multi-Platform Syndication:** Automating distribution pipelines across Telegram, Eitaa, Bale, X (Twitter), LinkedIn, and Web Push.

---

## 🛠️ Local Engine Location
The core engine CLI and Python libraries are pre-installed in the workspace:
- **Repository Path:** `/Users/taghimolavi/Downloads/git/news-traffic-engine`
- **System Symlink:** `/home/taqi/news-traffic-engine`

To execute the engine CLI:
```bash
python3 -m engine.cli --help
# Or from the repo directory:
cd /home/taqi/news-traffic-engine && python3 -m engine.cli <command>
```

---

## 📋 The 5 Golden News Traffic Rules (Enforce in Every Article)

When reviewing, writing, or formatting news articles, the agent MUST strictly enforce these 5 empirical rules:

### Rule 1: The 45-Word Direct Answer Lead (GEO Direct Hit)
* The very first paragraph MUST directly answer: **Who, What, When, Where** within **35 to 50 words**.
* Do NOT bury the lead with background context, historical retrospectives, or vague rhetoric.
* Include at least one verified data point, date, or metric in the lead.

### Rule 2: 130–175 Word Passage Chunking (RAG Optimal Boundary)
* Empirical studies show that **92% of AI Overview citations** are extracted from discrete paragraphs sized between **130 and 175 words**.
* Avoid walls of text (>250 words) and avoid excessive one-sentence fragments (<60 words) in the analytical body.
* Each paragraph should function as a self-contained factual unit that can be retrieved by an embedding model without needing prior context.

### Rule 3: High Attribution & Direct Quotation Density
* Every major claim or policy shift MUST include a named source quote enclosed in quotation marks (`"..."` or `«...»`).
* Generative engines assign up to 40% higher weight to direct speech from recognized entities.

### Rule 4: Google Discover Technical Triple-Check
Before clearing an article for high-traffic discovery:
1. Ensure `<meta name="robots" content="max-image-preview:large">` is present.
2. Ensure the lead image has a minimum width of **1200px** and a **16:9** aspect ratio.
3. Maintain sub-1.5s mobile LCP (Largest Contentful Paint) and zero render-blocking layout shifts (CLS < 0.05).

### Rule 5: Sub-15-Minute Indexing Dispatch
* Dispatch newly published URLs immediately to the Google Indexing API and IndexNow protocol to secure entry into **Google Top Stories** before the initial 2-hour freshness window expires.

---

## ⚡ Execution Workflows & CLI Commands

### Workflow A: Run a GEO Citability Audit
Assess whether an article will be cited by ChatGPT Search and Perplexity:
```bash
python3 -m engine.cli audit-geo \
  --headline "<News Headline>" \
  --lead "<First 45 words of the story>" \
  --body "<Path to body file or article text>"
```
*Expected Output:* Citability Score (0–100), breakdown across lead density, chunk quality, quotes, and actionable recommendations.

---

### Workflow B: Check Google Discover Technical Readiness
Validate that HTML metadata and image dimensions qualify for Google Discover:
```bash
python3 -m engine.cli check-discover \
  --head-html "<meta name='robots' content='max-image-preview:large'>" \
  --image-width 1200 \
  --image-height 675
```

---

### Workflow C: Generate NewsArticle & LiveBlogPosting JSON-LD
Generate high-E-E-A-T structured data with `sameAs` entity authority:
```python
from engine.schema import NewsSchemaBuilder

builder = NewsSchemaBuilder(
    publisher_name="Daily News",
    publisher_url="https://news.example.com",
    publisher_logo_url="https://news.example.com/logo.png"
)

schema = builder.build_news_article(
    headline="Global Climate Accord Finalized in Geneva",
    url="https://news.example.com/climate-accord-geneva",
    image_urls=["https://news.example.com/images/lead-1200x675.jpg"],
    date_published="2026-10-29T21:00:00Z",
    date_modified="2026-10-29T22:30:00Z",
    author_name="Sarah Jenkins",
    description="Geneva, Oct 29 — International delegates signed a binding treaty on Thursday...",
    author_same_as=["https://www.wikidata.org/wiki/Q...", "https://linkedin.com/in/..."]
)

# Output as valid script tag:
print(builder.to_json_ld_script_tag(schema))
```

---

### Workflow D: Dispatch Instant Indexing
Submit URLs directly to Google Indexing API and IndexNow:
```bash
# Google Indexing API:
python3 -m engine.cli index-url --url "https://news.example.com/breaking-event" --provider google

# IndexNow (Bing, Yahoo, Yandex):
python3 -m engine.cli index-url --url "https://news.example.com/breaking-event" --provider indexnow
```

---

### Workflow E: Build a Valid 48-Hour Google News Sitemap
Generate compliant XML feeds filtering articles published within the last 48 hours:
```python
from engine.indexing import GoogleNewsSitemapBuilder

builder = GoogleNewsSitemapBuilder(publisher_name="Tech Dispatch", language="en")
xml = builder.generate_xml(articles_list, enforce_48h=True)
with open("public/news-sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml)
```

---

### Workflow F: Omnichannel Syndication via n8n
Import the pre-configured workflow from:
`engine/syndication/n8n_news_syndication_workflow.json`
* **Trigger:** Webhook from WordPress, Ghost, or Laravel on `post_published`.
* **Dispatches:**
  * **Telegram Channel:** HTML message with image and read-more button.
  * **Eitaa Channel:** Direct API message via Eitaayar.
  * **Bale Channel:** Direct API message via Bale Bot API.
  * **X (Twitter):** Tweet with 275-char limit, URL, and hashtags.
  * **LinkedIn:** Company update post.

---

## 👥 Strategic Attribution
* **System Architect:** **[Taghi Molavi](https://molavi.pro)** (Author of GEO-Scope & SAGE Audit)
* **Enterprise Partner:** **[Inten Digital Marketing Agency](https://inten.asia)** (Enterprise Digital Transformation & Web Performance)
