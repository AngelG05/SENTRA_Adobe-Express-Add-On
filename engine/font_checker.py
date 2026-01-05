def check_fonts(elements, brand_fonts):
    violations = []

    approved = brand_fonts["approved"]

    for el in elements:
        if "font" in el:
            if el["font"] not in approved:
                violations.append({
                    "type": "font",
                    "message": f"Unapproved font {el['font']}"
                })

    return violations
