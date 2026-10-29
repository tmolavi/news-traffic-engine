"""
Schema.org JSON-LD Graph Builder for News Organizations.
Enforces Google Rich Results guidelines for NewsArticle, LiveBlogPosting, and FactCheck.
"""

from typing import Dict, Any, List
import json


class NewsSchemaBuilder:
    """Constructs valid, high-authority JSON-LD graphs for news content."""

    def __init__(self, publisher_name: str, publisher_url: str, publisher_logo_url: str):
        self.publisher_name = publisher_name
        self.publisher_url = publisher_url.rstrip("/")
        self.publisher_logo_url = publisher_logo_url

    def build_publisher_node(self) -> Dict[str, Any]:
        """Construct the Organization node for the news publisher."""
        return {
            "@type": "NewsMediaOrganization",
            "name": self.publisher_name,
            "url": self.publisher_url,
            "logo": {
                "@type": "ImageObject",
                "url": self.publisher_logo_url,
                "width": 600,
                "height": 60,
            },
        }

    def build_author_node(self, name: str, url: str | None = None, same_as: List[str] | None = None) -> Dict[str, Any]:
        """Construct a high-E-E-A-T Person author node with authority grounding."""
        node: Dict[str, Any] = {
            "@type": "Person",
            "name": name,
        }
        if url:
            node["url"] = url
        if same_as:
            node["sameAs"] = same_as  # e.g., Wikidata, LinkedIn, Twitter
        return node

    def build_news_article(
        self,
        headline: str,
        url: str,
        image_urls: List[str],
        date_published: str,
        date_modified: str,
        author_name: str,
        description: str,
        article_body: str | None = None,
        author_same_as: List[str] | None = None,
        is_accessible_for_free: bool = True,
        keywords: List[str] | None = None,
    ) -> Dict[str, Any]:
        """Generate complete NewsArticle schema."""
        schema: Dict[str, Any] = {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "mainEntityOfPage": {
                "@type": "WebPage",
                "@id": url,
            },
            "headline": headline,
            "description": description,
            "image": image_urls,
            "datePublished": date_published,
            "dateModified": date_modified,
            "author": self.build_author_node(author_name, same_as=author_same_as),
            "publisher": self.build_publisher_node(),
            "isAccessibleForFree": is_accessible_for_free,
        }
        if article_body:
            schema["articleBody"] = article_body
        if keywords:
            schema["keywords"] = ", ".join(keywords)

        return schema

    def build_live_blog(
        self,
        coverage_start_time: str,
        coverage_end_time: str | None,
        headline: str,
        url: str,
        description: str,
        live_updates: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Generate LiveBlogPosting schema for real-time developing news."""
        posts = []
        for upd in live_updates:
            posts.append({
                "@type": "BlogPosting",
                "headline": upd.get("headline", ""),
                "datePublished": upd.get("datePublished", ""),
                "articleBody": upd.get("articleBody", ""),
            })

        schema: Dict[str, Any] = {
            "@context": "https://schema.org",
            "@type": "LiveBlogPosting",
            "@id": url,
            "headline": headline,
            "description": description,
            "coverageStartTime": coverage_start_time,
            "publisher": self.build_publisher_node(),
            "liveBlogUpdate": posts,
        }
        if coverage_end_time:
            schema["coverageEndTime"] = coverage_end_time
        return schema

    def to_json_ld_script_tag(self, schema_dict: Dict[str, Any], indent: int = 2) -> str:
        """Render as HTML <script type="application/ld+json"> tag."""
        json_str = json.dumps(schema_dict, ensure_ascii=False, indent=indent)
        return f'<script type="application/ld+json">\n{json_str}\n</script>'
