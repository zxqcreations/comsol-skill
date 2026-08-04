# Physics Interfaces — mph Feature Tags

Extracted from mph tags.json (COMSOL 6.4).
Feature type strings for use with `create(tag, type_string, dim)`.

Tag: `physics`

### Aeroacoustics
Tag: `ae`
  Tag: `ae`
  - `AeroacousticsModel` -> `aem*`
  - `AxialSymmetry` -> `axi*`
  - `Impedance` -> `imp*`
  - `InteriorSoundHard` -> `ishb*`
  - `NormalMassFlow` -> `nmf*`
  - `SoundHard` -> `shb*`
  - `VelocityPotential` -> `pvel*`
  - `VortexSheet` -> `vs*`
  - `init` -> `init*`

### BeamRotor
Tag: `rotbm`
  Tag: `rotbm`

  ### ActiveMagneticBearing
  Tag: `amb*`
    Tag: `amb*`
    - `FlexibleFoundation` -> `ffd*`
    - `MovingFoundation` -> `mfd*`

  ### JournalBearing
  Tag: `jrb*`
    Tag: `jrb*`
    - `FlexibleFoundation` -> `ffd*`
    - `MovingFoundation` -> `mfd*`
    - `SqueezeFilmDamper` -> `sfd*`

  ### LinearElasticModel
  Tag: `lemm*`
    Tag: `lemm*`
    - `Damping` -> `dmp*`

  ### RadialRollerBearing
  Tag: `rrb*`
    Tag: `rrb*`
    - `FlexibleFoundation` -> `ffd*`
    - `MovingFoundation` -> `mfd*`
    - `SqueezeFilmDamper` -> `sfd*`
  - `Disk` -> `disk*`
  - `FixAxRot` -> `far*`
  - `Free` -> `free*`
  - `Gravity` -> `gr*`
  - `MultiSpoolBearing` -> `msb*`
  - `RotorCoupling` -> `cpl*`
  - `RotorCrossSection` -> `rcs*`
  - `RotorSpeed` -> `rsp*`
  - `init` -> `init*`

### BioHeat
Tag: `ht`
  Tag: `ht`

  ### BiologicalTissue
  Tag: `bt*`
    Tag: `bt*`
    - `Bioheat` -> `bh*`
    - `Opacity` -> `opac*`
    - `ThermalDamage` -> `tdam*`

  ### IsothermalDomainInterface
  Tag: `idi*`
    Tag: `idi*`
    - `LayerOpacity` -> `lopac*`

  ### SolidHeatTransferModel
  Tag: `solid*`
    Tag: `solid*`
    - `Opacity` -> `opac*`
  - `AxialSymmetry` -> `axi*`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `HeatSource` -> `hs*`
  - `OpaqueSurface` -> `os*`
  - `TemperatureBoundary` -> `temp*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### BoltzmannEquation
Tag: `be`
  Tag: `be`
  - `BoltzmannModel` -> `bmdl*`
  - `CrossSectionImport` -> `xsec*`
  - `ElectronImpactReaction` -> `eir*`
  - `InitialValues` -> `init*`

### BoundaryModeAcoustics
Tag: `acbm`
  Tag: `acbm`
  - `FrequencyPressureAcousticsModel` -> `fpam*`
  - `SoundHard` -> `shb*`
  - `init` -> `init*`

### BoundaryModeAeroacoustics
Tag: `aebm`
  Tag: `aebm`
  - `AeroacousticsModel` -> `aem*`
  - `AxialSymmetry` -> `axi*`
  - `SoundHard` -> `shb*`
  - `init` -> `init*`

### BoundaryODE
Tag: `bode`
  Tag: `bode`
  - `DistributedODE` -> `dode*`
  - `init` -> `init*`

### Brinkman
Tag: `br`
  Tag: `br`
  - `AxialSymmetry` -> `axi*`
  - `FluidAndMatrixProperties` -> `fmp*`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `OutletBoundary` -> `out*`
  - `PressurePointConstraint` -> `prpc*`
  - `Symmetry` -> `sym*`
  - `VolumeForce` -> `vf*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### BubblyFlowkeps
Tag: `bf`
  Tag: `bf`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `gr*`
  - `PressurePointConstraint` -> `prpc*`
  - `Symmetry` -> `sym*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### ChargeTransport
Tag: `ct`
  Tag: `ct`
  - `AxialSymmetry` -> `axi*`
  - `NoFlux` -> `nflx*`
  - `Source` -> `st*`
  - `TransportProperties` -> `tp*`
  - `init` -> `init*`

### ChargedParticleTracing
Tag: `cpt`
  Tag: `cpt`

  ### Collisions
  Tag: `col*`
    Tag: `col*`
    - `Elastic` -> `ela*`
    - `NonResonantChargeExchange` -> `ncex*`
    - `ResonantChargeExchange` -> `cex*`

  ### ParticleMatterInteractions
  Tag: `pmi*`
    Tag: `pmi*`
    - `IonizationLoss` -> `il*`
    - `NuclearStopping` -> `ns*`
  - `AuxiliaryField` -> `aux*`
  - `AxialSymmetry` -> `axi*`
  - `ElectricForce` -> `ef*`
  - `Inlet` -> `inl*`
  - `MagneticForce` -> `mf*`
  - `ParticleBeam` -> `pbeam*`
  - `ParticleCounter` -> `pcnt*`
  - `ParticleProperties` -> `pp*`
  - `ParticlePropertiesOther` -> `pp*`
  - `Release` -> `rel*`
  - `ReleaseGrid` -> `relg*`
  - `Symmetry` -> `sym*`
  - `ThermionicEmission` -> `te*`
  - `VelocityReinitialization` -> `vre*`
  - `Wall` -> `wall*`

### Chemistry
Tag: `chem`
  Tag: `chem`

  ### SpeciesGroup
  Tag: `sg_rgr*`
    Tag: `sg_rgr*`
    - `SpeciesThermodynamics` -> `sthm*`
  - `ReactionChem` -> `rch*`
  - `ReversibleReactionGroup` -> `rgr*`
  - `SpeciesChem` -> `sch*`

### Circuit
Tag: `cir`
  Tag: `cir`

  ### SubCircuitBlock
  Tag: `sub*`
    Tag: `sub*`
    - `Capacitor` -> `C*`
    - `Inductor` -> `L*`
    - `Resistor` -> `R*`
    - `VoltageCurrentSource` -> `G*`
    - `VoltageVoltageSource` -> `V*`
  - `BjtNpn` -> `Q*`
  - `Capacitor` -> `C*`
  - `CurrentSourceCircuit` -> `I*`
  - `CurrentVoltageSource` -> `H*`
  - `Diode` -> `D*`
  - `GlobalEquations` -> `ge*`
  - `GroundNode` -> `gnd*`
  - `Inductor` -> `L*`
  - `ModelDeviceIV` -> `IvsU*`
  - `ModelTerminalIV` -> `termI*`
  - `Resistor` -> `R*`
  - `SubCircuit` -> `X*`
  - `VoltMeter` -> `vm*`
  - `VoltageSource` -> `V*`

### CoefficientFormBoundaryPDE
Tag: `cb`
  Tag: `cb`
  - `CoefficientFormPDE` -> `cfeq*`
  - `DirichletBoundary` -> `dir*`
  - `init` -> `init*`

### CoefficientFormPDE
Tag: `c`
  Tag: `c`
  - `CoefficientFormPDE` -> `cfeq*`
  - `DirichletBoundary` -> `dir*`
  - `FluxBoundary` -> `flux*`
  - `ZeroFluxBoundary` -> `zflx*`
  - `init` -> `init*`

### ColdPlasma
Tag: `plas`
  Tag: `plas`

  ### Species
  Tag: `sp*`
    Tag: `sp*`
    - `Outflow` -> `out*`
  - `AxialSymmetry` -> `axi*`
  - `ChargeConservation` -> `ccn*`
  - `CrossSectionImport` -> `xsec*`
  - `DielectricContact` -> `dct*`
  - `DisplacementField` -> `df*`
  - `ElectronImpactReaction` -> `eir*`
  - `ElectronOutlet` -> `eout*`
  - `Ground` -> `gnd*`
  - `InitialValues` -> `init*`
  - `Insulation` -> `ins*`
  - `MetalContact` -> `mct*`
  - `PlasmaEsModel` -> `pes*`
  - `Reaction` -> `rxn*`
  - `SurfaceChargeAccumulation` -> `sca*`
  - `SurfaceReaction` -> `sr*`
  - `Terminal` -> `term*`
  - `WallDriftDiffusion` -> `wall*`
  - `ZeroCharge` -> `zc*`

### CompressiblePotentialFlow
Tag: `cpf`
  Tag: `cpf`
  - `AxialSymmetry` -> `axi*`
  - `CompressiblePotentialFlow` -> `cpf*`
  - `MassFlow` -> `mf*`
  - `NormalFlow` -> `nf*`
  - `SlipVelocity` -> `slip*`
  - `init` -> `init*`

### ConcentratedSpecies
Tag: `tcs`
  Tag: `tcs`
  - `AxialSymmetry` -> `axi*`
  - `ConvectionDiffusionMigration` -> `cdm*`
  - `Inflow` -> `in*`
  - `MassFraction` -> `mf*`
  - `NoFlux` -> `nflx*`
  - `Outflow` -> `out*`
  - `ReactionSources` -> `reac*`
  - `ReactionWithTurbulenceModel` -> `treac*`
  - `Symmetry` -> `sym*`
  - `TCSPorousMediaTransportProperties` -> `pmtcs*`
  - `init` -> `init*`

### ConductiveMedia
Tag: `ec`
  Tag: `ec`

  ### PairElectricalContact
  Tag: `pelc*`
    Tag: `pelc*`
    - `ElectricInsulation` -> `ein*`
  - `AxialSymmetry` -> `axi*`
  - `ContactImpedance` -> `ci*`
  - `CurrentConservation` -> `cucn*`
  - `ElectricInsulation` -> `ein*`
  - `ElectricPotential` -> `pot*`
  - `ElectricShielding` -> `es*`
  - `ExternalCurrentDensity` -> `ecd*`
  - `Ground` -> `gnd*`
  - `NormalCurrentDensity` -> `ncd*`
  - `Terminal` -> `term*`
  - `init` -> `init*`

### ConductiveMediaShell
Tag: `ecs`
  Tag: `ecs`
  - `CurrentConservation` -> `cucn*`
  - `ElectricInsulation` -> `ein*`
  - `Ground` -> `gnd*`
  - `PiezoresistiveMaterial` -> `pzrm*`
  - `Terminal` -> `term*`
  - `init` -> `init*`

### ConvectedWaveEquation
Tag: `cwe`
  Tag: `cwe`
  - `AcousticImpedance` -> `imp*`
  - `ConvectedWaveEquationModel` -> `cwem*`
  - `NormalVelocity` -> `nvel*`
  - `SoundHardWall` -> `shw*`
  - `Symmetry` -> `sym*`
  - `init` -> `init*`

### ConvectionDiffusionEquation
Tag: `cdeq`
  Tag: `cdeq`
  - `ConvectionDiffusionEquation` -> `cdeq*`
  - `DirichletBoundary` -> `dir*`
  - `ZeroFluxBoundary` -> `zflx*`
  - `init` -> `init*`

### CreepingFlow
Tag: `spf`
  Tag: `spf`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `OpenBoundary` -> `open*`
  - `OutletBoundary` -> `out*`
  - `Symmetry` -> `sym*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### CurrentDistributionBEM
Tag: `cdbem`
  Tag: `cdbem`

  ### EdgeElectrode
  Tag: `edge*`
    Tag: `edge*`
    - `EdgeElectrodeReaction` -> `er*`
  - `Electrolyte` -> `ice*`
  - `ElectrolyteNormalCurrentDensityEdge` -> `icd*`
  - `Insulation` -> `ins*`
  - `InsulationEdge` -> `ins*`
  - `init2` -> `init*`

### CurrentDistributionShell
Tag: `cdsh`
  Tag: `cdsh`

  ### ExternalElectrodeSurface
  Tag: `eebii*`
    Tag: `eebii*`
    - `ElectrodeReaction` -> `er*`
  - `Electrolyte` -> `ice*`
  - `init` -> `init*`

### CurvilinearCoordinates
Tag: `cc`
  Tag: `cc`

  ### DiffusionMethod
  Tag: `diff*`
    Tag: `diff*`
    - `Inlet` -> `inl*`
    - `Outlet` -> `out*`
    - `WallDefault` -> `wall*`
  - `CoordinateSystemSettings` -> `css*`

### DarcysLaw
Tag: `dl`
  Tag: `dl`

  ### FractureFlow
  Tag: `dfn*`
    Tag: `dfn*`
    - `Aperture` -> `ap*`
    - `DarcysLawModel` -> `dlm*`
  - `AxialSymmetry` -> `axi*`
  - `DarcysLawModel` -> `dlm*`
  - `Gravity` -> `gr*`
  - `HydraulicHead` -> `hh*`
  - `Inlet` -> `inl*`
  - `LineMassSource` -> `lms*`
  - `MassFlux` -> `mf*`
  - `MassSource` -> `ms*`
  - `NoFlow` -> `nf*`
  - `Outlet` -> `out*`
  - `PointwiseConstraint` -> `constr*`
  - `PoroelasticMaterial` -> `psm*`
  - `Precipitation` -> `prec*`
  - `Pressure` -> `pr*`
  - `PressureHead` -> `ph*`
  - `StorageModel` -> `smm*`
  - `Symmetry` -> `sym*`
  - `Well` -> `well*`
  - `init` -> `init*`

### DeformedGeometry
Tag: `dg`
  Tag: `dg`
  - `FixedMesh` -> `fix*`
  - `FreeDeformation` -> `free`
  - `PrescribedDeformation` -> `pres*`
  - `PrescribedMeshDisplacement` -> `disp*`
  - `PrescribedMeshVelocity` -> `vel*`
  - `PrescribedNormalMeshVelocity` -> `pnmv*`
  - `ZeroNormalMeshDisplacement` -> `znmd*`

### DilutedSpecies
Tag: `tds`
  Tag: `tds`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`
    - `NoFlux` -> `nflx*`

  ### ConvectionDiffusionMigration
  Tag: `cdm*`
    Tag: `cdm*`
    - `TurbulentMixing` -> `tm*`

  ### ElectrodeElectrolyteInterfaceCoupling
  Tag: `eeic*`
    Tag: `eeic*`
    - `BoundaryReactionCoefficients` -> `rc*`

  ### PorousMedium
  Tag: `porous*`
    Tag: `porous*`
    - `FluidPorousMedium` -> `fluid*`
    - `PorousMatrixPorousMedium` -> `pm*`
  - `AxialSymmetry` -> `axi*`
  - `Concentration` -> `conc*`
  - `FluxBoundary` -> `fl*`
  - `Inflow` -> `in*`
  - `MassSourceLine` -> `lms*`
  - `NoFlux` -> `nflx*`
  - `Outflow` -> `out*`
  - `PartitionCondition` -> `pac*`
  - `Reactions` -> `reac*`
  - `SurfaceEquilibriumReaction` -> `seqreac*`
  - `SurfaceReactionsFlux` -> `srf*`
  - `Symmetry` -> `sym*`
  - `ThinImpermeableBarrier` -> `tib*`
  - `init` -> `init*`

### DilutedSpeciesInPorousMedia
Tag: `tds`
  Tag: `tds`

  ### PorousMedium
  Tag: `porous*`
    Tag: `porous*`
    - `Adsorptions` -> `ads*`
    - `Dispersion` -> `disp*`
    - `FluidPorousMedium` -> `fluid*`
    - `PorousMatrixPorousMedium` -> `pm*`

  ### ReactivePelletBed
  Tag: `rpb*`
    Tag: `rpb*`
    - `Diffusion` -> `df*`
    - `Reactionx` -> `reac*`
    - `initcx` -> `init*`

  ### UnsaturatedPorousMedium
  Tag: `usporous*`
    Tag: `usporous*`
    - `Adsorptions` -> `ads*`
    - `Dispersion` -> `disp*`
    - `GasUnsaturatedPorousMedium` -> `gas*`
    - `LiquidUnsaturatedPorousMedium` -> `liquid*`
    - `PorousMatrixPorousMedium` -> `pm*`
  - `AxialSymmetry` -> `axi*`
  - `Concentration` -> `conc*`
  - `ConvectionDiffusionMigration` -> `cdm*`
  - `Inflow` -> `in*`
  - `NoFlux` -> `nflx*`
  - `Outflow` -> `out*`
  - `Reactions` -> `reac*`
  - `Symmetry` -> `sym*`
  - `Volatilization` -> `vola*`
  - `init` -> `init*`

### DomainODE
Tag: `dode`
  Tag: `dode`
  - `DistributedODE` -> `dode*`
  - `init` -> `init*`

### EdgeODE
Tag: `eode`
  Tag: `eode`
  - `DistributedODE` -> `dode*`
  - `init` -> `init*`

### ElasticWavesTimeExplicit
Tag: `elte`
  Tag: `elte`
  - `AxialSymmetry` -> `axi*`
  - `BodyLoad` -> `bl*`
  - `BoundaryLoad` -> `bndl*`
  - `ElasticWavesTimeExplicitModel` -> `eltem*`
  - `Free` -> `free*`
  - `LowReflectingBoundary` -> `lrb*`
  - `MaterialDiscontinuityElem` -> `mde*`
  - `init` -> `init*`

### ElectricCurrentsShell
Tag: `ecis`
  Tag: `ecis`

  ### ConductiveShell
  Tag: `csh*`
    Tag: `csh*`
    - `BoundaryGround` -> `bgnd*`
    - `BoundaryTerminal` -> `bterm*`
    - `ElectricPotential` -> `pot*`
    - `Ground` -> `gnd*`
    - `Terminal` -> `term*`
  - `BoundaryElectricPotential` -> `bpot*`
  - `BoundaryGround` -> `bgnd*`
  - `ContinuityLayeredShell` -> `cls*`
  - `ElectricInsulation` -> `ein*`
  - `InsulatingLayer` -> `inl*`
  - `PiezoelectricLayer` -> `epzml*`

### ElectricInductionCurrents
Tag: `mef`
  Tag: `mef`

  ### MagneticInsulation
  Tag: `mi*`
    Tag: `mi*`
    - `ElectricInsulation` -> `ein*`
  - `AmperesLaw` -> `al*`
  - `AxialSymmetry` -> `axi*`
  - `ElectromagneticModel` -> `alc*`
  - `RLCCoilGroup` -> `rlccg*`
  - `Velocity` -> `vlt*`
  - `init` -> `init*`

### ElectricalBreakdownDetection
Tag: `ebd`
  Tag: `ebd`
  - `Cathode` -> `cod*`
  - `ElectricalBreakdownDetection` -> `ebd*`
  - `ParticleCounter` -> `pcnt*`
  - `Wall` -> `wall*`

### ElectrodeShell
Tag: `els`
  Tag: `els`
  - `AxialSymmetry` -> `axi*`
  - `DepositingElectrode` -> `depe*`
  - `ElectricInsulation` -> `ein*`
  - `Electrode` -> `ece*`
  - `Ground` -> `gnd*`
  - `NormalCurrentDensity` -> `ncd*`
  - `init` -> `init*`

### ElectromagneticWaves
Tag: `emw`
  Tag: `emw`

  ### FarFieldDomain
  Tag: `ffd*`
    Tag: `ffd*`
    - `FarFieldCalculation` -> `ffc*`

  ### LumpedPort
  Tag: `lport*`
    Tag: `lport*`
    - `UniformElement` -> `ue*`

  ### Port
  Tag: `port*`
    Tag: `port*`
    - `CircularPortReferenceAxis` -> `cportv*`
    - `ElectricPotential` -> `pot*`
    - `Ground` -> `gnd*`
  - `AxialSymmetry` -> `axi*`
  - `Impedance` -> `imp*`
  - `LumpedElement` -> `lelement*`
  - `MixedModeSparameters` -> `mms*`
  - `PerfectElectricConductor` -> `pec*`
  - `PerfectMagneticConductor` -> `pmc*`
  - `PeriodicCondition` -> `pc*`
  - `Scattering` -> `sctr*`
  - `SpecificAbsorptionRate` -> `sar*`
  - `SurfaceCurrent` -> `scu*`
  - `TransitionBoundaryCondition` -> `trans*`
  - `WaveEquationElectric` -> `wee*`
  - `init` -> `init*`

### ElectromagneticWavesBeamEnvelopes
Tag: `ewbe`
  Tag: `ewbe`

  ### MatchedBoundaryCondition
  Tag: `mbc*`
    Tag: `mbc*`
    - `ReferencePoint` -> `rpnt*`

  ### Scattering
  Tag: `sctr*`
    Tag: `sctr*`
    - `ReferencePoint` -> `rpnt*`
  - `FieldContinuity` -> `fcont*`
  - `Impedance` -> `imp*`
  - `PerfectElectricConductor` -> `pec*`
  - `PerfectMagneticConductor` -> `pmc*`
  - `PeriodicCondition` -> `pc*`
  - `Port` -> `port*`
  - `TransitionBoundaryCondition` -> `trans*`
  - `WaveEquationBeamEnvelopes` -> `webe*`
  - `init` -> `init*`

### ElectromagneticWavesFrequencyDomain
Tag: `ewfd`
  Tag: `ewfd`

  ### FarFieldDomain
  Tag: `ffd*`
    Tag: `ffd*`
    - `FarFieldCalculation` -> `ffc*`

  ### Port
  Tag: `port*`
    Tag: `port*`
    - `DiffractionOrder` -> `dport*`
    - `OrthogonalPolarization` -> `oport*`
    - `PeriodicPortReferencePoint` -> `pportp*`
  - `AxialSymmetry` -> `axi*`
  - `GlobalEquations` -> `ge*`
  - `Impedance` -> `imp*`
  - `PerfectElectricConductor` -> `pec*`
  - `PerfectMagneticConductor` -> `pmc*`
  - `PeriodicCondition` -> `pc*`
  - `Polarization` -> `pol*`
  - `Scattering` -> `sctr*`
  - `SurfaceCurrent` -> `scu*`
  - `TransitionBoundaryCondition` -> `trans*`
  - `WaveEquationElectric` -> `wee*`
  - `init` -> `init*`

### ElectromagneticWavesTransient
Tag: `ewt`
  Tag: `ewt`

  ### WaveEquationElectric
  Tag: `wee*`
    Tag: `wee*`
    - `DrudeLorentzPolarization` -> `dlp*`
  - `GlobalEquations` -> `ge*`
  - `PerfectElectricConductor` -> `pec*`
  - `PerfectMagneticConductor` -> `pmc*`
  - `PeriodicCondition` -> `pc*`
  - `Scattering` -> `sctr*`
  - `init` -> `init*`

### ElectrophoreticTransport
Tag: `el`
  Tag: `el`

  ### Ampholyte
  Tag: `amph*`
    Tag: `amph*`
    - `InitialConcentration` -> `initc*`
    - `NoFlux` -> `nflx*`

  ### Protein
  Tag: `prot*`
    Tag: `prot*`
    - `Inflow` -> `in*`
    - `InitialConcentration` -> `initc*`
    - `NoFlux` -> `nflx*`
    - `Outflow` -> `out*`

  ### WeakAcid
  Tag: `wa*`
    Tag: `wa*`
    - `Concentration` -> `conc*`
    - `Inflow` -> `in*`
    - `InitialConcentration` -> `initc*`
    - `NoFlux` -> `nflx*`
    - `Outflow` -> `out*`

  ### WeakBase
  Tag: `wb*`
    Tag: `wb*`
    - `Concentration` -> `conc*`
    - `Inflow` -> `in*`
    - `InitialConcentration` -> `initc*`
    - `NoFlux` -> `nflx*`
    - `Outflow` -> `out*`
  - `ElectrolyteNormalCurrentDensity` -> `icd*`
  - `ElectrolytePotential` -> `eip*`
  - `Insulation` -> `ins*`
  - `Solvent` -> `sol*`
  - `init` -> `init*`

### Electrostatics
Tag: `es`
  Tag: `es`

  ### DomainTerminal
  Tag: `term*`
    Tag: `term*`
    - `HarmonicPerturbation` -> `hp*`

  ### ElectricPotential
  Tag: `pot*`
    Tag: `pot*`
    - `HarmonicPerturbation` -> `hp*`
  - `AxialSymmetry` -> `axi*`
  - `ChargeConservation` -> `ccn*`
  - `ChargeConservationFerroelectric` -> `ccnf*`
  - `ChargeConservationPiezo` -> `ccnp*`
  - `DielectricShielding` -> `des*`
  - `DisplacementField` -> `df*`
  - `FloatingPotential` -> `fp*`
  - `GlobalEquations` -> `ge*`
  - `Ground` -> `gnd*`
  - `PeriodicCondition` -> `pc*`
  - `SpaceChargeDensity` -> `scd*`
  - `SurfaceChargeDensity` -> `sfcd*`
  - `Terminal` -> `term*`
  - `ZeroCharge` -> `zc*`
  - `init` -> `init*`

### ElectrostaticsBoundaryElements
Tag: `esbe`
  Tag: `esbe`
  - `ChargeConservation` -> `ccn*`
  - `FloatingPotential` -> `fp*`
  - `Ground` -> `gnd*`
  - `Terminal` -> `term*`
  - `ZeroCharge` -> `zc*`
  - `ZeroChargeEdge` -> `zc*`
  - `init2` -> `init*`

### Events
Tag: `ev`
  Tag: `ev`
  - `DiscreteStates` -> `ds*`
  - `ExplicitEvent` -> `expl*`
  - `ImplicitEvent` -> `impl*`
  - `IndicatorStates` -> `is*`

### Fatigue
Tag: `ftg`
  Tag: `ftg`
  - `CumulativeDamageModel2` -> `cdam*`
  - `EnergyBasedModel` -> `ener*`
  - `StrainBasedModel` -> `stra*`
  - `StrainLifeModel` -> `elif*`
  - `StressBasedModel` -> `stre*`
  - `StressLifeModel` -> `slif*`

### FlowInPipes
Tag: `pfl`
  Tag: `pfl`
  - `Bend` -> `bend*`
  - `FluidProperties` -> `fp*`
  - `Inlet` -> `inl*`
  - `LosslessFitting` -> `lf*`
  - `PhaseFractions` -> `phf*`
  - `PipeProperties` -> `pipe*`
  - `Pressure` -> `pr*`
  - `Valve` -> `valve*`
  - `VolumeForce` -> `vf*`
  - `init` -> `init*`

### FluidParticleTracing
Tag: `fpt`
  Tag: `fpt`

  ### DielectrophoreticForce
  Tag: `deff*`
    Tag: `deff*`
    - `Shell` -> `shl*`

  ### Wall
  Tag: `wall*`
    Tag: `wall*`
    - `Erosion` -> `ero*`
  - `BrownianForce` -> `bf*`
  - `ChargeAccumulation` -> `cacc*`
  - `DragForce` -> `df*`
  - `ElectricForce` -> `ef*`
  - `Inlet` -> `inl*`
  - `LiftForce` -> `lf*`
  - `Outlet` -> `out*`
  - `PairContinuity` -> `pcon*`
  - `ParticleCounter` -> `pcnt*`
  - `ParticleProperties` -> `pp*`
  - `ParticlePropertiesOther` -> `pp*`
  - `ReleaseGrid` -> `relg*`
  - `Symmetry` -> `sym*`

### FreeAndPorousMediaFlow
Tag: `fp`
  Tag: `fp`
  - `FluidAndMatrixProperties` -> `fmp*`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `OutletBoundary` -> `out*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### FreeMolecularFlow
Tag: `fmf`
  Tag: `fmf`
  - `AxialSymmetry` -> `axi*`
  - `Evaporation` -> `evap*`
  - `FreeMolecularFlowProperties` -> `fmfp*`
  - `NumberDensityReconDomain` -> `ndr*`
  - `NumberDensityReconEdge` -> `ndr*`
  - `PlaneSymmetry` -> `sym*`
  - `Reservoir` -> `res*`
  - `SurfaceTemperature` -> `st*`
  - `TotalVacuum` -> `tv*`
  - `VacuumPump` -> `pmp*`
  - `Wall` -> `wall*`
  - `init` -> `init*`

### FrequencyPipeAcoustics
Tag: `pafd`
  Tag: `pafd`
  - `Closed` -> `closed*`
  - `EndImpedance` -> `endimp*`
  - `FluidProperties` -> `fp*`
  - `PipeProperties` -> `pipe*`
  - `Pressure` -> `pres*`
  - `VolumeForce` -> `vf*`
  - `init` -> `init*`

### GeneralFormBoundaryPDE
Tag: `gb`
  Tag: `gb`
  - `GeneralFormPDE` -> `gfeq*`
  - `init` -> `init*`

### GeneralFormPDE
Tag: `g`
  Tag: `g`
  - `Constraint` -> `cons*`
  - `DirichletBoundary` -> `dir*`
  - `FluxBoundary` -> `flux*`
  - `GeneralFormPDE` -> `gfeq*`
  - `PeriodicCondition` -> `pc*`
  - `ZeroFluxBoundary` -> `zflx*`
  - `init` -> `init*`

### GeneralOptimization
Tag: `opt`
  Tag: `opt`

  ### ControlVariableField
  Tag: `cvar*`
    Tag: `cvar*`
    - `ControlVariableBounds` -> `bound*`

  ### GlobalLeastSquaresObjective
  Tag: `glsobj*`
    Tag: `glsobj*`
    - `ValueColumn` -> `v*`

  ### LeastSquaresObjective
  Tag: `lsobj*`
    Tag: `lsobj*`
    - `CoordinateColumn` -> `c*`
    - `ValueColumn` -> `v*`
  - `GlobalControlVariables` -> `gcvar*`
  - `GlobalObjective` -> `gobj*`
  - `IntegralInequality` -> `iconstr*`
  - `IntegralObjective` -> `iobj*`

### GeometricalOptics
Tag: `gop`
  Tag: `gop`

  ### CrossGrating
  Tag: `xgrat*`
    Tag: `xgrat*`
    - `CrossDiffractionOrder` -> `xdfo*`

  ### Grating
  Tag: `grat*`
    Tag: `grat*`
    - `DiffractionOrder` -> `dfo*`

  ### MaterialDiscontinuity
  Tag: `matd*`
    Tag: `matd*`
    - `ThinDielectricFilm` -> `film*`

  ### Wall
  Tag: `wall*`
    Tag: `wall*`
    - `BoundaryAccumulator` -> `bacc*`
    - `DepositedRayPowerBoundary` -> `bsrc*`
  - `GlobalEquations` -> `ge*`
  - `IlluminatedSurface` -> `ill*`
  - `LinearPolarizer` -> `lpol*`
  - `LinearWaveRetarder` -> `lwav*`
  - `MediumProperties` -> `mp*`
  - `Mirror` -> `mir*`
  - `RayProperties` -> `op*`
  - `RayTermination` -> `rt*`
  - `ReleaseFromBoundary` -> `relb*`
  - `ReleaseFromElectricField` -> `rele*`
  - `ReleaseFromFarFieldRadiationPattern` -> `rffr*`
  - `ReleaseFromPoint` -> `rpt*`
  - `ReleaseGrid` -> `relg*`
  - `SolarRadiation` -> `srad*`

### GlobalEquations
Tag: `ge`
  Tag: `ge`
  - `GlobalEquations` -> `ge*`

### HeatTransfer
Tag: `ht`
  Tag: `ht`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`

    ### IsothermalDomainInterface
    Tag: `idi*`
      Tag: `idi*`
      - `LayerOpacity` -> `lopac*`
    - `ThermalInsulation` -> `ins*`

  ### FluidHeatTransferModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `Opacity` -> `opac*`
    - `PhaseChangeMaterial` -> `phc*`

  ### FluidLayeredShell
  Tag: `fls*`
    Tag: `fls*`
    - `ThermalInsulation` -> `ins*`
    - `init` -> `init*`

  ### IsothermalDomain
  Tag: `id*`
    Tag: `id*`
    - `Opacity` -> `opac*`

  ### IsothermalDomainInterface
  Tag: `idi*`
    Tag: `idi*`
    - `LayerOpacity` -> `lopac*`

  ### PairBoundaryHeatSource
  Tag: `pbhs*`
    Tag: `pbhs*`

    ### IsothermalDomainInterface
    Tag: `idi*`
      Tag: `idi*`
      - `LayerOpacity` -> `lopac*`
    - `ThermalInsulation` -> `ins*`

  ### PairThermalContact
  Tag: `ptc*`
    Tag: `ptc*`

    ### IsothermalDomainInterface
    Tag: `idi*`
      Tag: `idi*`
      - `LayerOpacity` -> `lopac*`
    - `ThermalInsulation` -> `ins*`

  ### SolidHeatTransferModel
  Tag: `solid*`
    Tag: `solid*`
    - `Opacity` -> `opac*`
    - `TranslationalMotion` -> `trm*`

  ### SolidLayeredShell
  Tag: `sls*`
    Tag: `sls*`
    - `ThermalInsulation` -> `ins*`
    - `init` -> `init*`
  - `AxialSymmetry` -> `axi*`
  - `BoundaryHeatSource` -> `bhs*`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `DepositedBeamPower` -> `dbp*`
  - `GlobalEquations` -> `ge*`
  - `HeatFluxBoundary` -> `hf*`
  - `HeatSource` -> `hs*`
  - `LineHeatSource` -> `lihs*`
  - `LumpedSystemConnector` -> `lsc*`
  - `OpaqueSurface` -> `os*`
  - `PeriodicHeat` -> `pc*`
  - `PointwiseConstraint` -> `constr*`
  - `SurfaceToAmbientRadiation` -> `sar*`
  - `Symmetry` -> `sym*`
  - `TemperatureBoundary` -> `temp*`
  - `ThermalContact` -> `tc*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### HeatTransferInBuildingMaterials
Tag: `ht`
  Tag: `ht`

  ### BuildingMaterialHeatTransferModel
  Tag: `bm*`
    Tag: `bm*`
    - `Opacity` -> `opac*`

  ### IsothermalDomainInterface
  Tag: `idi*`
    Tag: `idi*`
    - `LayerOpacity` -> `lopac*`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `HeatFluxBoundary` -> `hf*`
  - `OpaqueSurface` -> `os*`
  - `TemperatureBoundary` -> `temp*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### HeatTransferInFilmsLM
Tag: `htlsh`
  Tag: `htlsh`
  - `FluidLayeredShell` -> `fls*`
  - `HeatSource` -> `hs*`
  - `TemperatureInterface` -> `tempi*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### HeatTransferInFluids
Tag: `ht`
  Tag: `ht`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`

    ### IsothermalDomainInterface
    Tag: `idi*`
      Tag: `idi*`
      - `LayerOpacity` -> `lopac*`
    - `ThermalInsulation` -> `ins*`

  ### FluidHeatTransferModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `Opacity` -> `opac*`
    - `PhaseChangeMaterial` -> `phc*`
    - `PressureWork` -> `pw*`

  ### IsothermalDomainInterface
  Tag: `idi*`
    Tag: `idi*`
    - `LayerOpacity` -> `lopac*`

  ### MoistAirHeatTransferModel
  Tag: `ma*`
    Tag: `ma*`
    - `Opacity` -> `opac*`

  ### PorousMediumHeatTransferModel
  Tag: `porous*`
    Tag: `porous*`
    - `FluidPorousMediumHeatTransferModel` -> `fluid*`
    - `PorousMatrixPorousMediumHeatTransferModel` -> `pm*`

  ### SolidHeatTransferModel
  Tag: `solid*`
    Tag: `solid*`
    - `Opacity` -> `opac*`

  ### SolidLayeredShell
  Tag: `sls*`
    Tag: `sls*`
    - `ThermalInsulation` -> `ins*`
    - `init` -> `init*`
  - `AxialSymmetry` -> `axi*`
  - `BoundaryHeatSource` -> `bhs*`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `ConvectiveOutflow` -> `ofl*`
  - `HeatFluxBoundary` -> `hf*`
  - `HeatSource` -> `hs*`
  - `Inflow` -> `ifl*`
  - `OpaqueSurface` -> `os*`
  - `SurfaceToAmbientRadiation` -> `sar*`
  - `Symmetry` -> `sym*`
  - `TemperatureBoundary` -> `temp*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### HeatTransferInMoistAir
Tag: `ht`
  Tag: `ht`

  ### FluidHeatTransferModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `ConvectivelyEnhancedConductivity` -> `cec*`
    - `Opacity` -> `opac*`

  ### IsothermalDomainInterface
  Tag: `idi*`
    Tag: `idi*`
    - `LayerOpacity` -> `lopac*`

  ### MoistAirHeatTransferModel
  Tag: `ma*`
    Tag: `ma*`
    - `Opacity` -> `opac*`

  ### SolidHeatTransferModel
  Tag: `solid*`
    Tag: `solid*`
    - `Opacity` -> `opac*`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `Inflow` -> `ifl*`
  - `OpaqueSurface` -> `os*`
  - `OpenBoundary` -> `open*`
  - `Symmetry` -> `sym*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### HeatTransferInShellsLM
Tag: `htlsh`
  Tag: `htlsh`
  - `ContinuityLayeredShell` -> `contls*`
  - `DepositedBeamPowerInterface` -> `dbpi*`
  - `HeatFlux` -> `lhf*`
  - `HeatFluxInterface` -> `hfi*`
  - `LineTemperature` -> `ltemp*`
  - `SolidLayeredShell` -> `sls*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### HeatTransferInSolidsAndFluids
Tag: `ht`
  Tag: `ht`

  ### FluidHeatTransferModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `Opacity` -> `opac*`

  ### IsothermalDomain
  Tag: `id*`
    Tag: `id*`
    - `Opacity` -> `opac*`

  ### IsothermalDomainInterface
  Tag: `idi*`
    Tag: `idi*`
    - `LayerOpacity` -> `lopac*`

  ### MoistAirHeatTransferModel
  Tag: `ma*`
    Tag: `ma*`
    - `Opacity` -> `opac*`

  ### SolidHeatTransferModel
  Tag: `solid*`
    Tag: `solid*`
    - `Opacity` -> `opac*`

  ### SolidLayeredShell
  Tag: `sls*`
    Tag: `sls*`
    - `ThermalInsulation` -> `ins*`
    - `init` -> `init*`
  - `AxialSymmetry` -> `axi*`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `ConvectiveOutflow` -> `ofl*`
  - `GlobalEquations` -> `ge*`
  - `HeatFluxBoundary` -> `hf*`
  - `HeatSource` -> `hs*`
  - `Inflow` -> `ifl*`
  - `OpaqueSurface` -> `os*`
  - `OpenBoundary` -> `open*`
  - `PeriodicHeat` -> `pc*`
  - `PhaseChangeInterface` -> `pci*`
  - `SurfaceToAmbientRadiation` -> `sar*`
  - `Symmetry` -> `sym*`
  - `TemperatureBoundary` -> `temp*`
  - `ThermalContact` -> `tc*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### HeatTransferPipes
Tag: `htp`
  Tag: `htp`

  ### WallHeatTransfer
  Tag: `wht*`
    Tag: `wht*`
    - `InternalFilmResistance` -> `intfilm*`
    - `WallLayer` -> `wall*`
  - `HeatOutflow` -> `hofl*`
  - `HeatTransfer` -> `ht*`
  - `PipeProperties` -> `pipe*`
  - `Temperature` -> `temp*`
  - `init` -> `init*`

### HeavySpeciesTransport
Tag: `hs`
  Tag: `hs`
  - `ConvectionDiffusion` -> `cdm*`
  - `Species` -> `sp*`
  - `SurfaceReaction` -> `sr*`
  - `SurfaceSpecies` -> `ssp*`

### HermitianBeam
Tag: `beam`
  Tag: `beam`

  ### CrossSectionBeam
  Tag: `csd*`
    Tag: `csd*`
    - `BeamSectionOrientation` -> `so*`

  ### EdgeLoad
  Tag: `el*`
    Tag: `el*`
    - `Phase` -> `ph*`

  ### Elastic
  Tag: `emm*`
    Tag: `emm*`
    - `Damping` -> `dmp*`
    - `ThermalExpansion` -> `te*`
  - `AddedMass1` -> `adm*`
  - `DispRot0` -> `pdr*`
  - `Fixed` -> `fix*`
  - `Free` -> `free*`
  - `Gravity` -> `gr*`
  - `Pinned` -> `pin*`
  - `PointLoad` -> `pl*`
  - `PointMass` -> `pm*`
  - `init` -> `init*`

### HighMachNumberFlow
Tag: `hmnf`
  Tag: `hmnf`

  ### HighMachNumberFlowModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `Opacity` -> `opac*`
  - `GlobalEquations` -> `ge*`
  - `Gravity` -> `grav*`
  - `HighMachNumberFlowInlet` -> `hminl*`
  - `HighMachNumberFlowOutlet` -> `hmout*`
  - `Symmetry` -> `sym*`
  - `ThermalInsulation` -> `ins*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### HighMachNumberFlowTurbulentSpalartAllmaras
Tag: `hmnf`
  Tag: `hmnf`

  ### HighMachNumberFlowModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `Opacity` -> `opac*`
  - `Gravity` -> `grav*`
  - `HighMachNumberFlowInlet` -> `hminl*`
  - `HighMachNumberFlowOutlet` -> `hmout*`
  - `ThermalInsulation` -> `ins*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### HighMachNumberFlowTurbulentkeps
Tag: `hmnf`
  Tag: `hmnf`

  ### HighMachNumberFlowModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `Opacity` -> `opac*`
  - `AxialSymmetry` -> `axi*`
  - `Gravity` -> `grav*`
  - `HighMachNumberFlowInlet` -> `hminl*`
  - `HighMachNumberFlowOutlet` -> `hmout*`
  - `ThermalInsulation` -> `ins*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### HydrodynamicBearing
Tag: `hdb`
  Tag: `hdb`

  ### FloatingRingBearing
  Tag: `frb*`
    Tag: `frb*`
    - `FlexibleFoundation` -> `ffd*`
    - `InnerFilmProperties` -> `if*`
    - `InnerOuterFilmConnection` -> `fc*`
    - `MovingFoundation` -> `mfd*`
    - `OuterFilmProperties` -> `of*`

  ### HydrodynamicJournalBearing
  Tag: `hjb*`
    Tag: `hjb*`
    - `FlexibleFoundation` -> `ffd*`
    - `Misalignment` -> `mlgn*`
    - `MovingFoundation` -> `mfd*`
    - `SqueezeFilmDamper` -> `sfd*`

  ### HydrodynamicThrustBearing
  Tag: `htb*`
    Tag: `htb*`
    - `FlexibleFoundation` -> `ffd*`
    - `MovingFoundation` -> `mfd*`
  - `BearingOrientation` -> `bax*`
  - `Border` -> `bdr*`
  - `SqueezeFilmDamper` -> `sfd*`
  - `init` -> `init*`

### InductionCurrents
Tag: `mf`
  Tag: `mf`

  ### AmperesLaw
  Tag: `al*`
    Tag: `al*`
    - `LossCalculation` -> `loss*`

  ### Coil
  Tag: `coil*`
    Tag: `coil*`

    ### CoilCurrentCalculation
    Tag: `ccc*`
      Tag: `ccc*`
      - `CoilGround` -> `cg*`
      - `CoilTerminal` -> `ct*`

    ### UserDefinedCoilGeometry
    Tag: `cg*`
      Tag: `cg*`
      - `CoilInput` -> `ci*`
      - `CoilOutput` -> `co*`
    - `CoilHarmonicPerturbation` -> `hp*`
    - `CoilReferenceEdge` -> `cre*`
    - `LossCalculation` -> `loss*`
    - `ReverseCoilGroupDomain` -> `rcd*`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`
    - `MagneticInsulation` -> `mi*`
  - `AmperesLawMagnetostrictive` -> `alm*`
  - `AxialSymmetry` -> `axi*`
  - `EdgeCurrent` -> `edc*`
  - `ExternalCurrentDensity` -> `ecd*`
  - `ForceCalculation` -> `fcal*`
  - `GaugeFixingA` -> `gfa*`
  - `GlobalEquations` -> `ge*`
  - `Impedance` -> `imp*`
  - `LumpedPort` -> `lport*`
  - `MagneticInsulation` -> `mi*`
  - `PerfectMagneticConductor` -> `pmc*`
  - `SurfaceCurrent` -> `scu*`
  - `ThinLowPermeabilityGap` -> `tg*`
  - `Velocity` -> `vlt*`
  - `init` -> `init*`

### LaminarBubblyFlow
Tag: `bf`
  Tag: `bf`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `gr*`
  - `InletBoundary` -> `inl*`
  - `OutletBoundary` -> `out*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### LaminarFlow
Tag: `spf`
  Tag: `spf`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`
    - `Wall` -> `wall*`
    - `WallBC` -> `wallbc*`

  ### FluidFluidInterface
  Tag: `ffi*`
    Tag: `ffi*`
    - `ContactAngle` -> `cnta*`

  ### FreeSurface
  Tag: `fs*`
    Tag: `fs*`
    - `ContactAngle` -> `cnta*`
  - `AxialSymmetry` -> `axi*`
  - `BoundaryStress` -> `bs*`
  - `FluidAndMatrixProperties` -> `fmp*`
  - `FluidProperties` -> `fp*`
  - `GlobalEquations` -> `ge*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `InteriorWallBC` -> `iwbc*`
  - `MassSource` -> `ms*`
  - `OpenBoundary` -> `open*`
  - `OutletBoundary` -> `out*`
  - `PointwiseConstraint` -> `constr*`
  - `PressurePointConstraint` -> `prpc*`
  - `Screen` -> `sc*`
  - `Symmetry` -> `sym*`
  - `VolumeForce` -> `vf*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### LaplaceEquation
Tag: `lpeq`
  Tag: `lpeq`
  - `DirichletBoundary` -> `dir*`
  - `FluxBoundary` -> `flux*`
  - `LaplaceEquation` -> `leq*`
  - `PointSourceTerm` -> `ptsrc*`
  - `ZeroFluxBoundary` -> `zflx*`
  - `init` -> `init*`

### LayeredShell
Tag: `lshell`
  Tag: `lshell`
  - `BodyLoad` -> `bl*`
  - `BoundaryLoad` -> `bndl*`
  - `ContinuityLayeredShell` -> `contls*`
  - `Delamination` -> `del*`
  - `Displacement` -> `disp*`
  - `DisplacementIntEP` -> `dispi*`
  - `EdgeLoad` -> `el*`
  - `FaceLoad` -> `fl*`
  - `Fixed` -> `fix*`
  - `Free` -> `free*`
  - `GlobalEquations` -> `ge*`
  - `LineLoad` -> `ll*`
  - `LinearElasticModel` -> `lemm*`
  - `PiezoelectricMaterialModel` -> `pzm*`
  - `RigidMotionSuppression` -> `rms*`
  - `Roller` -> `roll*`
  - `Symmetry` -> `sym*`
  - `init` -> `init*`

### LevelSet
Tag: `ls`
  Tag: `ls`
  - `AxialSymmetry` -> `axi*`
  - `InletBoundary` -> `inl*`
  - `LevelSetModel` -> `lsm*`
  - `NoFlow` -> `nf*`
  - `Outlet` -> `out*`
  - `SymmetryFluid` -> `sym*`
  - `init` -> `init*`
  - `initFluid2` -> `initfluid*`

### LinearizedNavierStokesFrequency
Tag: `lnsf`
  Tag: `lnsf`
  - `BackgroundAcousticFields` -> `baf*`
  - `LinearizedNavierStokesModel` -> `lnsm*`
  - `Symmetry` -> `sym*`
  - `Wall` -> `wall*`
  - `init` -> `init*`

### LumpedMechanicalSystem
Tag: `lms`
  Tag: `lms`

  ### SubSystemBlock
  Tag: `sub*`
    Tag: `sub*`
    - `Damper` -> `C*`
    - `FreeNode` -> `fr*`
    - `Mass` -> `M*`
    - `Spring` -> `K*`
  - `Damper` -> `C*`
  - `DisplacementNode` -> `disp*`
  - `ExternalSource` -> `E*`
  - `FixedNode` -> `fix*`
  - `ForceNode` -> `frc*`
  - `Mass` -> `M*`
  - `Spring` -> `K*`
  - `SubSystem` -> `X*`

### LumpedThermalSystem
Tag: `lts`
  Tag: `lts`
  - `ConductiveThermalResistor` -> `R*`
  - `ExternalTerminal` -> `term*`

### MagneticFieldFormulation
Tag: `mfh`
  Tag: `mfh`
  - `FaradaysLaw` -> `fl*`
  - `MagneticFieldBoundary` -> `mfb*`
  - `MagneticGaussLaw` -> `mgl*`
  - `MagneticInsulation` -> `mi*`
  - `init` -> `init*`

### MagneticFieldsCurrentsOnly
Tag: `mfco`
  Tag: `mfco`

  ### Conductor
  Tag: `cond*`
    Tag: `cond*`
    - `Ground` -> `gnd*`
    - `Terminal` -> `term*`
  - `ExteriorBoundaries` -> `ext*`
  - `FreeSpace` -> `free*`
  - `init` -> `init*`

### MagneticFieldsNoCurrentsBoundaryElements
Tag: `mfncbe`
  Tag: `mfncbe`
  - `ForceCalculation` -> `fcal*`
  - `MagneticFluxConservation` -> `mfc*`
  - `MagneticFluxDensity` -> `mflx*`
  - `MagneticInsulation` -> `mi*`
  - `ZeroMagneticScalarPotential` -> `zsp*`
  - `init2` -> `init*`

### MagnetostaticsNoCurrents
Tag: `mfnc`
  Tag: `mfnc`
  - `ExternalMagneticFluxDensity` -> `exfd*`
  - `ForceCalculation` -> `fcal*`
  - `MagneticFluxConservation` -> `mfc*`
  - `MagneticInsulation` -> `mi*`
  - `MagneticShielding` -> `ms*`
  - `ZeroMagneticScalarPotential` -> `zsp*`
  - `init` -> `init*`

### MathParticle
Tag: `pt`
  Tag: `pt`
  - `AuxiliaryField` -> `aux*`
  - `DomainAccumulator` -> `dacc*`
  - `Force` -> `for*`
  - `Inlet` -> `inl*`
  - `Outlet` -> `out*`
  - `ParticleCounter` -> `pcnt*`
  - `ParticleParticleInteraction` -> `ppi*`
  - `ParticleProperties` -> `pp*`
  - `Release` -> `rel*`
  - `ReleaseGrid` -> `relg*`
  - `RotatingFrame` -> `rf*`
  - `ThermalReEmission` -> `tre*`
  - `Wall` -> `wall*`

### MoistureTransportInAir
Tag: `mt`
  Tag: `mt`
  - `Gravity` -> `grav*`
  - `Inflow` -> `ifl*`
  - `InitialValues` -> `init*`
  - `Insulation` -> `ins*`
  - `MoistAir` -> `ma*`
  - `OpenBoundary` -> `open*`
  - `Symmetry` -> `sym*`
  - `WetSurface` -> `ws*`

### MoistureTransportInBuildingMaterials
Tag: `mt`
  Tag: `mt`
  - `BuildingMaterial` -> `bm*`
  - `Gravity` -> `grav*`
  - `InitialValues` -> `init*`
  - `Insulation` -> `ins*`
  - `MoistureContent` -> `mc*`
  - `MoistureFlux` -> `mf*`
  - `ThinMoistureBarrier` -> `tmb*`

### MovingMesh
Tag: `ale`
  Tag: `ale`
  - `FixedMesh` -> `fix*`
  - `FreeDeformation` -> `free`
  - `PrescribedDeformation` -> `pres*`
  - `PrescribedMeshDisplacement` -> `disp*`

### MultibodyDynamics
Tag: `mbd`
  Tag: `mbd`

  ### BallJoint
  Tag: `blj*`
    Tag: `blj*`
    - `CenterOfJointBnd` -> `cjb*`
    - `CenterOfJointEdge` -> `cje*`
    - `CenterOfJointPoint` -> `cjp*`
    - `DestinationFilter` -> `dstf*`
    - `JointElasticity` -> `je*`
    - `SourceFilter` -> `srcf*`

  ### BevelGear
  Tag: `bvg*`
    Tag: `bvg*`

    ### PrescribedDispRot
    Tag: `pdr*`
      Tag: `pdr*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`

    ### init
    Tag: `init*`
      Tag: `init*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`
    - `FixedConstraint` -> `fix*`
    - `GearAxis` -> `gax*`

  ### ChainDrive
  Tag: `cdr*`
    Tag: `cdr*`
    - `JointElasticity` -> `je*`
    - `SprocketAxis` -> `sja*`

  ### ClearanceJoint
  Tag: `crj*`
    Tag: `crj*`
    - `DestinationFilter` -> `dstf*`
    - `DestinationPointBnd` -> `dpb*`
    - `DestinationPointEdge` -> `dpe*`
    - `DestinationPointPoint` -> `dpp*`
    - `SourceFilter` -> `srcf*`
    - `SourcePointBnd` -> `spb*`
    - `SourcePointEdge` -> `spe*`
    - `SourcePointPoint` -> `spp*`

  ### CylindricalJoint
  Tag: `clj*`
    Tag: `clj*`
    - `CenterOfJointBnd` -> `cjb*`
    - `CenterOfJointEdge` -> `cje*`
    - `CenterOfJointPoint` -> `cjp*`
    - `DestinationFilter` -> `dstf*`
    - `JointAxis` -> `ja*`
    - `JointElasticity` -> `je*`
    - `PrescribedMotion` -> `pm*`
    - `SourceFilter` -> `srcf*`

  ### FixedJoint
  Tag: `fxj*`
    Tag: `fxj*`
    - `CenterOfJointBnd` -> `cjb*`
    - `CenterOfJointEdge` -> `cje*`
    - `CenterOfJointPoint` -> `cjp*`
    - `DestinationFilter` -> `dstf*`
    - `JointAxis` -> `ja*`
    - `JointElasticity` -> `je*`
    - `SourceFilter` -> `srcf*`

  ### GearPair
  Tag: `grp*`
    Tag: `grp*`
    - `Backlash` -> `bcl*`
    - `Friction` -> `fric*`
    - `GearElasticity` -> `gel*`
    - `TransmissionError` -> `ter*`

  ### HelicalGear
  Tag: `hlg*`
    Tag: `hlg*`

    ### init
    Tag: `init*`
      Tag: `init*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`
    - `GearAxis` -> `gax*`

  ### HingeJoint
  Tag: `hgj*`
    Tag: `hgj*`

    ### Friction
    Tag: `fric*`
      Tag: `fric*`
      - `ContactArea` -> `ca*`
    - `AppliedForceAndMoment` -> `afm*`
    - `CenterOfJointBnd` -> `cjb*`
    - `CenterOfJointEdge` -> `cje*`
    - `CenterOfJointPoint` -> `cjp*`
    - `Constraints` -> `ct*`
    - `DestinationFilter` -> `dstf*`
    - `JointAxis` -> `ja*`
    - `JointElasticity` -> `je*`
    - `Locking` -> `lk*`
    - `PrescribedMotion` -> `pm*`
    - `SourceFilter` -> `srcf*`
    - `SpringAndDamper` -> `sd*`

  ### PlanarJoint
  Tag: `plj*`
    Tag: `plj*`

    ### Friction
    Tag: `fric*`
      Tag: `fric*`
      - `ContactArea` -> `ca*`
    - `CenterOfJointBnd` -> `cjb*`
    - `CenterOfJointEdge` -> `cje*`
    - `CenterOfJointPoint` -> `cjp*`
    - `DestinationFilter` -> `dstf*`
    - `JointAxis` -> `ja*`
    - `JointElasticity` -> `je*`
    - `SourceFilter` -> `srcf*`

  ### PrismaticJoint
  Tag: `prj*`
    Tag: `prj*`
    - `CenterOfJointBnd` -> `cjb*`
    - `CenterOfJointEdge` -> `cje*`
    - `CenterOfJointPoint` -> `cjp*`
    - `DestinationFilter` -> `dstf*`
    - `JointAxis` -> `ja*`
    - `JointElasticity` -> `je*`
    - `Locking` -> `lk*`
    - `PrescribedMotion` -> `pm*`
    - `SourceFilter` -> `srcf*`
    - `SpringAndDamper` -> `sd*`

  ### RadialRollerBearing
  Tag: `rrb*`
    Tag: `rrb*`
    - `FlexibleFoundation` -> `ffd*`
    - `Misalignment` -> `mlgn*`
    - `MovingFoundation` -> `mfd*`

  ### ReducedSlotJoint
  Tag: `rslj*`
    Tag: `rslj*`
    - `CenterOfJointBnd` -> `cjb*`
    - `CenterOfJointEdge` -> `cje*`
    - `CenterOfJointPoint` -> `cjp*`
    - `DestinationFilter` -> `dstf*`
    - `JointElasticity` -> `je*`
    - `PrescribedMotion` -> `pm*`
    - `SourceFilter` -> `srcf*`

  ### RigidBodyContact
  Tag: `rbc*`
    Tag: `rbc*`
    - `DestinationPointBnd` -> `dpb*`
    - `DestinationPointEdge` -> `dpe*`
    - `DestinationPointPoint` -> `dpp*`
    - `Friction` -> `fric*`
    - `SourcePointBnd` -> `spb*`
    - `SourcePointEdge` -> `spe*`
    - `SourcePointPoint` -> `spp*`

  ### RigidConnector
  Tag: `rig*`
    Tag: `rig*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`
    - `RigidBodyForce` -> `rf*`
    - `RigidBodyMoment` -> `rm*`

  ### RigidDomain
  Tag: `rd*`
    Tag: `rd*`

    ### AppliedForce
    Tag: `af*`
      Tag: `af*`
      - `LocationBnd` -> `lcb*`
      - `LocationEdge` -> `lce*`
      - `LocationPoint` -> `lcp*`

    ### MassInertia
    Tag: `mmi*`
      Tag: `mmi*`
      - `CenterOfMassBnd` -> `cmb*`
      - `CenterOfMassEdge` -> `cme*`
      - `CenterOfMassPoint` -> `cmp*`

    ### PrescribedDispRot
    Tag: `pdr*`
      Tag: `pdr*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`

    ### init
    Tag: `init*`
      Tag: `init*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`
    - `AppliedMoment` -> `am*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`
    - `FixedConstraint` -> `fix*`

  ### SlotJoint
  Tag: `slj*`
    Tag: `slj*`
    - `CenterOfJointBnd` -> `cjb*`
    - `CenterOfJointEdge` -> `cje*`
    - `CenterOfJointPoint` -> `cjp*`
    - `DestinationFilter` -> `dstf*`
    - `JointElasticity` -> `je*`
    - `SourceFilter` -> `srcf*`

  ### SolidContact
  Tag: `cnt*`
    Tag: `cnt*`
    - `Free` -> `free*`

  ### SpringDamper
  Tag: `spd*`
    Tag: `spd*`
    - `DestinationFilter` -> `dstf*`
    - `DestinationPoint` -> `dp*`
    - `DestinationPointBnd` -> `dpb*`
    - `DestinationPointEdge` -> `dpe*`
    - `DestinationPointPoint` -> `dpp*`
    - `SourceFilter` -> `srcf*`
    - `SourcePoint` -> `sp*`
    - `SourcePointBnd` -> `spb*`
    - `SourcePointEdge` -> `spe*`
    - `SourcePointPoint` -> `spp*`

  ### SpurGear
  Tag: `spg*`
    Tag: `spg*`

    ### init
    Tag: `init*`
      Tag: `init*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`
    - `GearAxis` -> `gax*`
  - `AddedMass1` -> `adm*`
  - `Attachment` -> `att*`
  - `BaseMotion` -> `bsm*`
  - `BodyLoad` -> `bl*`
  - `BoundaryLoad` -> `bndl*`
  - `CamFollower` -> `cfc*`
  - `Fixed` -> `fix*`
  - `Free` -> `free*`
  - `GlobalEquations` -> `ge*`
  - `Gravity` -> `gr*`
  - `LinearElasticModel` -> `lemm*`
  - `SpringFoundation1` -> `spf*`
  - `init` -> `init*`

### NonisothermalPipeFlow
Tag: `nipfl`
  Tag: `nipfl`

  ### WallHeatTransfer
  Tag: `wht*`
    Tag: `wht*`
    - `ExternalFilmResistance` -> `extfilm*`
    - `InternalFilmResistance` -> `intfilm*`
    - `WallLayer` -> `wall*`
  - `Fluid` -> `fluid*`
  - `HeatOutflow` -> `hofl*`
  - `Inlet` -> `inl*`
  - `PipeProperties` -> `pipe*`
  - `Pressure` -> `pr*`
  - `Temperature` -> `temp*`
  - `init` -> `init*`

### NonlinearPressureAcousticsTimeExplicit
Tag: `nate`
  Tag: `nate`
  - `AxialSymmetry` -> `axi*`
  - `Impedance` -> `imp*`
  - `MaterialDiscontinuity` -> `md*`
  - `NonlinearPressureAcousticsTimeExplicitModel` -> `natem*`
  - `Pressure` -> `pr*`
  - `SoundHard` -> `shb*`
  - `init` -> `init*`

### ParticipatingMediaRadiation
Tag: `rpm`
  Tag: `rpm`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `OpaqueSurface` -> `os*`
  - `ParticipatingMedium` -> `rpm*`
  - `init` -> `init*`

### PhaseField
Tag: `pf`
  Tag: `pf`
  - `AxialSymmetry` -> `axi*`
  - `InletBoundary` -> `inl*`
  - `InteriorWettedWall` -> `iww*`
  - `Outlet` -> `out*`
  - `PhaseFieldModel` -> `pfm*`
  - `SymmetryFluid` -> `sym*`
  - `WettedWall` -> `ww*`
  - `init` -> `init*`
  - `initFluid2` -> `initfluid*`

### PhaseTransport
Tag: `phtr`
  Tag: `phtr`
  - `Gravity` -> `gr*`
  - `InitialValues` -> `init*`
  - `NoFlux` -> `nf*`
  - `PhaseAndTransportProperties` -> `ptp*`

### PhaseTransportPorousMedia
Tag: `phtr`
  Tag: `phtr`
  - `AxialSymmetry` -> `axi*`
  - `Gravity` -> `gr*`
  - `InitialValues` -> `init*`
  - `MassFlux` -> `mf*`
  - `MassFlux1` -> `mf*`
  - `NoFlux` -> `nf*`
  - `Outflow` -> `of*`
  - `PhaseAndPorousMediaTransportProperties` -> `pptp*`
  - `PorousMediumDiscontinuity` -> `pmd*`
  - `VolumeFraction` -> `sa*`

### PipeMechanics
Tag: `pipem`
  Tag: `pipem`

  ### PipeCrossSection
  Tag: `pcs*`
    Tag: `pcs*`
    - `BeamSectionOrientation` -> `so*`
  - `DispRot0` -> `pdr*`
  - `Fixed` -> `fix*`
  - `FluidLoad` -> `fl*`
  - `FluidPipeMat` -> `fpm*`
  - `Free` -> `free*`
  - `Gravity` -> `gr*`
  - `init` -> `init*`

### PlasmaTimePeriodic
Tag: `ptp`
  Tag: `ptp`
  - `AxialSymmetry` -> `axi*`
  - `CrossSectionImport` -> `xsecimp*`
  - `DielectricContact` -> `dct*`
  - `ElectronImpactReaction` -> `eir*`
  - `Ground` -> `gnd*`
  - `Insulation` -> `ins*`
  - `MetalContact` -> `mct*`
  - `PlasmaEsModel` -> `pes*`
  - `Reaction` -> `rxn*`
  - `Species` -> `sp*`
  - `SurfaceReaction` -> `sr*`
  - `WallDriftDiffusion` -> `wall*`
  - `ZeroCharge` -> `zc*`
  - `init` -> `init*`

### PointODE
Tag: `pode`
  Tag: `pode`
  - `DistributedODE` -> `dode*`
  - `init` -> `init*`

### PoroelasticWavesSinglePhysics
Tag: `pelw`
  Tag: `pelw`
  - `AxialSymmetry` -> `axi*`
  - `Fixed` -> `pfix*`
  - `PeriodicCondition` -> `pc*`
  - `PoroelasticWavesMaterial` -> `pelm*`
  - `PorousFree` -> `pfree*`
  - `init` -> `init*`

### PorousMediaHeatTransfer
Tag: `ht`
  Tag: `ht`

  ### FluidHeatTransferModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `Opacity` -> `opac*`

  ### IsothermalDomainInterface
  Tag: `idi*`
    Tag: `idi*`
    - `LayerOpacity` -> `lopac*`

  ### PorousMediumHeatTransferModel
  Tag: `porous*`
    Tag: `porous*`

    ### FluidPorousMediumHeatTransferModel
    Tag: `fluid*`
      Tag: `fluid*`
      - `PhaseChangeMaterial` -> `phc*`
    - `ImmobileFluidPorousMaterial` -> `imf*`
    - `PorousMatrixPorousMediumHeatTransferModel` -> `pm*`

  ### PorousMediumLayeredShell
  Tag: `pmls*`
    Tag: `pmls*`
    - `ThermalInsulation` -> `ins*`
    - `init` -> `init*`

  ### SolidHeatTransferModel
  Tag: `solid*`
    Tag: `solid*`
    - `Opacity` -> `opac*`
  - `AxialSymmetry` -> `axi*`
  - `BoundaryHeatSource` -> `bhs*`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `ConvectiveOutflow` -> `ofl*`
  - `HeatFluxBoundary` -> `hf*`
  - `HeatSource` -> `hs*`
  - `Inflow` -> `ifl*`
  - `LineHeatSource` -> `lihs*`
  - `OpaqueSurface` -> `os*`
  - `OpenBoundary` -> `open*`
  - `Symmetry` -> `sym*`
  - `TemperatureBoundary` -> `temp*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### PressureAcoustics
Tag: `acpr`
  Tag: `acpr`

  ### PlaneWaveRadiation
  Tag: `pwr*`
    Tag: `pwr*`
    - `IncidentPressureField` -> `ipf*`

  ### Port
  Tag: `port*`
    Tag: `port*`
    - `CircularPortReferenceAxis` -> `cpra*`

  ### SphericalWaveRadiation
  Tag: `swr*`
    Tag: `swr*`
    - `IncidentPressureField` -> `ipf*`
  - `AnisotropicAcousticsModel` -> `aam*`
  - `AxialSymmetry` -> `axi*`
  - `BackgroundPressureField` -> `bpf*`
  - `CylindricalWaveRadiation` -> `cwr*`
  - `ExteriorFieldCalculation` -> `efc*`
  - `FrequencyAcousticLineSource` -> `als*`
  - `FrequencyMonopoleLineSource` -> `mls*`
  - `FrequencyMonopolePointSource` -> `mps*`
  - `FrequencyPressureAcousticsModel` -> `fpam*`
  - `Impedance` -> `imp*`
  - `InteriorNormalAcceleration` -> `ina*`
  - `InteriorNormalVelocity` -> `inv*`
  - `InteriorPerforatedPlate` -> `ipp*`
  - `InteriorSoundHard` -> `ishb*`
  - `LumpedPort` -> `lport*`
  - `NarrowRegionAcousticsModel` -> `nra*`
  - `NormalAcceleration` -> `nacc*`
  - `NormalDisplacement` -> `ndisp*`
  - `PeriodicCondition` -> `pc*`
  - `PoroacousticsModel` -> `pom*`
  - `SoundHard` -> `shb*`
  - `Symmetry` -> `sym*`
  - `ThermoviscousBoundaryLayerImpedance` -> `tvb*`
  - `init` -> `init*`

### PressureAcousticsBoundaryElements
Tag: `pabe`
  Tag: `pabe`
  - `BackgroundPressureField` -> `bpf*`
  - `BoundaryElementsPressureAcousticsModel` -> `bpam*`
  - `ExcludedBoundary` -> `eb*`
  - `Impedance` -> `imp*`
  - `NormalVelocity` -> `nvel*`
  - `SoundHard` -> `shb*`
  - `init2` -> `init*`

### PressureAcousticsTimeExplicit
Tag: `pate`
  Tag: `pate`
  - `AxialSymmetry` -> `axi*`
  - `PressureAcousticsTimeExplicitModel` -> `patem*`
  - `SoundHard` -> `shb*`
  - `init` -> `init*`

### PrimaryCurrentDistribution
Tag: `cd`
  Tag: `cd`

  ### ElectrodeSurface
  Tag: `es*`
    Tag: `es*`
    - `ElectrodeReaction` -> `er*`

  ### ThinElectrodeSurface
  Tag: `tes*`
    Tag: `tes*`
    - `ElectrodeReaction` -> `er*`
  - `AxialSymmetry` -> `axi*`
  - `Electrolyte` -> `ice*`
  - `ElectrolyteNormalCurrentDensity` -> `icd*`
  - `ElectrolytePotential` -> `eip*`
  - `Insulation` -> `ins*`
  - `init` -> `init*`

### RayAcoustics
Tag: `rac`
  Tag: `rac`

  ### Wall
  Tag: `wall*`
    Tag: `wall*`
    - `SoundPressureLevelBoundary` -> `spl*`
  - `MaterialDiscontinuity` -> `matd*`
  - `MediumProperties` -> `mp*`
  - `RayProperties` -> `op*`
  - `RayTermination` -> `rt*`
  - `ReleaseGrid` -> `relg*`

### ReactionEng
Tag: `re`
  Tag: `re`

  ### ParameterEstimation
  Tag: `est*`
    Tag: `est*`
    - `Experiment` -> `exp*`

  ### SpeciesGroup
  Tag: `sg_rgr*`
    Tag: `sg_rgr*`
    - `SpeciesThermodynamics` -> `sthm*`
  - `AdditionalSourceFeature` -> `add*`
  - `FeedStream` -> `feed*`
  - `ReactionChem` -> `rch*`
  - `ReactionToMph` -> `sync*`
  - `ReversibleReactionGroup` -> `rgr*`
  - `SpeciesChem` -> `sp*`
  - `SpeciesInitialValue` -> `inits*`

### RichardsEquation
Tag: `dl`
  Tag: `dl`
  - `AxialSymmetry` -> `axi*`
  - `Gravity` -> `gr*`
  - `NoFlow` -> `nf*`
  - `PerviousLayer` -> `pl*`
  - `PressureHead` -> `ph*`
  - `RichardsEquationModel` -> `remm*`
  - `init` -> `init*`

### RotatingMachineryMagnetic
Tag: `rmm`
  Tag: `rmm`

  ### AmperesLaw
  Tag: `al*`
    Tag: `al*`
    - `LossCalculation` -> `loss*`

  ### Coil
  Tag: `coil*`
    Tag: `coil*`

    ### CoilCurrentCalculation
    Tag: `ccc*`
      Tag: `ccc*`
      - `CoilGround` -> `cg*`
      - `CoilTerminal` -> `ct*`

    ### UserDefinedCoilGeometry
    Tag: `cg*`
      Tag: `cg*`
      - `CoilInput` -> `ci*`
      - `CoilOutput` -> `co*`
    - `CoilReferenceEdge` -> `cre*`
    - `LossCalculation` -> `loss*`
    - `ReverseCoilGroupDomain` -> `rcd*`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`
    - `MagneticInsulation` -> `mi*`

  ### MagneticFluxConservation
  Tag: `mfc*`
    Tag: `mfc*`
    - `LossCalculation` -> `loss*`

  ### SectorSymmetry
  Tag: `ssc*`
    Tag: `ssc*`
    - `MagneticInsulation` -> `mi*`
  - `ElectricFieldTransformation` -> `etf*`
  - `ExternalCurrentDensity` -> `ecd*`
  - `ForceCalculation` -> `fcal*`
  - `GaugeFixingA` -> `gfa*`
  - `MagneticInsulation` -> `mi*`
  - `MixedFormulationBoundary` -> `mxb*`
  - `PeriodicCondition` -> `pc*`
  - `ZeroMagneticScalarPotential` -> `zsp*`
  - `init` -> `init*`

### SchrodingerEquation
Tag: `schr`
  Tag: `schr`
  - `AxialSymmetry` -> `axi*`
  - `DissipationSchrod` -> `diss*`
  - `EffectiveMass` -> `meff*`
  - `ElectronPotentialEnergy` -> `ve*`
  - `GlobalEquations` -> `ge*`
  - `LorentzForce_schr` -> `lorf*`
  - `OpenBoundary` -> `open*`
  - `PeriodicCondition` -> `pc*`
  - `RotatingFrameSchrod` -> `rotf*`
  - `SecondOrderHamiltonianSemicond` -> `H*`
  - `ZeroFlux` -> `zflx*`
  - `ZeroProbability` -> `zprb*`
  - `ZerothOrderHamiltonianSemicond` -> `H*`
  - `init` -> `init*`

### SecondaryCurrentDistribution
Tag: `cd`
  Tag: `cd`

  ### ElectrodeSurface
  Tag: `es*`
    Tag: `es*`
    - `ElectrodeReaction` -> `er*`

  ### SacrificialEdgeAnode
  Tag: `sacredge*`
    Tag: `sacredge*`
    - `EdgeElectrodeReaction` -> `er*`

  ### ThinElectrodeSurface
  Tag: `tes*`
    Tag: `tes*`
    - `ElectrodeReaction` -> `er*`
  - `AxialSymmetry` -> `axi*`
  - `ElectricGround` -> `egnd*`
  - `Electrode` -> `ece*`
  - `ElectrodeCurrent` -> `ec*`
  - `ElectrodeNormalCurrentDensity` -> `ecd*`
  - `Electrolyte` -> `ice*`
  - `ElectrolyteCurrent` -> `ic*`
  - `ElectrolyteCurrentSource` -> `ics*`
  - `ElectrolytePotential` -> `eip*`
  - `InfiniteElectrolyte` -> `infice*`
  - `Insulation` -> `ins*`
  - `ReferenceElectrodePoint` -> `refel*`
  - `Symmetry` -> `sym*`
  - `init` -> `init*`

### Semiconductor
Tag: `semi`
  Tag: `semi`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`
    - `WKBTunnelingModelElectrons` -> `wkbe*`

  ### GateContact
  Tag: `gc*`
    Tag: `gc*`
    - `HarmonicPerturbation` -> `hp*`

  ### GeometricDopingModel
  Tag: `gdm*`
    Tag: `gdm*`
    - `BoundarySelectionForDopingProfile` -> `gdmbs*`

  ### MetalContact
  Tag: `mc*`
    Tag: `mc*`
    - `HarmonicPerturbation` -> `hp*`

  ### SemiconductorMaterialModel
  Tag: `smm*`
    Tag: `smm*`
    - `AroraMobilityModel` -> `mmar*`
    - `CaugheyThomasMobilityModel` -> `mmct*`
    - `FletcherMobilityModel` -> `mmfl*`
    - `LombardiSurfaceMobilityModel` -> `mmls*`

  ### TrapAssistedSurfaceRecombination
  Tag: `tasr*`
    Tag: `tasr*`
    - `ContinuousEnergyLevelsBoundary` -> `ctb*`
    - `DiscreteEnergyLevelBoundary` -> `dtb*`
  - `AURecombination` -> `aur*`
  - `AnalyticDopingModel` -> `adm*`
  - `AxialSymmetry` -> `axi*`
  - `ChargeConservation` -> `ccn*`
  - `FloatingGate` -> `fg*`
  - `GlobalEquations` -> `ge*`
  - `IIGeneration` -> `iig*`
  - `Insulation` -> `ins*`
  - `InsulatorInterface` -> `ii*`
  - `OpticalTransitions` -> `ot*`
  - `SurfaceChargeDensity` -> `sfcd*`
  - `Terminal` -> `term*`
  - `TrapAssistedRecombination` -> `tar*`
  - `UDGeneration` -> `udg*`
  - `ZeroCharge` -> `zc*`
  - `init` -> `init*`

### Sensitivity
Tag: `sens`
  Tag: `sens`
  - `ControlVariableField` -> `cvar*`

### ShallowWaterEquationsTimeExplicit
Tag: `swe`
  Tag: `swe`
  - `DomainProperties` -> `dp*`
  - `InletBoundary` -> `inl*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### Shell
Tag: `shell`
  Tag: `shell`

  ### Elastic
  Tag: `emm*`
    Tag: `emm*`
    - `Damping` -> `dmp*`
    - `Safety` -> `sf*`
    - `ShellLocalSystem` -> `shls*`

  ### LayeredElastic
  Tag: `llem*`
    Tag: `llem*`
    - `LayeredPlasticity` -> `lplsty*`
    - `LayeredSafety` -> `lsf*`
    - `LayeredThermalExpansion` -> `lte*`

  ### RigidConnectorShell
  Tag: `srig*`
    Tag: `srig*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`
    - `RigidBodyMoment` -> `rm*`
  - `Attachment` -> `att*`
  - `AxialSymmetry` -> `axi*`
  - `BodyLoad` -> `bl*`
  - `Displacement0` -> `disp*`
  - `Displacement1` -> `disp*`
  - `Displacement2` -> `disp*`
  - `EdgeLoad` -> `el*`
  - `FaceLoad` -> `fl*`
  - `Fixed` -> `fix*`
  - `Free` -> `free*`
  - `GlobalEquations` -> `ge*`
  - `Gravity` -> `gr*`
  - `LayeredHyperelasticModel` -> `lhmm*`
  - `Pinned` -> `pin*`
  - `PointLoad` -> `pl*`
  - `PointLoadOnAxis` -> `pla*`
  - `RotatingFrame` -> `rotf*`
  - `ShellContact` -> `cnt*`
  - `SimplySupported` -> `ssp*`
  - `SpringFoundation2` -> `spf*`
  - `SymmetryPlane` -> `symp*`
  - `SymmetrySolid1` -> `sym*`
  - `ThicknessOffset` -> `to*`
  - `init` -> `init*`

### SlipFlow
Tag: `slpf`
  Tag: `slpf`

  ### IsothermalDomainInterface
  Tag: `idi*`
    Tag: `idi*`
    - `LayerOpacity` -> `lopac*`

  ### NonIsothermalFlowModel
  Tag: `fluid*`
    Tag: `fluid*`
    - `Opacity` -> `opac*`

  ### SolidHeatTransferModel
  Tag: `solid*`
    Tag: `solid*`
    - `Opacity` -> `opac*`
  - `ContinuityOnInteriorBoundary` -> `cib*`
  - `ExternalSlipWall` -> `eslw*`
  - `OpaqueSurface` -> `os*`
  - `PressurePointConstraint` -> `prpc*`
  - `SlipWall` -> `slw*`
  - `TemperatureBoundary` -> `temp*`
  - `ThermalInsulation` -> `ins*`
  - `init` -> `init*`

### SolidMechanics
Tag: `solid`
  Tag: `solid`

  ### AverageRotation
  Tag: `avgr*`
    Tag: `avgr*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationDom` -> `crd*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`

  ### BoltPrestress
  Tag: `pblt*`
    Tag: `pblt*`
    - `BoltSelection` -> `sblt*`

  ### BoltThreadContact
  Tag: `btc*`
    Tag: `btc*`

    ### ThreadBoundarySelection
    Tag: `tbs*`
      Tag: `tbs*`
      - `Free` -> `free*`

  ### BoundaryLoad
  Tag: `bndl*`
    Tag: `bndl*`
    - `Phase` -> `ph*`

  ### CellPeriodicity
  Tag: `cp*`
    Tag: `cp*`
    - `BoundaryPair` -> `bp*`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`
    - `Free` -> `free*`

  ### Crack
  Tag: `crack*`
    Tag: `crack*`
    - `CrackFaceLoad` -> `fl*`
    - `JIntegral` -> `jint*`

  ### ElastoplasticSoilMaterial
  Tag: `epsm*`
    Tag: `epsm*`
    - `ExternalStress` -> `exs*`

  ### HyperelasticModel
  Tag: `hmm*`
    Tag: `hmm*`
    - `ThermalExpansion` -> `te*`
    - `Viscoelasticity` -> `vis*`

  ### LinearElasticModel
  Tag: `lemm*`
    Tag: `lemm*`

    ### Plasticity
    Tag: `plsty*`
      Tag: `plsty*`
      - `SetVariables` -> `setv*`
    - `Activation` -> `act*`
    - `Concrete` -> `cm*`
    - `Creep` -> `cmm*`
    - `Damage` -> `dmg*`
    - `Damping` -> `dmp*`
    - `ExternalStress` -> `exs*`
    - `InitialStressandStrain` -> `iss*`
    - `PorousPlasticity` -> `popl*`
    - `Safety` -> `sf*`
    - `SoilModel` -> `soil*`
    - `ThermalExpansion` -> `te*`
    - `Viscoelasticity` -> `vis*`
    - `Viscoplasticity` -> `vpl*`

  ### PeriodicCondition
  Tag: `pc*`
    Tag: `pc*`
    - `DestinationDomains` -> `dd*`

  ### PiezoelectricMaterialModel
  Tag: `pzm*`
    Tag: `pzm*`
    - `DielectricLoss` -> `dels*`
    - `MechanicalDamping` -> `mdmp*`

  ### RigidConnector
  Tag: `rig*`
    Tag: `rig*`

    ### SpringFoundation
    Tag: `spf*`
      Tag: `spf*`
      - `LocationBnd` -> `lcb*`
      - `LocationEdge` -> `lce*`
      - `LocationPoint` -> `lcp*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`
    - `RigidBodyForce` -> `rf*`
    - `RigidBodyMassInertia` -> `rmm*`
    - `RigidBodyMoment` -> `rm*`

  ### RigidDomain
  Tag: `rd*`
    Tag: `rd*`

    ### AppliedForce
    Tag: `af*`
      Tag: `af*`
      - `LocationBnd` -> `lcb*`
      - `LocationEdge` -> `lce*`
      - `LocationPoint` -> `lcp*`

    ### MassInertia
    Tag: `mmi*`
      Tag: `mmi*`
      - `CenterOfMassBnd` -> `cmb*`
      - `CenterOfMassEdge` -> `cme*`
      - `CenterOfMassPoint` -> `cmp*`

    ### init
    Tag: `init*`
      Tag: `init*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`
    - `AppliedMoment` -> `am*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`

  ### ShapeMemoryAlloy
  Tag: `sma*`
    Tag: `sma*`
    - `PhaseTransformationDirection` -> `trdir*`
    - `ThermalExpansion` -> `te*`

  ### SolidContact
  Tag: `cnt*`
    Tag: `cnt*`
    - `Adhesion` -> `adh*`
    - `Decohesion` -> `dch*`
    - `Free` -> `free*`
    - `Friction` -> `fric*`
    - `FrictionSlipVelocity` -> `sv*`
    - `Wear` -> `wear*`

  ### SpringFoundation2
  Tag: `spf*`
    Tag: `spf*`
    - `PreDeformation` -> `prd*`
  - `AddedMass2` -> `adm*`
  - `Attachment` -> `att*`
  - `AxialSymmetry` -> `axi*`
  - `AxialSymmetrySolid` -> `axi*`
  - `BodyLoad` -> `bl*`
  - `Discretization` -> `disc*`
  - `Displacement0` -> `disp*`
  - `Displacement1` -> `disp*`
  - `Displacement2` -> `disp*`
  - `EdgeLoad` -> `el*`
  - `ElasticPredeformation` -> `epdm*`
  - `Fixed` -> `fix*`
  - `Free` -> `free*`
  - `GlobalConstraint` -> `gconstr*`
  - `GlobalEquations` -> `ge*`
  - `Gravity` -> `gr*`
  - `LowReflectingBoundary` -> `lrb*`
  - `MagnetostrictiveModel` -> `mgm*`
  - `PointLoad` -> `pl*`
  - `PointLoadOnAxis` -> `pla*`
  - `Port` -> `port*`
  - `RigidMotionSuppression` -> `rms*`
  - `Roller` -> `roll*`
  - `RotatingFrame` -> `rotf*`
  - `SpringFoundation0` -> `spf*`
  - `SpringFoundation1` -> `spf*`
  - `SpringFoundation3` -> `spf*`
  - `StressLinearization` -> `sl*`
  - `SymmetryPlane` -> `symp*`
  - `SymmetrySolid` -> `sym*`
  - `ThinElasticLayer` -> `tel*`
  - `Velocity` -> `vel*`
  - `init` -> `init*`

### SolidRotor
Tag: `rotsld`
  Tag: `rotsld`

  ### GearPair
  Tag: `grp*`
    Tag: `grp*`
    - `Backlash` -> `bcl*`
    - `Friction` -> `fric*`
    - `GearElasticity` -> `gel*`
    - `TransmissionError` -> `ter*`

  ### HelicalGear
  Tag: `hlg*`
    Tag: `hlg*`

    ### init
    Tag: `init*`
      Tag: `init*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`

  ### JournalBearing
  Tag: `jrb*`
    Tag: `jrb*`
    - `FlexibleFoundation` -> `ffd*`
    - `MovingFoundation` -> `mfd*`
    - `SqueezeFilmDamper` -> `sfd*`

  ### LinearElasticModel
  Tag: `lemm*`
    Tag: `lemm*`
    - `Damping` -> `dmp*`

  ### RigidDomain
  Tag: `rd*`
    Tag: `rd*`

    ### init
    Tag: `init*`
      Tag: `init*`
      - `CenterOfRotationBnd` -> `crb*`
      - `CenterOfRotationEdge` -> `cre*`
      - `CenterOfRotationPoint` -> `crp*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`

  ### RotorAxis
  Tag: `raxi*`
    Tag: `raxi*`
    - `Axis` -> `axis*`
    - `FirstSupport` -> `fsup*`
    - `SecondSupport` -> `ssup*`

  ### ThrustBearing
  Tag: `thrb*`
    Tag: `thrb*`
    - `FlexibleFoundation` -> `ffd*`
    - `MovingFoundation` -> `mfd*`
  - `AppliedTorque` -> `atq*`
  - `FixAxRot` -> `far*`
  - `Free` -> `free*`
  - `RotorSpeed` -> `rsp*`
  - `init` -> `init*`

### StructuralMembrane
Tag: `mbrn`
  Tag: `mbrn`

  ### LinearElasticModel
  Tag: `lemm*`
    Tag: `lemm*`
    - `InitialStressandStrain` -> `iss*`
  - `AxialSymmetry` -> `axi*`
  - `AxialSymmetrySolid` -> `axi*`
  - `Displacement0` -> `disp*`
  - `Displacement1` -> `disp*`
  - `EdgeLoad` -> `el*`
  - `FaceLoad` -> `fl*`
  - `Fixed` -> `fix*`
  - `Free` -> `free*`
  - `GlobalEquations` -> `ge*`
  - `HyperelasticModel` -> `hmm*`
  - `LayeredLinearElasticModel` -> `llemm*`
  - `SpringFoundation2` -> `spf*`
  - `Symmetry` -> `sym*`
  - `ThicknessOffset` -> `to*`
  - `init` -> `init*`

### SurfaceReactions
Tag: `sr*`
  Tag: `sr*`
  - `NoFlux` -> `nflx*`
  - `Reactions` -> `reac*`
  - `SurfaceProperties` -> `sp*`
  - `init` -> `init*`

### SurfaceToSurfaceRadiation
Tag: `rad`
  Tag: `rad`
  - `DiffuseSurface` -> `dsurf*`
  - `ExternalRadiationSource` -> `ers*`
  - `Opacity` -> `opac*`
  - `OpaqueSurfaceSpecularAndDiffuse` -> `osurf*`
  - `SymmetryForSurfaceToSurfaceRadiation` -> `rsym*`
  - `init` -> `init*`

### TernaryPhaseField
Tag: `terpf`
  Tag: `terpf`
  - `AxialSymmetry` -> `axi*`
  - `MixtureProperties` -> `mp*`
  - `WettedWall` -> `ww*`
  - `init` -> `init*`

### TertiaryCurrentDistributionNernstPlanck
Tag: `tcd`
  Tag: `tcd`

  ### ElectrodeSurface
  Tag: `es*`
    Tag: `es*`
    - `ElectrodeReaction` -> `er*`

  ### HighlyConductivePorousElectrode
  Tag: `hcpce*`
    Tag: `hcpce*`
    - `PorousElectrodeReaction` -> `per*`

  ### Separator
  Tag: `sep*`
    Tag: `sep*`
    - `NonFaradaicReactions` -> `nfr*`
  - `AxialSymmetry` -> `axi*`
  - `Concentration` -> `conc*`
  - `ElectricInsulation` -> `ein*`
  - `Electrolyte` -> `ice*`
  - `ElectrolytePotential` -> `eip*`
  - `ElectrolytePotentialPoint` -> `eip*`
  - `EquilibriumReaction` -> `eqreac*`
  - `GlobalConstraint` -> `gconstr*`
  - `Inflow` -> `in*`
  - `IonExchangeMembrane` -> `iem*`
  - `NoFlux` -> `nflx*`
  - `Outflow` -> `out*`
  - `PeriodicCondition` -> `pc*`
  - `SurfaceChargeDensity` -> `sfcd*`
  - `init` -> `init*`

### TertiaryElectroanalysis
Tag: `tcd`
  Tag: `tcd`

  ### ElectrodeSurface
  Tag: `es*`
    Tag: `es*`
    - `DoubleLayerCapacitance` -> `dlc*`
    - `ElectrodeReaction` -> `er*`
  - `AxialSymmetry` -> `axi*`
  - `Concentration` -> `conc*`
  - `ElectricInsulation` -> `ein*`
  - `Electrolyte` -> `ice*`
  - `EquilibriumReaction` -> `eqreac*`
  - `NoFlux` -> `nflx*`
  - `Reactions` -> `reac*`
  - `init` -> `init*`

### ThermoacousticsSinglePhysics
Tag: `ta`
  Tag: `ta`
  - `AxialSymmetry` -> `axi*`
  - `BackgroundAcousticFields` -> `baf*`
  - `Isothermal` -> `iso*`
  - `Port` -> `port*`
  - `PressureAdiabatic` -> `pra*`
  - `Symmetry` -> `sym*`
  - `ThermoviscousAcousticsModel` -> `tam*`
  - `VelocityThermoacoustic` -> `velt*`
  - `Wall` -> `wall*`
  - `init` -> `init*`

### ThermoacousticsSinglePhysicsTransient
Tag: `tatd`
  Tag: `tatd`
  - `NonlinearThermoviscousAcousticsContributions` -> `ntac*`
  - `ThermoviscousAcousticsModel` -> `tam*`
  - `Wall` -> `wall*`
  - `init` -> `init*`

### ThinFilmFlowDomain
Tag: `tff`
  Tag: `tff`
  - `Border` -> `bdr*`
  - `FluidFilmProperties` -> `ffp*`
  - `Perforations` -> `perf*`
  - `init` -> `init*`

### ThinFilmFlowEdge
Tag: `tffs`
  Tag: `tffs`
  - `AxialSymmetry` -> `axi*`
  - `Border` -> `bdr*`
  - `FluidFilmProperties` -> `ffp*`
  - `init` -> `init*`

### ThinFilmFlowShell
Tag: `tffs`
  Tag: `tffs`
  - `Border` -> `bdr*`
  - `FluidFilmProperties` -> `ffp*`
  - `GlobalEquations` -> `ge*`
  - `SymmetryFluid` -> `sym*`
  - `init` -> `init*`

### TransientElectromagneticWaves
Tag: `temw`
  Tag: `temw`

  ### WaveEquationElectric
  Tag: `wee*`
    Tag: `wee*`
    - `DrudeLorentzPolarization` -> `dlp*`
  - `AxialSymmetry` -> `axi*`
  - `LumpedPort` -> `lport*`
  - `PerfectElectricConductor` -> `pec*`
  - `PerfectMagneticConductor` -> `pmc*`
  - `PeriodicCondition` -> `pc*`
  - `Scattering` -> `sctr*`
  - `init` -> `init*`

### TransientPipeAcoustics
Tag: `patd`
  Tag: `patd`
  - `Closed` -> `closed*`
  - `EndImpedance` -> `endimp*`
  - `FluidProperties` -> `fp*`
  - `PipeProperties` -> `pipe*`
  - `Pressure` -> `pres*`
  - `VolumeForce` -> `vf*`
  - `init` -> `init*`

### TransientPressureAcoustics
Tag: `actd`
  Tag: `actd`

  ### CylindricalWaveRadiation
  Tag: `cwr*`
    Tag: `cwr*`
    - `IncidentPressureField` -> `ipf*`

  ### PlaneWaveRadiation
  Tag: `pwr*`
    Tag: `pwr*`
    - `IncidentPressureField` -> `ipf*`
  - `AxialSymmetry` -> `axi*`
  - `Impedance` -> `imp*`
  - `NonlinearAcousticsWestervelt` -> `nlaw*`
  - `Pressure` -> `pr*`
  - `SoundHard` -> `shb*`
  - `Symmetry` -> `sym*`
  - `TransientMonopoleLineSource` -> `mls*`
  - `TransientPressureAcousticsModel` -> `tpam*`
  - `init` -> `init*`

### TransmissionLine
Tag: `tl`
  Tag: `tl`
  - `LumpedPort` -> `lport*`
  - `OpenCircuit` -> `oc*`
  - `TransmissionLineEquation` -> `tle*`
  - `init` -> `init*`

### Truss
Tag: `truss`
  Tag: `truss`

  ### AverageRotation
  Tag: `avgr*`
    Tag: `avgr*`
    - `CenterOfRotationBnd` -> `crb*`
    - `CenterOfRotationDom` -> `crb*`
    - `CenterOfRotationEdge` -> `cre*`
    - `CenterOfRotationPoint` -> `crp*`

  ### Elastic
  Tag: `emm*`
    Tag: `emm*`
    - `InitialStressandStrain` -> `iss*`
    - `Plasticity` -> `plsty*`
  - `CrossSectionBeam` -> `csd*`
  - `Discretization` -> `disc*`
  - `Displacement0` -> `disp*`
  - `Free` -> `free*`
  - `Pinned` -> `pin*`
  - `PointLoad` -> `pl*`
  - `SpringFoundation1` -> `spf*`
  - `StraightEdgeConstraint` -> `sec*`
  - `init` -> `init*`

### TurbulentFlowAlgebraicYplus
Tag: `spf`
  Tag: `spf`

  ### StationaryFreeSurface
  Tag: `sfs*`
    Tag: `sfs*`
    - `ContactAngle` -> `cnta*`
  - `AxialSymmetry` -> `axi*`
  - `ExtFan` -> `fan*`
  - `FluidProperties` -> `fp*`
  - `GlobalEquations` -> `ge*`
  - `Gravity` -> `grav*`
  - `Grille` -> `grille*`
  - `InletBoundary` -> `inl*`
  - `InteriorWallBC` -> `iwbc*`
  - `OutletBoundary` -> `out*`
  - `PeriodicFlowCondition` -> `pfc*`
  - `PressurePointConstraint` -> `prpc*`
  - `Symmetry` -> `sym*`
  - `VolumeForce` -> `vf*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `WeakContribution` -> `weak*`
  - `init` -> `init*`

### TurbulentFlowSST
Tag: `spf`
  Tag: `spf`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `OpenBoundary` -> `open*`
  - `OutletBoundary` -> `out*`
  - `Symmetry` -> `sym*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### TurbulentFlowkeps
Tag: `spf`
  Tag: `spf`

  ### Continuity
  Tag: `cont*`
    Tag: `cont*`
    - `Wall` -> `wall*`
    - `WallBC` -> `wallbc*`

  ### FreeSurface
  Tag: `fs*`
    Tag: `fs*`
    - `ContactAngle` -> `cnta*`

  ### StationaryFreeSurface
  Tag: `sfs*`
    Tag: `sfs*`
    - `ContactAngle` -> `cnta*`
  - `AxialSymmetry` -> `axi*`
  - `FluidProperties` -> `fp*`
  - `GlobalEquations` -> `ge*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `InteriorWallBC` -> `iwbc*`
  - `NewTurbulenceModel` -> `nturb*`
  - `OpenBoundary` -> `open*`
  - `OutletBoundary` -> `out*`
  - `PeriodicFlowCondition` -> `pfc*`
  - `PressurePointConstraint` -> `prpc*`
  - `Symmetry` -> `sym*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### TurbulentFlowkomega
Tag: `spf`
  Tag: `spf`
  - `AxialSymmetry` -> `axi*`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `InteriorWallBC` -> `iwbc*`
  - `OutletBoundary` -> `out*`
  - `PeriodicFlowCondition` -> `pfc*`
  - `PressurePointConstraint` -> `prpc*`
  - `Symmetry` -> `sym*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### TurbulentFlowlowRekeps
Tag: `spf`
  Tag: `spf`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `OpenBoundary` -> `open*`
  - `OutletBoundary` -> `out*`
  - `Symmetry` -> `sym*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### TurbulentFlowv2f
Tag: `spf`
  Tag: `spf`
  - `FluidProperties` -> `fp*`
  - `Gravity` -> `grav*`
  - `InletBoundary` -> `inl*`
  - `OutletBoundary` -> `out*`
  - `Wall` -> `wall*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### VolumeAveragedMixtureModelLaminar
Tag: `mm`
  Tag: `mm`
  - `Gravity` -> `gr*`
  - `InletBoundary` -> `inl*`
  - `MixtureProperties` -> `mp*`
  - `OutletBoundary` -> `out*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### VolumeAveragedMixtureModelkeps
Tag: `mm`
  Tag: `mm`
  - `AxialSymmetry` -> `axi*`
  - `Gravity` -> `gr*`
  - `InletBoundary` -> `inl*`
  - `MixtureProperties` -> `mp*`
  - `OutletBoundary` -> `out*`
  - `WallBC` -> `wallbc*`
  - `init` -> `init*`

### WaterHammer
Tag: `whtd`
  Tag: `whtd`
  - `Closed` -> `closed*`
  - `FluidProperties` -> `fp*`
  - `PipeProperties` -> `pipe*`
  - `Pressure` -> `pres*`
  - `init` -> `init*`

### WeakFormBoundaryPDE
Tag: `wb`
  Tag: `wb`
  - `WeakFormPDE` -> `wfeq*`
  - `init` -> `init*`
- `BeamCrossSection` -> `bcs`
