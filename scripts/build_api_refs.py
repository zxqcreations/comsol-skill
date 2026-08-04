"""Build API reference files from pre-extracted PDF text + tags.json."""
import json, os, re
from pathlib import Path
from collections import defaultdict

TAGS_PATH = r"C:\Users\xueqianz\AppData\Local\Programs\Python\Python313\Lib\site-packages\mph\tags.json"
EXTRACT_DIR = Path(r"D:\ENV\claude\comsol-skill\references\_extracted")
OUT_DIR = Path(r"D:\ENV\claude\comsol-skill\references")
SEP = " → "

# Load tags
with open(TAGS_PATH, "r", encoding="utf-8-sig") as f:
    tags = json.load(f)

# Build tag lookup: feature_name -> tag
tag_lookup = {}
for k, v in tags.items():
    parts = k.split(SEP)
    if len(parts) >= 3:
        tag_lookup[parts[-1]] = {"tag": v, "full_path": k}
    elif len(parts) >= 2 and not any(k.startswith(p) for p in ["physics", "multiphysics", "geometries", "meshes", "studies"]):
        tag_lookup[parts[-1]] = {"tag": v, "full_path": k}

# Module definitions with their tag prefixes and key feature types
modules = {
    "api_rf": {
        "title": "RF Module",
        "extracts": ["api_rf_extract.txt"],
        "tag_matches": ["ElectromagneticWaves", "emw", "Port"],
        "feature_types": [],
    },
    "api_optics": {
        "title": "Optics Module (Ray + Wave)",
        "extracts": ["api_optics_ray_extract.txt", "api_optics_wave_extract.txt"],
        "tag_matches": ["GeometricalOptics", "WaveOptics", "gop", "ewfd"],
        "feature_types": [],
    },
    "api_plasma": {
        "title": "Plasma Module",
        "extracts": ["api_plasma_extract.txt"],
        "tag_matches": ["Plasma", "plasma", "DriftDiffusion"],
        "feature_types": [],
    },
    "api_semiconductor": {
        "title": "Semiconductor Module",
        "extracts": ["api_semiconductor_extract.txt"],
        "tag_matches": ["Semiconductor", "semiconductor", "Schottky", "Ohmic"],
        "feature_types": [],
    },
    "api_chemical_transport": {
        "title": "Chemical Species Transport Module",
        "extracts": ["api_chemical_extract.txt"],
        "tag_matches": ["TransportOfDilutedSpecies", "TransportOfConcentratedSpecies", "tds", "ReactionEngineering", "Chemistry"],
        "feature_types": [],
    },
    "api_electric_discharge": {
        "title": "Electric Discharge Module",
        "extracts": ["api_discharge_extract.txt"],
        "tag_matches": ["ElectricDischarge", "Discharge", "discharge"],
        "feature_types": [],
    },
    "api_mathematics": {
        "title": "Mathematics Module (PDE/ODE Interfaces)",
        "extracts": [],
        "tag_matches": ["CoefficientFormPDE", "GeneralFormPDE", "WeakFormPDE", "ODE", "DAE", "Optimization"],
        "feature_types": [],
    },
}

# Extract feature types from tags for each module
for filename, mod in modules.items():
    for tag_kw in mod["tag_matches"]:
        for k, v in tags.items():
            if tag_kw.lower() in k.lower():
                parts = k.split(SEP)
                mod["feature_types"].append({
                    "path": k,
                    "tag": v,
                    "name": parts[-1],
                    "parent": parts[-2] if len(parts) >= 2 else "",
                })

# Build reference files
for filename, mod in modules.items():
    out_path = OUT_DIR / f"{filename}.md"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# {mod['title']} — API Reference\n\n")
        f.write(f"Extracted from COMSOL 6.4 documentation and mph tags.json.\n\n")

        # Feature types from tags
        ft_count = len(mod["feature_types"])
        if ft_count > 0:
            f.write(f"## Feature Types ({ft_count} found)\n\n")
            f.write("| Feature Name | Tag | Parent Interface |\n")
            f.write("|-------------|-----|------------------|\n")
            seen = set()
            for ft in sorted(mod["feature_types"], key=lambda x: x["path"]):
                name = ft["name"]
                if name in seen: continue
                seen.add(name)
                f.write(f"| `{name}` | `{ft['tag']}` | {ft['parent']} |\n")
            f.write("\n")

        # Read extracted text for content
        for ext_file in mod["extracts"]:
            ext_path = EXTRACT_DIR / ext_file
            if ext_path.exists():
                with open(ext_path, "r", encoding="utf-8") as ef:
                    text = ef.read()

                # Extract TOC structure
                toc_lines = [l for l in text.split("\n") if "TOC:" in l]
                if toc_lines:
                    f.write(f"## Documentation Structure ({ext_file})\n\n")
                    f.write("```\n")
                    for line in toc_lines[:50]:
                        f.write(line + "\n")
                    f.write("```\n\n")

                # Extract pages with interface/feature content
                feature_pages = []
                pages = text.split("--- Page ")
                for page_text in pages:
                    if any(kw.lower() in page_text.lower() for kw in ["interface", "feature", "boundary", "domain", "node", "setting"]):
                        # Clean and truncate
                        clean = page_text[:1500].strip()
                        if len(clean) > 100:
                            feature_pages.append(clean)

                if feature_pages:
                    f.write(f"## Key API Content ({len(feature_pages)} sections)\n\n")
                    for i, page in enumerate(feature_pages[:20]):
                        f.write(f"### Section {i+1}\n\n")
                        f.write("```\n")
                        f.write(page[:1000])
                        f.write("\n```\n\n")

    size = os.path.getsize(out_path)
    print(f"  {filename}.md: {size} bytes")

# Also build mathematics from core tags
math_path = OUT_DIR / "api_mathematics.md"
if not math_path.exists() or os.path.getsize(math_path) < 500:
    with open(math_path, "w", encoding="utf-8") as f:
        f.write("# Mathematics Module — API Reference\n\n")
        f.write("PDE/ODE interfaces from COMSOL 6.4.\n\n")

        pde_keywords = [
            "CoefficientFormPDE", "GeneralFormPDE", "WeakFormPDE",
            "WeakContribution", "DirichletBoundary", "FluxBoundary",
            "ZeroFluxBoundary", "PeriodicCondition",
            "GlobalEquations", "DomainODE", "BoundaryODE",
            "Optimization", "Objective", "Constraint",
        ]

        for kw in pde_keywords:
            f.write(f"### {kw}\n\n")
            found = []
            for k, v in tags.items():
                if kw.lower() in k.lower():
                    parts = k.split(SEP)
                    found.append({"path": k, "tag": v, "name": parts[-1]})

            if found:
                f.write("| Feature Name | Tag | Full Path |\n")
                f.write("|-------------|-----|-----------|\n")
                for item in found:
                    f.write(f"| `{item['name']}` | `{item['tag']}` | {item['path']} |\n")
            else:
                f.write("(Not found in tags.json)\n")
            f.write("\n")

print(f"\nAll 7 API references built in {OUT_DIR}")
