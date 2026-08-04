# mph Python API Reference (COMSOL 6.4)

Complete mph API for COMSOL 6.4 automation, extracted from mph source code and verified through extensive testing.

## Session Management

```python
import mph

# Start local COMSOL session
client = mph.start(cores=4)          # Start with N cores
client = mph.Client()                # Connect to running session
client.version                       # '6.4'
client.cores                         # Number of cores

# Model management
model = client.create('model_name')  # Create new model
model = client.load('path.mph')      # Load existing model
model.save('path.mph')               # Save model
model.clear()                        # Clear solution data
client.remove('model_name')          # Remove model from memory

# Java API access
jm = model.java                      # Direct Java API access
comp = jm.component('comp1')         # Access component
```

## Parameters

```python
jm = model.java

# Set parameter (always include units)
jm.param().set('Uz_app', '50e-9[m]', 'Applied z-displacement')
jm.param().set('E_MX', '483.5[GPa]', 'MXene Young modulus')
jm.param().set('nu_MX', '0.20', 'MXene Poisson ratio')

# Get parameter
val = jm.param().get('Uz_app')       # Returns expression string
# Read via mph
val = model.evaluate('Uz_app', None)  # Returns float
```

## Geometry (2D Axisymmetric)

```python
comp = jm.component().create('comp1', True)
geom = comp.geom().create('geom1', 2)     # 2 = 2D
geom.label('Geometry (2D Axisymmetric)')
geom.axisymmetric(True)                   # Enable axisymmetry
geom.lengthUnit('nm')                     # Display unit

# Primitives
rect = geom.feature().create('r1', 'Rectangle')
rect.set('size', ['250[nm]', '500[nm]'])
rect.set('pos', ['0', '0'])

circle = geom.feature().create('c1', 'Circle')
circle.set('r', '50[nm]')
circle.set('pos', ['0', '250[nm]'])

# Boolean operations
diff = geom.feature().create('dif1', 'Difference')
diff.set('input', 'r1')
diff.set('input2', ['c1'])

# Build
geom.run()
nd = int(geom.getNDomains())
nb = int(geom.getNBoundaries())

# Feature types available:
# Rectangle, Circle, Polygon, BezierPolygon, ParametricCurve,
# Block, Cylinder, Sphere, Cone, Ellipse, Point,
# Union, Difference, Intersection, Array, Copy, Delete, Chamfer, Fillet
```

## Domain/Boundary Detection

```python
# Use COMSOL unit expressions in Box selections (CRITICAL with lengthUnit('nm'))
eps = '0.001[nm]'

def find_entity(comp, x_expr, y_expr, entity_dim):
    sel = comp.selection().create('_tmp', 'Box')
    sel.geom('geom1', entity_dim)   # 1=boundary, 2=domain
    sel.set('xmin', f'({x_expr}) - ({eps})')
    sel.set('xmax', f'({x_expr}) + ({eps})')
    sel.set('ymin', f'({y_expr}) - ({eps})')
    sel.set('ymax', f'({y_expr}) + ({eps})')
    sel.set('condition', 'intersects')
    entities = list(sel.entities())
    comp.selection().remove('_tmp')
    return [int(e) for e in entities]

# Find bottom boundary (z=0, mid-r):
bottom = find_entity(comp, 'R_rve/2', '0[nm]', 1)        # Returns [2]

# Find top boundary (z=H):
top = find_entity(comp, 'R_rve/2', '400[nm]', 1)          # Returns [14]

# Find BTO domain (near axis):
bto = find_entity(comp, '5[nm]', '200[nm]', 2)            # Returns [3]
```

## Solid Mechanics Physics

```python
solid = comp.physics().create('solid', 'SolidMechanics', 'geom1')
solid.label('Solid Mechanics')
solid.selection().all()

# Domain features (verified working types):
#   LinearElasticModel, PiezoelectricMaterialModel,
#   ElastoplasticSoilMaterial, HyperelasticModel, etc.

# Linear Elastic Material
lemm = solid.feature('lemm1')          # Default node (auto-created)
lemm.label('Linear Elastic Material')
lemm.set('E', 'E_MX')                  # User defined values
lemm.set('nu', 'nu_MX')
lemm.set('rho', 'rho_MX')

# Additional Linear Elastic for another domain:
lemm2 = solid.feature().create('lemm_gce', 'LinearElasticModel', 2)
lemm2.selection().set([gce_dom])
lemm2.set('E', 'E_gce')
lemm2.set('nu', 'nu_gce')
```

## Piezoelectric Material (Strain-Charge)

```python
pmat = solid.feature().create('pmat1', 'PiezoelectricMaterialModel', 2)
pmat.selection().set([bto_dom])
pmat.label('BaTiO3 (Piezo, 4mm)')

# 1. Constitutive relation
pmat.set('ConstitutiveRelation', 'StrainCharge')

# 2. Compliance matrix sE (6x6, column-major flat array)
pmat.set('sE_mat', 'userdef')
pmat.set('sE', _SE_CM_FLAT)  # 36-element column-major array

# 3. Coupling matrix dET (3x6, column-major flat array)
pmat.set('dET_mat', 'userdef')
pmat.set('dET', _DET_CM_FLAT)  # 18-element column-major array

# 4. Permittivity epsilonrS (3x3, column-major flat array)
pmat.set('epsilonrS_mat', 'userdef')
pmat.set('epsilonrS', _EPSR_CM_FLAT)  # 9-element column-major array

# 5. Density (CRITICAL: set mode BEFORE value!)
pmat.set('rho_mat', 'userdef')
pmat.set('rho', 'rho_BTO')

# 6. Disable unused matrices
pmat.set('cE_mat', 'from_mat')  # Don't use cE with StrainCharge
pmat.set('eES_mat', 'from_mat')  # Don't use eES with StrainCharge

# Boundary condition types (verified working):
#   Fixed ('fix1', 1), Displacement1 ('disp1', 1), Free ('free1', 1)
#   BoundaryLoad, Roller, Symmetry, AxialSymmetry

fix = solid.feature().create('fix1', 'Fixed', 1)
fix.selection().set([bottom_bnd])
fix.label('Fixed (z=0)')

disp = solid.feature().create('disp1', 'Displacement1', 1)
disp.selection().set([top_bnd])
disp.setIndex('U0', '0', 0)         # u_r = 0
disp.setIndex('U0', '-Uz_app', 1)   # u_z = -Uz_app
```

## Electrostatics Physics

```python
es = comp.physics().create('es', 'Electrostatics', 'geom1')
es.label('Electrostatics')
es.selection().all()

# Charge Conservation Piezo (on BTO domains)
ccp = es.feature().create('ccp1', 'ChargeConservationPiezo', 2)
ccp.selection().set([bto_dom])

# Boundary condition types:
#   Ground, ElectricPotential, FloatingPotential, ZeroCharge,
#   SurfaceChargeDensity, Terminal, DomainTerminal

gnd = es.feature().create('gnd1', 'Ground', 1)
gnd.selection().set([bottom_bnd])
gnd.label('Ground (V=0)')
```

## Multiphysics Couplings

```python
# Piezoelectric Effect
pze = comp.multiphysics().create('pze1', 'PiezoelectricEffect', 2)
pze.set('Solid_physics', 'solid')
pze.set('Electrostatics_physics', 'es')
pze.label('Piezo Coupling (solid <-> es)')

# Other available types:
#   ThermalStress, JouleHeating, FluidStructureInteraction,
#   ElectromechanicalForces, ThermoelectricEffect
```

## Operators

```python
# Maximum, average, minimum over all domains
maxop = comp.cpl().create('maxop1', 'Maximum')
aveop = comp.cpl().create('aveop1', 'Average')
minop = comp.cpl().create('minop1', 'Minimum')

# Domain-specific integration
intop = comp.cpl().create('intop_BTO1', 'Integration')
intop.selection().set([bto_dom])

# Boundary-specific average
aveop_top = comp.cpl().create('aveop_top', 'Average')
aveop_top.selection().set([top_bnd])

# Usage in expressions:
#   maxop1(es.V)       -> maximum potential
#   intop_BTO1(solid.Ws) -> strain energy in BTO domain
#   aveop_top(es.Dz)     -> average D_z on top surface
```

## Mesh

```python
mesh = comp.mesh().create('mesh1')

# Free triangular (2D)
ftri = mesh.create('ftri1', 'FreeTri')
ftri.selection().geom('geom1', 2)

# Domain-specific sizing
sz = mesh.feature().create('sz_bto', 'Size')
sz.selection().geom('geom1', 2)
sz.selection().set([bto_dom])
sz.set('hmax', '5[nm]')
sz.set('hmin', '1[nm]')

# Edge sizing for narrow gaps
sz_gap = mesh.feature().create('sz_gap', 'Size')
sz_gap.selection().geom('geom1', 1)  # 1D entity (edge)
sz_gap.selection().set([gap_bnd])
sz_gap.set('hmax', '2[nm]')

# Build
mesh.run()
ne = mesh.getNumElem()  # Check element count
```

## Study

```python
std = jm.study().create('std1')
std.feature().create('stat1', 'Stationary')
std.label('Study 1 (Stationary)')

# Available study types:
#   Stationary, TimeDependent, Frequency, Eigenfrequency,
#   Perturbation, Parametric

# Solve with mph (RECOMMENDED — avoids dataset issues):
model.solve()
# OR: model.solve('std1')

# Solve via Java (use only if mph solve fails):
jm.study('std1').run()
```

## Results Evaluation

```python
# After model.solve():
val = model.evaluate('maxop1(es.V)', 'mV')          # Returns float
vals = model.evaluate(['es.V', 'solid.mises'])       # Returns arrays
point = model.evaluate('at3(0,200e-9,es.V)', 'mV')  # Point evaluation

# Export images:
jm.result().export().create('_img', 'Image')
# ... (complex API, prefer MCP results_export_image)

# Save solved model:
model.save('model_solved.mph')
```

## Known Issues & Workarounds

### setIndex fails for matrix entries
```python
# ❌ setIndex('dET', '564[pC/N]', 0, 4) -> "not a scalar"
# ✅ pmat.set('dET', column_major_flat_array)
```

### model.evaluate returns -inf after Java solve
```python
# ❌ jm.study('std1').run(); model.evaluate(...) -> -inf
# ✅ model.solve(); model.evaluate(...) -> correct value
```

### model.solve() rebuilds geometry
```python
# model.solve() internally calls model.build() + model.mesh() + solve
# This can overwrite GUI modifications to geometry
# Workaround: Use jm.study('std1').run() and accept evaluate limitations
```

### FloatingPotential singular matrix
```python
# FloatingPotential adds void equation fp1.V0 in pure piezo-ES
# Fix: Don't create FP, use default Zero Charge + Ground
```

### Property values silently ignored
```python
# rho, E, nu etc. need *_mat='userdef' before value set
pmat.set('rho_mat', 'userdef')  # MUST come first
pmat.set('rho', 'rho_BTO')      # NOW takes effect
```
