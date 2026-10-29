"""
IndexNow Protocol Client for Multi-Search Engine Notification.
Instantly notifies Bing, Yandex, Seznam, and partner engines of fresh news items.
"""

from typing import Dict, Any, List
import time

try:
    import httpx
except ImportError:
    httpx = None


class IndexNowClient:
    """Client for IndexNow protocol."""

    API_ENDPOINT = "https://api.indexnow.org/indexnow"

    def __init__(self, host: str, key: str, key_location: str | None = None):
        self.host = host.replace("https://", "").replace("http://", "").strip("/")
        self.key = key
        self.key_location = key_location or f"https://{self.host}/{self.key}.txt"

    def build_payload(self, url_list: List[str]) -> Dict[str, Any]:
        """Generate IndexNow batch notification payload."""
        return {
            "host": self.host,
            "key": self.key,
            "keyLocation": self.key_location,
            "urlList": [u.strip() for u in url_list],
        }

    def submit_mock(self, url_list: List[str]) -> Dict[str, Any]:
        """Simulate IndexNow dispatch offline."""
        payload = self.build_payload(url_list)
        return {
            "status": "success",
            "submitted_count": len(url_list),
            "payload": payload,
            "timestamp": int(time.time()),
            "simulated": True,
        }

    async def submit_async(self, url_list: List[str]) -> Dict[str, Any]:
        """Dispatch URLs to IndexNow API asynchronously."""
        if not httpx:
            return self.submit_mock(url_list)

        payload = self.build_payload(url_list)
        headers = {"Content-Type": "application/json; charset=utf-8"}

        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(self.API_ENDPOINT, json=payload, headers=headers)
            return {
                "status": "success" if resp.status_code in [200, 202] else "error",
                "status_code": resp.status_code,
                "submitted_count": len(url_list),
                "response_text": resp.text,
            }
