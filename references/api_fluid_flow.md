# Fluid Flow (CFD) Module — API Reference

Extracted from COMSOL 6.4 CFD Module documentation.

tfluxInt` (sls1 = Thin Layer tag).

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
