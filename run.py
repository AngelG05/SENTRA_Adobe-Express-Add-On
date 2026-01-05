from sentra_engine import run_sentra

result = run_sentra(
    "input_designs/design_1.json",
    "brand_kit/brand_rules.json"
)

print("Violations:")
for v in result["violations"]:
    print("-", v["message"])

print("\nBrand Score:", result["brand_score"])
