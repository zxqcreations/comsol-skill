# Chemical Species Transport Module — Comprehensive API Reference

Transport of Diluted/Concentrated Species, Reaction Engineering, Chemistry

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
| `?` | `` | ? |  (3 features) |
| `BoltzmannEquation` | `be` | BoltzmannEquation |  (1 features) |
| `ChargeTransport` | `ct` | ChargeTransport | Chemical species transport (1 features) |
| `Chemistry` | `chem` | Chemistry |  (5 features) |
| `CoefficientFormPDE` | `c` | CoefficientFormPDE | Mathematics PDE interface (2 features) |
| `ColdPlasma` | `plas` | ColdPlasma | Plasma discharge (5 features) |
| `ConcentratedSpecies` | `tcs` | ConcentratedSpecies | Chemical species transport (7 features) |
| `ConvectionDiffusionEquation` | `cdeq` | ConvectionDiffusionEquation |  (4 features) |
| `CurrentDistributionBEM` | `cdbem` | CurrentDistributionBEM |  (1 features) |
| `CurrentDistributionShell` | `cdsh` | CurrentDistributionShell |  (1 features) |
| `CurvilinearCoordinates` | `cc` | CurvilinearCoordinates |  (4 features) |
| `DarcysLaw` | `dl` | DarcysLaw |  (1 features) |
| `DilutedSpecies` | `tds` | DilutedSpecies | Chemical species transport (15 features) |
| `DilutedSpeciesInPorousMedia` | `tds` | DilutedSpeciesInPorousMedia | Chemical species transport (22 features) |
| `ElectrophoreticTransport` | `el` | ElectrophoreticTransport | Chemical species transport (14 features) |
| `FluidParticleTracing` | `fpt` | FluidParticleTracing |  (2 features) |
| `FreeAndPorousMediaFlow` | `fp` | FreeAndPorousMediaFlow |  (8 features) |
| `GeneralFormPDE` | `g` | GeneralFormPDE | Mathematics PDE interface (2 features) |
| `HeatTransfer` | `ht` | HeatTransfer |  (1 features) |
| `HeatTransferInBuildingMaterials` | `ht` | HeatTransferInBuildingMaterials |  (1 features) |
| `HeatTransferInFluids` | `ht` | HeatTransferInFluids |  (6 features) |
| `HeatTransferInMoistAir` | `ht` | HeatTransferInMoistAir |  (1 features) |
| `HeatTransferInShellsLM` | `htlsh` | HeatTransferInShellsLM |  (2 features) |
| `HeatTransferInSolidsAndFluids` | `ht` | HeatTransferInSolidsAndFluids |  (3 features) |
| `HeatTransferPipes` | `htp` | HeatTransferPipes |  (1 features) |
| `HeavySpeciesTransport` | `hs` | HeavySpeciesTransport | Chemical species transport (2 features) |
| `LaplaceEquation` | `lpeq` | LaplaceEquation |  (2 features) |
| `MagneticFieldsNoCurrentsBoundaryElements` | `mfncbe` | MagneticFieldsNoCurrentsBoundaryElements | Boundary element method EM (2 features) |
| `MagnetostaticsNoCurrents` | `mfnc` | MagnetostaticsNoCurrents |  (2 features) |
| `MoistureTransportInAir` | `mt` | MoistureTransportInAir | Chemical species transport (1 features) |
| `MoistureTransportInBuildingMaterials` | `mt` | MoistureTransportInBuildingMaterials | Chemical species transport (1 features) |
| `NonisothermalPipeFlow` | `nipfl` | NonisothermalPipeFlow |  (1 features) |
| `PhaseTransport` | `phtr` | PhaseTransport | Chemical species transport (1 features) |
| `PhaseTransportPorousMedia` | `phtr` | PhaseTransportPorousMedia | Chemical species transport (10 features) |
| `PlasmaTimePeriodic` | `ptp` | PlasmaTimePeriodic | Plasma discharge (4 features) |
| `PoroelasticWavesSinglePhysics` | `pelw` | PoroelasticWavesSinglePhysics |  (1 features) |
| `PorousMedia` | `tds` | PorousMedia |  (3 features) |
| `PorousMediaHeatTransfer` | `ht` | PorousMediaHeatTransfer |  (25 features) |
| `PrimaryCurrentDistribution` | `cd` | PrimaryCurrentDistribution |  (1 features) |
| `ReactionEng` | `re` | ReactionEng | Reaction engineering (11 features) |
| `RotatingMachineryMagnetic` | `rmm` | RotatingMachineryMagnetic |  (2 features) |
| `SchrodingerEquation` | `schr` | SchrodingerEquation |  (1 features) |
| `SecondaryCurrentDistribution` | `cd` | SecondaryCurrentDistribution |  (2 features) |
| `SolidMechanics` | `solid` | SolidMechanics |  (1 features) |
| `SurfaceReactions` | `sr*` | SurfaceReactions | Reaction engineering (4 features) |
| `TertiaryCurrentDistributionNernstPlanck` | `tcd` | TertiaryCurrentDistributionNernstPlanck |  (21 features) |
| `TertiaryElectroanalysis` | `tcd` | TertiaryElectroanalysis |  (5 features) |
| `empty` | `` | empty |  (2 features) |
| `mixed` | `` | mixed |  (2 features) |
| `solid` | `` | solid |  (4 features) |
| `surface` | `` | surface |  (1 features) |

---

## 2. Domain Features

| Feature Name | mph Tag | Interface | Key Properties |
|-------------|---------|-----------|---------------|
| `ReactionWithTurbulenceModel` | `treac*` |  | — |
| `ConvectionDiffusionEquation` | `cdeq*` |  | — |
| `FluidPorousMedium` | `fluid*` |  | — |
| `PorousMatrixPorousMedium` | `pm*` |  | — |
| `PorousMedium` | `porous*` |  | FluidPorousMedium, PorousMatrixPorousMedium |
| `FluidPorousMedium` | `fluid*` |  | — |
| `GasUnsaturatedPorousMedium` | `gas*` |  | — |
| `LiquidUnsaturatedPorousMedium` | `liquid*` |  | — |
| `PorousMatrixPorousMedium` | `pm*` |  | — |
| `PorousMedium` | `porous*` |  | Adsorptions, Dispersion, FluidPorousMedium, PorousMatrixPorousMedium |
| `UnsaturatedPorousMedium` | `usporous*` |  | Adsorptions, Dispersion, GasUnsaturatedPorousMedium, LiquidUnsaturatedPorousMedium, PorousMatrixPorousMedium |
| `FluidPorousMediumHeatTransferModel` | `fluid*` |  | — |
| `PorousMatrixPorousMediumHeatTransferModel` | `pm*` |  | — |
| `PorousMediumHeatTransferModel` | `porous*` |  | FluidPorousMediumHeatTransferModel, PorousMatrixPorousMediumHeatTransferModel |
| `PorousMediumDiscontinuity` | `pmd*` |  | — |
| `FluidHeatTransferModel` | `fluid*` |  | Opacity |
| `FluidPorousMediumHeatTransferModel` | `fluid*` |  | PhaseChangeMaterial |
| `ImmobileFluidPorousMaterial` | `imf*` |  | — |
| `IsothermalDomainInterface` | `idi*` |  | LayerOpacity |
| `PhaseChangeMaterial` | `phc*` |  | — |
| `PorousMatrixPorousMediumHeatTransferModel` | `pm*` |  | — |
| `PorousMediumHeatTransferModel` | `porous*` |  | FluidPorousMediumHeatTransferModel, PhaseChangeMaterial, ImmobileFluidPorousMaterial, PorousMatrixPorousMediumHeatTransferModel |
| `PorousMediumLayeredShell` | `pmls*` |  | init, ThermalInsulation |
| `SolidHeatTransferModel` | `solid*` |  | Opacity |
| `PartitionDomains` | `pard*` |  | — |
| `PartitionDomains` | `pard*` |  | — |
| `PartitionDomains` | `pard*` |  | — |
| `PartitionDomains` | `pard*` |  | — |

---

## 3. Boundary Conditions

| BC Name | mph Tag | Interface | Key Properties |
|---------|---------|-----------|---------------|
| `PeriodicCondition` | `pc*` |  | — |
| `DirichletBoundary` | `dir*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `BoundaryReactionCoefficients` | `rc*` |  | — |
| `FluxBoundary` | `fl*` |  | — |
| `WallDriftDiffusion` | `wall*` |  | — |
| `WallDefault` | `wall*` |  | — |
| `WallDriftDiffusion` | `wall*` |  | — |
| `FluxBoundary` | `flux*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `FluxBoundary` | `flux*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `FluxBoundary` | `flux*` |  | — |
| `ZeroFluxBoundary` | `zflx*` |  | — |
| `BoundaryHeatSource` | `bhs*` |  | — |
| `ContinuityOnInteriorBoundary` | `cib*` |  | — |
| `HeatFluxBoundary` | `hf*` |  | — |
| `OpenBoundary` | `open*` |  | — |
| `TemperatureBoundary` | `temp*` |  | — |
| `InletBoundary` | `inl*` |  | — |
| `OutletBoundary` | `out*` |  | — |
| `Wall` | `wall*` |  | WallBC |
| `WallBC` | `wallbc*` |  | — |

---

## 4. Edge & Point Conditions

| Name | mph Tag | Type | Interface |
|------|---------|------|-----------|
| `ReactionChem` | `rch*` | Other |  |
| `ReversibleReactionGroup` | `rgr*` | Other |  |
| `SpeciesChem` | `sch*` | Other |  |
| `SpeciesGroup` | `sg_rgr*` | Other |  |
| `SpeciesThermodynamics` | `sthm*` | Other |  |
| `ConvectionDiffusionMigration` | `cdm*` | Other |  |
| `Inflow` | `in*` | Other |  |
| `NoFlux` | `nflx*` | Other |  |
| `Outflow` | `out*` | Other |  |
| `ReactionSources` | `reac*` | Other |  |
| `TCSPorousMediaTransportProperties` | `pmtcs*` | Other |  |
| `AxialSymmetry` | `axi*` | Other |  |
| `Concentration` | `conc*` | Other |  |
| `ElectricInsulation` | `ein*` | Other |  |
| `ElectrodeReaction` | `er*` | Other |  |
| `ElectrodeSurface` | `es*` | Other |  |
| `Electrolyte` | `ice*` | Other |  |
| `ElectrolytePotential` | `eip*` | Other |  |
| `ElectrolytePotentialPoint` | `eip*` | Point |  |
| `EquilibriumReaction` | `eqreac*` | Other |  |
| `GlobalConstraint` | `gconstr*` | Other |  |
| `HighlyConductivePorousElectrode` | `hcpce*` | Other |  |
| `Inflow` | `in*` | Other |  |
| `IonExchangeMembrane` | `iem*` | Other |  |
| `NoFlux` | `nflx*` | Other |  |
| `NonFaradaicReactions` | `nfr*` | Other |  |
| `Outflow` | `out*` | Other |  |
| `PorousElectrodeReaction` | `per*` | Other |  |
| `Separator` | `sep*` | Other |  |
| `SurfaceChargeDensity` | `sfcd*` | Other |  |
| `init` | `init*` | Other |  |
| `init` | `init*` | Other |  |
| `Concentration` | `conc*` | Other |  |
| `ConvectionDiffusionMigration` | `cdm*` | Other |  |
| `Inflow` | `in*` | Other |  |
| `NoFlux` | `nflx*` | Other |  |
| `Outflow` | `out*` | Other |  |
| `PartitionCondition` | `pac*` | Other |  |
| `Reactions` | `reac*` | Other |  |
| `SurfaceEquilibriumReaction` | `seqreac*` | Other |  |

---

## 5. Pair Conditions


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
| `AcousticPorousBoundary` | `apb*` | — |
| `MultiphaseFlowInPorousMedia` | `mfpm*` | — |
| `PorousStructureBoundary` | `psb*` | — |

---

## 8. Common Patterns & COMSOL 6.4 Notes

- Note: Some of the additional transport mechanisms listed below are only available in 
certain products. For details see www.comsol.com/products/specifications/.
• By default, the Convection checkbox i

- Note: Mass transport in porous media is only available in a limited set of 
add-on products. See www.comsol.com/products/specifications/ for 
more details on availability.


--- Page 137 ---
T H E  T 

- Note: There are other definitions of the migration transport equations in the 
literature which use mobilities expressed in m2/(V·s), whereas COMSOL 
Multiphysics uses s·mol/kg. To convert mobilities 

- Note: Some features explained in this section require certain add-on modules. For 
details see www.comsol.com/products/specifications/


--- Page 354 ---
354 |  C H A P T E R  3 :  C H E M I C A L  S 

- Note: The features below are only available in a limited set of add-on products. For a 
detailed overview of which features are available in each product, visit 
www.comsol.com/products/specifications

- Note: Migration is only available in a limited set of add-on products. For a detailed 
overview of which features are available in each product, visit 
www.comsol.com/products/specifications/
In addit

- Note: In the Nernst–Planck Equations interface, the ionic species contribute to the 
charge transfer in the solution. It includes an electroneutrality condition and also 
computes the electric potenti

