# Chemical Species Transport Module — API Reference

Extracted from COMSOL 6.4 documentation and mph tags.json.

## Feature Types (6 found)

| Feature Name | Tag | Parent Interface |
|-------------|-----|------------------|
| `Chemistry` | `chem` | physics |
| `ReactionChem` | `rch*` | Chemistry |
| `ReversibleReactionGroup` | `rgr*` | Chemistry |
| `SpeciesChem` | `sch*` | Chemistry |
| `SpeciesGroup` | `sg_rgr*` | Chemistry |
| `SpeciesThermodynamics` | `sthm*` | SpeciesGroup |

## Documentation Structure (api_chemical_extract.txt)

```
  TOC:   Contents (p.3)
  TOC:   User’s Guide Introduction (p.17)
  TOC:     About the Chemical Reaction Engineering Module (p.18)
  TOC:       The Scope of the Chemical Reaction Engineering Module (p.18)
  TOC:       The Chemical Reaction Engineering Module Physics Interface Guide (p.19)
  TOC:       The Material Database (p.24)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.24)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.25)
  TOC:     Overview of the User’s Guide (p.28)
  TOC:   The Chemistry and Reaction Engineering Interfaces (p.31)
  TOC:     Overview of the Reaction Engineering and Chemistry Interfaces (p.32)
  TOC:       Using the Reaction Node (p.33)
  TOC:       Using the Species Node (p.36)
  TOC:       Using the Equation View Node — Reactions and Species (p.39)
  TOC:     Theory for the Reaction Engineering and Chemistry Interfaces (p.40)
  TOC:       Reaction Kinetics and Rate Expressions (p.40)
  TOC:       The Equilibrium Constant (p.41)
  TOC:       Handling of Equilibrium Reactions (p.45)
  TOC:       Reactor Types in the Reaction Engineering Interface (p.48)
  TOC:       Transport Properties (p.55)
  TOC:       CHEMKIN Data and NASA Polynomials (p.59)
  TOC:       Working with Predefined Expressions (p.60)
  TOC:       References for the Reaction Engineering Interface (p.62)
  TOC:     The Reaction Engineering Interface (p.63)
  TOC:       Features Nodes Available for the Reaction Engineering Interface (p.72)
  TOC:       Initial Values (p.72)
  TOC:       Reaction (p.73)
  TOC:       Species (p.79)
  TOC:       Reversible Reaction Group (p.83)
  TOC:       Equilibrium Reaction Group (p.85)
  TOC:   Introducing the Chemical Reaction Engineering Module (p.5)
  TOC:   Chemical Reaction Engineering Simulations (p.6)
  TOC:     Modeling Strategy (p.7)
  TOC:     Investigating Chemical Reaction Kinetics — Modeling Perfectly Mixed and Plug Flow Reactors (p.8)
  TOC:     Investigating Reactors and Systems — Modeling Space Dependency (p.9)
  TOC:   Chemical Reaction Engineering Module Interfaces (p.11)
  TOC:     The Physics Interface List by Space Dimension and Study Type (p.18)
  TOC:   Tutorial Model: NOx and Ammonia Conversion in a Monolithic Reactor (p.22)
  TOC:     Introduction (p.22)
  TOC:     Tutorial Modeling Strategy (p.23)
  TOC:     Chemistry (p.24)
  TOC:     Single Channel Model (p.26)
  TOC:     Results for the Single Channel Model (p.28)
  TOC:     Monolith Reactor Model (p.38)
  TOC:     Results for the Monolith Reactor Model (p.43)
  TOC:     Summary (p.50)
  TOC:     References (p.50)
  TOC:     Note on the Models (p.51)
  TOC:   Modeling Instructions: Single Channel Model (p.52)
  TOC:     Model Wizard (p.52)
```

## Key API Content (58 sections)

### Section 1

```
=== ChemicalReactionEngineeringModuleUsersGuide.pdf ===
Pages: 570
  TOC:   Contents (p.3)
  TOC:   User’s Guide Introduction (p.17)
  TOC:     About the Chemical Reaction Engineering Module (p.18)
  TOC:       The Scope of the Chemical Reaction Engineering Module (p.18)
  TOC:       The Chemical Reaction Engineering Module Physics Interface Guide (p.19)
  TOC:       The Material Database (p.24)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.24)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.25)
  TOC:     Overview of the User’s Guide (p.28)
  TOC:   The Chemistry and Reaction Engineering Interfaces (p.31)
  TOC:     Overview of the Reaction Engineering and Chemistry Interfaces (p.32)
  TOC:       Using the Reaction Node (p.33)
  TOC:       Using the Species Node (p.36)
  TOC:       Using the Equation View Node — Reactions and Species (p.39)
  TOC:     Theory for the Reaction Engineering and Chemistry Interfaces (p.40)
  TOC:    
```

### Section 2

```
3 ---
C O N T E N T S  | 3
C o n t e n t s
Chapt e r 1: U s e r ’ s  G u i d e  I n t r o d u c t i o n
About the Chemical Reaction Engineering Module 
 18
The Scope of the Chemical Reaction Engineering Module   .   .   .   .   .   .   .  18
The Chemical Reaction Engineering Module Physics Interface Guide   .   .   .  19
The Material Database.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  24
Common Physics Interface and Feature Settings and Nodes    .   .   .   .   .   .  24
Where Do I Access the Documentation and Application Libraries? .   .   .   .  25
Overview of the User’s Guide 
 28
C h a p t e r  2 :  T h e  C h e m i s t r y  a n d  R e a c t i o n  
E n g i n e e r i n g  I n t e r f a c e s
Overview of the Reaction Engineering and Chemistry 
Interfaces 
 32
Using the Reaction Node.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  33
Using the Species Node  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  
```

### Section 3

```
4 ---
4 | C O N T E N T S
The Reaction Engineering Interface 
 63
Features Nodes Available for the Reaction Engineering Interface.   .   .   .   .  72
Initial Values    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  72
Reaction  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  73
Species    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  79
Reversible Reaction Group .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  83
Equilibrium Reaction Group.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  85
Species Group .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  86
Additional Source   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  87
Species Activity   .   .   .   .   .   .   .   .   .   .   .   .   .  
```

### Section 4

```
5 ---
C O N T E N T S  | 5
The Transport of Diluted Species Interface 
 134
The Transport of Diluted Species in Porous Media Interface   .   .   .   .   .    138
The Transport of Diluted Species in Porous Catalysts Interface  .   .   .   .    139
The Transport of Diluted Species in Packed Beds Interface .   .   .   .   .   .    140
Domain, Boundary, and Pair Nodes for the Transport of Diluted 
Species Interface.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    141
Prescribing Conditions on Fluid–Solid Interfaces .   .   .   .   .   .   .   .   .   .    143
Species Properties   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    143
Fluid   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    144
Solid    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    146
Initial Values    .   .   .   .   .   .   .   .   .   .   
```

### Section 5

```
6 ---
6 | C O N T E N T S
Unsaturated Porous Medium   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    167
Liquid  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    167
Gas .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    170
Adsorption  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    170
Volatilization   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    172
Packed Bed (Moving Packed Bed).   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    173
Pellets .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    174
Diffusion (Transport of Diluted Species) .   .   .   .   .   .   .   .   .   .   .   .   .    177
Shrinking Core Reactions    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   . 
```

### Section 6

```
7 ---
C O N T E N T S  | 7
Outflow  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    203
Reactions.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    203
Species Source.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    204
The Transport of Diluted Species in Moving Packed Beds Interface .   .   .    205
The Transport of Diluted Species in Moving Packed Beds, Shrinking 
Core  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    205
The Transport of Diluted Species in Packed Beds, Shrinking Core  .   .   .    206
The Transport of Concentrated Species Interface 
 208
The Transport of Concentrated Species in Porous Media Interface .   .   .    214
The Transport of Concentrated Species in Porous Catalysts Interface.   .    215
The Transport of Concentrated Species in Packed Beds Interface   .   .   .   
```

### Section 7

```
8 ---
8 | C O N T E N T S
Mass Fraction  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    252
Flux .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    252
Inflow  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    254
No Flux  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    255
Out-of-Plane Flux    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    255
Outflow  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    257
Symmetry   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    257
Flux Discontinuity   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    258
Open Boundary  .   .   .   .   .   .   .   .   .   .   .   .   .   
```

### Section 8

```
9 ---
C O N T E N T S  | 9
Domain, Boundary, and Pair Nodes for the Electrophoretic Transport 
Interface.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    283
Solvent    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    284
Porous Matrix Properties    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    285
Fully Dissociated Species .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    285
Uncharged Species  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    285
Weak Acid  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    285
Weak Base  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    286
Ampholyte  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    286
Protein    .   .   .   
```

### Section 9

```
10 ---
10 | C O N T E N T S
Initial Values    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    302
No Flux  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    302
Number Density .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    303
Outflow  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    303
The Vapor–Liquid Equilibrium Multiphysics Interfaces 
 304
Laminar Vapor Flow    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    304
Laminar Two-Phase Flow.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    305
Turbulent Flow, κ−ε .   .   .   .   .   .   .   .   .   .   .   .   .   .   . 305
Turbulent Flow, κ−ω    .   .   .   .   .   .   .   .   .   .   .   .   .   . 305
Turbulent Flow, SST   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  
```

### Section 10

```
11 ---
C O N T E N T S  | 11
with Shrinking Core Model Interface .   .   .   .   .   .   .   .   .   .   .   .   .    323
The Reacting Flow in Moving Packed Beds, Transport of Diluted 
Species Interface.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    324
The Reacting Flow in Moving Packed Beds, Transport of 
Concentrated Species Interface .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    325
The Reacting Flow in Moving Packed Beds, Transport of Diluted 
Species with Shrinking Core Model Interface .   .   .   .   .   .   .   .   .   .    326
The Reacting Flow, Diluted Species Coupling Feature .   .   .   .   .   .   .   .    326
The Reacting Flow Coupling Feature   .   .   .   .   .   .   .   .   .   .   .   .   .   .    326
Physics Interface Features   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    327
The Nonisothermal Reacting Flow Multiphysics Interfaces 
 328
The Nonisothermal Reacting Laminar Flow Interface  
```

### Section 11

```
12 ---
12 | C O N T E N T S
Theory for the Transport of Diluted Species Interface 
 353
Mass Balance Equation.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    354
Equilibrium Reaction Theory   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    355
Material Balance Formulation  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    357
Solving a Diffusion Equation Only    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    357
Mass Sources for Species Transport    .   .   .   .   .   .   .   .   .   .   .   .   .   .    358
Adding Transport Through Migration  .   .   .   .   .   .   .   .   .   .   .   .   .   .    360
Supporting Electrolytes   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    361
Crosswind Diffusion    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    362
Danckwerts Inflow Boundary Condition  .   .   .   .   .   .   .   .   .   .   .   .   .
```

### Section 12

```
13 ---
C O N T E N T S  | 13
Governing Equations for the Bulk Concentrations  .   .   .   .   .   .   .   .   .    416
ODE Formulations for Surface Concentrations   .   .   .   .   .   .   .   .   .   .    418
Surface Reaction Equations on Deforming Geometries   .   .   .   .   .   .   .    419
Reference for the Surface Reactions Interface .   .   .   .   .   .   .   .   .   .   .    420
Theory for the Nernst–Planck Equations Interface 
 421
Governing Equations for the Nernst–Planck Formulation.   .   .   .   .   .   .    421
Material Balance Formulation  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    423
Theory for the Size-Based Population Balance Interface 
 424
Population Balance Equation   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    424
Discretization of the Size Coordinate  .   .   .   .   .   .   .   .   .   .   .   .   .   .    425
Particle Nucleation  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
```

### Section 13

```
14 ---
14 | C O N T E N T S
Coupling to Other Physics Interfaces  .   .   .   .   .   .   .   .   .   .   .   .   .   .    449
Chapt e r 5: H e a t  T r a n s f e r  I n t e r f a c e s
Modeling Heat Transfer 
 452
Available Physics Interfaces .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    452
Coupling Heat Transfer with Other Physics Interfaces.   .   .   .   .   .   .   .    452
Chapt e r 6: T h e r m o d y n a m i c s
Using Thermodynamic Properties 
 454
Workflow for Thermodynamics Property Calculations   .   .   .   .   .   .   .    454
Thermodynamics .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    456
Thermodynamic System  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    457
External Thermodynamic Packages  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    465
External Thermodynamic System.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    466
Predefined System   
```

### Section 14

```
17 ---
 17
 1
User’s Guide Introduction
This guide describes the Chemical Reaction Engineering Module, an optional 
package that extends the COMSOL Multiphysics® modeling environment with 
customized physics interfaces and functionality for the analysis of mass transport, 
chemical reactions, thermodynamic properties, and other features that are 
important for chemical engineering simulation.
This chapter introduces you to the capabilities of the module. A summary of the 
physics interfaces and where you can find documentation and model examples is 
also included. The last section is a brief overview with links to each chapter in this 
guide.
• About the Chemical Reaction Engineering Module
• Overview of the User’s Guide
```

### Section 15

```
18 ---
18 |  C H A P T E R  1 :  U S E R ’ S  G U I D E  I N T R O D U C T I O N
About the Chemical Reaction 
Engineering Module
In this section:
• The Scope of the Chemical Reaction Engineering Module
• The Chemical Reaction Engineering Module Physics Interface Guide
• Common Physics Interface and Feature Settings and Nodes
• The Material Database
• Where Do I Access the Documentation and Application Libraries?
The Scope of the Chemical Reaction Engineering Module
The Chemical Reaction Engineering Module is tailor-made for the modeling of 
chemical systems primarily affected by chemical composition, reaction kinetics, fluid 
flow, and temperature as functions of space, time, and each other. It has a number of 
physics interfaces to model chemical reaction kinetics, mass transport in dilute, 
concentrated, and electric potential-affected solutions, laminar and porous media 
flows, and energy transport.
Included in these physics interfaces are the kinetic expressions for the reacting sy
```

### Section 16

```
19 ---
A B O U T  T H E  C H E M I C A L  R E A C T I O N  E N G I N E E R I N G  M O D U L E  |  19
• Meshing a modeling domain with appropriate consideration given to the reaction 
system’s behavior.
• Solving the equations that describe a system for stationary or dynamic behavior, or 
as a parametric or optimization study.
• Analyzing results to present for further use.
Once a model is defined, you can go back and make changes to all the branches listed 
above, while maintaining consistency in the other definitions throughout. You can 
restart the solver, for example, using the existing solution as an initial guess or even 
alter the geometry, while the equations and boundary conditions are kept consistent 
through the associative geometry feature. It is also useful to review the Introduction 
to the Chemical Reaction Engineering Module included with the module’s 
documentation.
While a major focus of this module is on chemical reactors and reacting systems, it is 
also extensively 
```

### Section 17

```
20 ---
20 |  C H A P T E R  1 :  U S E R ’ S  G U I D E  I N T R O D U C T I O N
with this module. See the COMSOL Multiphysics Reference Manual for details 
pertaining to the base package.
When one or several physics interfaces are chosen from the Model Wizard (or if you 
open the Add Study window), you select an analysis type (stationary, dynamic, or 
parametric) and then the modeling interfaces are available as a nodes in the Model 
Builder along with all the other nodes required for modeling (Definitions, Geometry, 
and so forth).
By adding another physics interface, you can account for a phenomenon not previously 
described in a model. To do this, right-click a Component node in the Model Builder to 
open the Add Physics window. You can do this at any stage during the modeling 
process. This action still retains the existing geometry, equations, boundary 
conditions, and current solution, which you can build upon for further development 
of the model.
The table below lists all the 
```

### Section 18

```
21 ---
A B O U T  T H E  C H E M I C A L  R E A C T I O N  E N G I N E E R I N G  M O D U L E  |  21
PHYSICS INTERFACE
ICON
TAG
SPACE 
DIMENSION
AVAILABLE STUDY TYPE
 Chemical Species Transport
Transport of Diluted 
Species1
tds
all dimensions
stationary; time dependent
Transport of 
Concentrated Species
tcs
all dimensions
stationary; time dependent
Chemistry
chem
all dimensions
stationary; time dependent
Reaction Engineering
re
0D
time dependent; stationary 
plug flow
Nernst–Planck Equations
npe
all dimensions
stationary; time dependent
Nernst–Planck–Poisson 
Equations
tds+es
all dimensions
stationary; time dependent; 
stationary source sweep; 
small-signal analysis, 
frequency domain
Electrophoretic Transport
el
all dimensions
stationary; stationary with 
initialization; time 
dependent; time dependent 
with initialization
Transport of Diluted 
Species in Porous Media
tds
all dimensions
stationary; time dependent
Transport of 
Concentrated Species in 
Porous Media
tcs
all dimensions

```

### Section 19

```
22 ---
22 |  C H A P T E R  1 :  U S E R ’ S  G U I D E  I N T R O D U C T I O N
Laminar Flow, 
Concentrated Species
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
 Reacting Flow in Porous Media
Transport of Diluted 
Species
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Transport of 
Concentrated Species
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Transport of Diluted 
Species, Porous 
Catalyst
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Transport of 
Concentrated Species, 
Porous Catalyst
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Transport of Diluted 
Species, Packed Bed
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Transport of 
Concentrated Species, 
Packed Bed
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Transport of Diluted 
Species, Packed Bed, 
Shrinking Core Model
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
 Nonisothermal Reacting Flow
Brinkman Equations
—
3D, 2D, 2D 
axisymmetric
stationary; time depende
```

### Section 20

```
23 ---
A B O U T  T H E  C H E M I C A L  R E A C T I O N  E N G I N E E R I N G  M O D U L E  |  23
Laminar Vapor Flow
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Laminar Two-Phase 
Flow
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
 Precipitation and Crystallization
Size-Based Population 
Balance
pbsb
all dimensions
stationary; time dependent
Laminar Two-Phase 
Flow
—
3D, 2D, 2D 
axisymmetric, 
0D
stationary; time dependent
 Fluid Flow
 Single-Phase Flow
Creeping Flow
spf
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Laminar Flow1
spf
3D, 2D, 2D 
axisymmetric
stationary; time dependent
 Porous Media and Subsurface Flow
Brinkman Equations
br
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Darcy’s Law
dl
all dimensions
stationary; time dependent
Free and Porous Media 
Flow, Brinkman
fp
3D, 2D, 2D 
axisymmetric
stationary; time dependent
Free and Porous Media 
Flow, Darcy
—
3D, 2D, 2D 
axisymmetric
stationary; time dependent
PHYSICS INTERFACE
ICON
TAG
SPACE 

```

