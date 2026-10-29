import unittest
from datetime import datetime, timezone
from engine.indexing.sitemap_generator import GoogleNewsSitemapBuilder


class TestSitemap(unittest.TestCase):
    def test_google_news_sitemap_xml(self):
        builder = GoogleNewsSitemapBuilder(publisher_name="Tech Dispatch", language="en")
        now_iso = datetime.now(timezone.utc).isoformat()

        articles = [
            {
                "url": "https://dispatch.example.com/ai-breakthrough",
                "title": "Quantum Hybrid AI System Breakthrough Announced",
                "publication_date": now_iso,
                "language": "en",
            }
        ]

        xml_output = builder.generate_xml(articles)
        self.assertIn("<urlset", xml_output)
        self.assertIn("xmlns:news=\"http://www.google.com/schemas/sitemap-news/0.9\"", xml_output)
        self.assertIn("<news:title>Quantum Hybrid AI System Breakthrough Announced</news:title>", xml_output)
        self.assertIn("<news:name>Tech Dispatch</news:name>", xml_output)


if __name__ == "__main__":
    unittest.main()
