def check_colors(elements, brand_colors):
    violations = []

    approved = [c.lower() for c in brand_colors["approved"]]

    for el in elements:
        if "color" in el:
            if el["color"].lower() not in approved:
                violations.append({
                    "type": "color",
                    "message": f"Unapproved color {el['color']}"
                })

    return violations
