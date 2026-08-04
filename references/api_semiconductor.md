# Semiconductor Module — API Reference

Extracted from COMSOL 6.4 documentation and mph tags.json.

## Feature Types (72 found)

| Feature Name | Tag | Parent Interface |
|-------------|-----|------------------|
| `SemiconductorElectromagneticWavesCoupling` | `semc*` | multiphysics |
| `Semiconductor` | `semi` | physics |
| `AURecombination` | `aur*` | Semiconductor |
| `AnalyticDopingModel` | `adm*` | Semiconductor |
| `AxialSymmetry` | `axi*` | Semiconductor |
| `ChargeConservation` | `ccn*` | Semiconductor |
| `Continuity` | `cont*` | Semiconductor |
| `WKBTunnelingModelElectrons` | `wkbe*` | Continuity |
| `FloatingGate` | `fg*` | Semiconductor |
| `GateContact` | `gc*` | Semiconductor |
| `HarmonicPerturbation` | `hp*` | GateContact |
| `GeometricDopingModel` | `gdm*` | Semiconductor |
| `BoundarySelectionForDopingProfile` | `gdmbs*` | GeometricDopingModel |
| `GlobalEquations` | `ge*` | Semiconductor |
| `IIGeneration` | `iig*` | Semiconductor |
| `Insulation` | `ins*` | Semiconductor |
| `InsulatorInterface` | `ii*` | Semiconductor |
| `MetalContact` | `mc*` | Semiconductor |
| `OpticalTransitions` | `ot*` | Semiconductor |
| `SemiconductorMaterialModel` | `smm*` | Semiconductor |
| `AroraMobilityModel` | `mmar*` | SemiconductorMaterialModel |
| `CaugheyThomasMobilityModel` | `mmct*` | SemiconductorMaterialModel |
| `FletcherMobilityModel` | `mmfl*` | SemiconductorMaterialModel |
| `LombardiSurfaceMobilityModel` | `mmls*` | SemiconductorMaterialModel |
| `SurfaceChargeDensity` | `sfcd*` | Semiconductor |
| `Terminal` | `term*` | Semiconductor |
| `TrapAssistedRecombination` | `tar*` | Semiconductor |
| `TrapAssistedSurfaceRecombination` | `tasr*` | Semiconductor |
| `ContinuousEnergyLevelsBoundary` | `ctb*` | TrapAssistedSurfaceRecombination |
| `DiscreteEnergyLevelBoundary` | `dtb*` | TrapAssistedSurfaceRecombination |
| `UDGeneration` | `udg*` | Semiconductor |
| `ZeroCharge` | `zc*` | Semiconductor |
| `init` | `init*` | Semiconductor |
| `SemiconductorEquilibrium` | `semie` | ? |
| `SemiconductorInitialization` | `semii` | ? |

## Documentation Structure (api_semiconductor_extract.txt)

```
  TOC:   Introduction (p.5)
  TOC:   Semiconductor Devices (p.7)
  TOC:   The Semiconductor Module Physics Interface Guide (p.12)
  TOC:     Physics Interface Guide by Space Dimension and Study Type (p.17)
  TOC:   Learning Resources (p.19)
  TOC:   Tutorial Model: DC Characteristics of a MOSFET (p.20)
  TOC:     Model Wizard (p.22)
  TOC:     Global Definitions (p.22)
  TOC:     Geometry 1 (p.23)
  TOC:     Materials (p.25)
  TOC:     Semiconductor (p.25)
  TOC:     Mesh 1 (p.31)
  TOC:     Study 1 (p.35)
  TOC:     Results (p.35)
  TOC:     Study 1 (p.36)
  TOC:     Results (p.37)
  TOC:     Study 2 (p.41)
  TOC:     Results (p.42)
  TOC:   Contents (p.3)
  TOC:   Introduction (p.11)
  TOC:     About the Semiconductor Module (p.12)
  TOC:       Modeling Semiconductor Devices (p.12)
  TOC:       What Can the Semiconductor Module Do? (p.13)
  TOC:       The Semiconductor Module Physics Interface Guide (p.13)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.15)
  TOC:       The Semiconductor Module Study Capabilities by Physics Interface (p.15)
  TOC:       The Semiconductor Materials Database (p.17)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.17)
  TOC:         The Documentation and Online Help (p.17)
  TOC:         The Application Libraries Window (p.18)
  TOC:         Contacting COMSOL by Email (p.19)
  TOC:         COMSOL Access and Technical Support (p.19)
  TOC:         COMSOL Online Resources (p.19)
  TOC:     Overview of the User’s Guide (p.20)
  TOC:       Modeling SEMICONDUCTORS (p.20)
  TOC:       The Semiconductor Branch Interfaces (p.20)
  TOC:       The AC/DC Branch Interfaces (p.20)
  TOC:       the Electric Discharge Branch interfaces (p.20)
  TOC:   Modeling Guidelines (p.21)
  TOC:     Physics for Semiconductor Modeling (p.22)
  TOC:       Zero Reference of Electric Potential (p.23)
  TOC:       Units of Band Gap and Electron Affinity (p.23)
  TOC:     Discretization and Formulation Options (p.25)
  TOC:     Defining the Carrier Mobility (p.28)
  TOC:     Doping (p.30)
  TOC:       Using the Analytic Doping Model (p.30)
  TOC:         Analytic Doping Model: User Defined (p.30)
  TOC:         Analytic Doping Model: Box (p.31)
```

## Key API Content (52 sections)

### Section 1

```
=== IntroductionToSemiconductorModule.pdf ===
Pages: 44
  TOC:   Introduction (p.5)
  TOC:   Semiconductor Devices (p.7)
  TOC:   The Semiconductor Module Physics Interface Guide (p.12)
  TOC:     Physics Interface Guide by Space Dimension and Study Type (p.17)
  TOC:   Learning Resources (p.19)
  TOC:   Tutorial Model: DC Characteristics of a MOSFET (p.20)
  TOC:     Model Wizard (p.22)
  TOC:     Global Definitions (p.22)
  TOC:     Geometry 1 (p.23)
  TOC:     Materials (p.25)
  TOC:     Semiconductor (p.25)
  TOC:     Mesh 1 (p.31)
  TOC:     Study 1 (p.35)
  TOC:     Results (p.35)
  TOC:     Study 1 (p.36)
  TOC:     Results (p.37)
  TOC:     Study 2 (p.41)
  TOC:     Results (p.42)
```

### Section 2

```
3 ---
 | 3
Contents
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
Semiconductor Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
The Semiconductor Module Physics Interface Guide . . . . . . . .12
Physics Interface Guide by Space Dimension and Study Type . . . 17
Learning Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19
Tutorial Model: DC Characteristics of a MOSFET. . . . . . . . . . .20
```

### Section 3

```
5 ---
 | 5
Introduction
Device engineers and physicists use the Semiconductor Module to design and 
optimize semiconductor devices. For many years semiconductor device design has 
been closely associated with the use of simulation tools, due to the high cost of 
prototyping new devices and processes. The advance of nanotechnology and 
organic semiconductors has helped create many novel devices. Researchers in 
these fields also use simulation to assist the fundamental understanding and design 
optimization. For all of the systems mentioned above, multiphysics effects often 
play an important role, and COMSOL Multiphysics is the ideal platform for 
investigating these effects.
The Semiconductor Module includes a predefined Semiconductor interface, 
which is based on the conventional drift–diffusion formulation. An optional 
density-gradient implementation is also available to provide a computationally 
efficient method to add the effect of quantum confinement to the drift–diffusion 
equ
```

### Section 4

```
6 ---
6 | 
or coding is required. These user-defined mobility models can be combined 
arbitrarily with the predefined mobility models built into the software. When 
COMSOL Multiphysics compiles the equations, the complex couplings generated 
by these user-defined expressions are automatically included in the equation 
system. The equations are then solved using a range of state-of-the-art solvers.
Once a solution is obtained, a large range of result analysis tools are available to 
interrogate the data, and predefined plots are automatically generated to show the 
device response. COMSOL Multiphysics offers the flexibility to evaluate a wide 
range of physical quantities including predefined quantities such as the electron 
and hole currents (including current components from drift, diffusion, and 
thermal diffusion), the electric field, the generation–recombination rate, and the 
temperature, all available through easy-to-use menus, as well as arbitrary 
user-defined expressions.
To m
```

### Section 5

```
7 ---
 | 7
Semiconductor Devices
The Semiconductor Module can be applied to solve a range of device simulation 
problems. The Semiconductor interface can be straightforwardly coupled with 
other physics interfaces, such as the Electromagnetic waves interfaces (using the 
predefined Semiconductor Optoelectronics multiphysics coupling), the Heat 
Transfer in Solids interface and the Electrical Circuits interface. Coupling to a 
circuit is straightforward using the terminals included with appropriate boundary 
conditions. Figure 1 shows results obtained from a 2D p–n junction model in 
which a device model of a diode is coupled to an electrical circuit to produce a 
rectifier. The electron and hole concentrations are shown in the plots when 
different voltages are applied to the circuit.
Figure 1: Electron and hole concentrations in a p–n junction diode connected to a series resistor under 
different bias conditions. This plot shows clearly the changing geometry and extent of the depletio
```

### Section 6

```
8 ---
8 | 
domain (with mixed DC and AC signals, using the small signal analysis study 
type).
A number of standard analyses are illustrated with the MOSFET model series, 
which shows how to include a range of increasingly complicated semiconductor 
physics effects using features included within the Semiconductor interface. The 
first model in the MOSFET series is described in the section Tutorial Model: DC 
Characteristics of a MOSFET, below. Figure 2 shows some of the results obtained 
from this analysis.
Figure 2: Stationary analysis of a MOSFET. The plot shows the drain current plotted against the drain 
voltage (Vd) for a range of different values of the gate voltage (Vg) The inset shows the logarithm of the 
electron concentration (in units of cm-3) for a gate voltage of 4 V and for a drain voltage of 1 V. The 
channel is clearly visible.
In addition to the MOSFET model series, a wide array of other example models 
are available. The Bipolar Transistor model sequence gives an exa
```

### Section 7

```
9 ---
 | 9
the electrochemistry physics. The Heterojunction Tunneling model shows how to 
add tunneling current contributions using the WKB approximation. The Interface 
Trapping Effects of A MOSCAP model does what its name suggests. The pair of 
models Reverse Recovery of a PIN Diode and Forward Recovery of a PIN Diode 
demonstrates the modeling of carrier dynamics with a time dependent study.
Several individual models are also provided, including a MESFET, an EEPROM 
device, a solar cell, a photodiode, and some LED models. Figure 3 shows the 
electron and hole currents flowing in a simple 2D Bipolar transistor.
Figure 3: Electric potential in V (color) and direction of the current flow for electrons (black arrows) and 
holes (white arrows) in a simple 2D bipolar transistor.
```

### Section 8

```
11 ---
 | 11
The Schrödinger Equation interface enables the modeling of various 
quantum-confined systems. The following graph shows the wave functions shifted 
by the respective energy levels for the resonant tunneling conditions of a double 
barrier structure.
The Schrödinger–Poisson Equation interface adds the Electrostatics physics to 
take into account the effects of the charge density of the carriers. The following 
graph shows the self-consistent result of electrons confined in a quantum wire.
```

### Section 9

```
12 ---
12 | 
The Semiconductor Module Physics Interface Guide
Each COMSOL Multiphysics physics interface (for example, the Semiconductor 
interface or the Schrödinger Equation interface) expresses the relevant physical 
phenomena in the form of sets of partial or ordinary differential equations, 
together with appropriate boundary and initial conditions. Each feature added to 
the physics interface represents a term or condition in the underlying equation set. 
These features are usually associated with a geometric entity within the model, 
such as a domain, boundary, edge, or point.
Figure 5 uses a model similar to the MOSFET application library example to show 
the Model Builder tree structure, and the Settings window for the selected 
Semiconductor Material Model 1 feature node. This node adds the 
semiconductor equations to the simulation within the domains selected. In the 
Model Inputs section the temperature of the material is specified. It is 
straightforward to link this tempe
```

### Section 10

```
13 ---
 | 13
Figure 5: The Model Builder (to the left), and the Settings window for Semiconductor Material Model1 
for the selected feature node (to the right). The Equation section in the Settings window shows the model 
equations.
{
Highlighted
Additive
Boundary
conditions
Equations
Material properties are obtained
from the built-in material library
in this model
Material
temperature
node shown
in settings
window
doping
features
the feature
added by
{
```

### Section 11

```
14 ---
14 | 
The Semiconductor interface is the starting point for most simulations. The 
Semiconductor Module also includes physics interfaces to enable modeling of 
different physical situations encountered in device design. When a new model is 
started, these physics interfaces are selected from the Model Wizard.
Figure 6 shows the physics interfaces included with the Semiconductor Module. 
The two Semiconductor Optoelectronics interfaces are only available with an 
additional Wave Optics module license.
Figure 6: The Semiconductor Module interfaces as displayed in the Model Wizard for a 3D model. The 
Semiconductor Optoelectronics interfaces are only available with an additional Wave Optics Module 
license.
Also see Physics Interface Guide by Space Dimension and Study Type. Below, a brief 
overview of each of the Semiconductor Module physics interfaces is given.
ELECTROSTATICS
The Electrostatics interface (
), found under the AC/DC branch in the Model 
Wizard, solves for the electr
```

### Section 12

```
15 ---
 | 15
TRANSPORT OF CHARGE CARRIERS
The Transport of Charge Carriers interface (
) is used to solve the number 
density of one or multiple charge carriers. The charge carriers can be charged 
species such as electrons, ions, and neutral species like molecules and their excited 
states. Transport and reactions of charge carriers can be handled with this 
interface. The driving forces for transport can be drift when coupled to an 
electromagnetic field, convection when coupled to a flow field, and diffusion.
SEMICONDUCTOR
The Semiconductor interface (
), found under the Semiconductor branch in the 
Model Wizard, solves the drift–diffusion and Poisson’s equations. The physics 
interface allows both insulating and semiconducting domains to be modeled. The 
equations account fully for thermal effects, and the interface can be coupled to a 
heat transfer interface using the temperature model input and the predefined heat 
source term. This physics interface is appropriate for modeling 
```

### Section 13

```
16 ---
16 | 
Wave Equation, Electric feature in the Electromagnetic Waves, Frequency 
Domain interface. Additionally spontaneous emission (for direct band-gap 
materials) is accounted for. The effect of the light adsorption or emission is 
accounted for by a corresponding change in the complex permittivity or refractive 
index in the Wave Equation, Electric feature.
This multiphysics interface can be used for modeling devices such as photodiodes, 
light emitting diodes and laser diodes without quantum wells in direct band gap 
materials.
SCHRÖDINGER EQUATION
The Schrödinger Equation interface (
), found under the Semiconductor 
branch in the Model Wizard, solves the Schrödinger equation for a single particle 
in an external potential. This physics interface is useful for general quantum 
mechanical problems as well as for quantum confined systems such as quantum 
wells, wires, and dots (with the envelope function approximation).
SCHRÖDINGER–POISSON EQUATION
The Schrödinger–Poisson Equa
```

### Section 14

```
17 ---
 | 17
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
eigenfrequency
Electrostatics1
es
all dimensions
stationary; time dependent; 
stationary source sweep; 
eigenfrequency; frequency 
domain; small signal analysis, 
frequency domain
 Electric Discharge
Transport of Charge 
Carriers
tcc
all dimensions
time dependent; stationary; 
frequency domain 
perturbation
 Semiconductor
Semiconductor
semi
all dimensions
small-signal analysis, 
frequency domain; 
stationary; time dependent; 
semiconductor equilibrium
Semiconductor 
Optoelectronics, Beam 
Envelopes2
—
3D, 2D, and 
2D 
axisymmetric
frequency–stationary; 
frequency–transient; 
small-signal analysis, 

```

### Section 15

```
18 ---
18 | 
Schrödinger–Poisson 
Equation
—
all dimensions
Schrödinger–Poisson
1 This physics interface is included with the core COMSOL package but has added functionality 
for this module.
2 Requires both the Wave Optics Module and the Semiconductor Module.
PHYSICS INTERFACE
ICON
TAG
SPACE 
DIMENSION
AVAILABLE STUDY TYPE
```

### Section 16

```
19 ---
 | 19
Learning Resources
In addition to the tutorial model in the next section (Tutorial Model: DC 
Characteristics of a MOSFET), there are many examples in the Application Libraries. 
Every example is accompanied by a PDF documentation with step-by-step instructions and 
useful comments. The examples can be accessed either online (www.comsol.com/models/
semiconductor-module) or within the software by going to the File menu > Application 
Libraries > Semiconductor Module.
For users interested in the drift–diffusion type of formulations, we recommend to 
start with the simple model of a p–n junction with user-defined generation for a 
silicon solar cell: www.comsol.com/model/si-solar-cell-1d-35661. This gives a quick 
introduction to building a semiconductor model from scratch.
Next, the 1D heterojunction model demonstrates standard techniques to achieve 
convergence (see comments in the accompanying PDF documentation): 
www.comsol.com/model/heterojunction-1d-14617.
The tutorial 
```

### Section 17

```
20 ---
20 | 
Tutorial Model: DC Characteristics of a MOSFET
This tutorial calculates the DC characteristics of a MOS (metal–oxide– 
semiconductor) transistor. The MOSFET (metal oxide semiconductor field-effect 
transistor) is by far the most common semiconductor device, and the primary 
building block in all commercial processors, memories, and digital integrated 
circuits. Since the first microprocessors were introduced approximately 40 years 
ago this device has experienced tremendous development, and today it is being 
manufactured with feature sizes of 22 nm and smaller.
The MOSFET is essentially a miniaturized switch. In this example the source and 
drain contacts (the input and output of the switch) are both ohmic (low 
resistance) contacts to heavily doped n-type regions of the device. Between these 
two contacts is a region of p-type semiconductor. The gate contact lies above the 
p-type semiconductor, slightly overlapping the two n-type regions. It is separated 
from the semic
```

### Section 18

```
21 ---
 | 21
Figure 8: Cross-section TEM (transmission electron microscopy) image of a 50 nm gate length MOSFET 
fabricated at KTH Electrum laboratory by P.E Hellström and coworkers within the ERC advanced grant 
OSIRIS research project headed by Prof. M. Östling.
As the voltage between the drain and the source is increased the current carried by 
the channel eventually saturates through a process known as pinch-off, in which 
the channel narrows at one end due to the effect of the field parallel to the surface. 
The channel width is controlled by the gate voltage. Typically a larger gate voltage 
results in wider channel and consequently a lower resistance for a given drain 
voltage. Additionally, the saturation current is larger for a higher gate voltage.
Figure 9: Model geometry showing the external connections.
Figure 9 shows the model geometry, indicating how the geometry elements 
correspond to features in Figure 7. In this model both the source and the base are 
connected to gro
```

### Section 19

```
22 ---
22 | 
voltage (2, 3, and 4 V). The drain current versus drain voltage is then plotted at 
several values of the gate voltage.
Model Wizard
Note: These instructions are for the user interface on Windows but apply, with 
minor differences, also to Linux and Mac.
1 To start the software, double-click the COMSOL icon on the desktop. When 
the software opens, you can choose to use either the Model Wizard to create a 
new model, or Blank Model to create one manually. For this tutorial, click the 
Model Wizard button.
If COMSOL Multiphysics is already open, you can start the Model Wizard by 
selecting New
 from the File menu and then click Model Wizard 
.
The Model Wizard guides you through the first steps of setting up a model. The 
next window lets you select the dimension of the modeling space.
2 In the Select Space Dimension window, click the 2D button 
.
3 In the Select Physics tree, under the Semiconductor branch, click 
Semiconductor (semi)
.
4 Click Add button. Observe that the
```

### Section 20

```
23 ---
 | 23
2 In the Settings window for Parameters, locate the Parameters section. In the 
table, enter the following settings:
These are examples of global parameters that we can use to parameterize the 
model. The parameters can be any global quantity, such as the geometric 
dimensions, material properties, or doping concentrations, just to name a few.
Geometry 1
The geometry can be specified using the built-in tools in COMSOL Multiphysics. 
First choose to define geometry objects using micrometer units.
1 In the Model Builder tree, under Component 1, click Geometry 1 
.
2 In the Settings window for Geometry, locate the Units section. From the 
“Length unit” list , choose μm.
Rectangle 1
Next create a rectangle to define the geometry extents.
1 In the Model Builder, right click Geometry 1 
 and choose Rectangle
.
2 In the Settings window for Rectangle, locate the “Size and Shape” section. In 
the Width text field, type 3. In the Height text field, type 0.7.
Polygon 1
Add a polygon 
```

