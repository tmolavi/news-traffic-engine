"""
Builder for /llms.txt and /llms-full.txt standards.
Provides structured, low-noise Markdown interfaces for LLMs and AI crawlers.
"""

from typing import List, Dict, Any
from datetime import datetime, timezone


class LlmsTxtBuilder:
    """Generates standardized llms.txt and curated news topic files."""

    def __init__(self, newsroom_name: str, domain: str, mission: str):
        self.newsroom_name = newsroom_name
        self.domain = domain.rstrip("/")
        self.mission = mission

    def build_llms_txt(self, top_stories: List[Dict[str, Any]], categories: List[str]) -> str:
        """Generate standard /llms.txt manifest."""
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        lines = [
            f"# {self.newsroom_name}",
            f"> {self.mission}",
            "",
            f"- Domain: {self.domain}",
            f"- Last Updated: {now}",
            "- License: Editorial News Content",
            "",
            "## Core News Desks",
        ]

        for cat in categories:
            slug = cat.lower().replace(" ", "-")
            lines.append(f"- [{cat}]({self.domain}/desk/{slug}): Real-time coverage and investigations.")

        lines.extend([
            "",
            "## Top Developing Stories & Investigations",
        ])

        for story in top_stories:
            title = story.get("title", "")
            url = story.get("url", "")
            summary = story.get("summary", "")
            lines.append(f"- [{title}]({url}): {summary}")

        lines.extend([
            "",
            "## AI & Machine Readability Resources",
            f"- [Full LLMs Manifest]({self.domain}/llms-full.txt): Complete uncompressed textual coverage.",
            f"- [Google News Sitemap]({self.domain}/news-sitemap.xml): Fresh 48-hour article registry.",
            f"- [Fact-Check Feed]({self.domain}/fact-checks.json): Verified claim ratings.",
        ])

        return "\n".join(lines)
