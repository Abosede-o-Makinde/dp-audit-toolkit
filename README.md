# Data Protection Audit Toolkit (dp-audit-toolkit)

> A Python-based GRC tool that audits an organisation's data protection controls against UK GDPR obligations and produces a scored compliance report.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)
![GDPR](https://img.shields.io/badge/Framework-UK%20GDPR-purple?style=flat)

---

## What this tool does

The **Data Protection Audit Toolkit** allows a data protection officer, information governance lead, or security engineer to run a structured audit of an organisation's GDPR compliance posture — without needing legal expertise to interpret the results.

It works by:

1. **Collecting responses** to a structured control checklist (via CLI or JSON input)
2. **Mapping each control** to the specific UK GDPR article it satisfies
3. **Scoring compliance** across six GDPR domains (0–100 per domain)
4. **Generating a detailed report** (PDF + JSON) with findings, risk ratings, and prioritised recommendations
5. **Flagging critical gaps** that represent the highest ICO enforcement risk

---

## Why this exists

UK GDPR compliance is often treated as a legal or administrative exercise. The result is that organisations produce policies that satisfy auditors on paper but fail technically — encryption is absent, breach detection is manual, access controls are undocumented.

This tool is built on the premise that **GDPR compliance is an engineering problem** as much as a legal one. Every article in the regulation has a technical implementation. This toolkit makes those implementations explicit and auditable.

---

## GDPR articles covered

| Article | Domain | Description |
|---|---|---|
| Article 5 | Data principles | Lawfulness, fairness, transparency, accuracy, minimisation, storage limitation, integrity |
| Article 13–14 | Transparency | Privacy notices and information obligations |
| Article 17 | Right to erasure | Technical ability to delete personal data on request |
| Article 25 | Privacy by design | Data protection by design and by default |
| Article 30 | Records | Records of processing activities (ROPA) |
| Article 32 | Security | Technical and organisational security measures |
| Article 33 | Breach notification | 72-hour notification to ICO |
| Article 34 | Communication | Notification to data subjects |
| Article 35 | DPIA | Data protection impact assessments |
| Article 37 | DPO | Data protection officer designation |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/dp-audit-toolkit.git
cd dp-audit-toolkit

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

### Option 1 — Interactive CLI audit

```bash
python main.py --mode interactive
```

The tool will walk you through each control domain, asking questions and recording responses. Takes approximately 15–20 minutes for a full audit.

### Option 2 — JSON input (pre-filled responses)

```bash
python main.py --mode json --input config/sample_audit.json
```

Useful for repeating audits or integrating into automated pipelines.

### Option 3 — Quick scan (critical controls only)

```bash
python main.py --mode quickscan
```

Runs only the 20 highest-risk controls. Produces a red/amber/green summary in under 5 minutes.

### Output

All outputs are saved to `sample_outputs/`:

```
sample_outputs/
├── audit_report_[timestamp].pdf     # Full scored report with recommendations
├── audit_summary_[timestamp].json   # Machine-readable results
└── gdpr_gap_analysis_[timestamp].md # Gap analysis in markdown
```

---

## Sample output

```
╔══════════════════════════════════════════════════════════╗
║         DATA PROTECTION AUDIT REPORT                    ║
║         Generated: 2026-04-21                           ║
╠══════════════════════════════════════════════════════════╣
║  OVERALL COMPLIANCE SCORE:  61 / 100   [AMBER]          ║
╠══════════════════════════════════════════════════════════╣
║  Article 5  — Data principles        72/100  🟡 AMBER   ║
║  Article 25 — Privacy by design      45/100  🔴 RED     ║
║  Article 32 — Security measures      58/100  🟡 AMBER   ║
║  Article 33 — Breach notification    40/100  🔴 RED     ║
║  Article 35 — DPIA                   55/100  🟡 AMBER   ║
║  Article 37 — DPO designation        90/100  🟢 GREEN   ║
╠══════════════════════════════════════════════════════════╣
║  CRITICAL GAPS: 3 identified                            ║
║  HIGH RISK:     5 identified                            ║
║  ICO ENFORCEMENT RISK: ELEVATED                         ║
╚══════════════════════════════════════════════════════════╝
```

---

## Project structure

```
dp-audit-toolkit/
├── main.py                     # Entry point
├── requirements.txt            # Dependencies
├── README.md                   # This file
├── LICENSE                     # MIT licence
├── .gitignore
│
├── src/
│   ├── auditor/
│   │   ├── __init__.py
│   │   ├── checklist.py        # All GDPR control questions and mappings
│   │   ├── scorer.py           # Scoring engine (per-article + overall)
│   │   └── risk_engine.py      # Risk rating and gap classification
│   │
│   ├── reporter/
│   │   ├── __init__.py
│   │   ├── pdf_report.py       # PDF report generator (reportlab)
│   │   ├── json_export.py      # JSON export
│   │   └── markdown_export.py  # Markdown gap analysis
│   │
│   └── utils/
│       ├── __init__.py
│       ├── cli.py              # CLI interaction handler
│       ├── validator.py        # Input validation
│       └── logger.py           # Audit logging
│
├── config/
│   ├── gdpr_articles.json      # Article metadata and descriptions
│   ├── sample_audit.json       # Pre-filled sample for testing
│   └── risk_thresholds.json    # Configurable scoring thresholds
│
├── tests/
│   ├── test_checklist.py
│   ├── test_scorer.py
│   ├── test_risk_engine.py
│   └── test_reporter.py
│
├── docs/
│   ├── METHODOLOGY.md          # How scoring and mapping works
│   ├── GDPR_ARTICLE_GUIDE.md   # Plain-English guide to each article
│   └── CONTRIBUTING.md         # How to contribute
│
└── sample_outputs/
    ├── example_report.pdf
    └── example_summary.json
```

---

## Methodology

Scoring is based on a weighted control framework. Each GDPR article is broken into discrete, verifiable controls. Each control is scored as:

| Response | Score |
|---|---|
| Fully implemented and documented | 100 |
| Partially implemented | 50 |
| Planned but not implemented | 20 |
| Not implemented | 0 |
| Not applicable (with justification) | N/A |

Article scores are weighted by ICO enforcement priority. Articles 32, 25, and 33 carry the highest weights, reflecting the ICO's published enforcement history.

Full methodology: [docs/METHODOLOGY.md](docs/METHODOLOGY.md)

---

## Roadmap

- [x] Core checklist engine (Articles 5, 25, 32, 33, 34)
- [x] CLI interactive mode
- [x] JSON input mode
- [x] PDF report generation
- [x] Markdown gap analysis export
- [ ] Web dashboard (Streamlit) — v1.1
- [ ] NHS / public sector control set — v1.2
- [ ] API endpoint for integration with GRC platforms — v1.3
- [ ] DPIA template generator — v1.4

---

## Contributing

Contributions are welcome. Please read [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) before submitting a pull request.

Areas where contributions are most needed:
- Additional sector-specific control sets (healthcare, finance, education)
- Translations of report output
- Additional export formats

---

## Disclaimer

This tool is designed to support GDPR compliance assessment. It does not constitute legal advice and does not guarantee regulatory compliance. Organisations should seek qualified legal and data protection advice for formal compliance programmes.

---

## Licence

MIT — see [LICENSE](LICENSE)

---

## Author

Built by Abosede Makinde   
Research focus: GDPR technical implementation · Biometric security · Privacy-aware engineering  
[LinkedIn](https://linkedin.com/in/abosede-makinde-83052a1b7) · [GitHub](https://github.com/Abosede-o-Makinde)
