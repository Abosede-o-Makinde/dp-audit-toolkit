"""
checklist.py
============
GDPR control checklist — all questions, article mappings, weights, and risk levels.

Each control is a dictionary with:
  - id:           unique control identifier
  - article:      GDPR article(s) this control satisfies
  - domain:       audit domain grouping
  - question:     the control question asked to the auditor
  - guidance:     plain-English explanation of what is required
  - weight:       scoring weight (1–3, where 3 = highest ICO enforcement priority)
  - quickscan:    True if included in the 20-question quickscan mode
  - risk_if_no:   risk classification if this control is not implemented
"""


class GDPRChecklist:
    """
    Loads and manages the full GDPR control checklist.
    All controls are mapped to specific UK GDPR articles.
    """

    RESPONSE_OPTIONS = {
        "Y": 100,   # Fully implemented and documented
        "P": 50,    # Partially implemented
        "N": 0,     # Not implemented
        "D": 20,    # Planned but not yet implemented (documented plan exists)
        "NA": None  # Not applicable (requires justification)
    }

    def __init__(self):
        self.controls = self._load_controls()

    def _load_controls(self):
        return [

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 5 — Data protection principles
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A5-01",
                "article": "Article 5(1)(a)",
                "domain": "Data Principles",
                "question": "Does the organisation have a documented lawful basis for each processing activity?",
                "guidance": "Every processing activity must have a lawful basis under Article 6 (or Article 9 for special categories). This must be documented before processing begins.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A5-02",
                "article": "Article 5(1)(b)",
                "domain": "Data Principles",
                "question": "Are personal data collected only for specified, explicit, and legitimate purposes?",
                "guidance": "Data must not be used in ways incompatible with the original collection purpose. This requires a documented purpose register.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A5-03",
                "article": "Article 5(1)(c)",
                "domain": "Data Principles",
                "question": "Is personal data limited to what is necessary for the processing purpose (data minimisation)?",
                "guidance": "Only data that is adequate, relevant and necessary should be collected. Forms and systems should be reviewed to remove unnecessary fields.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A5-04",
                "article": "Article 5(1)(d)",
                "domain": "Data Principles",
                "question": "Are there processes in place to keep personal data accurate and up to date?",
                "guidance": "Inaccurate data must be corrected or erased. Organisations should have data quality checks and procedures for handling correction requests.",
                "weight": 1,
                "quickscan": False,
                "risk_if_no": "MEDIUM"
            },
            {
                "id": "A5-05",
                "article": "Article 5(1)(e)",
                "domain": "Data Principles",
                "question": "Is personal data retained only for as long as necessary, with documented retention schedules?",
                "guidance": "A retention schedule must define how long each data category is kept and when it is deleted. This must be technically enforced, not just documented.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A5-06",
                "article": "Article 5(1)(f)",
                "domain": "Data Principles",
                "question": "Is personal data protected against unauthorised access, loss, or destruction (integrity and confidentiality)?",
                "guidance": "Appropriate technical and organisational measures must protect data. This is the principle that underpins Article 32 security requirements.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A5-07",
                "article": "Article 5(2)",
                "domain": "Data Principles",
                "question": "Can the organisation demonstrate compliance with all data protection principles (accountability)?",
                "guidance": "Controllers must be able to demonstrate compliance — not just assert it. This requires documented policies, records, and evidence of implementation.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLES 13–14 — Transparency and privacy notices
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A13-01",
                "article": "Article 13",
                "domain": "Transparency",
                "question": "Are data subjects provided with a privacy notice at the point of data collection?",
                "guidance": "Privacy notices must include: identity of controller, purposes, lawful basis, retention period, data subject rights, and right to complain to the ICO.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A13-02",
                "article": "Article 13",
                "domain": "Transparency",
                "question": "Is the privacy notice written in plain, clear language accessible to the audience?",
                "guidance": "Privacy notices must be concise, transparent, and intelligible. Legal jargon is not acceptable for public-facing notices.",
                "weight": 1,
                "quickscan": False,
                "risk_if_no": "MEDIUM"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 17 — Right to erasure
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A17-01",
                "article": "Article 17",
                "domain": "Data Subject Rights",
                "question": "Does the organisation have a documented and tested process to erase personal data on request?",
                "guidance": "Erasure must be technically possible and completed without undue delay (within 1 month). The process must cover all systems where data is held — including backups.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A17-02",
                "article": "Article 17",
                "domain": "Data Subject Rights",
                "question": "Are erasure requests logged and responded to within the required timeframe (1 month)?",
                "guidance": "A formal log of all data subject requests must be maintained, with response dates recorded.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 25 — Privacy by design and by default
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A25-01",
                "article": "Article 25(1)",
                "domain": "Privacy by Design",
                "question": "Are data protection requirements considered at the design stage of new systems and processes?",
                "guidance": "Privacy by design requires that data protection is embedded from the start — not added later. New systems should go through a privacy review before build.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A25-02",
                "article": "Article 25(2)",
                "domain": "Privacy by Design",
                "question": "Are systems configured by default to process only the minimum data necessary?",
                "guidance": "Default settings must be privacy-protective. For example, optional data fields should be opt-in, not pre-checked. Systems should not collect data that is not needed.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A25-03",
                "article": "Article 25",
                "domain": "Privacy by Design",
                "question": "Is a Privacy Impact Assessment (or DPIA) conducted before deploying high-risk processing activities?",
                "guidance": "DPIAs are mandatory for high-risk processing (e.g. large-scale processing of special category data, systematic monitoring). See also Article 35.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 30 — Records of processing activities
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A30-01",
                "article": "Article 30",
                "domain": "Records",
                "question": "Does the organisation maintain a Record of Processing Activities (ROPA)?",
                "guidance": "A ROPA must document all processing activities, including purpose, lawful basis, data categories, recipients, transfers, and retention. It must be kept up to date.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A30-02",
                "article": "Article 30",
                "domain": "Records",
                "question": "Is the ROPA reviewed and updated at least annually or when processing activities change?",
                "guidance": "A ROPA that does not reflect current processing is a liability, not a compliance asset. Regular review must be scheduled and evidenced.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 32 — Security of processing
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A32-01",
                "article": "Article 32(1)(a)",
                "domain": "Security",
                "question": "Is personal data encrypted at rest using an appropriate standard (e.g. AES-256)?",
                "guidance": "Encryption at rest protects data in the event of physical theft or unauthorised storage access. The ICO expects encryption to be the default for sensitive data.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A32-02",
                "article": "Article 32(1)(a)",
                "domain": "Security",
                "question": "Is personal data encrypted in transit using TLS 1.2 or higher?",
                "guidance": "All personal data transmitted across networks must be protected. TLS 1.0 and 1.1 are deprecated and should not be in use.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A32-03",
                "article": "Article 32(1)(b)",
                "domain": "Security",
                "question": "Are access controls in place to ensure only authorised personnel can access personal data?",
                "guidance": "Role-based access control (RBAC) should limit access to the minimum necessary for each role. Access logs must be maintained.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A32-04",
                "article": "Article 32(1)(b)",
                "domain": "Security",
                "question": "Is multi-factor authentication (MFA) enforced for access to systems processing personal data?",
                "guidance": "MFA significantly reduces the risk of unauthorised access following credential compromise. The ICO increasingly expects MFA as a baseline control.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A32-05",
                "article": "Article 32(1)(c)",
                "domain": "Security",
                "question": "Are there procedures to restore availability and access to personal data in the event of an incident?",
                "guidance": "Business continuity and disaster recovery plans must cover personal data. Recovery time objectives (RTOs) should be documented and tested.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A32-06",
                "article": "Article 32(1)(d)",
                "domain": "Security",
                "question": "Is the effectiveness of security measures regularly tested and evaluated?",
                "guidance": "Security testing — including penetration testing, vulnerability scanning, and access control reviews — must be conducted regularly and results acted upon.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A32-07",
                "article": "Article 32",
                "domain": "Security",
                "question": "Is there a documented information security policy approved by senior management?",
                "guidance": "A security policy must be in place, communicated to staff, and reviewed regularly. It must be backed by senior management commitment.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A32-08",
                "article": "Article 32",
                "domain": "Security",
                "question": "Are staff who process personal data trained in data protection and security awareness?",
                "guidance": "Human error is the leading cause of data breaches. Regular, documented training is essential and expected by the ICO as a baseline organisational measure.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 33 — Breach notification to ICO
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A33-01",
                "article": "Article 33",
                "domain": "Breach Response",
                "question": "Does the organisation have a documented data breach response procedure?",
                "guidance": "A breach response plan must define roles, escalation paths, and the 72-hour notification process. It must be tested before it is needed.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A33-02",
                "article": "Article 33",
                "domain": "Breach Response",
                "question": "Are staff aware of how to recognise and report a data breach internally?",
                "guidance": "Breaches must be reported internally without undue delay so the organisation can assess and notify the ICO within 72 hours where required.",
                "weight": 3,
                "quickscan": True,
                "risk_if_no": "CRITICAL"
            },
            {
                "id": "A33-03",
                "article": "Article 33",
                "domain": "Breach Response",
                "question": "Is a breach register maintained to record all personal data breaches (including those not notified to the ICO)?",
                "guidance": "All breaches must be logged regardless of whether they are notified to the ICO. The register must include the facts, effects, and remedial actions.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A33-04",
                "article": "Article 33",
                "domain": "Breach Response",
                "question": "Has the breach response procedure been tested in the last 12 months (e.g. tabletop exercise)?",
                "guidance": "An untested breach plan is not a reliable breach plan. Annual testing ensures staff know what to do before a real incident occurs.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 34 — Communication to data subjects
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A34-01",
                "article": "Article 34",
                "domain": "Breach Response",
                "question": "Is there a process for notifying data subjects when a breach is likely to result in high risk to them?",
                "guidance": "Where a breach is likely to result in high risk to individuals, they must be notified without undue delay. A template communication should be prepared in advance.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 35 — Data protection impact assessment
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A35-01",
                "article": "Article 35",
                "domain": "DPIA",
                "question": "Does the organisation have a DPIA process for high-risk processing activities?",
                "guidance": "DPIAs are mandatory for: large-scale processing of special category data, systematic profiling, systematic public monitoring, and new technologies with high risk.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A35-02",
                "article": "Article 35",
                "domain": "DPIA",
                "question": "Are completed DPIAs documented and reviewed when processing changes?",
                "guidance": "A DPIA is not a one-time exercise. It must be reviewed when the processing it covers changes in a way that could affect the risk assessment.",
                "weight": 1,
                "quickscan": False,
                "risk_if_no": "MEDIUM"
            },

            # ─────────────────────────────────────────────────────────────
            # ARTICLE 37 — Data Protection Officer
            # ─────────────────────────────────────────────────────────────
            {
                "id": "A37-01",
                "article": "Article 37",
                "domain": "DPO",
                "question": "Has the organisation assessed whether it is required to appoint a Data Protection Officer (DPO)?",
                "guidance": "DPO appointment is mandatory for: public authorities, organisations carrying out large-scale systematic monitoring, and large-scale processing of special category data.",
                "weight": 2,
                "quickscan": True,
                "risk_if_no": "HIGH"
            },
            {
                "id": "A37-02",
                "article": "Article 37-39",
                "domain": "DPO",
                "question": "Where a DPO is appointed, are they provided with sufficient resources and independence?",
                "guidance": "The DPO must have access to senior management, must not receive instructions on how to perform their tasks, and must not be conflicted by other duties.",
                "weight": 2,
                "quickscan": False,
                "risk_if_no": "HIGH"
            },
        ]

    def get_all_controls(self):
        return self.controls

    def get_quickscan_controls(self):
        return [c for c in self.controls if c["quickscan"]]

    def get_controls_by_article(self, article_key):
        return [c for c in self.controls if article_key.lower() in c["article"].lower()]

    def get_controls_by_domain(self, domain):
        return [c for c in self.controls if c["domain"] == domain]

    def get_article_groups(self):
        """Returns controls grouped by article prefix."""
        groups = {}
        for control in self.controls:
            # Extract article number prefix (e.g. "article_5")
            art = control["article"].split("(")[0].strip().lower().replace(" ", "_")
            if art not in groups:
                groups[art] = []
            groups[art].append(control)
        return groups