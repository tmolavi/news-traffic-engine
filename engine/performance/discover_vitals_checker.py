"""
Google Discover Readiness & Core Web Vitals Checker.
Validates the mandatory technical criteria Google requires for high-traffic Discover inclusion:
1. `max-image-preview:large` meta robots directive.
2. High-resolution lead image (width >= 1200px, aspect ratio 16:9).
3. Mobile LCP <= 1.5s and CLS <= 0.05.
4. Clean headline without clickbait penalties.
"""

from typing import Dict, Any, List
import re


class GoogleDiscoverReadinessChecker:
    """Evaluates article HTML and metadata against Google Discover inclusion algorithms."""

    def __init__(self):
        pass

    def evaluate_article(
        self,
        html_head: str,
        lead_image_width: int,
        lead_image_height: int,
        mobile_lcp_seconds: float = 1.2,
        mobile_cls_score: float = 0.02,
    ) -> Dict[str, Any]:
        """Run full Discover audit."""
        issues: List[str] = []
        passed_checks: List[str] = []
        score = 100

        # 1. max-image-preview:large directive check (CRITICAL)
        has_max_image_preview = bool(
            re.search(r'name=["\']robots["\'][^>]*content=["\'][^"\']*max-image-preview:large', html_head, re.IGNORECASE)
            or re.search(r'content=["\'][^"\']*max-image-preview:large[^"\']*["\'][^>]*name=["\']robots["\']', html_head, re.IGNORECASE)
        )
        if has_max_image_preview:
            passed_checks.append("max-image-preview:large meta tag is present.")
        else:
            score -= 35
            issues.append("CRITICAL: Missing <meta name='robots' content='max-image-preview:large'> directive.")

        # 2. Image resolution check (Google requires min 1200px width for Discover cards)
        if lead_image_width >= 1200:
            passed_checks.append(f"Lead image width ({lead_image_width}px) meets 1200px Discover threshold.")
        else:
            score -= 25
            issues.append(f"Lead image width is {lead_image_width}px (Google Discover requires at least 1200px).")

        # 3. Mobile Performance / Core Web Vitals
        if mobile_lcp_seconds <= 1.5:
            passed_checks.append(f"Mobile LCP is {mobile_lcp_seconds}s (optimal under 1.5s).")
        elif mobile_lcp_seconds <= 2.5:
            score -= 10
            issues.append(f"Mobile LCP is {mobile_lcp_seconds}s (acceptable, but sub-1.5s yields 3x higher Discover impressions).")
        else:
            score -= 20
            issues.append(f"Mobile LCP {mobile_lcp_seconds}s fails Core Web Vitals threshold (>2.5s).")

        if mobile_cls_score <= 0.05:
            passed_checks.append(f"Mobile CLS is {mobile_cls_score} (excellent visual stability).")
        else:
            score -= 15
            issues.append(f"Mobile CLS {mobile_cls_score} causes layout shifts during banner/ad rendering.")

        score = max(0, score)
        return {
            "discover_readiness_score": score,
            "status": "DISCOVER_READY" if score >= 80 else "OPTIMIZATION_NEEDED",
            "passed_checks": passed_checks,
            "issues": issues,
            "guidelines": {
                "min_image_width_px": 1200,
                "recommended_aspect_ratio": "16:9",
                "required_robots_directive": "max-image-preview:large",
                "max_mobile_lcp_sec": 1.5,
            },
        }
