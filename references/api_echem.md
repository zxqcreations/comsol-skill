# Electrochemistry + Chemical Reaction Engineering — API Reference (cd, tcd, aqt, cet, tds, tcs, chem, re, npe, el, sr)

Sources:
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Electrochemistry_Module\ElectrochemistryModuleUsersGuide.pdf` (COMSOL 6.4, 512 pp)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Electrochemistry_Module\IntroductionToElectrochemistryModule.pdf` (50 pp)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Chemical_Reaction_Engineering_Module\ChemicalReactionEngineeringModuleUsersGuide.pdf` (570 pp)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Chemical_Reaction_Engineering_Module\IntroductionToChemicalReactionEngineeringModule.pdf` (128 pp)
- mph tags.json via `references/tags_physics.md` (exact feature type strings; only interfaces listed there are marked "verified")

Conventions (same as `api_acdc.md`):
- **Feature type string** = Java/model-tree node type passed to
  `physics.feature().create(tag, 'TypeString', dim)` (mph) / `create(tag, type, dim)` (Java).
  Case-sensitive CamelCase, no spaces.
- **dim** = geometric entity dimension: `2` = domains (3D) / boundaries (2D); `1` = boundaries (3D) / edges (2D) / points (1D); `0` = edges (3D) / points (2D). Feature type strings listed under "Domain/Boundary" below follow this.
- Default tags: `cd` (Primary/Secondary CD), `tcd` (Tertiary CD Nernst–Planck / Electroanalysis), `aqt` (Aqueous Electrolyte Transport), `cet` (Concentrated Electrolyte Transport), `tds` (Transport of Diluted Species), `tcs` (Transport of Concentrated Species), `chem` (Chemistry), `re` (Reaction Engineering), `npe` (Nernst–Planck Equations), `el` (Electrophoretic Transport), `sr` (Surface Reactions).
- Physics interface creation: `comp.physics().create('cd', 'SecondaryCurrentDistribution', 'geom1')` (3rd arg = geometry tag). Type strings marked *(tags.json)* are confirmed in tags_physics.md; others are from UG text — verify against tags.json before shipping code.
- 2D out-of-plane thickness `d` (default 1 m), 1D cross-section area `Ac` (default 1 m²) — set on the physics interface top node.
- `<name>.<var>` pattern for all variables; `<name>` = interface Name (default cd/tcd/tds/...). `xxx` = interface tag, `yy` = (Porous) Electrode Reaction node tag (e.g. `er1`).
- Dependent variables: cd → `phil` (electrolyte potential), `phis` (electric/electrode potential); tcd → species concentrations + `phil` + `phis`; tds → concentrations (default `c1`, `c2`, … renamed per species); tcs → mass fractions (default `w1`, `w2`, …); cet → `cet.phil` + `cet.y_XXX`; aqt → `aqt.phil` + species.
- Study compatibility (intro tables): all CD interfaces, tds, tcs, npe, el, aqt, cet: Stationary + Time Dependent; cd additionally Frequency Domain / Eigenfrequency + small-signal; tcd additionally Frequency Domain (AC impedance); re: Time Dependent (CSTR/Batch/Semibatch) and Stationary Plug Flow; Nernst–Planck–Poisson = tds+es combo (also small-signal analysis, frequency domain). CD interfaces support the `Current Distribution Initialization` study step (Primary or Secondary).

---

## 1. Physics Interfaces — Tags, Type Strings, Space Dimensions

| Interface | Type string | Tag | Space dims | Notes |
|---|---|---|---|---|
| Primary Current Distribution | `PrimaryCurrentDistribution` *(tags.json)* | `cd` | 3D, 2D, 2D ax., 1D | Ohm's law + charge balance; **neglects** activation overpotential (potential constraints at equilibrium potential) |
| Secondary Current Distribution | `SecondaryCurrentDistribution` *(tags.json)* | `cd` | same | same equations + activation overpotentials (Butler–Volmer/Tafel current-flux BCs) |
| Tertiary CD, Nernst–Planck | `TertiaryCurrentDistributionNernstPlanck` *(tags.json)* | `tcd` | same | NP species transport + 5 electrolyte charge-conservation models |
| Electroanalysis (wizard entry) | `TertiaryElectroanalysis` *(tags.json)* | `tcd` | | supporting electrolyte, no potential gradients, cyclic voltammetry |
| Aqueous Electrolyte Transport | (type not in tags.json) | `aqt` | 3D, 2D, 2D ax., 1D | NP + electroneutrality + water autoprotolysis + weak acid/base/ampholyte equilibria |
| Concentrated Electrolyte Transport | (type not in tags.json) | `cet` | | Onsager–Stefan–Maxwell concentrated solution theory; ≥1 cation + ≥1 anion |
| Transport of Diluted Species | `DilutedSpecies` *(tags.json)* | `tds` | all | dilute solutes; Fick diffusion + convection + migration |
| TDS in Porous Media | `DilutedSpeciesInPorousMedia` *(tags.json)* | `tds` | all | same interface, porous defaults (Porous Medium node added) |
| Transport of Concentrated Species | `ConcentratedSpecies` *(tags.json)* | `tcs` | all | mass fractions; Maxwell–Stefan / Mixture-averaged / Fick diffusion |
| Nernst–Planck Equations | (type not in tags.json; npe) | `npe` | all | charged species + electroneutrality; solves concentrations + V |
| Nernst–Planck–Poisson Equations | combo `tds`+`es` | `tds`+`es` | all | resolves double layer (nm scale); same eqs as tcd Poisson option |
| Electrophoretic Transport | `ElectrophoreticTransport` *(tags.json)* | `el` | | weak acids/bases/ampholytes; charge balance for potential |
| Chemistry | `Chemistry` *(tags.json)* | `chem` | all | reaction/kinetics + mixture property provider (no space eqs) |
| Reaction Engineering | `ReactionEng` *(tags.json)* | `re` | 0D | tank/PFR reactors; mass + energy balance |
| Surface Reactions | `SurfaceReactions` *(tags.json)* | `sr*` | all | surface species on boundaries (stationary only in 3D/2D/2D-ax.) |
| TDS in Fractures | (type not in tags.json; dsf) | `dsf` | 3D, 2D, 2D ax. | |

---

## 2. Primary and Secondary Current Distribution Interfaces (`cd`)

Both share the same type string `SecondaryCurrentDistribution`; the UI node has a
`Current Distribution Type` setting (Primary/Secondary) that converts between them.
Current Distribution Type governs electrode-reaction treatment:
- **Primary** → potential constraints (Dirichlet): φl = φs − Eeq on electrode–electrolyte interfaces (η = 0).
- **Secondary** → Butler-Volmer kinetics: i_loc = f(η).

### Butler-Volmer Equation

The fundamental electrode kinetics equation, used in all Secondary/Tertiary current distribution interfaces:

```
i_loc = i₀ [exp(αₐFη/(RT)) − exp(−αcFη/(RT))]
```

| Parameter | Symbol | mph Property | Unit | Description |
|-----------|--------|-------------|------|-------------|
| Exchange current density | i₀ | `i0` | A/m² | Baseline reaction rate at equilibrium |
| Anodic transfer coefficient | αₐ | `alpha_a` | 1 | Typically 0.3–0.7 |
| Cathodic transfer coefficient | αc | `alpha_c` | 1 | αₐ + αc = 1 for single-electron |
| Overpotential | η | — | V | η = φs − φl − Eeq |
| Equilibrium potential | Eeq | `Eeq` | V | Nernst equation or user-defined |
| Faraday constant | F | — | 96485 C/mol | Built-in constant |
| Gas constant | R | — | 8.314 J/(mol·K) | Built-in constant |
| Temperature | T | `T` | K | From physics or user-defined |

**Simplified forms**:
- **Tafel** (high |η|): i_loc = i₀ exp(αₐFη/(RT)) — anodic; i_loc = −i₀ exp(−αcFη/(RT)) — cathodic
- **Linear** (low |η| << RT/F ≈ 25.7 mV): i_loc = i₀Fη/(RT)

**mph API usage**:
```python
# Create electrode reaction with Butler-Volmer kinetics
er = electrode.feature().create('er1', 'ElectrodeReaction')
er.set('kinetics_type', 'ButlerVolmer')
er.set('i0_type', 'MassActionLaw')  # or 'UserDefined'
er.set('i0', '1[A/m^2]')            # Exchange current density
er.set('alpha_a', '0.5')             # Anodic transfer coefficient
er.set('alpha_c', '0.5')             # Cathodic transfer coefficient
er.set('Eeq_type', 'Nernst')         # or 'UserDefined'
er.set('Eeq_ref', 'E0_formal')       # Formal potential
```

**Mass-action-law i₀** (for [Fe(CN)₆]³⁻ + e⁻ ⇌ [Fe(CN)₆]⁴⁻):
```
i₀ = F·k⁰·c_ox^(αc)·c_red^(αₐ)
```
Properties: `k0` (standard rate constant, m/s), stoichiometric coefficients (`stoich_<species>`)
- **Secondary** → current-flux conditions (Neumann): n·il = Σm iloc,m and n·is = −Σm iloc,m.

Top-node settings: Label/Name (default `cd`), Domain Selection, Out-of-plane Thickness d (2D) / Cross-sectional Area Ac (1D), `Physics vs. Materials Reference Electrode Potential` (scales Eeq/i0 between physics scale and materials node), Discretization (Linear default, Quadratic recommended for porous electrodes), dependent variables phil + phis.

### 2.1 Domain features (dim=2)

| Node (UI) | Feature type string | Key properties |
|---|---|---|
| Electrolyte | `Electrolyte` (sub-tag `ice*`) | `ElectrolyteConductivity` σl (S/m, default From material); current i = −σl∇φl |
| Porous Electrode | `PorousElectrode` (tcd: `PorousElectrodeNernstPlanck`-style domain node) | charge balances for electrode + pore electrolyte; `ElectrodeConductivity` σs, `ElectrolyteConductivity`, `EffectiveConductivityCorrection` (None/Bruggeman/Tortuosity), `ElectrodeVolumeFraction`; subnodes: `PorousElectrodeReaction` (`per*`), `PorousMatrixDoubleLayerCapacitance` |
| Initial Values | `init` (`InitialValues`) | phil, phis initial values (good guess: phis from BCs; phil ≈ −Eeq of grounded electrode) |
| Periodic Condition | `PeriodicCondition` | applies to electrolyte and/or electrode phase; `PotentialDifference` offset |
| Thin Electrolyte Layer | `ThinElectrolyteLayer` | resistive/insulating sheet on interior boundary |
| Edge Electrode (1D/edges) | `EdgeElectrode` | with `Ohm'sLaw` electric potential model; current sources `ElectrodeCurrent`/`ElectrolyteCurrent` |
| Line/Point/Symmetry-axis current sources | `ElectrodeLineCurrentSource`, `ElectrolyteLineCurrentSource`, `ElectrodePointCurrentSource`, `ElectrolytePointCurrentSource`, `ElectrodeSymmetryAxisCurrentSource`, `ElectrolyteSymmetryAxisCurrentSource` | source strength q (A) |

### 2.2 Boundary / edge / point features (shared across cd and tcd)

| Node (UI) | Feature type string | dim | Notes |
|---|---|---|---|
| Insulation (default exterior) | `Insulation` (`ins*`) | 1 | n·ik = 0, k = l, s |
| Symmetry | `Symmetry` (`sym*`) | 1 | = Insulation in cd; in tcd: no-flux of species molar flux |
| Electrode Surface | `ElectrodeSurface` (`es*`) | 1 (outer bnd to electrolyte) | electrode not in geometry; sections: Adsorbing–Desorbing Species (Density of sites Γs, site occupancy σs), Film Resistance (Rfilm Ω·m² or Thickness+conductivity), Harmonic Perturbation, Electrode Phase Potential Condition (`Electric potential`, `Electrode potential`, `Total current`, `Average current density`, `External short`, `Load Cycle`, `Cyclic voltammetry`; `Counter electrode` electroanalysis-only), Equilibrium Potential Handling, Constraint Settings |
| Internal Electrode Surface | `InternalElectrodeSurface` | 1 (interior, electrode|electrolyte domains) | |
| Perforated Electrode Surface | `PerforatedElectrodeSurface` | 1 (interior) | thin highly conductive mesh electrode |
| Thin Electrode Surface | `ThinElectrodeSurface` (`tes*`) | 1 (interior) | infinitely thin electrode; `Side` = Both/Up/Down; phil becomes slit variable (u/d suffixes on up/down side) |
| Electrolyte Potential | `ElectrolytePotential` (`eip*`) | 1, 0 | φl = φl,bnd; add `HarmonicPerturbation` subnode |
| Electrolyte Current Density | `ElectrolyteCurrentDensity` | 1 | set n·il |
| Electrolyte Current | `ElectrolyteCurrent` (`ic*`) | 1 | total current/avg current density w/ global DOF |
| Electrode (tcd) | `Electrode` (`ece*`) | 2 | current conductor domain node |
| Electric Ground | `ElectricGround` (`egnd*`) | 1 | φs = 0; optional Contact resistance Rc |
| Electric Potential | `ElectricPotential` | 1 | φs = φs,bnd; optional Rc |
| Electrode Current Density | `ElectrodeCurrentDensity` | 1 | n·is prescribed (uneven distribution in 2D/3D possible) |
| Electrode Current | `ElectrodeCurrent` (`ec*`) | 1 | total current; boundary potential solved for; Rc option |
| Electrode Power | `ElectrodePower` | 1 | power drawn/inserted |
| Electrode Potential | `ElectrodePotential` | 1 | φs vs `Electric Reference Potential` / `Reference Electrode` |
| External Short | `ExternalShort` | 1 | connects two electrodes over resistance R |
| Reference Electrode (point) | `ReferenceElectrode` | 0 | global reference potential (point in electrolyte) |
| Electric Reference Potential (point) | `ElectricReferencePotential` | 0 | global reference potential (point in electrode) |
| Load Cycle (+ Current/Voltage/Rest/Subloop children) | `LoadCycle` | 1 | galvanostatic/potentiostatic cycling with events |
| Electrode–Electrolyte Boundary Interface | `ElectrodeElectrolyteBoundaryInterface` | 1 (outer bnd to electrode, advanced) | electrolyte not in geometry; `BoundaryCondition` = Electrolyte potential / Total current / Avg current density |

---

## 3. Tertiary Current Distribution, Nernst–Planck Interface (`tcd`)

Solves NP species transport + electrode Ohm's law; dependent variables = species concentrations (one per species), phil, phis.

### 3.1 Electrolyte Charge Conservation (top-node setting)

Five options (set on `ElectrolyteChargeConservation`):
1. `Electroneutrality` — Σ zi ci = 0; one species eliminated (`From electroneutrality` list; choose high-concentration inert ion for stability).
2. `Water-based with electroneutrality` — adds water auto-ionization equilibrium; automatically adds `tcd.cH` (proton) and `tcd.cOH` (hydroxide) variables — do NOT add them under Dependent Variables. Initial pH set via other ions' initial concentrations.
3. `Supporting electrolyte` — constant-composition charge carrier; electrolyte potential only, no species mass balances (σl input).
4. `Electroanalysis (no potential gradients)` — sets phil = 0 (not a dependent variable), migration neglected; cyclic voltammetry support; requires large excess supporting electrolyte.
5. `Poisson` — NP + Poisson equation; resolves charge separation within ~nm of electrode (double layer must be meshed).

Other top-node settings: `Convection` checkbox (velocity field input), Material Balance Form (Nonconservative default / Conservative for compressible), stabilization (Streamline diffusion + Crosswind diffusion default; crosswind type Do Carmo and Galeão default or Codina, glim default `0.1[mol/m^3]/tcd.helem`), discretization (linear concentrations recommended under convection).

### 3.2 Electrolyte node (tcd)

Domain node; key settings:
- Species: added as subnodes/table; per species: `Diffusion coefficient` Di (m²/s), `Mobility` um,i (s·mol/kg; default from Nernst–Einstein um = Di/(RgT)... relation using Temperature model input), `Charge number` zc (dimensionless, signed).
- `Convection` section: velocity field u (feature input, e.g. from spf).
- Supporting electrolyte only: `Electrolyte conductivity` σl.
- Water-based only: `Water Self-ionization` section (Built-in T-dependent or user constant).
- Dependent variables get names `<name>.c<species>` (e.g. `tcd.cH`, `tcd.cOH` for the water-based auto-generated pair).

### 3.3 tcd feature list (tags.json, complete)

Domain: `Electrolyte` (ice*), `PorousElectrodeNernstPlanck` (porous* → subnodes `PorousElectrodeReaction` per*, `PorousMatrixDoubleLayerCapacitance`), `Separator` (sep* → `NonFaradaicReactions` nfr*), `IonExchangeMembrane` (iem*), `Reactions` (reac*), `init`.
Boundary/edge/point: `AxialSymmetry` (axi*), `Concentration` (conc*), `ElectricInsulation` (ein*), `ElectrolytePotential` (eip*), `ElectrolytePotentialPoint` (eip*), `EquilibriumReaction` (eqreac*), `GlobalConstraint` (gconstr*), `Inflow` (in*), `NoFlux` (nflx*), `Outflow` (out*), `PeriodicCondition` (pc*), `SurfaceChargeDensity` (sfcd*), plus shared cd features (§2.2).
Porous/electrode subnodes: `ElectrodeSurface` (es* → `ElectrodeReaction` er*), `HighlyConductivePorousElectrode` (hcpce* → `PorousElectrodeReaction` per*).

Notable node specifics:
- **Porous Electrode** (tcd): charge balances for electrode + pore electrolyte + species mass balances; effective transport corrections (Bruggeman/Tortuosity, electrode volume fraction); subnode Porous Electrode Reaction with `ActiveSpecificSurfaceArea` av (default 1e6 1/m; Particle-based area option).
- **Separator**: electronically insulating porous matrix; porosity/tortuosity corrections for Di and σl.
- **Ion-Exchange Membrane**: fixed space charge in electroneutrality (negative → cation-selective); optional Donnan boundary conditions on interior boundaries (not for Poisson); `Add Donnan shift to initial values`.
- **Ion-Exchange Membrane Boundary**: flux-continuous exterior boundary with potential shift (Donnan or user defined).
- **Reactions** (tcd): nonelectrochemical reactions; `Reacting Volume` = Total volume or Pore volume (multiplied by εl).
- **Thin Electrolyte Layer**: Insulating / Resistive (supporting electrolyte only) / Ion-exchange membrane.

---

## 4. Electrode Reaction — Kinetics Reference (cd and tcd)

Node: `ElectrodeReaction` (er*), parent = Electrode Surface / Internal Electrode Surface / Perforated / Thin Electrode Surface; `EdgeElectrodeReaction` (er*) for edges; `PorousElectrodeReaction` (per*) for porous electrodes (av multiplies iloc into domain source). Add multiple nodes for multiple reactions (mixed-potential problems).

### 4.1 Equilibrium Potential (Eeq, V)
- `From material` (materials node) / `Nernst Equation` / `User defined`.
- Nernst Equation in cd: concentration dependence from `Reduced species expression` CR and `Oxidized species expression` CO (dimensionless, CR/CO = 1 at reference state). In tcd: from `Stoichiometric Coefficients` + `Reference Concentrations` sections (Eeq = Eeq,ref at reference state); enables thermodynamically consistent i0 via `From Nernst Equation` / `Mass action law` / `Lumped multistep` (anodic/cathodic reaction orders or generic exponentials).
- Nernst Equation also enables `Linearize concentration dependence for low concentrations` (clim, mol/m³) for convergence.

### 4.2 Electrode Kinetics — Local current density iloc (A/m²)
iloc depends on overpotential η = φs − φl − Eeq. Input: `From material` / `From kinetics expression` / `User defined` (iloc,expr). Exchange current density i0 (A/m²); optional `Limiting Current Density` ilim.
Available expression types (Electrode Kinetics list):
1. **Butler–Volmer** — `iloc = i0 [ exp(αa F η/RT) − exp(−αc F η/RT) ]`; parameters Anodic transfer coefficient αa, Cathodic transfer coefficient αc. When i0 from Nernst Equation / Mass action law, αc is computed automatically (αa + αc = n).
2. **Linearized Butler–Volmer** — valid |η| << 25 mV; `iloc = i0 (αa+αc) F η/RT`; use for troubleshooting convergence.
3. **Anodic Tafel Equation** — anodic term only (η >> 100 mV); `Anodic Tafel slope` Αa (V; tenfold current per Αa).
4. **Cathodic Tafel Equation** — cathodic term only (η << −100 mV); `Cathodic Tafel slope` Αc (V, negative).
5. **Concentration Dependent Kinetics** — CO/CR expressions (not with Nernst Equation; prefer Nernst+BV instead).
6. **Fast Irreversible Electrode Reaction** — transport-limited: sets rate-limiting species concentration to 0 at boundary, balances fluxes with currents per stoichiometry.
7. **Thermodynamic Equilibrium (Primary Condition)** — imposes η = 0 via constraint (mixes primary/secondary on different electrodes; not for multiple reactions on one electrode in cd).

### 4.3 Stoichiometric Coefficients
`Number of participating electrons` n (positive); stoichiometric coefficients νi per species in generic reaction Σνox Sox + n e⁻ ⇌ Σνred Sred — positive (νred) for reduced species, negative (νox) for oxidized. If a species is eliminated via electroneutrality/water autoionization, its coefficient is set implicitly. Heat of Reaction section: `Temperature derivative` dEeq/dT (V/K) or `Thermoneutral voltage` Etherm (V).

### 4.4 Double-Layer Capacitance
`DoubleLayerCapacitance` (dlc*) subnode — nonfaradaic current ∝ Cdl dφ/dt; `Electrical double-layer capacitance` Cdl (F/m²). Not in Primary cd. Optional stoichiometric coefficients for double-layer mass exchange (negative for ions entering double layer during cathodic polarization).

### 4.5 Adsorbing–Desorbing Species (on Electrode Surface)
Table of species + site occupancy number; surface coverage variables `<name>.theta_<es_tag>_<species>` and free-site fraction `<name>.thetafree_<es_tag>`; `Density of sites` Γs sets the surface mass balance. Initial values via `InitialValuesForAdsorbingDesorbingSpecies` subnode.

---

## 5. Aqueous Electrolyte Transport (`aqt`) and Concentrated Electrolyte Transport (`cet`)

### 5.1 aqt
Nernst–Planck + electroneutrality + water autoprotolysis + dissociation equilibria (weak acids/bases/ampholytes). Transport mechanisms: diffusion + migration always; convection opt-in (default off); `Solve for electrolyte phase potential` checkbox (else phil fixed, default 0). Species defined via species nodes: `Fully Dissociated Species`, `Uncharged Species`, `Weak Acid`, `Weak Base`, `Ampholyte`, `Carbonic Acid`, `Complex Species` (each with dissociation equilibrium constants; e.g. WeakAcid Kw/Ka/... parameters). Domain nodes: `HighlyConductivePorousElectrode` (hcpce*), `Porous Electrode`, `Separator`; boundary nodes: `ElectrodeSurface` (+ElectrodeReaction), `Electrode Reaction`, `Reaction`, `Potential` (phil), `Species Source`, `No Flux`, etc.

### 5.2 cet
Onsager–Stefan–Maxwell (binary interactions) concentrated solution theory. `Species` section: Cations / Anions / Neutral species tables (name + molar mass; charge for ions; ≥1 cation + ≥1 anion). n species → n−1 electrolyte components → n−2 dependent variables: `cet.phil` (electrolyte potential) + `cet.y_XXX` (neutral electrolyte component fractions; names auto-generated, e.g. species Fe(+2), OH(−1), H2O → components `Fe_OH_2`, `H2O`). `Electrolyte component from molar-fraction constraint` selects eliminated component. Default domain nodes: `Electrolyte`, `Reference Electrode`.

---

## 6. Chemical Species Transport Interfaces

### 6.1 Transport of Diluted Species (`tds`)

Top-node settings: Transport Mechanisms (diffusion always; `Convection` checkbox default on; `Migration in electric field` checkbox → adds migration term −zum,i F ci ∇φ and enables `Species Properties` node); `Mass transport in porous media` checkbox (adds Porous Medium / Unsaturated Porous Medium / Porous Electrode Coupling / Volatilization / Species Source); Material Balance Form; stabilization (Streamline + Crosswind Do Carmo-Galeão/Codina default glim `0.1[mol/m^3]/tds.helem`); `Compute boundary fluxes` (default on → accurate flux vars `ndflux_<c>` normal diffusive flux, `ntflux_<c>` normal total flux; smoothing option).

Species: dependent variables in `Dependent Variables` section — default names `c1`, `c2`, …; renamed per species (then flux vars become `ndflux_<name>`, `ntflux_<name>`).

Feature list (tags.json, complete):
- Domain: `ConvectionDiffusionMigration` (cdm*; default; subnode `TurbulentMixing` tm*), `Reactions` (reac*), `SpeciesProperties` (when migration active; `Charge` zc signed, `SpeciesActivity` Debye–Hückel/User defined), `MassBasedConcentrations`, `PorousMedium` (porous* → `FluidPorousMedium` fluid*, `PorousMatrixPorousMedium` pm*), `ReactivePelletBed` (rpb*), `UnsaturatedPorousMedium` (usporous*), `Adsorption`, `Dispersion`, `Fluid`, `Solid`, `Liquid`, `Gas`, `HygroscopicSwelling`, `init`.
- Boundary/pair: `Concentration` (conc*), `FluxBoundary` (fl*), `Inflow` (in*), `NoFlux` (nflx*), `Outflow` (out*), `Symmetry` (sym*), `FluxDiscontinuity`, `PartitionCondition` (pac*), `PeriodicCondition` (pc*), `SurfaceEquilibriumReaction` (seqreac*), `SurfaceReactionsFlux` (srf*), `ThinImpermeableBarrier` (tib*), `MassSourceLine` (lms*), `ElectrodeElectrolyteInterfaceCoupling` (eeic* → `BoundaryReactionCoefficients` rc*), `Continuity` (cont* → NoFlux), `AxialSymmetry` (axi*).

Boundary-condition equations (with migration): No Flux n·(−D∇c − zumFc∇φ) = 0 (optionally + uc); Inflow c = c0 (Concentration constraint or Flux (Danckwerts) total-flux form); Outflow n·(−D∇c) = 0; Flux n·(−D∇c − zumFc∇φ) = J0 (positive inward; `External convection` variant J0 = kc(cb − c)); Flux Discontinuity n·(Ju+c − Jd+c) = N0; Concentration per-species checkboxes.

### 6.2 Transport of Concentrated Species (`tcs`)

Solves mass fractions (default `w1`, `w2`, …), ≥2 species; one species from mass constraint Σωi = 1 (`From mass constraint` list — use highest-concentration species). Equation (nonconservative): ρ ∂ωi/∂t + ρ u·∇ωi = −∇·ji + Ri.
- Diffusion models: `Maxwell–Stefan` (multicomponent diffusivities D̃ik + diffusional driving force dk, thermal diffusion; most expensive), `Mixture-averaged` (mixture-averaged Di, robust), `Fick's law` (Fickian Di, recommended when multicomponent data unavailable). `Mixture diffusion correction` (zero net diffusive flux) + `Diffusion flux type` (mole-fraction vs mass-fraction based) for approximate models.
- Migration: electric-field force in driving force gk = −(zkF/Mk)∇φ (added by `Migration in electric field` checkbox).
- `Regularization` (regularized mass fractions for property computation), `Pseudo time stepping` for stationary solves (CFL/PID).
- Fluid node (default domain node): Model Inputs Temperature T (user defined or ht) + Absolute pressure p (user defined or spf); `Mixture density` = Ideal gas (ρ = pM/RgT) or User defined; `Diffusivity` per diffusion model.
- Feature list (tags.json): `ConvectionDiffusionMigration` (cdm*), `ReactionSources` (reac*), `ReactionWithTurbulenceModel` (treac*), `TCSPorousMediaTransportProperties` (pmtcs* = Porous Medium), `SpeciesProperties`, `Fluid`, boundary: `Inflow` (in*), `MassFraction` (mf*), `NoFlux` (nflx*), `Outflow` (out*), `Flux`, `FluxDiscontinuity`, `OpenBoundary`, `Symmetry` (sym*), `EquilibriumReaction`, `SurfaceEquilibriumReaction`, `AxialSymmetry`, `init`. Porous variants: TCS in Porous Media / Porous Catalysts / Packed Beds (Pellets extra dimension) / Vapor / Moving Packed Beds.
- Species Properties node: `Molar mass` Mw (default 0.032 kg/mol = O2) and `Charge` zw (signed) when migration on.

### 6.3 Nernst–Planck Equations Interface (`npe`)

Flux Ni = −Di∇ci − zi um,i F ci ∇V + ci u; solves concentrations + electric potential V with electroneutrality (one species from `From electroneutrality`). Main domain node `Convection, Diffusion, and Migration` (settings: Temperature model input; Convection section with velocity field u (user defined or spf); Diffusion coefficients Di scalar/tensor; `Mobility` um,i default from Nernst–Einstein (user defined override); `Charge number` zi signed). `Species Properties` node: `Charge` zc + `Activity` (Debye–Hückel ion size a0 / User defined f). `Reactions` node: rate expressions Ri (mol/(m³·s)).
Boundary conditions (separate sets for concentrations and potential):
- Concentration: `Concentration` (ci = ci,0, not for electroneutrality species), `Flux` (n·(−D∇c − zumFc∇V) = J0; `Include` convection option; positive = inward), `NoFlux` (default), `Symmetry`, `Inflow` (all species, Concentration or Danckwerts), `Outflow` (n·(−D∇c) = 0), `FluxDiscontinuity` (interior), `OpenBoundary`.
- Potential: `Electric Insulation` (default; n·i = 0), `Electric Potential` (V = V0), `Current Density` (n·i = i0, inward positive), `Current Discontinuity` (interior).
- Edges/points: `Line Mass Source`, `Point Mass Source`.
Nernst–Planck–Poisson: multiphysics combo tds + es — same equations as tcd Poisson; double layer must be resolved in mesh (~tens of nm).

### 6.4 Electrophoretic Transport (`el`)

Species = weak acids/bases/ampholytes/proteins with individual equilibria; charge balance for electrolyte potential (current il = F Σ zi Ni; ∇·il = Ql). Solves phil (default variable `phil`) + species concentrations named `el.<species>`; boundary flux vars `<name>.nIl` (normal electrolyte current density), `<name>.ntflux_<species>`. Nodes: `Solvent` (sol*), `WeakAcid` (wa*), `WeakBase` (wb*), `Ampholyte` (amph*), `Protein` (prot*), `CarbonicAcid`, boundary: `ElectrolytePotential` (eip*), `ElectrolyteNormalCurrentDensity` (icd*), `Insulation` (ins*), `Concentration`, `Inflow`, `NoFlux`, `Outflow`, `init`.

### 6.5 Surface Reactions Interface (`sr`)

Boundary/edge interface for surface (adsorbed) species: `SurfaceProperties` (sp*; density of sites Γs, surface concentration units), `Reactions` (reac*; surface rate expressions), `NoFlux` (nflx*), `init`. ODE formulations for surface concentrations; bulk-species coupling via `SurfaceReactionsFlux` (srf*) in tds.

---

## 7. Chemistry (`chem`) and Reaction Engineering (`re`)

### 7.1 Chemistry interface (chem)

Generates kinetics + mixture property variables for space-dependent interfaces (no governing equations itself).
- Mixture Properties: `Type` = Diluted species (molar concentrations from tds) or Concentrated species (mass fractions from tcs); Phase; Thermodynamics coupling (to Global Definitions Thermodynamic System); Calculate Transport Properties (heat capacity, ratio of specific heats, thermal conductivity, dynamic viscosity; density + diffusivity always).
- Species Matching: `Species solved for` (select tds/tcs interface), Bulk species table (Molar concentration or Mass fraction or User defined value), Surface species (via Surface Reactions / Packed Bed / Porous Catalyst; `Density of sites` input when Electrode Reaction present), Solid (s), Aqueous (aq) species.
- Reaction node: Formula parsing ("A + B <=> C + D"; arrows `<=>` reversible, `=>` irreversible, `=` equilibrium), Balance button, Reaction Rate (Mass action law or User defined r with reaction orders; Arrhenius kf = Af (T/Tref)^nf exp(−Ef/RgT)), Equilibrium Settings (Keq0 = Π cprod/Π creact; Automatic = from Gibbs energy, Thermodynamics = coupled system), Reaction Thermodynamic Properties (enthalpy/entropy/heat source Qj = −rj Hj).
- **Electrode Reaction** (in chem; needs echem-family license): Formula as reduction with electron "e" and phase suffixes (aq)/(s)/(g)/(ads); Equilibrium potential from `Nernst Equation` (uses matched concentrations + reference concentrations; automatic reference state by phase: (aq) → 1 M, (g) → 1 atm via ideal gas, (s) → 1, (ads) → site density) or `Automatic` (from species enthalpies/entropies); kinetics: `User-defined`, `Butler–Volmer`, `Linearized Butler–Volmer` with exchange current density User defined or `Mass action law`; Heat of Reaction: Thermoneutral voltage Etherm = −ΔrH/(nF) (no Temperature derivative option). **Electrode Reaction Group**: group of electrode reactions; sum variables usable as input in CD-interface Electrode Reaction features.
- Nodes (tags.json): `SpeciesChem` (sch*), `ReactionChem` (rch*), `ReversibleReactionGroup` (rgr*), `SpeciesGroup` (sg_rgr* → `SpeciesThermodynamics` sthm*), plus electrode reaction features when enabled.
- Variables: `chem.Rsum_<species>` total reaction rate per species; kinetics/mixture-property variables named `<name>.<species>...` per Species nodes.

### 7.2 Reaction Engineering interface (re)

0D tank/PFR reactor balances. Reactor types: `Batch`, `Batch, constant volume` (default), `CSTR, constant mass/generic`, `CSTR, constant volume`, `Semibatch`, `Plug flow` — each with parameters (reactor volume Vr, volumetric production rate vp, volumetric outlet rate v, surface reaction area / area-to-volume ratio). Energy Balance: `Exclude` (isothermal; temperature input) or `Include` (temperature dependent variable; External heating/cooling Qext, W or W/m³ for plug flow). Mixture Properties: phase, density (Automatic: liquid ideal & incompressible ρ = 1/Σ(wi/ρi); gas ρ = Σ ci Mi; or Thermodynamics-coupled), reactor pressure (gas; ideal gas law or user defined), Species Matching to Thermodynamic System, Calculate Transport Properties (cp, k, μ, ρ transferred to space model), Equilibrium Species (each equilibrium reaction reduces solved species by one; `User defined equilibrium species` list; `Suppress negative concentrations`), Activity option, CHEMKIN import (Thermo → NASA coefficients; Transport → Lennard–Jones σ, ε/kb, dipole μD, thermal conductivity, diffusivity).
Study steps: Time Dependent for Batch/CSTR/Semibatch; `Stationary Plug Flow` for Plug flow (molar flow rates Fi in mol/s).
Nodes (tags.json): `ReactionChem` (rch*), `SpeciesChem` (sp*), `SpeciesInitialValue` (inits*), `ReversibleReactionGroup` (rgr*), `SpeciesGroup` (sg_rgr*), `AdditionalSourceFeature` (add*), `FeedStream` (feed*), `ReactionToMph` (sync* — the Generate Space-Dependent Model node), `ParameterEstimation` (est* → `Experiment` exp*).
- Reaction node: same formula parsing; Rate constants kf/kr with `Specify equilibrium constant` (kr = kf/Keq0) and Arrhenius option; units auto-derived from order (m³/mol)^(α−1)/s, surface species m^(3α+2β−2)/mol^(α+β−1)/s.
- Species node: Type = Bulk species (mol/m³, variable `c_<species>`), Surface species (mol/m², `csurf_<species>_surf`; "(ads)" suffix; site occupancy; density of sites Γs), Solvent (not solved for). Chemical Formula auto-derives molar mass + charge; Transport Expressions (LJ σ, ε/kb, μD, ki, Di); Thermodynamic Expressions (NASA 7-coefficient polynomials, Tlo/Tmid/Thi).
- Initial Values: initial concentrations (mol/m³), surface concentrations, initial volume Vr0, initial temperature T0; Equilibria: `Mass-preserving initialization` option.

---

## 8. Variable Reference (documented in UG)

### 8.1 Potential variables (Table 2-1; unit V)
| Variable | Description | Defined at |
|---|---|---|
| `phil` | Electrolyte phase potential | Electrolyte and Porous Electrode domains |
| `phis` | Electrode phase potential | Electrode and Porous Electrode domains |
| `xxx.phisext` | Electrode phase potential | Electrode Reaction boundaries to Electrolyte domains |
| `xxx.Eeq_yy` | Equilibrium potential | Electrode Reaction boundaries and Porous Electrode Reaction domains |
| `xxx.eta_yy` | Overpotential (η = φs − φl − Eeq) | Electrode Reaction boundaries |

### 8.2 Current density variables (Table 2-2)
| Variable | Unit | Description | Defined at |
|---|---|---|---|
| `xxx.nIl` | A/m² | Electrolyte current density, normal direction | Boundaries to Electrolyte / Porous Electrode |
| `xxx.nIs` | A/m² | Electrode current density, normal direction | Boundaries to Electrode / Porous Electrode |
| `xxx.iloc_yy` | A/m² | Local current density of electrode reaction | Electrode Reaction boundaries |
| `xxx.itot` | A/m² | Total interface current density (Σ all xxx.iloc_yy) | Electrode Reaction boundaries |
| `xxx.iv_yy` | A/m³ | Volumetric current density of a Porous Electrode Reaction | Porous Electrode domains |
| `xxx.ivtot` | A/m³ | Total volumetric current density (Σ all xxx.iv_yy) | Porous Electrode domains |
| `xxx.IlMag` | A/m² | Electrolyte current density magnitude (L2 norm) | Electrolyte domains |
| `xxx.IsMag` | A/m² | Electrode current density magnitude (L2 norm) | Electrode domains |

`xxx` = interface tag (cd/tcd/...), `yy` = reaction node tag (er1, per1, ...). Avoid IlMag/IsMag on boundaries — use nIl/nIs. Total cell current: integrate nIl/nIs (or iloc) over the electrode boundary (line integral 2D, surface integral 3D; 2D-axi: check `Compute integral in revolved geometry`).

### 8.3 Species / coverage / misc variables
- Species concentration: `<name>.c<species>` (tcd/tds style; tds default `c1`, `c2`; npe `c1`...; el `el.<species>`; cet `cet.y_XXX` component fractions; re bulk `c_<species>`, surface `csurf_<species>_surf`).
- Water-based tcd auto-adds `tcd.cH` (proton) and `tcd.cOH` (hydroxide).
- Adsorbing–desorbing: `<name>.theta_<es_tag>_<species>` (fractional surface coverage), `<name>.thetafree_<es_tag>` (free sites).
- Boundary flux (tds/npe, computed accurate fluxes): `ndflux_<c>` (normal diffusive flux), `ntflux_<c>` (normal total flux); smoothing option.
- Electrophoretic: `<name>.nIl` (normal electrolyte current density), `<name>.ntflux_<species>`.
- Chemistry: `chem.Rsum_<species>` total species reaction rate.
- LIB interfaces: `xxx.I_1C_cell` (C-rate current) when SOC defined in Cell Settings.
- Element size: `tds.helem`, `npe.helem`, `tcd.helem` (local element size used in default glim).
- Kinetics inputs: iloc (A/m²), i0 (A/m²), i0,ref, αa, αc, Eeq, η, ilim, CR, CO, clim, n (electrons), νi, Cdl, Rfilm, Γs, σs.

---

## 9. Governing Equations (Theory Summary)

- **Nernst–Planck flux** (per species i): Ni = −Di∇ci − zi um,i F ci ∇φl + ci u; current density il = F Σ zi Ni; mass balance ∂ci/∂t + ∇·Ni = Ri,tot. Conservative form ∂ci/∂t + ∇·(Ji + ci u) = Ri; porous: ∂(εi ci)/∂t + ∇·(Ji + ci u) = Ri (conservative) vs εi ∂ci/∂t + ∇·Ji + u·∇ci = Ri (nonconservative).
- **Primary/secondary**: il = −σl∇φl, σl = F² Σ zi² um,i ci (constant for cd); ∇·ik = Qk, ik = −σk∇φk (k = l, s). Porous: ∇·il = Σm Av,m iloc,m, ∇·is = −Σm Av,m iloc,m.
- **Tertiary + electroneutrality**: Σ zi ci = 0; il = F Σ zi [−Di∇ci − zi um,i F ci ∇φl]; ∇·il = Ql.
- **Butler–Volmer**: iloc,m = i0,m [ exp(αa,m F ηm/RT) − exp(−αc,m F ηm/RT) ], ηm = φs − φl − Eeq,m. Nernst-consistent i0: i0 = i0,ref (cR/cR,ref)^(αc/n) (cO/cO,ref)^(αa/n) (tcd form). Interface conditions: n·il = Σm iloc,m and n·is = −Σm iloc,m.
- **Faraday's law mass fluxes**: species molar flux at electrode Ni·n = Σm νi,m iloc,m/(n m F) (νi positive for products/reduced species in reduction-form reaction).
- **tds**: ∂ci/∂t + ∇·(−Di∇ci) + u·∇ci = Ri; with migration −zi um,i F ci ∇φ added to flux; no-flux n·(−D∇c − z um F c ∇φ) = 0.
- **tcs**: ρ ∂ωi/∂t + ρ u·∇ωi = −∇·ji + Ri; Maxwell–Stefan ji = ρωi Σk D̃ik dk − (Di^T/T)∇T; dk = ∇xk + (1/p)(xk − ωk)∇p + ρ Σl ωk ωl (gl − gk) with gk = −(zkF/Mk)∇φ for ions.
- **Surface concentrations (sr)**: ODEs on boundaries; surface mass balance with site density Γs, coverage θi, rates from Reactions node.

---

## 10. Multiphysics Coupling Nodes (echem UG ch. 7)

- `ElectrochemicalHeating` — reversible + irreversible heat from electrode reactions (couples to Heat Transfer; total overpotential calculation for concentration-dependent kinetics).
- `PotentialCoupling` — connects two cd/tcd interfaces (e.g. different potential scales/regions).
- `SpaceChargeDensityCoupling` — feeds electrolyte space charge into Electrostatics.
- `ElectrodeElectrolyteInterfaceCoupling` (eeic*) in tds — couples tds species fluxes to cd/tcd electrode reactions (subnode `BoundaryReactionCoefficients` rc*).
- `PorousElectrodeCoupling` (tds/tcs ↔ cd/tcd porous electrodes), `ElectrodeSurfaceCoupling` (tds ↔ Electrode Surface boundary), Reacting Flow multiphysics (spf+tds / spf+tcs), Nonisothermal Reacting Flow (spf+ht+tds/tcs).

---

## 11. Practical Notes

- Initial values matter for Butler–Volmer convergence: phis from cell-potential BCs; phil ≈ −Eeq of grounded electrode; at least one cation and one anion with positive nonzero initial concentration.
- Choose the electroneutrality-eliminated species (tcd/npe) as a high-concentration, relatively inert ion for numerical robustness; you cannot set flux/concentration BCs or initial values on the eliminated species.
- Use Primary CD only when activation losses << ohmic losses; add Porous Electrode to a Primary model only to later extend to charge-transfer resistance.
- tcd Electroneutrality assumes all major current-carrying ions are modeled; otherwise use Supporting Electrolyte.
- For 2D models, out-of-plane thickness d is used to compute total currents from current densities (per-boundary areas otherwise needed for Total current BCs).
- Linear elements recommended for cd by default; Quadratic for porous electrodes / 2D+ current distribution; avoid >Quadratic concentrations in convection-dominated tcd/tds.
