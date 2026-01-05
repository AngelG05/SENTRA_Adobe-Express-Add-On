from transformers import pipeline

rewriter = pipeline(
    "text2text-generation",
    model="google/flan-t5-small"
)

def rewrite_text(text, target_tone="professional"):
    prompt = f"""
Rewrite the following sentence to sound {target_tone},
neutral, and brand-safe. Avoid promotional language.

Sentence: {text}
Rewrite:
"""
    result = rewriter(prompt, max_length=64)
    return result[0]["generated_text"].strip()
