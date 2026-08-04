# Plasma Module — Comprehensive API Reference

COMSOL 6.4 · mph Python API · Based on official Plasma Module Users Guide and tags.json

---

## 1. Physics Interfaces

The Plasma Module provides 4 core interfaces under the **Plasma** branch:

| Interface | mph Tag | Default Name | Purpose |
|-----------|---------|-------------|---------|
| Plasma | `plas` | `plas` | Integrated multiphysics: Drift Diffusion + Heavy Species Transport + Electrostatics |
| Drift Diffusion | `dd` | `dd` | Electron density and mean energy transport |
| Heavy Species Transport | `hst` | `hst` | Ion and neutral species transport with reactions |
| Boltzmann Equation, Two-Term Approximation | `eb` | `eb` | Electron energy distribution function (EEDF) from cross-section data |

### 1.1 Plasma (plas) — Default Nodes

When adding the Plasma interface, COMSOL auto-creates:

| Default Node | mph Type | Purpose |
|-------------|---------|---------|
| Plasma Model | `PlasmaModel` | Species list, reactions, transport properties, electron kinetics |
| Zero Charge | `ZeroCharge` | n·D = 0 — default exterior BC |
| Insulation | `Insulation` | Species flux insulation |
| Initial Values | `InitialValues` | Initial electron density (nₑ₀), mean energy (ε̄₀), potentials |

### 1.2 Plasma Key Settings (Interface Level)

| Setting | Options | Description |
|---------|---------|-------------|
| Diffusion model | `MixtureAveraged` (default), `FicksLaw`, `Global` | Species diffusion model |
| Transport mechanisms | Convection, Migration, Thermodynamic properties, Tensor ion transport | Included transport effects |
| Heavy species energy | On/Off (Global model only) | Background gas temperature equation |
| Electron energy distribution | Maxwellian, Two-term Boltzmann, User defined | EEDF type for rate coefficients |
| Out-of-plane thickness (2D) | d (m) | 1 m default |
| Cross-section area (1D) | A (m²) | 0.01 m² default |

---

## 2. Domain Features — Plasma Interface

### 2.1 Plasma Model (default domain node)

| Aspect | Detail |
|--------|--------|
| mph type | `PlasmaModel` |
| Default tag | `pm1` |

**Sub-sections in Settings**:

| Section | Key Properties |
|---------|---------------|
| Species | Electron (e), ions (Ar⁺, O₂⁺...), neutrals (Ar, O₂...), excited states |
| Electron transport | Mobility μₑ, diffusivity Dₑ, energy mobility μₑε, energy diffusivity Dₑε |
| Heavy species transport | Mobility μₖ, diffusivity Dₖ per ion species |
| Reactions | Table: reaction formula, type, rate coefficient, energy loss per reaction |
| Surface reactions | Wall recombination, secondary emission, sputtering |
| Electron kinetics | EEDF source (Maxwellian, Boltzmann solution, user-defined) |
| Thermodynamics | Species enthalpy, heat capacity (for energy equation) |
| Magnetic field | B vector components (for tensor transport) |

### 2.2 Reaction Types

| Type | Formula Example | Description |
|------|---------------|-------------|
| Elastic | e + Ar → e + Ar | Momentum transfer, no chemistry change |
| Excitation | e + Ar → e + Ar* | Electronic excitation |
| Ionization | e + Ar → 2e + Ar⁺ | Electron impact ionization |
| Attachment | e + O₂ → O₂⁻ | Electron attachment |
| Recombination | e + Ar⁺ → Ar | Electron-ion recombination |
| Charge exchange | Ar⁺ + Ar → Ar + Ar⁺ | Resonant charge transfer |
| Penning ionization | Ar* + Ar* → e + Ar + Ar⁺ | Excited state pooling |
| Step-wise ionization | e + Ar* → 2e + Ar⁺ | Ionization from excited state |
| Dissociation | e + O₂ → e + O + O | Molecular dissociation |
| Dissociative attachment | e + O₂ → O + O⁻ | Attachment with dissociation |
| Ion conversion | Ar⁺ + 2Ar → Ar₂⁺ + Ar | Three-body ion conversion |
| Surface recombination | Ar⁺ + wall → Ar | Ion neutralization at walls |
| Secondary emission | Ar⁺ + wall → e + Ar | Electron emission from ion impact |

### 2.3 Additional Domain Features

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Species | `Species` | Define chemical species and properties |
| Reaction | `Reaction` | Add reaction to reaction set |
| Surface Reaction | `SurfaceReaction` | Wall reaction (boundary subnode) |
| Electron Impact Reaction | — | Cross-section based rate |
| Heavy Species Reaction | — | Ion-neutral chemistry |
| Reduced Electric Field | — | E/N based rate coefficients |
| Source | `Source` | External species/energy source |
| Loss | `Loss` | Species sink term |
| Mobility | — | Override species mobility |
| Diffusivity | — | Override species diffusivity |

---

## 3. Boundary Conditions — Plasma Interface

### 3.1 Wall

| Aspect | Detail |
|--------|--------|
| mph type | `Wall` |
| Dim | 1 (boundary) |

**Wall BC sub-models**:

| Model | Description | Key Properties |
|-------|-------------|---------------|
| Insulation | Γₑ·n = 0 (no flux) | Default |
| Ground | V = 0, plasma in contact with grounded electrode | Secondary emission coefficient γ |
| Dielectric | Surface charge accumulation σₛ | Surface charge density, secondary emission |
| Electrode | V = V₀, powered electrode | Voltage, DC/RF, blocking capacitor |
| Axial Symmetry | Auto on r=0 for 2D axisymmetry | — |

**Wall reaction types**:

| Type | Description |
|------|-------------|
| Sticking | Species sticks to wall with probability S |
| Recombination | Two surface-adsorbed species recombine |
| Ion neutralization | Ion + wall → neutral (with secondary electron emission) |
| Sputtering | Energetic ion knocks wall material off |

### 3.2 Additional BCs

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Ground | `Ground` | V = 0 at electrode |
| Electric Potential | `ElectricPotential` | V = V₀, DC or time-dependent |
| Floating Potential | `FloatingPotential` | Self-consistent V from current balance |
| Circuit Terminal | `Terminal` | Connect to Electrical Circuit interface |
| Surface Charge | `SurfaceCharge` | σₛ = Q/A |
| Axial Symmetry | `AxialSymmetry` | r = 0 for 2D axisymmetry |

---

## 4. Standalone Interfaces (without Plasma multiphysics)

### 4.1 Drift Diffusion (dd)

Solves electron continuity and energy equations:

| Node | mph Type | Purpose |
|------|---------|---------|
| Drift Diffusion Model | — | μₑ, Dₑ, electron source terms |
| Effective Diffusion | — | Corrected diffusion for high E/N |
| Electron Source | — | Net production rate from reactions |
| Townsend Coefficients | — | α (ionization), η (attachment) |

### 4.2 Heavy Species Transport (hst)

Solves multi-component diffusion for ions and neutrals:

| Node | mph Type | Purpose |
|------|---------|---------|
| Transport Properties | — | μₖ, Dₖ per species |
| Mixture Diffusion | — | Maxwell-Stefan multicomponent diffusion |
| Migration | — | Electric field drift for ions |

### 4.3 Boltzmann Equation, Two-Term Approximation (eb)

Solves for electron energy distribution function f₀(ε):

| Node | mph Type | Purpose |
|------|---------|---------|
| Boltzmann Equation | — | EEDF from cross-section database |
| Cross Section Data | — | Elastic, excitation, ionization cross sections |
| Reduced Electric Field | — | E/N sweep for rate coefficient tabulation |
| Rate Coefficients | — | kₖ = ∫ σₖ(ε)·f₀(ε)·√ε dε |

---

## 5. Expression Reference

### 5.1 Plasma Variables (`plas.*`)

| Expression | Unit | Description |
|-----------|------|-------------|
| `plas.Ne` | 1/m³ | Electron density |
| `plas.Ni` | 1/m³ | Ion density (per species) |
| `plas.Nn` | 1/m³ | Neutral density |
| `plas.V` | V | Electric potential |
| `plas.Er`, `plas.Ez` | V/m | Electric field |
| `plas.Te` | eV | Electron temperature (2/3·ε̄) |
| `plas.en` | V/m | Reduced electric field (E/N) |
| `plas.mue` | m²/(V·s) | Electron mobility |
| `plas.De` | m²/s | Electron diffusivity |
| `plas.Gamma_e` | 1/(m²·s) | Electron flux |
| `plas.Re` | 1/(m³·s) | Net electron production rate |
| `plas.Pabs` | W/m³ | Absorbed power density |
| `plas.Je` | A/m² | Electron current density |
| `plas.Ji` | A/m² | Ion current density |
| `plas.Jtot` | A/m² | Total current density |
| `plas.Vdc` | V | DC bias (CCP) |
| `plas.Vrf` | V | RF voltage amplitude |
| `plas.neutral_gas_temp` | K | Background gas temperature |

### 5.2 Drift Diffusion Variables (`dd.*`)

| Expression | Unit | Description |
|-----------|------|-------------|
| `dd.Ne` | 1/m³ | Electron density |
| `dd.mue` | m²/(V·s) | Electron mobility |
| `dd.Te` | eV | Electron temperature |
| `dd.alpha` | 1/m | Townsend ionization coefficient |
| `dd.eta` | 1/m | Townsend attachment coefficient |

---

## 6. Multiphysics Couplings

| Coupling | Interfaces | Application |
|----------|-----------|-------------|
| Plasma (built-in) | dd + hst + es | All plasma discharges |
| Inductive Plasma | plas ↔ mf | ICP (transformer coupled) |
| Microwave Plasma | plas ↔ emw | Surface wave, ECR |
| DC Discharge | plas (DC voltage) | Glow, arc, corona |
| Capacitively Coupled | plas (RF voltage) | CCP for etching/deposition |
| Plasma-Circuit | plas ↔ cir | Impedance matching networks |
| Plasma-Chemistry | plas ↔ chem | Complex gas-phase chemistry |

---

## 7. Study Types

| Study | Purpose |
|-------|---------|
| Time Dependent | Pulsed DC, RF transients, streamer propagation |
| Frequency Domain | CCP at fixed frequency |
| Stationary | DC glow discharge steady state |
| Time Dependent with Initialization | DC → steady base → RF modulation |
| Eigenfrequency | Plasma resonance |

---

## 8. mph API Usage

```python
# Create Plasma interface
plas = comp.physics().create('plas', 'Plasma', 'geom1')

# Access Plasma Model node
pm = plas.feature('pm1')
# Species, reactions, transport are configured in GUI or via complex API

# Set electrode boundary
el = plas.feature().create('el1', 'ElectricPotential', 1)
el.selection().set([electrode_bnd])
el.set('V0', '100[V]')  # DC or RMS for RF

# Ground boundary
gnd = plas.feature().create('gnd1', 'Ground', 1)
gnd.selection().set([ground_bnd])

# Time-dependent study for pulsed discharge
std = jm.study().create('std1')
td = std.feature().create('td1', 'Transient')
td.set('tlist', 'range(0,1e-9,1e-5)')
```

---

## 9. COMSOL 6.4 Specific Notes

- **Plasma (plas)** is a multiphysics interface; it automatically couples dd, hst, es — you don't create them separately
- **Boltzmann solver (eb)** is typically run BEFORE the plasma simulation to tabulate rate coefficients vs E/N
- **Surface charge on dielectrics**: Accumulates over time; crucial for DBD and CCP simulations
- **Secondary emission coefficient γ**: ~0.01-0.3 for most materials; critical for discharge sustainment
- **Mixture-averaged diffusion** is default and works well for most low-pressure plasmas
- **Fick's law** is simpler but less accurate for multi-component mixtures
- **Global model** adds heavy species energy equation for self-consistent gas heating
- **Tensor transport** only needed for strongly magnetized low-pressure plasmas (ECR, magnetron)
