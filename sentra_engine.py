import json
from engine.color_checker import check_colors
from engine.font_checker import check_fonts
from engine.logo_checker import check_logo
from engine.aspect_ratio_checker import check_aspect_ratio
from engine.scorer import calculate_score
from engine.compliance_logger import log_compliance

def run_sentra(design_data, brand_rules_path):
    design = design_data
    brand = json.load(open(brand_rules_path))

    elements = design.get("elements", [])
    canvas = design.get("canvas", {})

    violations = []
    violations += check_colors(elements, brand["colors"])
    violations += check_fonts(elements, brand["fonts"])
    violations += check_logo(elements, brand["logo"])
    violations += check_aspect_ratio(canvas, brand["layout"])

    score = calculate_score(violations)

    result = {
        "violations": violations,
        "brand_score": score,
        "tone_issues": []   # ML temporarily off
    }

    log_compliance(result)
    return result
