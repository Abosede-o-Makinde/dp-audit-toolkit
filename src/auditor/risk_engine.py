# Risk rating and gap classification

def assess_risks(scores):
    critical_gaps = []
    high_risks = []
    for article, score in scores.items():
        if score < 50:
            critical_gaps.append(article)
        elif score < 70:
            high_risks.append(article)
    ico_risk = "ELEVATED" if len(critical_gaps) > 0 else "MODERATE"
    return {
        "critical_gaps": len(critical_gaps),
        "high_risks": len(high_risks),
        "ico_enforcement_risk": ico_risk
    }