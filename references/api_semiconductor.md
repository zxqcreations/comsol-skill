# Semiconductor Module — Comprehensive API Reference

Semiconductor physics — Drift-Diffusion, Density-Gradient, Schrodinger-Poisson

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
| `?` | `` | ? |  (5 features) |
| `BioHeat` | `ht` | BioHeat |  (1 features) |
| `ChargeTransport` | `ct` | ChargeTransport | Chemical species transport (1 features) |
| `Circuit` | `cir` | Circuit |  (5 features) |
| `ColdPlasma` | `plas` | ColdPlasma | Plasma discharge (3 features) |
| `ConcentratedSpecies` | `tcs` | ConcentratedSpecies | Chemical species transport (1 features) |
| `ConductiveMedia` | `ec` | ConductiveMedia |  (3 features) |
| `DarcysLaw` | `dl` | DarcysLaw |  (2 features) |
| `DilutedSpecies` | `tds` | DilutedSpecies | Chemical species transport (1 features) |
| `Eigenfrequency` | `` | Eigenfrequency |  (4 features) |
| `HeatTransfer` | `ht` | HeatTransfer |  (9 features) |
| `HeatTransferInFilmsLM` | `htlsh` | HeatTransferInFilmsLM |  (1 features) |
| `HeatTransferInFluids` | `ht` | HeatTransferInFluids |  (2 features) |
| `HeatTransferInSolidsAndFluids` | `ht` | HeatTransferInSolidsAndFluids |  (2 features) |
| `LaminarFlow` | `spf` | LaminarFlow |  (2 features) |
| `LaplaceEquation` | `lpeq` | LaplaceEquation |  (1 features) |
| `LumpedMechanicalSystem` | `lms` | LumpedMechanicalSystem |  (1 features) |
| `MultibodyDynamics` | `mbd` | MultibodyDynamics |  (13 features) |
| `Parametric` | `` | Parametric |  (6 features) |
| `PlasmaTimePeriodic` | `ptp` | PlasmaTimePeriodic | Plasma discharge (3 features) |
| `PlotGroup1D` | `` | PlotGroup1D |  (1 features) |
| `PorousMediaHeatTransfer` | `ht` | PorousMediaHeatTransfer |  (3 features) |
| `PressureAcoustics` | `acpr` | PressureAcoustics |  (3 features) |
| `ReactionEng` | `re` | ReactionEng | Reaction engineering (1 features) |
| `SecondaryCurrentDistribution` | `cd` | SecondaryCurrentDistribution |  (1 features) |
| `Semiconductor` | `semi` | Semiconductor | Semiconductor device (31 features) |
| `Shell` | `shell` | Shell |  (1 features) |
| `SolidMechanics` | `solid` | SolidMechanics |  (9 features) |
| `Stationary` | `` | Stationary |  (4 features) |
| `SurfaceToSurfaceRadiation` | `rad` | SurfaceToSurfaceRadiation |  (1 features) |
| `Time` | `elte` | Time |  (4 features) |
| `TransientPressureAcoustics` | `actd` | TransientPressureAcoustics | Time-domain electromagnetic waves (1 features) |
| `TurbulentFlowAlgebraicYplus` | `spf` | TurbulentFlowAlgebraicYplus |  (1 features) |
| `TurbulentFlowkeps` | `spf` | TurbulentFlowkeps |  (1 features) |

---

## 2. Domain Features

| Feature Name | mph Tag | Interface | Key Properties |
|-------------|---------|-----------|---------------|
| `AnalyticDopingModel` | `adm*` |  | — |
| `AroraMobilityModel` | `mmar*` |  | — |
| `CaugheyThomasMobilityModel` | `mmct*` |  | — |
| `FletcherMobilityModel` | `mmfl*` |  | — |
| `GeometricDopingModel` | `gdm*` |  | BoundarySelectionForDopingProfile |
| `GlobalEquations` | `ge*` |  | — |
| `LombardiSurfaceMobilityModel` | `mmls*` |  | — |
| `SemiconductorMaterialModel` | `smm*` |  | AroraMobilityModel, CaugheyThomasMobilityModel, FletcherMobilityModel, LombardiSurfaceMobilityModel |
| `WKBTunnelingModelElectrons` | `wkbe*` |  | — |
| `FrequencyDomainSourceSweep` | `fdss` |  | — |
| `IsothermalDomainInterface` | `idi*` |  | LayerOpacity |

---

## 3. Boundary Conditions

| BC Name | mph Tag | Interface | Key Properties |
|---------|---------|-----------|---------------|
| `BoundarySelectionForDopingProfile` | `gdmbs*` |  | — |
| `ContinuousEnergyLevelsBoundary` | `ctb*` |  | — |
| `DiscreteEnergyLevelBoundary` | `dtb*` |  | — |
| `OpticalTransitions` | `ot*` |  | — |
| `Terminal` | `term*` |  | — |
| `WallDriftDiffusion` | `wall*` |  | — |
| `WallDriftDiffusion` | `wall*` |  | — |
| `ContactImpedance` | `ci*` |  | — |
| `BoundaryHeatSource` | `bhs*` |  | — |
| `PairBoundaryHeatSource` | `pbhs*` |  | IsothermalDomainInterface, LayerOpacity, ThermalInsulation |
| `ThreadBoundarySelection` | `tbs*` |  | Free |
| `BoundaryHeatSource` | `bhs*` |  | — |
| `BoundaryHeatSource` | `bhs*` |  | — |

---

## 4. Edge & Point Conditions

| Name | mph Tag | Type | Interface |
|------|---------|------|-----------|
| `AURecombination` | `aur*` | Other |  |
| `AxialSymmetry` | `axi*` | Other |  |
| `ChargeConservation` | `ccn*` | Other |  |
| `FloatingGate` | `fg*` | Other |  |
| `HarmonicPerturbation` | `hp*` | Other |  |
| `IIGeneration` | `iig*` | Other |  |
| `Insulation` | `ins*` | Other |  |
| `InsulatorInterface` | `ii*` | Other |  |
| `SurfaceChargeDensity` | `sfcd*` | Other |  |
| `TrapAssistedRecombination` | `tar*` | Other |  |
| `TrapAssistedSurfaceRecombination` | `tasr*` | Other |  |
| `UDGeneration` | `udg*` | Other |  |
| `ZeroCharge` | `zc*` | Other |  |
| `init` | `init*` | Other |  |
| `SemiconductorEquilibrium` | `semie` | Other |  |
| `SemiconductorInitialization` | `semii` | Other |  |
| `SourceInitialization` | `init` | Other |  |
| `StationarySourceSweep` | `stssw` | Other |  |
| `OctaveBand` | `oct*` | Other |  |
| `ElectricInsulation` | `ein*` | Other |  |
| `HeatSource` | `hs*` | Other |  |
| `LayerOpacity` | `lopac*` | Other |  |
| `LineHeatSource` | `lihs*` | Other |  |
| `ThermalInsulation` | `ins*` | Other |  |
| `HeatSource` | `hs*` | Other |  |
| `MassSource` | `ms*` | Other |  |
| `DestinationPointBnd` | `dpb*` | Point |  |
| `DestinationPointEdge` | `dpe*` | Edge |  |
| `DestinationPointPoint` | `dpp*` | Point |  |
| `Free` | `free*` | Other |  |
| `Friction` | `fric*` | Other |  |
| `SourceFilter` | `srcf*` | Other |  |
| `SourcePoint` | `sp*` | Point |  |
| `SourcePointBnd` | `spb*` | Point |  |
| `SourcePointEdge` | `spe*` | Edge |  |
| `SourcePointPoint` | `spp*` | Point |  |
| `Adhesion` | `adh*` | Other |  |
| `Decohesion` | `dch*` | Other |  |
| `Free` | `free*` | Other |  |
| `Friction` | `fric*` | Other |  |

---

## 5. Pair Conditions

| Name | mph Tag | Interface |
|------|---------|----------|
| `Continuity` | `cont*` |  |
| `GateContact` | `gc*` |  |
| `MetalContact` | `mc*` |  |
| `DielectricContact` | `dct*` |  |
| `MetalContact` | `mct*` |  |
| `DielectricContact` | `dct*` |  |
| `MetalContact` | `mct*` |  |
| `PairElectricalContact` | `pelc*` |  |
| `PairThermalContact` | `ptc*` |  |
| `ThermalContact` | `tc*` |  |
| `ThermalContact` | `tc*` |  |
| `ContactAngle` | `cnta*` |  |
| `ContactArea` | `ca*` |  |
| `RigidBodyContact` | `rbc*` |  |
| `SolidContact` | `cnt*` |  |
| `ShellContact` | `cnt*` |  |
| `BoltThreadContact` | `btc*` |  |
| `SolidContact` | `cnt*` |  |
| `ContactAngle` | `cnta*` |  |
| `ContactAngle` | `cnta*` |  |

---

## 6. Expression Reference

Common postprocessing expressions (use with `model.evaluate()`):

| Expression | Unit | Description |
|-----------|------|-------------|
| `semi.V` | V | Electric potential |
| `semi.n` | 1/m^3 | Electron concentration |
| `semi.p` | 1/m^3 | Hole concentration |
| `c.u` | — | PDE dependent variable |
| `g.u` | — | PDE dependent variable |

---

## 7. Multiphysics Couplings

| Coupling | mph Type | Links |
|----------|---------|-------|
| `ElectronHeatSourceMultiphysicsCoupling` | `ehs*` | — |
| `EquilibriumDischargeHeatSource` | `phs*` | — |
| `RayHeatSource` | `rhs*` | — |
| `SemiconductorElectromagneticWavesCoupling` | `semc*` | — |

---

## 8. Common Patterns & COMSOL 6.4 Notes

- Note: The state of the switch (on/off) is changed only when a condition goes from 
false to true and not when going from true to false. Thus, if the state is off and the on 
condition goes from false 

