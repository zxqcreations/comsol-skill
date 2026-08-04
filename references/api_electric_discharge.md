# Electric Discharge Module — API Reference

Extracted from COMSOL 6.4 documentation and mph tags.json.

## Feature Types (2 found)

| Feature Name | Tag | Parent Interface |
|-------------|-----|------------------|
| `EquilibriumDischargeHeatSource` | `phs*` | multiphysics |

## Documentation Structure (api_discharge_extract.txt)

```
  TOC:   Content (p.3)
  TOC:   Introduction (p.11)
  TOC:     About the Electric Discharge Module (p.12)
  TOC:       What Can the Electric Discharge Module Do? (p.12)
  TOC:       Electric Discharge Module Physics Interface Guide (p.13)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.15)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.16)
  TOC:     Overview of the User’s Guide (p.18)
  TOC:   Modeling Guidelines (p.19)
  TOC:     Connecting to Electrical Circuits (p.20)
  TOC:       About Connecting Electrical Circuits to Physics Interfaces (p.20)
  TOC:       Connecting Electrical Circuits Using Predefined Couplings (p.21)
  TOC:       Connecting Electrical Circuits by User-Defined Couplings (p.21)
  TOC:       Solving (p.23)
  TOC:       Results Processing (p.23)
  TOC:     SPICE Import and Export (p.24)
  TOC:       SPICE Import (p.24)
  TOC:       SPICE Export (p.25)
  TOC:       Reference (p.25)
  TOC:     Meshing (p.27)
  TOC:     Solving (p.28)
  TOC:     Material Libraries (p.29)
  TOC:   Electric Discharge Interfaces (p.31)
  TOC:     The Electric Discharge Interface (p.32)
  TOC:       Domain, Boundary, and Pair Nodes for the Electric Discharge Interface (p.35)
  TOC:       Gas (p.37)
  TOC:       Liquid (p.40)
  TOC:       Solid (p.43)
  TOC:       Initial Values (p.45)
  TOC:       Insulation (p.46)
  TOC:   Introduction (p.5)
  TOC:   The Electric Discharge Module Physics Interface Guide (p.6)
  TOC:     Physics Interface Guide by Space Dimension and Study Type (p.11)
```

## Key API Content (32 sections)

### Section 1

```
=== ElectricDischargeModuleUsersGuide.pdf ===
Pages: 287
  TOC:   Content (p.3)
  TOC:   Introduction (p.11)
  TOC:     About the Electric Discharge Module (p.12)
  TOC:       What Can the Electric Discharge Module Do? (p.12)
  TOC:       Electric Discharge Module Physics Interface Guide (p.13)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.15)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.16)
  TOC:     Overview of the User’s Guide (p.18)
  TOC:   Modeling Guidelines (p.19)
  TOC:     Connecting to Electrical Circuits (p.20)
  TOC:       About Connecting Electrical Circuits to Physics Interfaces (p.20)
  TOC:       Connecting Electrical Circuits Using Predefined Couplings (p.21)
  TOC:       Connecting Electrical Circuits by User-Defined Couplings (p.21)
  TOC:       Solving (p.23)
  TOC:       Results Processing (p.23)
  TOC:     SPICE Import and Export (p.24)
  TOC:       SPICE Import (p.24)
  TOC:       SPICE Export (p.25)
 
```

### Section 2

```
3 ---
C O N T E N T S  | 3
C o n t e n t
C h a p t e r  1 :  I n t r o d u c t i o n
About the Electric Discharge Module 
 12
What Can the Electric Discharge Module Do?.   .   .   .   .   .   .   .   .   .   .   .  12
Electric Discharge Module Physics Interface Guide  .   .   .   .   .   .   .   .   .   .  13
Common Physics Interface and Feature Settings and Nodes    .   .   .   .   .   .  15
Where Do I Access the Documentation and Application Libraries? .   .   .   .  16
Overview of the User’s Guide 
 18
C h a p t e r  2 :  M o d e l i n g  G ui d e l i n e s
Connecting to Electrical Circuits 
 20
About Connecting Electrical Circuits to Physics Interfaces  .   .   .   .   .   .   .  20
Connecting Electrical Circuits Using Predefined Couplings  .   .   .   .   .   .   .  21
Connecting Electrical Circuits by User-Defined Couplings  .   .   .   .   .   .   .  21
Solving.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  23
Postproces
```

### Section 3

```
4 ---
4 | C O N T E N T S
Meshing 
 26
Solving 
 27
Material Libraries 
 28
C h a p t e r  3 :  E l e c t r i c  D i s c h a r g e  I n t e r f a c e s
The Electric Discharge Interface 
 30
Domain, Boundary, and Pair Nodes for the Electric Discharge 
Interface.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  33
Gas .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  34
Liquid  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  37
Solid    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  40
Initial Values    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  42
Insulation.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  42
Dielectric Interface, Bulk Transport.   .   .   .  
```

### Section 4

```
5 ---
C O N T E N T S  | 5
Flux .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  61
Symmetry   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  61
Periodic Condition  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  61
Current Calculation.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  63
Theory for the Electric Discharge Interface 
 64
Review of Charge Relaxation  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  64
Overview of Physical Models   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  65
Gas Discharges   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  67
Discharges in Liquids   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  70
Bipolar Charge Transport in Solids  .   .   .
```

### Section 5

```
7 ---
C O N T E N T S  | 7
The Electrical Circuit Interface 
 126
Ground Node .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    127
Voltmeter   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    128
Ampère Meter.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    128
Resistor  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    128
Capacitor.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    129
Inductor  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    129
Voltage Source    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    129
Current Source   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    130
Voltage-Controlled Voltage Source .   
```

### Section 6

```
8 ---
8 | C O N T E N T S
Theory for the Electrical Circuit Interface 
 150
Electrical Circuit Modeling and the Semiconductor Device Models  .   .   .    150
Bipolar Transistors  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    151
MOSFET Transistors   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    154
Diode  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    157
Reference for the Electrical Circuit Interface   .   .   .   .   .   .   .   .   .   .   .    159
C h a p t e r  5 :  C h e m i s t r y  a n d  R e a c t i o n  En g i n e e r i n g  
I n t e r f a c e s
Overview of the Reaction Engineering and Chemistry 
Interfaces 
 162
Using the Reaction Node.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    163
Using the Species Node  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    166
Using the Equation View Node
```

### Section 7

```
9 ---
C O N T E N T S  | 9
Additional Source   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    217
Reaction Thermodynamics  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    218
Species Activity   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    218
Species Thermodynamics.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    218
Feed Inlet.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    219
Generate Space-Dependent Model  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    220
The Chemistry Interface 
 232
Feature Nodes Available for the Chemistry Interface  .   .   .   .   .   .   .   .    239
Reaction  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    239
Species    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
```

### Section 8

```
11 ---
 11
 1
In t r od u c t i on 
This guide describes the Electric Discharge Module, an optional add-on package 
for COMSOL Multiphysics® designed to assist you to solve and model electric 
discharges.
This chapter introduces you to the capabilities of the module including an 
introduction to the modeling stages and some realistic and illustrative models. A 
summary of the physics interfaces and where you can find documentation and 
model examples is also included. The last section is a brief overview with links to 
each chapter in this guide.
In this chapter:
• About the Electric Discharge Module
• Overview of the User’s Guide
```

### Section 9

```
12 ---
12 |  C H A P T E R  1 :  I N T R O D U C T I O N
About the Electric Discharge Module
In this section:
• What Can the Electric Discharge Module Do?
• Electric Discharge Module Physics Interface Guide
• Common Physics Interface and Feature Settings and Nodes
• Where Do I Access the Documentation and Application Libraries?
What Can the Electric Discharge Module Do?
The Electric Discharge Module provides a unique environment for simulation of 
electric discharges. The module is a powerful tool for detailed analysis of 
low-temperature and high-temperature gas discharges as well as charge transport in 
liquid and solid dielectrics. With this module you can run static and transient 
simulations in an easy-to-use user interface.
The available physics interfaces cover the following types of electric discharge 
simulations:
• Arc discharges
• Corona discharges
• Dielectric barrier discharges
• Electrostatic discharges
• Streamer discharges
In addition to the standard results and visuali
```

### Section 10

```
13 ---
A B O U T  T H E  E L E C T R I C  D I S C H A R G E  M O D U L E  |  13
The Electric Discharge interfaces are fully multiphysics enabled — couple them to any 
other physics interface in COMSOL Multiphysics or other modules. The Electric 
Discharge Module contains predefined multiphysics interfaces to facilitate easy setup 
of models with the most commonly occurring couplings. For example, the Arc 
Discharge multiphysics interface combines all features from the Magnetic and Electric 
Fields interface in the stationary and time-dependent formulations with the Heat 
Transfer interface and Laminar Flow interface to model the dynamics of electric arc.
The Electric Discharge Module also provides interfaces for modeling electrical circuits.
Electric Discharge Module Physics Interface Guide
The interfaces in the Electric Discharge Module form a complete set of simulation 
tools for electric discharge simulations. To select the right physics interface for 
describing the real-life physi
```

### Section 11

```
14 ---
14 |  C H A P T E R  1 :  I N T R O D U C T I O N
The table below lists the physics interfaces available specifically with this module in 
addition to the COMSOL Multiphysics basic license.
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
Electrostatics
es
all dimensions
stationary; time dependent; 
stationary source sweep; 
eigenfrequency; frequency 
domain; small signal 
analysis, frequency domain
Magnetic and Electric 
Fields
mef
3D, 2D, 2D 
axisymmetric
stationary; time dependent
 Chemical Species Transport
Chemistry
chem
all dimensions
stationary; time dependent
Reaction Engineering
re
0D
time dependent; stationary 
plug flow
 Electric Discharge
Electric Discharge
edis
all dimensions
time dependent; stationary; 
frequency domain 
perturbation
Arc Discharge
—
all dimensions
time dependent; stationary; 
frequency–transient; 
fre
```

### Section 12

```
15 ---
A B O U T  T H E  E L E C T R I C  D I S C H A R G E  M O D U L E  |  15
In 2D, in-plane and out-of-plane variants are available for problems with a planar 
symmetry as well as axisymmetric interfaces for problems with a cylindrical symmetry. 
See What Problems Can You Solve? for information about the available study types and 
variables. See also Overview of the User’s Guide for links to the chapters in this guide.
Common Physics Interface and Feature Settings and Nodes
There are several common settings and sections available for the physics interfaces and 
feature nodes. Some of these sections also have similar settings or are implemented in 
the same way no matter the physics interface or feature being used.
Electrical Breakdown 
Detection
ebd
3D, 2D, 2D 
axisymmetric
time dependent
 
 Radio Frequency
Electromagnetic Waves, 
Transient
temw
3D, 2D, 2D 
axisymmetric
eigenfrequency; time 
dependent; time 
dependent, modal; time 
dependent with FFT
Transmission Line, 
Transient
t
```

### Section 13

```
16 ---
16 |  C H A P T E R  1 :  I N T R O D U C T I O N
In each module’s documentation, only unique or extra information is included; 
standard information and procedures are centralized in the COMSOL Multiphysics 
Reference Manual.
Where Do I Access the Documentation and Application Libraries?
A number of online resources have more information about COMSOL, including 
licensing and technical information. The electronic documentation, topic-based (or 
context-based) help, and the Application Libraries are all accessed through the 
COMSOL Desktop.
C O N T A C T I N G  C O M S O L  B Y  E M A I L
For general product information, contact COMSOL at info@comsol.com.
C O M S O L  A C C E S S  A N D  T E C H N I C A L  S U P P O R T
To receive technical support from COMSOL for the COMSOL products, please 
contact your local COMSOL representative or send your questions to 
support@comsol.com. An automatic notification and a case number will be sent to you 
by email. You can also access techni
```

### Section 14

```
18 ---
18 |  C H A P T E R  1 :  I N T R O D U C T I O N
Overview of the User’s Guide
The Electric Discharge Module User’s Guide gets you started with modeling using 
COMSOL Multiphysics. The information in this guide is specific to this module. 
Instructions how to use COMSOL in general are included with the COMSOL 
Multiphysics Reference Manual.
T A B L E  O F  C O N T E N T S ,  G L O S S A R Y ,  A N D  I N D E X
To help you navigate through this guide, see the Contents, Glossary, and Index.
M O D E L I N G  G U I D E L I N E S
The Modeling Guidelines chapter summarizes general procedures and strategies for 
modeling electric discharges. Topics include Connecting to Electrical Circuits, SPICE 
Import and Export, Meshing, Solving, and Material Libraries.
E L E C T R I C  D I S C H A R G E  I N T E R F A C E S
The Electric Discharge Interfaces chapter includes physics feature information and 
theory for physics interfaces under the Electric Discharge branch in the Model Wizard.
A C /
```

### Section 15

```
20 ---
20 |  C H A P T E R  2 :  M O D E L I N G  G U I D E L I N E S
Connecting to Electrical Circuits
In this section:
• About Connecting Electrical Circuits to Physics Interfaces
• Connecting Electrical Circuits Using Predefined Couplings
• Connecting Electrical Circuits by User-Defined Couplings
• Solving
• Results Processing
About Connecting Electrical Circuits to Physics Interfaces
This section describes the various ways electrical circuits can be connected to other 
physics interfaces in COMSOL Multiphysics. If you are not familiar with circuit 
modeling, it is recommended that you review the Theory for the Electrical Circuit 
Interface.
In general electrical circuits connect to other physics interfaces via one or more of three 
special circuit features:
•
External I vs. U
•
External U vs. I
•
External I-Terminal
Electrostatic Discharge: Application Library path 
Electric_Discharge_Module/Electrostatic_Discharges/esd
```

### Section 16

```
21 ---
C O N N E C T I N G  T O  E L E C T R I C A L  C I R C U I T S  |  21
These features either accept a voltage measurement from the connecting noncircuit 
physics interface and return a current from an Electrical Circuit interface or the other 
way around.
Connecting Electrical Circuits Using Predefined Couplings
In addition to these circuit features, interfaces in the AC/DC Module, RF Module, 
MEMS Module, Electric Discharge Module, Plasma Module, and Semiconductor 
Module (the modules that include the Electrical Circuit interface) also contain features 
that provide couplings to the Electrical Circuit interface by accepting a voltage or a 
current from one of the specific circuit features (External I vs. U, External U vs. I, and 
External I-Terminal).
This coupling is typically activated when:
• A choice is made in the Settings window for the noncircuit physics interface feature, 
which then announces (that is, includes) the coupling to the Electrical Circuit 
interface. Its vol
```

### Section 17

```
22 ---
22 |  C H A P T E R  2 :  M O D E L I N G  G U I D E L I N E S
• Define your own voltage or current measurement in the noncircuit physics interface 
using variables, coupling operators, and so forth.
• In the Settings window for the Electrical Circuit interface feature, selecting the 
User-defined option and entering the name of the variable or expression using 
coupling operators defined in the previous step.
D E T E R M I N I N G  A  C U R R E N T  O R  V O L T A G E  V A R I A B L E  N A M E
To determine a current or voltage variable name, look at the Dependent Variables node 
under the Study node. To do this:
1 In the Model Builder, right-click the Study node and select Show Default Solver.
2 Expand the Solver > Dependent Variables node and click the state node, in this 
example, Current through device R1 (comp1.currents). The variable name is shown in 
the Settings window for State.
Typically, voltage variables are named cir.Xn_v and current variables 
cir.Xn_i, where n is 
```

### Section 18

```
23 ---
C O N N E C T I N G  T O  E L E C T R I C A L  C I R C U I T S  |  23
Solving
Results Processing
The Electrical Circuits interface, unlike most of the other physics interfaces, solves for 
a relatively large number of global dependent variables (such as voltages and currents), 
instead of solving for a few space-varying fields (such as temperature or displacement). 
For this reason, the Electrical Circuit interface does not provide default plots when 
computing a study.
The physics interface defines a number of variables that can be used in postprocessing. 
All variables defined by the Electrical Circuit interface are of a global scope, and can 
be evaluated in a Global Evaluation node (under Derived Values). In addition, the time 
evolution or dependency on a parameter can be plotted in a Global plot (under a 1D 
Plot Group node).
The physics interface defines a Node voltage variable for each electrical node in the 
circuit, with name cir.v_name, where cir is the physics interf
```

### Section 19

```
24 ---
24 |  C H A P T E R  2 :  M O D E L I N G  G U I D E L I N E S
SPICE Import and Export
SPICE Import
The circuit definition in COMSOL Multiphysics adheres to the SPICE format 
developed at the University of California, Berkeley (see Ref. 1 and Ref. 2 for further 
information). SPICE netlists can be imported and the corresponding circuit nodes are 
generated in the COMSOL Multiphysics model. Most circuit simulators can export to 
this format or some version of it.
The Electrical Circuit interface supports the following device models:
Statements corresponding to multiple devices are resolved by parsing the associated 
.model statement. The physics interface also supports the .subckt statement, which 
is represented in COMSOL by a Subcircuit Definition node, and the .include 
statement. SPICE commands are interpreted case-insensitively. The statement defining 
each device is also interpreted as the Device name.
According to SPICE specification, the first line in the netlist file is 
```

### Section 20

```
25 ---
S P I C E  I M P O R T  A N D  E X P O R T  |  25
SPICE Export
The SPICE Export functionality creates a SPICE netlist file containing a description of 
the circuit represented by the physics interface. This functionality can be accessed from 
the physics interface context menu (right-click the physics interface node and select 
Export SPICE Netlist). After specifying a filename, the circuit is exported and messages 
from the export process display in the Messages window. During the export process, a 
series of operations are performed:
• In order to avoid conflicts, each component must be identified by a unique Device 
name. If one or more components have the same device name, the export operation 
fails and an error message is displayed. All characters in a Device name that are not 
letters, digits, or underscores are replaced by underscores.
• According to the SPICE specification, each circuit must have a node with name 0, 
which is assumed to be the only ground node. When exp
```

