import unittest
from engine.indexing.google_indexing import GoogleIndexingClient
from engine.indexing.indexnow import IndexNowClient


class TestIndexing(unittest.TestCase):
    def test_google_indexing_payload(self):
        client = GoogleIndexingClient()
        payload = client.prepare_payload("https://news.example.com/breaking-event")
        self.assertEqual(payload["url"], "https://news.example.com/breaking-event")
        self.assertEqual(payload["type"], "URL_UPDATED")

    def test_indexnow_payload(self):
        client = IndexNowClient(host="news.example.com", key="sample_key_123")
        payload = client.build_payload(["https://news.example.com/news-1", "https://news.example.com/news-2"])
        self.assertEqual(payload["host"], "news.example.com")
        self.assertEqual(payload["key"], "sample_key_123")
        self.assertEqual(len(payload["urlList"]), 2)


if __name__ == "__main__":
    unittest.main()
