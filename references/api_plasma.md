# Plasma Module — API Reference

Extracted from COMSOL 6.4 documentation and mph tags.json.

## Feature Types (76 found)

| Feature Name | Tag | Parent Interface |
|-------------|-----|------------------|
| `PlasmaConductivityMultiphysicsCoupling` | `pcc*` | multiphysics |
| `ColdPlasma` | `plas` | physics |
| `AxialSymmetry` | `axi*` | ColdPlasma |
| `ChargeConservation` | `ccn*` | ColdPlasma |
| `CrossSectionImport` | `xsec*` | ColdPlasma |
| `DielectricContact` | `dct*` | ColdPlasma |
| `DisplacementField` | `df*` | ColdPlasma |
| `ElectronImpactReaction` | `eir*` | ColdPlasma |
| `ElectronOutlet` | `eout*` | ColdPlasma |
| `Ground` | `gnd*` | ColdPlasma |
| `InitialValues` | `init*` | ColdPlasma |
| `Insulation` | `ins*` | ColdPlasma |
| `MetalContact` | `mct*` | ColdPlasma |
| `PlasmaEsModel` | `pes*` | ColdPlasma |
| `Reaction` | `rxn*` | ColdPlasma |
| `Species` | `sp*` | ColdPlasma |
| `Outflow` | `out*` | Species |
| `SurfaceChargeAccumulation` | `sca*` | ColdPlasma |
| `SurfaceReaction` | `sr*` | ColdPlasma |
| `Terminal` | `term*` | ColdPlasma |
| `WallDriftDiffusion` | `wall*` | ColdPlasma |
| `ZeroCharge` | `zc*` | ColdPlasma |
| `PlasmaTimePeriodic` | `ptp` | physics |
| `init` | `init*` | PlasmaTimePeriodic |

## Documentation Structure (api_plasma_extract.txt)

```
  TOC:   Introduction (p.5)
  TOC:     The Use of the Plasma Module (p.5)
  TOC:   Plasma Modeling (p.14)
  TOC:     Physics Guide (p.14)
  TOC:     Physics Interface List by Space Dimension and Preset Study Type (p.15)
  TOC:     Application Specific Interfaces (p.18)
  TOC:     References (p.21)
  TOC:   Argon Discharge in the GEC Reference Cell (p.22)
  TOC:     Model Wizard (p.23)
  TOC:     Importing the Geometry (p.23)
  TOC:     Definitions (p.24)
  TOC:     Plasma and Magnetic Fields (p.25)
  TOC:     Materials (p.28)
  TOC:     Mesh (p.31)
  TOC:     Study (p.33)
  TOC:     Results (p.33)
  TOC:     Bibliography (p.41)
  TOC:   Contents (p.3)
  TOC:   Introduction (p.17)
  TOC:     About the Plasma Module (p.18)
  TOC:       How the Plasma Module Improves Your Modeling (p.18)
  TOC:       Plasma Module Nomenclature (p.20)
  TOC:       The Plasma Module Physics Interface Guide (p.22)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.24)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.25)
  TOC:     Overview of the User’s Guide (p.28)
  TOC:   Data Required for Plasma Modeling (p.33)
  TOC:     Data Requirements (p.34)
  TOC:       Electron Impact Reactions (p.34)
  TOC:       Reaction (p.36)
  TOC:       Surface Reaction (p.36)
  TOC:       Species (p.37)
  TOC:     Importing Collision Cross-Section Data (p.39)
  TOC:       Cross-Section Data File Format (p.39)
  TOC:       The File Format (p.40)
  TOC:       References for the Plasma Module Cross-Section Data Requirements (p.42)
  TOC:     Plasma Chemistry Import (p.43)
  TOC:       Introduction (p.43)
  TOC:       Plasma Chemistry File Format (p.43)
  TOC:   The Boltzmann Equation, Two-Term Approximation Interface (p.49)
  TOC:     The Boltzmann Equation, Two-Term Approximation Interface (p.50)
  TOC:       Global Nodes for the Boltzmann Equation, Two-Term Approximation Interface (p.53)
  TOC:       Boltzmann Model (p.54)
  TOC:       Initial Values (p.55)
  TOC:       Cross Section Import (p.56)
  TOC:       Electron Impact Reaction (p.56)
  TOC:     Theory for the Boltzmann Equation, Two-Term Approximation Interface (p.58)
```

## Key API Content (46 sections)

### Section 1

```
=== IntroductionToPlasmaModule.pdf ===
Pages: 42
  TOC:   Introduction (p.5)
  TOC:     The Use of the Plasma Module (p.5)
  TOC:   Plasma Modeling (p.14)
  TOC:     Physics Guide (p.14)
  TOC:     Physics Interface List by Space Dimension and Preset Study Type (p.15)
  TOC:     Application Specific Interfaces (p.18)
  TOC:     References (p.21)
  TOC:   Argon Discharge in the GEC Reference Cell (p.22)
  TOC:     Model Wizard (p.23)
  TOC:     Importing the Geometry (p.23)
  TOC:     Definitions (p.24)
  TOC:     Plasma and Magnetic Fields (p.25)
  TOC:     Materials (p.28)
  TOC:     Mesh (p.31)
  TOC:     Study (p.33)
  TOC:     Results (p.33)
  TOC:     Bibliography (p.41)
```

### Section 2

```
3 ---
 | 3
Contents
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
The Use of the Plasma Module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
Plasma Modeling  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .14
Physics Guide  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
Physics Interface List by Space Dimension and Preset Study Type15
Application Specific Interfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Argon Discharge in the GEC Reference Cell. . . . . . . . . . . . . . .22
```

### Section 3

```
5 ---
 | 5
Introduction
The Plasma Module is specifically designed for the modeling and simulation of 
both low-temperature and equilibrium plasma systems. It empowers engineers 
and scientists to investigate discharge physics and assess the performance of both 
existing and conceptual plasma designs.
Supporting simulations in 0D, 1D, 2D, and 3D, the Plasma Module addresses the 
complex and highly nonlinear nature of plasma behavior, where even small 
changes in parameters like electrical input, pressure, or plasma chemistry can lead 
to significant variations in discharge characteristics.
Plasma systems involve a wide range of interconnected physical phenomena, 
including fluid dynamics, reaction kinetics, heat and mass transfer, and 
electromagnetism. The Plasma Module offers specialized tools for accurately 
simulating both non-equilibrium and equilibrium discharges across a broad 
spectrum of engineering applications. It includes:
• A comprehensive suite of physics interfaces for b
```

### Section 4

```
6 ---
6 | 
In addition, the Plasma Module supports the modeling of Equilibrium Discharges, 
where all species share a common temperature and the plasma is assumed to be 
fully ionized.
DIRECT CURRENT DISCHARGES
Direct current (DC) discharges are typically sustained through secondary electron 
emission from the cathode, triggered by ion bombardment. Electrons emitted 
from the cathode are accelerated through the cathode fall region, gaining energy 
as they enter the bulk plasma. If they acquire sufficient energy, these electrons can 
ionize the background gas, producing new electron-ion pairs. The resulting 
electrons travel toward the anode, while the ions migrate back to the cathode, 
where they may generate additional secondary electrons.
The discharge dynamics are such that most of the applied electric potential drops 
across the cathode fall region, a narrow zone near the cathode. Within this region, 
electron density and flux increase exponentially. Under certain conditions, the 

```

### Section 5

```
8 ---
8 | 
CAPACITIVELY COUPLED PLASMAS
Capacitively coupled plasmas (CCPs) are widely used in the semiconductor 
industry for thin film deposition and etching applications. In typical industrial 
setups, the plasma is generated between parallel plate electrodes spaced about 3 
cm apart, with electrode diameters often reaching 30 cm. These systems usually 
operate at frequencies ranging from 100 kHz to 100 MHz and at pressures 
between 2 and 200 Pa. Although CCP sources can also operate at atmospheric 
pressure, doing so requires a much smaller discharge gap, typically on the order of 
a millimeter, to maintain a manageable pressure–distance (pd) product and ensure 
stable discharge conditions.
In CCP discharges, the charged species dynamics can create regions of intense 
charge separation at the electrodes that are strongly time modulated, the so-called 
plasma sheaths. Within the sheaths, intense electric fields accelerate electrons to 
energies sufficient for ionization, thus sustai
```

### Section 6

```
11 ---
 | 11
PLASMA ENHANCED CHEMICAL VAPOR DEPOSITION
Plasma enhanced chemical vapor deposition (PECVD) is a widely used 
plasma-assisted thin-film deposition technique that enables the formation of 
high-quality coatings at relatively low substrate temperatures. By utilizing reactive 
plasma species generated from precursor gases, PECVD facilitates enhanced 
chemical reactions on the substrate surface, resulting in improved film properties. 
Modeling PECVD processes requires capturing the complex interplay between 
plasma dynamics, gas-phase chemistry, surface reactions, and transport 
phenomena. The Plasma Module provides comprehensive tools to simulate these 
coupled physical and chemical processes, enabling detailed analysis and 
optimization of PECVD reactor performance.
Variation of silicon deposition rate along the wafer with silane mole fraction in an inductively coupled 
plasma reactor using a silane-argon mixture at 13.56 MHz and 50 W.
PLASMA ENHANCED ETCHING
Plasma enhanced
```

### Section 7

```
15 ---
 | 15
as the electric field and electron-impact reactions that define the plasma chemistry, 
all without needing to solve a space-dependent problem.
For space-dependent models, the plasma chemistry (comprising reactions and 
species) is conveniently managed within the Model Builder. When fluid velocity 
and gas temperature are relevant, dedicated physics interfaces for laminar flow and 
heat transfer are available. Additionally, several options exist to couple charged 
species transport with electromagnetic fields, offering flexibility in modeling the 
plasma environment.
Physics Interface List by Space Dimension and Preset Study Type
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
eigenfrequency
Electrostatics1
es
all dimensions
stationary; time dependent; 
stationary source sweep
 Fluid Flow
 Single-Phase Flow
Laminar Flow1
spf
3D, 2D, 2D 
axis
```

### Section 8

```
16 ---
16 | 
Inductively Coupled 
Plasma2,4
—
3D, 2D, 2D 
axisymmetric.
frequency–transient; 
frequency–stationary
Inductively Coupled Plasma 
with RF Bias2,4
—
2D, 2D 
axisymmetric.
frequency-time periodic; 
time periodic to time 
dependent
Microwave Plasma3,4
—
3D, 2D, 2D 
axisymmetric
frequency–transient
 Nonisothermal Plasma Flow
Plasma, Nonisothermal 
Flow4
—
3D, 2D, 2D 
axisymmetric.
time dependent; stationary
Inductively Coupled 
Plasma, Nonisothermal 
Flow2,4
—
3D, 2D, 2D 
axisymmetric.
frequency–transient; 
frequency–stationary
Microwave Plasma, 
Nonisothermal Flow3,4
—
3D, 2D, 2D 
axisymmetric.
frequency-transient
Plasma, Time Periodic, 
Nonisothermal Flow4
—
2D, 2D 
axisymmetric.
time periodic; time periodic 
to time dependent
Inductively Coupled 
Plasma with RF Bias, 
Nonisothermal Flow2,4
—
2D, 2D 
axisymmetric.
frequency-time periodic; 
time periodic to time 
dependent
 Equilibrium Discharges
Equilibrium Discharges, 
Out-of-Plane 
Currents2,4
—
2D, 2D 
axisymmetric
statio
```

### Section 9

```
17 ---
 | 17
AC/DC INTERFACES
The AC/DC Branch chapter describes the two physics interfaces available with 
this module under the AC/DC branch of the Model Wizard. Many of the plasma 
interfaces already solve Poisson’s equation, and volume and surface charges are 
automatically accounted for. This means that the Electrostatics interface will rarely 
need to be used.
FLUID FLOW INTERFACES
The Fluid Flow Branch describes the Laminar Flow interface, which has a few 
additional features available for this module compared to the basic license.
BOLTZMANN EQUATION, TWO-TERM APPROXIMATION INTERFACE
The Boltzmann Equation, Two-Term Approximation interface 
 computes the 
electron energy distribution function (EEDF) from a set of collision cross sections 
for some mean discharge conditions. The interface can be used as a preprocessing 
stage before solving a full space dependent model. The main purpose of this 
interface is to compute electron source coefficients and transport properties.
DRIFT 
```

### Section 10

```
18 ---
18 | 
available to handle secondary emission, thermionic emission, and wall losses. This 
interface rarely needs to be used by itself as it makes up part of the application 
specific interfaces described later.
CHARGE TRANSPORT
The Charge Transport interface computes the density of charge carriers in a 
background gas under the assumption that the transport is dominated by 
migration. This is typically only used as part of the Corona Discharge multiphysics 
interface (see below).
THE HEAVY SPECIES INTERFACE
The Heavy Species Transport interface 
 solves a mass balance equation for all 
nonelectron species. This includes charged, neutral, and electronically excited 
species. The interface also allows you to add electron impact reactions, chemical 
reactions, surface reactions, volumetric species, and surface species via the Model 
Builder. This interface rarely needs to be used by itself as it makes up part of the 
application specific interfaces described later.
Application Spec
```

### Section 11

```
19 ---
 | 19
underlying mathematical equations representing one RF cycle, and enforcing 
periodic boundary conditions in the aforementioned extra dimension.
INDUCTIVELY COUPLED PLASMA
The Inductively Coupled Plasma interface 
 can be used to model discharges 
sustained through induction currents. These discharges typically operate in the 
MHz frequency range. Inductively coupled plasmas (ICP) are important in plasma 
processing and plasma sources because the plasma density can be considerably 
higher than in capacitively coupled discharges. Inductively coupled plasmas are 
also attractive from the modeling perspective because they are relatively 
straightforward to model, due to the fact that the induction currents can be solved 
for in the frequency domain. This means that the RF cycle applied to the driving 
coil does not need to be explicitly resolved when solving. As such, the quasi 
steady-state solution is reached in relatively few time steps.
INDUCTIVELY COUPLED PLASMA WITH RF B
```

### Section 12

```
20 ---
20 | 
when there are important fluid velocities and when the background gas 
temperature depends strongly on the operation conditions.
EQUILIBRIUM DISCHARGES, OUT-OF-PLANE CURRENTS
The Equilibrium Discharges, Out-of-plane Currents 
 multiphysics interface, 
available in 2D and 2D axisymmetric, is used to study equilibrium discharges in a 
magnetohydrodynamics (MHD) framework where the currents are out-of-plane. 
This multiphysics interface adds three single physics interfaces: Magnetic Fields, 
Heat Transfer in Fluids, and Laminar Flow, together with several multiphysics 
coupling features. The multiphysics couplings add the MHD coupling between 
the Magnetic Fields and the Laminar Flow interfaces. The multiphysics couplings 
also add heating and cooling of the equilibrium plasma by enthalpy transport, 
Joule heating and radiation loss.
EQUILIBRIUM DISCHARGES, IN-PLANE CURRENTS
The Equilibrium Discharges, in-plane Currents 
 multiphysics interface, 
available in 2D and 2D axisym
```

### Section 13

```
21 ---
 | 21
CORONA DISCHARGE
The Corona Discharge interface employs a simplified charge transport model 
combined with electrostatics to approximate the charge density and electrostatic 
field in stationary corona discharges. This model does not include the ionization 
layer of corona discharges, instead utilizing an approximate boundary condition. 
Additionally, electron dynamics are not solved in this approach.
ELECTRICAL BREAKDOWN DETECTION
The Electrical Breakdown Detection interfaces uses an approximate method to 
determine if electrical breakdown will occur in a given design by integrating 
Townsend growth coefficients along electric field lines.
LIMITATIONS OF THE PLASMA MODULE
The Plasma module cannot model plasmas that are not collisional enough for the 
fluid-type equations used to be valid. For reactors with characteristic dimensions 
of 10 cm the lower possible pressure would be 20 mTorr.
References
1. A. Bogaerts, E. Neyts, R. Gijbels, and J. van der Mullen, “Gas discharg
```

### Section 14

```
23 ---
 | 23
which increases the coil’s effective resistance. The current flowing through the 
plasma depends both on the coil current and the plasma’s reaction kinetics. The 
total plasma current can range from zero (when the plasma is not sustained) to 
matching the primary coil current, which represents perfect coupling between the 
coil and plasma. In this example, the coil is powered at a fixed input of 1500 W.
Model Wizard
The first step to build a model is to open the COMSOL Desktop and then specify 
the type of analysis you want to do — in this case, a frequency-transient inductively 
coupled plasma analysis. The frequency-transient study type means that the high 
frequency electromagnetic field is computed in the frequency domain and all other 
variables are computed in the time domain.
Note: These instructions are for the user interface on Windows® but apply, with 
minor differences, also to Linux® and macOS.
1 Open COMSOL Multiphysics. In the New window, click the Model Wiza
```

### Section 15

```
24 ---
24 | 
2 Browse to the folder Plasma_Module\Inductively_Coupled_Plasmas under the 
COMSOL installation directory and double-click on the file 
argon_gec_icp_geom.mph.
3 Click the Import button. The geometry should appear in the Graphics window 
as shown below.
Definitions
1 In the Definitions toolbar, click Explicit 
.
2 In the Settings window, type Walls in the Label field.
3 Locate the Input Entities section.
4 From the Geometric entity level list, choose Boundary.
5 Go to the Home tab on the Model desktop toolbar, then choose Windows > 
Selection List.
6 Select Boundaries 6, 8, 35–38, 44, 45, and 51–56 only (by holding shown shift 
and clicking on the list), then click the Add to selection button 
 at the top 
of the Selection List settings window. The selected boundaries in the graphics 
window will turn blue, indicating that the selection is confirmed.
7 Click back on the Model Builder tab.
```

### Section 16

```
25 ---
 | 25
8 In the Definitions toolbar, click Explicit 
.
9 In the Settings window, type Coils in the Label field.
10Click on the Selection List tab and select Domains 6 and 8–11 only, then click 
the Add to selection button 
 at the top of the Selection List settings window.
11Click back on the Model Builder tab.
12In the Definitions toolbar, click Explicit 
.
13In the Settings window, type Coil Boundaries in the Label field.
14Click on the Selection List tab and select Domains 6 and 8–11 only, then click 
the Add to selection button 
 at the top of the Selection List settings window.
15Click back on the Model Builder tab. In the Explicit settings window, locate the 
Output Entities section.
16From the Output entities list, choose Adjacent boundaries.
17Go to the Model desktop toolbar.
18In the Home toolbar, click Parameters 
 and select Parameters 1
.
19In the Parameters settings window, locate the Parameters section.
In the table, enter the following settings:
Plasma and Magnetic
```

### Section 17

```
26 ---
26 | 
4 In the Model Builder window, right-click Plasma and choose Cross Section 
Import.
5 In the Cross Section Import settings window, locate the Cross Section Import 
section.
6 Click the Browse button.
7 Browse to the module Application Library folder and double-click the file 
Ar_xsecs.txt.
Now you add two more regular reactions which describe how electronically 
excited argon atoms are consumed on the volumetric level. The rate coefficients 
for these reactions are taken from the literature.
1 In the Model Builder window, right-click Plasma and choose the domain setting 
Heavy Species Transport > Reaction 
.
2 In the Reaction settings window, locate the Reaction Formula section.
3 In the Formula field, type Ars+Ars=>e+Ar+Ar+. Click off the settings window.
4 Locate the Kinetics Expressions section. In the kf field, type 3.734E8.
5 In the Model Builder window, right-click Plasma and choose the domain setting 
Heavy Species Transport > Reaction 
.
6 In the Reaction settings 
```

### Section 18

```
27 ---
 | 27
3 Select the Initial value from electroneutrality constraint checkbox.
Initial conditions for the electron number density and mean electron energy are 
critical for any plasma model. If the initial electron density is too low then the 
plasma may not be able to sustain itself and may self-extinguish. If the initial 
electron density is too high then convergence problems may occur during initial 
time steps.
1 In the Model Builder window, under Component 1 > Plasma click Initial Values 
1 
.
2 In the Initial Values settings window, locate the Initial Values section.
3 In the ne,0 field, type 1E15[1/m^3].
4 In the ε0 field, type 5[V].
5 In the Model Builder window, under Component 1 > Plasma click Plasma 
Model 1 
.
6 In the Plasma Model settings window, locate the Model Inputs section.
7 In the T field, type T0.
8 In the pA field, type p0.
9 Locate the Electron Density and Energy section. In the μeNn field, type mueN.
Surface reactions must always be included in a plasma mo
```

### Section 19

```
28 ---
28 | 
3 In the re field, type 0.2.
4 Locate the Boundary Selection section. From the Selection list, choose Walls.
5 In the Physics toolbar, click Boundaries and choose Ground 
.
6 In the Ground settings window, locate the Boundary Selection section.
7 From the Selection list, choose Walls.
You need to compute the AC electric field both inside and outside the plasma. It 
is not necessary to compute the high frequency fields in the wafer or wafer 
pedestal, so start by modifying the selection for the Magnetic Fields interface.
1 In the Model Builder window, click Magnetic Fields.
2 Select Domains 3–6 and 8–12 only.
The Coil feature allows you to drive the system with a fixed total power. Some of 
this power will be dissipated in the coil, the rest will be coupled into the plasma. 
In this example 1500 W are applied to the system. This results in a plasma with a 
high number density. You also need to specify the gas temperature and pressure.
1 In the Model Builder window, right-cl
```

### Section 20

```
29 ---
 | 29
5 In the Model Builder window, under Component 1 right-click Materials and 
choose Blank Material 
.
6 In the Material settings window, locate the Geometric Entity Selection section. 
Select Domain 5 only. In the table, enter the following settings:
```

