# RF Module — Comprehensive API Reference

COMSOL 6.4 · mph Python API · Based on official RF Module Users Guide (376 pages) and tags.json

---

## 1. Physics Interfaces

The RF Module provides 9 physics interfaces under the **Radio Frequency** branch:

| # | Interface | mph Tag | Default Name | Supported Studies |
|---|-----------|---------|-------------|-------------------|
| 1 | Electromagnetic Waves, Frequency Domain | `emw` | `emw` | Frequency Domain, Eigenfrequency, Mode Analysis, Boundary Mode Analysis |
| 2 | Electromagnetic Waves, Transient | `emw` | `emw` | Time Dependent |
| 3 | Electromagnetic Waves, Time Explicit | `emw` | `emw` | Time Dependent (explicit) |
| 4 | Electromagnetic Waves, Asymptotic Scattering | `emw` | `emw` | Frequency Domain |
| 5 | Electromagnetic Waves, Boundary Elements | `emw` | `emw` | Frequency Domain |
| 6 | Electromagnetic Waves, FEM-BEM | `emw` | `emw` | Frequency Domain |
| 7 | Transmission Line | `tl` | `tl` | Frequency Domain |
| 8 | Transmission Line, Transient | `tl` | `tl` | Time Dependent |
| 9 | Transmission Line, Parameters | `tl` | `tl` | Stationary |

### 1.1 EMW Frequency Domain — Auto-Created Default Nodes

When the interface is added, COMSOL creates these nodes automatically:

| Default Node | mph Type | Dim | Equation/Purpose |
|-------------|---------|-----|------------------|
| Wave Equation, Electric | `WaveEquationElectric` | Domain (2) | ∇×(μᵣ⁻¹∇×E) − k₀²(εᵣ − jσ/(ωε₀))E = 0 |
| Perfect Electric Conductor | `PerfectElectricConductor` | Boundary (1) | n×E = 0 — default exterior boundary |
| Initial Values | `InitialValues` | Domain (2) | E = (0,0,0) |

### 1.2 Interface-Level Settings

| Property | mph set() Name | Values | Description |
|----------|---------------|--------|-------------|
| Formulation | `Formulation` | `FullField` (default), `ScatteredField` | Scattered field separates background from scattered |
| Components | `Components` | `ThreeComponentVector`, `OutOfPlaneVector`, `InPlaneVector` | Dimensionality of solved E-field |
| Background wave | — | `UserDefined`, `GaussianBeam`, `LinearlyPolarizedPlaneWave`, `CircularlyPolarizedPlaneWave` | For scattered field formulation |
| Mesh control | — | `FromStudy`, `UserDefined`, `Frequency`, `Wavelength` | Controls λ-based mesh sizing |

---

## 2. Domain Features — EMW Frequency Domain

### 2.1 Wave Equation, Electric (Default Domain Node)

| Aspect | Detail |
|--------|--------|
| mph type | `WaveEquationElectric` |
| Default tag | `we1` |

**Material Models** (select one in Settings):

| Model | mph Property | Key Parameters |
|-------|-------------|----------------|
| Relative permittivity | `RelativePermittivity` | εᵣ, μᵣ, σ (scalar or matrix) |
| Refractive index | — | n, k (εᵣ = (n−jk)², assumes μᵣ=1, σ=0) |
| Loss tangent, loss angle | — | εᵣ', δ |
| Dielectric loss | — | εᵣ', εᵣ'' (εᵣ = εᵣ'−jεᵣ'') |
| Drude-Lorentz dispersion | — | ε∞, ωₚ, oscillator table |
| Debye dispersion | — | ε∞, Δεₖ, τₖ |

### 2.2 Additional Domain Features

| Feature | mph Type | Tag Pattern | Purpose |
|---------|---------|------------|---------|
| Divergence Constraint | `DivergenceConstraint` | `dc*` | Suppresses spurious modes in eigenfrequency |
| External Current Density | `ExternalCurrentDensity` | `ecd*` | Adds Jₑ source term |
| Far-Field Domain | `FarFieldDomain` | `ffd*` | Enclosing domain for far-field calculation |
| Far-Field Domain, Inhomogeneous | `FarFieldDomainInhomogeneous` | `ffdi*` | Far-field with superstrate/substrate (3D) |
| Periodic Structure | `PeriodicStructure` | `ps*` | Periodic cell with diffraction orders |
| Specific Absorption Rate | `SpecificAbsorptionRate` | `sar*` | SAR = σ|E|²/(2ρ) for dosimetry |
| Axial Symmetry | `AxialSymmetry` | `axi*` | Auto-added for 2D axisymmetry |

---

## 3. Boundary Conditions

### 3.1 Primary BCs

| BC | mph Type | Tag | Equation | Use Case |
|----|---------|-----|----------|----------|
| Perfect Electric Conductor | `PerfectElectricConductor` | `pec*` | n×E = 0 | Lossless metal surfaces, ground planes |
| Perfect Magnetic Conductor | `PerfectMagneticConductor` | `pmc*` | n×H = 0 | High-impedance surfaces, symmetry |
| Port | `Port` | `p*` | Various | Waveguide/transmission line excitation |
| Lumped Port | `LumpedPort` | `lp*` | Uniform field | Concentrated port with voltage input |
| Scattering BC | `ScatteringBoundaryCondition` | `sbc*` | 1st or 2nd order | Absorbing outgoing plane waves |
| Impedance BC | `ImpedanceBoundaryCondition` | `ibc*` | Leontovich | Thin conductive layers (no mesh inside) |
| Transition BC | `TransitionBoundaryCondition` | `tbc*` | — | Thin dielectric/metal interior layers |
| Layered Transition BC | `LayeredTransitionBoundaryCondition` | `ltbc*` | — | Multilayer thin structures |
| Periodic Condition | `PeriodicCondition` | `pc*` | Phase shift φ | Unit cell periodicity |
| Floquet Periodicity | `FloquetPeriodicity` | `fp*` | k-vector | Bloch-Floquet boundaries |
| Perfectly Matched Layer | `PerfectlyMatchedLayer` | `pml*` | — | Reflectionless absorption |
| Symmetry Plane | `SymmetryPlane` | `sp*` | PEC or PMC | Model size reduction |
| Electric Field | `ElectricField` | `ef*` | n×E = n×E₀ | Specified tangential E-field |
| Magnetic Field | `MagneticField` | `mf*` | n×H = n×H₀ | Specified tangential H-field |
| Surface Current | `SurfaceCurrentDensity` | `scd*` | — | Specified surface current |
| Far-Field Calculation | `FarFieldCalculation` | `ffc*` | — | Selects far-field computation boundaries |

### 3.2 Port Types and Properties

| Port Type | Geometry | Key Properties |
|-----------|----------|---------------|
| Rectangular | Width a, Height b | Mode number, polarization |
| Circular | Radius r | Mode number, polarization |
| Coaxial | Inner a, Outer b | Mode number, TEM |
| Periodic | — | Diffraction orders, incident angle |
| User Defined | — | Custom E/H field expressions |
| Numeric | — | N×N port (coupled ports) |

**Common Port Properties**:

| Property | Values | Description |
|----------|--------|-------------|
| `WaveExcitation` | `On`/`Off` | Enable source excitation at this port |
| `Pin` | Power (W) | Input power for excited port |
| `SparameterSweep` | `On`/`Off` | Include in S-parameter calculation |
| `ActivateTerminal` | `On`/`Off` | Connect to Electrical Circuit interface |
| `Zref` | Impedance (Ω) | Reference impedance (default 50Ω) |

### 3.3 Scattering BC Orders

| Order | Equation | Reflection |
|-------|----------|------------|
| First | n×∇×E − jkn×(E×n) = 0 | ~10⁻¹ at 30° from normal |
| Second | (higher-order absorbing) | ~10⁻³ at 45° from normal |

---

## 4. Edge & Point Features

| Feature | mph Type | Dim | Purpose |
|---------|---------|-----|---------|
| Electric Field (Edge) | `ElectricField` | 0 (edge) | Specified E on edges |
| Magnetic Current (Edge) | `MagneticCurrent` | 0 (edge) | Line magnetic current |
| Electric Point Dipole | `ElectricPointDipole` | 0 (point) | Hertzian dipole (3D) |
| Magnetic Point Dipole | `MagneticPointDipole` | 0 (point) | Magnetic dipole (3D) |

---

## 5. Expression Reference

### 5.1 Field Variables (`emw.*`)

| Expression | Unit | Description |
|-----------|------|-------------|
| `emw.Ex`, `emw.Ey`, `emw.Ez` | V/m | Electric field components |
| `emw.normE` | V/m | |E| magnitude |
| `emw.Hx`, `emw.Hy`, `emw.Hz` | A/m | Magnetic field components |
| `emw.normH` | A/m | |H| magnitude |

### 5.2 Power, Energy & Heating

| Expression | Unit | Description |
|-----------|------|-------------|
| `emw.Poavx/y/z` | W/m² | Time-averaged Poynting vector |
| `emw.normPoav` | W/m² | Power flow magnitude |
| `emw.Qh` | W/m³ | Resistive/dielectric heating |
| `emw.Weav` | J/m³ | Electric energy density |
| `emw.Wmav` | J/m³ | Magnetic energy density |
| `emw.SAR` | W/kg | Specific absorption rate |

### 5.3 S-Parameters & Port Quantities

| Expression | Unit | Description |
|-----------|------|-------------|
| `emw.S11`, `emw.S21` | 1 | Complex S-parameters |
| `emw.S11dB` | dB | S-parameters in dB |
| `emw.VSWR1` | 1 | VSWR at port 1 |
| `emw.Zin` | Ω | Input impedance |
| `emw.Yin` | S | Input admittance |
| `emw.Qfactor` | 1 | Quality factor (eigenfrequency) |
| `emw.neff` | 1 | Effective mode index |
| `emw.beta` | rad/m | Propagation constant |

### 5.4 Far-Field

| Expression | Unit | Description |
|-----------|------|-------------|
| `emw.Efarx/y/z` | V/m | Far-field electric field |
| `emw.normEfar` | V/m | |Efar| magnitude |
| `emw.gaindB` | dB | Antenna gain |
| `emw.DdB` | dB | Directivity |
| `emw.RCS` | m² | Radar cross section |

### 5.5 Constants

| Expression | Unit | Value | Description |
|-----------|------|-------|-------------|
| `emw.c_const` | m/s | 2.998e8 | Speed of light |
| `emw.epsilon0_const` | F/m | 8.854e-12 | Vacuum permittivity |
| `emw.mu0_const` | H/m | 4π×10⁻⁷ | Vacuum permeability |
| `emw.Z0_const` | Ω | ~377 | Impedance of free space |
| `emw.k0` | rad/m | 2π/λ₀ | Free-space wavenumber |
| `emw.lambda` | m | c/f | Free-space wavelength |
| `emw.freq` | Hz | — | Frequency |
| `emw.omega` | rad/s | 2πf | Angular frequency |

---

## 6. Mesh Requirements

The RF interfaces use **physics-controlled mesh** that auto-sizes elements based on wavelength:

| Shape Function | 2D Max Size | 3D Max Size |
|---------------|------------|------------|
| Quadratic (default) | λ₀/8 | λ₀/5 |
| Linear | λ₀/16 | λ₀/10 |
| Cubic | ~2.25× quadratic | ~2.25× quadratic |

In dielectric media: max_size = free_space_size / √(εᵣμᵣ)

In lossy media (when "Resolve wave in lossy media" is on): max_size = min(δ_skin/2, λ₀/5)

---

## 7. Multiphysics Couplings

| Coupling | mph Type | Interfaces Linked | Application |
|----------|---------|-------------------|-------------|
| Electromagnetic Heating | `ElectromagneticHeating` | emw ↔ ht | RF/microwave heating |
| Thermal-Structure from EM | — | emw ↔ ht ↔ solid | Thermal stress from RF |
| Plasma-EM | — | emw ↔ plasma | Self-consistent plasma-MW |
| Circuit-EM | — | emw ↔ cir | SPICE co-simulation |
| Semiconductor-EM | — | emw ↔ semi | Photodetectors, solar cells |

---

## 8. mph API Usage — Working Examples (COMSOL 6.4)

### Create Interface

```python
emw = comp.physics().create('emw', 'ElectromagneticWaves', 'geom1')
# Default nodes available: we1 (Wave Equation), pec1 (PEC), init1
```

### Set Material

```python
we = emw.feature('we1')
we.set('RelativePermittivity', '4.5')  # scalar εr
we.set('RelativePermeability', '1.0')
we.set('ElectricConductivity', '0[S/m]')
```

### Add Port

```python
port = emw.feature().create('p1', 'Port', 1)  # dim=1 for boundary
port.selection().set([bnd_num])
port.set('PortType', 'Rectangular')
port.set('WaveExcitation', 'On')
port.set('Pin', '1[W]')
```

### Add Scattering BC

```python
sbc = emw.feature().create('sbc1', 'ScatteringBoundaryCondition', 1)
sbc.selection().set([radiation_bnd])
```

### Set Mesh Size

```python
sz = mesh.feature().create('sz_em', 'Size')
sz.selection().all()
# λ/5 for 3D at 10 GHz
sz.set('hmax', f'{3e8/10e9/5}[m]')  # = 6mm
```

---

## 9. COMSOL 6.4 Specific Notes

- **Physics-controlled mesh**: Must be enabled in Mesh node settings; uses vacuum wavelength from highest study frequency
- **Port sweeps**: Use `Parametric` study with port name; auto-creates `modeNum` parameter for 2D axisymmetry
- **Touchstone export**: `model.result().export().create('touchstone', 'Touchstone')` for S-parameter files
- **Far-field variables** (`Efar`, gain, RCS): Only available when Far-Field Domain + Far-Field Calculation nodes are present
- **Periodic structures**: Require `PeriodicStructure` (domain) + `FloquetPeriodicity` (BC) + `Periodic`/`DiffractionOrder` ports
- **Default reference impedance**: 50Ω for all ports
- **2D axisymmetric**: Use `LinearlyPolarizedPlaneWave` with `Set up Sweep` button to auto-create azimuthal mode expansion
- **Maximum mesh element**: λ₀/5 in 3D free space is the COMSOL default (not just a recommendation)
