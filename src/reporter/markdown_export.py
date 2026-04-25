# Markdown gap analysis

def generate_markdown_report(scores, overall_score, risks, filename="gap_analysis.md"):
    with open(filename, 'w') as f:
        f.write("# Data Protection Audit Gap Analysis\n\n")
        f.write(f"Overall Score: {overall_score}/100\n\n")
        f.write("## Article Scores\n\n")
        for article, score in scores.items():
            f.write(f"- {article}: {score}/100\n")
        f.write("\n## Risks\n\n")
        f.write(f"- Critical Gaps: {risks['critical_gaps']}\n")
        f.write(f"- High Risks: {risks['high_risks']}\n")
        f.write(f"- ICO Risk: {risks['ico_enforcement_risk']}\n")