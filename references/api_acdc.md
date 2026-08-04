# AC/DC Module — API Reference (es, ec, mf, emw)

Sources:
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\ACDC_Module\ACDCModuleUsersGuide.pdf` (COMSOL 6.4, 540 pp)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\ACDC_Module\IntroductionToACDCModule.pdf` (84 pp)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\RF_Module\RFModuleUsersGuide.pdf` (Electromagnetic Waves, Frequency Domain node list)
- mph tags.json (exact feature type strings) via `references/tags_physics.md`; verified against working code in `D:\tmp\wyk\Comsol仿真\scheme1\scripts\01_build_model_v2.py`

Conventions (same as `api_structural.md`):
- **Feature type string** = Java/model-tree node type passed to
  `physics.feature().create(tag, 'TypeString', dim)` (mph) / `create(tag, type, dim)` (Java).
  Case-sensitive CamelCase, no spaces (Ampère → `Amperes`, e.g. `AmperesLaw`).
- **dim** = geometric entity dimension: `2` = domains (3D) / boundaries (2D); `1` = boundaries (3D) / edges (2D) / points (1D); `0` = edges (3D) / points (2D).
- Default tags: `es` (Electrostatics), `ec` (Electric Currents), `mf` (Magnetic Fields), `emw`/`ewfd` (EM Waves).
- Physics interface creation: `comp.physics().create('es', 'Electrostatics', 'geom1')` (3rd arg = geometry tag).
- 2D out-of-plane thickness `d` (default 1 m), 1D cross-section area `A` (default 1 m²) — set on the physics interface; per-entity override via `ChangeThickness`/`ChangeCrossSection` nodes.
- `<name>.<var>` pattern for all variables, `<name>` = interface Name (default es/ec/mf/emw).
- Study compatibility: es/ec/mf support Stationary, Frequency Domain, Time Dependent, Eigenfrequency, and small-signal analysis (mf: no eigenfrequency); emw/ewfd: Frequency Domain, Eigenfrequency.

---

## 1. Physics Interfaces — Tags and Space Dimensions

| Interface | Type string | Tag | Space dims | Notes |
|---|---|---|---|---|
| Electrostatics | `Electrostatics` | `es` | 3D, 2D, 2D axisym, 1D | solves Gauss' law for scalar V |
| Electrostatics, Boundary Elements | `ElectrostaticsBoundaryElements` | `esbe` | 2D, 3D | BEM, no mesh in domains |
| Electric Currents | `ElectricCurrents` | `ec` | 3D, 2D, 2D axisym, 1D | solves current conservation for V |
| Electric Currents in Shells | `ElectricCurrentsShell` | `ecis` | 2D, 3D (on boundaries) | layered shells, extra dim |
| Electric Currents, Single Layer Shell | `ElectricCurrentsSingleLayerShell` | `ecs` | 2D, 3D (boundaries) | tags.json: `ConductiveMediaShell` |
| Magnetic Fields | `MagneticFields` | `mf` | 3D, 2D, 2D axisym | solves Ampère's law for A; tags.json: `InductionCurrents` |
| Magnetic Fields, No Currents | `MagneticFieldsNoCurrents` | `mfnc` | 3D, 2D, 2D axisym | scalar magnetic potential; tags.json: `MagnetostaticsNoCurrents` |
| Magnetic Fields, No Currents, Boundary Elements | `MagneticFieldsNoCurrentsBoundaryElements` | `mfncbe` | 2D, 3D | |
| Magnetic and Electric Fields | `MagneticAndElectricFields` | `mef` | 3D, 2D, 2D axisym | A + V; tags.json: `ElectricInductionCurrents` |
| Magnetic Field Formulation | `MagneticFieldFormulation` | `mfh` | 3D, 2D | H formulation |
| Magnetic Fields, Currents Only | `MagneticFieldsCurrentsOnly` | `mfco` | 3D, 2D, 2D axisym | Biot–Savart integral |
| Rotating Machinery, Magnetic | `RotatingMachineryMagnetic` | `rmm` | 2D, 2D axisym, 3D | |
| Electrical Circuit | `ElectricalCircuit` | `cir` | global | circuit elements, connects to Terminal/Circuit |
| Electromagnetic Waves | `ElectromagneticWaves` | `emw` | 3D, 2D, 2D axisym, 1D | RF Module; emw = Frequency Domain |
| Electromagnetic Waves, Frequency Domain | `ElectromagneticWavesFrequencyDomain` | `ewfd` | 3D, 2D, 2D axisym, 1D | explicit type string |
| Electromagnetic Waves, Beam Envelopes | `ElectromagneticWavesBeamEnvelopes` | `ewbe` | | |
| Electromagnetic Waves, Transient | `ElectromagneticWavesTransient` | `ewt` | | |
| Transient Electromagnetic Waves | `TransientElectromagneticWaves` | `temw` | | |

Study guidance (Table 4-1 in ACDC guide): relaxation time τ vs external time scale T —
τ >> T → Electrostatics (Stationary); τ << T → Electric Currents (Stationary); τ ~ T → Electric Currents (Time Dependent / Frequency Domain).

---

## 2. Electrostatics Interface (`es`)

Dependent variable: **Electric potential V** (default Quadratic). Optional **D-V formulation**: mixed FE, displacement field D + V as dependent variables (set in interface Discretization, `Mixed finite element`). Solves ∇·(−ε₀∇V − P) = ρ.

Default nodes on creation: `FreeSpace` (domain), `ZeroCharge` (default boundary), `init` (Initial Values).

### 2.1 Domain features (dim=2)

| Node (UI) | Feature type string | Key properties |
|---|---|---|
| Free Space | `FreeSpace` | vacuum canvas; adds ChargeConservation with εr = 1; also stabilizes mf |
| Charge Conservation | `ChargeConservation` | `MaterialType` (Solids/Fluids), `DielectricModel` (RelativePermittivity default / Polarization / RemanentElectricDisplacement / DielectricLosses / Ferroelectric / Dispersion), `RelativePermittivity` εr (isotropic/diagonal/symmetric/full, `_mat` mode: `from_mat` default / `userdef`), `Polarization` P, `RemanentElectricDisplacement` Dr; subnodes: `EffectiveMedium`, `ArchieLaw`, `Dispersion`, `ConductionLoss` |
| Charge Conservation, Piezoelectric | `ChargeConservationPiezo` | `RelativePermittivity` εrS; used with Piezoelectricity multiphysics (es + solid + `PiezoelectricEffect`); default node in Piezoelectricity interface |
| Charge Conservation, Ferroelectric | `ChargeConservationFerroelectric` | with Ferroelectroelasticity multiphysics |
| Initial Values | `init` (also `InitialValues`) | `V` initial value |
| Space Charge Density | `SpaceChargeDensity` | `rho` ρv (C/m³) |
| Force Calculation | `ForceCalculation` | `ForceName`, `TorqueAxis`, `TorqueRotationPoint`; vars `<name>.Forcex_<fn>`, `<name>.Torquex_<fn>`, `<name>.Tax_<fn>`, cycle-averaged `Forceav.../Tav.../Taxav...` |
| Conduction Loss (Time-Harmonic) | `ConductionLoss` (subnode of ChargeConservation) | `ElectricConductivity` σ; active in Eigenfrequency/Frequency Domain only |
| Dispersion | `Dispersion` (subnode) | Debye / Multipole Debye, shift functions (Vogel–Fulcher, Arrhenius, WLF, TNM) |
| Effective Medium | `EffectiveMedium` (subnode) | mixture averaging of εr |
| Archie's Law | `ArchieLaw` (subnode) | conductivity in porous matrix |
| Change Thickness (Out-of-Plane) | `ChangeThicknessOutOfPlane` | `d` (2D) |
| Change Cross Section | `ChangeCrossSection` | `A` (1D) |

### 2.2 Boundary / edge / point features

| Node (UI) | Feature type string | dim | Key properties / equation |
|---|---|---|---|
| Zero Charge (default) | `ZeroCharge` | 1 (edges 2D/points 1D) | n·D = 0; default exterior BC |
| Ground | `Ground` | 1, 0 | V = 0; also on edges (3D) / points, axis |
| Electric Potential | `ElectricPotential` | 1, 0 | `V0` (default 0 V); V = V0 |
| Surface Charge Density | `SurfaceChargeDensity` | 1 | `rho_s` ρs (C/m²); n·D = ρs |
| Floating Potential | `FloatingPotential` | 1 | `V0` constant, `Q0` total charge (default 0 C = floating equipotential), `UseGroup` (floating potential group), `TerminalType`/Circuit option, `Vinit`; var `es.V0_<id>` |
| Terminal | `Terminal` | 1 (boundary) or 2 (domain) | `TerminalName`, `TerminalType`: **Charge (default, Q0=0 → floating) / Voltage (V0, default 1 V) / Circuit (needs cir interface; Time Dependent or Frequency Domain only) / Terminated (power) (P0, Zref, S-params) / Terminated (voltage)**; `Zref` 50 Ω; advanced: `AreaMultiplicationFactor`, `Vinit`, `Qinit`; lumped capacitance via terminal sweep |
| Electric Displacement Field | `DisplacementField` | 1 | `D0` (C/m²); n·D = n·D0 |
| External Surface Charge Accumulation | `ExternalSurfaceChargeAccumulation` | 1 | `nJi` (normal ion current), `nJe` (normal electron current); dρs/dt ODE |
| Distributed Capacitance | `DistributedCapacitance` | 1 | `RelativePermittivity` εr, `SurfaceThickness` ds (1 mm), `Vref`; n·D = ε₀εr(V−Vref)/ds |
| Symmetry Plane (for Electric Field) | `SymmetryPlane` | 1 | `SymmetryType`: Symmetry (n·E=0) / Antisymmetry (n×E=0) |
| Periodic Condition | `PeriodicCondition` | 1 | `Type`: Continuity / Antiperiodicity / Floquet (kF); manual destination selection |
| Thin Low Permittivity Gap | `ThinLowPermittivityGap` | 1 | `RelativePermittivity` εr, `Thickness` d (default 5 mm) |
| Dielectric Shielding | `DielectricShielding` | 1 | `RelativePermittivity` εr, `SurfaceThickness` ds (1 m) |
| Line Charge | `LineCharge` | 0 (3D edges) | `QL` (C/m) |
| Line Charge (on Axis) | `LineChargeOnAxis` | 0 | axisymmetric, `QL` |
| Line Charge (Out-of-Plane) | `LineChargeOutOfPlane` | 0 (2D points) | `QL` |
| Point Charge | `PointCharge` | 0 | `QP` (C) |
| Point Charge (on Axis) | `PointChargeOnAxis` | 0 | `QP` |
| Electric Sensor | `ElectricSensor` | 1 | sensing electrode for charge |

### 2.3 Common subnode: Harmonic Perturbation
`HarmonicPerturbation` (tag `hp*`) attaches to Terminal (Charge/Voltage), Floating Potential, ElectricPotential, SurfaceChargeDensity, SpaceChargeDensity, point/line charges for small-signal analysis.

---

## 3. Electric Currents Interface (`ec`)

Dependent variable: **Electric potential V**. Solves ∇·J = Qj, J = σE + Je + ∂D/∂t (frequency: ∇·(σ + jωε₀εr)∇V = Qj). Default nodes: `CurrentConservation`, `ElectricInsulation` (default BC), `init`.

### 3.1 Domain features (dim=2)

| Node (UI) | Feature type string | Key properties |
|---|---|---|
| Current Conservation | `CurrentConservation` | `MaterialType` (Solids/Fluids), `ElectricConductivity` σ (From material / User defined / Effective medium / Archie's Law / Hall effect / Linearized resistivity), `DielectricModel`: RelativePermittivity / Polarization / RemanentElectricDisplacement / DielectricLosses / **LossTangentLossAngle** (ε′, δ) / **LossTangentDissipationFactor** (ε′, tanδ) / Dispersion; subnodes `EffectiveMedium`, `ArchieLaw`, `Dispersion` |
| External Current Density | `ExternalCurrentDensity` | `Je` (A/m²); option to add contribution to losses (`AddContributionToLosses`) |
| Current Source | `CurrentSource` | `Qj` (A/m³) |
| Initial Values | `init` | `V` |
| Dispersion | `Dispersion` (subnode) | Debye / Multipole Debye / Constant loss tangent; thermal shift functions |
| Force Calculation | `ForceCalculation` | same as es |
| Change Thickness / Change Cross Section | as es | |

### 3.2 Boundary / edge / point features

| Node (UI) | Feature type string | dim | Key properties / equation |
|---|---|---|---|
| Electric Insulation (default) | `ElectricInsulation` | 1 | n·J = 0; default exterior BC |
| Ground | `Ground` | 1, 0 | V = 0 |
| Electric Potential | `ElectricPotential` | 1, 0 | `V0` |
| Floating Potential | `FloatingPotential` | 1 | `I0` total current (default 0 A), Circuit option, `Vinit`, group option |
| Normal Current Density | `NormalCurrentDensity` | 1 | `Type`: Inward current density (`Jn`, default) / Current density (`J0`); −n·J = Jn |
| Boundary Current Source | `BoundaryCurrentSource` | 1 | `Qj` (A/m²); interior source/sink |
| Distributed Impedance | `DistributedImpedance` | 1 | `Vref`; `LayerSpecification`: Thin layer (ds, σ, εr) / Surface impedance (ρs Ω·m², Cs F/m²) |
| Terminal | `Terminal` | 1 or 2 | `TerminalName`, `TerminalType`: **Current (default, I0=0 A → open circuit) / Voltage (V0, default 1 V) / Circuit (cir coupling; TD/FD only) / Power (P0=1 W, cycle-averaged in FD) / Terminated (power) (P0, Zref, S-params) / Terminated (voltage)**; `Vinit`, `Iinit` (Power only); domain-level Terminal replaces conductor interior with single constant |
| Electric Shielding | `ElectricShielding` | 1 | thin conducting shield, `ds` |
| Contact Impedance | `ContactImpedance` | 1 | thin layer contact between conductors, `ds`, σ |
| Electrical Contact | `ElectricalContact` | 1 | surface conductance between touching boundaries |
| Sector Symmetry | `SectorSymmetry` | 1 | sector geometry symmetry |
| Symmetry Plane (for Electric Field) | `SymmetryPlane` | 1 | Symmetry / Antisymmetry |
| Periodic Condition | `PeriodicCondition` | 1 | Continuity / Antiperiodicity |
| Line Current Source | `LineCurrentSource` | 0 (3D edges) | `QL` (A/m) |
| Line Current Source (on Axis) | `LineCurrentSourceOnAxis` | 0 | axisymmetric |
| Point Current Source | `PointCurrentSource` | 0 | `QP` (A) |
| Point Current Source (on Axis) | `PointCurrentSourceOnAxis` | 0 | |
| Electric Point Dipole | `ElectricPointDipole` | 0 | `p` dipole moment (A·m), `np` direction |

Terminal types used with `ElectricalCircuit` (`cir`) coupling: circuit "External I vs U" / "External U vs I" / "External I-Terminal" nodes bind by terminal name.

---

## 4. Magnetic Fields Interface (`mf`)

Dependent variable: **Magnetic vector potential A** (default Quadratic; Linear/Cubic). Solves Ampère's law ∇×(μ₀⁻¹μr⁻¹∇×A) = J. Interface settings: Background field (Solve for Full field / Reduced field with Background specification: Magnetic vector potential Ab or Uniform magnetic flux density Bb), Components (2D: Out-of-plane / In-plane / Three-component vector potential; 3D always three-component), Out-of-plane thickness d, Port sweep settings (Zref, PortName). Default nodes: `FreeSpace`, `MagneticInsulation` (default BC), `init`.

### 4.1 Domain features (dim=2)

| Node (UI) | Feature type string | Key properties |
|---|---|---|
| Free Space | `FreeSpace` | adds Ampère's law, μr=εr=1, `StabilizationConductivity` (From material / Automatic / From skin depth / Off / User defined) |
| Ampère's Law | `AmperesLaw` | `MaterialType` (Solids/Fluids), `MagnetizationModel`: **RelativePermeability** (μr, default) / BHCurve (B-H curve) / MagneticLosses (μ′, μ″; FD only) / RemanentFluxDensity (Br, μrec, e) / Magnetization (M) / EffectiveBHCurve / HysteresisJilesAtherton (Ms, a, k, c, α) / NonlinearPermanentMagnet (Hc) / AnalyticMagnetizationCurve / ExternalMaterial; `ElectricConductivity` σ (JC-E section); `RelativePermittivity` εr (D-E section); subnodes `EffectiveMedium`, `ArchieLaw` |
| Ampère's Law, Piezomagnetic | `AmperesLawPiezomagnetic` | with Piezomagnetism multiphysics (mf + solid + `PiezomagneticEffect`) |
| Ampère's Law, Magnetostrictive | `AmperesLawMagnetostrictive` | obsolete (≤6.0), cannot be added in 6.1+ |
| External Current Density | `ExternalCurrentDensity` | `Je` (A/m²) |
| Velocity (Lorentz Term) | `Velocity` | `VelocityField` v → J = σ(E + v×B) |
| Initial Values | `init` | `A` components |
| Force Calculation | `ForceCalculation` | force/torque vars `<name>.Forcex_...`, `<name>.Torquex_...` |
| Gauge Fixing for A-Field | `GaugeFixingA` | enforces ∇·A = 0 (needed for In-plane/Three-component in 2D, and 3D) |
| Coil | `Coil` | `CoilName`, `ConductorModel`: **Single conductor (default) / Homogenized multiturn / Homogenized litz coil**; 3D `CoilType` (Numeric default / Circular / Linear / User defined); `CoilExcitation`: **Current (Icoil, default 1 A) / Voltage (Vcoil) / Circuit (current) / Circuit (voltage) / Power (Pcoil, 2D only)**; Homogenized conductor: `NumberTurns` N (default 10), Wire properties (From conductivity / From resistivity / From resistance / From resistance and mutually coupled circuit), wire area (Filling factor / From diameter / Standard wire gauge / American wire gauge / User defined), `IncludeHarmonicLoss`; 2D `CoilGroup` option; subnodes: `CoilGeometry` (circular/linear), `UserDefinedCoilGeometry` (with `CoilInput`, `CoilOutput`), `GeometryAnalysis` (with `Input`, `Output`, `ElectricInsulation`, `ConnectedBoundaries`, `PeriodicBoundaries`), `LossCalculation`, `CoilHarmonicPerturbation`, `CoilReferenceEdge`, `ReverseCoilGroupDomain`; needs `CoilGeometryAnalysis` study step for Numeric/Single conductor in 3D |
| Single Conductor Coil | `SingleConductorCoil` | obsolete (use Coil with Single conductor); subnodes `BoundaryFeed`, `GapFeed`, `Ground`, `FloatingPotential` |
| Lumped Port | `LumpedPort` | `LumpedPortName`, port type (2D: Out-of-plane / In-plane); voltage/current excitation, lumped impedance |
| Lumped Element | `LumpedElement` | RLC lumped element |
| Edge Current | `EdgeCurrent` | `I0` (A) on edges (2D) |
| External Magnetic Vector Potential | `ExternalMagneticVectorPotential` | `A0` (Wb/m) |
| Laminated Core | `LaminatedCore` | laminated iron core model |
| Passive Conductor | `PassiveConductor` | coil-like conductor without excitation |
| Magnet | `Magnet` | subnodes `North`, `South`, `DomainDirection` |
| Magnetic Point Dipole | `MagneticPointDipole` | dipole moment (A·m²) |
| Magnetic Point Dipole (on Axis) | `MagneticPointDipoleOnAxis` | axisymmetric |
| Electric Point Dipole | `ElectricPointDipole` | current dipole (A·m) |
| Line Current (Out-of-Plane) | `LineCurrentOutOfPlane` | `I0` (A) at 2D points |
| Line Current (on Axis) | `LineCurrentOnAxis` | `Iz` (A), axisymmetric edges |

### 4.2 Boundary features (dim=1)

| Node (UI) | Feature type string | Key properties / equation |
|---|---|---|
| Magnetic Insulation (default) | `MagneticInsulation` | n × A = 0; lossless metallic surface / symmetry; supports interior boundaries with surface currents |
| Perfect Magnetic Conductor | `PerfectMagneticConductor` | n × H = 0; high surface impedance / symmetry |
| Tangential Magnetic Field | `TangentialMagneticField` | `H0` (A/m); n × H = n × H0 |
| Surface Current Density | `SurfaceCurrent` | `Js0` (A/m); n × H = −Js |
| Surface Magnetic Current Density | `SurfaceMagneticCurrentDensity` | `Jms0` (V/m); n × E = Jms |
| Tangential Magnetic Vector Potential | `TangentialMagneticVectorPotential` | `A0` (Wb/m); n × A = n × A0 |
| Exterior Electric Insulation | `ExteriorElectricInsulation` | exterior only; electric insulation via truncated scalar potential |
| Impedance Boundary Condition | `ImpedanceBoundaryCondition` | surface impedance Zs, lossy walls |
| Layered Impedance Boundary Condition | `LayeredImpedanceBoundaryCondition` | layered lossy surface |
| Transition Boundary Condition | `TransitionBoundaryCondition` | thin layer with fields on both sides; subnode `SurfaceCurrent` |
| Layered Transition Boundary Condition | `LayeredTransitionBoundaryCondition` | layered thin layer |
| Thin Low Permeability Gap | `ThinLowPermeabilityGap` | μr, d (5 mm default) |
| Magnetic Shielding | `MagneticShielding` | thin magnetic shield |
| Symmetry Plane (for Magnetic Flux Density) | `SymmetryPlane` | Symmetry (n·B=0) / Antisymmetry (n×B=0) |
| Periodic Magnetic Continuity | `PeriodicMagneticContinuity` | pair-based periodicity |
| Continuity | `Continuity` | identity-pair continuity (assembly); `ContinuityConstraintParameters`: Automatic / Legacy |
| Gap Feed / Boundary Feed / Ground / Floating Potential | (Single Conductor Coil subnodes) | coil potential excitation on boundaries |
| Axial Symmetry | `AxialSymmetry` | auto-added on r=0 axis in axisymmetry |

---

## 5. Electromagnetic Waves (frequency-domain EM; RF Module)

Full settings docs: `RF_Module\RFModuleUsersGuide.pdf`. ACDC guide references these interfaces for full-Maxwell (wave) regimes only; the ACDC Module itself is for low-frequency/quasistatic modeling.

### 5.1 Interfaces
- `ElectromagneticWaves` (tag `emw`) — classic frequency-domain interface (wave equation in E).
- `ElectromagneticWavesFrequencyDomain` (tag `ewfd`) — explicit frequency-domain type string; same feature set.
- `ElectromagneticWavesBeamEnvelopes` (`ewbe`), `ElectromagneticWavesTransient` (`ewt`), `TransientElectromagneticWaves` (`temw`).

Dependent variable: **Electric field E** (vector, Quadratic/Linear). Governing equation: ∇×(μr⁻¹∇×E) − k₀²εrcE = 0, k₀ = ω/c₀.

### 5.2 Features (emw / ewfd)

| Node (UI) | Feature type string | Key properties |
|---|---|---|
| Wave Equation, Electric (main domain) | `WaveEquationElectric` | `ElectricDisplacementFieldModel`: Relative permittivity (default) / Refractive index / Loss tangent, loss angle / Loss tangent, dissipation factor / Dielectric loss / Drude–Lorentz dispersion / Debye dispersion / Wideband Debye; `RelativePermeability` μr, `ElectricConductivity` σ, `EffectiveRefractiveIndex` (Beam Envelopes); subnode `DrudeLorentzPolarization` (ewt) |
| Initial Values | `init` | E components (V/m) |
| Perfect Electric Conductor (default BC) | `PerfectElectricConductor` | n × E = 0 |
| Perfect Magnetic Conductor | `PerfectMagneticConductor` | n × H = 0 |
| Impedance | `Impedance` | `Z0` surface impedance |
| Scattering | `Scattering` | `FarFieldScattering` boundary; subnode `ReferencePoint` (ewbe) |
| Surface Current | `SurfaceCurrent` | `Js0` |
| Transition Boundary Condition | `TransitionBoundaryCondition` | thin layer; `LayeredTransitionBoundaryCondition` |
| Periodic Condition | `PeriodicCondition` | Continuity / Antiperiodicity / Floquet (kF) |
| Port | `Port` | `PortName`, port type (Rectangular, Circular, Coaxial, etc.), `PortExcitation` (On/Off), `WaveExcitationType`, `PortModeNumber`; subnodes `DiffractionOrder`, `OrthogonalPolarization`, `PeriodicPortReferencePoint`, `CircularPortReferenceAxis`, `ElectricPotential`, `Ground` |
| Lumped Port | `LumpedPort` | `LumpedPortName`, `TypeOfLumpedPort` (Coaxial / User defined / Via), `TerminalType` (Cable port), `SourceType` (Voltage V0 / Power P0), `Zref`; subnode `UniformElement` |
| Lumped Element | `LumpedElement` | lumped RLC/coaxial element |
| Far-Field Domain | `FarFieldDomain` | `FarFieldVariableName` (default Efar); subnode `FarFieldCalculation` |
| Specific Absorption Rate | `SpecificAbsorptionRate` | SAR computation |
| Mixed Mode S-Parameters | `MixedModeSparameters` | mixed-mode S-matrix |
| Polarization | `Polarization` | polarization reference direction |
| Global Equations | `GlobalEquations` | global unknowns |
| Axial Symmetry | `AxialSymmetry` | axisymmetric |

---

## 6. Expression Reference (variables)

Naming: `<physics_name>.<variable>`. Units shown; all components exist (x/y/z, r/phi/z).

### Electrostatics (`es`)
| Expression | Meaning | Unit |
|---|---|---|
| `es.V` | electric potential | V |
| `es.Ex`, `es.Ey`, `es.Ez` | electric field components E = −∇V | V/m |
| `es.normE` | |E| field norm | V/m |
| `es.Dx`, `es.Dy`, `es.Dz` | electric displacement field components | C/m² |
| `es.normD` | |D| | C/m² |
| `es.rho` | space charge density (Space Charge Density node) | C/m³ |
| `es.intWe` | integral of electrostatic energy density over domains (2W_e; used in energy method for capacitance) | J |
| `es.Wel` | electrostatic energy density we = ε₀εr E·E / 2 | J/m³ |
| `es.Q0` / `es.I0` | terminal charge / current (per Terminal name) | C / A |
| `es.C11`, `es.C12` … | capacitance matrix entries (lumped parameters) | F |
| `es.Forcex_<fn>` / `es.Torquex_<fn>` | force / torque from Force Calculation | N / N·m |

Verified in working piezo code: `maxop1(es.V)`, `aveop_top(es.Dz)` (Scheme1 scripts).

### Electric Currents (`ec`)
| Expression | Meaning | Unit |
|---|---|---|
| `ec.V` | electric potential | V |
| `ec.Jx`, `ec.Jy`, `ec.Jz` | current density components | A/m² |
| `ec.normJ` | |J| | A/m² |
| `ec.Ex/Ey/Ez`, `ec.normE` | electric field | V/m |
| `ec.Qj` | current source | A/m³ |
| `ec.I0` | terminal current | A |
| `ec.R11` / `ec.Z11` | resistance / impedance matrix entries (lumped) | Ω |
| `ec.Qh` | Joule heating source term (with Heat Transfer coupling) | W/m³ |

### Magnetic Fields (`mf`)
| Expression | Meaning | Unit |
|---|---|---|
| `mf.Ax`, `mf.Ay`, `mf.Az` | magnetic vector potential components | Wb/m |
| `mf.normA` | |A| | Wb/m |
| `mf.Bx/By/Bz`, `mf.normB` | magnetic flux density | T |
| `mf.Hx/Hy/Hz`, `mf.normH` | magnetic field | A/m |
| `mf.Jx/Jy/Jz`, `mf.normJ` | induced current density | A/m² |
| `mf.intWm` | integral of magnetic energy density (energy method → inductance) | J |
| `mf.Wm` | magnetic energy density | J/m³ |
| `mf.Icoil` / `mf.Vcoil` | coil current / voltage (per Coil name) | A / V |
| `mf.Lcoil` | coil inductance (lumped) | H |
| `mf.Forcex_<fn>` / `mf.Torquex_<fn>` | force / torque | N / N·m |

### Electromagnetic Waves (`emw`)
| Expression | Meaning | Unit |
|---|---|---|
| `emw.Ex/Ey/Ez`, `emw.normE` | electric field (dependent variable) | V/m |
| `emw.Hx/Hy/Hz`, `emw.normH` | magnetic field | A/m |
| `emw.Sx/Sy/Sz`, `emw.normS` | Poynting vector | W/m² |
| `emw.Poav` | cycle-averaged power flow | W |
| `emw.S11`, `emw.S21` … | S-parameters (ports) | dB |
| `emw.Efar` | far-field variable (Far-Field Domain) | V/m |

Capacitance / inductance via energy method: C = 2·intWe/V², L = 2·intWm/I² (used by Terminal / Coil lumped parameters; "energy method" documented in ACDC guide for capacitance/inductance computation).

---

## 7. Practical API Notes

- **Piezoelectricity preset** (piezo): `comp.multiphysics().create('pze1', 'PiezoelectricEffect', 2)` couples `solid` + `es`; es gets `ChargeConservationPiezo` (type string `ChargeConservationPiezo`, NOT `ChargeConservation`) and solid gets `PiezoelectricMaterialModel` with strain-charge `e` matrix + `epsilon` (εrS) + `C` stiffness (see `api_structural.md` §3).
- **Dependent variable sharing**: renaming es.V to share DOFs with another interface is supported (used for es↔esbe couplings).
- **Terminal naming**: Terminal/Coil/Port names must be numeric for sweeps (parametric sweep over `PortName`).
- **Circuit coupling**: `Terminal` (es/ec) with type Circuit, or mf `Coil` excitation Circuit (current/voltage), bind to `ElectricalCircuit` interface nodes (External I vs U / External U vs I / External I-Terminal) via terminal name.
- **2D axisymmetry**: axial-symmetry boundary at r=0 auto-adds `AxialSymmetry` node; axis-specific features: Line Charge (on Axis), Point Charge (on Axis), Line Current (on Axis), Magnetic Point Dipole (on Axis).
- **Feature tag prefixes** (from tags.json): ChargeConservation→`ccn*`, Ground→`gnd*`, ElectricPotential→`pot*`, Terminal→`term*`, FloatingPotential→`fp*`, ZeroCharge→`zc*`, SurfaceChargeDensity→`sfcd*`, SpaceChargeDensity→`scd*`, CurrentConservation→`cucn*`, ElectricInsulation→`ein*`, NormalCurrentDensity→`ncd*`, MagneticInsulation→`mi*`, AmperesLaw→`al*`, PerfectMagneticConductor→`pmc*`, PerfectElectricConductor→`pec*`, WaveEquationElectric→`wee*`.
