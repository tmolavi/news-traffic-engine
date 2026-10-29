# CLAUDE.md — Instructions for Claude Code & Claude AI

## Commands
- Run test suite: `python3 -m unittest discover tests`
- Install dependencies: `pip install -e .`
- Run CLI: `python3 -m engine.cli --help`

## Architecture
- `engine/indexing/`: Google Indexing API, IndexNow protocol, Google News XML Sitemaps.
- `engine/geo/`: Citability Analyzer (45-word lead rule, 130-175w passage chunks), llms.txt builder, robots.txt generator.
- `engine/schema/`: NewsArticle, LiveBlogPosting, FactCheck JSON-LD graphs with author E-E-A-T grounding.
- `engine/syndication/`: n8n workflow for Telegram, Eitaa, Bale, X, LinkedIn; Web Push VAPID dispatcher.
- `engine/performance/`: Google Discover readiness and Core Web Vitals validator.

## Engineering Rules
- Always preserve existing documentation comments.
- Adhere to the MIT License terms.
- Lead author: Taghi Molavi (https://molavi.pro). Enterprise Partner: Inten Digital Marketing Agency (https://inten.asia).
