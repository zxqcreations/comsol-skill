# Optics Module — Comprehensive API Reference

COMSOL 6.4 · mph Python API · Based on official Ray Optics (276pp) + Wave Optics Module documentation and tags.json

---

## 1. Physics Interfaces

The Optics Module spans two sub-modules:

### 1.1 Ray Optics Interfaces

| Interface | mph Tag | Studies | Purpose |
|-----------|---------|---------|---------|
| Geometrical Optics | `gop` | Ray Tracing, Bidirectionally Coupled Ray Tracing | Ray trajectories in large structures (L >> λ) |

### 1.2 Wave Optics Interfaces

| Interface | mph Tag | Studies | Purpose |
|-----------|---------|---------|---------|
| Electromagnetic Waves, Frequency Domain | `ewfd` | Frequency Domain, Eigenfrequency, Mode Analysis | Full-wave EM for optical frequencies |
| Electromagnetic Waves, Beam Envelopes | `ewbe` | Frequency Domain | Slowly-varying envelope (waveguide, fiber) |

---

## 2. Ray Optics — Geometrical Optics (gop)

### 2.1 Ray Tracing Algorithm

Rays propagate ballistically through domains. Position q and wave vector k evolve as:

```
dq/dt = ∂ω/∂k      (group velocity)
dk/dt = −∂ω/∂q      (refraction/reflection)
```

Where ω is the angular frequency. The ray is advanced in time steps or optical path length steps specified in the Ray Tracing study step.

### 2.2 Domain Features

#### Medium Properties (default domain node)

| mph Type | Purpose |
|----------|---------|
| `MediumProperties` | Defines refractive index n(λ) in each domain |

**Refractive index specification options**:

| Model | Key Properties | Description |
|-------|---------------|-------------|
| Refractive index | n (real), k (imaginary) | n − jk complex index |
| Sellmeier | B₁,B₂,B₃, C₁,C₂,C₃ | n² = 1 + Σ Bᵢλ²/(λ²−Cᵢ) |
| Schott | a₀−a₅ coefficients | Glass catalog formula |
| Polynomial | Degree, coefficients | n(λ) as polynomial |
| Temperature-dependent | dn/dT | Thermo-optic effects |
| Abbe number | n_d, V_d, P_gF | Optical glass characterization |

#### Additional Domain Features

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Scattering | `Scattering` | Volume scattering (Mie, Rayleigh) |
| Absorption | `Absorption` | Attenuation coefficient α(λ) |
| Thermal Expansion | — | Temperature-dependent geometry |
| External Force | — | Electromagnetic/gravity forces on rays |

### 2.3 Boundary Conditions

#### Material Discontinuity (default)

| mph Type | Purpose |
|----------|---------|
| `MaterialDiscontinuity` | Automatic reflection and refraction at interfaces |

Reflection/refraction governed by Snell's law: n₁sinθ₁ = n₂sinθ₂

#### Wall Conditions

| BC | mph Type | Equation | Purpose |
|----|---------|----------|---------|
| Wall | `Wall` | User-defined interaction | General ray termination |
| Freeze | `Wall` (Freeze) | Ray stops | Ray termination at boundaries |
| Disappear | `Wall` (Disappear) | Ray deleted | Absorption at walls |
| Reflect | `Wall` (Reflect) | Specular reflection | Mirror surfaces |
| Refract | `Wall` (Refract) | Snell's law | Transparent interfaces |
| Absorb | `Wall` (Absorb) | Partial absorption | Lossy walls |
| Scatter | `Wall` (Scatter) | BSDF model | Diffuse/specular scattering |

#### Special Boundary Features

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Grating | `Grating` | Diffraction grating (orders + efficiency) |
| Interference Pattern | — | Computes interference from ray phase data |
| Diffraction Order | — | Subnode of Grating for each order |
| Cross Grating | `CrossGrating` | 2D periodic grating |
| Stop Condition | — | Conditional ray termination |

**Grating Properties**:

| Property | Description |
|----------|-------------|
| Grating period | d (μm or nm) |
| Diffraction order | m = ..., -2, -1, 0, 1, 2, ... |
| Grating vector | Orientation of periodic lines |
| Efficiency | Per-order relative intensity |

### 2.4 Ray Release Features

Rays are emitted from one of these feature types:

| Release Type | mph Type | Dim | Description |
|-------------|---------|-----|-------------|
| Grid-Based | `ReleaseFromGrid` | 2 (domain) | Rays from regular grid points |
| From Boundary | `ReleaseFromBoundary` | 1 (boundary) | Rays from selected boundaries |
| From Edge | `ReleaseFromEdge` | 0 (edge) | Rays from curve (2D) |
| From Point | `ReleaseFromPoint` | 0 (point) | Rays from single point |
| From Domain | `ReleaseFromDomain` | 2 (domain) | Volume-distributed rays |
| Annular | `AnnularRelease` | 1 | Ring-shaped distribution |
| Hexapolar | `HexapolarRelease` | 1 | 6-fold symmetric release |
| Solar | `SolarRelease` | 1 | Angular solar disc distribution |

**Key Release Properties**:

| Property | Unit | Description |
|----------|------|-------------|
| `Nx`, `Ny`, `Nz` | 1 | Number of rays per direction |
| `RayDirectionVector` | 1 | Initial direction (unit vector) |
| `VacuumWavelength` | m | λ₀ for polychromatic simulations |
| `InitialIntensity` | W/m² | Ray intensity (or power) |
| `Polarization` | — | Stokes parameters or Jones vector |
| `InitialWavefrontCurvature` | 1/m | For Gaussian beam propagation |
| `ReleaseTime` | s | When rays start (transient) |

### 2.5 Auxiliary Dependent Variables

Beyond ray position and wave vector, gop supports additional DOFs:

| Variable | Purpose |
|----------|---------|
| Intensity | Power carried by each ray |
| Polarization (Stokes parameters S₀,S₁,S₂,S₃) | Full polarization state |
| Wavefront curvature (5 components) | Astigmatic Gaussian beam propagation |
| Deposited ray power | Absorbed power in domains/walls |
| Optical path length (OPL) | Phase tracking for interference |
| Ray index | Unique identifier per ray |

### 2.6 Ray Optics Expression Reference

| Expression | Unit | Description |
|-----------|------|-------------|
| `gop.rrel` | 1 | Relative ray position (0→1 along path) |
| `gop.qx,qy,qz` | m | Ray position |
| `gop.kx,ky,kz` | rad/m | Wave vector components |
| `gop.Intensity` | W/m² | Ray intensity |
| `gop.Power` | W | Transmitted ray power |
| `gop.OPL` | m | Optical path length |
| `gop.wavelength` | m | Vacuum wavelength |
| `gop.freq` | Hz | Frequency |
| `gop.n` | 1 | Refractive index at ray position |
| `gop.S0,S1,S2,S3` | W/m² | Stokes parameters |
| `gop.DOP` | 1 | Degree of polarization |
| `gop.s1xys_curv` | 1/m | Wavefront curvature component (s₁,xy) |
| `gop.rpd` | W/m³ | Deposited ray power density |

---

## 3. Wave Optics

### 3.1 Electromagnetic Waves, Frequency Domain (ewfd)

Same as RF Module's `emw` interface (see api_rf.md), but at optical frequencies. Default name is `ewfd` to distinguish from RF usage.

**Key differences from RF:**
- Wavelengths: ~400-1600nm instead of mm-cm
- Materials: glass catalogs (Schott, Ohara), Sellmeier models
- Ports less common; scattering BC and PML more common
- Mode analysis for waveguide/fiber eigenmodes

### 3.2 Electromagnetic Waves, Beam Envelopes (ewbe)

The **Beam Envelope Method** solves Maxwell's equations with the ansatz:

```
E(r) = Ẽ(r) · exp(−jk₁·r)
```

Where Ẽ(r) is the slowly-varying envelope and k₁ is the wave vector. This allows much coarser mesh for guided-wave problems.

**Default Nodes**:

| Node | mph Type | Purpose |
|------|---------|---------|
| Wave Equation, Electric | — | Maxwell with envelope ansatz |
| Perfect Electric Conductor | — | n×E = 0 |
| Initial Values | — | Ẽ = 0 |

**Wave Vector Specification**:

| Method | Description |
|--------|-------------|
| User defined | Enter k₁ components directly |
| From mode analysis | Use k from Boundary Mode Analysis |

**Key Benefit**: Mesh size determined by envelope variation, not wavelength. For fiber with λ=1.55μm and mm-scale length: mesh can be ~λ (no envelope) vs ~mm (with envelope) — orders of magnitude difference.

### 3.3 Wave Optics Expression Reference

| Expression | Unit | Description |
|-----------|------|-------------|
| `ewfd.Ex,Ey,Ez` | V/m | Electric field |
| `ewfd.normE` | V/m | |E| |
| `ewfd.neff` | 1 | Effective mode index |
| `ewfd.beta` | rad/m | Propagation constant |
| `ewfd.D` | 1 | Group velocity dispersion |
| `ewfd.alpha` | dB/m | Attenuation constant |
| `ewfd.Aeff` | m² | Effective mode area |
| `ewfd.gamma` | 1 | Nonlinear coefficient |

For Beam Envelopes interface (`ewbe.*`): same variables but envelope fields.

---

## 4. Multiphysics Couplings

| Coupling | Interfaces | Application |
|----------|-----------|-------------|
| Ray-EM coupling | gop ↔ ewfd | Bidirectional: EM → ray source; rays → EM source |
| Ray-Heating | gop ↔ ht | Laser/material processing |
| Ray-Thermal-Structure | gop ↔ ht ↔ solid | Thermal stress from optical absorption |
| Optoelectronics | ewfd ↔ semi | Photodetectors, solar cells, LEDs |

---

## 5. Study Types

| Study | Interface | Purpose |
|-------|-----------|---------|
| Ray Tracing | gop | Forward ray trace with fixed time/OPL steps |
| Bidirectionally Coupled Ray Tracing | gop ↔ physics | Rays and physics solve iteratively |
| Frequency Domain | ewfd, ewbe | Single-frequency or swept-frequency |
| Eigenfrequency | ewfd, ewbe | Resonant modes, propagation constants |
| Mode Analysis | ewfd | Waveguide cross-section modes |
| Boundary Mode Analysis | ewfd | Port mode calculation |

### Ray Tracing Study Step Properties

| Property | Description |
|----------|-------------|
| `TimeStep` | Ray time step size |
| `MaxSteps` | Max steps per ray (stop condition) |
| `OPLInterval` | Optical path length interval (alternative to time step) |
| `StopCondition` | Custom termination condition expression |

---

## 6. Mesh Guidelines (Ray Optics)

Ray Optics mesh is **not wavelength-dependent** (unlike RF). Mesh only needs to resolve geometry curvature:

| Region | Mesh Guidance |
|--------|--------------|
| Curved surfaces | Curvature factor ≤ 0.3 |
| Flat surfaces | Coarse mesh acceptable |
| Discretization error | Larger mesh → more ray-geometry intersection error |
| Imported CAD mesh | Direct ray tracing on surface mesh possible |

---

## 7. mph API Usage — Working Examples

### 7.1 Ray Optics

```python
gop = comp.physics().create('gop', 'GeometricalOptics', 'geom1')

# Set medium refractive index
mp = gop.feature('mp1')  # Medium Properties (default)
mp.set('RefractiveIndex', '1.5')  # n = 1.5

# Release rays from a boundary
rel = gop.feature().create('rel1', 'ReleaseFromBoundary', 1)
rel.selection().set([input_bnd])
rel.set('Nx', '100')
rel.set('Ny', '100')
rel.set('VacuumWavelength', '550[nm]')

# Add a mirror wall
mirror = gop.feature().create('w1', 'Wall', 1)
mirror.selection().set([mirror_bnd])
mirror.set('WallCondition', 'Reflect')

# Ray Tracing study
study = jm.study().create('std1')
rt = study.feature().create('rt1', 'RayTracing')
rt.set('TimeStep', '1e-13[s]')
rt.set('MaxSteps', '1000')
```

### 7.2 Wave Optics

```python
ewfd = comp.physics().create('ewfd', 'ElectromagneticWaves', 'geom1')

# Set Sellmeier dispersion for silica
we = ewfd.feature('we1')
# (Set material via Materials node, then "From material")

# Beam Envelopes
ewbe = comp.physics().create('ewbe', 'ElectromagneticWavesBeamEnvelopes', 'geom1')
ewbe.set('WaveVector', 'ewbe.beta0 0 0')  # Propagation along x
```

---

## 8. COMSOL 6.4 Specific Notes

- **Ray Optics**: Uses `RayTracing` study step (not `Stationary`); rays are advanced time-step by time-step
- **Bidirectional coupling**: Requires `BidirectionallyCoupledRayTracing` study step; solves physics ↔ rays iteratively
- **Interference Pattern plot**: Available only when OPL auxiliary variable is enabled
- **Spot Diagram**: Automatically finds focal plane via minimum RMS spot size
- **Ray index** (`gop.ri`): Unique integer for each ray — useful for filtering in postprocessing
- **Beam Envelope**: Much coarser mesh than full-wave; mesh only needs to resolve envelope variation, not carrier wavelength
- **Grating efficiency**: COMSOL automatically splits ray into diffraction orders with computed efficiencies
- **Stokes parameters**: S₀ (total intensity), S₁ (horizontal vs vertical), S₂ (45° vs -45°), S₃ (circular)
