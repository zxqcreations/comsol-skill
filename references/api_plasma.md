# Plasma Module — Comprehensive API Reference

Plasma physics — DC, CCP, ICP, Microwave, and Drift Diffusion

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
| `?` | `` | ? |  (36 features) |
| `Batch` | `` | Batch |  (1 features) |
| `BeamRotor` | `rotbm` | BeamRotor | Beam envelope (slowly varying) (3 features) |
| `BioHeat` | `ht` | BioHeat |  (1 features) |
| `BoltzmannEquation` | `be` | BoltzmannEquation |  (4 features) |
| `ChargedParticleTracing` | `cpt` | ChargedParticleTracing |  (9 features) |
| `Chemistry` | `chem` | Chemistry |  (5 features) |
| `Circuit` | `cir` | Circuit |  (1 features) |
| `ColdPlasma` | `plas` | ColdPlasma | Plasma discharge (20 features) |
| `ConcentratedSpecies` | `tcs` | ConcentratedSpecies | Chemical species transport (11 features) |
| `ConductiveMedia` | `ec` | ConductiveMedia |  (3 features) |
| `ConductiveMediaShell` | `ecs` | ConductiveMediaShell |  (2 features) |
| `ConvectedWaveEquation` | `cwe` | ConvectedWaveEquation |  (6 features) |
| `ConvectionDiffusionEquation` | `cdeq` | ConvectionDiffusionEquation |  (4 features) |
| `CurrentDistributionBEM` | `cdbem` | CurrentDistributionBEM |  (7 features) |
| `CurrentDistributionShell` | `cdsh` | CurrentDistributionShell |  (4 features) |
| `CurvilinearCoordinates` | `cc` | CurvilinearCoordinates |  (5 features) |
| `DarcysLaw` | `dl` | DarcysLaw |  (21 features) |
| `DeformedGeometry` | `dg` | DeformedGeometry |  (2 features) |
| `DilutedSpecies` | `tds` | DilutedSpecies | Chemical species transport (22 features) |
| `DilutedSpeciesInPorousMedia` | `tds` | DilutedSpeciesInPorousMedia | Chemical species transport (22 features) |
| `Eigenfrequency` | `` | Eigenfrequency |  (28 features) |
| `Eigenvalue` | `` | Eigenvalue |  (9 features) |
| `ElectricCurrentsShell` | `ecis` | ElectricCurrentsShell |  (3 features) |
| `ElectricInductionCurrents` | `mef` | ElectricInductionCurrents |  (8 features) |
| `ElectricalBreakdownDetection` | `ebd` | ElectricalBreakdownDetection |  (4 features) |
| `ElectrodeShell` | `els` | ElectrodeShell |  (1 features) |
| `ElectromagneticWaves` | `emw` | ElectromagneticWaves |  (6 features) |
| `ElectromagneticWavesBeamEnvelopes` | `ewbe` | ElectromagneticWavesBeamEnvelopes | Beam envelope (slowly varying) (5 features) |
| `ElectromagneticWavesFrequencyDomain` | `ewfd` | ElectromagneticWavesFrequencyDomain | Frequency-domain electromagnetic waves (9 features) |
| `ElectromagneticWavesTransient` | `ewt` | ElectromagneticWavesTransient | Time-domain electromagnetic waves (4 features) |
| `ElectrophoreticTransport` | `el` | ElectrophoreticTransport | Chemical species transport (3 features) |
| `Electrostatics` | `es` | Electrostatics |  (7 features) |
| `ElectrostaticsBoundaryElements` | `esbe` | ElectrostaticsBoundaryElements | Boundary element method EM (1 features) |
| `FlowInPipes` | `pfl` | FlowInPipes |  (1 features) |
| `FluidParticleTracing` | `fpt` | FluidParticleTracing |  (2 features) |
| `FreeMolecularFlow` | `fmf` | FreeMolecularFlow |  (1 features) |
| `GeneralFormPDE` | `g` | GeneralFormPDE | Mathematics PDE interface (1 features) |
| `GeneralOptimization` | `opt` | GeneralOptimization | Optimization interface (10 features) |
| `GeometricalOptics` | `gop` | GeometricalOptics | Ray tracing optics (6 features) |
| `GlobalEquations` | `ge` | GlobalEquations |  (1 features) |
| `HeatTransfer` | `ht` | HeatTransfer |  (4 features) |
| `HeatTransferInBuildingMaterials` | `ht` | HeatTransferInBuildingMaterials |  (1 features) |
| `HeatTransferInFilmsLM` | `htlsh` | HeatTransferInFilmsLM |  (1 features) |
| `HeatTransferInFluids` | `ht` | HeatTransferInFluids |  (2 features) |
| `HeatTransferInMoistAir` | `ht` | HeatTransferInMoistAir |  (1 features) |
| `HeatTransferInShellsLM` | `htlsh` | HeatTransferInShellsLM |  (1 features) |
| `HeatTransferInSolidsAndFluids` | `ht` | HeatTransferInSolidsAndFluids |  (3 features) |
| `HeavySpeciesTransport` | `hs` | HeavySpeciesTransport | Chemical species transport (4 features) |
| `HermitianBeam` | `beam` | HermitianBeam | Beam envelope (slowly varying) (3 features) |
| `HighMachNumberFlow` | `hmnf` | HighMachNumberFlow |  (2 features) |
| `HighMachNumberFlowTurbulentSpalartAllmaras` | `hmnf` | HighMachNumberFlowTurbulentSpalartAllmaras |  (1 features) |
| `HighMachNumberFlowTurbulentkeps` | `hmnf` | HighMachNumberFlowTurbulentkeps |  (1 features) |
| `HydrodynamicBearing` | `hdb` | HydrodynamicBearing |  (4 features) |
| `InductionCurrents` | `mf` | InductionCurrents |  (28 features) |
| `LaminarFlow` | `spf` | LaminarFlow |  (1 features) |
| `LaplaceEquation` | `lpeq` | LaplaceEquation |  (6 features) |
| `LayeredShell` | `lshell` | LayeredShell |  (3 features) |
| `MagneticFieldFormulation` | `mfh` | MagneticFieldFormulation | Mathematics PDE interface (5 features) |
| `MagneticFieldsNoCurrentsBoundaryElements` | `mfncbe` | MagneticFieldsNoCurrentsBoundaryElements | Boundary element method EM (3 features) |
| `MagnetostaticsNoCurrents` | `mfnc` | MagnetostaticsNoCurrents |  (3 features) |
| `MaterialSweep` | `` | MaterialSweep |  (1 features) |
| `MathParticle` | `pt` | MathParticle |  (2 features) |
| `MoistureTransportInAir` | `mt` | MoistureTransportInAir | Chemical species transport (1 features) |
| `MoistureTransportInBuildingMaterials` | `mt` | MoistureTransportInBuildingMaterials | Chemical species transport (1 features) |
| `MovingMesh` | `ale` | MovingMesh |  (2 features) |
| `MultibodyDynamics` | `mbd` | MultibodyDynamics |  (20 features) |
| `NONE` | `` | NONE |  (14 features) |
| `Parametric` | `` | Parametric |  (54 features) |
| `ParticipatingMediaRadiation` | `rpm` | ParticipatingMediaRadiation |  (4 features) |
| `PhaseTransportPorousMedia` | `phtr` | PhaseTransportPorousMedia | Chemical species transport (1 features) |
| `PipeMechanics` | `pipem` | PipeMechanics |  (2 features) |
| `PlasmaTimePeriodic` | `ptp` | PlasmaTimePeriodic | Plasma discharge (14 features) |
| `PlotGroup1D` | `` | PlotGroup1D |  (5 features) |
| `PlotGroup2D` | `` | PlotGroup2D |  (8 features) |
| `PlotGroup3D` | `` | PlotGroup3D |  (5 features) |
| `PolarGroup` | `` | PolarGroup |  (1 features) |
| `PoroelasticWavesSinglePhysics` | `pelw` | PoroelasticWavesSinglePhysics |  (1 features) |
| `PorousMediaHeatTransfer` | `ht` | PorousMediaHeatTransfer |  (1 features) |
| `PressureAcoustics` | `acpr` | PressureAcoustics |  (9 features) |
| `PrimaryCurrentDistribution` | `cd` | PrimaryCurrentDistribution |  (9 features) |
| `RayAcoustics` | `rac` | RayAcoustics | Ray tracing optics (1 features) |
| `ReactionEng` | `re` | ReactionEng | Reaction engineering (11 features) |
| `RichardsEquation` | `dl` | RichardsEquation |  (7 features) |
| `RotatingMachineryMagnetic` | `rmm` | RotatingMachineryMagnetic |  (10 features) |
| `SchrodingerEquation` | `schr` | SchrodingerEquation |  (14 features) |
| `SecondaryCurrentDistribution` | `cd` | SecondaryCurrentDistribution |  (19 features) |
| `Semiconductor` | `semi` | Semiconductor | Semiconductor device (14 features) |
| `Sequence` | `` | Sequence |  (1 features) |
| `ShallowWaterEquationsTimeExplicit` | `swe` | ShallowWaterEquationsTimeExplicit | Explicit time-stepping EM waves (4 features) |
| `Shell` | `shell` | Shell |  (6 features) |
| `SlipFlow` | `slpf` | SlipFlow |  (1 features) |
| `SmithGroup` | `` | SmithGroup |  (2 features) |
| `SolidMechanics` | `solid` | SolidMechanics |  (31 features) |
| `SolidRotor` | `rotsld` | SolidRotor |  (7 features) |
| `Stationary` | `` | Stationary |  (43 features) |
| `StructuralMembrane` | `mbrn` | StructuralMembrane |  (2 features) |
| `SurfaceReactions` | `sr*` | SurfaceReactions | Reaction engineering (4 features) |
| `SurfaceToSurfaceRadiation` | `rad` | SurfaceToSurfaceRadiation |  (6 features) |
| `TertiaryCurrentDistributionNernstPlanck` | `tcd` | TertiaryCurrentDistributionNernstPlanck |  (21 features) |
| `TertiaryElectroanalysis` | `tcd` | TertiaryElectroanalysis |  (5 features) |
| `ThermoacousticsSinglePhysicsTransient` | `tatd` | ThermoacousticsSinglePhysicsTransient | Time-domain electromagnetic waves (1 features) |
| `ThinFilmFlowDomain` | `tff` | ThinFilmFlowDomain |  (1 features) |
| `ThinFilmFlowShell` | `tffs` | ThinFilmFlowShell |  (1 features) |
| `Time` | `elte` | Time |  (45 features) |
| `Timeparametric` | `` | Timeparametric |  (21 features) |
| `TransientElectromagneticWaves` | `temw` | TransientElectromagneticWaves | Time-domain electromagnetic waves (3 features) |
| `TransientPressureAcoustics` | `actd` | TransientPressureAcoustics | Time-domain electromagnetic waves (3 features) |
| `TransmissionLine` | `tl` | TransmissionLine |  (4 features) |
| `Truss` | `truss` | Truss |  (8 features) |
| `TurbulentFlowAlgebraicYplus` | `spf` | TurbulentFlowAlgebraicYplus |  (5 features) |
| `TurbulentFlowkeps` | `spf` | TurbulentFlowkeps |  (4 features) |
| `TurbulentFlowkomega` | `spf` | TurbulentFlowkomega |  (1 features) |
| `curve` | `` | curve |  (3 features) |
| `empty` | `` | empty |  (11 features) |
| `mixed` | `` | mixed |  (9 features) |
| `solid` | `` | solid |  (20 features) |
| `surface` | `` | surface |  (8 features) |

---

## 2. Domain Features

| Feature Name | mph Tag | Interface | Key Properties |
|-------------|---------|-----------|---------------|
| `PlasmaEsModel` | `pes*` |  | — |
| `PlasmaEsModel` | `pes*` |  | — |
| `WaveEquationElectric` | `wee*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `WaveEquationElectric` | `wee*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `ReverseCoilGroupDomain` | `rcd*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `WKBTunnelingModelElectrons` | `wkbe*` |  | — |
| `DestinationDomains` | `dd*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `BoltzmannModel` | `bmdl*` |  | — |
| `ReactionWithTurbulenceModel` | `treac*` |  | — |
| `FluidPorousMedium` | `fluid*` |  | — |
| `PorousMatrixPorousMedium` | `pm*` |  | — |
| `PorousMedium` | `porous*` |  | FluidPorousMedium, PorousMatrixPorousMedium |
| `FluidPorousMedium` | `fluid*` |  | — |
| `GasUnsaturatedPorousMedium` | `gas*` |  | — |
| `LiquidUnsaturatedPorousMedium` | `liquid*` |  | — |
| `PorousMatrixPorousMedium` | `pm*` |  | — |
| `PorousMedium` | `porous*` |  | Adsorptions, Dispersion, FluidPorousMedium, PorousMatrixPorousMedium |
| `UnsaturatedPorousMedium` | `usporous*` |  | Adsorptions, Dispersion, GasUnsaturatedPorousMedium, LiquidUnsaturatedPorousMedium, PorousMatrixPorousMedium |
| `GlobalEquations` | `ge*` |  | — |
| `DomainDecomposition` | `dd*` |  | CoarseSolver, Direct, DomainSolver, Direct, DirectPreconditioner |
| `DomainDecompositionSchur` | `dd*` |  | DomainSolver, Direct, SchurSolver, SchurKrylovPreconditioner, SchurLocal |
| `DomainSolver` | `ds` |  | Direct, DirectPreconditioner |
| `ModelReduction` | `mr` |  | — |
| `PartitionDomains` | `pard*` |  | — |
| `PartitionDomains` | `pard*` |  | — |
| `PartitionDomains` | `pard*` |  | — |
| `PartitionDomains` | `pard*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `ConvectedWaveEquationModel` | `cwem*` |  | — |
| `ConvectionDiffusionEquation` | `cdeq*` |  | — |
| `DarcysLawModel` | `dlm*` |  | — |
| `PoroelasticMaterial` | `psm*` |  | — |
| `StorageModel` | `smm*` |  | — |
| `ElectromagneticModel` | `alc*` |  | — |
| `WaveEquationBeamEnvelopes` | `webe*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `WaveEquationElectric` | `wee*` |  | DrudeLorentzPolarization |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `LaplaceEquation` | `leq*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `ParticipatingMedium` | `rpm*` |  | — |
| `NarrowRegionAcousticsModel` | `nra*` |  | — |
| `RichardsEquationModel` | `remm*` |  | — |
| `DomainProperties` | `dp*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `GlobalEquations` | `ge*` |  | — |
| `WaveEquationElectric` | `wee*` |  | DrudeLorentzPolarization |
| `TransmissionLineEquation` | `tle*` |  | — |

---

## 3. Boundary Conditions

| BC Name | mph Tag | Interface | Key Properties |
|---------|---------|-----------|---------------|
| `Ground` | `gnd*` |  | — |
| `Terminal` | `term*` |  | — |
| `WallDriftDiffusion` | `wall*` |  | — |
| `Ground` | `gnd*` |  | — |
| `WallDriftDiffusion` | `wall*` |  | — |
| `BoundaryElectricPotential` | `bpot*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `TransitionBoundaryCondition` | `trans*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicPortReferencePoint` | `pportp*` |  | — |
| `TransitionBoundaryCondition` | `trans*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `CoilGround` | `cg*` |  | — |
| `CoilTerminal` | `ct*` |  | — |
| `Impedance` | `imp*` |  | — |
| `LumpedPort` | `lport*` |  | — |
| `PerfectMagneticConductor` | `pmc*` |  | — |
| `BoundarySelectionForDopingProfile` | `gdmbs*` |  | — |
| `ContinuousEnergyLevelsBoundary` | `ctb*` |  | — |
| `DiscreteEnergyLevelBoundary` | `dtb*` |  | — |
| `OpticalTransitions` | `ot*` |  | — |
| `PeriodicCondition` | `pc*` |  | DestinationDomains |
| `ThreadBoundarySelection` | `tbs*` |  | Free |
| `BoundaryReactionCoefficients` | `rc*` |  | — |
| `FluxBoundary` | `fl*` |  | — |
| `ElectricGround` | `egnd*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `OpenBoundary` | `open*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `WallDistanceInitialization` | `wdi` |  | — |
| `AcousticImpedance` | `imp*` |  | — |
| `SoundHardWall` | `shw*` |  | — |
| `DirichletBoundary` | `dir*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `WallDefault` | `wall*` |  | — |
| `Wall` | `wall*` |  | — |
| `MatchedBoundaryCondition` | `mbc*` |  | ReferencePoint |
| `PeriodicCondition` | `pc*` |  | — |
| `TransitionBoundaryCondition` | `trans*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `DirichletBoundary` | `dir*` |  | — |
| `FluxBoundary` | `flux*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `MagneticFieldBoundary` | `mfb*` |  | — |
| `ContinuityOnInteriorBoundary` | `cib*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `CoilGround` | `cg*` |  | — |
| `CoilTerminal` | `ct*` |  | — |
| `MixedFormulationBoundary` | `mxb*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `InletBoundary` | `inl*` |  | — |
| `WallBC` | `wallbc*` |  | — |
| `PeriodicCondition` | `pc*` |  | — |
| `LumpedPort` | `lport*` |  | — |
| `PeriodicFlowCondition` | `pfc*` |  | — |
| `PeriodicFlowCondition` | `pfc*` |  | — |
| `PeriodicFlowCondition` | `pfc*` |  | — |

---

## 4. Edge & Point Conditions

| Name | mph Tag | Type | Interface |
|------|---------|------|-----------|
| `AxialSymmetry` | `axi*` | Other |  |
| `ChargeConservation` | `ccn*` | Other |  |
| `CrossSectionImport` | `xsec*` | Other |  |
| `DisplacementField` | `df*` | Other |  |
| `ElectronImpactReaction` | `eir*` | Other |  |
| `ElectronOutlet` | `eout*` | Other |  |
| `InitialValues` | `init*` | Other |  |
| `Insulation` | `ins*` | Other |  |
| `Outflow` | `out*` | Other |  |
| `Reaction` | `rxn*` | Other |  |
| `Species` | `sp*` | Other |  |
| `SurfaceChargeAccumulation` | `sca*` | Other |  |
| `SurfaceReaction` | `sr*` | Other |  |
| `ZeroCharge` | `zc*` | Other |  |
| `AxialSymmetry` | `axi*` | Other |  |
| `CrossSectionImport` | `xsecimp*` | Other |  |
| `ElectronImpactReaction` | `eir*` | Other |  |
| `Insulation` | `ins*` | Other |  |
| `Reaction` | `rxn*` | Other |  |
| `Species` | `sp*` | Other |  |
| `SurfaceReaction` | `sr*` | Other |  |
| `ZeroCharge` | `zc*` | Other |  |
| `init` | `init*` | Other |  |
| `CurrentConservation` | `cucn*` | Other |  |
| `ElectricInsulation` | `ein*` | Other |  |
| `ElectricPotential` | `pot*` | Other |  |
| `ElectricInsulation` | `ein*` | Other |  |
| `ElectricPotential` | `pot*` | Other |  |
| `ElectricPotential` | `pot*` | Other |  |
| `FarFieldCalculation` | `ffc*` | Other |  |
| `SpecificAbsorptionRate` | `sar*` | Other |  |
| `DiffractionOrder` | `dport*` | Other |  |
| `FarFieldCalculation` | `ffc*` | Other |  |
| `OrthogonalPolarization` | `oport*` | Other |  |
| `Polarization` | `pol*` | Other |  |
| `ChargeConservation` | `ccn*` | Other |  |
| `ChargeConservationFerroelectric` | `ccnf*` | Other |  |
| `ChargeConservationPiezo` | `ccnp*` | Other |  |
| `ElectricPotential` | `pot*` | Other |  |
| `HarmonicPerturbation` | `hp*` | Other |  |

---

## 5. Pair Conditions

| Name | mph Tag | Interface |
|------|---------|----------|
| `DielectricContact` | `dct*` |  |
| `MetalContact` | `mct*` |  |
| `DielectricContact` | `dct*` |  |
| `MetalContact` | `mct*` |  |
| `Continuity` | `cont*` |  |
| `Continuity` | `cont*` |  |
| `ContactArea` | `ca*` |  |
| `ContactAngle` | `cnta*` |  |
| `ContactAngle` | `cnta*` |  |

---

## 6. Expression Reference

Common postprocessing expressions (use with `model.evaluate()`):

| Expression | Unit | Description |
|-----------|------|-------------|
| `tds.c` | mol/m^3 | Concentration |
| `tds.Nx` | mol/(m^2*s) | Flux, x-component |
| `c.u` | — | PDE dependent variable |
| `g.u` | — | PDE dependent variable |

---

## 7. Multiphysics Couplings

| Coupling | mph Type | Links |
|----------|---------|-------|
| `AcousticPipeAcousticConnection` | `apc*` | — |
| `AcousticPorousBoundary` | `apb*` | — |
| `ElectricParticleFieldInteraction` | `epfi*` | — |
| `ElectronHeatSourceMultiphysicsCoupling` | `ehs*` | — |
| `FluidPipeInteraction` | `fpipe*` | — |
| `FluidStructureInteractionBC` | `fsi*` | — |
| `FluidStructureInteractionPair` | `fsip*` | — |
| `HeatTransferWithRadiationInParticipatingMedia` | `htrpm*` | — |
| `HeatTransferWithSurfaceToSurfaceRadiation` | `htrad*` | — |
| `LayeredShellStructTransition` | `lsst*` | — |
| `LumpedStructureConnection` | `lsc*` | — |
| `MagneticParticleFieldInteraction` | `mpfi*` | — |
| `Magnetostriction` | `pzm*` | — |
| `PipeConnection` | `plc*` | — |
| `PlasmaConductivityMultiphysicsCoupling` | `pcc*` | — |
| `ShellBeamConnection` | `shbc*` | — |
| `SolidBeamConnection3D` | `sbc*` | — |
| `SolidShellConnection` | `sshc*` | — |
| `SpaceChargeLimitedEmission` | `scle*` | — |
| `ThermalExpansion` | `te*` | — |
| `ThermalExpansionLS` | `tel*` | — |

---

## 8. Common Patterns & COMSOL 6.4 Notes

- Note: The state of the switch (on/off) is changed only when a condition goes from 
false to true and not when going from true to false. Thus, if the state is off and the on 
condition goes from false 

