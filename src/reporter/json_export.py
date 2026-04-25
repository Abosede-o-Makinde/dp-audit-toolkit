# JSON export

import json

def export_to_json(scores, overall_score, risks, filename="audit_summary.json"):
    data = {
        "overall_score": overall_score,
        "article_scores": scores,
        "risks": risks,
        "generated": __import__('datetime').datetime.now().isoformat()
    }
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)