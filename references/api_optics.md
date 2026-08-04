# Optics Module — Comprehensive API Reference

Ray Optics + Wave Optics (Electromagnetic Waves, Frequency Domain + Beam Envelopes)

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
| `ElectromagneticWaves` | `emw` | ElectromagneticWaves |  (1 features) |
| `ElectromagneticWavesBeamEnvelopes` | `ewbe` | ElectromagneticWavesBeamEnvelopes | Beam envelope (slowly varying) (12 features) |
| `ElectromagneticWavesFrequencyDomain` | `ewfd` | ElectromagneticWavesFrequencyDomain | Frequency-domain electromagnetic waves (4 features) |
| `ElectromagneticWavesTransient` | `ewt` | ElectromagneticWavesTransient | Time-domain electromagnetic waves (2 features) |
| `FlowInPipes` | `pfl` | FlowInPipes |  (1 features) |
| `GeometricalOptics` | `gop` | GeometricalOptics | Ray tracing optics (23 features) |
| `HeatTransfer` | `ht` | HeatTransfer |  (1 features) |
| `HeatTransferInFluids` | `ht` | HeatTransferInFluids |  (1 features) |
| `HeatTransferInSolidsAndFluids` | `ht` | HeatTransferInSolidsAndFluids |  (1 features) |
| `HermitianBeam` | `beam` | HermitianBeam | Beam envelope (slowly varying) (1 features) |
| `MultibodyDynamics` | `mbd` | MultibodyDynamics |  (11 features) |
| `PhaseField` | `pf` | PhaseField |  (9 features) |
| `PhaseTransport` | `phtr` | PhaseTransport | Chemical species transport (4 features) |
| `PhaseTransportPorousMedia` | `phtr` | PhaseTransportPorousMedia | Chemical species transport (10 features) |
| `PlotGroup1D` | `` | PlotGroup1D |  (3 features) |
| `PlotGroup2D` | `` | PlotGroup2D |  (5 features) |
| `PlotGroup3D` | `` | PlotGroup3D |  (5 features) |
| `PorousMediaHeatTransfer` | `ht` | PorousMediaHeatTransfer |  (1 features) |
| `RayAcoustics` | `rac` | RayAcoustics | Ray tracing optics (7 features) |
| `Semiconductor` | `semi` | Semiconductor | Semiconductor device (1 features) |
| `SmithGroup` | `` | SmithGroup |  (2 features) |
| `SolidMechanics` | `solid` | SolidMechanics |  (2 features) |
| `TernaryPhaseField` | `terpf` | TernaryPhaseField |  (4 features) |
| `TransientElectromagneticWaves` | `temw` | TransientElectromagneticWaves | Time-domain electromagnetic waves (2 features) |
| `curve` | `` | curve |  (2 features) |
| `empty` | `` | empty |  (2 features) |
| `mixed` | `` | mixed |  (2 features) |
| `solid` | `` | solid |  (2 features) |
| `surface` | `` | surface |  (1 features) |

---

## 2. Domain Features

| Feature Name | mph Tag | Interface | Key Properties |
|-------------|---------|-----------|---------------|
| `GlobalEquations` | `ge*` |  | — |
| `MaterialDiscontinuity` | `matd*` |  | ThinDielectricFilm |
| `MediumProperties` | `mp*` |  | — |
| `WaveEquationBeamEnvelopes` | `webe*` |  | — |
| `MaterialDiscontinuity` | `matd*` |  | — |
| `MediumProperties` | `mp*` |  | — |
| `PhaseChangeMaterial` | `phc*` |  | — |
| `PhaseChangeMaterial` | `phc*` |  | — |
| `PhaseFieldModel` | `pfm*` |  | — |
| `PorousMediumDiscontinuity` | `pmd*` |  | — |
| `PhaseChangeMaterial` | `phc*` |  | — |

---

## 3. Boundary Conditions

| BC Name | mph Tag | Interface | Key Properties |
|---------|---------|-----------|---------------|
| `BoundaryAccumulator` | `bacc*` |  | — |
| `DepositedRayPowerBoundary` | `bsrc*` |  | — |
| `ReleaseFromBoundary` | `relb*` |  | — |
| `Wall` | `wall*` |  | BoundaryAccumulator, DepositedRayPowerBoundary |
| `Impedance` | `imp*` |  | — |
| `MatchedBoundaryCondition` | `mbc*` |  | ReferencePoint |
| `PerfectElectricConductor` | `pec*` |  | — |
| `PerfectMagneticConductor` | `pmc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `Port` | `port*` |  | — |
| `Scattering` | `sctr*` |  | ReferencePoint |
| `TransitionBoundaryCondition` | `trans*` |  | — |
| `SoundPressureLevelBoundary` | `spl*` |  | — |
| `Wall` | `wall*` |  | SoundPressureLevelBoundary |
| `PhasePortrait` | `phpo*` |  | Color |
| `Scattering` | `sctr*` |  | — |
| `Scattering` | `sctr*` |  | — |
| `Scattering` | `sctr*` |  | — |
| `Scattering` | `sctr*` |  | — |
| `InletBoundary` | `inl*` |  | — |
| `InteriorWettedWall` | `iww*` |  | — |
| `WettedWall` | `ww*` |  | — |
| `WettedWall` | `ww*` |  | — |
| `OpticalTransitions` | `ot*` |  | — |

---

## 4. Edge & Point Conditions

| Name | mph Tag | Type | Interface |
|------|---------|------|-----------|
| `CrossDiffractionOrder` | `xdfo*` | Other |  |
| `CrossGrating` | `xgrat*` | Other |  |
| `DiffractionOrder` | `dfo*` | Other |  |
| `Grating` | `grat*` | Other |  |
| `IlluminatedSurface` | `ill*` | Other |  |
| `LinearPolarizer` | `lpol*` | Other |  |
| `LinearWaveRetarder` | `lwav*` | Other |  |
| `Mirror` | `mir*` | Other |  |
| `RayProperties` | `op*` | Other |  |
| `RayTermination` | `rt*` | Other |  |
| `ReleaseFromElectricField` | `rele*` | Other |  |
| `ReleaseFromFarFieldRadiationPattern` | `rffr*` | Other |  |
| `ReleaseFromPoint` | `rpt*` | Point |  |
| `ReleaseGrid` | `relg*` | Other |  |
| `SolarRadiation` | `srad*` | Other |  |
| `ThinDielectricFilm` | `film*` | Other |  |
| `ReferencePoint` | `rpnt*` | Point |  |
| `init` | `init*` | Other |  |
| `Array` | `arr*` | Other |  |
| `BidirectionallyCoupledRayTracing` | `bcrt` | Other |  |
| `Mirror` | `mir*` | Other |  |
| `PhaseInitialization` | `phasei` | Other |  |
| `RayTracing` | `rtrac` | Other |  |
| `Array` | `arr*` | Other |  |
| `Mirror` | `mir*` | Other |  |
| `Array` | `arr*` | Other |  |
| `Mirror` | `mir*` | Other |  |
| `Array` | `arr*` | Other |  |
| `Mirror` | `mir*` | Other |  |
| `Array` | `arr*` | Other |  |
| `Mirror` | `mir*` | Other |  |
| `Array` | `arr*` | Other |  |
| `RayProperties` | `op*` | Other |  |
| `RayTermination` | `rt*` | Other |  |
| `ReleaseGrid` | `relg*` | Other |  |
| `Color` | `col*` | Other |  |
| `Polarization` | `plz*` | Other |  |
| `Ray1D` | `rtp*` | Other |  |
| `Color` | `col*` | Other |  |
| `OpticalAberration` | `oab*` | Other |  |

---

## 5. Pair Conditions

| Name | mph Tag | Interface |
|------|---------|----------|
| `FieldContinuity` | `fcont*` |  |

---

## 6. Expression Reference

Common postprocessing expressions (use with `model.evaluate()`):

| Expression | Unit | Description |
|-----------|------|-------------|
| `gop.rrel` | 1 | Ray position (relative) |
| `gop.Intensity` | W/m^2 | Ray intensity |
| `gop.OPL` | m | Optical path length |
| `c.u` | — | PDE dependent variable |
| `g.u` | — | PDE dependent variable |

---

## 7. Multiphysics Couplings

| Coupling | mph Type | Links |
|----------|---------|-------|
| `MultiphaseFlowInPorousMedia` | `mfpm*` | — |
| `MultiphaseFlowMixtureModel` | `mfmm*` | — |
| `RayHeatSource` | `rhs*` | — |
| `TernaryFlowPhaseField` | `tfpf*` | — |
| `TwoPhaseFlowLevelSet` | `tpf*` | — |
| `TwoPhaseFlowPhaseField` | `tpf*` | — |

---

## 8. Common Patterns & COMSOL 6.4 Notes

- Note: the superscript (i) is used to distinguish this coordinate system 
rotation angle from the angle of incidence of the ray, often denoted θi.)
4 Transform the principal curvatures to the local coo

