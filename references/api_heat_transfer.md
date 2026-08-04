# Heat Transfer Module — API Reference

Extracted from COMSOL 6.4 Heat Transfer Module documentation.

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

Thin structures: flux on a Thin Layer is NOT in `ht.ntfluxInt`; use local `ht.sls1.n