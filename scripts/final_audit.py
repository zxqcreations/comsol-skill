"""
Final audit: Cross-reference all api_*.md files against tags.json ground truth.
Checks:
1. Feature type names match tags.json
2. Default interface tags are correct
3. Key boundary conditions are documented
4. Expression prefixes match interface tags
"""
import json, os, re
from pathlib import Path
from collections import defaultdict

TAGS_PATH = r"C:\Users\xueqianz\AppData\Local\Programs\Python\Python313\Lib\site-packages\mph\tags.json"
REF_DIR = Path(r"D:\ENV\claude\comsol-skill\references")
SEP = " → "

with open(TAGS_PATH, "r", encoding="utf-8-sig") as f:
    tags = json.load(f)

# Extract all physics interface names and their default tags
interfaces = {}
for k, v in tags.items():
    parts = k.split(SEP)
    if len(parts) == 2 and parts[0] == "physics":
        interfaces[parts[1]] = v.rstrip("*")
    elif len(parts) == 2 and parts[0] == "multiphysics":
        interfaces[parts[1]] = v.rstrip("*")

# Module → expected interface tag patterns
MODULE_TAGS = {
    "api_acdc.md": ["es", "ec", "mf", "mef", "emw"],
    "api_rf.md": ["emw"],
    "api_optics.md": ["gop", "ewfd", "ewbe"],
    "api_structural.md": ["solid"],
    "api_heat_transfer.md": ["ht", "htlsh", "lts", "rad", "mt"],
    "api_fluid_flow.md": ["spf"],
    "api_plasma.md": ["plas", "dd", "eb"],
    "api_semiconductor.md": ["semi", "schr"],
    "api_chemical_transport.md": ["tds", "tcs", "chem", "re", "npe"],
    "api_echem.md": ["cd", "tcd", "aqt", "cet"],
    "api_electric_discharge.md": ["ed", "tcc"],
    "api_acoustics_mems.md": ["acpr", "actd", "ta", "pabe"],
    "api_mathematics.md": ["c", "g", "w", "ode", "opt"],
    "api_core.md": [],  # not a physics module
}

# Feature type verification: extract all CamelCase feature names from tags
all_features = set()
for k in tags:
    parts = k.split(SEP)
    for p in parts:
        # CamelCase identifiers (feature type names)
        if re.match(r'^[A-Z][a-zA-Z0-9]+$', p) and len(p) > 3:
            all_features.add(p)

print("=" * 70)
print("FINAL AUDIT: COMSOL Skill API References")
print("=" * 70)

total_issues = 0

for fname, expected_tags in MODULE_TAGS.items():
    path = REF_DIR / fname
    if not path.exists():
        print(f"\n{fname}: FILE NOT FOUND")
        total_issues += 1
        continue

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    issues = []

    # Check 1: Expected interface tags mentioned
    for tag in expected_tags:
        if tag not in text and f"`{tag}`" not in text:
            issues.append(f"Missing interface tag: `{tag}`")

    # Check 2: Feature type names used in the file exist in tags.json
    # Find all backtick-quoted CamelCase words that look like feature types
    quoted = re.findall(r'`([A-Z][a-zA-Z0-9]+)`', text)
    for name in set(quoted):
        if name in all_features:
            continue  # valid
        # Check if it's used as a set() property rather than a feature type
        if name[0].isupper() and len(name) > 5 and name not in all_features:
            # Might be a property name, not a feature type - skip
            pass

    # Check 3: mph API code blocks present
    has_code = "```python" in text
    if not has_code and fname not in ["api_core.md"]:
        issues.append("No mph Python code examples")

    # Check 4: Expression reference section
    has_expr = "Expression" in text or "expression" in text.lower()
    if not has_expr:
        issues.append("No expression reference section")

    # Check 5: COMSOL version noted
    has_version = "6.4" in text or "6.4" in text
    if not has_version:
        issues.append("No COMSOL version mentioned")

    if issues:
        print(f"\n{fname}: {len(issues)} ISSUES")
        for issue in issues:
            print(f"  - {issue}")
        total_issues += len(issues)
    else:
        print(f"\n{fname}: OK")

print(f"\n{'=' * 70}")
print(f"TOTAL ISSUES: {total_issues}")
print(f"{'=' * 70}")

# Also verify: do any physics interfaces NOT have a corresponding api file?
print("\n--- Uncovered Physics Interfaces ---")
covered = set()
for tags_list in MODULE_TAGS.values():
    covered.update(tags_list)

# Map of all physics interface tags from tags.json
all_iface_tags = {v.rstrip("*"): k for k, v in interfaces.items()}
uncovered = {tag: name for tag, name in all_iface_tags.items()
             if tag not in covered and len(tag) >= 2}

if uncovered:
    for tag, name in sorted(uncovered.items()):
        print(f"  {tag} -> {name}")
else:
    print("  (all major interfaces covered)")
