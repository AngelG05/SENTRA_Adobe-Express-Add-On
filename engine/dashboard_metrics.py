import json
import os

LOG_FILE = "logs/compliance_logs.json"

def get_metrics():
    if not os.path.exists(LOG_FILE):
        return {
            "total_checks": 0,
            "average_brand_score": 0,
            "average_visual_violations": 0,
            "average_tone_violations": 0
        }

    data = json.load(open(LOG_FILE))

    if len(data) == 0:
        return {
            "total_checks": 0,
            "average_brand_score": 0,
            "average_visual_violations": 0,
            "average_tone_violations": 0
        }

    total = len(data)

    avg_score = sum(d["brand_score"] for d in data) / total
    avg_visual = sum(d["visual_violations"] for d in data) / total
    avg_tone = sum(d["tone_violations"] for d in data) / total

    return {
        "total_checks": total,
        "average_brand_score": round(avg_score, 2),
        "average_visual_violations": round(avg_visual, 2),
        "average_tone_violations": round(avg_tone, 2)
    }
