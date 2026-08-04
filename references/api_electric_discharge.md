# Electric Discharge Module — Comprehensive API Reference

COMSOL 6.4 · mph Python API · Based on official Electric Discharge Module Users Guide and tags.json

---

## 1. Physics Interfaces

| Interface | mph Tag | Default | Studies | Purpose |
|-----------|---------|---------|---------|---------|
| Electric Discharge | `ed` | `ed` | Time Dependent, Stationary | Corona, streamer, DBD discharges |
| Arc Discharge | (multiphysics) | — | Time Dependent, Stationary | Thermal arc plasma |
| Transport of Charge Carriers | `tcc` | `tcc` | Time Dependent, Stationary | Charge injection and transport in dielectrics |
| Electrostatics | `es` | `es` | Stationary | Electric field for discharge (from AC/DC) |

### 1.1 Electric Discharge (ed) — Default Nodes

| Default Node | mph Type | Purpose |
|-------------|---------|---------|
| Electric Discharge Model | — | Governing equations: drift + diffusion + reactions + Poisson |
| Zero Charge | `ZeroCharge` | n·D = 0 |
| Insulation | — | Species flux insulation |
| Initial Values | `InitialValues` | nₑ₀, n₊₀, n₋₀, V₀ |

### 1.2 Key Settings

| Setting | Options | Description |
|---------|---------|-------------|
| Discharge type | `Corona`, `Streamer`, `DBD`, `UserDefined` | Type of discharge |
| Species | Electrons, positive ions, negative ions | Active charge carriers |
| Transport | Drift + diffusion | μₑE·∇nₑ + Dₑ∇²nₑ |
| Reactions | Ionization α, attachment η, recombination β | Townsend coefficients |
| Photoionization | On/Off | Non-local ionization in streamers |
| Dielectric interfaces | Surface charge accumulation σ(t) | For DBD |

---

## 2. Domain Features

### 2.1 Electric Discharge Model

**Governing Equations**:

∂nₑ/∂t + ∇·(−nₑμₑE − Dₑ∇nₑ) = (α−η)|Γₑ| − βₑₚnₑn₊ + S_photo

**Transport Parameters**:

| Parameter | Symbol | Unit | Description |
|-----------|--------|------|-------------|
| Electron mobility | μₑ | m²/(V·s) | Often μₑN = f(E/N) |
| Electron diffusivity | Dₑ | m²/s | Dₑ = μₑk_BTₑ/e |
| Ion mobility | μ₊, μ₋ | m²/(V·s) | Lighter ions move faster |
| Townsend ionization | α | 1/m | α/N = f(E/N) — electrons per unit length |
| Townsend attachment | η | 1/m | For electronegative gases (O₂, SF₆) |
| Effective ionization | ᾱ = α−η | 1/m | Net electron production |
| Recombination | βₑₚ | m³/s | Electron-ion recombination |
| Ion-ion recombination | β₊₋ | m³/s | In electronegative mixtures |
| Secondary emission | γ | 1 | Electrons per ion impact at cathode |
| Photoionization | S_photo | 1/(m³·s) | Zheleznyak model for air |

### 2.2 Additional Domain Features

| Feature | Purpose |
|---------|---------|
| Townsend Coefficients | α(E/N), η(E/N) from table or function |
| Photoionization Model | Non-local source term integral |
| Dielectric Interface, Bulk Transport | Charge transport inside dielectric bulk |
| Dielectric Interface, Surface Transport | Surface charge mobility on dielectric |

---

## 3. Boundary Conditions

| BC | mph Type | Equation | Application |
|----|---------|----------|-------------|
| Ground | `Ground` | V = 0 | Cathode |
| Electric Potential | `ElectricPotential` | V = V₀ | Anode |
| Floating Potential | `FloatingPotential` | Self-consistent V | Dielectric barriers |
| Outflow | `Outflow` | Species leave domain | Open boundaries |
| Wall (species) | — | n·Γₑ = (secondary emission) | Gas-solid interface |
| Axial Symmetry | `AxialSymmetry` | Auto on r=0 | 2D axisymmetric |

---

## 4. Expression Reference

| Expression | Unit | Description |
|-----------|------|-------------|
| `ed.Ne` | 1/m³ | Electron density |
| `ed.Np` | 1/m³ | Positive ion density |
| `ed.Nn` | 1/m³ | Negative ion density |
| `ed.V` | V | Electric potential |
| `ed.Ex`, `ed.Ez` | V/m | Electric field (vector + magnitude) |
| `ed.W_e` | eV | Mean electron energy |
| `ed.Te` | K | Electron temperature |
| `ed.mue` | m²/(V·s) | Electron mobility |
| `ed.alpha` | 1/m | Ionization coefficient |
| `ed.eta` | 1/m | Attachment coefficient |
| `ed.Gamma_e` | 1/(m²·s) | Electron flux magnitude |
| `ed.S_photo` | 1/(m³·s) | Photoionization source |
| `ed.spacecharge` | C/m³ | Space charge density |

---

## 5. Multiphysics Couplings

| Coupling | Interfaces | Application |
|----------|-----------|-------------|
| Arc Discharge | ed + ht + spf + mf | Welding arcs, circuit breakers |
| Electric Discharge–Heat Transfer | ed + ht | Gas heating in streamers |
| Electric Discharge–Laminar Flow | ed + spf | Ionic wind, EHD flow |

---

## 6. COMSOL 6.4 Specific Notes

- **Photoionization**: Computationally expensive (integral over emission-absorption); use Zheleznyak model for air
- **Streamer propagation**: Requires fine mesh (~1-10 μm) at the streamer head; adaptive mesh refinement recommended
- **E/N scaling**: Townsend coefficients tabulated vs reduced electric field E/N (Td = 10⁻²¹ V·m²)
- **Dielectric barriers**: Surface charge σ stored as boundary ODE; integrates ion/electron fluxes over time
- **Secondary emission γ**: ~0.001–0.1; critical for DC glow sustainment
