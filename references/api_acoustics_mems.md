# Acoustics + MEMS Modules — API Reference (acpr, actd, ta, pabe, pzr*, emi)

Sources:
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Acoustics_Module\AcousticsModuleUsersGuide.pdf` (COMSOL 6.4)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Acoustics_Module\IntroductionToAcousticsModule.pdf`
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\MEMS_Module\MEMSModuleUsersGuide.pdf` (COMSOL 6.4)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\MEMS_Module\IntroductionToMEMSModule.pdf`
- mph tags.json (exact feature type strings) via `references/tags_physics.md`; feature names in the tables below match the guide's node labels

Conventions (same as `api_acdc.md` / `api_structural.md`):
- **Feature type string** = Java/model-tree node type passed to `physics.feature().create(tag, 'TypeString', dim)`. Case-sensitive CamelCase.
- **dim** = geometric entity dimension: `2` = domains (3D) / boundaries (2D); `1` = boundaries (3D) / edges (2D) / points (1D); `0` = edges (3D) / points (2D). In the Acoustics module docs, "boundary" nodes include edge/point variants per dimension.
- `<name>.<var>` pattern for all variables, `<name>` = interface Name (default `acpr`, `actd`, `ta`, `pabe`, `tff`, `pzrd`, ...).
- Interface creation (Java): `comp.physics().create('acpr', 'PressureAcoustics', 'geom1')`. In the Model Wizard the physics interface branch names are "Pressure Acoustics", "Thermoviscous Acoustics", etc.
- Study compatibility per interface listed below; acoustics frequency-domain interfaces support eigenfrequency, frequency domain, frequency-domain modal, and (2D/1D axisym) mode analysis.

---

# Part A — Acoustics Module

## A.1 Physics Interfaces — Tags and Space Dimensions

| Interface | Type string (tags.json) | Tag | Space dims | Notes / studies |
|---|---|---|---|---|
| Pressure Acoustics, Frequency Domain | `PressureAcoustics` | `acpr` | all dims | eigenfrequency; frequency domain; freq-domain modal; adaptive frequency sweep; mode analysis (2D/1D axisym); boundary mode analysis (3D/2D axisym) |
| Pressure Acoustics, Transient | `PressureAcousticsTransient` | `actd` | all dims | eigenfrequency; freq domain; freq-domain modal; time dependent; time-dependent modal; mode analysis (2D/1D axisym) |
| Pressure Acoustics, Boundary Mode | `PressureAcousticsBoundaryMode` | `acbm` | 3D, 2D | mode analysis; boundary FE mode shapes for Ports |
| Pressure Acoustics, Boundary Elements | `PressureAcousticsBoundaryElements` | `pabe` | 3D, 2D | frequency domain; BEM, no volume mesh needed; `bpam` model node |
| Pressure Acoustics, Time Explicit | `PressureAcousticsTimeExplicit` | `pate` | 3D, 2D, 2D axisym | time dependent; DG-FEM; `patem` model node |
| Pressure Acoustics, Asymptotic Scattering | `PressureAcousticsAsymptoticScattering` | `paas` | 3D | frequency domain |
| Pressure Acoustics, Kirchhoff–Helmholtz | `PressureAcousticsKirchhoffHelmholtz` | `pakh` | 3D, 2D | frequency domain |
| Thermoviscous Acoustics, Frequency Domain | `ThermoacousticsSinglePhysics` | `ta` | all dims | eigenfrequency; freq domain; freq-domain modal; mode analysis (2D/1D axisym). Solves p, u, T (linearized Navier–Stokes + energy) |
| Thermoviscous Acoustics, Transient | `ThermoacousticsSinglePhysicsTransient` | `tatd` | all dims | time dependent |
| Thermoviscous Acoustics, Boundary Mode | `ThermoviscousAcousticsBoundaryMode` | `tabm` | 3D, 2D | mode analysis |
| Thermoviscous Acoustics, SLNS Approximation | `ThermoviscousAcousticsSLNS` | `slns` | 3D, 2D, 2D axisym | frequency domain; Sequential Linearized Navier–Stokes, cheaper boundary-layer losses |
| Linearized Euler, Frequency Domain | `LinearizedEulerFrequencyDomain` | `lef` | 3D, 2D, 2D axisym, 1D | frequency domain; eigenfrequency; mode analysis |
| Linearized Euler, Transient | `LinearizedEulerTransient` | `let` | 3D, 2D, 2D axisym, 1D | time dependent |
| Linearized Euler, Boundary Mode | `LinearizedEulerBoundaryMode` | `lebm` | 3D, 2D | mode analysis |
| Linearized Potential Flow, Frequency Domain | `LinearizedPotentialFlowFrequencyDomain` | `lpf` | all dims | frequency domain; mode analysis |
| Linearized Potential Flow, Transient | `LinearizedPotentialFlowTransient` | `lpt` | all dims | frequency domain; time dependent; mode analysis |
| Linearized Potential Flow, Boundary Mode | `LinearizedPotentialFlowBoundaryMode` | `lpbm` | 3D, 2D | mode analysis |
| Compressible Potential Flow | `CompressiblePotentialFlow` | `cpf` | all dims | stationary; time dependent |
| Imported Fluid Flow | `ImportedFluidFlow` | `iff` | 3D | mapping; transient mapping (aeroacoustics) |
| Linearized Navier–Stokes, Frequency Domain | `LinearizedNavierStokesFrequencyDomain` | `lnsf` | 3D, 2D, 2D axisym, 1D | frequency domain; eigenfrequency; mode analysis |
| Linearized Navier–Stokes, Transient | `LinearizedNavierStokesTransient` | `lnst` | 3D, 2D, 2D axisym, 1D | time dependent |
| Linearized Navier–Stokes, Boundary Mode | `LinearizedNavierStokesBoundaryMode` | `lnsbm` | 3D, 2D | mode analysis |
| Convected Wave Equation, Time Explicit | `ConvectedWaveEquationTimeExplicit` | `cwe` | 3D, 2D, 2D axisym | time dependent |
| Nonlinear Pressure Acoustics, Time Explicit | `NonlinearPressureAcousticsTimeExplicit` | `nate` | 3D, 2D, 2D axisym | time dependent |
| Ray Acoustics | `RayAcoustics` | `rac` | 3D, 2D, 2D axisym | ray tracing; time dependent |
| Acoustic Diffusion Equation | `AcousticDiffusionEquation` | `ade` | 3D | eigenvalue; stationary; time dependent |
| Pipe Acoustics, Frequency Domain | `PipeAcousticsFrequencyDomain` | `pafd` | 3D, 2D | eigenfrequency; frequency domain |
| Pipe Acoustics, Transient | `PipeAcousticsTransient` | `patd` | 3D, 2D | time dependent |
| Acoustic Streaming from Pressure Acoustics | `AcousticStreamingFromPressureAcoustics` | — | 3D, 2D, 2D axisym | frequency–stationary; frequency–transient |
| Acoustic Streaming from Thermoviscous Acoustics | `AcousticStreamingFromThermoviscousAcoustics` | — | 3D, 2D, 2D axisym | frequency–stationary; frequency–transient |

Notes: (1) `PressureAcoustics`, `SolidMechanics`, `Piezoelectricity`(partial) are core-COMSOL interfaces with module-added functionality. (2) Predefined multiphysics interfaces (add all sub-interfaces + couplings automatically) are flagged in the docs; e.g. Acoustic–Solid Interaction, Acoustic–Shell Interaction, Acoustic–Piezoelectric Interaction (3D, 2D axisym; eigenfrequency/frequency domain/transient), Acoustic–Solid–Poroelastic Waves Interaction, Acoustic–Poroelastic Waves Interaction, Acoustic–Solid Interaction Time Explicit. (3) Some interfaces require the Structural Mechanics, AC/DC, or MEMS modules (footnotes in the interface guide).

## A.2 Pressure Acoustics, Frequency Domain (`acpr`)

Dependent variable: **acoustic pressure p** (default: Quadratic Lagrange). Solves the Helmholtz equation for time-harmonic waves, `e^{iωt}` convention. Scattered/total field via `BackgroundPressureField`. Continuity in total pressure is the default on interior boundaries.

Default nodes on creation: `PressureAcoustics` (model, tag `fpam` → `FrequencyPressureAcousticsModel`), `SoundHard` (default exterior BC, tag `shb*`), `init` (Initial Values).

### A.2.1 Domain features (dim = 2)

| Node (UI) | Feature type string | Key properties |
|---|---|---|
| Pressure Acoustics | `FrequencyPressureAcousticsModel` | `ModelInput` (absolute pressure pA, temperature T from material/user), `FluidModel`: Lossless, Thermally Conducting (uses heat capacity Cp + thermal conductivity k), Thermally Conducting and Viscous (adds bulk viscosity μB, dynamic viscosity μ), Ocean attenuation (semianalytical, inputs T, Depth D, salinity Sp, pH; for ray tracing over large distances); Speed of sound c, Density ρ (From material / User defined); `BulkAttenuation`; `Activate port sweep` (compute full S-matrix); `SoundPressureLevel` ref pressure (Use reference pressure for air 20 µPa / water 1 µPa / User defined), zero level; Discretization |
| Poroacoustics | `PoroacousticsModel` | equivalent-fluid models: Johnson–Champoux–Allard (JCA) (rigid frame), Lafarge (adds thermal permeability), Miki, Qunli, Modified Allard and Champoux, Wood, Williams EDFM; Porous matrix properties (flow resistivity, porosity, tortuosity, viscous/thermal characteristic lengths), Fluid properties |
| Narrow Region Acoustics | `NarrowRegionAcousticsModel` | homogenized viscous/thermal boundary-layer losses in constant-cross-section waveguides; ducts: Slit, Circular, Rectangular (N terms, default 100), Equilateral triangular; low reduced frequency (LRF); not for eigenfrequency without care (frequency-dependent model) |
| Anisotropic Acoustics | `AnisotropicAcousticsModel` | effective bulk modulus K + anisotropic density tensor; metamaterials / fibrous materials; `CoordinateSystem` |
| Anisotropic Poroacoustics | `AnisotropicPoroacousticsModel` | as Poroacoustics with anisotropic flow resistivity Rf, tortuosity α∞, viscous characteristic length Λ |
| Background Pressure Field | `BackgroundPressureField` | `Type`: Plane wave, Cylindrical wave, Spherical wave, User defined; `PressureFieldInput` (Amplitude p0, Wave direction kdirx/kdiry/kdirz, source position); enables scattered-field formulation; option to calculate background/scattered intensity |
| Initial Values | `init` | p initial value |
| Monopole Domain Source | `MonopoleDomainSource` | `Qm` monopole source strength (1/s²) |
| Dipole Domain Source | `DipoleDomainSource` | `Fd` vector dipole force density (N/m³) |
| Heat Source | `HeatSource` | `Qheat` (W/m³); uses ambient T model input (coefficient of thermal expansion) |
| Aeroacoustic Flow Source | `AeroacousticFlowSource` | 3D only; Lighthill-like source from stress tensor Tij; couples to fluid-flow via `AeroacousticFlowSourceCoupling` (LES/DES/RANS-EVM SST-SAS or Imported Fluid Flow + Transient Mapping study); `WindowFunction` |
| Flame Model | `FlameModel` | n–τ combustion model heat source; `FlameModel` n, time delay τ, reference flame transfer function; `AcousticReference` |

### A.2.2 Boundary features (dim = 1)

| Node (UI) | Feature type string | Key properties / equation |
|---|---|---|
| Sound Hard Boundary (Wall) (default) | `SoundHard` | n·(−1/ρc²)∇p_t = 0 (normal acceleration zero); tag `shb*` |
| Axial Symmetry | `AxialSymmetry` | default on symmetry axis in axisymmetric models |
| Normal Acceleration | `NormalAcceleration` | inward normal acceleration a_n: −n·(−1/ρc²)∇p_t = −a_n/iω; used for prescribed wall motion |
| Normal Velocity | `NormalVelocity` | v_n: −n·(−1/ρc²)∇p_t = −v_n (harmonic) |
| Normal Displacement | `NormalDisplacement` | d_n: −n·(−1/ρc²)∇p_t = ω²d_n ... (harmonic displacement) |
| Sound Soft Boundary | `SoundSoft` | p_t = 0 (liquid–gas interface / simple open ends) |
| Pressure | `Pressure` | p_t = p0 (constant pressure source; amplitude in freq domain) |
| Impedance | `Impedance` | −n·(−1/ρc²)∇p_t = −iωp_t/Zn; `ImpedanceModel`: User defined (only one valid in time domain), RCL (Serial/Parallel circuits of Rac, Lac, Cac), Physiological (Human skin, Outward human ear radiation, Human ear drum, Human ear without pinna, Human ear full), Waveguide end impedance (Flanged pipe circular/rectangular, Unflanged pipe circular ±low-ka), Porous layer (thickness d, backed by sound-hard wall; Normal/Automatic=50° random incidence/User defined/From angle of incidence; all Poroacoustics models), Specific characteristic impedance (plane/cylindrical/spherical wave), Absorption Coefficient (α_n + phase φ); `BoundaryGeometry` area (Use symmetries / Selected boundaries) for RCL + Physiological; rayl units: `[rayl]`=Pa·s/m, `[rayl_cgs]`=10 rayl |
| Symmetry | `Symmetry` | p symmetry; mathematically identical to Sound Hard |
| Periodic Condition | `PeriodicCondition` | Periodicity types: Continuity, Antiperiodicity, Floquet (Bloch) periodicity; Destination selection; used with Periodic Port |
| Matched Boundary | `MatchedBoundary` | nonreflecting; allows 1–2 modes (k1, k2) out with minimal reflection; Incident Pressure Field subnode |
| Exterior Field Calculation | `ExteriorFieldCalculation` | integral (Kirchhoff–Helmholtz) of boundary data to points outside; `AdvancedSettings`; evaluates e.g. `acpr.efc1.pext`, `acpr.efc1.Lp_pext`, directivity; used with Radiation Pattern plots |
| Port | `Port` | waveguide excitation/absorption, one mode per port; `Type`: User defined, Numeric, Circular, Annular, Rectangular, Slit, User defined (nondispersive); mode shape p_n, wave number k_n (User defined: 1 and acpr.k for plane wave); Rectangular: mode numbers m,n on longest/shortest side; incident excitation On/Off (Amplitude A_pin / Power P_in + phase); S-parameter output `acpr.S11` etc.; cutoff freq vars `acpr.port1.fc`; numeric ports: solve Boundary Mode first, reference with `withsol()`; normalization: unit max amplitude or unit apparent power |
| Port Reference Axis | `CircularPortReferenceAxis` | two points defining azimuthal reference axis; required for Circular/Annular ports |
| Periodic Port | `PeriodicPort` | transmission/reflection/scattering of periodic structures; with Floquet Periodic Condition; incident plane wave (Amplitude/Power, polar + azimuthal angle, Reference corner in 3D); subnode Diffraction Order Port |
| Diffraction Order Port | `DiffractionOrderPort` | subfeature of Periodic Port; order m (2D), m,n (3D); include pairs ±; check `imag(acpr.pport1.dport1.kn)` to confirm all propagating orders captured |
| Lumped Port | `LumpedPort` | connects waveguide end to Electrical Circuit / transfer matrix / lumped waveguide; plane waves only; `ConnectionType`: Two port network (transfer matrix T11..T22), Electrical Circuit (circuit reference), Lumped waveguide; Source settings; Impedance; Incident mode; place ≥1 waveguide diameter from geometry features |
| Lumped Speaker Boundary | `LumpedSpeakerBoundary` | loudspeaker/transducer lumped model coupled to Electrical Circuit (Thiele–Small parameters); `SpeakerGeometry` area, `BackVolumeCorrection` (Volume compliance / RCL circuit / User defined impedance); `Circuit` |
| Thermoviscous Boundary Layer Impedance | `ThermoviscousBoundaryLayerImpedance` | BLI model; integrates viscous+thermal boundary-layer losses analytically; `MechanicalCondition` (Velocity/Displacement), `ThermalCondition` (Isothermal/Adiabatic), `WallProperties`, `FluidProperties`; not for overlapping boundary layers / very narrow waveguides |
| Transfer Matrix Coupling | `TransferMatrixCoupling` | couples two boundaries (source+destination) via transfer matrix; `MappingBetweenSourceAndDestination` |
| Plane Wave Radiation | `PlaneWaveRadiation` | nonreflecting, plane wave, near-normal incidence; subnode Incident Pressure Field |
| Spherical Wave Radiation | `SphericalWaveRadiation` | nonreflecting, spherical wave, source location r0; subnode Incident Pressure Field |
| Cylindrical Wave Radiation | `CylindricalWaveRadiation` | nonreflecting, cylindrical wave, source location + axis direction; subnode Incident Pressure Field |
| Incident Pressure Field | `IncidentPressureField` | subnode of Matched Boundary / Plane / Spherical / Cylindrical Wave Radiation; `PressureFieldType`: Plane wave, Cylindrical wave, Spherical wave, User defined; plane-wave expansion built in for 2D axisym scattering |
| Perfectly Matched Boundary | `PerfectlyMatchedBoundary` | frequency domain only; PML via extra dimension, no geometry layer; `ScalingAndMesh` (Typical wavelength from / User defined) |
| Interior Sound Hard Boundary (Wall) | `InteriorSoundHard` | sound hard on interior boundaries |
| Interior Normal Acceleration | `InteriorNormalAcceleration` | pressure slit; prescribed acceleration (e.g. speaker cone as boundary); `SlitCondition` |
| Interior Normal Velocity | `InteriorNormalVelocity` | slit condition, velocity = iω×acceleration counterpart |
| Interior Normal Displacement | `InteriorNormalDisplacement` | slit condition, prescribed displacement |
| Interior Impedance / Pair Impedance | `InteriorImpedance` | transfer impedance: p_t,down − p_t,up = Z_t v; `ImpedanceModel` User defined, Perforated plate, Thin plate, Membrane, Porous mass layer; Incident wave settings |
| Interior Perforated Plate / Pair Perforated Plate | `InteriorPerforatedPlate` | Model types: Thin plate (default), Finite thickness plate, Semi-empirical model (Maa/Allard); hole radius, porosity, plate thickness, FLUID PROPERTIES |
| Interior Lumped Speaker Boundary | `InteriorLumpedSpeakerBoundary` | lumped speaker on interior boundary; includes both-side fluid loading explicitly |
| Continuity | `Continuity` | pair condition: continuity of total pressure + normal acceleration |

### A.2.3 Edge / point features (dim = 1 edge 3D / 0 point 2D, dim = 0 point 3D)

| Node (UI) | Feature type string | Key properties |
|---|---|---|
| Line Source | `FrequencyAcousticLineSource` | along edges (3D) / boundaries (2D); `LineSourceStrength` QS, source phase, orientation |
| Line Source on Axis | `LineSourceOnAxis` | 2D axisym, source on symmetry axis (r=0) |
| Monopole Point Source | `FrequencyMonopolePointSource` | points (3D); strength QS, phase; only when point is inside the domain |
| Dipole Point Source | `DipolePointSource` | points; dipole strength FD + direction |
| Quadrupole Point Source | `QuadrupolePointSource` | points; quadrupole strength |
| Point Sources (for 2D Components) | `FrequencyMonopolePointSource` (2D variants) | 2D monopole/dipole point sources |
| Circular Source (for 2D Axisymmetric Components) | `CircularSource` | ring source at (r0, z0) in 2D axisym |
| Pressure (Point Condition) | `PressurePointCondition` | fixed pressure at point |
| AWE Expression | `AWEExpression` | Asymptotic Waveform Evaluation expression (frequency-domain AWE reduced-order modeling) |

## A.3 Pressure Acoustics, Transient (`actd`)

Same node set as acpr (shares nodes), plus:
- `PressureAcousticsTransientModel` model node: `EquationForm` (wave equation / mixed formulation), Courant number control for the time-explicit/discontinuous formulations; time-domain Impedance uses partial-fraction approximation; Gaussian Pulse source type in Incident Pressure Field (time domain); background pressure field for transient models; time-domain PMLs (polynomial/rational stretching, ≥8 mesh layers, typical wavelength = c[1/s] per Hz); exterior field calculation for transient.

## A.4 Thermoacoustics / Thermoviscous Acoustics (`ta`, `tatd`, `tabm`, `slns`)

"Thermoviscous acoustics is also known as viscothermal acoustics or sometimes thermoacoustics." Solves linearized Navier–Stokes (continuity + momentum + energy) for **p, u, T** — needed for microacoustics where viscous (δ_v) and thermal (δ_th) penetration depths matter. Scattered-field formulation with `BackgroundAcousticFields`. Postprocessing vars: `ta.d_visc`, `ta.d_therm`, `ta.Pr` (Prandtl).

### A.4.1 `ta` (ThermoacousticsSinglePhysics) features

| Node (UI) | Feature type string | Key properties |
|---|---|---|
| Thermoviscous Acoustics Model | `ThermoviscousAcousticsModel` | `AdiabaticFormulation` (drop T DOF; liquids); Model Inputs (T0, p0); Fluid Properties (viscosity, thermal conductivity, heat capacity, bulk viscosity, ratio of specific heats, thermal expansion); Sound pressure level settings; Typical wave speed for PMLs; Stabilization; Global port settings |
| Background Acoustic Fields | `BackgroundAcousticFields` | background p_b, u_b, T_b (user-defined expressions or predefined waves) |
| Heat Source | `HeatSource` | acoustic heat source |
| Initial Values | `init` | initial p, u, T |
| Axial Symmetry | `AxialSymmetry` | axisym default |
| Wall | `Wall` | default exterior; Mechanical (No slip / Slip (perfect) / Slip length), Thermal (Isothermal / Adiabatic / Temperature variation) |
| Pressure (Adiabatic) | `PressureAdiabatic` | prescribed total pressure (adiabatic) |
| Symmetry | `Symmetry` | symmetry in p, u, T |
| Slip Wall | `SlipWall` | rarefied gas effects; `SlipModel` (Maxwell slip, Smoluchowski temperature jump); thermal accommodation coefficient, momentum accommodation coefficient |
| Port | `Port` | mode excitation/absorption incl. viscothermal mode shapes (numeric from Boundary Mode) |
| Lumped Port | `LumpedPort` | lumped element / circuit connection |
| Lumped Speaker Boundary | `LumpedSpeakerBoundary` | lumped transducer + circuit |
| Periodic Condition | `PeriodicCondition` | continuity/antiperiodic/Floquet |
| Interior Wall | `InteriorWall` | interior wall (both sides) |
| Interior Impedance | `InteriorImpedance` | transfer impedance between two thermoviscous domains |
| Interior Velocity | `InteriorVelocity` | prescribed velocity on interior boundary |
| Interior Temperature Variation | `InteriorTemperatureVariation` | prescribed temperature variation |
| Interior Lumped Speaker Boundary | `InteriorLumpedSpeakerBoundary` | interior lumped transducer |
| Interior Slip Wall | `InteriorSlipWall` | rarefied interior wall |
| Surface Tension | `SurfaceTension` | free-surface capillary BC (fluid interface) |
| No Slip | `NoSlip` | u = 0 at solid wall (thermal subfeature settings) |
| Slip (Perfect) | `SlipPerfect` | n·u = 0 at wall |
| Velocity | `Velocity` | prescribed velocity boundary |
| No Stress | `NoStress` | traction-free |
| Boundary Stress | `BoundaryStress` | prescribed traction |
| Impedance | `Impedance` | impedance relation between T and p variations |
| Isothermal | `Isothermal` | T = 0 (isothermal wall) |
| Adiabatic | `Adiabatic` | n·∇T = 0 |
| Temperature Variation | `TemperatureVariation` | prescribed T |
| Heat Flux | `HeatFlux` | prescribed heat flux |

### A.4.2 `tatd` (ThermoacousticsSinglePhysicsTransient)
Same model + `NonlinearThermoviscousAcousticsContributions` (`NonlinearThermoviscousAcousticsContributions` → `ntac*`) for nonlinear terms; transient boundary conditions: Impedance, Lumped Speaker Boundary, Interior Lumped Speaker Boundary, Wall; time-explicit DG-FEM option for convection-dominated problems.

### A.4.3 `tabm` (Thermoviscous Acoustics, Boundary Mode)
Boundary mode analysis of the linearized Navier–Stokes equations: solves out-of-plane wave number at given frequency on a boundary; feeds numeric `Port` mode shapes; features: ThermoviscousAcousticsModel, Impedance.

### A.4.4 `slns` (Thermoviscous Acoustics, SLNS Approximation)
Sequential Linearized Navier–Stokes: pressure acoustics enhanced with viscous + thermal scaling functions v, th; much cheaper than full ta. Features: Wall, Pressure, Impedance, Symmetry, Periodic Condition, Lumped Port, Lumped Speaker Boundary, Monopole/Dipole Domain Source, Background Pressure Field, Initial Values, Axial Symmetry, Normal Acceleration/Velocity/Displacement.

### A.4.5 Thermoviscous predefined multiphysics interfaces
- Acoustic–Thermoviscous Acoustic Interaction, Frequency Domain: ta + acpr + `AcousticThermoviscousAcousticBoundary` coupling.
- Thermoviscous Acoustic–Solid Interaction, Frequency Domain: ta + solid + `ThermoviscousAcousticStructureBoundary`.
- Thermoviscous Acoustic–Shell Interaction, Frequency Domain (3D, 2D axisym): ta + shell; needs Structural Mechanics Module.
- Thermoviscous Acoustic–Thermoelasticity Interaction (Frequency Domain + Transient; 3D, 2D, 2D axisym): ta/tatd + Thermoelasticity (solid + ht + Thermal Expansion); needs MEMS Module; MEMS damping applications.

## A.5 Multiphysics Couplings (Acoustics Module)

### A.5.1 Coupling features (addable manually under the Multiphysics node)

| Coupling (UI) | Couples | Key settings |
|---|---|---|
| Acoustic–Structure Boundary (`asb1`) | acpr/actd/pabe ↔ solid, shell, layered shell, membrane, multibody dynamics | fluid load f_a = p_t n; structural acceleration n·u_tt; slit for thin interior structures; 2D thickness rescaling; subfeature `ThermoviscousBoundaryLayerImpedance` (BLI losses at wall) |
| Pair Acoustic–Structure Boundary | acpr/actd ↔ solid on identity pairs | nonconforming mesh at interface |
| Thermoviscous Acoustic–Structure Boundary (`tsb1`) | ta/tatd ↔ solid, shell, layered shell, membrane, multibody | Mechanical: No slip / Slip (perfect); Thermal: Isothermal / Adiabatic; Constraint: Study controlled (weak for eigenfrequency) / Weak / Nitsche / Pointwise; Elemental/Nodal; special eigenfrequency formulation |
| Pair Thermoviscous Acoustic–Structure Boundary | ta/tatd ↔ solid on pairs | nonconforming mesh; Thermal isothermal/adiabatic |
| Thermoviscous Acoustic–Thermoelasticity Boundary | ta/tatd ↔ solid + ht (Thermoelasticity) | Mechanical No slip / Slip (perfect); Frequency-Domain Perturbation or Time Dependent studies only (stationary temperature linearization point) |
| Thermoviscous Acoustic–Thermal Perturbation Boundary | ta temperature field ↔ ht (solids/fluids) | couples acoustic T to HT perturbation; requires mechanical condition on acoustic side; MEMS/water-glass systems |
| Thermoviscous Acoustic SLNS-Structure Boundary (`tssb1`) | slns ↔ solid, shell, layered shell, membrane, multibody | Mechanical No slip / Slip (perfect, default); Thermal Isothermal / Adiabatic (default); sets up v and th scaling functions |
| Aeroacoustic–Structure Boundary (`aesb1`) | lnsf/lnst ↔ solid, shell, layered shell, membrane, multibody | Mechanical No slip / Slip (perfect); Thermal Isothermal (default) / Adiabatic; frequency-domain FSI |
| Acoustic–Thermoviscous Acoustic Boundary | ta ↔ acpr (FEM or BEM) | continuity of total normal stress + normal acceleration; adiabatic temperature condition; hybrid ta-near-walls / pa-elsewhere models; warning: unphysical at common walls with no-slip+isothermal ta |
| Pair Acoustic–Thermoviscous Acoustic Boundary | ta ↔ acpr on pairs | — |
| Acoustic-Acoustic Boundary | FEM–FEM acoustics | domain-to-domain coupling |
| Acoustic–Porous Boundary | acpr ↔ poroacoustics | continuity of pressure and normal velocity at porous interface |
| Porous–Structure Boundary | poroacoustics ↔ solid | Biot poroelastic coupling (couples fluid pressure + solid) |
| Background Potential Flow Coupling | flow ↔ LPF (convected acoustics) | maps fluid flow solution to background potential flow |
| Background Fluid Flow Coupling | flow ↔ LNS/LEF | maps velocity, pressure, density, temperature; `VariablesToMap`; Smoothing (Isotropic diffusion default 1e-4 / None); used with Transient Mapping |
| Aeroacoustic Flow Source Coupling | flow ↔ acpr `AeroacousticFlowSource` | Lighthill stress tensor from flow solution |
| Acoustic BEM–FEM Boundary (`apb1`) | pabe ↔ acpr | bidirectional; continuity in total pressure; subfeature `Impedance` (User defined / Perforated plate / Thin plate / Membrane / Porous mass layer) |
| Acoustic–Pipe Acoustic Connection (`apc1`) | pafd/patd ↔ acpr | point (1D pipe end) ↔ boundary; quiescent mean flow |
| Acoustic–Structure Boundary, Time Explicit (`asbte1`) | pate/nate ↔ elte | DG-FEM ASI; prefer pair version |
| Pair Acoustic–Structure Boundary, Time Explicit (`aspte1`) | pate/nate ↔ elte on pairs | nonconforming meshes, CFL-controlled; quadrature-free flux w/ projection quadrature default |
| Convected Acoustic–Structure Boundary, Time Explicit | cwe ↔ elte | convected wave equation ASI |
| Pair Convected Acoustic–Structure Boundary, Time Explicit | cwe ↔ elte on pairs | — |
| Piezoelectricity, Time Explicit | pate/nate ↔ elte + es | piezo transducers in time-explicit vibroacoustics |
| Piezoelectricity | solid + es (piezo) | standard piezo coupling (see api_structural) |
| Magnetomechanics, Solid | solid + mf | magnetostriction / magnetomechanics |
| Acoustic Streaming Domain Coupling | acoustic ↔ flow | body force f_aco for streaming |
| Acoustic Streaming Boundary Coupling | acoustic ↔ flow | slip velocity v_slip at boundaries (Stokes slip) |

### A.5.2 Predefined multiphysics interfaces
Vibroacoustics: Acoustic–Solid Interaction (FD/Transient), Acoustic–Shell Interaction (FD/Transient), Acoustic–Piezoelectric Interaction (FD/Transient), Acoustic–Solid–Poroelastic Waves Interaction, Acoustic–Poroelastic Waves Interaction, Acoustic–Solid Interaction Time Explicit. Acoustic streaming: from Pressure Acoustics / from Thermoviscous Acoustics. Modeling notes: use Selections to limit coupling domains; Override behavior for nested couplings; PML setup guidance.

## A.6 Expression Reference (key variables)

Variable prefix = interface Name (default `acpr`, `ta`, ...). All are global unless noted.

### A.6.1 Sound pressure level & acoustic quantities
- `acpr.Lp` — sound pressure level (dB) computed from rms pressure vs reference pressure (default 20 µPa air / 1 µPa water; settable in interface Sound Pressure Level settings).
- `acpr.p` — total acoustic pressure field; `acpr.pt` total incl. background, `acpr.ps`/scattered variants with Background Pressure Field.
- `acpr.c` — speed of sound; `acpr.rho`/`acpr.rho_c` — density / characteristic impedance ρc; `acpr.K_eq` — effective bulk modulus (narrow region/poroacoustics); `acpr.k` — wave number (use in User defined port mode shapes).
- `acpr.Rf` (flow resistivity), `acpr.epsilon_p` (porosity), `acpr.mu`, `acpr.tau` (tortuosity), `acpr.Lv` (viscous characteristic length) — poroacoustics.

### A.6.2 Intensity (frequency domain)
- `acpr.Ix`, `acpr.Iy`, `acpr.Iz` (2D: Ix, Iy; 2D axisym: Ir, Iz), `acpr.I_mag` — intensity vector components / magnitude (W/m²), I = ½Re(p u*).

### A.6.3 Power dissipation
- `acpr.diss_visc` — viscous power dissipation density; `acpr.diss_therm` — thermal dissipation density; `acpr.diss_tot` — total; `acpr.Q_pw` — plane-wave total dissipated power density Q_pw = −2|I|·Im(k) (valid for traveling plane waves only).

### A.6.4 Port / S-parameter / lumped quantities (global)
- `acpr.S11`, `acpr.S21`, ... — scattering matrix elements (port sweep); `acpr.S` — full scattering matrix; `acpr.T11`..`acpr.T22` — transfer matrix (two ports); `acpr.Z11`..`acpr.Z22` — impedance matrix (two ports, plane waves only); `acpr.TL_12` — transmission loss between ports 1 and 2.
- `acpr.port1.pn` — normalized mode shape of Port 1; `acpr.port1.fc` — port cutoff frequency; `acpr.pport1.dport1.kn` — diffraction-order-port wave number (imaginary part → evanescent check).
- `acpr.lport1.p1`, `acpr.lport1.p2`, `acpr.lport1.Lp1`, `acpr.lport1.Lp2` — Lumped Port pressures / SPL.
- `acpr.efc1.pext`, `acpr.efc1.Lp_pext`, `acpr.efc1.P_rad` — Exterior Field Calculation external pressure / SPL / radiated power; `acpr.efc1.nx/ny/nz` — evaluation normal.
- `acpr.imp1.alpha_n`, `acpr.imp1.alpha_ran` — normal / random incidence absorption coefficient of Impedance feature `imp1`; `acpr.imp1.p_ear_drum` — ear-drum pressure (Physiological models).
- `acpr.bpf1.kdirx/kdiry/kdirz` — Background Pressure Field wave direction components.
- `acpr.p_i` — incident pressure.

### A.6.5 Thermoviscous acoustics (`ta`)
- `ta.d_visc`, `ta.d_therm` — viscous / thermal penetration depths; `ta.Pr` — Prandtl number; `ta.c` — speed of sound; `ta.T0`, `ta.p0` — background temperature/pressure model inputs; `ta.v_real`, `ta.v_imag`, `ta.v_rms` — velocity components (real/imag/rms); `ta.diss_visc`, `ta.diss_therm`, `ta.diss_tot`; port variables `ta.S11`, `ta.T11`, `ta.Z11` as for acpr.
- `ta.Lp` — SPL; dependent variables: p (pressure), u/v/w (velocity), T (temperature variation); total-field variants pt, ut, Tt.

### A.6.6 Other interfaces
- `pabe.Lp`, `pabe.p` — BEM pressure acoustics; `rac.Lp`, `rac.LI` — ray acoustics SPL / sound intensity level; `ade.Lp` — acoustic diffusion equation SPL; `pate`/`nate`/`cwe`/`elte` — time-explicit interfaces (use `at3_spatial()`/`withsol()` for point evaluation).
- `at2()`, `at3()`, `at2_spatial()`, `at3_spatial()` — evaluation operators for globally defined variables (e.g. `at2(x,y,acpr.Lp)` inside EFC boundary).

---

# Part B — MEMS Module

## B.1 Physics Interfaces — Tags, Variables, Studies

| Interface | Tag | Dependent vars | Preset studies (subset) |
|---|---|---|---|
| Electrostatics | `es` | V | stationary; eigenfrequency; freq domain; time dependent |
| Electric Currents | `ec` | V | stationary; freq domain; time dependent |
| Electrical Circuit | `cir` | (circuit DOFs) | stationary; time dependent; freq domain |
| Thin-Film Flow | `tff` | p_f | stationary; time dependent |
| Thin-Film Flow, Domain | `tff` (domain variant, `ThinFilmFlowDomain`) | p_f | stationary; time dependent |
| Fluid–Structure Interaction | — | u,v,w; p | stationary; time dependent |
| Fluid–Structure Interaction, Fixed Geometry | — | u,v,w; p | stationary; time dependent |
| Solid Mechanics | `solid` | u,v,w | stationary; eigenfrequency; time dependent; freq domain; prestressed; buckling; response spectrum; random vibration; modal ROM; AWE ROM |
| Piezoelectricity (predefined) | — | u,v,w; V | as solid + es (incl. small-signal analysis, freq domain) |
| Thermal Stress | — | u,v,w; T | stationary; time dependent |
| Thermoelasticity | `te` | u,v,w; T | time dependent; thermal perturbation eigenfrequency; thermal perturbation freq domain |
| Joule Heating and Thermal Expansion | — | u,v,w; T; V | stationary; time dependent |
| Electromechanics | `emi` | u,v,w; V | stationary; eigenfrequency, prestressed; time dependent; frequency domain, prestressed |
| Electromechanics, Boundary Elements | `emibe` | u,v,w; V (BEM) | stationary; eigenfrequency, prestressed; time dependent; freq domain, prestressed |
| Electromechanics, Shell | — | shell vars; V | stationary; eigenfrequency prestressed; time dependent; freq domain prestressed |
| Electromechanics, Membrane | — | membrane vars; V | stationary; eigenfrequency prestressed; time dependent; freq domain prestressed |
| Piezoresistivity, Domain Currents | `pzrd` | u,v,w; V | stationary; time dependent; freq domain |
| Piezoresistivity, Boundary Currents | `pzrb` | u,v,w; V (surface) | stationary; time dependent; freq domain |
| Piezoresistivity, Shell | `pzrs` | shell vars; V | stationary; time dependent; freq domain |
| Piezoresistivity, Layered Shell | `pzrl` | layered shell vars; V | stationary; time dependent; freq domain |
| Pyroelectricity | `pye` | V; T | stationary; time dependent |
| Piezoelectricity and Pyroelectricity | — | u,v,w; V; T | stationary; time dependent; freq domain |

Note: Electromechanics, Shell / Membrane require the Structural Mechanics Module. Piezoresistivity, Layered Shell and Piezoelectricity, Layered Shell require Structural Mechanics Module (Shell). Detailed feature docs for `Electromechanics, Solid`, `Electromechanics, Boundary Elements`, `Thermal Stress, Solid`, `Joule Heating and Thermal Expansion`, `Piezoelectricity, Solid`, `Fluid–Solid Interaction` live in the Structural Mechanics Module User's Guide (Multiphysics Interfaces and Couplings chapter) — see `api_structural.md`.

## B.2 Multiphysics Coupling Types (MEMS)

Coupling families (Table 1-1 of the guide):

| Family | Phenomena / couplings |
|---|---|
| Electromechanical | Electrostructural, Electrothermal, Thermomechanical, Thermal-electric-structural, Piezoelectric, Piezoresistive, Prestressed modal analysis, Stress stiffening |
| Fluid–structure interaction | Moving boundary (ALE), Squeeze-film damping |
| Typical devices | Cantilever beams, comb drives, resonators, micromirrors, thermomechanical actuators, inertial sensors, pressure sensors, mechanical pumps/valves |

Predefined multiphysics interfaces in the MEMS module (add the constituent physics + couplings automatically):
- **Pyroelectricity** (`pye`): es + ht + `Pyroelectricity` coupling.
- **Piezoelectricity and Pyroelectricity**: solid + es + ht + `Piezoelectricity` + `Pyroelectricity` + `ThermalExpansion` couplings.
- **Thermoelasticity** (`te`): solid + ht + `ThermalExpansion` (thermoelastic damping enabled by default).
- **Electromechanics** (`emi`): solid + es + `Electromechanics` coupling + `MovingMesh` (deforming domains, electrostatic forces via Maxwell stress); isotropic electrostriction optional.
- **Electromechanics, Boundary Elements**: solid + `Electrostatics, Boundary Elements` + `Electromechanics` coupling (no Moving Mesh needed; BEM electrostatics on domain boundaries).
- **Piezoresistivity, Domain Currents** (`pzrd`): solid + ec + `Piezoresistivity, Domain Currents` coupling.
- **Piezoresistivity, Boundary Currents** (`pzrb`): solid + `Electric Currents in Shells` + `Piezoresistivity, Boundary Currents` coupling.
- **Piezoresistivity, Shell** (`pzrs`): shell + `Electric Currents, Shell` + `Piezoresistivity, Shell` coupling.
- **Piezoresistivity, Layered Shell**: layered shell + `Electric Currents in Layered Shells` + `Piezoresistivity, Layered` coupling.
- Thin-Film Flow / Fluid–Structure Interaction families (see below).

Circuit coupling: connect any physics interface to the Electrical Circuit interface via `Terminal`/`Circuit` boundary conditions; predefined couplings add the circuit automatically (e.g. Lumped Port, Lumped Speaker Boundary in Acoustics; Terminal + circuit in es/ec); user-defined couplings via Terminal nodes with circuit references.

## B.3 Electromechanics Features (MEMS-relevant)

Full feature docs: `api_structural.md` (Electromechanics, Solid; Electromechanics, Boundary Elements). MEMS-specific facts from the MEMS docs:

- `Electromechanics` (`emi`, tag in table; Model Wizard branch Structural Mechanics) = Electrostatics + Solid Mechanics + Electromechanics coupling + Moving Mesh. Electrostatic forces are added to the structure; used for electrostatically actuated MEMS (comb drives, accelerometers, micromirrors, capacitive sensors). Force via Maxwell stress tensor on the es/solid interface.
- `Electromechanics, Boundary Elements` — same physics but electrostatics solved by BEM; no Moving Mesh required; forces from Maxwell stress on boundaries.
- **Isotropic electrostriction** optional in Electromechanics, Solid (stress tensor augmented; see SM guide).
- **D-V formulation**: with the `Electromechanics` coupling, es default discretization is Mixed Finite Element (quadratic). Optionally use the es **D-V formulation** (mixed FE solving D + V) — recommended for comb drives in tight geometries because forces are derived from D (Maxwell stress); see `api_acdc.md`.
- **Force Calculation / Maxwell stress**: `ForceCalculation` feature computes force/torque from Maxwell stress tensor (`es.Forcex_<name>`, etc.). `Electromechanics` coupling and `ForceCalculation` both use the Maxwell stress tensor.
- **Lumped parameters**: capacitance via es `Terminal` BC (energy method: C = 2W_e/V²; or charge method); resistance/conductance via ec Terminals; impedance/admittance matrices in the time-harmonic case; conversion Z↔Y and to C/L/R via formulas in the Lumped Parameters section (chapter 2 of the MEMS guide).
- **Reduced-order modeling / electromechanical coupling factor**: ROM + Equivalent Circuit workflow (chapter 2): apply 1 V → induced modal forces F_UT = Γ V; `Γ_i` = electromechanical coupling factor per mode; reciprocal: modal motional current `i_mot,i` relates to displacement; builds equivalent-circuit / state-space models from eigenmode data.
- **Electrostatic fringing / scaling**: electrostatic forces scale with size (L² vs inertia L³); for 2D models use out-of-plane thickness d.
- **Squeeze-film damping**: Thin-Film Damping boundary condition available on solid, Piezoelectricity, Electromechanics, and Joule Heating and Thermal Expansion interfaces — auto-couples damping forces from the thin gas film (Reynolds equation); Knudsen number effects via slip boundary conditions.

## B.4 Piezoresistivity Interfaces (`pzrd`, `pzrb`, `pzrs`, `pzrl`)

Physics: unidirectional effect — stress changes resistivity (no reverse coupling). E = ρ·J + Δρ·J with Δρ = π:S (piezoresistance form) or Δρ = M:ε (elastoresistance form); π (m²/Pa... units Pa⁻¹·m as matrix; guide: π SI unit Pa⁻¹m, M SI unit m), both rank-4 tensors in Voigt notation. Effective conductivity σ(c,eff) = (σ(c)⁻¹ + Δρ)⁻¹ (tensor inversion).

### B.4.1 Piezoresistivity, Domain Currents (`pzrd`)
Predefined interface: solid + ec + `Piezoresistivity, Domain Currents` coupling. Use when conducting/piezoresistive layer thickness is resolved by the mesh.
- Default ec node: **Current Conservation, Piezoresistive** (`ChargeConservationPiezoResistive`; tag class `pzrc*`) — all piezoresistivity properties entered here (conductivity form; resistivity model isotropic/anisotropic; dopant number density as model input; resistivity+piezo coefficients From material / User defined).
- Coupling node `Piezoresistivity, Domain Currents` (`PiezoresistivityDomainCurrents` → `pzrd*`): computes conductivity tensor from stress/strain of `LinearElasticMaterial` (or `HyperelasticMaterial`) + piezo properties; active only where both features are active.
- Domain equation: ∇·(σ(c,eff)(−∇V) − J_e) + ∂/∂t(ε₀ε(r)∇V) = Q_j.
- Coupled with solid `LinearElasticMaterial`; also supports `HyperelasticMaterial`.
- Material libraries: single-crystal silicon (Smith 1957), polysilicon, plus user-defined.

### B.4.2 Piezoresistivity, Boundary Currents (`pzrb`)
For thin piezoresistive layers (≈100 nm) on thick structural layers — layer modeled as a boundary.
- solid + `Electric Currents in Shells` + `Piezoresistivity, Boundary Currents` coupling.
- Default node: **Piezoresistive Shell** (`PiezoresistiveShell` → `pzrs*`) — layer thickness h, conductivity, piezo coefficients; tangential form: ∇_t·(d_s σ(c,eff) ∇_t V) ... = Q_j.

### B.4.3 Piezoresistivity, Shell (`pzrs`)
Structural layer thin enough for the Shell interface, conducting layer even thinner.
- `Shell` + `Electric Currents in Shells` + `Piezoresistivity, Shell` coupling; active where `PiezoresistiveShell` and `LinearElasticMaterial` overlap. Requires Structural Mechanics Module.

### B.4.4 Piezoresistivity, Layered Shell (`pzrl`)
- `LayeredShell` + `Electric Currents in Layered Shells` + `Piezoresistivity, Layered` coupling; piezoresistance or elastoresistance form selectable.

### B.4.5 Theory / material property notes
- Voigt notation used throughout (reduced subscript: s1..s6, r1..r6); π and M matrices are not symmetric in general (triclinic); m = D·π (D = elasticity matrix, Voigt).
- Engineering convention: π = ρ₀·π′ (relative change of resistivity per unit stress, Pa⁻¹), M = ρ₀·M′ (dimensionless); valid for cubic materials (isotropic unstressed resistivity, e.g. silicon); properties then doping-independent below ~10¹⁶ cm⁻³.
- Piezoresistance coefficients for silicon: π11, π12, π44 set (from Smith); material orientation via **local coordinate system** (Rotated System, Euler angles; quadratic transformation laws for reduced matrices); solid mechanics solved in local CS, electric currents in global CS.
- Material libraries: MEMS Material Library, Piezoelectric Materials Library, Piezoresistivity Material Library (4 materials × 7 properties).
- Example apps: Piezoresistive Pressure Sensor (`MEMS_Module/Sensors/piezoresistive_pressure_sensor`), shell version (`..._shell`).

## B.5 Pyroelectricity / Piezoelectricity+Pyroelectricity / Thermoelasticity

### B.5.1 Pyroelectricity (`pye`)
es + ht + `Pyroelectricity` coupling (`pye1`). Direct pyroelectric + inverse electrocaloric effects.
- `Pyroelectricity` coupling `CouplingType`: Pyroelectric effect (P_e = (T−Tref)·p_ET), Electrocaloric effect (Q_p = −T ∂/∂t(p_ET·E)), Fully coupled (default).
- `CouplingSettings`: Total pyroelectric coefficient p_ET (C/(m²·K)), vector in selected coordinate system; Reference temperature Tref (default 293.15 K). Relation p_ET = p_ES + e·α (primary clamped + secondary).
- Applicable es domains: `ChargeConservation` (solid), `ChargeConservationPiezo`, `ChargeConservationFerroelectric`; ht domains: `Solid` (+ Fluid for convection).

### B.5.2 Piezoelectricity and Pyroelectricity
solid + es + ht; automatically adds three couplings: `Piezoelectricity`, `Pyroelectricity`, `ThermalExpansion`. Default features: `PiezoelectricMaterial` (solid; piezo coupling data + structural/electrical material data entered here) and `ChargeConservationPiezo` (es). Coupling active where both are active.

### B.5.3 Thermoelasticity (`te`)
solid + ht + `ThermalExpansion` coupling with `Thermoelastic damping` enabled; `StructuralTransientBehavior` = Include inertial terms. Computes thermoelastic damping of vibrating MEMS (quality factor limits).
- Recommended studies only: Time Dependent; Thermal Perturbation, Eigenfrequency; Thermal Perturbation, Frequency Domain (stationary step establishes baseline temperature = linearization point).
- Temperature variable has two components in freq domain: baseline + harmonic perturbation; `Temperature` BC sets baseline, right-click → `Harmonic Perturbation` subnode for the harmonic part.
- Equations: first law dU = T_a ds + (1/ρ₀) σ:dε; second Piola–Kirchhoff stress split into elastic (work) and inelastic (heat, damping) parts; Duhamel–Hooke linear thermoelasticity; thermal expansivity includes temperature dependence from material library.
- Example: Thermoelastic Damping in a MEMS Resonator (`MEMS_Module/Actuators/thermoelastic_damping_3d`).

## B.6 Thin-Film Damping (squeeze-film) — quick reference
- `ThinFilmFlow` (`tff`, `ThinFilmFlowDomain`) interfaces solve the (modified) Reynolds equation: full form (pressure + density) and pressure-only form (`EquationType` setting); include squeeze-film and slide-film damping; rarefaction via slip length / Knudsen number.
- Boundary-condition variant: **Thin-Film Damping** on solid/Electromechanics/Piezoelectricity/Joule Heating interfaces (thin gap between moving and fixed walls, gas squeeze-film).
- Example apps: microresistor beam, microresonator damping models under `MEMS_Module/...`.
