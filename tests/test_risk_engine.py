import pytest
from src.auditor.risk_engine import assess_risks

def test_assess_risks():
    scores = {"A": 40, "B": 65, "C": 85}
    risks = assess_risks(scores)
    assert risks["critical_gaps"] == 1
    assert risks["high_risks"] == 1
    assert risks["ico_enforcement_risk"] == "ELEVATED"