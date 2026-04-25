# CLI interaction handler

import click
from ..auditor.checklist import GDPR_CHECKLIST
from ..auditor.scorer import calculate_article_score, calculate_overall_score
from ..auditor.risk_engine import assess_risks
from ..reporter.pdf_report import generate_pdf_report
from ..reporter.json_export import export_to_json
from ..reporter.markdown_export import generate_markdown_report

@click.command()
@click.option('--output', default='audit_report', help='Output file prefix')
def main(output):
    scores = {}
    for article in GDPR_CHECKLIST:
        responses = []
        for question in GDPR_CHECKLIST[article]["questions"]:
            resp = click.prompt(f"{question} (yes/no)", type=click.Choice(['yes', 'no']))
            responses.append(resp)
        scores[article] = calculate_article_score(article, responses)

    overall_score = calculate_overall_score(scores)
    risks = assess_risks(scores)

    generate_pdf_report(scores, overall_score, risks, f"{output}.pdf")
    export_to_json(scores, overall_score, risks, f"{output}.json")
    generate_markdown_report(scores, overall_score, risks, f"{output}.md")

    click.echo(f"Reports generated: {output}.pdf, {output}.json, {output}.md")