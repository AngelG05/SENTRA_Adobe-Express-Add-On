from engine.text_extractor import extract_text
from engine.tone_classifier import detect_tone
from engine.tone_rewriter import rewrite_text

def analyze_tone(design, brand_rules):
    texts = extract_text(design)

    if not texts:
        return None

    expected = brand_rules["tone"]["expected"]
    restricted = brand_rules["tone"]["restricted_words"]

    issues = []

    for text in texts:
        lower = text.lower()

        # Rule-based restricted words
        for word in restricted:
            if word in lower:
                issues.append({
                    "type": "restricted_word",
                    "text": text,
                    "issue": f"Restricted word '{word}' used"
                })

        # ML-based tone detection
        detected_tone, confidence = detect_tone(text)

        if detected_tone != expected:
            rewritten = rewrite_text(text, expected)
            issues.append({
                "type": "tone_mismatch",
                "text": text,
                "detected_tone": detected_tone,
                "expected_tone": expected,
                "confidence": confidence,
                "suggestion": rewritten
            })


    return issues if issues else None
