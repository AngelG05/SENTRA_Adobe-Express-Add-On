def calculate_score(violations):
    score = 100
    breakdown = []

    for v in violations:
        if v["type"] == "color":
            score -= 15
            breakdown.append("Color mismatch")
        elif v["type"] == "font":
            score -= 10
            breakdown.append("Font violation")
        elif v["type"] == "logo":
            score -= 20
            breakdown.append("Logo misuse")
        elif v["type"] == "layout":
            score -= 10
            breakdown.append("Layout mismatch")

    return {
        "score": max(score, 0),
        "reasons": breakdown
    }
