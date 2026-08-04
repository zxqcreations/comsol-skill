"""Audit quality of all API reference files."""
import os

ref_dir = r"D:\ENV\claude\comsol-skill\references"
files = sorted([f for f in os.listdir(ref_dir) if f.startswith("api_") and f.endswith(".md")])

print(f"AUDITING {len(files)} API REFERENCE FILES\n")

for f in files:
    path = os.path.join(ref_dir, f)
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()

    lines = len(text.split("\n"))

    # Quality signals
    sections = text.count("## ")
    subsections = text.count("### ")
    feature_tables = text.count("| Feature") + text.count("| Domain") + text.count("| Boundary Condition")
    has_bc_detail = text.count("| BC") + text.count("| Condition")
    has_expr = "Expression" in text or "expression" in text
    has_props = "set(" in text or "property" in text.lower()
    has_raw_toc = "TOC:" in text
    has_raw_pages = "--- Page " in text
    is_dump = has_raw_toc or has_raw_pages

    # Determine quality
    if is_dump:
        quality = "RAW_DUMP"
    elif sections >= 4 and feature_tables >= 2:
        quality = "GOOD"
    elif sections >= 2:
        quality = "PARTIAL"
    else:
        quality = "MINIMAL"

    print(f"{f}")
    print(f"  Lines: {lines} | Sections: {sections} | Subsections: {subsections}")
    print(f"  Feature/BC tables: {feature_tables} | Has expressions: {has_expr} | Has properties: {has_props}")
    print(f"  Raw TOC/Pages: {has_raw_toc}/{has_raw_pages}")
    print(f"  QUALITY: {quality}")
    print()

# Summary
good = 0
partial = 0
raw = 0
for f in files:
    path = os.path.join(ref_dir, f)
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if "TOC:" in text or "--- Page " in text:
        raw += 1
    elif text.count("## ") >= 4 and (text.count("| Feature") + text.count("| Domain") + text.count("| Boundary Condition")) >= 2:
        good += 1
    else:
        partial += 1

print(f"SUMMARY: {good} GOOD | {partial} PARTIAL | {raw} RAW_DUMP (out of {len(files)})")
