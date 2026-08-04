# COMSOL Troubleshooting Guide

## Solver Issues

### es.V = -Inf (Potential Unbounded)

**Symptoms**: maxop1(es.V) returns -Infinity, minop1(es.V) returns Infinity

**Root Causes** (in order of likelihood):
1. **Electrostatics physics doesn't include the domain containing Ground** → Ground is isolated, no potential reference
2. **FloatingPotential on a boundary in pure piezo-ES** → Adds void equation, singular matrix
3. **No Ground at all** → Potential undefined up to constant
4. **Materials node is empty** → from_mat properties resolve to zero

**Fix**: 
- Check ES domain selection includes all domains
- Remove FloatingPotential, rely on Zero Charge + Ground
- Ensure Ground boundary is in an ES-active domain

### solid.mises = 0 Everywhere

**Symptoms**: Stress field is zero despite applied displacement

**Root Causes**:
1. **Material properties are From material but Materials node is empty/missing**
2. **E/nu mode not switched to User defined** (values silently ignored)
3. **Fixed constraint not on correct boundary** (rigid body motion suppressed by something else)
4. **Displacement BC not on correct boundary** (no load applied)
5. **Both sE and cE are User defined simultaneously** (conflicting stiffness definitions)

**Fix**: 
- Check E, nu, rho are User defined (not From material)
- Verify BCs are on correct boundary numbers
- Ensure only ONE of {cE, sE} is User defined

### Mesh: 0 Elements (No Error)

**Symptoms**: mesh.run() completes, getNumElem() = 0, no error messages

**Root Causes**:
1. **Semicircle + Boolean Difference geometry** → FreeTri can't triangulate
2. **Extremely narrow gaps** (< 1nm) with mesh sizes too large
3. **Overlapping geometry entities**

**Fix**:
- Use full circles (not semicircles) at r=0 in axisymmetric models
- Exclude r<0 domains from physics instead
- Set minimum element size < gap size
- Set "Resolution of narrow regions" >= 2

### Matrix Entries Wrong in GUI

**Symptoms**: d-matrix shows values in wrong positions

**Root Cause**: Flat arrays passed to `set(name, array)` are interpreted in column-major (Fortran) order, not row-major

**Fix**: Rearrange arrays to column-major: `array[col*M + row] = matrix[row][col]`

### "Matrix item is not a scalar" Error

**Symptoms**: setIndex() calls with string expressions fail

**Root Cause**: COMSOL 6.4 expression compiler rejects string expressions for matrix entries via setIndex()

**Fix**: Use `pmat.set(name, flat_array)` instead of `pmat.setIndex(name, value, row, col)`

## Physics Issues

### No Piezoelectric Response

**Symptoms**: Mechanical solution works (non-zero stress) but V = 0 everywhere

**Root Causes**:
1. **d-matrix or e-matrix is all zeros** (not filled or filled incorrectly)
2. **Piezoelectric Effect multiphysics not created** or not referencing correct physics
3. **Charge Conservation Piezo not on BTO domains**
4. **Constitutive relation mismatch** (StrainCharge with eES, or StressCharge with dET)

### Study Not Found by mph

**Symptoms**: `model.solve('std1')` says "Study does not exist"

**Root Cause**: mph's internal state doesn't know about studies created via Java API

**Fix**: Use `model.solve()` without study name (auto-detects), or use `jm.study('std1').run()`

## API Issues

### Property Value Silently Ignored

**Symptoms**: Setting `rho`, `E`, `nu` etc. via mph but GUI shows default values

**Root Cause**: Property mode is `from_mat` (default); values set without changing mode are ignored

**Fix**: Always set mode first: `pmat.set('rho_mat', 'userdef')` then `pmat.set('rho', value)`

### model.evaluate() Returns Empty Array

**Symptoms**: `model.evaluate(expr, unit)` returns `[]`

**Root Cause**: Mesh has 0 elements; solution is empty

**Fix**: Fix the mesh first (see Mesh section above)

### COMSOL Expression Needs Units

**Symptoms**: Box selections find wrong entities or nothing

**Root Cause**: geometry.lengthUnit('nm') requires COMSOL expressions with units; raw floats interpreted as meters

**Fix**: Use `'100[nm]'` or parameter names like `'R_rve/2'`, never `str(float_value)` without units
