# Heat Transfer & CFD Modules — API Reference (ht, htlsh, lts, rad, mt, spf)

Sources:
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Heat_Transfer_Module\HeatTransferModuleUsersGuide.pdf` (COMSOL 6.4, 1068 pp) — Chapters 3 (Variables), 5 (Interfaces), 6 (Features), 8 (Multiphysics Interfaces), 9 (Multiphysics Couplings)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\CFD_Module\CFDModuleUsersGuide.pdf` (COMSOL 6.4, 1164 pp) — Chapter 3 (Single-Phase Flow Interfaces) incl. theory
- mph tags.json (exact feature type strings) via `references/tags_physics.md`

Conventions (same as `api_structural.md` / `api_acdc.md`):
- **Feature type string** = Java/model-tree node type passed to
  `physics.feature().create(tag, 'TypeString', dim)` (mph) / `create(tag, type, dim)` (Java).
  Case-sensitive CamelCase, no spaces (`Heat Transfer in Solids` → `HeatTransferInSolids`,
  `Temperature` boundary → `TemperatureBoundary`).
- **dim** = geometric entity dimension: `2` = domains (3D) / boundaries (2D); `1` = boundaries (3D) / edges (2D); `0` = edges (3D) / points (2D).
- Default tags: `ht` (Heat Transfer, all versions), `htlsh` (Heat Transfer in Shells/Films/Fractures), `lts` (Lumped Thermal System), `rad` (Surface-to-Surface Radiation), `otl` (Orbital Thermal Loads), `rpm`/`rasm`/`rbam` (radiation in participating media), `mt`/`mts` (moisture), `spf` (all single-phase flow interfaces, laminar + turbulent + LES + DES + creeping).
- `<name>.<var>` pattern for all variables; `<name>` = interface Name (default as above).
- Physics creation: `comp.physics().create('ht', 'HeatTransferInSolids', 'geom1')`; `comp.physics().create('spf', 'LaminarFlow', 'geom1')`.
- Constraint implementation options on Dirichlet-type features: Pointwise (default), Weak, Nitsche.

---

## 1. Heat Transfer Module — Physics Interfaces

### 1.1 Interface table (Table 5-1 of HT Users Guide)

| Interface (UI) | Type string | Tag | Notes |
|---|---|---|---|
| Heat Transfer in Solids | `HeatTransferInSolids` | `ht` | conduction; default nodes: `SolidHeatTransferModel` (Solid), `ThermalInsulation` (default BC), `init` (Initial Values); Quadratic T |
| Heat Transfer in Fluids | `HeatTransferInFluids` | `ht` | convection–diffusion; default: `FluidHeatTransferModel` (Fluid), `ThermalInsulation`, `init`; Linear T |
| Heat Transfer in Solids and Fluids | `HeatTransferInSolidsAndFluids` | `ht` | default: Solid active on all domains + Fluid added inactive; used by Conjugate Heat Transfer |
| Bioheat Transfer | `BioheatTransfer` | `ht` | living tissue; blood perfusion, metabolic heat, thermal damage |
| Heat Transfer in Porous Media | `HeatTransferInPorousMedia` | `ht` | default `PorousMediumHeatTransferModel` (Local thermal equilibrium) |
| Local Thermal Nonequilibrium | `LocalThermalNonequilibrium` | `ht` | solid+fluid phase temperatures solved separately, coupled via transfer term |
| Heat Transfer in Packed Beds | `HeatTransferInPackedBeds` | `ht` | pellet + fluid phase, radial pellet conduction |
| Heat Transfer in Moist Porous Media | `HeatTransferInMoistPorousMedia` | `ht` | via Heat and Moisture Transport multiphysics |
| Heat Transfer in Building Materials | `HeatTransferInBuildingMaterials` | `ht` | default `BuildingMaterialHeatTransferModel`; 2nd-order T |
| Heat Transfer in Moist Air | `HeatTransferInMoistAir` | `ht` | default `MoistAirHeatTransferModel` |
| Heat Transfer in Shells | `HeatTransferInShells` | `htlsh` | layered shells, extra dimension; default: `SolidLayeredShell`, `ThermalInsulation`, `init` |
| Heat Transfer in Films | `HeatTransferInFilms` | `htlsh` | default `FluidLayeredShell` (Fluid) |
| Heat Transfer in Fractures | `HeatTransferInFractures` | `htlsh` | default `PorousMediumLayeredShell` (Porous Medium) |
| Lumped Thermal System | `LumpedThermalSystem` | `lts` | discrete (0D) thermal network: thermal resistors, capacitors, heat pipes, TECs, subsystems |
| Surface-to-Surface Radiation | `SurfaceToSurfaceRadiation` | `rad` | radiosity on opaque/diffuse surfaces; view factors; Ray shooting or Hemicube method |
| Orbital Thermal Loads | `OrbitalThermalLoads` | `otl` | orbital heating (sun, albedo, IR) |
| Radiation in Participating Media | `RadiationInParticipatingMedia` | `rpm` | P1 / Rosseland / Discrete ordinates; radiative intensity I |
| Radiation in Absorbing–Scattering Media | `RadiationInAbsorbingScatteringMedia` | `rasm` | |
| Radiative Beam in Absorbing Media | `RadiativeBeamInAbsorbingMedia` | `rbam` | Beer–Lambert beams |
| Moisture Transport in Air / Porous Media / Building Materials / Free and Porous Media | `MoistureTransport` | `mt` | relative humidity φ in moist air / porous media |
| Moisture Transport in Solids | `MoistureTransportInSolids` | `mts` | |
| Heat Transfer in Pipes | `HeatTransferPipes` | `htp` | Pipe Flow Module (1D) |

Turbulent heat transfer interface variants (Conjugate Heat Transfer / Nonisothermal Flow, see §3): turbulent flow versions pair `ht` with `TurbulentFlow*` interfaces (Algebraic yPlus, L-VEL, k-ε, Realizable k-ε, k-ω, SST, Low Re k-ε, Spalart–Allmaras, v2-f).

Default nodes added for a heat transfer interface: domain model node (Solid/Fluid/Porous Medium/…), `ThermalInsulation` (default exterior BC), `Initial Values`. `IsothermalDomainInterface` is auto-added when an `IsothermalDomain` feature exists.

### 1.2 Domain features (dim = 2)

| Node (UI) | Feature type string | Tag | Key properties / equation |
|---|---|---|---|
| Solid | `SolidHeatTransferModel` | `solid*` | ρCp(∂T/∂t + u·∇T) + ∇·q = Q, q = −k∇T. `ThermalConductivity` (k: Isotropic/Diagonal/Symmetric/Full; `from_mat` default), `Density` ρ, `HeatCapacity` Cp, `VelocityField` u (Moving Mesh); anisotropic k → vars ht.kxx, ht.kyy, ht.kzz, ht.kmean |
| Fluid | `FluidHeatTransferModel` | `fluid*` | convection–diffusion. `VelocityField` u (select `Velocity field (spf)` or user defined), `Density`, `HeatCapacityCp`, `ThermalConductivity`, `DynamicViscosity`, `AbsolutePressure` pA; subnodes: `PhaseChangeMaterial` (`phc*`), `PressureWork` (`pw*`), `ConvectivelyEnhancedConductivity` (`cec*`), `Opacity` (`opac*`) |
| Porous Medium | `PorousMediumHeatTransferModel` | `porous*` | subnodes: `FluidPorousMediumHeatTransferModel` (`fluid*`), `PorousMatrixPorousMediumHeatTransferModel` (`pm*`), `ImmobileFluidPorousMaterial` (`imf*`); heat sources/fluxes per phase scaled by volume fraction |
| Moist Air | `MoistAirHeatTransferModel` | `ma*` | dry-bulb T; moisture-coupled thermodynamics |
| Building Material | `BuildingMaterialHeatTransferModel` | `bm*` | porous medium + moisture, latent heat of evaporation in dflux |
| Isothermal Domain | `IsothermalDomain` | `id*` | single T for a domain set |
| Heat Source | `HeatSource` | `hs*` | Q = Q0. `HeatSource` list: General source (Q0, W/m³), Linear source (`qs` production/absorption coefficient), Heat rate (P0, then Q0 = P0/V). Preset sources: `Total power dissipation density (ec)`, `Electromagnetic heating (mf)`, `(mef)`, `(emw)`. MaterialType: Solid (material frame, default) / Nonsolid (spatial frame) / From material |
| Initial Values | `init` | `init*` | initial T |
| Bioheat | `BioHeat` | `bio*` | metabolic heat Qmet + blood perfusion |
| Phase Change Material | `PhaseChangeMaterial` (subnode) | `phc*` | apparent heat capacity / latent heat method |
| Pressure Work | `PressureWork` (subnode) | `pw*` | fluid compression work |
| Viscous Dissipation | `ViscousDissipation` (subnode) | `vd*` | viscous heating μΦ |
| Translational Motion | `TranslationalMotion` (subnode) | `trm*` | solid translation (rotation/linear), ht variables in material frame |
| Thermoelastic Damping | `ThermoelasticDamping` (subnode) | `ted*` | Q ∝ T·∂ε/∂t |
| Thermal Dispersion | `ThermalDispersion` (subnode) | `td*` | porous media dispersion |
| Out-of-Plane Heat Flux | `OutOfPlaneHeatFlux` (subnode) | `oophf*` | 2D/1D: defines q0_u, q0_d, q0_z |
| Out-of-Plane Radiation | `OutOfPlaneRadiation` (subnode) | `oopr*` | defines rflux_u, rflux_d, rflux_z |
| Thickness | `Thickness` (subnode) | `th*` | 2D out-of-plane thickness d / 1D cross-section A |
| Cell Periodicity, Thermal Damage, Shape Memory Alloy, Irreversible Transformation, Geothermal Heating, Convectively Enhanced Conductivity | — | — | advanced specific-media features |

### 1.3 Boundary features (dim = 1; 3D boundaries / 2D edges)

| Node (UI) | Feature type string | Tag | Equation / key properties |
|---|---|---|---|
| Temperature | `TemperatureBoundary` | `temp*` | T = T0 (`Temperature` T0, default 293.15 K; can link to Ambient Properties). Constraints: Pointwise (default) / Weak / Nitsche (good on convection-dominated inlets). Optional `HarmonicPerturbation` subnode |
| Heat Flux | `HeatFluxBoundary` | `hf*` | `FluxType`: **GeneralInwardHeatFlux** (default) −n·q = q0; **ConvectiveHeatFlux** −n·q = h(Text−T) with `HeatTransferCoefficient` h + `ExternalTemperature` Text (user defined or correlations: External/Internal natural/forced convection — vertical wall, horizontal plate, cylinder, sphere, chimney, tube; `Fluid` list Air/Transformer oil/Water/Moist air/From material; `AbsolutePressure` pA, `ExternalRelativeHumidity` φw,ext); **HeatRate** q0 = P0/A; **NucleateBoilingHeatFlux** (Rohsenow: Csf, s, Tsat, Lv, σ) |
| Thermal Insulation | `ThermalInsulation` | `ins*` | −n·q = 0. **Default BC** for all HT interfaces; exterior only by default, interior when added manually |
| Boundary Heat Source | `BoundaryHeatSource` | `bhs*` | −n·q = Qb (W/m²); on pairs applies on source side |
| Surface-to-Ambient Radiation | `SurfaceToAmbientRadiation` | `sar*` | −n·q = εσ(Tamb⁴ − T⁴); `AmbientTemperature` Tamb, `SurfaceEmissivity` ε, `RadiatingSide` (Upside/Downside) |
| Convective Outflow | `ConvectiveOutflow` | `ofl*` | convection-dominated outlet, ∇T·n = 0, no input |
| Inflow | `Inflow` | `ifl*` | Danckwerts inlet condition on enthalpy |
| Open Boundary | `OpenBoundary` | `open*` | outflow: −n·q = 0 (n·u ≥ 0); inflow: −n·q = ρΔH u·n (Flux/Danckwerts default) or T = Tustr (Nitsche). `UpstreamTemperature` Tustr; `InflowCondition` (Flux (Danckwerts) / Nitsche constraints) |
| Symmetry | `Symmetry` | `sym*` | like Thermal Insulation (no flux) for T only |
| Periodic Condition | `PeriodicHeat` | `pc*` | periodic T on pairs; `TemperatureOffset` ΔT; constraints Nitsche (default) / Pointwise / Weak |
| Thermal Contact | `ThermalContact` | `tc*` | −n·q_d = h(Tu−Td) + rQb; interior boundaries or pairs; Contact model: Constriction conductance with interstitial gas / Equivalent thin resistive layer; vars ht.Tu, ht.Td |
| Pair Thermal Contact | `PairThermalContact` | `ptc*` | pair version |
| Continuity | `ContinuityOnInteriorBoundary` | `cib*` | default on interior boundaries (T continuous) |
| Phase Change Interface | `PhaseChangeInterface` | `pci*` | Stefan condition, phase interface tracking |
| Axial Symmetry | `AxialSymmetry` | `axi*` | 2D axisymmetry axis |
| Line Heat Source | `LineHeatSource` (3D edges) | `lihs*` | Ql (W/m), dim=0 |
| Thin Layer (layered solid) | `SolidLayeredShell` | `sls*` | boundary "domain"; its flux accounted in ht.sls1.ntfluxInt, not ht.ntfluxInt |
| Thin Film (layered fluid) | `FluidLayeredShell` | `fls*` | |
| Fracture | (Heat Transfer in Fractures) | — | |
| Lumped System Connector | `LumpedSystemConnector` | `lsc*` | connects FE boundary to lts node |
| Deposited Beam Power | `DepositedBeamPower` | `dbp*` | beam energy deposit (laser) |
| Opaque Surface | `OpaqueSurface` | `os*` | radiation interface BC |

Boundary Interface features (Heat Transfer in Shells): `HeatFluxInterface` (`hfi*`), `TemperatureInterface` (`tempi*`), `HeatSource`, `ThermalInsulation`, `DepositedBeamPowerInterface` (`dbpi*`), `LumpedSystemConnectorInterface`, `SurfaceToAmbientRadiation`, `ThermalContactInterface`, `ContinuityLayeredShell` (`contls*`).

Edge features (dim=0, 3D): `LineHeatSource`, `HeatFlux` (Thin Layer), `Temperature`, `ThermalInsulation`, `Symmetry`, `SurfaceToAmbientRadiation`, `ThinRod`, `ShellContinuity`.
Point features (3D points/2D points): `PointHeatSource`, `PointHeatFlux`, `SurfaceToAmbientRadiation` (Thin Rod), `Temperature` (Thin Rod).

Global features (Lumped Thermal System, dim=0/global): `ThermalConnection` (`thc*`), `ConductiveThermalResistor` (`R*`), `ConvectiveThermalResistor`, `RadiativeThermalResistor`, `ThermalCapacitor` (`C*`), `ThermalMass`, `HeatRateSource`, `HeatRate`, `NucleateBoilingHeatRate`, `HeatPipe`, `ThermoelectricModule` (`TEM` prefix), `ExternalTerminal` (`term*`), `SubsystemDefinition`, `SubsystemInstance`, `ExternalRadiationSource`, `EventsTimeline`, `OrbitalParameters`, `GroundPointing`, `SunProperties`, `PlanetProperties`, `SpacecraftAxes/Orientation`, `ImplicitEvent`, `GenerateEventsInterface`.

### 1.4 Expression reference (prefix `ht`, `htlsh`, `mt`)

Variable naming: `<interface>.<variable>`; e.g. `ht.T`, `ht.tflux`. Reference chapter: HT Users Guide Ch. 3 "Heat Transfer Variables".

Heat/energy balance (global integrals):
- `ht.dEiInt` — total accumulated heat rate (∂/∂t ∫ ρEi)
- `ht.ntfluxInt` — total net heat rate (integral of tflux over exterior boundaries)
- `ht.QInt` — total heat source (domains + interior boundaries + edges + points + radiation)
- `ht.WstrInt` — total stress power (pressure work + viscous dissipation, signed: losses negative)
- `ht.heatBalance` = dEiInt + ntfluxInt + WstrInt − QInt (≈0)
- `ht.dEi0Int`, `ht.ntefluxInt`, `ht.WInt`, `ht.energyBalance` — energy balance counterparts
- Constant-property fast variants: `heatBalance_cst`, `dEiInt_cst`, `ntfluxInt_cst`, `WstrInt_cst`, `QInt_cst`, `energyBalance_cst`, …

Domain variables (vectors, W/m²):
- `ht.tflux` — total heat flux = dflux + cflux (radiative NOT included)
- `ht.dflux` — conductive heat flux = −keff∇T (keff = k, or k+kT turbulent, or porous effective; includes latent heat term for building materials)
- `ht.cflux` — convective heat flux = ρuEi
- `ht.turbflux` — turbulent heat flux = −kT∇T (CFD Module)
- `ht.teflux` — total energy flux = thflux + dflux
- `ht.thflux` — total enthalpy flux = ρuH0
- `ht.Qtot` — total domain heat source (sum of Q, Qmet, Qdmg, Qr, Qgeo, Qevap)

Boundary variables:
- `ht.q0` — inward heat flux (scalar; = h(Text−T) for convective, = P0/A for heat rate)
- `ht.ntflux` — normal total heat flux (ndflux + ncflux)
- `ht.ndflux` — normal conductive heat flux (−dflux·n)
- `ht.ncflux` — normal convective heat flux
- `ht.rflux` — radiative heat flux on boundary = ε(G − eb(T)) + qr,net
- `ht.nteflux`, `ht.nthflux` — normal total energy / enthalpy flux
- `ht.Qbtot` — total boundary heat source (sum Qb, Qsh, Qs), W/m²
- `ht.h` — heat transfer coefficient (convective correlations)
- `ht.nx`, `ht.ny`, `ht.nz` — boundary normal (note: global normal (nx,ny,nz) points downside→upside and may differ in sign from ht.nx…)
- `ht.Tu`, `ht.Td` — upside/downside temperatures (Thermal Contact, thin structures)

Interior boundary (upside/downside) variables: `ht.ndflux_u/_d`, `ht.ncflux_u/_d`, `ht.ntflux_u/_d`, `ht.nteflux_u/_d`, `ht.nthflux_u/_d`.

Line/point: `ht.Qltot` (W/m), `ht.Qptot` (W).

Other predefined: `ht.Tref` (reference temperature), `ht.alpha` (damage indicator), `ht.alphanecr`, `ht.theta_d`, `ht.theta_d_sm`, `ht.T_dp` (dew point), `ht.T_eq` (equivalent temp), `ht.psat` (saturation pressure), `ht.phi` (relative humidity), `ht.Lv` (latent heat of evaporation); `ht.kxx/kyy/kzz` (anisotropic conductivity), `ht.kmean`, `ht.alphaTdxx/…`, `ht.alphaTdMean` (thermal diffusivity). All flux/source variables except `turbflux`/`Qptot` also exist with `_material` suffix (evaluated in material frame), e.g. `ht.ndflux_material`.

Thin structures: flux on a Thin Layer is NOT in `ht.ntfluxInt`; use local `ht.sls1.ntfluxInt` (sls1 = Thin Layer tag).

Model inputs (Global Definitions → Default Model Inputs): `minput.T` (293.15 K), `minput.pA` (1 atm), `minput.u`, `minput.Tempref` (293.15 K) — selectable as "Common model input" in HT feature Model Input sections.

Moisture Transport variables (prefix `mt`): `mt.phi` (RH), `mt.cv`, `mt.cl`, `mt.cw` (vapor/liquid/total concentration), `mt.ca`, `mt.csat`, `mt.psat`, `mt.pv`, `mt.wc_l`, `mt.wc_v`, `mt.wcVar`, `mt.omega_v`, `mt.omega_moist`, `mt.xvap` (humidity ratio), `mt.Lv`, `mt.Xa`, `mt.Xv`, `mt.rhoa`, `mt.rhov`, `mt.rho_moist`; global `mt.dwcInt`, `mt.ntfluxInt`, `mt.GInt`, `mt.massBalance`.

---

## 2. CFD Module — Single-Phase Flow (tag `spf`)

### 2.1 Interface table (Table 3-1 of CFD Users Guide)

All single-phase flow interfaces use the same **Name `spf`** and differ only in default settings (compressibility, turbulence model, Stokes flow). Type strings for `physics().create()`:

| Interface (UI) | Type string | Turbulence |
|---|---|---|
| Creeping Flow (Stokes) | `CreepingFlow` | none (neglects inertial term) |
| Laminar Flow | `LaminarFlow` | none |
| Turbulent Flow, Algebraic yPlus | `TurbulentFlowAlgebraicYplus` | RANS-EVM |
| Turbulent Flow, L-VEL | `TurbulentFlowLVEL` | RANS-EVM |
| Turbulent Flow, k-ε | `TurbulentFlowkeps` | RANS-EVM |
| Turbulent Flow, Realizable k-ε | `TurbulentFlowRealizablekeps` | RANS-EVM |
| Turbulent Flow, k-ω | `TurbulentFlowkomega` | RANS-EVM |
| Turbulent Flow, SST | `TurbulentFlowSST` | RANS-EVM |
| Turbulent Flow, Low Re k-ε | `TurbulentFlowlowRekeps` | RANS-EVM |
| Turbulent Flow, Spalart–Allmaras | `TurbulentFlowSpalartAllmaras` | RANS-EVM |
| Turbulent Flow, v2-f | `TurbulentFlowv2f` | RANS-EVM |
| Turbulent Flow, Wilcox R-ω | `TurbulentFlowWilcoxRomega` | RANS-RSM |
| Turbulent Flow, SSG-LRR | `TurbulentFlowSSGLRR` | RANS-RSM |
| Turbulent Flow, Elliptic Blending R-ε | `TurbulentFlowEllipticBlendingRepsilon` | RANS-RSM |
| LES RBVM / RBVMWV / Smagorinsky | `LESRBVM` / `LESRBVMWV` / `LESSmagorinsky` | LES |
| DES RBVM, Spalart–Allmaras (and RBVMWV, Smagorinsky variants) | `DESRBVM` / `DESRBVMWV` / `DESSmagorinsky` | DES |
| Rotating Machinery, Laminar Flow (and Turbulent Flow variants) | `RotatingMachineryLaminarFlow` etc. | see Table 3-1 |

Changing `TurbulenceModelType` (None / RANS-EVM / RANS-RSM / LES / DES) and `TurbulenceModel` on the Laminar Flow interface relabels it (e.g. k-ε → "Turbulent Flow, k-ε").

### 2.2 Laminar Flow interface settings (`LaminarFlow`)

- Physical Model: `Compressibility` = Incompressible flow (default) / Weakly compressible flow / Compressible flow (Ma<0.3); `SwirlFlow` (2D axisym); `NeglectInertialTerm` (Stokes); `EnablePorousMediaDomains`; `PorousTreatmentOfNoSlip` (Standard no slip / Porous slip); `IncludeGravity` (+ `UseReducedPressure`); `RotatingFrame`; `IncludeBuoyancyInducedTurbulence`; `UseShallowChannelApproximation` (dz channel thickness, 2D)
- Reference values: `ReferencePressureLevel` pref (gauge vs absolute pA = p + pref), `ReferenceTemperature` (293.15 K), `ReferencePosition`
- Turbulence section: `TurbulenceModelType`, `TurbulenceModel`, `WallTreatment` (Wall functions / Low Re / Automatic), wall roughness
- Dependent variables: Velocity field **u** (u,v,w) + Pressure **p** (default P2+P1; P1+P1 for turbulent); turbulence variables per model (k, ep, om, G, uu…vw, zeta, alpha, v0, yPlus, uPlus)
- Default nodes: `FluidProperties`, `Wall` (No Slip), `init` (Initial Values)
- Non-Newtonian: Power law, Carreau, Bingham–Papanastasiou, Herschel–Bulkley–Papanastasiou, Casson–Papanastasiou (set on FluidProperties)

### 2.3 Domain features (dim = 2)

| Node (UI) | Feature type string | Tag | Key properties |
|---|---|---|---|
| Fluid Properties | `FluidProperties` | `fp*` | `Density` ρ, `DynamicViscosity` μ, `NonNewtonianModel` (off/from material/Power law/Carreau/…); `Thermodynamics` for compressible (IdealGas etc.) |
| Volume Force | `VolumeForce` | `vf*` | `VolumeForce` F (N/m³); several nodes sum |
| Initial Values | `init` | `init*` | `VelocityField` u, `Pressure` p; turbulence fields (k, ep, om, G, uu…vw, zeta, alpha, v0, yPlus, uPlus) |
| Gravity | `Gravity` | `grav*` | g (default 9.81 m/s², −z) |
| Rotating Frame | `RotatingFrame` (feature) | — | angular velocity ω, axis; Coriolis/centrifugal/Euler forces |
| Mass Source | `MassSource` | `ms*` | Qm (kg/m³/s) |
| Fluid and Matrix Properties (porous) | `FluidAndMatrixProperties` | `fmp*` | porosity εp, permeability κ; with `ForchheimerDrag` subnode |
| Moving Mesh | (Moving Mesh interface) | — | |

### 2.4 Boundary conditions (dim = 1)

| Node (UI) | Feature type string | Tag | Options / equation |
|---|---|---|---|
| Wall | `Wall` | `wall*` | `BoundaryCondition`: **NoSlip** (default; u = uw; wall roughness: `ApplyWallRoughness` → Sand roughness kseq or Generic roughness ks, Cs), **Slip** (u·n = 0, no penetration), **SlipVelocity** (tangential moving wall Uw; sliding wall), **LeakingWall** (with velocity), **NavierSlip** (slip length Ls). `WallTreatment` per turbulence model (wall functions: rough walls; Low Re: resolved). Constraint: Automatic / Pointwise / Nitsche / Weak |
| Inlet | `InletBoundary` | `inl*` | `BoundaryCondition`: **Velocity** (`NormalInflowVelocity` U0: u = −nU0, or `VelocityField` u0; `FlowDirection` Normal/User defined du; synthetic turbulence for LES/DES), **FullyDevelopedFlow** (`AverageVelocity` Uav / `FlowRate` V0 / `AveragePressure` Pav), **MassFlow** (`MassFlowRate` m / `PointwiseMassFlux` Mf / `StandardFlowRate` Qsv (SEMI E12, Vm or Pst,Tst) / `StandardFlowRateSCCM` Qsccm; channel thickness dbc in 2D), **Pressure** (static p0 / total p0, `Average`, `SuppressBackflow`) |
| Outlet | `OutletBoundary` | `out*` | `BoundaryCondition`: **Pressure** (p0 static/total, `SuppressBackflow` default on, `NormalFlow`), **Velocity**, **FullyDevelopedFlow** (Uav / V0 (+Dz) / Pav), **MassFlow**. Pressure outlet is the usual choice paired with velocity inlet |
| Symmetry | `Symmetry` | `sym*` | u·n = 0 + vanishing shear stress (Dirichlet + Neumann) |
| Open Boundary | `OpenBoundary` | `open*` | `BoundaryCondition`: **NormalStress** (f0, p≈f0) / **NoViscousStress** (σ·n = 0; must combine with pressure constraints) |
| Boundary Stress | `BoundaryStress` | `bs*` | prescribed stress F on boundary |
| Interior Wall | `InteriorWallBC` | `iwbc*` | thin wall / interior obstacles |
| Periodic Flow Condition | `PeriodicFlowCondition` | `pfc*` | source/destination pairs; `FlowCondition` (incompressible): `PressureDifference` psrc−pdst or `MassFlow` ṁ; velocity auto-transformed for non-parallel boundaries; `DestinationSelection` subnode |
| Screen | `Screen` | `sc*` | pressure drop across screen (flow coefficient) |
| Fan | `ExtFan` (turbulent) / `Fan` | `fan*` | `FlowDirection` Inlet/Outlet; `InputPressure` pinput / `ExitPressure` pexit; `StaticPressureCurve` (Linear pnf, V0,fd / Data / User defined; uses phys_id.V0 = spf.V0) |
| Interior Fan | `InteriorFan` | `ifan*` | same on interior boundaries |
| Grille | `Grille` | `grille*` | pressure drop: Quadratic loss qlc / Grille type (Wire gauze, Square mesh, Perforated plate, σs) / Loss coefficient K: Δp = 0.5Kρ(u·n)² |
| Vacuum Pump | `VacuumPump` | `vp*` | pump curve (data interpolation Linear/Piecewise cubic/Cubic spline) |
| Porous Interface | `PorousInterface` | — | porosity jump εp; Continuity conditions: Velocity and stress / Velocity and porosity-corrected stress (default) / with loss (Borda–Carnot, vena contracta) |
| Flow Continuity | `Continuity` | `cont*` | continuity across matching pairs; Wall as fallback BC |
| Pressure Point Constraint | `PressurePointConstraint` | `prpc*` | p0 at a point (gauge vs absolute; hydrostatic compensation) |
| Pointwise Constraint | `PointwiseConstraint` | `constr*` | general point constraint |
| Axial Symmetry | `AxialSymmetry` | `axi*` | auto-added on r=0 in 2D axisym (ur = 0) |
| Free Surface | `FreeSurface` / `StationaryFreeSurface` | `fs*` / `sfs*` | with `ContactAngle` subnode (`cnta*`) |
| Point Mass Source / Line Mass Source | (PointSource / LineMassSource) | — | Q (kg/s) / Ql (kg/m·s) |
| Generate New Turbulence Model | `NewTurbulenceModel` | `nturb*` | advanced: user turbulence model |
| Weak Contribution | `WeakContribution` | `weak*` | generic weak terms |

Tips: specify velocity at inlet + pressure at outlet (not velocity at both) for well-posed problems. `SuppressBackflow` adjusts pressure locally to reduce inflow at outlets/inlets. Hydrostatic compensation: when `IncludeGravity` on and `UseReducedPressure` off, pressure inputs are automatically hydrostatic-compensated.

### 2.5 Expression reference (prefix `spf`)

Core fields/variables (theory: CFD Users Guide §General Single-Phase Flow Theory):
- `spf.u`, `spf.v`, `spf.w` — velocity components (m/s); `spf.p` — pressure (Pa; relative, pA = p + pref)
- `spf.U` / `spf.normU` — velocity magnitude |u|
- `spf.rho` — density (kg/m³); `spf.mu` / `spf.eta` — dynamic viscosity (Pa·s); `spf.nuf` — kinematic viscosity (m²/s)
- `spf.T` — temperature (nonisothermal); `spf.Cp` — heat capacity; `spf.k` — thermal conductivity
- `spf.sr` — shear rate γ̇ (1/s); `spf.gradU` — velocity gradient; `spf.gradp` — pressure gradient
- `spf.tau` / `spf.K` — viscous stress tensor; `spf.stress` — total stress
- `spf.F` — volume force; `spf.Q` — mass source (kg/m³/s); `spf.mf` — mass flux; `spf.V0` — volumetric flow rate (used e.g. in Fan static-pressure curve expressions `spf.V0`)
- `spf.nx`, `spf.ny`, `spf.nz` — boundary normal; `spf.tx…` — boundary tangent
- `spf.Re` — Reynolds number; `spf.Ma` — Mach number; `spf.dt` — (pseudo) time step
- `spf.utau` — friction velocity uτ; `spf.nutau` — wall shear stress τw; `spf.yPlus` — wall distance in viscous units; `spf.uPlus` — tangential velocity in viscous units; `spf.wallRes` — wall resolution estimate

Turbulence variables (present depending on model):
- `spf.k` — turbulent kinetic energy (m²/s²); `spf.ep` — dissipation rate ε (k-ε family; also `spf.epsilon`); `spf.om` — specific dissipation ω (k-ω, SST); `spf.G` — reciprocal wall distance
- `spf.muT` — turbulent (eddy) viscosity; `spf.nuT` — turbulent kinematic viscosity; `spf.kt` — turbulent thermal conductivity (HT coupling)
- RSM (Wilcox R-ω, SSG-LRR, Elliptic Blending R-ε): `spf.uu`, `spf.vv`, `spf.ww`, `spf.uv`, `spf.uw`, `spf.vw` — kinematic Reynolds stresses
- v2-f: `spf.zeta` (turbulent relative fluctuation), `spf.alpha` (elliptic blending function); SA: `spf.v0` (undamped turbulent kinematic viscosity); LES: filtered `spf.u`, `spf.p` (resolved fields)

Study compatibility: Stationary, Time Dependent, Frequency Domain (linearized Navier–Stokes `LinearizedNavierStokesFrequency`), Eigenfrequency.

---

## 3. Heat Transfer + Flow Multiphysics

### 3.1 Predefined multiphysics interfaces

| Interface (UI) | Constituent interfaces | Coupling |
|---|---|---|
| Conjugate Heat Transfer, Laminar Flow (Heat Transfer branch) | `HeatTransferInSolidsAndFluids` (ht) + `LaminarFlow` (spf) | Nonisothermal Flow |
| Conjugate Heat Transfer, Turbulent Flow (k-ε, SST, Low Re k-ε, …) | ht + `TurbulentFlow*` | Nonisothermal Flow (thermal wall functions) |
| Nonisothermal Flow, Laminar/Turbulent Flow (Fluid Flow branch) | `HeatTransferInFluids` (ht) + spf | Nonisothermal Flow |
| Heat Transfer with Surface-to-Surface Radiation | ht + `SurfaceToSurfaceRadiation` (rad) | Surface-to-Surface Radiation |
| Heat Transfer with Orbital Thermal Loads | ht + `OrbitalThermalLoads` (otl) | |
| Heat Transfer with Radiation in Participating Media / Absorbing–Scattering Media / Radiative Beam | ht + rpm/rasm/rbam | |
| Thermoelectric Effect | Electric Currents (ec) + Heat Transfer in Solids | Thermoelectric Effect (Peltier–Seebeck–Thomson + Joule) |
| Joule Heating / Laser Heating / Induction Heating / Microwave Heating | ec or mf or emw + ht | Electromagnetic Heating |
| Heat and Moisture Transport / Heat and Moisture Flow | ht + mt + flow | Heat and Moisture |

### 3.2 Multiphysics couplings (feature types in `comp.multiphysics()`)

Domain couplings: `ElectromagneticHeating` (ec/mf/emw + ht), `HeatAndMoisture` (ht + mt; latent heat Qevap), `HeatTransferWithRadiationInParticipatingMedia`, `HeatTransferWithRadiationInAbsorbingScatteringMedia`, `HeatTransferWithRadiativeBeamInAbsorbingMedia`, `MoistureFlow`, `NonisothermalFlow` (ht + spf; Boussinesq approximation when incompressible — density evaluated at reference temperature; thermal wall functions for turbulent flow), `ThermalExpansion` (ht + solid, Structural Mechanics), `ThermoelectricEffect`.

Global couplings: `ThermalConnectionLayeredShellSurfaces`, `ThermalConnectionNonlayeredShell` (ht ↔ htlsh continuity; Shared/Facing boundaries; Connection tolerance Δ = 0.5% shell thickness).

Nonisothermal Flow notes: heat transfer Fluid feature selects `Velocity field (spf)`; flow density can depend on T (weakly compressible) and p; buoyancy via Boussinesq; wall functions redistribute viscous dissipation into heat balance variables.

---

## 4. Quick-start recipe (mph)

```python
# Conjugate heat transfer: solid + fluid + laminar flow
model.component().create("comp1", True)
geom = model.component("comp1").geom().create("geom1", 3)
model.component("comp1").physics().create("ht", "HeatTransferInSolidsAndFluids", "geom1")
ht = model.component("comp1").physics("ht")
ht.create("solid1", "SolidHeatTransferModel", 2)          # Solid domain node
ht.create("fluid1", "FluidHeatTransferModel", 2)          # Fluid domain node
ht.create("temp1", "TemperatureBoundary", 1)              # T = T0 on boundary
ht.feature("temp1").set("T0", "293.15[K]")
ht.create("hf1", "HeatFluxBoundary", 1)                   # convective heat flux
ht.feature("hf1").set("FluxType", "ConvectiveHeatFlux")
ht.feature("hf1").set("HeatTransferCoefficient", "10[W/(m^2*K)]")
ht.feature("hf1").set("Tinf", "300[K]")                   # external temperature

spf = model.component("comp1").physics().create("spf", "LaminarFlow", "geom1")
spf.create("inl1", "InletBoundary", 1)                    # velocity inlet
spf.feature("inl1").set("BoundaryCondition", "Velocity")
spf.feature("inl1").set("U0", "0.01[m/s]")
spf.create("out1", "OutletBoundary", 1)                   # pressure outlet
spf.feature("out1").set("BoundaryCondition", "Pressure")

nitf = model.component("comp1").multiphysics().create("nitf1", "NonisothermalFlow")
nitf.selection().setAll(True)
nitf.set("FlowInterface", "spf"); nitf.set("HeatInterface", "ht")

model.study().create("std1")   # Stationary
```

Common boundary value property names (mph `set()`):
- Heat Flux: `FluxType` (`GeneralInwardHeatFlux`/`ConvectiveHeatFlux`/`HeatRate`/`NucleateBoilingHeatFlux`), `q0`, `HeatTransferCoefficient`, `Tinf` (external temperature), `HeatRate` P0
- Temperature: `T0`; Surface-to-Ambient: `Tamb` (or `AmbientTemperature`), `epsilon` (or `SurfaceEmissivity`)
- Inlet: `BoundaryCondition` (`Velocity`/`FullyDevelopedFlow`/`MassFlow`/`Pressure`), `U0`, `u0`, `p0`, `m`; Outlet: `BoundaryCondition` (`Pressure`/`Velocity`/`FullyDevelopedFlow`/`MassFlow`), `p0`; Wall: `BoundaryCondition` (`NoSlip`/`Slip`/`SlipVelocity`/`LeakingWall`/`NavierSlip`), `Uw`; Open Boundary: `BoundaryCondition` (`NormalStress`/`NoViscousStress`), `f0`; Periodic Flow: `FlowCondition`, `PressureDifference`, `MassFlow`
- Heat Source: `Q0` (general), `qs` (linear), `HeatRate` P0; Boundary Heat Source: `Qb`; Lumped Thermal System components prefixed `R*`, `C*`, `term*`

Property strings are version-sensitive; when a `set()` is rejected, inspect the feature's `getPropertyNames()` (mph) or check the feature description in Ch. 6 of the HT Users Guide / Ch. 3 of the CFD Users Guide.
