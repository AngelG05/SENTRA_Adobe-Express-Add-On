import json
import os
from datetime import datetime
print("LOGGER FILE LOADED")
LOG_DIR = r"C:\Users\bhavy\sentra_logs"
LOG_FILE = os.path.join(LOG_DIR, "compliance_logs.json")

def log_compliance(result):
    print("LOGGER FUNCTION CALLED")
    os.makedirs(LOG_DIR, exist_ok=True)

    entry = {
        "timestamp": datetime.now().isoformat(),
        "brand_score": result["brand_score"],
        "visual_violations": len(result["violations"]),
        "tone_violations": len(result.get("tone_issues", []))
    }

    if os.path.exists(LOG_FILE):
        data = json.load(open(LOG_FILE))
    else:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)
