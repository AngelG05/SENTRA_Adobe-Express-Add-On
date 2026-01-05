def check_aspect_ratio(canvas, layout_rules):
    w = canvas["width"]
    h = canvas["height"]
    ratio = f"{w//min(w,h)}:{h//min(w,h)}"

    if ratio not in layout_rules["allowed_aspect_ratios"]:
        return [{
            "type": "layout",
            "message": f"Aspect ratio {ratio} not allowed"
        }]

    return []
