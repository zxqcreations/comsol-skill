# COMSOL Simulation Skill

Full-lifecycle COMSOL Multiphysics automation skill for Claude Code. Covers all 13 COMSOL physics modules with complete API references, debugging guides, and a web dashboard.

## Features

- **13 physics modules** fully documented — AC/DC, Acoustics, Chemical Transport, Electrochemistry, Fluid Flow, Heat Transfer, Optics, Plasma, RF, Semiconductor, Structural Mechanics, Electric Discharge, Mathematics (PDE/ODE)
- **mph Python API reference** — Complete session management, geometry, physics, materials, mesh, study, solve, and result extraction
- **Diagnostic strategy** — PDF-first troubleshooting: never guess, always consult the official docs
- **Pipeline dashboard** — Web UI with Three.js 3D RVE model preview and progress tracking
- **2,500+ feature type tags** — Machine-extracted from mph tags.json, organized by category

## Structure

```
comsol-skill/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file
├── .gitignore
├── mcp_server/                       # COMSOL MCP server (Python)
│   └── src/tools/                    # geometry, mesh, model, physics, results, session, study
├── web/
│   └── index.html                    # Three.js dashboard with 3D model preview
├── scripts/
│   ├── extract_tags.py               # Extract feature types from mph tags.json
│   ├── build_api_refs.py             # Build API references from PDF extracts + tags
│   ├── audit_quality.py              # Audit reference file completeness
│   ├── final_audit.py                # Cross-reference against tags.json ground truth
│   └── fix_audit_issues.py           # Apply audit fixes automatically
└── references/
    ├── mph_api.md                    # Complete mph Python API (COMSOL 6.4)
    ├── lessons_learned.md            # All lessons from real RVE model builds
    ├── troubleshooting.md            # Symptoms -> causes -> fixes
    ├── tags_physics.md               # 2,021 physics feature types
    ├── tags_geometries.md            # 293 geometry features
    ├── tags_multiphysics.md           # 69 multiphysics coupling types
    ├── tags_meshes.md                # 46 mesh feature types
    ├── tags_studies.md               # 57 study/solver types
    ├── tags_materials.md             # Material types
    ├── tags_selections.md            # Selection types
    ├── tags_functions.md             # Function types
    ├── tags_batches.md               # Batch/sweep types
    ├── api_core.md                   # Core API: Geometry, Mesh, Studies, Results
    ├── api_acdc.md                   # AC/DC Module
    ├── api_acoustics_mems.md         # Acoustics + MEMS
    ├── api_chemical_transport.md     # Chemical Species Transport
    ├── api_echem.md                  # Electrochemistry
    ├── api_electric_discharge.md     # Electric Discharge
    ├── api_fluid_flow.md             # Fluid Flow (CFD)
    ├── api_heat_transfer.md          # Heat Transfer
    ├── api_mathematics.md            # Mathematics (PDE/ODE)
    ├── api_optics.md                 # Optics (Ray + Wave)
    ├── api_plasma.md                 # Plasma
    ├── api_rf.md                     # Radio Frequency
    ├── api_semiconductor.md          # Semiconductor
    └── api_structural.md             # Structural Mechanics
```

## Module Coverage (14 files, all audited)

| # | Module | Quality |
|---|--------|---------|
| 1 | AC/DC | Workflow-generated |
| 2 | Acoustics + MEMS | Workflow-generated |
| 3 | Chemical Species Transport | Hand-written |
| 4 | Electric Discharge | Hand-written |
| 5 | Electrochemistry | Workflow-generated |
| 6 | Fluid Flow | Workflow-generated |
| 7 | Heat Transfer | Workflow-generated |
| 8 | Optics (Ray + Wave) | Hand-written |
| 9 | Plasma | Hand-written |
| 10 | Radio Frequency | Hand-written |
| 11 | Semiconductor | Hand-written |
| 12 | Structural Mechanics | Workflow-generated |
| 13 | Mathematics (PDE/ODE) | Hand-written |
| — | COMSOL Core | Workflow-generated |

## Key API Rules

- **Column-major arrays**: `pmat.set('dET', flat_array)` reads in Fortran order. `setIndex` fails for matrix entries in COMSOL 6.4.
- **Mode before value**: `pmat.set('rho_mat', 'userdef')` MUST come before `pmat.set('rho', value)`, or the value is silently ignored.
- **Unit expressions**: Box selections with `lengthUnit('nm')` require `'100[nm]'` expressions, never raw floats.
- **Feature names**: `LinearElasticModel` (not `LinearElasticMaterial`), `Displacement1` (not `Displacement`), `PiezoelectricMaterialModel`.
- **No FloatingPotential in piezo-ES**: Causes singular matrix. Use Zero Charge + Ground.
- **mph `model.solve()` rebuilds geometry**: Use `jm.study('std1').run()` to preserve GUI fixes.
- **`model.evaluate('r')` returns lengthUnit values**: If `lengthUnit('nm')`, r and z are already in nm — don't multiply by 1e9 again.

## Built From

- Real MXene/BaTiO3 piezoelectric RVE simulation project (Scheme 1)
- COMSOL 6.4 PDF documentation (~50 module directories)
- mph 1.3.1 source code and tags.json (3,281 entries)
- Zgonik et al. (1994) — BaTiO3 constants
- Rong et al. (2024) — MXene mechanical properties
