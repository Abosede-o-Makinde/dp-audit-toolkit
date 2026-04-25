"""
risk_engine.py
==============
Risk classification and gap analysis engine.

Classifies gaps as CRITICAL / HIGH / MEDIUM / LOW and
assesses overall ICO enforcement risk based on the audit results.
"""

# Controls that — if failed — represent the highest ICO enforcement risk
CRITICAL_CONTROL_IDS = {
    "A5-01", "A5-06", "A5-07",
    "A25-01",
    "A30-01",
    "A32-01", "A32-02", "A32-03", "A32-04",
    "A33-01", "A33-02"
}

# Article scores below which enforcement risk is elevated
ENFORCEMENT_THRESHOLDS = {
    "article_32": 60,  # Security — most heavily penalised
    "article_33": 60,  # Breach notification
    "article_5":  60,  # Principles
    "article_25": 50,  # Privacy by design
    "article_30": 50,  # Records
}


class RiskEngine:
    """
    Assesses risk from audit scores and responses.

    Produces:
    - List of critical gaps (highest priority remediation)
    - List of high risks
    - Overall ICO enforcement risk rating
    - Prioritised recommendations
    """

    def assess(self, scores, responses):
        """
        Run the full risk assessment.

        Args:
            scores:    output of ComplianceScorer.calculate_scores()
            responses: dict of {control_id: response}

        Returns:
            dict with critical_gaps, high_risks, enforcement_risk, recommendations
        """
        critical_gaps = self._find_critical_gaps(responses)
        high_risks = self._find_high_risks(responses)
        enforcement_risk = self._assess_enforcement_risk(scores, critical_gaps)
        recommendations = self._generate_recommendations(critical_gaps, high_risks, scores)

        return {
            "critical_gaps": critical_gaps,
            "high_risks": high_risks,
            "enforcement_risk": enforcement_risk,
            "recommendations": recommendations
        }

    def _find_critical_gaps(self, responses):
        """Identify critical controls that are not implemented."""
        gaps = []
        for control_id in CRITICAL_CONTROL_IDS:
            response = responses.get(control_id, "N")
            if response.upper() in ("N", "D"):
                gaps.append({
                    "control_id": control_id,
                    "response": response,
                    "risk_level": "CRITICAL"
                })
        return gaps

    def _find_high_risks(self, responses):
        """Identify high-risk controls that are not implemented."""
        high_risk_ids = {
            "A5-02", "A5-03", "A5-05",
            "A13-01",
            "A17-01", "A17-02",
            "A25-02",
            "A30-02",
            "A32-05", "A32-06", "A32-07", "A32-08",
            "A33-03", "A33-04",
            "A34-01",
            "A35-01",
            "A37-01"
        }
        high_risks = []
        for control_id in high_risk_ids:
            response = responses.get(control_id, "N")
            if response.upper() == "N":
                high_risks.append({
                    "control_id": control_id,
                    "response": response,
                    "risk_level": "HIGH"
                })
        return high_risks

    def _assess_enforcement_risk(self, scores, critical_gaps):
        """
        Determine overall ICO enforcement risk level.

        ELEVATED:  3+ critical gaps OR any Article 32/33 score below threshold
        MODERATE:  1-2 critical gaps OR key articles below threshold
        LOW:       0 critical gaps and all key articles above threshold
        """
        article_scores = scores.get("articles", {})

        # Check if any high-priority articles are below threshold
        articles_below_threshold = [
            art for art, threshold in ENFORCEMENT_THRESHOLDS.items()
            if article_scores.get(art, 0) < threshold
        ]

        if len(critical_gaps) >= 3 or len(articles_below_threshold) >= 2:
            return "ELEVATED"
        elif len(critical_gaps) >= 1 or len(articles_below_threshold) >= 1:
            return "MODERATE"
        else:
            return "LOW"

    def _generate_recommendations(self, critical_gaps, high_risks, scores):
        """
        Generate prioritised remediation recommendations.
        Returns a list of recommendation dicts ordered by priority.
        """
        recommendations = []

        # Recommendation templates keyed by control ID
        rec_templates = {
            "A5-01": {
                "priority": 1,
                "action": "Document a lawful basis for every processing activity",
                "detail": "Create a processing register that maps each activity to a specific Article 6 (or Article 9) lawful basis. Review with a qualified DPO.",
                "effort": "Medium",
                "ico_risk": "High — absence of lawful basis is directly actionable by the ICO"
            },
            "A5-06": {
                "priority": 1,
                "action": "Implement integrity and confidentiality controls across all personal data stores",
                "detail": "Conduct a data mapping exercise, then apply encryption, access controls, and logging to all identified stores.",
                "effort": "High",
                "ico_risk": "High — security failures are the leading cause of ICO enforcement action"
            },
            "A32-01": {
                "priority": 1,
                "action": "Encrypt all personal data at rest using AES-256 or equivalent",
                "detail": "Audit all data stores. Implement database-level and file-level encryption. Document the encryption standard in use.",
                "effort": "High",
                "ico_risk": "Critical — unencrypted personal data at rest is a significant ICO fine trigger"
            },
            "A32-02": {
                "priority": 1,
                "action": "Enforce TLS 1.2 or higher for all data in transit",
                "detail": "Audit all network connections that carry personal data. Disable TLS 1.0 and 1.1. Test with SSL Labs or equivalent.",
                "effort": "Medium",
                "ico_risk": "Critical — unencrypted data in transit is a critical breach risk factor"
            },
            "A32-03": {
                "priority": 1,
                "action": "Implement role-based access control (RBAC) for all personal data systems",
                "detail": "Map roles to minimum necessary access rights. Remove standing access to sensitive data. Implement access request and review processes.",
                "effort": "High",
                "ico_risk": "Critical — improper access controls feature in the majority of reported breaches"
            },
            "A32-04": {
                "priority": 1,
                "action": "Enforce multi-factor authentication (MFA) on all systems processing personal data",
                "detail": "Deploy MFA via an authenticator app or hardware token. Password-only access to personal data systems is no longer considered adequate.",
                "effort": "Medium",
                "ico_risk": "High — ICO increasingly cites absent MFA as an aggravating factor in enforcement"
            },
            "A33-01": {
                "priority": 1,
                "action": "Develop and test a data breach response procedure",
                "detail": "Create a breach response plan covering: detection, internal escalation, ICO notification (72-hour clock), and data subject communication. Test it with a tabletop exercise.",
                "effort": "Medium",
                "ico_risk": "Critical — late or absent breach notification carries significant ICO penalties"
            },
            "A33-02": {
                "priority": 1,
                "action": "Train all staff on how to recognise and report a data breach",
                "detail": "Conduct mandatory breach awareness training. Create a simple internal reporting mechanism (email address, form, or helpdesk route). Document training records.",
                "effort": "Low",
                "ico_risk": "High — staff who do not report breaches prevent the 72-hour clock from starting"
            },
            "A25-01": {
                "priority": 2,
                "action": "Embed privacy review into the design process for new systems",
                "detail": "Create a pre-build privacy checklist. All new systems must complete a privacy review before development begins. Document outcomes.",
                "effort": "Medium",
                "ico_risk": "High — privacy-by-design failures compound other compliance gaps"
            },
            "A30-01": {
                "priority": 2,
                "action": "Create and maintain a Record of Processing Activities (ROPA)",
                "detail": "Map all processing activities across the organisation. Document purpose, lawful basis, data categories, recipients, and retention. Keep the ROPA in an accessible format.",
                "effort": "High",
                "ico_risk": "High — ICO routinely requests ROPA as first step in any investigation"
            },
        }

        # Add recommendations for critical gaps
        for gap in critical_gaps:
            cid = gap["control_id"]
            if cid in rec_templates:
                rec = rec_templates[cid].copy()
                rec["control_id"] = cid
                rec["triggered_by"] = "CRITICAL GAP"
                recommendations.append(rec)

        # Add recommendations for high risks not already covered
        covered_ids = {r["control_id"] for r in recommendations}
        for risk in high_risks:
            cid = risk["control_id"]
            if cid in rec_templates and cid not in covered_ids:
                rec = rec_templates[cid].copy()
                rec["control_id"] = cid
                rec["triggered_by"] = "HIGH RISK"
                recommendations.append(rec)

        # Sort by priority
        recommendations.sort(key=lambda x: x.get("priority", 99))
        return recommendations