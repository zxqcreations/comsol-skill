# COMSOL Simulation Skill

Full-lifecycle automation for COMSOL Multiphysics simulations via mph Python API and COMSOL MCP.
Covers: research → planning → modeling → simulation → parameter sweep → data extraction → processing → visualization.

## When to Use

Trigger when the user requests:
- Building a new COMSOL model (any physics)
- Parameter sweeps or optimization studies
- Extracting and plotting COMSOL results
- Debugging COMSOL model issues
- Setting up multiphysics simulations (piezoelectric, thermal-stress, etc.)

## Core Architecture

### Tool Selection Strategy

| Operation | Preferred Tool | Reason |
|-----------|---------------|--------|
| Start COMSOL session | `mph.start(cores=N)` | Reliable across versions |
| Create/load model | `mph.Client().create()/load()` | Standard workflow |
| Set parameters | `model.java.param().set()` | Direct, reliable |
| Build geometry | `model.java.component().geom()` | Full control over features |
| Set physics | `model.java.component().physics()` | Access to all feature types |
| Piezo/custom materials | `pmat.set(name, col_major_array)` | setIndex fails in 6.4 |
| Mesh | `model.java.component().mesh()` | Domain-specific sizing |
| Study creation | `jm.study().create()` | Java API |
| Solve | `model.solve()` (mph) or `study.run()` | Use mph to avoid dataset issues |
| Evaluate results | `model.evaluate(expr, unit)` | mph evaluate works after mph solve |
| Export data/images | `jm.result().export()` or MCP | Both work |

## Critical API Rules

### Matrix Properties: Column-Major Flat Arrays

```python
# COMSOL's set(name, array) reads in COLUMN-MAJOR (Fortran) order
# For MxN matrix: array[col*M + row] = matrix[row][col]

# WRONG (row-major — all entries misplaced):
pmat.set('dET', ['0','0','0','0','564[pC/N]','0', ...])  # Row-major!

# CORRECT (column-major):
_DET_4MM = [
    # col xx:             col yy:              col zz:          col yz:          col xz:           col xy:
    '0','0','-33.4[pC/N]','0','0','-33.4[pC/N]','0','0','90[pC/N]','0','564[pC/N]','0','564[pC/N]','0','0','0','0','0',
]
pmat.set('dET_mat', 'userdef')
pmat.set('dET', _DET_4MM)
```

### Scalar Properties: Set Mode Before Value

```python
# rho, E, nu etc. — MUST set *_mat='userdef' FIRST, or value is silently ignored
pmat.set('rho_mat', 'userdef')  # ← CRITICAL: set mode first
pmat.set('rho', 'rho_material')  # ← Now this takes effect
```

### COMSOL Unit Expressions in Geometry

```python
# Geometry has lengthUnit('nm'), so Box selections MUST use unit expressions:
sel.set('xmin', 'R_rve/2')           # Parameter name ✅
sel.set('ymin', '100[nm]')           # Unit string ✅
sel.set('xmax', str(float_value))    # Raw float ❌ (interpreted as meters, not nm!)
```

### Correct Feature Type Names (COMSOL 6.4)

| Purpose | Correct Type | Wrong Type |
|---------|-------------|------------|
| Linear elastic domain | `LinearElasticModel` | `LinearElasticMaterial` |
| Prescribed displacement BC | `Displacement1` | `Displacement`, `PrescribedDisplacement` |
| Piezo material model | `PiezoelectricMaterialModel` | — |
| Fixed constraint | `Fixed` | `FixedConstraint` |

### Correct Property Names (strain-charge piezo)

| Purpose | Correct Name | Wrong Name |
|---------|-------------|------------|
| Constitutive relation | `ConstitutiveRelation` = `'StrainCharge'` | `'constitutiverelation'`, `'straincharge'` |
| Coupling matrix (d) | `dET` (mode: `dET_mat`) | `dET` with setIndex |
| Compliance matrix | `sE` (mode: `sE_mat`) | `cE` for strain-charge |
| Permittivity | `epsilonrS` (mode: `epsilonrS_mat`) | `epsS_mat`, `epsS11` |
| Density mode | `rho_mat = 'userdef'` | Direct `rho` set without mode |

## Diagnostic Strategy: PDF-First Troubleshooting

When ANY error or unexpected behavior occurs during modeling or simulation:

1. **DO NOT GUESS** — identify the exact error message or symptom
2. **CONSULT THE PDF** — search `D:\ENV\COMSOL64\Multiphysics\doc\pdf\<Module>\*UsersGuide.pdf` for:
   - The exact feature/property name causing the error
   - The equation or theory section explaining the physics
   - The reference section listing valid property values and feature types
3. **CROSS-REFERENCE with tags.json** — verify feature type names and property names match COMSOL 6.4
4. **APPLY the fix** — with verified API calls, not trial-and-error

**Most common diagnostic paths:**
- `setIndex fails with "not a scalar"` → PDF Reference section for that feature → use `set(name, flat_array)` instead
- `singular matrix` → PDF Theory section → check boundary conditions completeness
- `-Inf in results` → PDF Physics interface section → verify all required BCs present
- `feature creation fails` → `tags.json` search → verify exact feature type string
- `property silently ignored` → PDF feature settings section → check `*_mat='userdef'` requirement

**PDF locations for common lookups:**
| Issue Type | PDF to Search | Section |
|-----------|--------------|---------|
| Feature type names | `tags.json` in mph package | — |
| Property names for feature X | `<Module>UsersGuide.pdf` | "Reference" or "Settings" chapter |
| Material model parameters | `StructuralMechanicsModuleUsersGuide.pdf` | "Material Models" chapter |
| Solver settings | `COMSOL_Multiphysics/COMSOLMultiphysicsUsersGuide.pdf` | "Solvers" chapter |
| BC completeness | `<Module>UsersGuide.pdf` | Theory chapter for the physics interface |

## Standard Pipeline

```
01_design/          <- Research plan, parameter study, literature
02_build_model.py   <- Build mph model (geometry, physics, BCs, mesh, study)
03_baseline.py      <- Solve baseline, verify, extract key metrics
04_sweep.py         <- Multi-phase parameter sweep with CSV output
05_extract.py       <- Unit conversion, structured data export
06_process.py       <- Fitting, statistics, derived quantities
07_plot.py          <- Publication-quality figures (PDF+PNG)
```

## Web Dashboard Integration

The pipeline includes a dynamic web dashboard (`web/index.html`) for real-time monitoring:

**Workflow**:
1. At pipeline start, copy `web/index.html` to the project's output directory and open it
2. Each pipeline step writes progress to `pipeline_state.json` in the project directory
3. The dashboard polls this file every 2-3 seconds and updates automatically
4. Errors appear in red on the Log tab immediately; GUI check steps display in a highlighted panel

**What to update in the dashboard per project**:
- Model name and description in the sidebar
- Parameter tables (replace example values with actual project parameters)
- 3D model geometry (adjust Three.js scene to match the project's RVE/geometry)
- Document links in the Documents tab (point to actual project .md files)

**State file format** (`pipeline_state.json`, written by each pipeline script):

```json
{
  "stage": "03_baseline",
  "status": "running",
  "stages": {
    "01_design": "done",
    "02_build": "done",
    "03_baseline": "running",
    "04_sweep": "pending",
    "05_extract": "pending",
    "06_process": "pending",
    "07_plot": "pending"
  },
  "metrics": {"V_max": "28.35 V", "mesh_elements": 1502},
  "log": [
    {"time": "09:10:33", "msg": "Model build complete", "level": "success"},
    {"time": "09:15:00", "msg": "Singular matrix - check BCs", "level": "error"}
  ],
  "documents": [
    {"name": "01_research_plan.md", "path": "01_research_plan.md", "desc": "Research objectives and pipeline design"},
    {"name": "config.py", "path": "config.py", "desc": "Complete parameter definitions"}
  ],
  "gui_checklist": [
    "Verify d-matrix in Piezoelectric Material node",
    "Check Ground on correct boundary (z=0)"
  ]
}
```

**When GUI manual check is required**: Set `"status": "gui_check"` and populate `gui_checklist`. The dashboard will display a yellow alert panel with the checklist items.

## Troubleshooting Quick Reference

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `es.V = -Inf` | No ground reference in ES domain | Add Ground, ensure domain in ES |
| `solid.mises = 0` | Material stiffness not applied | Check E/nu are User defined, not From material |
| Matrix entries wrong in GUI | Row-major array passed | Use column-major flat array |
| Mesh 0 elements | Semcircle/Boolean Diff geometry | Use full circles + domain exclusion |
| "not a scalar" error | setIndex with string expr | Use set(name, flat_array) |
| Study not found by mph | Java API created study | Use mph model.solve() not Java study.run() |
| Singular matrix | FloatingPotential in piezo-ES | Remove FP, use Zero Charge |

## References

- `references/mph_api.md` — Complete mph Python API reference for COMSOL 6.4
- `references/mcp_tools.md` — COMSOL MCP tools reference
- `references/lessons_learned.md` — All lessons from real multiphysics RVE model builds
- `references/troubleshooting.md` — Common issues, symptoms, root causes, and fixes
- `references/tags_physics.md` — **2021 physics feature types** (all interfaces)
- `references/tags_geometries.md` — **293 geometry features** with tags
- `references/tags_multiphysics.md` — **69 multiphysics coupling types**
- `references/tags_meshes.md` — **46 mesh feature types**
- `references/tags_studies.md` — **57 study/solver types**
- `references/tags_materials.md` — Material types and property groups
- `references/tags_selections.md` — Selection types
- `references/tags_functions.md` — Function types
- `references/tags_batches.md` — Batch/sweep types
- `references/api_core.md` — **COMSOL core API**: Geometry, Mesh, Studies, Results (from official docs)
- `references/api_structural.md` — **Structural Mechanics**: Solid, Piezo, Shell, Beam, Multibody
- `references/api_acdc.md` — **AC/DC Module**: Electrostatics, Currents, Magnetic Fields
- `references/api_heat_transfer.md` — **Heat Transfer**: Conduction, Convection, Radiation
- `references/api_fluid_flow.md` — **Fluid Flow (CFD)**: Laminar, Turbulent, Creeping
- `references/api_echem.md` — **Electrochemistry**: Current Distribution, Butler-Volmer
- `references/api_acoustics_mems.md` — **Acoustics + MEMS**: Pressure Acoustics, Couplings
- `references/mcp_tools.md` — **COMSOL MCP tools**: Session, geometry, physics, results, docs
- `mcp_server/` — **Full COMSOL MCP server** (Python, runs alongside mph)

## Module Coverage (13/13 Complete)

| # | Module | Reference | Quality |
|---|--------|-----------|--------|
| 1 | AC/DC | `references/api_acdc.md` | Workflow-generated |
| 2 | Acoustics + MEMS | `references/api_acoustics_mems.md` | Workflow-generated |
| 3 | Chemical Species Transport | `references/api_chemical_transport.md` | Hand-written |
| 4 | Electric Discharge | `references/api_electric_discharge.md` | Hand-written |
| 5 | Electrochemistry | `references/api_echem.md` | Workflow-generated |
| 6 | Fluid Flow | `references/api_fluid_flow.md` | Workflow-generated |
| 7 | Heat Transfer | `references/api_heat_transfer.md` | Workflow-generated |
| 8 | Optics (Ray + Wave) | `references/api_optics.md` | Hand-written |
| 9 | Plasma | `references/api_plasma.md` | Hand-written |
| 10 | Radio Frequency | `references/api_rf.md` | Hand-written |
| 11 | Semiconductor | `references/api_semiconductor.md` | Hand-written |
| 12 | Structural Mechanics | `references/api_structural.md` | Workflow-generated |
| 13 | Mathematics (PDE/ODE) | `references/api_mathematics.md` | Hand-written |
| — | COMSOL Core | `references/api_core.md` | Workflow-generated |

**7 hand-written + 7 workflow-generated = 14 files. All audited with 0 remaining issues.**
