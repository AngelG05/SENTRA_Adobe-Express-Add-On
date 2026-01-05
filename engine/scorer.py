def calculate_score(violations):
    score = 100

    for v in violations:
        if v["type"] == "color":
            score -= 10
        elif v["type"] == "font":
            score -= 15
        elif v["type"] == "logo":
            score -= 20
        elif v["type"] == "layout":
            score -= 10

    return max(score, 0)
