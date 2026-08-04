# Electric Discharge Module — Comprehensive API Reference

Corona, streamer, arc, and dielectric barrier discharge

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
| `CurrentDistributionBEM` | `cdbem` | CurrentDistributionBEM |  (2 features) |
| `CurrentDistributionShell` | `cdsh` | CurrentDistributionShell |  (2 features) |
| `CurvilinearCoordinates` | `cc` | CurvilinearCoordinates |  (5 features) |
| `DarcysLaw` | `dl` | DarcysLaw |  (21 features) |
| `DeformedGeometry` | `dg` | DeformedGeometry |  (2 features) |
| `DilutedSpecies` | `tds` | DilutedSpecies | Chemical species transport (2 features) |
| `ElectrodeShell` | `els` | ElectrodeShell |  (7 features) |
| `Electrostatics` | `es` | Electrostatics |  (1 features) |
| `PrimaryCurrentDistribution` | `cd` | PrimaryCurrentDistribution |  (3 features) |
| `SecondaryCurrentDistribution` | `cd` | SecondaryCurrentDistribution |  (8 features) |
| `TertiaryCurrentDistributionNernstPlanck` | `tcd` | TertiaryCurrentDistributionNernstPlanck |  (4 features) |
| `TertiaryElectroanalysis` | `tcd` | TertiaryElectroanalysis |  (3 features) |
| `curve` | `` | curve |  (1 features) |
| `empty` | `` | empty |  (1 features) |
| `mixed` | `` | mixed |  (1 features) |
| `solid` | `` | solid |  (1 features) |

---

## 2. Domain Features

| Feature Name | mph Tag | Interface | Key Properties |
|-------------|---------|-----------|---------------|
| `DarcysLawModel` | `dlm*` |  | — |
| `PoroelasticMaterial` | `psm*` |  | — |
| `StorageModel` | `smm*` |  | — |

---

## 3. Boundary Conditions

| BC Name | mph Tag | Interface | Key Properties |
|---------|---------|-----------|---------------|
| `WallDefault` | `wall*` |  | — |
| `BoundaryReactionCoefficients` | `rc*` |  | — |
| `Ground` | `gnd*` |  | — |

---

## 4. Edge & Point Conditions

| Name | mph Tag | Type | Interface |
|------|---------|------|-----------|
| `CircularArc` | `ca*` | Other |  |
| `CircularArc` | `ca*` | Other |  |
| `CircularArc` | `ca*` | Other |  |
| `CircularArc` | `ca*` | Other |  |
| `CoordinateSystemSettings` | `css*` | Other |  |
| `DiffusionMethod` | `diff*` | Other |  |
| `Inlet` | `inl*` | Other |  |
| `Outlet` | `out*` | Other |  |
| `Aperture` | `ap*` | Other |  |
| `AxialSymmetry` | `axi*` | Other |  |
| `FractureFlow` | `dfn*` | Other |  |
| `Gravity` | `gr*` | Other |  |
| `HydraulicHead` | `hh*` | Other |  |
| `Inlet` | `inl*` | Other |  |
| `LineMassSource` | `lms*` | Other |  |
| `MassFlux` | `mf*` | Other |  |
| `MassSource` | `ms*` | Other |  |
| `NoFlow` | `nf*` | Other |  |
| `Outlet` | `out*` | Other |  |
| `PointwiseConstraint` | `constr*` | Point |  |
| `Precipitation` | `prec*` | Other |  |
| `Pressure` | `pr*` | Other |  |
| `PressureHead` | `ph*` | Other |  |
| `Symmetry` | `sym*` | Other |  |
| `Well` | `well*` | Other |  |
| `init` | `init*` | Other |  |
| `SpaceChargeDensity` | `scd*` | Other |  |
| `EdgeElectrode` | `edge*` | Edge |  |
| `EdgeElectrodeReaction` | `er*` | Edge |  |
| `ElectrodeReaction` | `er*` | Other |  |
| `ExternalElectrodeSurface` | `eebii*` | Other |  |
| `ElectrodeElectrolyteInterfaceCoupling` | `eeic*` | Other |  |
| `AxialSymmetry` | `axi*` | Other |  |
| `DepositingElectrode` | `depe*` | Other |  |
| `ElectricInsulation` | `ein*` | Other |  |
| `Electrode` | `ece*` | Other |  |
| `NormalCurrentDensity` | `ncd*` | Other |  |
| `init` | `init*` | Other |  |
| `ElectrodeReaction` | `er*` | Other |  |
| `ElectrodeSurface` | `es*` | Other |  |

---

## 5. Pair Conditions


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
| `DeformingElectrodeSurface` | `des*` | — |
| `Electrode` | `el*` | — |
| `EquilibriumDischargeHeatSource` | `phs*` | — |
| `SpaceChargeDensityCoupling` | `scdc*` | — |
| `SpaceChargeLimitedEmission` | `scle*` | — |

---

## 8. Common Patterns & COMSOL 6.4 Notes

- Note: The state of the switch (on/off) is changed only when a condition goes from 
false to true and not when going from true to false. Thus, if the state is off and the on 
condition goes from false 

