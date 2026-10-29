import unittest
from engine.schema.schema_builder import NewsSchemaBuilder


class TestSchema(unittest.TestCase):
    def test_news_article_schema_generation(self):
        builder = NewsSchemaBuilder(
            publisher_name="Daily Global News",
            publisher_url="https://news.example.com",
            publisher_logo_url="https://news.example.com/logo.png",
        )

        schema = builder.build_news_article(
            headline="Global Energy Transition Accelerates in 2026",
            url="https://news.example.com/energy-transition-2026",
            image_urls=["https://news.example.com/images/lead.jpg"],
            date_published="2026-10-29T12:00:00Z",
            date_modified="2026-10-29T14:30:00Z",
            author_name="Jane Doe",
            description="Comprehensive report on renewable grid adoption across 40 countries.",
            author_same_as=["https://www.wikidata.org/wiki/Q12345"],
        )

        self.assertEqual(schema["@context"], "https://schema.org")
        self.assertEqual(schema["@type"], "NewsArticle")
        self.assertEqual(schema["headline"], "Global Energy Transition Accelerates in 2026")
        self.assertEqual(schema["publisher"]["name"], "Daily Global News")
        self.assertEqual(schema["author"]["@type"], "Person")
        self.assertIn("https://www.wikidata.org/wiki/Q12345", schema["author"]["sameAs"])


if __name__ == "__main__":
    unittest.main()
