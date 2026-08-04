# RF Module — API Reference

Extracted from COMSOL 6.4 documentation and mph tags.json.

## Feature Types (183 found)

| Feature Name | Tag | Parent Interface |
|-------------|-----|------------------|
| `exports` | `export` |  |
| `Animation` | `anim*` | exports |
| `Data` | `data*` | exports |
| `Image` | `img*` | exports |
| `Plot` | `plot*` | exports |
| `Import` | `imp*` | ? |
| `SemiconductorElectromagneticWavesCoupling` | `semc*` | multiphysics |
| `CrossSectionImport` | `xsec*` | BoltzmannEquation |
| `ChargeTransport` | `ct` | physics |
| `AxialSymmetry` | `axi*` | ChargeTransport |
| `NoFlux` | `nflx*` | ChargeTransport |
| `Source` | `st*` | ChargeTransport |
| `TransportProperties` | `tp*` | ChargeTransport |
| `init` | `init*` | ChargeTransport |
| `TCSPorousMediaTransportProperties` | `pmtcs*` | ConcentratedSpecies |
| `ElectromagneticWaves` | `emw` | physics |
| `FarFieldDomain` | `ffd*` | ElectromagneticWaves |
| `FarFieldCalculation` | `ffc*` | FarFieldDomain |
| `Impedance` | `imp*` | ElectromagneticWaves |
| `LumpedElement` | `lelement*` | ElectromagneticWaves |
| `LumpedPort` | `lport*` | ElectromagneticWaves |
| `UniformElement` | `ue*` | LumpedPort |
| `MixedModeSparameters` | `mms*` | ElectromagneticWaves |
| `PerfectElectricConductor` | `pec*` | ElectromagneticWaves |
| `PerfectMagneticConductor` | `pmc*` | ElectromagneticWaves |
| `PeriodicCondition` | `pc*` | ElectromagneticWaves |
| `Port` | `port*` | ElectromagneticWaves |
| `CircularPortReferenceAxis` | `cportv*` | Port |
| `ElectricPotential` | `pot*` | Port |
| `Ground` | `gnd*` | Port |
| `Scattering` | `sctr*` | ElectromagneticWaves |
| `SpecificAbsorptionRate` | `sar*` | ElectromagneticWaves |
| `SurfaceCurrent` | `scu*` | ElectromagneticWaves |
| `TransitionBoundaryCondition` | `trans*` | ElectromagneticWaves |
| `WaveEquationElectric` | `wee*` | ElectromagneticWaves |
| `ElectromagneticWavesBeamEnvelopes` | `ewbe` | physics |
| `FieldContinuity` | `fcont*` | ElectromagneticWavesBeamEnvelopes |
| `MatchedBoundaryCondition` | `mbc*` | ElectromagneticWavesBeamEnvelopes |
| `ReferencePoint` | `rpnt*` | MatchedBoundaryCondition |
| `WaveEquationBeamEnvelopes` | `webe*` | ElectromagneticWavesBeamEnvelopes |
| `ElectromagneticWavesFrequencyDomain` | `ewfd` | physics |
| `GlobalEquations` | `ge*` | ElectromagneticWavesFrequencyDomain |
| `Polarization` | `pol*` | ElectromagneticWavesFrequencyDomain |
| `DiffractionOrder` | `dport*` | Port |
| `OrthogonalPolarization` | `oport*` | Port |
| `PeriodicPortReferencePoint` | `pportp*` | Port |
| `ElectromagneticWavesTransient` | `ewt` | physics |
| `DrudeLorentzPolarization` | `dlp*` | WaveEquationElectric |
| `ElectrophoreticTransport` | `el` | physics |
| `Ampholyte` | `amph*` | ElectrophoreticTransport |
| `InitialConcentration` | `initc*` | Ampholyte |
| `ElectrolyteNormalCurrentDensity` | `icd*` | ElectrophoreticTransport |
| `ElectrolytePotential` | `eip*` | ElectrophoreticTransport |
| `Insulation` | `ins*` | ElectrophoreticTransport |
| `Protein` | `prot*` | ElectrophoreticTransport |
| `Inflow` | `in*` | Protein |
| `Outflow` | `out*` | Protein |
| `Solvent` | `sol*` | ElectrophoreticTransport |
| `WeakAcid` | `wa*` | ElectrophoreticTransport |
| `Concentration` | `conc*` | WeakAcid |
| `WeakBase` | `wb*` | ElectrophoreticTransport |
| `HeavySpeciesTransport` | `hs` | physics |
| `ConvectionDiffusion` | `cdm*` | HeavySpeciesTransport |
| `Species` | `sp*` | HeavySpeciesTransport |
| `SurfaceReaction` | `sr*` | HeavySpeciesTransport |
| `SurfaceSpecies` | `ssp*` | HeavySpeciesTransport |
| `MoistureTransportInAir` | `mt` | physics |
| `Gravity` | `grav*` | MoistureTransportInAir |
| `InitialValues` | `init*` | MoistureTransportInAir |
| `MoistAir` | `ma*` | MoistureTransportInAir |
| `OpenBoundary` | `open*` | MoistureTransportInAir |
| `Symmetry` | `sym*` | MoistureTransportInAir |
| `WetSurface` | `ws*` | MoistureTransportInAir |
| `MoistureTransportInBuildingMaterials` | `mt` | physics |
| `BuildingMaterial` | `bm*` | MoistureTransportInBuildingMaterials |
| `MoistureContent` | `mc*` | MoistureTransportInBuildingMaterials |
| `MoistureFlux` | `mf*` | MoistureTransportInBuildingMaterials |
| `ThinMoistureBarrier` | `tmb*` | MoistureTransportInBuildingMaterials |
| `PhaseTransport` | `phtr` | physics |
| `PhaseAndTransportProperties` | `ptp*` | PhaseTransport |
| `PhaseTransportPorousMedia` | `phtr` | physics |
| `MassFlux` | `mf*` | PhaseTransportPorousMedia |
| `MassFlux1` | `mf*` | PhaseTransportPorousMedia |
| `PhaseAndPorousMediaTransportProperties` | `pptp*` | PhaseTransportPorousMedia |
| `PorousMediumDiscontinuity` | `pmd*` | PhaseTransportPorousMedia |
| `VolumeFraction` | `sa*` | PhaseTransportPorousMedia |
| `SimplySupported` | `ssp*` | Shell |
| `FirstSupport` | `fsup*` | RotorAxis |
| `SecondSupport` | `ssup*` | RotorAxis |
| `TransientElectromagneticWaves` | `temw` | physics |
| `PhasePortrait` | `phpo*` | PlotGroup2D |
| `Color` | `col*` | PhasePortrait |

## Documentation Structure (api_rf_extract.txt)

```
  TOC:   Introduction (p.5)
  TOC:     The Use of the RF Module (p.6)
  TOC:   The RF Module Physics Interfaces (p.11)
  TOC:     Physics Interface Guide by Space Dimension and Study Type (p.15)
  TOC:   Tutorial Model: Impedance Matching of a Lossy Ferrite 3-Port Circulator (p.17)
  TOC:     Introduction (p.17)
  TOC:     Impedance Matching (p.18)
  TOC:     Model Definition (p.18)
  TOC:     The Lossy Ferrite Material Model (p.18)
  TOC:     References (p.20)
  TOC:     Model Wizard (p.20)
  TOC:     Global Definitions - Parameters (p.21)
  TOC:     Geometry (p.22)
  TOC:     Definitions - Variables (p.22)
  TOC:     Materials (p.23)
  TOC:     Electromagnetic Waves, Frequency Domain (p.24)
  TOC:     Mesh (p.27)
  TOC:     Study 1 (p.29)
  TOC:     Results (p.29)
  TOC:     Study 1 (p.30)
  TOC:     Results (p.32)
  TOC:     Global Definitions - Parameters (p.32)
  TOC:     Study 1 (p.33)
  TOC:     Results (p.34)
  TOC:     Study 2 (p.34)
  TOC:     Results (p.35)
  TOC:     Study 3 (p.37)
  TOC:     Results (p.38)
  TOC:     Definitions (p.39)
  TOC:     Results (p.40)
  TOC:   Contents (p.3)
  TOC:   Introduction (p.13)
  TOC:     About the RF Module (p.14)
  TOC:       What Can the RF Module Do? (p.14)
  TOC:       What Problems Can You Solve? (p.15)
  TOC:       The RF Module Physics Interface Guide (p.16)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.18)
  TOC:       Selecting the Study Type (p.19)
  TOC:       The RF Module Modeling Process (p.20)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.21)
  TOC:     Overview of the User’s Guide (p.24)
  TOC:   RF Modeling (p.27)
  TOC:     Preparing for RF Modeling (p.29)
  TOC:     Simplifying Geometries (p.30)
  TOC:       2D Models (p.30)
  TOC:       3D Models (p.32)
  TOC:       Using Efficient Boundary Conditions (p.33)
  TOC:       Applying Electromagnetic Sources (p.33)
  TOC:       Meshing and Solving (p.34)
  TOC:     Periodic Boundary Conditions (p.35)
```

## Key API Content (45 sections)

### Section 1

```
=== IntroductionToRFModule.pdf ===
Pages: 52
  TOC:   Introduction (p.5)
  TOC:     The Use of the RF Module (p.6)
  TOC:   The RF Module Physics Interfaces (p.11)
  TOC:     Physics Interface Guide by Space Dimension and Study Type (p.15)
  TOC:   Tutorial Model: Impedance Matching of a Lossy Ferrite 3-Port Circulator (p.17)
  TOC:     Introduction (p.17)
  TOC:     Impedance Matching (p.18)
  TOC:     Model Definition (p.18)
  TOC:     The Lossy Ferrite Material Model (p.18)
  TOC:     References (p.20)
  TOC:     Model Wizard (p.20)
  TOC:     Global Definitions - Parameters (p.21)
  TOC:     Geometry (p.22)
  TOC:     Definitions - Variables (p.22)
  TOC:     Materials (p.23)
  TOC:     Electromagnetic Waves, Frequency Domain (p.24)
  TOC:     Mesh (p.27)
  TOC:     Study 1 (p.29)
  TOC:     Results (p.29)
  TOC:     Study 1 (p.30)
  TOC:     Results (p.32)
  TOC:     Global Definitions - Parameters (p.32)
  TOC:     Study 1 (p.33)
  TOC:     Results (p.34)
  TOC:     Study 2 (p.34
```

### Section 2

```
3 ---
 | 3
Contents
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
The Use of the RF Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
The RF Module Physics Interfaces . . . . . . . . . . . . . . . . . . . . . . . .11
Physics Interface Guide by Space Dimension and Study Type . . . 15
Tutorial Model: Impedance Matching of a Lossy Ferrite 3-Port 
Circulator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .17
Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
Impedance Matching. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Model Definition. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
The Lossy Ferrite Material Model . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
```

### Section 3

```
5 ---
 | 5
Introduction
The RF Module is used by engineers and scientists to understand, predict, and 
design electromagnetic wave propagation and resonance effects in high-frequency 
applications. Simulations of this kind result in more powerful and efficient 
products and engineering methods. It allows users to quickly and accurately 
predict electromagnetic field distributions, transmission, reflection, and power 
dissipation in a proposed design. Compared to traditional prototyping, it offers 
the benefits of lower cost and the ability to evaluate and predict phenomena that 
cannot be measured directly in experiments. It also allows the exploration of 
operating conditions that would destroy a real prototype or be hazardous.
This module covers electromagnetic fields and waves in two- and 
three-dimensional space along with traditional circuit-based modeling of passive 
and active devices. All modeling formulations are based on Maxwell’s equations or 
subsets and special cases of th
```

### Section 4

```
6 ---
6 | 
lightning surge studies, ferrimagnetic devices, filters, microwave heating, passive 
components, scattering and radar cross-section (RCS) analysis, and transmission 
lines and waveguides. It also provides tutorials for education and verification 
models for benchmarking the RF interfaces.
This introduction is intended to give you a jump start in your modeling work. It 
has examples of the typical use of the RF Module, a list of the physics interfaces 
with a short description, and a tutorial model that introduces the modeling 
workflow.
The Use of the RF Module
The RF interfaces are used to model electromagnetic fields and waves in high 
frequency applications. The latter means that it covers the modeling of devices that 
are above about 0.1 electromagnetic wavelength in size. Thus, it may be used to 
model microscale devices or human size devices operating at frequencies above 
10 MHz.
RF simulations are frequently used to extract S-parameters characterizing the 
transmissi
```

### Section 5

```
9 ---
 | 9
The RF Module also offers a comprehensive set of features for 2D modeling 
including both source driven wave propagation and mode analysis. Figure 5 shows 
mode analysis of a step-index profile optical fiber.
Figure 5: The surface plot visualizes the longitudinal component of the electric field in the fiber core. From 
the application library entry Step Index Fiber.
Both in 2D and 3D, the analysis of periodic structures is popular. Figure 6 is an 
example of a plane wave incidence on a wire grating with a dielectric substrate.
Figure 6: Electric field norm for TE incidence at π/5. From the application library entry Plasmonic Wire 
Grating.
```

### Section 6

```
11 ---
 | 11
The RF Module Physics Interfaces
The RF Module physics interfaces are based on Maxwell’s equations or subsets 
and special cases of these together with material constitutive relations. In the 
module, these laws of physics are translated by the RF interfaces to sets of partial 
differential equations with corresponding initial and boundary conditions.
The RF interfaces define a number of features. Each feature represents a term or 
condition in the underlying equations and may be defined in a geometric entity of 
the model, such as a domain, boundary, edge (for 3D components), or point.
Figure 8: The Model Builder (left), and the Settings window for Wave Equation, Electric (right). The 
Equation section shows the model equations and the terms added by the Wave Equation, Electric 1 node 
to the model equations. The added terms are underlined with a dotted line. The text also explains the 
link between the Dielectric node in Materials and the values for the relative permitti
```

### Section 7

```
12 ---
12 | 
Figure 8 uses the Coaxial Waveguide Coupling model from the RF Module 
application library to show the Model Builder window and the Settings window 
for the selected Wave Equation, Electric 1 feature node. The Wave Equation, 
Electric 1 node adds the terms representing Electromagnetic Waves to the model 
equations in a selected geometrical domain in the model.
Furthermore, the Wave Equation, Electric 1 feature node may link to the 
Materials feature node to obtain physical properties such as relative permittivity — 
in this case the relative permittivity of a user-defined dielectric. The properties, 
defined by the Dielectric material, can be functions of the modeled physical 
quantities, such as temperature. In the same fashion, the Perfect Electric 
Conductor 1 feature adds a reflecting boundary condition to truncate the 
modeling domain.
Figure 9 shows the Radio Frequency (RF) interfaces as displayed in the Model 
Wizard for this module.
Figure 9: The Radio Frequency (R
```

### Section 8

```
13 ---
 | 13
ELECTROMAGNETIC WAVES, TIME EXPLICIT
The Electromagnetic Waves, Time Explicit interface (
) solves a system of two 
first-order partial differential equations (Faraday’s law and Maxwell–Ampère’s 
law) for the electric and magnetic fields using the Time Explicit Discontinuous 
Galerkin method. The sources can be in the form of volumetric electric or 
magnetic currents or electric surface currents or fields on boundaries. It is used 
primarily to model electromagnetic wave propagation in linear media. Typical 
applications involve the transient propagation of electromagnetic pulses.
ELECTROMAGNETIC WAVES, TRANSIENT
The Electromagnetic Waves, Transient interface (
) solves a time-domain wave 
equation for the electric field. The sources can be in the form of point dipoles, line 
currents, or incident fields on boundaries or domains. It is used primarily to model 
electromagnetic wave propagation in different media and structures when a 
time-domain solution is required — for 
```

### Section 9

```
14 ---
14 | 
ELECTROMAGNETIC WAVES, ASYMPTOTIC SCATTERING
The Electromagnetic Waves, Asymptotic Scattering interface (
) is used for 
quick studies of the far-field response of a 3D or 2D object to a given background 
field. The physics interface sets up a surface electric background field for the 
far-field transformation, using the Stratton–Chu formula, performed in the 
postprocessing. Use this physics interface in 2D and 3D when approximating the 
scattered far-field of an object configured only by a perfect electric conductor 
boundary condition.
ELECTROMAGNETIC WAVES, BOUNDARY ELEMENTS
The Electromagnetic Waves, Boundary Elements interface (
) solves a 
frequency-domain wave equation for the electric field. The formulation is based 
on the boundary element method (BEM) and requires the availability of a Green’s 
function. Thus, the physics interface solves the vector Helmholtz equation for 
piecewise-constant material properties.
The interface is fully multiphysics enabled and ca
```

### Section 10

```
15 ---
 | 15
ELECTROMAGNETIC WAVES, FEM-BEM
The Electromagnetic Waves, FEM-BEM multiphysics interface (
) allows to 
build hybrid FEM-BEM models, where the boundary element method (BEM) is 
used to compute the electric fields outside the finite element method (FEM) 
domains. This multiphysics interface adds an Electromagnetic Waves, Frequency 
Domain interface and an Electromagnetic Waves, Boundary Elements interface. 
The multiphysics coupling assures continuity of the tangential electric and 
magnetic fields across boundaries between the two interfaces.
Frequency-domain modeling is supported in 2D and 3D.
Physics Interface Guide by Space Dimension and Study Type
The table below lists the physics interfaces available specifically with this module 
in addition to the COMSOL Multiphysics basic license.
PHYSICS INTERFACE
ICON
TAG
SPACE 
DIMENSION
AVAILABLE STUDY TYPE
 AC/DC
Electrical Circuit
cir
Not space 
dependent
stationary; frequency 
domain; time dependent; 
frequency domain; 
eige
```

### Section 11

```
16 ---
16 | 
Electromagnetic Waves, 
Frequency Domain
emw
3D, 2D, 2D 
axisymmetric
adaptive frequency sweep; 
boundary mode analysis; 
eigenfrequency; frequency 
domain; frequency domain, 
modal; frequency domain, 
RF adaptive mesh; frequency 
domain source sweep; 
mode analysis (2D and 2D 
axisymmetric models only); 
TEM boundary mode 
analysis
Electromagnetic Waves, 
Time Explicit
ewte
3D, 2D, 2D 
axisymmetric
time dependent; time 
dependent with FFT
Electromagnetic Waves, 
Transient
temw
3D, 2D, 2D 
axisymmetric
eigenfrequency; time 
dependent; time dependent, 
modal; time dependent with 
FFT
Transmission Line
tl
3D, 2D, 1D
eigenfrequency; frequency 
domain
Transmission Line, 
Transient
tlt
3D, 2D, 1D
time dependent
Transmission Line, 
Parameters
2D
frequency domain
Electromagnetic Waves, 
FEM-BEM1
3D, 2D
frequency domain
1 This physics interface is a predefined multiphysics coupling that automatically adds all the 
physics interfaces and coupling features required.
PHYSICS INTERFAC
```

### Section 12

```
20 ---
20 | 
with an effective loss tangent of 2·10-4 and ΔH = 3.18·103 A/m, are taken for 
aluminum garnet from Ref. 2. The applied bias field is set to H0 = 7.96·103 A/m. 
The electron gyromagnetic ratio is defined as the ratio between the elementary 
charge and the electron mass.
References
1. R.E. Collin, Foundations for Microwave Engineering, 2nd ed., IEEE Press/
Wiley-Interscience, 2000.
2. D.M. Pozar, Microwave Engineering, 3rd ed., John Wiley & Sons Inc, 2004.
Model Wizard
These step-by-step instructions guide you through the design and modeling of the 
lossy three-port circulator in 3D. The first part involves the geometric design and 
impedance matching at a nominal frequency of 3 GHz. A frequency sweep is then 
performed over a 400 MHz band centered at 3 GHz to evaluate the device 
performance. Finally, the entire S-parameter matrix is computed.
Note: These instructions are for the user interface on Windows but also apply, 
with minor differences, also to Linux and Mac.
1 To
```

### Section 13

```
21 ---
 | 21
4 Click Study 
.
5 In the Studies tree under General Studies, click Frequency Domain 
.
6 Click Done 
.
Global Definitions - Parameters
The geometry is set up using a parameterized approach. This allows you to match 
the input impedance to that of the connecting waveguide sections by variation of 
two geometric design parameters. These are dimensionless numbers used to scale 
selected geometric building blocks.
In this section, multiple parameters are entered to prepare for characterizing the 
ferrite material properties and drawing the circulator geometry which is described 
in the section Geometry Sequence. Alternatively, a predefined application library file 
containing the geometry and parameters can be imported, as described in 
Geometry. If you import the geometry, you only need to review this section for 
information.
1 In the Home toolbar click Parameters
 and select Parameter 1.
Note: On Linux and Mac, the Home toolbar refers to the specific set of controls 
near 
```

### Section 14

```
22 ---
22 | 
Here, e_const, me_const, and mu0_const are predefined COMSOL constants for 
the elementary charge, the electron mass, and the permeability of vacuum, 
respectively.
Geometry
In the Global Definitions section, you entered parameters and imported variables 
in preparation for drawing the geometry. To learn how to draw the circulator, go 
to Geometry Sequence. 
To save time, a predefined model containing the parameters, variables, and 
geometry can be opened from the Application Libraries window. 
1 In the Home toolbar click Windows
 and select Application Libraries
. 
2 In the Application Libraries window, under RF Module > 
Ferrimagnetic Devices double-click lossy circulator 3d geom to open it. 
Discard Untitled.mph, a blank model with parameters created in the previous 
section.
Once the geometry is either drawn or imported, you can then experiment with 
different dimensions by changing the values of sc_chamfer and sc_ferrite and 
rerunning the geometry sequence.
Definitio
```

### Section 15

```
23 ---
 | 23
3 In the Settings window under Variables 1, enter the following variables as 
shown below in the table.
freq is a built-in COMSOL variable representing the frequency in frequency 
domain studies.
Materials
The next step is to assign material properties to the model. The air that fills most 
of the volume is available as a built-in material. The lossy ferrite has user-defined 
properties assigned to it later, which will illustrate how external material data can 
be directly entered into the electromagnetic waves model. The walls of the 
waveguide sections are modeled as perfect electric conductors and do not require 
a material configuration.
1 In the Home toolbar click Add Material 
.
```

### Section 16

```
24 ---
24 | 
2 In the Materials tree under Built-In, right-click Air and choose Add to 
Component 1
.
3 Click Add Material 
 again to close the Add Material window.
Electromagnetic Waves, Frequency Domain 
The ferrite is introduced in the physics interface as a separate, user-defined 
equation model, referring to the global variables defined in the section Global 
Definitions - Parameters.
Wave Equation, Electric 2
1 In the Physics toolbar click Domains 
 and choose Wave Equation, 
Electric
. 
A new node called Wave Equation, Electric 2 is added to the Model Builder. 
The nodes with a ‘D’ in the upper left corner indicate a default node.
2 To get a view of the interior part of the circulator, click the Wireframe 
Rendering button 
 in the Graphics toolbar.
3 In the Settings window for Wave Equation, Electric 2, type Wave Equation, 
Electric 2, Ferrite in the Label text field.
```

### Section 17

```
25 ---
 | 25
4 Select Domain 2 only.
Note: There are many ways to select geometric entities. When you know the 
domain to add, such as in this exercise, you can click the Paste Selection 
button
 located beside the Selection list and enter the information in the 
Selection text field. In this example enter 2 in the Paste Selection window. For 
more information about selecting geometric entities in the Graphics window, see 
the COMSOL Multiphysics Reference Manual.
Domain 2
```

### Section 18

```
26 ---
26 | 
5 Go to the Settings window for Wave 
Equation, Electric 2. Under Electric 
Displacement Field: 
- From the Electric displacement 
field model list, select Loss 
tangent, dissipation factor.
- From the ε′ list, select User 
defined. In the associated text 
field, enter 14.5.
- From the tanδ list, select User 
defined. In the associated text 
field, enter 0.0002.
6 Under Magnetic Field, from the μr 
list, select User defined and Full.
7 In the μr table, enter the settings as 
in the figure to the right.
Now add ports for excitation and transmission.
Port 1, Port 2, and Port 3
1 In the Physics toolbar click Boundaries
 and choose Port 
. Port 1 is added 
to the Model Builder.
2 Select Boundary 1 only for Port 1.
3 Go to the Settings window for Port. Under Port Properties from the Type of 
port list, select Rectangular.
4 For the first port, the Wave excitation 
at this port is On by default.
5 In the Physics toolbar click 
Boundaries 
 and choose Port 
 
to add another Port 
```

### Section 19

```
27 ---
 | 27
6 Add another Port 
 node. For Port 3:
- Select Boundary 19
- Select Rectangular from the Type of port list
The node sequence in the Model Builder should match this figure.
Mesh
The mesh automatically aligns to the geometry. In addition, it needs to resolve the 
local wavelength and the skin depth for each material domain. It is recommended 
to use a maximum mesh size that is at a fifth of the local wavelength (at the 
maximum frequency) or smaller. This can be done by defining the maximum mesh 
size per domain using a Size feature.
```

### Section 20

```
28 ---
28 | 
Free Tetrahedral 1
1 In the Mesh toolbar click Free 
Tetrahedral 
.
2 Right-click Free Tetrahedral 1 
 
and choose Size 
.
3 Go to the Settings window for Size. 
Under Geometric Entity Selection 
from the Geometric entity level list, 
select Domain. 
4 Select Domain 1 only. This is the 
domain filled with air inside the 
waveguide.
5 Under Element Size, click the 
Custom button.
6 Under Element Size Parameters, 
select the Maximum element size 
checkbox. Enter 1.5e-2 in the text 
field.
Size 2
1 Right-click Free Tetrahedral 1
 
and choose Size 
. A second Size 
node is added to the sequence.
2 Go to the Settings window for Size. 
Under Geometric Entity Selection 
from the Geometric entity level list, select Domain.
3 Select Domain 2 only. This is the ferrite post domain.
4 Under Element Size, click the Custom button.
5 Under Element Size Parameters, select the Maximum element size checkbox. 
Enter 4.5e-3 in the text field.
6 In the Settings window for Size click Build All 
```

