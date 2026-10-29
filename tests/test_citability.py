import unittest
from engine.geo.citability_analyzer import NewsCitabilityAnalyzer


class TestCitability(unittest.TestCase):
    def test_citability_score_calculation(self):
        analyzer = NewsCitabilityAnalyzer()
        headline = "Space Agency Launches Next-Gen Climate Satellite from Cape Canaveral"
        lead = "Cape Canaveral, Oct 29 — The Space Agency successfully launched its 12th environmental observation satellite on Thursday, expanding global climate tracking capabilities by 35% across all oceans."
        body = (
            "The mission lifted off at 09:00 UTC under optimal atmospheric telemetry conditions from Pad 39A. "
            "Engineers and astrophysicists reported complete nominal stage separation approximately eight minutes into flight. "
            "\"This launch marks an indispensable step forward in planetary telemetry and climate preservation,\" said project director Dr. Sarah Vance. "
            "The onboard multispectral sensors are engineered to monitor micro-particulate shifts across 150 critical atmospheric regions with unprecedented radiometric precision.\n\n"
            "Secondary payload telemetry confirmed solar array deployment at 09:47 UTC with optimal power efficiency. "
            "Total capital investment for the initiative reached $250 million, funded through a multi-national consortium. "
            "\"We expect initial calibrated data streams to reach international meteorological centers within 72 hours,\" added chief engineer Marcus Reed. "
            "The spacecraft will maintain a sun-synchronous low Earth orbit for the next seven years."
        )

        res = analyzer.analyze(headline=headline, lead_paragraph=lead, body_text=body)
        self.assertGreaterEqual(res["citability_score"], 60)
        self.assertGreaterEqual(res["metrics"]["quotes_detected"], 1)
        self.assertGreaterEqual(res["metrics"]["data_points_detected"], 1)


if __name__ == "__main__":
    unittest.main()
