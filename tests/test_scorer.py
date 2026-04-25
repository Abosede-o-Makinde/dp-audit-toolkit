import pytest
from src.auditor.scorer import calculate_article_score, calculate_overall_score

def test_calculate_article_score():
    responses = ["yes", "no", "yes", "yes", "no", "yes"]  # 6 responses for Article 5
    score = calculate_article_score("Article 5", responses)
    assert score == 67  # 4/6 * 100 rounded

def test_calculate_overall_score():
    scores = {"A": 50, "B": 100}
    overall = calculate_overall_score(scores)
    assert overall == 75