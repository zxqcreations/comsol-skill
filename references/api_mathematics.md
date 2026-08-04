# Mathematics Module — Comprehensive API Reference

PDE Interfaces — Coefficient Form, General Form, Weak Form, ODE/DAE, Optimization

COMSOL 6.4 · mph Python API · Extracted from official documentation and tags.json

---

## Contents

1. [Physics Interfaces](#physics-interfaces)
2. [Domain Features](#domain-features)
3. [Boundary Conditions](#boundary-conditions)
4. [Edge & Point Conditions](#edge-point-conditions)
5. [Pair Conditions](#pair-conditions)
6. [Expression Reference](#expression-reference)
7. [Multiphysics Couplings](#multiphysics-couplings)
8. [Common Patterns & Notes](#common-patterns)

---

## 1. Physics Interfaces

| Interface | mph Tag | COMSOL Name | Description |
|-----------|---------|-------------|-------------|
| `?` | `` | ? |  (4 features) |
| `BoundaryODE` | `bode` | BoundaryODE | ODE/DAE interface (2 features) |
| `Brinkman` | `br` | Brinkman |  (1 features) |
| `BubblyFlowkeps` | `bf` | BubblyFlowkeps |  (1 features) |
| `Circuit` | `cir` | Circuit |  (1 features) |
| `CoefficientFormBoundaryPDE` | `cb` | CoefficientFormBoundaryPDE | Mathematics PDE interface (2 features) |
| `CoefficientFormPDE` | `c` | CoefficientFormPDE | Mathematics PDE interface (5 features) |
| `ConvectionDiffusionEquation` | `cdeq` | ConvectionDiffusionEquation |  (2 features) |
| `DarcysLaw` | `dl` | DarcysLaw |  (1 features) |
| `DilutedSpecies` | `tds` | DilutedSpecies | Chemical species transport (1 features) |
| `DomainODE` | `dode` | DomainODE | ODE/DAE interface (2 features) |
| `EdgeODE` | `eode` | EdgeODE | ODE/DAE interface (1 features) |
| `ElectromagneticWaves` | `emw` | ElectromagneticWaves |  (1 features) |
| `ElectromagneticWavesBeamEnvelopes` | `ewbe` | ElectromagneticWavesBeamEnvelopes | Beam envelope (slowly varying) (1 features) |
| `ElectromagneticWavesFrequencyDomain` | `ewfd` | ElectromagneticWavesFrequencyDomain | Frequency-domain electromagnetic waves (2 features) |
| `ElectromagneticWavesTransient` | `ewt` | ElectromagneticWavesTransient | Time-domain electromagnetic waves (2 features) |
| `Electrostatics` | `es` | Electrostatics |  (2 features) |
| `GeneralFormBoundaryPDE` | `gb` | GeneralFormBoundaryPDE | Mathematics PDE interface (1 features) |
| `GeneralFormPDE` | `g` | GeneralFormPDE | Mathematics PDE interface (7 features) |
| `GeneralOptimization` | `opt` | GeneralOptimization | Optimization interface (10 features) |
| `GeometricalOptics` | `gop` | GeometricalOptics | Ray tracing optics (1 features) |
| `GlobalEquations` | `ge` | GlobalEquations |  (1 features) |
| `HeatTransfer` | `ht` | HeatTransfer |  (3 features) |
| `HeatTransferInBuildingMaterials` | `ht` | HeatTransferInBuildingMaterials |  (1 features) |
| `HeatTransferInFluids` | `ht` | HeatTransferInFluids |  (1 features) |
| `HeatTransferInSolidsAndFluids` | `ht` | HeatTransferInSolidsAndFluids |  (2 features) |
| `HighMachNumberFlow` | `hmnf` | HighMachNumberFlow |  (1 features) |
| `InductionCurrents` | `mf` | InductionCurrents |  (1 features) |
| `LaminarFlow` | `spf` | LaminarFlow |  (3 features) |
| `LaplaceEquation` | `lpeq` | LaplaceEquation |  (3 features) |
| `LayeredShell` | `lshell` | LayeredShell |  (1 features) |
| `MultibodyDynamics` | `mbd` | MultibodyDynamics |  (3 features) |
| `Parametric` | `` | Parametric |  (17 features) |
| `PointODE` | `pode` | PointODE | ODE/DAE interface (2 features) |
| `PoroelasticWavesSinglePhysics` | `pelw` | PoroelasticWavesSinglePhysics |  (1 features) |
| `PorousMediaHeatTransfer` | `ht` | PorousMediaHeatTransfer |  (1 features) |
| `PressureAcoustics` | `acpr` | PressureAcoustics |  (1 features) |
| `RotatingMachineryMagnetic` | `rmm` | RotatingMachineryMagnetic |  (1 features) |
| `SchrodingerEquation` | `schr` | SchrodingerEquation |  (2 features) |
| `Semiconductor` | `semi` | Semiconductor | Semiconductor device (1 features) |
| `Sensitivity` | `sens` | Sensitivity |  (1 features) |
| `Shell` | `shell` | Shell |  (1 features) |
| `SlipFlow` | `slpf` | SlipFlow |  (1 features) |
| `SolidMechanics` | `solid` | SolidMechanics |  (4 features) |
| `Stationary` | `` | Stationary |  (19 features) |
| `StructuralMembrane` | `mbrn` | StructuralMembrane |  (1 features) |
| `TertiaryCurrentDistributionNernstPlanck` | `tcd` | TertiaryCurrentDistributionNernstPlanck |  (2 features) |
| `ThinFilmFlowShell` | `tffs` | ThinFilmFlowShell |  (1 features) |
| `Time` | `elte` | Time |  (6 features) |
| `Timeparametric` | `` | Timeparametric |  (6 features) |
| `TransientElectromagneticWaves` | `temw` | TransientElectromagneticWaves | Time-domain electromagnetic waves (1 features) |
| `Truss` | `truss` | Truss |  (1 features) |
| `TurbulentFlowAlgebraicYplus` | `spf` | TurbulentFlowAlgebraicYplus |  (19 features) |
| `TurbulentFlowkeps` | `spf` | TurbulentFlowkeps |  (2 features) |
| `TurbulentFlowkomega` | `spf` | TurbulentFlowkomega |  (1 features) |
| `WeakFormBoundaryPDE` | `wb` | WeakFormBoundaryPDE | Mathematics PDE interface (1 features) |

---

## 2. Domain Features

| Feature Name | mph Tag | Interface | Key Properties |
|-------------|---------|-----------|---------------|
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `DestinationDomains` | `dd*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |

---

## 3. Boundary Conditions

| BC Name | mph Tag | Interface | Key Properties |
|---------|---------|-----------|---------------|
| `DirichletBoundary` | `dir*` |  | — |
| `DirichletBoundary` | `dir*` |  | — |
| `FluxBoundary` | `flux*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `DirichletBoundary` | `dir*` |  | — |
| `FluxBoundary` | `flux*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `DirichletBoundary` | `dir*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `DirichletBoundary` | `dir*` |  | — |
| `FluxBoundary` | `flux*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `FluxBoundary` | `fl*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | DestinationDomains |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `InletBoundary` | `inl*` |  | — |
| `InteriorWallBC` | `iwbc*` |  | — |
| `OutletBoundary` | `out*` |  | — |
| `PeriodicFlowCondition` | `pfc*` |  | — |
| `Wall` | `wall*` |  | WallBC |
| `WallBC` | `wallbc*` |  | — |

---

## 4. Edge & Point Conditions

| Name | mph Tag | Type | Interface |
|------|---------|------|-----------|
| `CoefficientFormPDE` | `cfeq*` | Other |  |
| `CoefficientFormPDE` | `cfeq*` | Other |  |
| `init` | `init*` | Other |  |
| `GeneralFormPDE` | `gfeq*` | Other |  |
| `Constraint` | `cons*` | Other |  |
| `GeneralFormPDE` | `gfeq*` | Other |  |
| `init` | `init*` | Other |  |
| `WeakFormPDE` | `wfeq*` | Other |  |
| `PointwiseConstraint` | `constr*` | Point |  |
| `GlobalConstraint` | `gconstr*` | Other |  |
| `GlobalConstraint` | `gconstr*` | Other |  |
| `PointwiseConstraint` | `constr*` | Point |  |
| `PressurePointConstraint` | `prpc*` | Point |  |
| `Constraints` | `ct*` | Other |  |
| `FixedConstraint` | `fix*` | Other |  |
| `AxialSymmetry` | `axi*` | Other |  |
| `ExtFan` | `fan*` | Other |  |
| `FluidProperties` | `fp*` | Other |  |
| `Gravity` | `grav*` | Other |  |
| `Grille` | `grille*` | Other |  |
| `PressurePointConstraint` | `prpc*` | Point |  |
| `StationaryFreeSurface` | `sfs*` | Other |  |
| `Symmetry` | `sym*` | Other |  |
| `VolumeForce` | `vf*` | Other |  |
| `WeakContribution` | `weak*` | Other |  |
| `init` | `init*` | Other |  |
| `PressurePointConstraint` | `prpc*` | Point |  |
| `DistributedODE` | `dode*` | Other |  |
| `init` | `init*` | Other |  |
| `DistributedODE` | `dode*` | Other |  |
| `init` | `init*` | Other |  |
| `DistributedODE` | `dode*` | Point |  |
| `init` | `init*` | Point |  |
| `ControlVariableBounds` | `bound*` | Other |  |
| `ControlVariableField` | `cvar*` | Other |  |
| `CoordinateColumn` | `c*` | Other |  |
| `GlobalControlVariables` | `gcvar*` | Other |  |
| `GlobalLeastSquaresObjective` | `glsobj*` | Other |  |
| `GlobalObjective` | `gobj*` | Other |  |
| `IntegralInequality` | `iconstr*` | Other |  |

---

## 5. Pair Conditions

| Name | mph Tag | Interface |
|------|---------|----------|
| `ContactAngle` | `cnta*` |  |

---

## 6. Expression Reference

Common postprocessing expressions (use with `model.evaluate()`):

| Expression | Unit | Description |
|-----------|------|-------------|
| `c.u` | — | PDE dependent variable |
| `g.u` | — | PDE dependent variable |

---

## 7. Multiphysics Couplings

| Coupling | mph Type | Links |
|----------|---------|-------|
| *(No module-specific multiphysics couplings)* |

---

## 8. Common Patterns & COMSOL 6.4 Notes

- **mph API rule**: Use column-major flat arrays for all matrix properties
- **mph API rule**: Set property mode (`*_mat='userdef'`) before setting value
- **mph API rule**: Use COMSOL unit expressions (`'100[nm]'`) for Box selections
- **COMSOL 6.4**: `FloatingPotential` causes singular matrix in pure-field problems

