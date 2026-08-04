# Lessons Learned — Scheme 1 MXene/BaTiO3 RVE Model

Complete compilation of all issues encountered and solved during the build of a 2D axisymmetric piezoelectric RVE model in COMSOL 6.4 via mph.

## 1. Geometry

### 1.1 2D Axisymmetric: Circles at r=0 Become Spheres
- A circle centered at (r=0, z=z0) in the 2D axisymmetric plane represents a **sphere** after revolution around z-axis
- A circle NOT at r=0 represents a **torus** (ring), NOT a sphere
- For spherical nanoparticles on the symmetry axis, the circle MUST be at r=0

### 1.2 Semicircle + Boolean Difference = Unmeshable
- Creating semicircles (angle=180deg) and using Boolean Difference to embed them in a rectangle produces geometry that COMSOL's FreeTri mesher cannot triangulate
- Symptoms: mesh.run() succeeds, getNumElem() = 0, no error messages
- Root cause: flat edge at r=0 combined with narrow 5nm gaps creates degenerate topology
- Solution: Use full circles at r=0; COMSOL creates r<0 domains that can be excluded from physics

### 1.3 Domain Mapping with Unit Expressions
- `geom.lengthUnit('nm')` sets display unit but COMSOL internally uses SI (meters)
- Box selections for domain/boundary detection MUST use COMSOL expressions with units, not raw floats
- `sel.set('xmin', '0[nm]')` ← CORRECT
- `sel.set('xmin', str(0.0))` → interpreted as 0 meters not 0 nm ← WRONG when lengthUnit is 'nm'
- Parameter names like `'R_rve/2'` or `'100[nm]'` work correctly

### 1.4 Domain Splitting with Full Circles
- Full circles at r=0 in 2D automatically split by Form Union into r>=0 and r<0 halves
- r<0 domains must be excluded from ALL physics (both Solid Mechanics and Electrostatics)
- Typical result: N BTO particles → 3*N+2 domains (N valid BTO + N invalid BTO + GCE + MXene)

## 2. Materials

### 2.1 Flat Arrays Use Column-Major Order
- `pmat.set('dET', array)` reads the array in **column-major (Fortran) order**
- For M×N matrix: `array[col * M + row] = matrix[row][col]`
- Row-major arrays produce all entries in wrong positions
- Verification: check key positions like [0,0], [2,2], [3,3] after getStringArray()

### 2.2 Mode Must Be Set Before Value for Scalar Properties
- `rho_mat` must be set to `'userdef'` BEFORE setting `rho`
- Same for `E_mat`, `nu_mat` on LinearElasticModel nodes
- Default mode is `'from_mat'` — values set without changing mode are silently ignored
- `from_mat` reads from Materials node; if no Materials node exists, values are empty

### 2.3 Strain-Charge vs Stress-Charge Form
- StrainCharge form uses: **sE (compliance)** + **dET (d-matrix)** + **epsilonrS (clamped permittivity)**
- StressCharge form uses: **cE (stiffness)** + **eES (e-matrix)** + **epsilonrS**
- StrainCharge requires cE to be `from_mat` and sE to be `userdef` (can't have both active)
- Property name is `ConstitutiveRelation` (camelCase), value is `'StrainCharge'` or `'StressCharge'`

### 2.4 Permittivity Property Names
- Correct: `epsilonrS_mat` and `epsilonrS` (for clamped permittivity)
- Wrong: `epsS_mat`, `epsS11`, `epsS33` (these are scalar accessors, not matrix properties)

### 2.5 Feature Type Names for COMSOL 6.4
- Linear elastic domain: `'LinearElasticModel'` (NOT `'LinearElasticMaterial'`)
- Piezoelectric domain: `'PiezoelectricMaterialModel'` (correct)
- Prescribed displacement BC: `'Displacement1'` (NOT `'Displacement'` or `'PrescribedDisplacement'`)
- Fixed constraint: `'Fixed'` (correct)

## 3. Boundary Conditions

### 3.1 Displacement1 BC
- Feature type: `'Displacement1'` with dim=1 (boundary)
- Set components via setIndex: `disp.setIndex('U0', '0', 0)` for r, `disp.setIndex('U0', '-Uz_app', 1)` for z
- In 2D axisymmetric: index 0 = r (radial), index 1 = z (axial)

### 3.2 FloatingPotential Causes Singular Matrix
- In pure piezo-electrostatic problems (no current, no external circuit), FloatingPotential adds a void equation for fp1.V0
- This makes the stiffness matrix singular → solver fails or produces -Inf
- Fix: Remove FloatingPotential entirely; Zero Charge (default) + Ground provides sufficient reference
- The piezo polarization charge D = e:epsilon is the field source

### 3.3 Ground Must Be in an ES Domain
- Ground boundary must belong to a domain that's included in the Electrostatics physics
- If the domain containing Ground is excluded from ES, the reference is lost → singular matrix

## 4. Solver

### 4.1 mph model.solve() vs Java study.run()
- `model.solve()` (mph) → rebuilds geometry and mesh, then solves → breaks GUI fixes
- `jm.study('std1').run()` → solves without rebuilding → preserves geometry but mph evaluate may fail
- For models built entirely via mph: use `model.solve()`
- For models modified in GUI: use `jm.study('std1').run()`, accept evaluation limitations

### 4.2 mph evaluate Limitations
- `model.evaluate()` returns -inf/nan/inf after Java API solve (jm.study().run())
- `model.evaluate()` returns correct values after `model.solve()`
- Point evaluation via `at3(r,z,expr)` may fail with FlException if dataset isn't properly set
- Workaround for GUI-modified models: solve in GUI, read results manually

### 4.3 Fully Coupled vs Segregated
- Piezoelectric problems may need Fully Coupled solver (not Segregated)
- If Segregated solver is used, the piezo coupling step may be skipped
- Direct solver (MUMPS/PARDISO) recommended for small models

## 5. Results & Extraction

### 5.1 Always Verify in GUI First
- Before running parameter sweeps, solve once in COMSOL GUI
- Check: maxop1(es.V) ≠ 0, strain energy > 0, stress field is non-zero
- If these fail in GUI, sweeps will also fail

### 5.2 Save Versioned Files
- Save model at each pipeline stage: build, baseline, sweep
- Use timestamps in filenames to track iterations
- Keep a `_latest.mph` symlink for pipeline scripts

## 6. Process

### 6.1 Pipeline Order
```
01_design/          ← Research, parameters, geometry spec
02_build_model.py   ← Build complete mph model  
03_baseline.py      ← Solve + verify + extract baseline
04_sweep.py         ← Multi-phase parameter sweep
05_extract.py       ← Unit conversion + data structuring
06_process.py       ← Fitting + statistics + analysis
07_plot.py          ← Publication figures
```

### 6.2 Design Before Building
- Research all material parameters from literature (NOT estimates)
- Document sources for every numerical value
- Design geometry on paper/schematic before coding
- Enumerate all domains and boundaries with expected numbering
- List all boundary conditions with physical justification

### 6.3 Incremental Verification
- After each build step, verify the model structure (domain count, boundary types, BC assignments)
- Solve baseline and check key metrics before running sweeps
- For multiphysics: verify each physics works independently before coupling
