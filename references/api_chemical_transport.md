# Chemical Species Transport Module — Comprehensive API Reference

COMSOL 6.4 · mph Python API · Based on official Chemical Reaction Engineering Module Users Guide and tags.json

---

## 1. Physics Interfaces

The module spans two categories:

### 1.1 Chemical Species Transport Interfaces

| Interface | mph Tag | Default | Description |
|-----------|---------|---------|-------------|
| Transport of Diluted Species | `tds` | `tds` | Fickian diffusion + convection + migration for dilute solutions |
| Transport of Diluted Species in Porous Media | `tds` | `tds` | Same with porosity ε, tortuosity τ |
| Transport of Diluted Species in Porous Catalysts | `tds` | `tds` | Porous media + catalytic reactions |
| Transport of Concentrated Species | `tcs` | `tcs` | Maxwell-Stefan multicomponent diffusion |
| Nernst-Planck Equations | `npe` | `npe` | Electrolyte ion transport with electroneutrality |
| Electrokinetic Flow | `ek` | `ek` | Electroosmosis + electrophoresis |
| Reacting Flow in Porous Media | — | — | Transport + reaction in porous flow |
| Reacting Flow, Diluted Species | — | — | Transport + reaction with fluid flow |

### 1.2 Chemistry & Reaction Engineering Interfaces

| Interface | mph Tag | Default | Description |
|-----------|---------|---------|-------------|
| Chemistry | `chem` | `chem` | Define species, reactions, thermodynamics |
| Reaction Engineering | `re` | `re` | Ideal reactor models (batch, CSTR, PFR) |

### 1.3 Transport of Diluted Species (tds) — Default Nodes

| Default Node | mph Type | Purpose |
|-------------|---------|---------|
| Transport Properties | `TransportProperties` | Dᵢ, u (velocity field) |
| No Flux | `NoFlux` | n·Nᵢ = 0 (default BC) |
| Initial Values | `InitialValues` | cᵢ = cᵢ₀ |

**Governing equation**: ∂cᵢ/∂t + ∇·(−Dᵢ∇cᵢ) + u·∇cᵢ = Rᵢ

Where Dᵢ is the diffusion coefficient, u is convection velocity, Rᵢ is reaction source term.

**Available transport mechanisms** (each can be toggled on/off):

| Mechanism | Equation Term | When to Use |
|-----------|--------------|-------------|
| Diffusion | −Dᵢ∇cᵢ | Always (Fick's law) |
| Convection | u·∇cᵢ | Flow fields from CFD coupling |
| Migration | −zᵢuₘᵢFcᵢ∇V | Electrolytes with electric field |
| Turbulent mixing | −(D_T/Sc_T)∇cᵢ | Turbulent flow coupling |

---

## 2. Domain Features — Transport of Diluted Species

### 2.1 Transport Properties (default)

| Property | Symbol | Unit | Description |
|----------|--------|------|-------------|
| Diffusion coefficient | Dᵢ | m²/s | Per species; can be T/c-dependent |
| Velocity field | u | m/s | From Laminar/Turbulent Flow interface |
| Electric potential | V | V | From Electrostatics/Electric Currents |
| Temperature | T | K | For T-dependent Dᵢ |
| Porosity | ε | 1 | For porous media variant |
| Tortuosity | τ | 1 | D_eff = D·ε/τ |

### 2.2 Reactions

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Reactions | `Reactions` | Bulk volume reactions Rᵢ in domain |
| Volumetric Reaction Rate | — | User-defined rate expression |

### 2.3 Additional Domain Features

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Species Source/Sink | `Source` | External species source term |
| Dispersion | `Dispersion` | Dispersion tensor for porous media |
| Adsorption/Desorption | `Adsorption` | Surface adsorption equilibrium |
| Partition Coefficient | `Partition` | Interface partitioning (membrane) |

---

## 3. Boundary Conditions — Transport of Diluted Species

| BC | mph Type | Equation | Purpose |
|----|---------|----------|---------|
| Concentration | `Concentration` | cᵢ = c₀ | Fixed concentration |
| Flux | `Flux` | −n·Nᵢ = N₀ | Specified inward flux |
| No Flux | `NoFlux` | −n·Nᵢ = 0 | Insulation/symmetry (default) |
| Inflow | `Inflow` | cᵢ = c₀ᵢ (inflow), −n·Dᵢ∇cᵢ = 0 (outflow) | Open boundary with fluid flow |
| Outflow | `Outflow` | −n·Dᵢ∇cᵢ = 0 | Convection-dominated outlet |
| Symmetry | `Symmetry` | −n·Nᵢ = 0 | Symmetry plane |
| Thin Diffusion Barrier | `ThinDiffusionBarrier` | Interior BC with resistance | Membrane/permeable wall |
| Periodic Condition | `PeriodicCondition` | c_src = c_dst | Unit cell |
| Surface Reactions | — | −n·Nᵢ = R_surf | Catalytic surface reactions |

---

## 4. Transport of Concentrated Species (tcs)

Uses **Maxwell-Stefan** equations for multicomponent diffusion:

dₖ = −Σ xₖxⱼ(uₖ−uⱼ)/Đₖⱼ

**Key Differences from Diluted**:

| Aspect | Diluted (tds) | Concentrated (tcs) |
|--------|--------------|-------------------|
| Diffusion model | Fick's law (Dᵢ per species) | Maxwell-Stefan (Đₖⱼ per pair) |
| Solvent | Implicit (excess solvent) | All species explicit |
| Use case | Trace species in solvent | Gas mixtures, concentrated electrolytes |
| Computaion | Light (N equations) | Heavy (N(N−1)/2 pairs) |

---

## 5. Reaction Engineering Interface (re)

Ideal reactor models for kinetic studies:

| Reactor Type | Variables | Description |
|-------------|-----------|-------------|
| Batch | c(t) | Closed system, no flow |
| CSTR | c (steady) | Continuous stirred tank |
| PFR | c(z) | Plug flow reactor (1D) |
| Semibatch | c(t), V(t) | Feed addition over time |

**Reaction definition**:
```python
# Reaction: A + 2B → C
reaction.set('Formula', 'A+2B=>C')
reaction.set('RateConstant', 'kf')
reaction.set('Rate', 'kf*cA*cB^2')    # Elementary
reaction.set('ActivationEnergy', 'Ea')  # Arrhenius k = A·exp(−Ea/(RT))
```

**Rate law types**:

| Type | Rate Expression | Parameters |
|------|----------------|-----------|
| Mass action | r = k·Πcᵢ^(νᵢ) | k, reaction order |
| Langmuir-Hinshelwood | r = k·K·c/(1+K·c) | k, K |
| Enzymatic (Michaelis-Menten) | r = V_max·c/(K_m+c) | V_max, K_m |
| User defined | Any expression | — |

---

## 6. Chemistry Interface (chem)

Defines species and reactions independent of transport. Used to:

1. Generate rate expressions automatically from formulas
2. Import CHEMKIN files
3. Define thermodynamic properties (NASA polynomials)
4. Couple to transport interfaces via "Species" matching

```python
chem = comp.physics().create('chem', 'Chemistry')
# Add species
sp = chem.feature().create('sp_O2', 'Species')
sp.set('Formula', 'O2')
# Add reaction
rxn = chem.feature().create('rxn1', 'Reaction')
rxn.set('Formula', 'H2+0.5O2=>H2O')
rxn.set('RateConstant', '1e10[m^3/(mol*s)]')
```

---

## 7. Expression Reference

### 7.1 Transport Variables (`tds.*`)

| Expression | Unit | Description |
|-----------|------|-------------|
| `tds.c` | mol/m³ | Concentration (indexed by species) |
| `tds.c_<name>` | mol/m³ | Named species concentration |
| `tds.Nx`, `tds.Ny`, `tds.Nz` | mol/(m²·s) | Total flux |
| `tds.D_<name>` | m²/s | Diffusion coefficient |
| `tds.R_<name>` | mol/(m³·s) | Reaction rate |
| `tds.dfluxMag_<name>` | mol/(m²·s) | Diffusive flux magnitude |
| `tds.cfluxMag_<name>` | mol/(m²·s) | Convective flux magnitude |

### 7.2 Concentrated Species (`tcs.*`)

| Expression | Unit | Description |
|-----------|------|-------------|
| `tcs.x_<name>` | 1 | Mole fraction |
| `tcs.c` | mol/m³ | Total concentration |
| `tcs.w_<name>` | 1 | Mass fraction |
| `tcs.Dij` | m²/s | Binary Maxwell-Stefan diffusivity |

### 7.3 Reaction Engineering (`re.*`)

| Expression | Unit | Description |
|-----------|------|-------------|
| `re.c_<name>` | mol/m³ | Species concentration |
| `re.r_<reaction>` | mol/(m³·s) | Reaction rate |
| `re.k_f_<name>` | varies | Forward rate constant |
| `re.K_eq` | varies | Equilibrium constant |

---

## 8. Multiphysics Couplings

| Coupling | Interfaces | Application |
|----------|-----------|-------------|
| Reacting Flow | tds/tds + spf/ns | Chemical reactor with flow |
| Transport of Diluted Species–Laminar Flow | tds + spf | Microfluidic mixing |
| Nernst-Planck–Electrostatics | npe + es | Electrochemical cells |
| Porous Media Transport | tds + brinkman/darcy | Catalytic packed beds |
| Chemistry–Transport | chem + tds | Complex kinetics in flow |

---

## 9. COMSOL 6.4 Specific Notes

- **Species names**: Must be valid COMSOL identifiers (no spaces, special chars) — use underscores
- **Diffusion coefficients**: For liquids ~10⁻⁹ m²/s; for gases ~10⁻⁵ m²/s
- **Migration**: Requires electric field from AC/DC interface; mobility uₘ = D/(RT) (Nernst-Einstein)
- **Surface reactions**: Flux BC — rate in mol/(m²·s), convert from volume rate × surface area
- **Equilibrium reactions**: Set `ReactionType` to `Equilibrium`; COMSOL solves algebraic constraint
- **CHEMKIN import**: Use `chem.feature().create('imp1', 'CHEMKINImport')` — reads gas-phase kinetics
- **Turbulent Schmidt number**: Sc_T ≈ 0.7 for gases, ≈ 1000 for liquids (default in COMSOL)
- **Porous media tortuosity**: Bruggeman model: τ = ε^(−0.5)
