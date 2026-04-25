# PDF report generator (reportlab)

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def generate_pdf_report(scores, overall_score, risks, filename="audit_report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("DATA PROTECTION AUDIT REPORT", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}", styles['Normal']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"OVERALL COMPLIANCE SCORE: {overall_score} / 100", styles['Heading2']))
    story.append(Spacer(1, 12))

    for article, score in scores.items():
        color = "🟢 GREEN" if score >= 80 else "🟡 AMBER" if score >= 60 else "🔴 RED"
        story.append(Paragraph(f"{article} — {score}/100 {color}", styles['Normal']))

    story.append(Spacer(1, 12))
    story.append(Paragraph(f"CRITICAL GAPS: {risks['critical_gaps']} identified", styles['Normal']))
    story.append(Paragraph(f"HIGH RISK: {risks['high_risks']} identified", styles['Normal']))
    story.append(Paragraph(f"ICO ENFORCEMENT RISK: {risks['ico_enforcement_risk']}", styles['Normal']))

    doc.build(story)