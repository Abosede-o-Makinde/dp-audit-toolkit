"""
scorer.py
=========
Compliance scoring engine.

Calculates per-article scores and an overall weighted compliance score.
Weights reflect ICO enforcement priority based on published penalty history.
"""

from collections import defaultdict


# ICO enforcement weights by article
# Based on published ICO enforcement actions 2018-2025
# Higher weight = more frequently enforced = higher score impact
ARTICLE_WEIGHTS = {
    "article_5":  2.5,
    "article_13": 1.5,
    "article_14": 1.5,
    "article_17": 1.5,
    "article_25": 2.0,
    "article_30": 2.0,
    "article_32": 3.0,   # Highest — security failures dominate ICO fines
    "article_33": 2.5,
    "article_34": 1.5,
    "article_35": 1.5,
    "article_37": 1.0,
}

RESPONSE_SCORES = {
    "Y": 100,
    "P": 50,
    "D": 20,
    "N": 0,
    "NA": None
}


class ComplianceScorer:
    """
    Calculates GDPR compliance scores from audit responses.

    Scoring methodology:
    - Each control is scored 0-100 based on the response
    - Article scores are weighted averages of their controls
    - Article scores are then weighted by ICO enforcement priority
    - Overall score = weighted average of all article scores
    """

    def __init__(self, checklist):
        self.checklist = checklist

    def _get_article_key(self, article_str):
        """Extract normalised article key from control article string."""
        # e.g. "Article 32(1)(a)" -> "article_32"
        parts = article_str.lower().split("(")
        number = parts[0].replace("article", "").strip()
        return f"article_{number}"

    def _score_response(self, response, weight):
        """Return weighted score for a single response."""
        score = RESPONSE_SCORES.get(response.upper())
        if score is None:
            return None  # NA — exclude from calculation
        return score * weight

    def calculate_scores(self, responses):
        """
        Calculate compliance scores from a dict of {control_id: response}.

        Returns:
            dict with 'overall' score and 'articles' dict of per-article scores
        """
        controls = self.checklist.get_all_controls()

        # Build article -> list of (score, weight) tuples
        article_data = defaultdict(list)

        for control in controls:
            control_id = control["id"]
            response = responses.get(control_id, "N")
            weight = control["weight"]
            article_key = self._get_article_key(control["article"])

            raw_score = RESPONSE_SCORES.get(response.upper() if response else "N")
            if raw_score is not None:
                article_data[article_key].append((raw_score, weight))

        # Calculate per-article scores
        article_scores = {}
        for article_key, data_points in article_data.items():
            if not data_points:
                continue
            total_weighted = sum(score * w for score, w in data_points)
            total_weight = sum(w for _, w in data_points)
            article_scores[article_key] = round(total_weighted / total_weight)

        # Calculate overall weighted score
        if not article_scores:
            overall = 0
        else:
            weighted_sum = 0
            weight_sum = 0
            for article_key, score in article_scores.items():
                art_weight = ARTICLE_WEIGHTS.get(article_key, 1.0)
                weighted_sum += score * art_weight
                weight_sum += art_weight
            overall = round(weighted_sum / weight_sum) if weight_sum > 0 else 0

        return {
            "overall": overall,
            "articles": article_scores
        }

    def get_rag_rating(self, score):
        """Return RAG status for a given score."""
        if score >= 75:
            return "GREEN"
        elif score >= 50:
            return "AMBER"
        else:
            return "RED"

    def get_score_breakdown(self, responses):
        """Return detailed per-control score breakdown for verbose output."""
        controls = self.checklist.get_all_controls()
        breakdown = []
        for control in controls:
            control_id = control["id"]
            response = responses.get(control_id, "N")
            raw_score = RESPONSE_SCORES.get(response.upper() if response else "N")
            breakdown.append({
                "id": control_id,
                "article": control["article"],
                "domain": control["domain"],
                "question": control["question"][:80] + "..." if len(control["question"]) > 80 else control["question"],
                "response": response,
                "score": raw_score,
                "weight": control["weight"]
            })
        return breakdown