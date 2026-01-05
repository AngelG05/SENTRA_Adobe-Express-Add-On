def check_logo(elements, logo_rules):
    violations = []

    for el in elements:
        if el["type"] == "logo":
            if el["padding"] < logo_rules["min_padding_px"]:
                violations.append({
                    "type": "logo",
                    "message": "Logo padding too small"
                })

            if el["position"] not in logo_rules["allowed_positions"]:
                violations.append({
                    "type": "logo",
                    "message": f"Logo position {el['position']} not allowed"
                })

    return violations
