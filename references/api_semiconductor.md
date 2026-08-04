# Semiconductor Module — Comprehensive API Reference

COMSOL 6.4 · mph Python API · Based on official Semiconductor Module Users Guide and tags.json

---

## 1. Physics Interfaces

The Semiconductor Module provides 5 interfaces under the **Semiconductor** branch:

| Interface | mph Tag | Default | Studies | Purpose |
|-----------|---------|---------|---------|---------|
| Semiconductor | `semi` | `semi` | Stationary, Time Dependent, Frequency Domain, Small-Signal | Drift-diffusion + Poisson for V, n, p |
| Semiconductor Optoelectronics, Beam Envelopes | `semi` | — | Frequency Domain | Optoelectronic with slowly-varying envelope |
| Semiconductor Optoelectronics, Frequency Domain | `semi` | — | Frequency Domain | Full-wave optoelectronic coupling |
| Schrodinger Equation | `schr` | — | Stationary, Eigenfrequency | Quantum confinement in nanostructures |
| Schrodinger-Poisson Equation | (multiphysics) | — | Stationary | Self-consistent quantum-electrostatic |

### 1.1 Semiconductor (semi) — Default Nodes

| Default Node | mph Type | Purpose |
|-------------|---------|---------|
| Semiconductor Material Model | `SemiconductorMaterialModel` | Governing equations: Poisson + drift-diffusion |
| Insulation | `Insulation` | n·Jₙ = n·Jₚ = 0 |
| Zero Charge | `ZeroCharge` | n·D = 0 |
| Initial Values | `InitialValues` | V = 0, n = n₀, p = p₀ |

### 1.2 Interface-Level Settings

| Setting | Options | Description |
|---------|---------|-------------|
| Carrier statistics | `MaxwellBoltzmann` (default), `FermiDirac` | MB: non-degenerate; FD: degenerate doping |
| Solution | `ElectronsAndHoles` (default), `MajorityCarriersOnly` | Full or single-carrier |
| Majority carriers | `Electrons`, `Holes` | For majority-carrier-only mode |
| Out-of-plane thickness | d (m) | 1 m default for 2D |
| Continuation parameter | Cp (0-1) | Doping ramping for convergence |
| Reference temperature | T_ref (K) | 300K default |

---

## 2. Domain Features — Semiconductor Interface

### 2.1 Semiconductor Material Model (default)

| Aspect | Detail |
|--------|--------|
| mph type | `SemiconductorMaterialModel` |
| Default tag | `smm1` |

**Key Material Properties**:

| Property | Symbol | Unit | Description |
|----------|--------|------|-------------|
| Relative permittivity | εᵣ | 1 | Semiconductor dielectric constant |
| Band gap | E_g | eV | Si: 1.12, GaAs: 1.42, GaN: 3.4 |
| Electron affinity | χ | eV | Si: 4.05, GaAs: 4.07 |
| Electron mobility | μₙ | cm²/(V·s) | Can be doping/temperature/field dependent |
| Hole mobility | μₚ | cm²/(V·s) | Models: Constant, Arora, Masetti, Klaassen |
| Electron lifetime | τₙ | s | SRH recombination |
| Hole lifetime | τₚ | s | SRH recombination |
| Effective DOS, conduction band | N_c | 1/cm³ | Si: 2.8e19 at 300K |
| Effective DOS, valence band | N_v | 1/cm³ | Si: 1.04e19 at 300K |

**Mobility Models**:

| Model | Parameters | Application |
|-------|-----------|-------------|
| Constant | μ₀ | Simple |
| Arora | μ_min, μ_max, N_ref, α | Doping-dependent (Si) |
| Masetti | μ_min1, μ_min2, μ₁, etc. | Wide doping range |
| Klaassen | Full parameter set | Most accurate (Si) |
| Lombardi (surface) | — | MOSFET channel mobility |
| High-field saturation | v_sat, β | GaN, SiC power devices |
| Temperature-dependent | μ(T) ∝ T^(-α) | Any |

### 2.2 Doping Profile

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Doping Profile | `DopingProfile` | n-type (donor) or p-type (acceptor) doping |
| Analytic Doping | — | Gaussian or error-function profiles |
| Constant Doping | — | N_D or N_A uniform |
| User-Defined Doping | — | Expression for N_D(x,y,z) |

**Key Properties**:

| Property | Unit | Description |
|----------|------|-------------|
| `N_D0` or `N_A0` | 1/cm³ | Peak doping concentration |
| `DopingType` | `Donor` or `Acceptor` | n-type or p-type |
| `JunctionDepth` | m | For Gaussian profiles |
| `DopingDistribution` | `Constant`, `Gaussian`, `ErrorFunction`, `UserDefined` | Profile shape |

### 2.3 Generation-Recombination (GR) Models

| Model | mph Type | Equation | Application |
|-------|---------|----------|-------------|
| Shockley-Read-Hall | `ShockleyReadHall` | R = (np−nᵢ²)/(τₚ(n+n₁)+τₙ(p+p₁)) | Defect-assisted |
| Auger | `AugerRecombination` | R = (Cₙn+Cₚp)(np−nᵢ²) | High carrier density |
| Direct/Band-to-Band | `DirectRecombination` | R = B(np−nᵢ²) | Direct gap (GaAs) |
| Impact Ionization | `ImpactIonization` | G = αₙ|Jₙ|/q + αₚ|Jₚ|/q | Avalanche |
| Trap-Assisted Tunneling | — | — | High-field regions |
| Optical Generation | `OpticalGeneration` | G = α·P/(hν) | Photodetectors |
| User Defined | — | User expression | Custom |

### 2.4 Additional Domain Features

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Trap Density | `TrapDensity` | Deep-level traps (energy, concentration, capture cross-section) |
| Discrete Energy Level | `DiscreteEnergyLevel` | Quantum well/quantum dot states |
| Continuous Energy Levels | `ContinuousEnergyLevels` | Band tail states (amorphous Si) |
| Insulator | `Insulator` | Dielectric regions (SiO₂, HfO₂) |
| Insulator Interface | `InsulatorInterface` | Heterointerface trap model |

---

## 3. Boundary Conditions

### 3.1 Metal Contacts

| BC | mph Type | Equation | Application |
|----|---------|----------|-------------|
| Ohmic Contact | `OhmicContact` | V = V₀ + V_bi, Δn = Δp = 0 | Ohmic metal-semiconductor |
| Schottky Contact | `SchottkyContact` | Jₙ·n = qvₙ(n−n₀), Jₚ·n = −qvₚ(p−p₀) | Rectifying metal-semiconductor |
| Gate | `Gate` | n·D = −ε_ox(V_G−V_FB)/t_ox | MOS gate with oxide |

**Ohmic Contact Properties**:

| Property | Description |
|----------|-------------|
| `V0` | Applied voltage (V) |
| `ContactType` | `IdealOhmic` — perfect neutrality |

**Schottky Contact Properties**:

| Property | Description |
|----------|-------------|
| `V0` | Applied voltage |
| `PhiB` | Barrier height (eV) |
| `v_n`, `v_p` | Surface recombination velocities (m/s) |
| `A_R` | Richardson constant (A/(cm²·K²)) |

**Gate Properties**:

| Property | Description |
|----------|-------------|
| `V_G` | Gate voltage |
| `V_FB` | Flat-band voltage |
| `t_ox` | Oxide thickness |
| `eps_ox` | Oxide permittivity |

### 3.2 Additional BCs

| BC | mph Type | Purpose |
|----|---------|---------|
| Insulation | `Insulation` | n·J = 0 (default) |
| Electric Potential | `ElectricPotential` | Specified V on non-contact boundaries |
| Ground | `Ground` | V = 0 |
| Surface Recombination | `SurfaceRecombination` | Boundary GR with v_s |
| Boundary Trap Density | — | Interface traps (D_it) |
| Periodic Condition | `PeriodicCondition` | Unit cell boundaries |

---

## 4. Edge & Point Features

| Feature | mph Type | Dim | Purpose |
|---------|---------|-----|---------|
| Line/Edge Contact | — | 0 (edge) | 2D contact on edges |
| Point Contact | — | 0 (point) | 1D/2D point contact |

---

## 5. Heterointerface Models

For heterojunctions (GaAs/AlGaAs, Si/SiGe, etc.):

| Feature | Description |
|---------|-------------|
| Trap-Assisted Heterointerface Recombination | Interface traps at heterojunction |
| Discrete Energy Level (Heterointerfaces) | Quantum states at interface |
| Transition Between Discrete Levels | Inter-subband transitions |
| Continuous Energy Levels (Heterointerfaces) | Band tails at interface |
| Insulator Interface | Dielectric/semiconductor boundary |

---

## 6. Expression Reference

### 6.1 Semiconductor Variables (`semi.*`)

| Expression | Unit | Description |
|-----------|------|-------------|
| `semi.V` | V | Electrostatic potential |
| `semi.n` | 1/m³ | Electron concentration |
| `semi.p` | 1/m³ | Hole concentration |
| `semi.E_fn` | V | Electron quasi-Fermi level |
| `semi.E_fp` | V | Hole quasi-Fermi level |
| `semi.Phi_n` | V | −E_fn/q (electron quasi-Fermi potential) |
| `semi.Phi_p` | V | −E_fp/q (hole quasi-Fermi potential) |
| `semi.Nc` | 1/m³ | Effective DOS, conduction band |
| `semi.Nv` | 1/m³ | Effective DOS, valence band |
| `semi.ni` | 1/m³ | Intrinsic carrier concentration |
| `semi.Eg` | V | Band gap (in eV as V) |
| `semi.Ec` | V | Conduction band edge |
| `semi.Ev` | V | Valence band edge |

### 6.2 Currents

| Expression | Unit | Description |
|-----------|------|-------------|
| `semi.Jnx`, `semi.Jny`, `semi.Jnz` | A/m² | Electron current density |
| `semi.Jpx`, `semi.Jpy`, `semi.Jpz` | A/m² | Hole current density |
| `semi.Jx`, `semi.Jy`, `semi.Jz` | A/m² | Total current density |
| `semi.Jtot` | A/m² | |J| magnitude |
| `semi.I0_1`, `semi.I0_2` | A | Terminal currents |

### 6.3 GR Rates

| Expression | Unit | Description |
|-----------|------|-------------|
| `semi.R_SRH` | 1/(m³·s) | SRH recombination rate |
| `semi.R_Auger` | 1/(m³·s) | Auger recombination rate |
| `semi.G_impact` | 1/(m³·s) | Impact ionization generation |
| `semi.G_op` | 1/(m³·s) | Optical generation rate |

### 6.4 Derived

| Expression | Unit | Description |
|-----------|------|-------------|
| `semi.mun`, `semi.mup` | m²/(V·s) | Mobility (field/doping-dependent) |
| `semi.Dn`, `semi.Dp` | m²/s | Diffusivity (Einstein relation) |
| `semi.taun`, `semi.taup` | s | Lifetime |
| `semi.Ln`, `semi.Lp` | m | Diffusion length |
| `semi.rho` | Ω·m | Resistivity |
| `semi.sigma` | S/m | Conductivity |
| `semi.Efield` | V/m | Electric field magnitude |
| `semi.Ex`, `semi.Ey`, `semi.Ez` | V/m | Electric field components |
| `semi.spacecharge` | C/m³ | Space charge density ρ = q(p−n+N_D−N_A) |

### 6.5 Small-Signal AC

| Expression | Unit | Description |
|-----------|------|-------------|
| `semi.Y11`, `semi.Y12` | S | Admittance parameters |
| `semi.Cgs`, `semi.Cgd` | F | Gate-source/drain capacitance |
| `semi.gm` | S | Transconductance |
| `semi.ft` | Hz | Cutoff frequency |

---

## 7. Multiphysics Couplings

| Coupling | Interfaces | Application |
|----------|-----------|-------------|
| Schrodinger-Poisson | schr + semi | Quantum-confined carriers |
| Optoelectronics, Beam Envelopes | semi + ewbe | Waveguide photodetectors |
| Optoelectronics, Frequency Domain | semi + ewfd | Solar cells, photodetectors |
| Semiconductor-Electromagnetic | semi + emw | Full-wave optoelectronic |
| Semiconductor-Heat Transfer | semi + ht | Self-heating (Joule + recombination) |
| Circuit-Semiconductor | semi + cir | Mixed-mode device-circuit simulation |

---

## 8. Study Types

| Study | Purpose |
|-------|---------|
| Stationary | DC operating point (I-V curves) |
| Time Dependent | Transient response, switching |
| Frequency Domain | Small-signal AC, capacitance |
| Small-Signal, Frequency Domain | Y-parameters, s-parameters |
| Eigenfrequency | Resonant tunneling, plasma oscillations |
| Semiconductor Equilibrium | Initial condition (V=0, thermal equilibrium) |

---

## 9. COMSOL 6.4 Specific Notes

- **Equilibrium study step**: Always run first to establish V=0 thermal equilibrium before DC bias sweep
- **Continuation parameter Cp**: Ramp doping from 0→full to aid convergence at high bias
- **Fermi-Dirac statistics**: Required when doping > ~10¹⁸ cm⁻³ (degenerate); computationally heavier than Maxwell-Boltzmann
- **Mobility models**: Klaassen is most accurate for Si but requires 15+ parameters; Arora is simpler
- **Impact ionization**: Uses Okuto-Crowell or van Overstraeten models; critical for breakdown voltage simulation
- **Triangular well quantization**: For MOSFET inversion layers, use Schrodinger-Poisson coupling
- **Heterojunctions**: Require careful band alignment (electron affinity difference = ∆E_c)
- **Surface recombination velocity v_s**: ~10⁴ cm/s for unpassivated Si, ~1 cm/s for passivated

## mph API Usage

```python
semi = comp.physics().create('semi', 'Semiconductor', 'geom1')
semi.set('CarrierStatistics', 'MaxwellBoltzmann')
doping = semi.feature().create('dop1', 'DopingProfile', 2)
ohmic = semi.feature().create('oc1', 'OhmicContact', 1)
ohmic.set('V0', '0[V]')
model.evaluate('semi.n', '1/cm^3')
```
