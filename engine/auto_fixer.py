def auto_fix_design(design, brand_rules):
    fixed = False
    changes = []

    # ---------- COLORS ----------
    approved_colors = brand_rules["colors"]["approved"]
    default_color = approved_colors[0]

    for el in design["elements"]:
        if "color" in el:
            if el["color"] not in approved_colors:
                changes.append(
                    f"Color {el['color']} replaced with {default_color}"
                )
                el["color"] = default_color
                fixed = True

    # ---------- FONTS ----------
    approved_fonts = brand_rules["fonts"]["approved"]
    default_font = approved_fonts[0]

    for el in design["elements"]:
        if "font" in el:
            if el["font"] not in approved_fonts:
                changes.append(
                    f"Font {el['font']} replaced with {default_font}"
                )
                el["font"] = default_font
                fixed = True

    # ---------- LOGO ----------
    logo_rules = brand_rules["logo"]

    for el in design["elements"]:
        if el.get("type") == "logo":
            if el["padding"] < logo_rules["min_padding_px"]:
                changes.append(
                    f"Logo padding set to {logo_rules['min_padding_px']}"
                )
                el["padding"] = logo_rules["min_padding_px"]
                fixed = True

            if el["position"] not in logo_rules["allowed_positions"]:
                new_pos = logo_rules["allowed_positions"][0]
                changes.append(
                    f"Logo position changed to {new_pos}"
                )
                el["position"] = new_pos
                fixed = True

    return design, changes, fixed
