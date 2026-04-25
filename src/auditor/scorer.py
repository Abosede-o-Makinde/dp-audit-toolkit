# Scoring engine (per-article + overall)

from .checklist import GDPR_CHECKLIST

def calculate_article_score(article, responses):
    questions = GDPR_CHECKLIST[article]["questions"]
    total_questions = len(questions)
    yes_count = sum(1 for resp in responses if resp.lower() == 'yes')
    score = (yes_count / total_questions) * 100
    return round(score)

def calculate_overall_score(scores):
    return round(sum(scores.values()) / len(scores))

def get_score_color(score):
    if score >= 80:
        return "GREEN"
    elif score >= 60:
        return "AMBER"
    else:
        return "RED"