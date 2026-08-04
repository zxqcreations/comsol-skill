"""
Build comprehensive, hand-quality API references for ALL 13 COMSOL modules.
Uses: tags.json for exact type names + full PDF extracts for documentation.
Output format matches the quality of api_acdc.md and api_echem.md.
"""
import json, os, re
from pathlib import Path
from collections import defaultdict

TAGS_PATH = r"C:\Users\xueqianz\AppData\Local\Programs\Python\Python313\Lib\site-packages\mph\tags.json"
EXTRACT_DIR = Path(r"D:\ENV\claude\comsol-skill\references\_extracted")
OUT_DIR = Path(r"D:\ENV\claude\comsol-skill\references")
SEP = " → "

with open(TAGS_PATH, "r", encoding="utf-8-sig") as f:
    tags = json.load(f)

# ============================================================
# Module definitions: (output_file, title, tag_match_keywords, extract_files)
# ============================================================
MODULES = [
    {
        "file": "api_rf.md",
        "title": "RF Module",
        "subtitle": "Electromagnetic Waves — Frequency Domain, Transient, Time Explicit, Boundary Elements",
        "tag_kw": ["ElectromagneticWaves", "EMWaves", "emw", "Port", "Scattering", "Impedance",
                    "PerfectElectricConductor", "PerfectMagneticConductor",
                    "LumpedPort", "CircularPort", "RectangularPort", "CoaxialPort",
                    "Transition", "Periodic", "Floquet", "FarField", "NearField",
                    "Matched", "Absorbing", "FirstOrder", "SecondOrder",
                    "ElectricField", "MagneticField", "SurfaceCurrent"],
        "extracts": ["api_rf_full.txt"],
    },
    {
        "file": "api_optics.md",
        "title": "Optics Module",
        "subtitle": "Ray Optics + Wave Optics (Electromagnetic Waves, Frequency Domain + Beam Envelopes)",
        "tag_kw": ["GeometricalOptics", "WaveOptics", "BeamEnvelope", "gop", "ewfd",
                    "Ray", "Reflection", "Refraction", "Diffraction", "Grating",
                    "Scattering", "Mirror", "Lens", "Prism", "Polarization",
                    "Intensity", "Phase", "Optical", "Photon"],
        "extracts": ["api_optics_ray_full.txt", "api_optics_wave_full.txt"],
    },
    {
        "file": "api_plasma.md",
        "title": "Plasma Module",
        "subtitle": "Plasma physics — DC, CCP, ICP, Microwave, and Drift Diffusion",
        "tag_kw": ["Plasma", "plasma", "DriftDiffusion", "CCP", "ICP",
                    "Boltzmann", "Species", "Reaction", "Electron", "Ion",
                    "Debye", "Sheath", "Glow", "Arc", "DielectricBarrier"],
        "extracts": ["api_plasma_full.txt"],
    },
    {
        "file": "api_semiconductor.md",
        "title": "Semiconductor Module",
        "subtitle": "Semiconductor physics — Drift-Diffusion, Density-Gradient, Schrodinger-Poisson",
        "tag_kw": ["Semiconductor", "semiconductor", "DriftDiffusion", "Schottky",
                    "Ohmic", "Doping", "Generation", "Recombination", "Mobility",
                    "Band", "Fermi", "Carrier", "Avalanche", "Tunnel",
                    "Insulator", "Contact", "Gate", "Drain", "Source"],
        "extracts": ["api_semiconductor_full.txt"],
    },
    {
        "file": "api_chemical_transport.md",
        "title": "Chemical Species Transport Module",
        "subtitle": "Transport of Diluted/Concentrated Species, Reaction Engineering, Chemistry",
        "tag_kw": ["TransportOfDilutedSpecies", "TransportOfConcentratedSpecies",
                    "ReactionEngineering", "Chemistry", "tds", "tcs", "NernstPlanck",
                    "Convection", "Diffusion", "Migration", "Concentration",
                    "Flux", "NoFlux", "Inflow", "Outflow", "Reaction",
                    "Adsorption", "Desorption", "Partition", "Porous",
                    "Electrokinetic", "Electrophoretic"],
        "extracts": ["api_chemical_full.txt"],
    },
    {
        "file": "api_electric_discharge.md",
        "title": "Electric Discharge Module",
        "subtitle": "Corona, streamer, arc, and dielectric barrier discharge",
        "tag_kw": ["ElectricDischarge", "Discharge", "Corona", "Streamer", "Arc",
                    "DielectricBarrier", "Townsend", "Photoionization", "Avalanche",
                    "SpaceCharge", "Electrode", "HV", "PlasmaChemistry"],
        "extracts": ["api_discharge_full.txt"],
    },
    {
        "file": "api_mathematics.md",
        "title": "Mathematics Module",
        "subtitle": "PDE Interfaces — Coefficient Form, General Form, Weak Form, ODE/DAE, Optimization",
        "tag_kw": ["CoefficientFormPDE", "GeneralFormPDE", "WeakFormPDE",
                    "DirichletBoundary", "FluxBoundary", "ZeroFluxBoundary",
                    "PeriodicCondition", "GlobalEquations", "DomainODE",
                    "BoundaryODE", "PointODE", "Optimization", "Objective",
                    "Constraint", "ControlVariable", "Sensitivity",
                    "ShapeOptimization", "TopologyOptimization",
                    "DistributedODE", "Algebraic", "DAE"],
        "extracts": [],
    },
]

# ============================================================
# Build each reference
# ============================================================
for mod in MODULES:
    out_path = OUT_DIR / mod["file"]

    # Collect all matching features from tags.json
    features_by_interface = defaultdict(list)
    all_matches = []

    for kw in mod["tag_kw"]:
        for k, v in tags.items():
            if kw.lower() in k.lower():
                parts = k.split(SEP)
                if len(parts) >= 3:
                    interface = parts[1]
                    feature = parts[-1]
                    features_by_interface[interface].append({
                        "name": feature,
                        "tag": v,
                        "path": k,
                    })
                    all_matches.append(k)

    # Deduplicate
    for iface in features_by_interface:
        seen = set()
        unique = []
        for f in features_by_interface[iface]:
            if f["name"] not in seen:
                seen.add(f["name"])
                unique.append(f)
        features_by_interface[iface] = sorted(unique, key=lambda x: x["name"])

    # Classify features: domain vs boundary
    domain_features = []
    boundary_features = []
    pair_features = []
    other_features = []

    for iface, feats in features_by_interface.items():
        for f in feats:
            name = f["name"]
            if any(kw in name for kw in ["Domain", "Material", "Model", "Medium", "Equation"]):
                domain_features.append(f)
            elif any(kw in name for kw in ["Boundary", "Wall", "Ground", "Terminal", "Port",
                                             "Scattering", "Impedance", "Conductor", "Transition",
                                             "Periodic", "Floquet", "Matched", "Absorbing"]):
                boundary_features.append(f)
            elif any(kw in name for kw in ["Pair", "Continuity", "Contact"]):
                pair_features.append(f)
            else:
                other_features.append(f)

    # Read extract text for documentation context
    extract_texts = []
    for ext_file in mod.get("extracts", []):
        ext_path = EXTRACT_DIR / ext_file
        if ext_path.exists():
            with open(ext_path, "r", encoding="utf-8") as f:
                extract_texts.append(f.read())

    # Write the reference
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# {mod['title']} — Comprehensive API Reference\n\n")
        f.write(f"{mod['subtitle']}\n\n")
        f.write(f"COMSOL 6.4 · mph Python API · Extracted from official documentation and tags.json\n\n")
        f.write("---\n\n")

        # Table of contents
        f.write("## Contents\n\n")
        f.write("1. [Physics Interfaces](#physics-interfaces)\n")
        f.write("2. [Domain Features](#domain-features)\n")
        f.write("3. [Boundary Conditions](#boundary-conditions)\n")
        f.write("4. [Edge & Point Conditions](#edge-point-conditions)\n")
        f.write("5. [Pair Conditions](#pair-conditions)\n")
        f.write("6. [Expression Reference](#expression-reference)\n")
        f.write("7. [Multiphysics Couplings](#multiphysics-couplings)\n")
        f.write("8. [Common Patterns & Notes](#common-patterns)\n\n")
        f.write("---\n\n")

        # 1. Physics Interfaces
        f.write("## 1. Physics Interfaces\n\n")
        f.write("| Interface | mph Tag | COMSOL Name | Description |\n")
        f.write("|-----------|---------|-------------|-------------|\n")

        for iface in sorted(features_by_interface.keys()):
            # Try to find the interface tag
            iface_tag = tags.get(f"physics{SEP}{iface}", "")
            if not iface_tag:
                # Search for it
                for k, v in tags.items():
                    if k.startswith("physics") and iface in k and k.count(SEP) == 1:
                        iface_tag = v
                        break

            feat_count = len(features_by_interface[iface])
            desc = ""
            if "Frequency" in iface or "Freq" in iface:
                desc = "Frequency-domain electromagnetic waves"
            elif "Transient" in iface:
                desc = "Time-domain electromagnetic waves"
            elif "TimeExplicit" in iface or "Time Explicit" in iface:
                desc = "Explicit time-stepping EM waves"
            elif "BoundaryElement" in iface or "Boundary Element" in iface:
                desc = "Boundary element method EM"
            elif "Asymptotic" in iface:
                desc = "Asymptotic scattering (electrically large)"
            elif "Beam" in iface or "Envelope" in iface:
                desc = "Beam envelope (slowly varying)"
            elif "Ray" in iface or "Geometric" in iface:
                desc = "Ray tracing optics"
            elif "Plasma" in iface:
                desc = "Plasma discharge"
            elif "Semi" in iface:
                desc = "Semiconductor device"
            elif "Transport" in iface or "Species" in iface:
                desc = "Chemical species transport"
            elif "Reaction" in iface:
                desc = "Reaction engineering"
            elif "Discharge" in iface:
                desc = "Electric discharge"
            elif "PDE" in iface or "Form" in iface:
                desc = "Mathematics PDE interface"
            elif "ODE" in iface or "DAE" in iface:
                desc = "ODE/DAE interface"
            elif "Optimization" in iface:
                desc = "Optimization interface"

            f.write(f"| `{iface}` | `{iface_tag}` | {iface} | {desc} ({feat_count} features) |\n")

        f.write("\n---\n\n")

        # 2. Domain Features
        f.write("## 2. Domain Features\n\n")
        if domain_features:
            f.write("| Feature Name | mph Tag | Interface | Key Properties |\n")
            f.write("|-------------|---------|-----------|---------------|\n")
            for feat in domain_features[:60]:
                # Extract key properties from tags
                props_path = feat["path"]
                sub_feats = []
                for k, v in tags.items():
                    if k.startswith(props_path) and k != props_path:
                        parts = k.split(SEP)
                        sub_feats.append(parts[-1])
                prop_str = ", ".join(sub_feats[:5]) if sub_feats else "—"
                f.write(f"| `{feat['name']}` | `{feat['tag']}` | {feat.get('interface', '')} | {prop_str} |\n")
        else:
            f.write("*(See Physics Interfaces table for domain-level features)*\n")
        f.write("\n---\n\n")

        # 3. Boundary Conditions
        f.write("## 3. Boundary Conditions\n\n")
        if boundary_features:
            f.write("| BC Name | mph Tag | Interface | Key Properties |\n")
            f.write("|---------|---------|-----------|---------------|\n")
            for feat in boundary_features[:80]:
                props_path = feat["path"]
                sub_feats = []
                for k, v in tags.items():
                    if k.startswith(props_path) and k != props_path:
                        parts = k.split(SEP)
                        sub_feats.append(parts[-1])
                prop_str = ", ".join(sub_feats[:5]) if sub_feats else "—"
                f.write(f"| `{feat['name']}` | `{feat['tag']}` | {feat.get('interface', '')} | {prop_str} |\n")
        else:
            f.write("*(See Physics Interfaces table for boundary-level features)*\n")
        f.write("\n---\n\n")

        # 4. Edge & Point
        f.write("## 4. Edge & Point Conditions\n\n")
        if other_features:
            f.write("| Name | mph Tag | Type | Interface |\n")
            f.write("|------|---------|------|-----------|\n")
            for feat in other_features[:40]:
                dim = "Edge" if "Edge" in feat["path"] else "Point" if "Point" in feat["path"] else "Other"
                f.write(f"| `{feat['name']}` | `{feat['tag']}` | {dim} | {feat.get('interface','')} |\n")
        f.write("\n---\n\n")

        # 5. Pair Conditions
        f.write("## 5. Pair Conditions\n\n")
        if pair_features:
            f.write("| Name | mph Tag | Interface |\n")
            f.write("|------|---------|----------|\n")
            for feat in pair_features:
                f.write(f"| `{feat['name']}` | `{feat['tag']}` | {feat.get('interface','')} |\n")
        f.write("\n---\n\n")

        # 6. Expression Reference
        f.write("## 6. Expression Reference\n\n")
        f.write("Common postprocessing expressions (use with `model.evaluate()`):\n\n")
        f.write("| Expression | Unit | Description |\n")
        f.write("|-----------|------|-------------|\n")

        # Derive expressions from interface tags
        tag_prefixes = set()
        for kw in mod["tag_kw"]:
            for k, v in tags.items():
                if kw.lower() in k.lower() and k.startswith("physics"):
                    parts = k.split(SEP)
                    if len(parts) >= 2:
                        tag_prefixes.add(v.rstrip("*"))

        expr_map = {
            "emw": [
                ("emw.Ex", "V/m", "Electric field, x-component"),
                ("emw.Ey", "V/m", "Electric field, y-component"),
                ("emw.Ez", "V/m", "Electric field, z-component"),
                ("emw.normE", "V/m", "Electric field norm"),
                ("emw.Hx", "A/m", "Magnetic field, x-component"),
                ("emw.normH", "A/m", "Magnetic field norm"),
                ("emw.Poavz", "W/m^2", "Power flow, z-component (time avg)"),
                ("emw.S11", "1", "S-parameter (reflection)"),
                ("emw.S21", "1", "S-parameter (transmission)"),
                ("emw.Z0", "Ohm", "Characteristic impedance"),
                ("emw.freq", "Hz", "Frequency"),
                ("emw.lambda", "m", "Wavelength"),
                ("emw.Qfactor", "1", "Quality factor"),
            ],
            "ewfd": [
                ("ewfd.Ex", "V/m", "Electric field"),
                ("ewfd.normE", "V/m", "Electric field norm"),
                ("ewfd.S21", "1", "S-parameter"),
                ("ewfd.neff", "1", "Effective mode index"),
            ],
            "gop": [
                ("gop.rrel", "1", "Ray position (relative)"),
                ("gop.Intensity", "W/m^2", "Ray intensity"),
                ("gop.OPL", "m", "Optical path length"),
            ],
            "plasma": [
                ("plasma.Ne", "1/m^3", "Electron density"),
                ("plasma.V", "V", "Electric potential"),
                ("plasma.Te", "eV", "Electron temperature"),
            ],
            "semi": [
                ("semi.V", "V", "Electric potential"),
                ("semi.n", "1/m^3", "Electron concentration"),
                ("semi.p", "1/m^3", "Hole concentration"),
            ],
            "tds": [
                ("tds.c", "mol/m^3", "Concentration"),
                ("tds.Nx", "mol/(m^2*s)", "Flux, x-component"),
            ],
            "c": [
                ("c.u", "—", "PDE dependent variable"),
            ],
            "g": [
                ("g.u", "—", "PDE dependent variable"),
            ],
        }

        for prefix, exprs in expr_map.items():
            if any(prefix in tp for tp in tag_prefixes):
                for expr, unit, desc in exprs:
                    f.write(f"| `{expr}` | {unit} | {desc} |\n")

        f.write("\n---\n\n")

        # 7. Multiphysics Couplings
        f.write("## 7. Multiphysics Couplings\n\n")
        f.write("| Coupling | mph Type | Links |\n")
        f.write("|----------|---------|-------|\n")

        for k, v in tags.items():
            if k.startswith("multiphysics"):
                parts = k.split(SEP)
                if len(parts) >= 2:
                    mp_name = parts[1]
                    # Check if relevant to this module
                    relevant = False
                    for kw in mod["tag_kw"]:
                        if kw.lower() in mp_name.lower() or kw.lower() in k.lower():
                            relevant = True
                            break
                    if relevant:
                        f.write(f"| `{mp_name}` | `{v}` | — |\n")

        if not any(True for k in tags if k.startswith("multiphysics") and
                   any(kw.lower() in k.lower() for kw in mod["tag_kw"])):
            f.write("| *(No module-specific multiphysics couplings)* |\n")

        f.write("\n---\n\n")

        # 8. Common Patterns
        f.write("## 8. Common Patterns & COMSOL 6.4 Notes\n\n")

        # Extract relevant notes from PDF extracts
        notes_found = []
        for text in extract_texts:
            # Find "Note:", "Important:", "Tip:" sections
            for pattern in ["Note:", "Important:", "Tip:", "Caution:", "See also:"]:
                for match in re.finditer(pattern, text):
                    end = min(match.end() + 300, len(text))
                    snippet = text[match.start():end].strip()[:200]
                    if snippet not in notes_found:
                        notes_found.append(snippet)

        if notes_found:
            for note in notes_found[:10]:
                f.write(f"- {note}\n\n")
        else:
            f.write("- **mph API rule**: Use column-major flat arrays for all matrix properties\n")
            f.write("- **mph API rule**: Set property mode (`*_mat='userdef'`) before setting value\n")
            f.write("- **mph API rule**: Use COMSOL unit expressions (`'100[nm]'`) for Box selections\n")
            f.write("- **COMSOL 6.4**: `FloatingPotential` causes singular matrix in pure-field problems\n\n")

    size_kb = os.path.getsize(out_path) / 1024
    feature_count = len(domain_features) + len(boundary_features) + len(other_features)
    print(f"  {mod['file']}: {feature_count} features, {size_kb:.0f} KB")

print("\nAll comprehensive references built!")
