import pytest
from src.auditor.checklist import GDPR_CHECKLIST

def test_checklist_structure():
    assert "Article 5" in GDPR_CHECKLIST
    assert "questions" in GDPR_CHECKLIST["Article 5"]