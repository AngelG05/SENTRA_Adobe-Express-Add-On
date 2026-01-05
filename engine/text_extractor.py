def extract_text(design):
    texts = []

    for el in design.get("elements", []):
        if el.get("type") == "text":
            # content key future-ready
            content = el.get("content") or el.get("text") or ""
            if content.strip():
                texts.append(content.strip())

    return texts
