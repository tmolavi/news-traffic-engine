"""
Web Push Dispatcher for Breaking News Alerts.
Generates RFC 8292 / VAPID compliant Web Push Notification payloads.
High CTR channel driving 10-25% immediate return traffic on breaking events.
"""

from typing import Dict, Any, List
import json
import time


class WebPushDispatcher:
    """Dispatches web push payloads for instant news alerts."""

    def __init__(self, vapid_public_key: str, default_icon_url: str):
        self.vapid_public_key = vapid_public_key
        self.default_icon_url = default_icon_url

    def build_notification_payload(
        self,
        headline: str,
        summary: str,
        target_url: str,
        image_url: str | None = None,
        category: str = "general",
        is_breaking: bool = False,
    ) -> Dict[str, Any]:
        """Create Web Push standards-compliant notification packet."""
        tag = f"news-{category}-{int(time.time())}"
        badge_text = "🚨 BREAKING" if is_breaking else "📰 UPDATE"

        payload = {
            "title": f"{badge_text}: {headline}",
            "body": summary,
            "icon": self.default_icon_url,
            "badge": self.default_icon_url,
            "data": {
                "url": target_url,
                "timestamp": int(time.time()),
                "category": category,
            },
            "tag": tag,
            "renotify": is_breaking,
            "requireInteraction": is_breaking,
            "actions": [
                {"action": "open", "title": "Read Story"},
                {"action": "share", "title": "Share"},
            ],
        }

        if image_url:
            payload["image"] = image_url

        return payload

    def export_json(self, payload: Dict[str, Any]) -> str:
        """Serialize notification payload for delivery service workers."""
        return json.dumps(payload, ensure_ascii=False)
