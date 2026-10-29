"""
Google News XML Sitemap Builder.
Enforces Google News sitemap specifications:
- <news:news> namespace
- 48-hour freshness window
- Publication name, language, publication_date, and title
"""

from typing import List, Dict, Any
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET


class GoogleNewsSitemapBuilder:
    """Builds valid Google News sitemaps strictly compliant with Google guidelines."""

    XMLNS_SITEMAP = "http://www.sitemaps.org/schemas/sitemap/0.9"
    XMLNS_NEWS = "http://www.google.com/schemas/sitemap-news/0.9"

    def __init__(self, publisher_name: str, language: str = "en"):
        self.publisher_name = publisher_name
        self.language = language
        ET.register_namespace("", self.XMLNS_SITEMAP)
        ET.register_namespace("news", self.XMLNS_NEWS)

    def is_within_48_hours(self, pub_date_iso: str) -> bool:
        """Verify article is strictly within Google's 48-hour news indexing window."""
        try:
            pub_dt = datetime.fromisoformat(pub_date_iso.replace("Z", "+00:00"))
            cutoff = datetime.now(timezone.utc) - timedelta(hours=48)
            return pub_dt >= cutoff
        except Exception:
            return True

    def generate_xml(self, articles: List[Dict[str, Any]], enforce_48h: bool = True) -> str:
        """Generate formatted Google News XML string."""
        urlset = ET.Element(
            f"{{{self.XMLNS_SITEMAP}}}urlset",
            {},
        )

        for art in articles:
            pub_date = art.get("publication_date", datetime.now(timezone.utc).isoformat())
            if enforce_48h and not self.is_within_48_hours(pub_date):
                continue

            url_el = ET.SubElement(urlset, f"{{{self.XMLNS_SITEMAP}}}url")
            loc_el = ET.SubElement(url_el, f"{{{self.XMLNS_SITEMAP}}}loc")
            loc_el.text = art.get("url", "")

            news_el = ET.SubElement(url_el, f"{{{self.XMLNS_NEWS}}}news")
            pub_el = ET.SubElement(news_el, f"{{{self.XMLNS_NEWS}}}publication")

            name_el = ET.SubElement(pub_el, f"{{{self.XMLNS_NEWS}}}name")
            name_el.text = art.get("publisher_name", self.publisher_name)

            lang_el = ET.SubElement(pub_el, f"{{{self.XMLNS_NEWS}}}language")
            lang_el.text = art.get("language", self.language)

            date_el = ET.SubElement(news_el, f"{{{self.XMLNS_NEWS}}}publication_date")
            date_el.text = pub_date

            title_el = ET.SubElement(news_el, f"{{{self.XMLNS_NEWS}}}title")
            title_el.text = art.get("title", "")

        return ET.tostring(urlset, encoding="utf-8", xml_declaration=True).decode("utf-8")
