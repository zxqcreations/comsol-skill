# Mathematics Module — Comprehensive API Reference

COMSOL 6.4 · mph Python API · Based on COMSOL Multiphysics Users Guide (PDE Interfaces chapter) and tags.json

---

## 1. PDE Interfaces Overview

The Mathematics branch provides equation-based modeling without predefined physics:

| Interface | mph Tag | Default | Description |
|-----------|---------|---------|-------------|
| Coefficient Form PDE | `c` | `c` | Most common: −∇·(c∇u) + β·∇u + au = f |
| General Form PDE | `g` | `g` | Conservative: ∇·Γ = F with Γ = −c∇u − αu + γ |
| Weak Form PDE | `w` | `w` | User-defined weak: ∫(test(u)·F − ∇test(u)·Γ)dV = 0 |
| ODE/DAE | `ode` | `ode` | Global ODEs (no spatial derivatives) |
| Distributed ODE | `dode` | `dode` | ODE at each spatial point |
| Boundary ODE | `bode` | `bode` | ODE defined on boundaries only |
| Domain ODE | `dode2` | — | ODE within spatial domains |
| Optimization | `opt` | `opt` | Objective + constraint formulation |
| Sensitivity | `sens` | `sens` | Parameter sensitivity analysis |
| Shape Optimization | `shapeopt` | — | Free boundary optimization |
| Topology Optimization | `topoopt` | — | Material distribution optimization |

---

## 2. Coefficient Form PDE (c)

### 2.1 Governing Equation

eₐ∂²u/∂t² + dₐ∂u/∂t + ∇·(−c∇u − αu + γ) + β·∇u + au = f

| Coefficient | Symbol | Unit | Description |
|------------|--------|------|-------------|
| Diffusion | c | varies | Isotropic/Diagonal/Symmetric/Full tensor |
| Absorption | a | 1/m²·[u] | Sink term (Helmholtz: a = −k²) |
| Source | f | [u]/m³ | Source term |
| Damping/Mass | dₐ | [u]·s | Time-derivative coefficient |
| Conservative flux convection | α | — | Matrix for Γ convection |
| Conservative flux source | γ | [u]/m² | Vector source in flux |
| Convection | β | 1/m | Non-conservative convection |
| Mass acceleration | eₐ | [u]·s² | Wave equation term |

### 2.2 PDE Settings

| Setting | Values | Description |
|---------|--------|-------------|
| Dependent variables | u, u2, ... | Number of PDEs to solve |
| Units | User-specified | Dependent variable unit and source term unit |
| Discretization | `Linear`, `Quadratic`, `Cubic`, etc. | Shape function order |

### 2.3 Boundary Conditions

| BC | mph Type | Equation | Dim |
|----|---------|----------|-----|
| Dirichlet | `DirichletBoundaryCondition` | u = r | 1 |
| Flux/Source | `FluxBoundary` | −n·Γ = g − qu | 1 |
| Zero Flux | `ZeroFluxBoundary` | −n·Γ = 0 | 1 |
| Constraint | `Constraint` | General constraint | 1 |
| Periodic Condition | `PeriodicCondition` | u_src = u_dst | 1 |

**Flux BC properties**:

| Property | Description |
|----------|-------------|
| `g` | Boundary flux/source |
| `q` | Boundary absorption coefficient |

### 2.4 Initial Values

| Setting | Description |
|---------|-------------|
| u(t=0) | Initial value for dependent variable |
| ∂u/∂t(t=0) | Initial time derivative (eₐ > 0) |

### 2.5 Eigenvalue PDE

When used with Eigenvalue study, the PDE becomes:

∇·(c∇u) − au = λdₐu − λ²eₐu

Where λ is the eigenvalue. Set `a` for the desired spectral transformation.

---

## 3. General Form PDE (g)

### 3.1 Governing Equation

eₐ∂²u/∂t² + dₐ∂u/∂t + ∇·Γ = F

Where:
- Γ = −c∇u − αu + γ (conservative flux)
- F = f − β·∇u − au (source)

**Key difference from Coefficient Form**: Equations written in **conservative form** — better for nonlinear problems where flux continuity is critical.

### 3.2 Boundary Conditions

Same types as Coefficient Form, but Flux BC uses Γ directly:

| BC | mph Type | Equation |
|----|---------|----------|
| Dirichlet | `DirichletBoundaryCondition` | u = r |
| Flux | `FluxBoundary` | −n·Γ = g − qu |
| Zero Flux | `ZeroFluxBoundary` | −n·Γ = 0 |
| Constraint | `Constraint` | Any expression |

### 3.3 Conservative Flux Specification

| Component | Expression | Format |
|-----------|-----------|--------|
| Γ (flux vector) | −c∇u − αu + γ | Enter as components (Γx, Γy, Γz) |
| F (source) | f − β·∇u − au | Scalar expression |

---

## 4. Weak Form PDE (w)

### 4.1 Formulation

∫Ω (test(u)·F − ∇test(u)·Γ) dV + boundary terms = 0

Where `test(u)` is the test function for variable u.

### 4.2 Weak Expression

| Term | mph Property | Description |
|------|-------------|-------------|
| Weak contribution | `weak` | Domain integral expression |
| Boundary weak | — | Boundary integral (add as subnode) |
| Constraint | — | Pointwise constraints |
| Pointwise constraint | — | Lagrange multiplier enforcement |

### 4.3 Usage Pattern

```python
# Poisson equation: ∇²u = f → weak form: ∫(−∇v·∇u − v·f)dV = 0
w = comp.physics().create('w', 'WeakFormPDE', 'geom1')
w.set('weak', '-test(ux)*ux - test(uy)*uy - test(u)*f')
```

---

## 5. ODE/DAE Interfaces

### 5.1 Global ODEs and DAEs (ode)

| Interface | Scope | Variables | Purpose |
|-----------|-------|-----------|---------|
| Global ODEs/DAEs | Model-wide | Scalar ODE variables | Lumped parameter models |
| Domain ODEs | Per-domain | u(x,y,z,t) | ODE at each spatial point |
| Boundary ODEs | Per-boundary | u(t) on boundary | Surface reactions, circuits |
| Point ODEs | Per-point | u(t) at vertices | Lumped element attachment |

### 5.2 ODE Equation Format

eₐ·d²u/dt² + dₐ·du/dt = f(t,u)

| Coefficient | Purpose |
|------------|---------|
| `f` | Right-hand side (source) |
| `d_a` | Damping coefficient (multiplies du/dt) |
| `e_a` | Mass coefficient (multiplies d²u/dt²) |

### 5.3 DAE (Differential-Algebraic) Format

When `d_a = 0` for some equations, the system becomes a DAE:

f(t,u,v) = 0  (algebraic constraint)
dₐ·dv/dt = g(t,u,v)  (differential equation)

COMSOL automatically detects DAE structure and applies consistent initialization.

### 5.4 Initial Conditions

| Setting | For |
|---------|-----|
| `u(t0)` | Initial value of variable (all ODEs/DAEs) |
| `du/dt(t0)` | Initial derivative (2nd-order ODEs only) |

---

## 6. Optimization Interfaces

### 6.1 Optimization (opt)

| Feature | mph Type | Purpose |
|---------|---------|---------|
| Objective | `Objective` | Quantity to minimize/maximize |
| Control Variable | `ControlVariable` | Parameter to optimize |
| Constraint | `Constraint` | Equality/inequality constraint |

**Objective types**:

| Type | Description |
|------|-------------|
| Integral objective | ∫f(u)dV — minimize total quantity |
| Point objective | f at a specific point |
| Global objective | Single scalar from Global Evaluation |
| Least-squares | Σ(yᵢ − yᵢ_target)²/N |

### 6.2 Sensitivity (sens)

Computes df/dp for objective f with respect to parameter p.

**Methods**: Forward (direct), Adjoint (efficient for many parameters)

### 6.3 Shape Optimization

Optimizes the shape of boundaries to minimize an objective subject to PDE constraints. Uses free boundary displacement as control.

### 6.4 Topology Optimization

Optimizes material distribution (density ρ ∈ [0,1]) in a design domain. Uses SIMP (Solid Isotropic Material with Penalization) or level-set methods.

---

## 7. Expression Reference

### 7.1 PDE Variables (`c.*`, `g.*`, `w.*`)

| Expression | Description |
|-----------|-------------|
| `c.u` | Dependent variable (Coefficient Form) |
| `c.ux`, `c.uy`, `c.uz` | Spatial derivatives |
| `c.uxx`, `c.uyy`, `c.uzz` | Second derivatives |
| `c.ut` | Time derivative |
| `c.utt` | Second time derivative |
| `g.u`, `g.ux`, etc. | Same for General Form |
| `w.u`, `w.ux`, etc. | Same for Weak Form |

### 7.2 ODE Variables (`ode.*`)

| Expression | Description |
|-----------|-------------|
| `ode.u1`, `ode.u2` | ODE variables |
| `ode.ut1` | Time derivative |
| `ode.utt1` | Second derivative |

### 7.3 Optimization (`opt.*`)

| Expression | Description |
|-----------|-------------|
| `opt.obj` | Objective value |
| `opt.sens_<param>` | Sensitivity w.r.t. parameter |

---

## 8. mph API Usage

### Coefficient Form PDE

```python
c = comp.physics().create('c', 'CoefficientFormPDE', 'geom1')
c.selection().all()
c.set('c', '1')       # Diffusion coefficient = 1
c.set('a', '0')       # Absorption = 0
c.set('f', '1')       # Source = 1
c.set('da', '0')      # No damping
c.set('ea', '0')      # No mass term

# Dirichlet BC: u = 0 at boundary
dirichlet = c.feature().create('dir1', 'DirichletBoundaryCondition', 1)
dirichlet.selection().set([bnd])
dirichlet.set('r', '0')

# Flux BC: −n·Γ = 1
flux = c.feature().create('flux1', 'FluxBoundary', 1)
flux.set('g', '1')
```

### ODE

```python
ode = comp.physics().create('ode1', 'GlobalEquations')
ode.set('u1_init', '0')
ode.set('f_1', 'sin(2*pi*1[Hz]*t)')  # f(t,u) RHS
ode.set('da_1', '1')                   # du/dt coefficient
```

---

## 9. COMSOL 6.4 Specific Notes

- **PDE unit handling**: COMSOL requires consistent units; set `Dependent variable unit` and `Source term unit` in PDE Settings
- **Eigenvalue PDE**: Use `Eigenvalue` study; a = −λ² for Helmholtz (eₐ=0, dₐ=0), or a = 0 for diffusion eigenmodes
- **Weak form integration**: Use `test(u)` notation; COMSOL automatically handles integration by parts
- **DAE initialization**: For DAEs, COMSOL uses consistent initialization; may require `Initial Values` study step first
- **Optimization solver**: Requires Optimization Module license; uses SNOPT, MMA, or IPOPT
- **Shape optimization**: Mesh deformation via ALE (Arbitrary Lagrangian-Eulerian) — geometry must be parameterized
- **Topology optimization**: HELMholtz filter for mesh-independence; projection for 0/1 designs
