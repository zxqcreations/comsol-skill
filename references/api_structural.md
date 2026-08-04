# Structural Mechanics Module — API Reference

Sources:
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Structural_Mechanics_Module\StructuralMechanicsModuleUsersGuide.pdf` (COMSOL 6.4, 2400 pp)
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Multibody_Dynamics_Module\MultibodyDynamicsModuleUsersGuide.pdf`
- `D:\ENV\COMSOL64\Multiphysics\doc\pdf\Rotordynamics_Module\RotordynamicsModuleUsersGuide.pdf`
- mph tags.json (feature type strings) + verified working code in `mph_api.md` / `lessons_learned.md`

Conventions used throughout:
- **Feature type string** = Java/model-tree node type, e.g. `LinearElasticModel`, used with
  `physics.feature().create(tag, 'TypeString', dim)` (mph) or `create(tag, type, dim)` (Java).
- **dim** = geometric entity dimension of the selection:
  `2` = domains (3D) / boundaries (2D) / edges (1D); `1` = boundaries (3D) / edges (2D) / points (1D); `0` = edges (3D)/points.
  Suffixed types encode this: `Displacement0` (domain), `Displacement1` (boundary), `Displacement2` (edge/point).
- **Property mode suffix `_mat`**: every material-linked scalar/matrix property has a companion
  mode property named `<prop>_mat` with values `from_mat` (default) | `userdef`. Set the mode
  BEFORE setting the value: `pmat.set('sE_mat','userdef'); pmat.set('sE', arr)`.
- **Matrix arrays** are always flat, **column-major (Fortran) order**.

---

## 1. Physics Interfaces — Tags, Dimensions, Studies

| Interface | Tag | Space dims | Notes |
|---|---|---|---|
| Solid Mechanics | `solid` | 3D, 2D, 2D axisym, 1D, 1D axisym | core interface; everything below applies |
| Solid Mechanics, Explicit Dynamics | `solte` (guide prints `solid`) | 3D, 2D, 2D axisym | explicit dynamics study |
| Shell | `shell` | 3D, 2D axisym | shell on boundaries |
| Plate | `plate` | 2D | shell on domains |
| Layered Shell | `lshell` (guide prints `shelll`) | 3D | layered composite |
| Membrane | `mbrn` | 3D, 2D axisym | |
| Beam | `beam` | 3D, 2D | |
| Beam Cross Section | `bcs` | 3D, 2D | computes section properties |
| Truss | `truss` | 3D, 2D | |
| Truss, Explicit Dynamics | `trexd` (guide prints `truss`) | 3D, 2D | |
| Wire | `wire` | 3D, 2D | |
| Pipe Mechanics | `pipem` | 3D, 2D | |
| Phase Field in Solids | `pfs` | 3D, 2D, 2D axisym | |
| Transport in Solids | `ts` | all dims | |
| Multibody Dynamics | `mbd` | 3D, 2D, 2D axisym | separate module |
| Joints | `jnt` | global | |
| Lumped Mechanical System | `lms` | global | |
| Solid Rotor | `rotsld` | 3D | Rotordynamics module |
| Solid Rotor, Fixed Frame | `rotsff` | 3D | |
| Beam Rotor | `rotbm` | 3D | |
| Hydrodynamic Bearing | `hdb` | 3D | |

Predefined multiphysics interfaces (add the physics + coupling automatically):
`Piezoelectricity, Solid` (solid + es + `PiezoelectricEffect`), `Piezoelectricity, Layered Shell`,
`Electrostriction`, `Ferroelectroelasticity`, `Piezomagnetism`, `Nonlinear Magnetostriction`,
`Magnetomechanics, Solid/Shell/Membrane`, `Thermal Stress, Solid/Shell/Membrane`, `Fluid–Solid Interaction`, ...

Study types (typical): stationary, eigenfrequency (+ prestressed), mode analysis, time dependent (+ modal,
modal ROM), frequency domain (+ prestressed, modal, AWE ROM), response spectrum, random vibration (PSD),
linear buckling, bolt pretension, inertia relief. Explicit dynamics for the `solte`/explicit interfaces.

---

## 2. Solid Mechanics Interface (`solid`)

Dependent variables: displacement `u` (u, v, w), velocity `du/dt`; optional pressure/volumetric strain (mixed formulation).

### 2.1 Domain material model nodes (dim=2, submenu Material Models)

| Node (UI) | Feature type string | Key properties / notes |
|---|---|---|
| Linear Elastic Material | `LinearElasticModel` | `MaterialModel` (Isotropic/Orthotropic/Anisotropic/Crystal), `E`, `nu`, `G`, `K`, `lambda`, `mu`, `cp`, `cs` (pairs via `Specify`), `rho`, `CoordinateSystem`, `UseMixedFormulation` (None/Pressure/Strain), `Formulation`, `StrainDecomposition` (Automatic/Additive/Logarithmic/Multiplicative) |
| Nonlinear Elastic Material | `NonlinearElasticModel` | |
| Elastoplastic Soil Material | `ElastoplasticSoilMaterial` | subnodes: `ExternalStress` |
| Hyperelastic Material | `HyperelasticModel` | `MaterialModel` (NeoHookean, MooneyRivlin, Ogden, ArrudaBoyce, etc.), subnodes: `ThermalExpansion`, `Viscoelasticity` |
| Shape Memory Alloy | `ShapeMemoryAlloy` | subnodes: `PhaseTransformationDirection`, `ThermalExpansion` |
| Piezoelectric Material | `PiezoelectricMaterialModel` | see Section 3 (full detail) |
| Piezomagnetic Material | `PiezomagneticMaterialModel` | cH/sH, dHT/eHS, murT/murS, rho |
| Magnetostrictive Material | `MagnetostrictiveModel` | |
| Rigid Material | `RigidDomain` | subnodes: `AppliedForce`, `AppliedMoment`, `MassInertia`, `PrescribedDispRot` (tag `pdr*`), `FixedConstraint`, `init`, `CenterOfRotationBnd/Edge/Point`, `SpringFoundation` |
| External Stress–Strain Relation | `ExternalStressStrainRelation` | external library material |

Subnodes attachable to material models (Attributes menu):
`ThermalExpansion` (for Materials), `HygroscopicSwelling`, `InitialStressandStrain`, `ExternalStress`,
`ExternalStrain`, `InelasticStrainRate`, `Damping`, `MechanicalDamping` (piezo), `CouplingLoss` (piezo),
`DielectricLoss` (piezo), `ConductionLoss` (piezo), `Viscoelasticity`, `Plasticity` (tag `plsty*`, subnode `SetVariables`),
`PressureDependentPlasticity`, `Creep`, `AdditionalCreep`, `Viscoplasticity`, `PolymerViscoplasticity`,
`PorousPlasticity`, `SoilModel`, `CapAndCutoff`, `Concrete` (tag `cm*`), `Rocks`, `Fiber`, `Damage`, `Activation`, `Safety`, `MullinsEffect`, `Annealing`, `IntercalationStrain`.

### 2.2 Domain-level nodes (dim=2)

| Node | Type string | Key properties |
|---|---|---|
| Initial Values | `init` | `U`, `U_t0` / displacement + velocity |
| Prescribed Displacement (domain) | `Displacement0` | `U0` vector; per-component Free/Prescribed/Limited; `kp` penalty; constraint method Penalty/AugmentedLagrangian |
| Prescribed Velocity | `Velocity` | `U0_t0` |
| Prescribed Acceleration | `Acceleration` | |
| Fixed Constraint (domain) | `Fixed` | zero displacement (and rotations) |
| Free | `Free` | removes constraints |
| Body Load | `BodyLoad` | `LoadType` (ForcePerReferenceVolume/ForcePerDeformedVolume/TotalForce/ForcePerReferenceArea/ForcePerDeformedArea), `F`/`fV`/`fv`/`Ftot`, `TreatAsDeadLoad` |
| Gravity | `Gravity` | `g` (default `g_const`), `grav_dir` (0/1/2) |
| Rotating Frame | `RotatingFrame` | `Omega` (angular velocity), axis definition |
| Linearly Accelerated Frame | `LinearlyAcceleratedFrame` | acceleration vector |
| Base Excitation | `BaseExcitation` | |
| Inertia Relief | `InertiaRelief` | |
| Change Thickness | `ChangeThickness` | `d` (2D, 1D axisym only) |
| Change Cross Section | `ChangeCrossSection` | `Ac` (1D only) |
| Added Mass | `AddedMass2` | |
| Spring Foundation (domain) | `SpringFoundation0` | `ks` stiffness, `cs` damping |
| Spring–Damper (points) | `SpringDamper` (tag `spd*`) | `k`, `c`; subnodes `SourcePoint`/`DestinationPoint` |
| Elastic Predeformation | `ElasticPredeformation` | |
| Test Material | `TestMaterial` | |
| Section Forces | `SectionForces` | |
| Stress Linearization | `StressLinearization` | |

### 2.3 Boundary nodes (dim=1)

| Node | Type string | Key properties |
|---|---|---|
| Fixed Constraint | `Fixed` | |
| Prescribed Displacement | `Displacement1` | `U0` (setIndex per component), Free/Prescribed/Limited, `kp` |
| Prescribed Velocity | `Velocity` | |
| Prescribed Acceleration | `Acceleration` | |
| Thermal Expansion (for Constraints) | `ThermalExpansionConstraint` | subnode of Fixed/Displacement |
| Roller | `Roller` | `NormalOrientation` (Automatic/Plane/Cylinder/Sphere) |
| Symmetry | `SymmetrySolid` (tag `sym*`) | free in-plane, fixed normal |
| Symmetry Plane (2D axisym) | `SymmetryPlane` | |
| Antisymmetry | `Antisymmetry` | |
| Rigid Motion Suppression | `RigidMotionSuppression` | 3 orthogonal constraints |
| Boundary Load | `BoundaryLoad` | `LoadType` (ForcePerReferenceArea/ForcePerDeformedArea/TotalForce/Pressure/Resultant), `FA`/`fa`/`Ftot`/`p`/`F`,`M`; subnode `Phase` (tag `ph*`); `HarmonicPerturbation`; `TreatAsDeadLoad` |
| Edge Load (3D) | `EdgeLoad` | `LoadType` (ForcePerReferenceLength/ForcePerDeformedLength/TotalForce), `fL`/`fl`/`Ftot` |
| Point Load | `PointLoad` | `Fp`/`Ftot`/Resultant (F, M); subnode `Phase` |
| Point Load, Free | `PointLoadFree` | point load on a point of a free domain (2D/3D) |
| Point Load (on Axis) | `PointLoadOnAxis` | 2D axisym |
| Ring Load / Ring Load, Free | `RingLoad` / `RingLoadFree` | 2D axisym |
| Spring Foundation | `SpringFoundation1` | `ks`, `cs`, `xf`, `yf` (anchor), `SpringBase` (Absolute/Relative) |
| Thin Elastic Layer | `ThinElasticLayer` | `ks`, `cs`, `thickness` |
| Predeformation | `PreDeformation` (subnode of SpringFoundation) | `U0` |
| Spring–Damper | `SpringDamper` | source/destination points |
| Point Mass | `PointMass` | `M` |
| Added Mass | `AddedMass2` | |
| Periodic Condition | `PeriodicCondition` | destination selection, `PeriodicType` |
| Cell Periodicity | `CellPeriodicity` | subnode `BoundaryPair` (tag `bp*`) |
| Low-Reflecting Boundary | `LowReflectingBoundary` | damping to absorb waves |
| Continuity | `Continuity` | continuity between mesh vertices |
| Boundary Pair | `BoundaryPair` | |
| Contact (pair) | `SolidContact` (tag `cnt*`) | subnodes `Friction` (tag `fric*`), `Adhesion`, `Decohesion`, `Wear`, `FrictionSlipVelocity` (tag `sv*`), `Free`; contact methods penalty/augmented Lagrangian/Nitsche |
| Interior Contact | `SolidContact` on interior boundary | |
| General Contact | `GeneralContact` | subnodes `ContactModel`, `NoContact`, `Offset`, `Damping`, `Friction`, `Stabilization` |
| Bolt Pretension | `BoltPrestress` (tag `pblt*`) | subnode `BoltSelection` (tag `sblt*`) |
| Bolt Thread Contact | `BoltThreadContact` | subnode `ThreadBoundarySelection` |
| Crack | `Crack` | subnodes `CrackFaceLoad` (tag `fl*`), `JIntegral` (tag `jint*`), `CrackClosure`, `ReverseCrackFront`, `VirtualCrackExtension` |
| Enclosed Cavity | `EnclosedCavity` | subnodes `Fluid`, `PrescribedPressure`, `Filter` |
| Fasteners | `Fasteners` | subnodes `HoleSelection`, `Safety` |
| Port | `Port` | acoustic-structure coupling |
| Rigid Connector | `RigidConnector` | ConnectionType (Rigid/Flexible); subnodes `RigidBodyForce` (rf*), `RigidBodyMoment` (rm*), `RigidBodyMassInertia` (rmm*), `SpringFoundation`, `CenterOfRotationBnd/Edge/Point`, `ThermalExpansion` |
| Attachment | `Attachment` | ConnectionType Rigid/Flexible; subnode `ThermalExpansion`; for joints in Multibody |
| Reduced Flexible Components | `ReducedFlexibleComponents` | subnodes `ComponentDefinition`, `FixedJoint`, `SourceFilter`, `DestinationFilter` |
| Thin Layer (on boundary) | `ThinLayer` | subnodes `Fiber`, `PrescribedDisplacement`, `FixedConstraint`, `Roller`, `FaceLoad`, `BoundaryLoad`, `SpringMaterial` (with `Damping`) |
| Adiabatic Heating | `AdiabaticHeating` | thermoelastic heating |
| External Stress/Strain, Hygroscopic Swelling, Thermal Expansion (for Materials) | as subnodes of material models | |

### 2.4 Edge / Point nodes (dim=0)

- Edge (3D): `EdgeLoad`, `Fixed`, `Displacement2`, `Velocity`, `Free`, `Symmetry`, `Antisymmetry`, `RigidConnector` (edge level), `SpringDamper`, `PointMass`, `EdgeGroup`, `Section Orientation` (Beam).
- Point: `PointLoad`, `PointLoadFree`, `RingLoad`/`RingLoadFree`, `Fixed`, `Displacement2` (as `PointConstraint`), `Free`, `PointMass`, `SpringDamper` (with `SourcePoint`/`DestinationPoint`), `RigidConnector` (point level), `Attachment` (Beam).

### 2.5 Global nodes

`HarmonicPerturbation` (harmonic load scaling), `GlobalEquations` (tag `ge*`), `GlobalConstraint` (tag `gconstr*`),
`AverageRotation` (tag `avgr*`, subnodes `CenterOfRotationBnd/Dom/Edge/Point`), `Warpage`, `WaveSpeeds`, `Discretization`.

### 2.6 Interface-level properties (Solid Mechanics node)

`Thickness` (`d`, used in 2D/1D axisym), `CrossSectionArea` (`Ac`, 1D), `PlaneStress` (2D), `AnalysisType`,
`Discretization` (shape order: 1st/2nd order Lagrange/Serendipity), `GeometricNonlinearity` (per study step),
`ReferenceTemperature` (`Tref`), Energy Dissipation settings.

---

## 3. Piezoelectric Material Model — Full Detail

Node: **Piezoelectric Material**, type string `PiezoelectricMaterialModel` (tag prefix `pzm*`).
Available in `solid` for 3D, 2D, 2D axisymmetry (NOT 1D); also in Layered Shell (`lshell`, same type string)
and as `PiezoelectricMaterialModelLayered` ("Piezoelectric Material, Layered") in the Shell interface.
Requires Structural Mechanics Module, MEMS Module, or Acoustics Module. Added automatically by the
`Piezoelectricity, Solid` multiphysics interface together with `ChargeConservationPiezo` in Electrostatics.

### 3.1 Constitutive relations

Property `ConstitutiveRelation`: `'StressCharge'` | `'StrainCharge'` (UI: Stress–charge form / Strain–charge form).

In structural mechanics notation (strain = ε, stress = σ):

- **Stress–charge**:  σ = cE·ε − eT·E ;  D = e·ε + ε₀·εrS·E
- **Strain–charge**:  ε = sE·σ + dT·E ;  D = d·σ + ε₀·εrT·E

The stress–charge form is always used internally in the weak form; strain–charge data is transformed:
- cE = (sE)⁻¹
- e = d·(sE)⁻¹
- εrS = εrT − d·(sE)⁻¹·dT / ε₀vac

Classical notation (piezo theory): S strain, T stress, E electric field, D electric displacement.

### 3.2 Property names and matrix dimensions

| Property | Size | Meaning | Used with |
|---|---|---|---|
| `cE` | 6×6 | Elasticity (stiffness) matrix, Voigt | StressCharge |
| `sE` | 6×6 | Compliance matrix, Voigt | StrainCharge |
| `eES` | 6×3 | Coupling matrix e (stress form) | StressCharge |
| `dET` | 3×6 | Coupling matrix d (charge form) | StrainCharge |
| `epsilonrS` | 3×3 | Relative permittivity at constant strain (clamped) | both |
| `epsilonrT` | 3×3 | Relative permittivity at constant stress | StrainCharge variant |
| `Dr` | 3-vector | Remanent electric displacement | both |
| `rho` | scalar | Density | both |

- `cE` and `sE` are 6×6; coupling `eES` is 6×3 (rows = stress components, cols = E components), `dET` is 3×6;
  permittivity `epsilonrS`/`epsilonrT` are 3×3 (symmetric).
- Coupling tensor reduction: e.g. eₑₓᵢ (tensor eᵢₖₗ): first index kept, last two replaced by a single Voigt index → 6×3 matrix.
- For `dET` (18 entries) and `epsilonrS` (9 entries), pass flat arrays in **column-major order** (verified: mph `set` reads Fortran order).

**Property mode suffixes `_mat`** (mode property, values `from_mat` | `userdef`):
`cE_mat`, `sE_mat`, `eES_mat`, `dET_mat`, `epsilonrS_mat`, `epsilonrT_mat`, `Dr_mat`, `rho_mat`.
Set mode first, then value:
```python
pmat = solid.feature().create('pmat1', 'PiezoelectricMaterialModel', 2)
pmat.selection().set([bto_dom])
pmat.set('ConstitutiveRelation', 'StrainCharge')
pmat.set('sE_mat', 'userdef');  pmat.set('sE', se_flat_36)     # column-major
pmat.set('dET_mat', 'userdef'); pmat.set('dET', det_flat_18)   # column-major
pmat.set('epsilonrS_mat', 'userdef'); pmat.set('epsilonrS', eps_flat_9)
pmat.set('rho_mat', 'userdef');  pmat.set('rho', 'rho_BTO')
pmat.set('cE_mat', 'from_mat')   # disable unused matrix in StrainCharge
pmat.set('eES_mat', 'from_mat')
```

### 3.3 Voigt notation ordering

Piezoelectric data uses the Voigt (abbreviated subscript) ordering, the standard for piezo materials
(differs from the general Solid Mechanics anisotropic convention): **xx, yy, zz, yz, xz, xy**.
For matrix entry, the docs give the order "xx, yy, zz, yz, xz, zy" (indices 1..6 = xx, yy, zz, yz, xz, xy).
The data is defined in the **material frame** with crystal axes aligned to the selected coordinate system
(Global by default). Crystal cuts are defined by a rotated coordinate system (Euler angles, ZXZ convention);
COMSOL adopts the IEEE 1978 standard (IRE 1949 for quartz library data).

### 3.4 Other node properties (Piezoelectric Material)

- `UseMixedFormulation`: None | Pressure | Strain (low-compressibility stabilization)
- `Formulation`: From study step | Total Lagrangian | Geometrically linear
- `StrainDecomposition`: Automatic | Additive | Logarithmic | Multiplicative (`Method`: Analytic | Padé)
- `UseMultiplicativeFormulation` checkbox (multiplicative decomposition of elastic/inelastic strains; forces geometric nonlinearity)
- `EnergyDissipation` settings, reduced integration, hourglass stabilization (same as LinearElasticModel)

### 3.5 Subnodes (damping and losses)

| Subnode | Type string | Properties |
|---|---|---|
| Initial Stress and Strain | `InitialStressandStrain` | `sigma0`, `epsilon0` |
| Thermal Expansion (for Materials) | `ThermalExpansion` | `alpha`, `Tref` |
| Mechanical Damping | `MechanicalDamping` (tag `mdmp*`) | `DampingType`: LossFactorC / LossFactorS / LossFactorCH / LossFactorSH / IsotropicLossFactor (`etas`) / RayleighDamping (`alphaD`, `betaD`) / MaximumLossFactor (`etaMax`, `fref`) |
| Coupling Loss | `CouplingLoss` | `CouplingLossType`: LossFactorE (`etae`, 3×6) / RayleighDamping (`betaDc`) |
| Dielectric Loss | `DielectricLoss` (tag `dels*`) | `DielectricLossType`: LossFactorEpsilonS / LossFactorEpsilonT / Dispersion (`tau_d`, `dEpsilonrS`) / ComplexPermittivity (`epsilonp`, `epsilonpp`, `fref`) / MaximumLossTangent (`etaMax`, `fref`) |
| Conduction Loss (Time-Harmonic) | `ConductionLoss` | `sigma_e` (Electric conductivity), LinearizedResistivity (`rho0`, `alpha_r`, `T0`) |

Loss-factor implementation (component-wise, j = √−1):
- c̃E = cE(1 + j·ηcE),  s̃E = sE(1 − j·ηsE)
- ẽ = e(1 + j·ηe),  d̃ = d(1 + j·ηd)
- ε̃rS = εrS(1 − j·ηεS),  ε̃rT = εrT(1 − j·ηεT)

Loss factors only act in eigenfrequency/frequency-domain studies, except Rayleigh damping,
Dispersion, Complex permittivity and Maximum loss tangent which also work in time-dependent studies.

### 3.6 Piezo material in other interfaces

- **Layered Shell** (`lshell`): same type `PiezoelectricMaterialModel`; layer selection; pairs with
  `Piezoelectricity, Layered` coupling and `PiezoelectricLayer` node in Electric Currents in Layered Shells (`ecs`);
  has `OutOfPlaneMaterialOrientation` section for poling direction.
- **Shell** (3D): `PiezoelectricMaterialModelLayered` ("Piezoelectric Material, Layered").
- Poling: material library data assumes poling along the local third axis; rotate via coordinate system.

---

## 4. Shell and Plate Interfaces (`shell` / `plate`)

Shell = boundary-level in 3D and 2D axisym; Plate = 2D domain-level. DOFs: u (translation) + θ (rotation of normals).

### 4.1 Domain/boundary nodes

| Node | Type string | Notes |
|---|---|---|
| Initial Values | `init` | u, du/dt, ar (normal displacement), dar/dt |
| Thickness and Offset | `ThicknessOffset` (tag `to*`) | `d0`, `Position` (Top/Midsurface/Bottom/User defined), `zrel_offset` |
| Thickness Change | `ThicknessChange` | time-dependent thickness |
| Linear Elastic Material | `Elastic` (tag `emm*`) | subnodes `Damping` (dmp*), `Safety` (sf*), `ShellLocalSystem` (shls*) |
| Linear Elastic Material, Layered | `LayeredElastic` (tag `llem*`) | subnodes `LayeredPlasticity` (lplsty*), `LayeredSafety` (lsf*), `LayeredThermalExpansion` (lte*) |
| Hyperelastic Material, Layered | `LayeredHyperelasticModel` (tag `lhmm*`) | |
| Piezoelectric Material, Layered | `PiezoelectricMaterialModelLayered` | |
| Viscoelasticity / Plasticity / Creep / Viscoplasticity | subnodes | |
| Section Stiffness | `SectionStiffness` | |
| Shell Local System | `ShellLocalSystem` | |

Loads: `FaceLoad` (tag `fl*`, pressure/tractions on shell faces), `EdgeLoad`, `PointLoad`, `PointLoadOnAxis`,
`RingLoad`, `BodyLoad`, `Gravity`, `RotatingFrame`, `LinearlyAcceleratedFrame`, `BaseExcitation`,
`AddedMass`, `SpringFoundation2` (tag `spf*`), `Predeformation`.

Constraints: `Fixed`, `Displacement0/1/2` (Prescribed Displacement/Rotation: `U0` + `theta0`),
`Velocity`, `Acceleration`, `Pinned` (tag `pin*`), `NoRotation`, `SimplySupported` (tag `ssp*`),
`SymmetrySolid1` (tag `sym*`), `SymmetryPlane`, `Antisymmetry`, `Free`, `RigidMotionSuppression`,
`ThermalExpansion` (for Constraints), `PeriodicCondition`.

Connections: `RigidConnectorShell` (tag `srig*`, subnodes `CenterOfRotationBnd/Edge/Point`, `RigidBodyMoment`),
`Attachment` (edge level), `BoundaryToBoundary` (solid-shell), `EdgeToBoundary`, `EdgeToEdge`, `SpotWelds`,
`Fasteners` (+ `HoleSelection`), `ReducedFlexibleComponents`, `SpringFoundation` (+ `PreDeformation`).

Contact: `ShellContact` (tag `cnt*`).

### 4.2 Layered Shell Interface (`lshell`)

Top-level type strings: `BodyLoad`, `BoundaryLoad`, `ContinuityLayeredShell` (contls*), `Delamination` (del*),
`Displacement` (disp*), `DisplacementIntEP` (dispi*), `EdgeLoad`, `FaceLoad`, `Fixed`, `Free`,
`GlobalEquations`, `LineLoad` (ll*), `LinearElasticModel`, `PiezoelectricMaterialModel`, `RigidMotionSuppression`,
`Roller`, `Symmetry`, `init`.
Node list (UI): Initial Values, Linear Elastic Material, Hyperelastic Material, Piezoelectric Material,
Viscoelasticity, Mullins Effect, Plasticity, Set Variables, Creep, Additional Creep, Viscoplasticity,
Polymer Viscoplasticity, Additional Network, Thermal Expansion (for Materials), Hygroscopic Swelling,
Initial Stress and Strain, External Stress, External Strain, Inelastic Strain Rate, Damage, Activation,
Delamination, Safety, Damping, Mechanical Damping, Coupling Loss, Dielectric Loss, Rigid Material,
Free, Prescribed Displacement (+ Interface variant), Prescribed Velocity (+ Interface), Prescribed Acceleration
(+ Interface), Fixed Constraint (+ Interface), Thermal Expansion (for Constraints), Roller (+ Interface),
Symmetry, Antisymmetry, Rigid Motion Suppression, Body Load, Face Load, Rotating Frame,
Linearly Accelerated Frame, Boundary Load, Edge Load, Line Load, Point Load, Phase, Spring Foundation
(+ Interface), Thin Elastic Layer (+ Interface), Predeformation, Added Mass (+ Interface), Adiabatic Heating,
Rigid Connector (+ Interface), Attachment, Continuity.

---

## 5. Membrane Interface (`mbrn`)

Boundary-level (3D) / domain-level... actually boundaries; 3D and 2D axisym.

Type strings: `LinearElasticModel`, `HyperelasticModel`, `LayeredLinearElasticModel` (llemm*),
`ThicknessOffset` (to*), `FaceLoad` (fl*), `EdgeLoad` (el*), `Displacement0` (disp*), `Displacement1` (disp*),
`Fixed` (fix*), `Free`, `SpringFoundation2` (spf*), `Symmetry` (sym*), `AxialSymmetry`, `AxialSymmetrySolid`,
`GlobalEquations`, `init`.

Node list (UI): Linear Elastic Material, Linear Elastic Material, Layered, Viscoelasticity, Plasticity,
Set Variables, Creep, Additional Creep, Viscoplasticity, Wrinkling, Fiber, Thermal Expansion (for Materials),
Hygroscopic Swelling, Initial Stress and Strain, External Stress, Inelastic Strain Rate, Safety, Damping,
Symmetry, Antisymmetry, Stabilization, Adiabatic Heating, Layered, Face Load, Edge Load, Ring Load,
Ring Load, Free; inherited from Solid/Shell: Fixed Constraint, Prescribed Displacement, Prescribed Velocity,
Prescribed Acceleration, Free, Point Load, Point Load, Free, Point Load (on Axis), Spring Foundation,
Spring–Damper, Point Mass, Added Mass, Body Load, Gravity, Rotating Frame, Linearly Accelerated Frame,
Base Excitation, Thickness and Offset, Thickness Change, Contact, Enclosed Cavity, Rigid Connector,
Attachment, Thermal Expansion (for Constraints/Materials/Fiber).

---

## 6. Beam Interface (`beam`)

Edges in 3D / boundaries in 2D. DOFs: u + θ (3 translations + 3 rotations).

Type strings (from tags/verified): `CrossSectionBeam` (csd*, "Cross-Section Data"), `SectionOrientation` (so*),
`LinearElasticModel` (lemm*), `PrescribedDisplacementOrRotation` (DispRot, tag `pdr*`), `Pinned` (pin*),
`NoRotation`, `Symmetry`, `Antisymmetry`, `EdgeLoad` (el*), `PointLoad` (pl*), `PointLoadFree`,
`PointMass`, `RigidConnector` (rig*), `Attachment` (att*), `BeamEndRelease`, `EdgeGroup`, `Free`, `Fixed`,
`Velocity`, `Acceleration`, `SectionStiffness`, `init`.

Node list (UI): Initial Values, Cross-Section Data (Section type: Rectangle, Box, Circular, Pipe, H-profile,
U-profile, T-profile, C-profile, Hat, User defined), Section Orientation, Linear Elastic Material,
Thermal Expansion (for Materials), Hygroscopic Swelling, Initial Stress and Strain, External Stress,
Section Stiffness, Prescribed Displacement/Rotation, Prescribed Velocity, Prescribed Acceleration, Pinned,
Thermal Expansion (for Constraints), No Rotation, Symmetry, Antisymmetry, Edge Load, Point Load,
Point Load, Free, Point Mass, Rigid Connector, Attachment, Beam End Release, Edge Group, Phase,
Harmonic Perturbation. Inherited: Fixed Constraint, Free, Body Load, Gravity, Rotating Frame,
Linearly Accelerated Frame, Base Excitation, Spring Foundation, Spring–Damper, Damping, Added Mass,
Predeformation, Safety.

---

## 7. Beam Cross Section Interface (`bcs`)

Solves 2D cross-section problem to compute section properties for Beam.
Nodes: Homogeneous Cross Section, Hole, Safety. Couplings: `BeamCrossSection–Beam` (bcs→beam section data).

---

## 8. Truss Interface (`truss`)

Type strings: `Elastic` (emm*, Linear Elastic Material, subnodes `InitialStressandStrain` iss*, `Plasticity` plsty*),
`CrossSectionBeam` (csd*), `Displacement0` (disp*), `Pinned` (pin*), `PointLoad` (pl*),
`SpringFoundation1` (spf*), `StraightEdgeConstraint` (sec*), `Free`, `Discretization`, `AverageRotation` (avgr*), `init`.

Node list (UI): Cross-Section Data (same section types as Beam), Straight Edge Constraint,
Linear Elastic Material (with subnodes Set Variables, Thermal Expansion (for Linear Elastic Material),
Thermal Expansion (for Shape Memory Alloy), Hygroscopic Swelling, Initial Stress and Strain, External Stress,
Spring-Damper Material), Pinned, Thermal Expansion (for Constraints), Symmetry, Antisymmetry,
Edge Load, Point Mass. Inherited: Point Load, Point Load, Free, Prescribed Displacement, Prescribed Velocity,
Prescribed Acceleration, Fixed Constraint, Free, Body Load, Gravity, Rotating Frame, Linearly Accelerated Frame,
Base Excitation, Spring Foundation, Spring–Damper, Damping, Plasticity, Shape Memory Alloy, Activation, Safety.

---

## 9. Wire Interface (`wire`)

Nodes: Elastic Wire, Thermal Expansion (for Elastic Wire), Hygroscopic Swelling, Initial Stress and Strain,
Pinned, Thermal Expansion (for Constraints), Symmetry, Antisymmetry, Edge Load. Inherited: Point Load,
Fixed Constraint, Free, Gravity, Spring Foundation, Spring–Damper, Point Mass, Damping, Safety, etc.

---

## 10. Pipe Mechanics Interface (`pipem`)

Type strings: `PipeCrossSection` (pcs*, subnode `BeamSectionOrientation` so*), `DispRot0` (pdr*),
`Fixed` (fix*), `FluidLoad` (fl*), `FluidPipeMat` (fpm*), `Free`, `Gravity` (gr*), `init`.

Nodes: Pipe Cross Section, Section Orientation, Bend, Fluid and Pipe Materials, Rigid Material,
Thermal Expansion (for Materials), Gravity, Base Excitation, Linearly Accelerated Frame, Fluid Load;
inherited constraints/loads (Pinned, Fixed, Edge Load, Point Load, etc.). Coupling: `Structure–Pipe Connection`.

---

## 11. Multibody Dynamics Interface (`mbd`)

Rigid/flexible bodies + joints. Interface-level: Initial Values, Initially Rigid, Rigid Material, Linear Elastic Material.

### 11.1 Joints (global level, submenu Joints)

| Joint | Type string | Free relative motion |
|---|---|---|
| Prismatic Joint | `PrismaticJoint` (prj*) | translation along joint axis (2D, 3D) |
| Hinge Joint | `HingeJoint` (hgj*) | rotation about joint axis (2D, 3D) |
| Cylindrical Joint | `CylindricalJoint` (clj*) | translation + rotation about axis (3D) |
| Screw Joint | `ScrewJoint` (scj*) | coupled translation/rotation, `Pitch`, `Start` (3D) |
| Planar Joint | `PlanarJoint` (plj*) | translation in plane ⊥ axis + rotation about axis (3D) |
| Ball Joint | `BallJoint` (blj*) | rotation about all 3 axes (3D) |
| Slot Joint | `SlotJoint` (slj*) | 3 rotations + translation along slot axis (3D) |
| Reduced Slot Joint | `ReducedSlotJoint` (rslj*) | slot with reduced DOFs (2D, 3D) |
| Clearance Joint | `ClearanceJoint` (crj*) | slot with clearance/gap (2D, 3D) |
| Fixed Joint | `FixedJoint` (fxj*) | rigidly connects two attachments |
| Distance Joint | `DistanceJoint` (dsj*) | fixed distance between two points |
| Universal Joint | `UniversalJoint` (uvj*) | rotation about two perpendicular axes |

Joint common settings: `Source`/`Destination` (Attachment, Rigid Material, gears, Fixed, Base Motion),
`SourceFilter`/`DestinationFilter` (srcf*/dstf*), `CenterOfJoint` (Centroid of source/destination/selected, User defined + `Xc`, `Offset`),
`AxisOfJoint` (Specify direction `e0` / parallel edge / coordinate system axis; subnode `JointAxis` ja*),
`JointElasticity` (Rigid/Elastic joint; subnode `JointElasticity` je*), `JointForcesAndMoments`
(Computed on destination/source, Do not compute, weak constraints, penalty `pj`).

Joint subnodes (Attributes): `Constraints` (ct*), `Locking` (lk*), `SpringAndDamper` (sd*, `k`, `c`),
`PrescribedMotion` (pm*), `AppliedForceAndMoment` (afm*), `Friction` (fric*, subnode `ContactArea` ca*).

Point nodes for joints: `CenterOfJointBnd/Edge/Point` (cjb*/cje*/cjp*), `SourcePointBnd/Edge/Point` (spb/spe/spp*),
`DestinationPointBnd/Edge/Point` (dpb/dpe/dpp*).

### 11.2 Gears and other nodes

- Gears (domain level): `SpurGear` (spg*), `HelicalGear` (hlg*), `BevelGear` (bvg*), `WormGear`,
  `SpurRack`, `HelicalRack`; subnodes `GearAxis` (gax*), `RackAxis`, `init`, `CenterOfRotationBnd/Edge/Point`,
  `PrescribedDispRot` (pdr*, Bevel only).
- `GearPair` (grp*; global): subnodes `Backlash` (bcl*), `Friction` (fric*), `GearElasticity` (gel*),
  `TransmissionError` (ter*); plus `WormAndWheel`, `RackAndPinion`.
- `CamFollower` (cfc*): subnode `Friction (Cam–Follower)`.
- `RigidBodyContact` (rbc*): subnodes `SourcePoint*`, `DestinationPoint*`, `Friction`; `SourceAxis`/`DestinationAxis`.
- `ChainDrive` (cdr*): subnode `SprocketAxis` (sja*), `JointElasticity`.
- `SpringDamper` (spd*): between attachments; subnodes `SourcePoint*`/`DestinationPoint*` + filters.
- `BaseMotion` (bsm*): prescribed motion of a base attachment (also appears as Source option).
- `Measure` (global): measures joint DOFs.
- `RadialRollerBearing` (rrb*): subnodes `FlexibleFoundation` (ffd*), `MovingFoundation` (mfd*), `Misalignment` (mlgn*).
- `FlexibleFoundation`, `MovingFoundation`.
- Top-level types: `Attachment` (att*, boundary level), `BodyLoad` (bl*), `BoundaryLoad` (bndl*),
  `Fixed` (fix*), `Free`, `GlobalEquations` (ge*), `Gravity` (gr*), `LinearElasticModel` (lemm*),
  `SpringFoundation1` (spf*), `AddedMass1` (adm*), `RigidConnector` (rig*), `RigidDomain` (rd*), `init`.
- Multiphysics: Fluid–Multibody Interaction; Magnetic–Rigid-Body Interaction in Rotating Machinery.

### 11.3 Lumped Mechanical System (`lms`)

Nodes: `Mass` (M*), `Spring` (K*), `Damper` (C*), `Impedance`, `DisplacementNode` (disp*),
`VelocityNode`, `AccelerationNode`, `MassNode`, `ForceNode` (frc*), `ImpedanceNode`, `ExternalSource` (E*),
`FixedNode` (fix*), `FreeNode` (fr*), `SubSystem` (X*) with `SubSystemBlock` (sub*, containing Mass/Spring/Damper/FreeNode),
`Lumped–Structure Connection`.

---

## 12. Rotordynamics Module

### 12.1 Solid Rotor (`rotsld`) — 3D, corotating frame

Domain/boundary nodes:
- `LinearElasticModel` (lemm*, subnode `Damping` dmp*), `RigidDomain` (rd*), `init`
- `RotatingFrame` — axis of rotation (x/y/z/from points/from edges/user defined), local x direction, base point;
  rotational velocity (Constant/General angular velocity ωr, Constant/General revolutions per time), spin softening
- `FixedAxialRotation` (`FixAxRot`, tag far*) — boundary: axial rotation locked; `ChangeRotorSpeed` (rsp? — `RotorSpeed` rsp*)
- Bearings: `JournalBearing` (jrb*) — orientation, properties (stiffness/damping), foundation; subnodes
  `FlexibleFoundation` (ffd*), `MovingFoundation` (mfd*), `SqueezeFilmDamper` (sfd*)
- `ThrustBearing` (thrb*) — orientation, properties, foundation (+ ffd*/mfd*)
- `RadialRollerBearing` (rrb*) — orientation, geometric properties (rollers, races), clearance/preload, material, foundation (+ ffd*, mfd*, sfd*)
- `ActiveMagneticBearing` (amb*) — orientation, air gap, control parameters, currents, foundation
- `FlexibleFoundation` (ffd*), `MovingFoundation` (mfd*), `SqueezeFilmDamper` (sfd*), `Misalignment` (mlgn*)
- `MultiSpoolBearing` (msb*) — intershaft connection (rigid/flexible)
- `LiquidAnnularSeal` — seal model (Black & Jenssen / Childs), geometric/fluid/flow properties
- `RotorCoupling` (cpl*) — spline/torsional/user defined couplings
- Loads: `BodyLoad` (frame type: corotating/spatial), `BoundaryLoad`, `AppliedTorque` (atq*), `Gravity` (gr*), `AddedMass`
- Gears: `SpurGear`, `HelicalGear` (hlg*), `BevelGear`, `GearAxis`; `GearPair` (grp*) with `Backlash` (bcl*),
  `Friction` (fric*), `GearElasticity` (gel*), `TransmissionError` (ter*)
- `RotorAxis` (raxi*) with subnodes `Axis` (axis*), `FirstSupport` (fsup*), `SecondSupport` (ssup*)
- Inherited from Solid Mechanics: Initial Values, Linear Elastic Material, Damping, External Stress,
  External Strain, Initial Stress and Strain, Phase, Thermal Expansion (for Materials), Average Rotation, etc.
- Also: `Free` (free*), `RotorSpeed` (rsp*)

Solid Rotor, Fixed Frame (`rotsff`): same nodes as Solid Rotor (space-fixed frame; axially symmetric rotor assumed).

### 12.2 Beam Rotor (`rotbm`) — 3D, Timoshenko beam on edge

Top-level types: `LinearElasticModel` (lemm* + Damping), `ActiveMagneticBearing` (amb* + ffd*/mfd*),
`JournalBearing` (jrb* + ffd*/mfd*/sfd*), `RadialRollerBearing` (rrb* + ffd*/mfd*/sfd*),
`Disk` (disk*), `FixAxRot` (far*), `Free` (free*), `Gravity` (gr*), `MultiSpoolBearing` (msb*),
`RotorCoupling` (cpl*), `RotorCrossSection` (rcs*, subnode `BeamSectionOrientation` so*),
`RotorSpeed` (rsp*), `init`.

Nodes: Initial Values, Rotor Cross Section (+ Section Orientation), Rotor Rub (contact), Fixed Axial Rotation,
Disk (Disk Properties: mass, inertia), Journal Bearing, Thrust Bearing, Radial Roller Bearing,
Squeeze-Film Damper, Rotor Coupling, Edge Load (frame type, force, moment), Point Load (frame type, force, moment),
Gravity, plus inherited Linear Elastic Material, External Stress, Initial Stress and Strain, Thermal Expansion.

### 12.3 Hydrodynamic Bearing (`hdb`) — 3D film flow (Reynolds equation)

Top-level types: `BearingOrientation` (bax*), `Border` (bdr*), `SqueezeFilmDamper` (sfd*), `init`.
Domain features: `HydrodynamicJournalBearing` (hjb*) — reference surface, bearing properties, journal properties,
film boundary condition, contact surface, fluid properties, film flow model; subnodes `FlexibleFoundation` (ffd*),
`MovingFoundation` (mfd*), `SqueezeFilmDamper` (sfd*), `Misalignment` (mlgn*).
`HydrodynamicThrustBearing` (htb*) — reference surface, bearing/collar properties, film BC, contact surface,
fluid properties, film flow model.
`FloatingRingBearing` (frb*) — bearing/journal properties, film BC, fluid properties, film flow model;
subnodes `InnerFilmProperties` (if*), `OuterFilmProperties` (of*), `InnerOuterFilmConnection` (fc*), ffd*, mfd*.
Boundary nodes: Inlet, Outlet, Wall, Symmetry. Studies include Bearing Dynamic Coefficients (perturbation).

---

## 13. Quick property/type reference (verified in this skill's models)

```python
comp = model.java.component('comp1')
solid = comp.physics().create('solid', 'SolidMechanics', 'geom1')
lemm = solid.feature().create('lemm1', 'LinearElasticModel', 2)   # domain
pmat = solid.feature().create('pmat1', 'PiezoelectricMaterialModel', 2)
fix  = solid.feature().create('fix1',  'Fixed', 1)                 # boundary
disp = solid.feature().create('disp1', 'Displacement1', 1)         # boundary
free = solid.feature().create('free1', 'Free', 1)
# joint in multibody:
mbd  = comp.physics().create('mbd', 'MultibodyDynamics', 'geom1')
att  = mbd.feature().create('att1', 'Attachment', 1)
hgj  = mbd.feature().create('hgj1', 'HingeJoint')                  # global
# rotordynamics:
rot  = comp.physics().create('rot', 'SolidRotor', 'geom1')
jrb  = rot.feature().create('jrb1', 'JournalBearing', 1)
```

Key gotchas (from lessons_learned.md):
- `set('dET', array)` and all matrix sets are **column-major**.
- StrainCharge ↔ (sE, dET, epsilonrS); StressCharge ↔ (cE, eES, epsilonrS). Disable the unused matrices with `_mat='from_mat'`.
- Set `<prop>_mat` mode before setting the value; set `rho_mat` explicitly for user-defined density.
- `ChargeConservationPiezo` (tag `ccp*`) is the piezo domain node in Electrostatics; coupling type `PiezoelectricEffect`
  with properties `Solid_physics` / `Electrostatics_physics`.
- With `Displacement1`, use `setIndex('U0', value, i)` per component.
