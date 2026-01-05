from transformers import pipeline

# Load once (important for performance)
classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def detect_tone(text):
    """
    Returns: detected_tone, confidence
    """
    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    # Map sentiment → tone
    if label == "POSITIVE":
        tone = "promotional"
    else:
        tone = "neutral"

    return tone, round(score, 2)
