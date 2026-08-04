# COMSOL Simulation Skill

Full-lifecycle COMSOL Multiphysics automation skill for Claude Code.

## Features

- **Automated model building** — Multiphysics models via mph Python API
- **Parameter sweeps** — Multi-phase sweep execution with CSV output
- **Result extraction** — Automated evaluation and data export
- **Pipeline dashboard** — Web-based monitoring with 3D model preview (Three.js)
- **Comprehensive troubleshooting** — Documented solutions for common COMSOL issues

## Structure

```
comsol-skill/
├── SKILL.md              # Main skill definition
├── README.md             # This file
├── references/           # API and troubleshooting references
│   ├── mph_api.md        # Complete mph Python API for COMSOL 6.4
│   ├── lessons_learned.md # All lessons from real model builds
│   └── troubleshooting.md # Common issues and fixes
├── web/
│   └── index.html        # Pipeline dashboard with Three.js 3D preview
├── scripts/              # Reusable pipeline script templates
└── assets/               # 3D models and static assets
```

## Key API Rules

- **Column-major arrays**: `pmat.set('dET', flat_array)` reads in Fortran order
- **Mode before value**: `pmat.set('rho_mat', 'userdef')` before `pmat.set('rho', value)`
- **Unit expressions**: Box selections need `'100[nm]'`, not raw floats
- **Feature names**: `LinearElasticModel`, `Displacement1`, `PiezoelectricMaterialModel`

## References

- Built from real experience with MXene/BaTiO3 piezoelectric RVE models
- COMSOL 6.4 + mph Python API
- Zgonik et al. (1994) — BaTiO3 material constants
- Rong et al. (2024) — MXene mechanical properties
