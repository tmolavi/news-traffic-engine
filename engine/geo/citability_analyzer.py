"""
News Citability Analyzer for Generative Search Engines (GEO).
Empirically assesses whether news copy will be cited by ChatGPT Search, Perplexity, and Google AI Overviews.
Based on research from GEO-Scope, SAGE, and SparkToro AI Referral Benchmarks.
"""

from typing import Dict, Any, List
import re


class NewsCitabilityAnalyzer:
    """Analyzes news article copy for passage citability, inverted-pyramid density, and RAG extractability."""

    OPTIMAL_PASSAGE_MIN = 130
    OPTIMAL_PASSAGE_MAX = 175
    OPTIMAL_LEAD_WORDS = 50

    def __init__(self):
        pass

    def tokenize_words(self, text: str) -> List[str]:
        """Unicode-aware word tokenization supporting English, Persian, Arabic, Turkish, Spanish."""
        return [w for w in re.split(r"[\s\.,;:!?\(\)\[\]\"'«»—]+", text) if w]

    def extract_passages(self, body_text: str) -> List[str]:
        """Split body into structural passages / paragraphs."""
        raw_paras = body_text.split("\n")
        passages = [p.strip() for p in raw_paras if len(p.strip()) > 30]
        return passages

    def analyze(self, headline: str, lead_paragraph: str, body_text: str) -> Dict[str, Any]:
        """
        Evaluate full news piece and return Citability Score (0-100) and actionable diagnosis.
        """
        lead_words = self.tokenize_words(lead_paragraph)
        lead_word_count = len(lead_words)

        # 1. Direct Answer in Lead (30%)
        # Check if the lead answers What/Who/When directly within first 40-50 words
        lead_score = 0
        if 25 <= lead_word_count <= 65:
            lead_score = 30
        elif lead_word_count < 25:
            lead_score = 15  # Too brief, lacks factual meat
        else:
            lead_score = 18  # Buried answer, AI crawler may truncate

        # Check for numbers/dates/statistics in lead
        has_stats = bool(re.search(r"\d+", lead_paragraph))
        if has_stats:
            lead_score = min(30, lead_score + 5)

        # 2. Passage Chunk Optimization (30%)
        passages = self.extract_passages(body_text)
        passage_scores = []
        for p in passages:
            wc = len(self.tokenize_words(p))
            if self.OPTIMAL_PASSAGE_MIN <= wc <= self.OPTIMAL_PASSAGE_MAX:
                passage_scores.append(1.0)
            elif 80 <= wc <= 220:
                passage_scores.append(0.7)
            else:
                passage_scores.append(0.4)

        avg_passage_score = (sum(passage_scores) / len(passage_scores)) if passage_scores else 0.5
        chunk_score = round(avg_passage_score * 30, 1)

        # 3. Attribution & Quotation Density (20%)
        # AI engines strongly favor direct quotes from named authorities
        quotes = re.findall(r'["«][^"»]+["»]', body_text)
        quote_score = min(20, len(quotes) * 5)

        # 4. Data Point Density (20%)
        # Specific metrics, percentages, numbers
        data_points = re.findall(r"\b\d+([,\.]\d+)?(%|\$|€|£|٪)?\b", body_text)
        data_score = min(20, len(data_points) * 2.5)

        total_score = round(lead_score + chunk_score + quote_score + data_score, 1)

        # Actionable recommendations
        recommendations = []
        if lead_word_count > 60:
            recommendations.append("Lead paragraph is too long. Keep the primary factual answer within the first 45 words.")
        if not has_stats:
            recommendations.append("Add verified data points, dates, or specific numbers to the lead section.")
        if len(quotes) < 2:
            recommendations.append("Include at least 2 direct quotes with explicit source attribution (e.g. 'said minister...').")
        if avg_passage_score < 0.7:
            recommendations.append(f"Passage lengths vary wildly. Target {self.OPTIMAL_PASSAGE_MIN}-{self.OPTIMAL_PASSAGE_MAX} words per paragraph for optimal RAG chunking.")

        return {
            "citability_score": total_score,
            "grade": "A+" if total_score >= 85 else "A" if total_score >= 70 else "B" if total_score >= 50 else "C",
            "breakdown": {
                "lead_direct_answer": lead_score,
                "passage_chunk_quality": chunk_score,
                "attribution_quotes": quote_score,
                "data_point_density": data_score,
            },
            "metrics": {
                "lead_word_count": lead_word_count,
                "passage_count": len(passages),
                "quotes_detected": len(quotes),
                "data_points_detected": len(data_points),
            },
            "recommendations": recommendations,
        }
