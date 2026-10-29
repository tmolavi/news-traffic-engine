"""
Robots.txt Generator for News Websites in the AI Era.
Balances search crawl budget, allows AI referral bots (ChatGPT Search, Perplexity), and links sitemaps and llms.txt.
"""

from typing import List


class RobotsTxtGenerator:
    """Generates an optimal robots.txt for maximum search and AI visibility."""

    def __init__(self, domain: str):
        self.domain = domain.rstrip("/")

    def generate(self, disallow_paths: List[str] | None = None) -> str:
        disallows = disallow_paths or ["/admin/", "/cdn-cgi/", "/api/internal/"]
        disallow_block = "\n".join([f"Disallow: {p}" for p in disallows])

        content = f"""# ==============================================================================
# Robots.txt for {self.domain}
# Optimized for Google News, Google Discover, and Generative Engine Optimization (GEO)
# ==============================================================================

# 1. Universal Search Crawlers (Google, Bing, Yahoo, Yandex)
User-agent: *
Allow: /
{disallow_block}

# 2. AI Search & Answer Referral Crawlers (Explicitly Allowed for Citations)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

# 3. Dedicated Sitemaps & Machine-Readable Manifests
Sitemap: {self.domain}/sitemap.xml
Sitemap: {self.domain}/news-sitemap.xml

# 4. LLM & Machine Discovery Manifest
# See https://llmstxt.org
# llms-txt: {self.domain}/llms.txt
"""
        return content.strip() + "\n"
