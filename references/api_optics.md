# Optics Module (Ray + Wave) — API Reference

Extracted from COMSOL 6.4 documentation and mph tags.json.

## Feature Types (24 found)

| Feature Name | Tag | Parent Interface |
|-------------|-----|------------------|
| `GeometricalOptics` | `gop` | physics |
| `CrossGrating` | `xgrat*` | GeometricalOptics |
| `CrossDiffractionOrder` | `xdfo*` | CrossGrating |
| `GlobalEquations` | `ge*` | GeometricalOptics |
| `Grating` | `grat*` | GeometricalOptics |
| `DiffractionOrder` | `dfo*` | Grating |
| `IlluminatedSurface` | `ill*` | GeometricalOptics |
| `LinearPolarizer` | `lpol*` | GeometricalOptics |
| `LinearWaveRetarder` | `lwav*` | GeometricalOptics |
| `MaterialDiscontinuity` | `matd*` | GeometricalOptics |
| `ThinDielectricFilm` | `film*` | MaterialDiscontinuity |
| `MediumProperties` | `mp*` | GeometricalOptics |
| `Mirror` | `mir*` | GeometricalOptics |
| `RayProperties` | `op*` | GeometricalOptics |
| `RayTermination` | `rt*` | GeometricalOptics |
| `ReleaseFromBoundary` | `relb*` | GeometricalOptics |
| `ReleaseFromElectricField` | `rele*` | GeometricalOptics |
| `ReleaseFromFarFieldRadiationPattern` | `rffr*` | GeometricalOptics |
| `ReleaseFromPoint` | `rpt*` | GeometricalOptics |
| `ReleaseGrid` | `relg*` | GeometricalOptics |
| `SolarRadiation` | `srad*` | GeometricalOptics |
| `Wall` | `wall*` | GeometricalOptics |
| `BoundaryAccumulator` | `bacc*` | Wall |
| `DepositedRayPowerBoundary` | `bsrc*` | Wall |

## Documentation Structure (api_optics_ray_extract.txt)

```
  TOC:   Introduction (p.5)
  TOC:     About This Book (p.6)
  TOC:     Physics Interfaces by Space Dimension and Preset Study Type (p.6)
  TOC:   The Ray Optics Interfaces (p.7)
  TOC:     Geometrical Optics (p.7)
  TOC:     Ray Heating (p.7)
  TOC:   Ray Tracing Fundamentals (p.8)
  TOC:     Ray Propagation (p.8)
  TOC:     Reflection and Refraction (p.9)
  TOC:     Scattering and Absorption (p.11)
  TOC:     Polychromatic Light (p.11)
  TOC:   Intensity and Polarization (p.13)
  TOC:     Reflected and Refracted Ray Intensity (p.13)
  TOC:     Visualizing Polarization (p.15)
  TOC:   Modeling Tools (p.16)
  TOC:     Optical Material Library (p.16)
  TOC:     Part Library (p.17)
  TOC:     Ray Sources (p.18)
  TOC:     Ray-Thermal Coupling (p.21)
  TOC:     Multiscale Electromagnetics Modeling (p.22)
  TOC:   Results Analysis (p.24)
  TOC:     Spot Diagram Plot (p.24)
  TOC:     Optical Aberration Plot (p.26)
  TOC:   Tutorial: Tracing Rays Through a Double Gauss Lens (p.27)
  TOC:     Model Wizard (p.28)
  TOC:     Global Definitions (p.29)
  TOC:     Component (p.31)
  TOC:     Geometry (p.31)
  TOC:     Materials (p.33)
  TOC:     Physics Interfaces (p.35)
  TOC:   Contents (p.3)
  TOC:   Introduction (p.9)
  TOC:     About the Ray Optics Module (p.10)
  TOC:       The Ray Optics Module Physics Interface Guide (p.10)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.11)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.11)
  TOC:         The Documentation and Online Help (p.12)
  TOC:         The Application Libraries Window (p.13)
  TOC:         Contacting COMSOL by Email (p.13)
  TOC:         COMSOL Access and Technical Support (p.13)
  TOC:         COMSOL Online Resources (p.14)
  TOC:     Overview of the User’s Guide (p.15)
  TOC:       Table of contents and Index (p.15)
  TOC:       Ray Optics Modeling (p.15)
  TOC:       Ray Optics Interfaces (p.15)
  TOC:       Multiphysics Interfaces and Couplings (p.15)
  TOC:   Ray Optics Modeling (p.17)
  TOC:     Essentials of Ray Tracing (p.18)
  TOC:       The Ray Tracing Algorithm (p.18)
  TOC:       Basic Requirements of a Geometrical Optics Model (p.19)
```

## Key API Content (51 sections)

### Section 1

```
=== IntroductionToRayOpticsModule.pdf ===
Pages: 48
  TOC:   Introduction (p.5)
  TOC:     About This Book (p.6)
  TOC:     Physics Interfaces by Space Dimension and Preset Study Type (p.6)
  TOC:   The Ray Optics Interfaces (p.7)
  TOC:     Geometrical Optics (p.7)
  TOC:     Ray Heating (p.7)
  TOC:   Ray Tracing Fundamentals (p.8)
  TOC:     Ray Propagation (p.8)
  TOC:     Reflection and Refraction (p.9)
  TOC:     Scattering and Absorption (p.11)
  TOC:     Polychromatic Light (p.11)
  TOC:   Intensity and Polarization (p.13)
  TOC:     Reflected and Refracted Ray Intensity (p.13)
  TOC:     Visualizing Polarization (p.15)
  TOC:   Modeling Tools (p.16)
  TOC:     Optical Material Library (p.16)
  TOC:     Part Library (p.17)
  TOC:     Ray Sources (p.18)
  TOC:     Ray-Thermal Coupling (p.21)
  TOC:     Multiscale Electromagnetics Modeling (p.22)
  TOC:   Results Analysis (p.24)
  TOC:     Spot Diagram Plot (p.24)
  TOC:     Optical Aberration Plot (p.26)
  TOC:   Tutorial: Traci
```

### Section 2

```
3 ---
 | 3
Contents
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
About This Book. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
Physics Interfaces by Space Dimension and Preset Study Type . . . 6
The Ray Optics Interfaces. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Geometrical Optics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Ray Heating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Ray Tracing Fundamentals  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
Ray Propagation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
Reflection and Refraction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
Scattering and Absorption. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
Polychromatic Light . . . . . .
```

### Section 3

```
5 ---
 | 5
Introduction
The Ray Optics Module is a computational tool for modeling the propagation of 
light and other electromagnetic radiation with a ray tracing approach. The rays can 
propagate through the model geometry while being reflected, refracted, or 
absorbed at boundaries.
You can control where the rays are released, and in what direction. You can also 
assign different boundary conditions to every surface in the geometry.
A simple Newtonian telescope. The incident rays are focused by a parabolic primary mirror and then 
redirected to the focal plane by a flat secondary mirror.
The fundamental assumption of ray optics is that the wavelength of the radiation 
is much smaller than the smallest geometric detail in the model, so that diffraction 
can be ignored.
The Ray Optics Module employs nonsequential ray tracing with a deterministic 
ray splitting algorithm at boundaries. In other words, rays can interact with any 
surfaces in the model geometry that they hit, without the
```

### Section 4

```
6 ---
6 | 
About This Book
The next section of this booklet gives a list of the physics interfaces and 
multiphysics couplings that are available with the Ray Optics Module.
The subsequent sections explain the different types of physics interface settings 
and features that are provided for ray optics simulation.
The final section of this book is a detailed, step-by-step tutorial of the setup, ray 
tracing, and postprocessing of a double Gauss lens system.
Physics Interfaces by Space Dimension and Preset Study Type
PHYSICS INTERFACE
ICON
TAG
SPACE 
DIMENSION
AVAILABLE STUDY TYPE
 Optics
 Ray Optics
Geometrical Optics
gop
3D, 2D, 2D 
axisymmetric
ray tracing; bidirectionally 
coupled ray tracing; time 
dependent
Ray Heating
—
3D, 2D, 2D 
axisymmetric
ray tracing; bidirectionally 
coupled ray tracing; time 
dependent
```

### Section 5

```
7 ---
 | 7
The Ray Optics Interfaces
The Ray Optics Module includes the Geometrical Optics physics interface
, as 
well as a dedicated Ray Heating multiphysics interface
.
Geometrical Optics
The Geometrical Optics interface
 is found under the Optics
 branch in the 
Model Wizard
. It is used to model the propagation of electromagnetic rays. 
By default only the ray paths are solved for, but it is possible to solve for additional 
variables to analyze ray intensity, polarization, phase, optical path length, and 
more. Rays can propagate through both homogeneous and graded-index media. 
This interface supports a wide variety of ray sources, and the released rays can be 
reflected, refracted, or absorbed at any boundary in the model.
Ray Heating
The Ray Heating interface 
 is found under the Optics
 branch in the Model 
Wizard
. It combines the Geometrical Optics
 interface with the Heat 
Transfer in Solids
 interface. These two interfaces are coupled together using 
the Ray Heat Source m
```

### Section 6

```
8 ---
8 | 
Ray Tracing Fundamentals
The most essential assumption of a ray optics approach is that the geometry is 
optically large, meaning that the smallest detail of the model geometry is still much 
larger than the wavelength of the radiation. This assumption is necessary because 
the Geometrical Optics interface does not include diffraction effects that occur at 
the wavelength scale when electromagnetic waves interact with edges or points in 
the surrounding geometry.
Wave propagation around an obstruction (far left) or through a slit (middle left) comparable to the 
wavelength produces diffraction patterns. Ray propagation around an optically large obstruction 
(middle right) or a wide slit (far right) produces clearly defined regions of light and shadow.
Ray Propagation
Ray propagation is controlled by the refractive index of the medium. This affects 
the speed at which rays propagate through the domain,
If the medium is homogeneous, or spatially uniform in each domain, then ra
```

### Section 7

```
9 ---
 | 9
In some cases, the refractive index varies continuously within a domain. Since the 
gradient of the refractive index is then nonzero, such a material is called a 
graded-index medium. In graded-index media, the rays can follow curved paths.
Graded-index media most often arise in coupled simulations, such as 
nonisothermal domains where the refractive index is temperature dependent. 
Graded-index media may also appear in models of chemical diffusion if the 
refractive index is a function of the concentration of a diluted species.
Rays follow curved paths through the graded-index medium of a Luneburg lens. The color along the rays 
indicates optical path length (left). The grayscale in the background is the refractive index.
Reflection and Refraction
The rays can interact with any number of boundaries in the model, in any order. 
It is not necessary to specify the order of the boundary interactions because the 
intersection points of rays with a boundary are detected nonsequen
```

### Section 8

```
10 ---
10 | 
Whenever a ray reaches a boundary between two media with different refractive 
indices, the deterministic ray splitting algorithm generates a refracted ray and a 
specularly reflected ray. The direction of the refracted ray is computed using 
Snell’s law,
where n is the refractive index, θi is the angle of incidence with respect to the 
surface normal, θt is the angle of the refracted ray, and the subscripts 1 and 2 
indicate the side of the incident and refracted ray, respectively. The ray splitting 
algorithm automatically also detects when rays undergo total internal reflection 
and suppresses the release of refracted rays accordingly.
Refraction of an incident ray (blue) at a boundary. A second, reflected ray (red) is also released.
It is easy to suppress the release of reflected rays at material discontinuities. This 
allows you to focus exclusively on the refracted rays in lens systems, where the stray 
light may not be of much interest.
Ray tracing in a pair of conv
```

### Section 9

```
11 ---
 | 11
Scattering and Absorption
The default behavior of the Geometrical Optics
 interface is to treat each 
surface as a perfectly smooth reflecting and refracting boundary between two 
dielectric media. Each incident ray splits into reflected and refracted rays. A wide 
variety of other boundary conditions can also be selected.
Any surface can reflect rays diffusely, isotropically, or specularly. Surfaces can also 
absorb rays; you can decide to retain the final ray position for results analysis or 
simply remove rays as they hit the boundary. A dedicated boundary condition for 
modeling reflection and refraction at random rough surfaces is also available.
It is possible to combine different boundary conditions based on a probability or 
logical expression. For example, you could specularly reflect 70% of rays and 
diffusely reflect the remaining 30%; or you could diffusely reflect rays for which 
x > 0 at the intersection point, and absorb all others.
Rays can be specularly re
```

### Section 10

```
12 ---
12 | 
Alternatively, you can enter the coefficients for one of the built-in optical 
dispersion models, such as Sellmeier coefficients. Many glasses in the Optical 
Material Library use these standard optical dispersion models. Some glasses also 
include thermo-optic dispersion coefficients so that the refractive index becomes 
a function of both wavelength and temperature.
A prism containing a dispersive medium can separate light into different colors.
DIFFRACTION GRATINGS
At a diffraction grating, both reflected and transmitted rays of many diffraction 
orders can be released. The built-in boundary condition for the diffraction grating 
automatically computes the direction of each of the specified diffraction orders. If 
you know the transmittance or reflectance associated with each order, you can 
specify them as well. A wavelength-scale model, solving the electromagnetic wave 
equation in the frequency domain, can generate this data.
Czerny–Turner Monochromator: An arrangeme
```

### Section 11

```
13 ---
 | 13
Intensity and Polarization
The intensity of each ray is computed by solving for a set of four variables called 
the Stokes parameters. Because the rays represent electromagnetic waves, in 
general it is often necessary to store information about the direction of the 
electromagnetic field vector, not just its amplitude, and the Stokes parameters 
accomplish this with ease.
Whenever the ray intensity is solved for in the Geometrical Optics interface, the 
complete state of polarization of the ray is also recorded. Any combination of 
different polarization states can be included in the same model, meaning that the 
rays can be any combination of the following:
• Unpolarized,
• Circularly polarized,
• Elliptically polarized,
• Linearly polarized, or
• Partially polarized, with any degree of polarization between 0 and 1.
It is important to note that ray intensity is always solved for in radiometric, not 
photometric, units. In other words, the intensity is represented as an e
```

### Section 12

```
14 ---
14 | 
DIELECTRIC COATINGS ON BOUNDARIES
In practice, very few refracting boundaries are simply discontinuities between two 
domains with different refractive indices. Most lenses and mirrors are coated with 
one or more thin dielectric layers that cause the reflection and transmission 
coefficients to differ from a simple implementation of the Fresnel coefficients.
If you know the properties of each layer in a dielectric coating — the thickness and 
refractive index of each layer, and the order in which the layers appear — then you 
can build these layers directly into the Material Discontinuity boundary condition. 
The Fresnel coefficients are then automatically adjusted to take each layer into 
account, in addition to the refractive indices of the two adjacent domains.
You can also specify that some of these dielectric layers are periodic, allowing you 
to quickly create multilayer coatings with tens or hundreds of layers.
Distributed Bragg Reflector (DBR): Several thin dielec
```

### Section 13

```
15 ---
 | 15
OTHER BOUNDARY CONDITIONS TO CONTROL POLARIZATION
Dedicated boundary conditions to manipulate ray intensity and polarization are 
available. These boundary conditions do not affect the ray direction but do modify 
the Stokes parameters of the outgoing ray. These include the following:
• Ideal linear polarizers,
• Linear or circular wave retarders,
• Depolarizers,
• Customized 4 by 4 Mueller matrices that can represent nearly any 
combination of optical components.
Linear Wave Retarder tutorial: An unpolarized ray (going left to right) passes through a linear polarizer, 
a quarter-wave retarder, and a second linear polarizer orthogonal to the first. Polarization ellipses are 
shown in the ray diagram. The color expression indicates the ray intensity.
Visualizing Polarization
You can see the effects of different boundary conditions on polarization by 
plotting polarization ellipses along each ray. These ellipses show whether the ray 
is linearly, circularly, or elliptically 
```

### Section 14

```
16 ---
16 | 
Modeling Tools
In addition to the physics features described previously, the Ray Optics Module 
provides a variety of tools to help you set up your model and analyze results.
Optical Material Library
The Optical Material Library features more than 1700 materials, including more 
than 500 optical glasses. For most of these glasses, the refractive index is defined 
using optical dispersion coefficients to support accurate ray tracing of 
polychromatic light. Many of these glasses also include tabulated internal 
transmittance data as a function of wavelength, enabling volumetric light 
absorption to be predicted, as well as coefficients that describe the temperature 
dependence of the refractive index. Finally, most optical glasses include additional 
properties such as density, Young’s modulus, Poisson’s ratio, thermal 
conductivity, specific heat capacity, and thermal expansion coefficient, which 
facilitate coupled structural-thermal-optical performance (STOP) analysis.
T
```

### Section 15

```
18 ---
18 | 
Ray Sources
The Geometrical Optics interface provides a variety of ray sources, called ray 
release features, to specify the initial position and direction of rays. Any number 
of ray sources of different types can be used in the same model.
GRID SOURCES
The most direct way to specify the ray release positions is with a grid-based release. 
As shown below, there are several ways to control the initial positions of the rays.
At each release position, the rays can propagate outward in a single direction or in 
a spherical, hemispherical, conical, or Lambertian (cosine law) distribution. A 
dedicated Solar Radiation feature is also available to initialize the ray direction 
based on the location on Earth’s surface and the date and time.
Rays can be released in a cylindrical (far left), hexapolar (middle left), rectangular (middle right), or 
nonuniform grid (far right).
DOMAIN AND BOUNDARY SOURCES
You can release rays from a selected set of domains or boundaries. The distribu
```

### Section 16

```
19 ---
 | 19
ILLUMINATED SURFACES
If you know that light will be reflected or refracted by a surface somewhere in the 
model geometry, you do not need to explicitly model the path of the incident 
light. Using the Illuminated Surface node, you can release reflected or refracted 
light directly from the selected boundary, just by specifying the direction of the 
incident light that hits it. There is also a built-in option to release reflected or 
refracted sunlight. Optionally, perturbations due to surface roughness and the 
solar limb darkening effect can be included.
Note that the Illuminated Surface node does not consider shading of the selected 
boundary; it assumes that the entire surface can release reflected or refracted light. 
If part of the surface is obscured or vignetted, it is still necessary to trace the 
incident rays on their path toward the surface.
Rays released from an illuminated solar reflector and resulting concentration ratios in the focal plane. The 
top row is t
```

### Section 17

```
20 ---
20 | 
GAUSSIAN BEAMS
While solving for ray intensity or power, you can use the Gaussian Beam ray release 
feature to launch rays with a Gaussian intensity or power distribution.
The Geometrical Optics interface can only make rays follow curved paths if the 
medium has a graded refractive index. Rays do not behave exactly like a Gaussian 
beam in the vicinity of a beam waist, where the curvature of isosurfaces of constant 
phase can change nonlinearly as a function of distance along the nominal beam 
axis. Therefore, the Gaussian Beam ray release feature is only appropriate to use in 
the asymptotic limits where the geometry is either much larger or much smaller 
than the Rayleigh range.
Release of a Gaussian beam from a point. The ray power is a Gaussian function of the release angle. 
This type of power distribution is appropriate when the geometry is much larger than the Rayleigh range.
BLACKBODY RADIATION
You can use the Blackbody Radiation node to release rays from a surface
```

### Section 18

```
21 ---
 | 21
Ray-Thermal Coupling
If the refractive indices in a ray optics model are complex-valued, then the 
imaginary part is treated as an absorption term. A ray propagating through a 
complex-valued refractive index loses some of its energy through this attenuation, 
and it is possible to deposit an equal amount of energy into the surrounding 
domain as a heat source term.
A dedicated Multiphysics interface, the Ray Heating interface, is available to use 
the heat generated by ray propagation in absorbing media with another physics 
interface for computing temperature, such as the Heat Transfer in Solids interface. 
The Ray Heating interface enables bidirectional couplings to be set up, allowing 
phenomena such as thermal lensing to be modeled.
Unidirectional coupling from ray optics to heat transfer.
Bidirectional coupling between ray optics and heat transfer, including thermal stress.
A ray passes through a layer of absorbing material, causing the temperature in the layer to in
```

### Section 19

```
22 ---
22 | 
Multiscale Electromagnetics Modeling
The Geometrical Optics interface uses the assumption that the wavefronts 
represented by rays are locally plane. Thus, the rays should be far away from any 
objects that are comparable in size to the wavelength. Diffraction effects are also 
ignored. In other words, ray tracing requires an optically large modeling domain.
Other optional add-on modules for COMSOL Multiphysics provide physics 
interfaces that solve Maxwell’s equations in the frequency domain, allowing 
accurate calculation of the fields in a wavelength-scale geometry. These interfaces 
can fully resolve every oscillation of the electric field with a finite element mesh, 
but they become computationally expensive if the geometry spans a large number 
of wavelengths. For second-order elements, about 5 elements per wavelength are 
needed (the Nyquist criterion).
For true multiscale modeling of electromagnetic wave propagation, in which a 
wavelength-scale source releases rad
```

### Section 20

```
23 ---
 | 23
RELEASING FROM THE ELECTRIC FIELD IN AN ADJACENT REGION
If you first solve for the electric field in the frequency domain using the 
Electromagnetic Waves, Frequency Domain interface or the Electromagnetic 
Waves, Beam Envelopes interface, you can then release rays from surfaces adjacent 
to the simulation domain using the Release from Electric Field node.
RELEASING WAVES USING A FAR-FIELD RADIATION PATTERN
After solving for the far-field radiation pattern of an antenna or waveguide using 
the Far-Field Domain feature, you can release rays with an intensity distribution 
that matches this radiation pattern. The Release from Far-Field Radiation Pattern 
node can release rays from a grid of points. At the release points, you can also 
specify Euler angles to rotate the ray intensity distribution.
Ray release based on the far-field radiation pattern of a dipole antenna.
```

## Documentation Structure (api_optics_wave_extract.txt)

```
  TOC:   Introduction (p.5)
  TOC:     The Use of the Wave Optics Module (p.6)
  TOC:   The Wave Optics Module Physics Interfaces (p.16)
  TOC:     Physics Interface Guide by Space Dimension and Study Type (p.20)
  TOC:   Tutorial Model: Directional Coupler (p.23)
  TOC:     Introduction (p.23)
  TOC:     Model Definition (p.24)
  TOC:     Results and Discussion (p.26)
  TOC:     Reference (p.33)
  TOC:     Model Wizard (p.33)
  TOC:     Global Definitions - Parameters (p.34)
  TOC:     Geometry 1 (p.35)
  TOC:     Definitions (p.38)
  TOC:     Materials (p.38)
  TOC:     Electromagnetic Waves, Beam Envelopes (p.40)
  TOC:     Mesh (p.42)
  TOC:     Study 1 (p.44)
  TOC:     Results (p.44)
  TOC:     Study, Unidirectional (p.50)
  TOC:     Results (p.51)
  TOC:     Electromagnetic Waves, Beam Envelopes, Unidirectional (p.55)
  TOC:     Study, Unidirectional (p.56)
  TOC:     Results (p.56)
  TOC:     Electromagnetic Waves, Beam Envelopes, Unidirectional (p.56)
  TOC:     Mesh, Unidirectional (p.57)
  TOC:     Mesh, Bidirectional (p.58)
  TOC:     Add Study (p.59)
  TOC:     Study, Bidirectional (p.59)
  TOC:     Results (p.60)
  TOC:     Component 1 (p.63)
  TOC:   Contents (p.3)
  TOC:   Introduction (p.9)
  TOC:     About the Wave Optics Module (p.10)
  TOC:       About the Wave Optics Module (p.10)
  TOC:       What Problems Can You Solve? (p.11)
  TOC:       The Wave Optics Module Physics Interface Guide (p.12)
  TOC:       Common Physics Interface and Feature Settings and Nodes (p.14)
  TOC:       Selecting the Study Type (p.14)
  TOC:         Comparing the Time Dependent and Frequency Domain Studies (p.14)
  TOC:         comparing the electromagnetic waves, frequency domain and the electromagnetic waves, beam envelopes interfaces (p.15)
  TOC:         comparing the electromagnetic waves, frequency domain and the electromagnetic waves, Boundary Elements interfaces (p.16)
  TOC:       The Wave Optics Module Modeling Process (p.17)
  TOC:       Where Do I Access the Documentation and Application Libraries? (p.17)
  TOC:         The Documentation and Online Help (p.18)
  TOC:         The Application Libraries Window (p.19)
  TOC:         Contacting COMSOL by Email (p.19)
  TOC:         COMSOL Access and Technical Support (p.19)
  TOC:         COMSOL Online Resources (p.20)
  TOC:     Overview of the User’s Guide (p.21)
  TOC:       Table of Contents, Glossary, and Index (p.21)
```

## Key API Content (42 sections)

### Section 1

```
=== IntroductionToWaveOpticsModule.pdf ===
Pages: 78
  TOC:   Introduction (p.5)
  TOC:     The Use of the Wave Optics Module (p.6)
  TOC:   The Wave Optics Module Physics Interfaces (p.16)
  TOC:     Physics Interface Guide by Space Dimension and Study Type (p.20)
  TOC:   Tutorial Model: Directional Coupler (p.23)
  TOC:     Introduction (p.23)
  TOC:     Model Definition (p.24)
  TOC:     Results and Discussion (p.26)
  TOC:     Reference (p.33)
  TOC:     Model Wizard (p.33)
  TOC:     Global Definitions - Parameters (p.34)
  TOC:     Geometry 1 (p.35)
  TOC:     Definitions (p.38)
  TOC:     Materials (p.38)
  TOC:     Electromagnetic Waves, Beam Envelopes (p.40)
  TOC:     Mesh (p.42)
  TOC:     Study 1 (p.44)
  TOC:     Results (p.44)
  TOC:     Study, Unidirectional (p.50)
  TOC:     Results (p.51)
  TOC:     Electromagnetic Waves, Beam Envelopes, Unidirectional (p.55)
  TOC:     Study, Unidirectional (p.56)
  TOC:     Results (p.56)
  TOC:     Electromagnetic Waves, Beam Envel
```

### Section 2

```
3 ---
 | 3
Contents 
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
The Use of the Wave Optics Module . . . . . . . . . . . . . . . . . . . . . . . . 6
The Wave Optics Module Physics Interfaces. . . . . . . . . . . . . . . 16
Physics Interface Guide by Space Dimension and Study Type . . . 20
Tutorial Model: Directional Coupler . . . . . . . . . . . . . . . . . . . . . . 23
Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
Model Definition. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Results and Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
Reference. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
```

### Section 3

```
5 ---
 | 5
Introduction
The Wave Optics Module is used by engineers and scientists to understand, 
predict, and design electromagnetic wave propagation and resonance effects in 
optical applications. Simulations of this kind result in more powerful and efficient 
products and engineering methods. It allows its users to quickly and accurately 
predict electromagnetic field distributions, transmission and reflection 
coefficients, and power dissipation in a proposed design. Compared to traditional 
prototyping, it offers the benefits of lower cost and the ability to evaluate and 
predict entities that are not directly measurable in experiments. It also allows the 
exploration of operating conditions that would destroy a real prototype or be 
hazardous.
This module covers electromagnetic fields and waves in two-dimensional and 
three-dimensional spaces. All modeling formulations are based on Maxwell’s 
equations together with material laws for propagation in various media. The 
modeling c
```

### Section 4

```
6 ---
6 | 
and solver selection steps are usually carried out automatically using default 
settings, which are tuned for each specific Wave Optics interface.
The Wave Optics Module application library describes the physics interfaces and 
their different features through tutorial and benchmark examples for the different 
formulations. The library includes examples addressing gratings and 
metamaterials, laser cavities, nonlinear optics, optical scattering, waveguides and 
couplers, and benchmark models for verification and validation of the Wave Optics 
interfaces.
This introduction is intended to give you a jump start in your modeling work. It 
has examples of the typical use of the Wave Optics Module, a list of the physics 
interfaces with a short description, and a tutorial model that introduces the 
modeling workflow.
The Use of the Wave Optics Module
The Wave Optics interfaces are used to model electromagnetic fields and waves in 
optical applications. Typical wavelengths for opti
```

### Section 5

```
11 ---
 | 11
A Far-Field Domain is used in the model to calculate the far-field pattern of the 
scattered waves, as shown in Figure 5.
Figure 5: The far-field radiation pattern in the E-plane (blue) and H-plane (green) when wavelength is 
700 nm.
```

### Section 6

```
12 ---
12 | 
The Wave Optics Module also offers a comprehensive set of features for 2D 
modeling, including both source driven wave propagation and mode analysis. 
Figure 6 shows mode analysis of a microstructured optical fiber.
Figure 6: The surface plot visualizes the norm of the tangential and longitudinal electric and magnetic 
fields for one of the two degenerate HE11-like modes for a holey fiber. From Leaky Modes in a 
Microstructured Optical Fiber in the Wave Optics Module application library.
In both 2D and 3D, the analysis of periodic structures is popular. Figure 7 is an 
example of a plane wave incident on a metallic wire grating with a dielectric 
substrate.
Figure 7: Electric field norm for TE incidence at π/5 radians. From Plasmonic Wire Grating in the Wave 
Optics Module application library.
```

### Section 7

```
14 ---
14 | 
surface-emitting laser (VCSEL) after a self-consistent solution for the resonance 
frequency and the threshold gain.
Figure 10: The mode field of a vertical-cavity surface-emitting laser (VCSEL), for a self-consistent solution 
of the resonance frequency and the threshold gain. From Threshold Gain Calculations for Vertical-Cavity 
Surface-Emitting Lasers (VCSELs) in the Wave Optics Module application library.
The Wave Optics interfaces can easily be combined with physics interfaces from 
other physics areas, such as heat transfer, structural mechanics, semiconductor 
physics and low-frequency electromagnetics. Figure 11 shows the result of a 
multiphysics simulation, combining the Electromagnetic Waves, Frequency 
Domain interface from the Wave Optics Module with the Electrostatics and the 
Weak Form PDE interfaces from the COMSOL Multiphysics platform product. 
Using these three physics interfaces, the Oseen–Frank equation is solved for the 
distribution of the directors 
```

### Section 8

```
16 ---
16 | 
The Wave Optics Module Physics Interfaces
The Wave Optics interfaces are based upon Maxwell’s equations together with 
material laws. In the module, these laws of physics are translated by the Wave 
Optics interfaces to sets of partial differential equations with corresponding initial 
and boundary conditions.
The Wave Optics interfaces define a number of features. Each feature represents a 
term or condition in the underlying Maxwell-based formulation and may be 
defined in a geometric entity of the model, such as a domain, boundary, edge (for 
3D components), or point. 
Figure 12 uses the Plasmonic Wire Grating application from the Wave Optics 
Module application library to show the Model Builder window and the Settings 
window for the selected Wave Equation, Electric 1 feature node. The Wave 
Equation, Electric 1 node adds terms representing the Helmholtz wave equation 
to the model equations for, in this case, all domains in the model. As this is an 
example of a perio
```

### Section 9

```
17 ---
 | 17
used for exciting and absorbing waves and the Floquet Periodic Condition relates 
fields on parallel opposing boundaries with Floquet periodicity conditions.
Figure 12: The Model Builder (left), and the Settings window for Wave Equation, Electric (right). The 
Equation section shows the model equations and the terms added by the Wave Equation, Electric 1 node 
to the model equations. The added terms are underlined with a dotted line. The text also explains the 
link between the Dielectric node and the values for the refractive index.
```

### Section 10

```
18 ---
18 | 
Figure 13 shows the Wave Optics interfaces, as displayed in the Model Wizard for 
this module. 
Figure 13: The Wave Optics Module physics interfaces as displayed in the Model Wizard.
This module includes Wave Optics interfaces (
) for frequency-domain 
modeling and time-domain modeling, respectively. It also includes the Laser 
Heating interface, available under Heat Transfer. Also see Physics Interface Guide by 
Space Dimension and Study Type.
With the addition of the Semiconductor Module license, you also get the 
Semiconductor Optoelectronics, Beam Envelopes and The Semiconductor 
Optoelectronics, Frequency Domain interfaces that model the interaction of 
electromagnetic waves with semiconductors.
A brief overview of the Wave Optics interfaces follows.
ELECTROMAGNETIC WAVES, FREQUENCY DOMAIN
The Electromagnetic Waves, Frequency Domain interface (
) solves a 
frequency-domain wave equation for the electric field. The sources can be in the 
form of point dipoles, line cur
```

### Section 11

```
19 ---
 | 19
wavelength). The sources can be in the form of incident fields on boundaries, 
surface currents, or electric or magnetic fields on boundaries. The interface can be 
used for propagation problems at a fixed frequency and for finding 
eigenfrequencies in a resonant structure. Some typical applications that are 
simulated with the interface are waveguide structures, like directional couplers, 
nonlinear optical phenomena, and laser beam propagation.
ELECTROMAGNETIC WAVES, BOUNDARY ELEMENTS
The Electromagnetic Waves, Boundary Elements interface (
) solves a 
frequency-domain wave equation for the electric field. The formulation is based 
on the boundary element method (BEM) and requires the availability of a Green’s 
function. Thus, the physics interface solves the vector Helmholtz equation for 
piecewise-constant material properties.
The interface is fully multiphysics enabled and can be coupled seamlessly with the 
physics interfaces that are based on the finite element meth
```

### Section 12

```
20 ---
20 | 
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
LASER HEATING
The Laser Heating interface (
) is used to model electromagnetic heating for 
systems and devices where the electric field amplitude varies slowly on a 
wavelength scale. This multiphysics interface adds an Electromagnetic Waves, 
Beam Envelopes interface and a Heat Transfer in Solids interface. The 
multiphysics couplings add the electromagnetic losses from the electr
```

### Section 13

```
21 ---
 | 21
Laser Heating1
—
3D, 2D, 2D 
axisymmetric
frequency–stationary; 
frequency–transient; 
frequency–stationary, 
one-way electromagnetic 
heating; frequency–transient, 
one-way electromagnetic 
heating
 Optics
 Wave Optics
Electromagnetic Waves, 
Beam Envelopes
ewbe
3D, 2D, 2D 
axisymmetric
adaptive frequency sweep; 
boundary mode analysis; 
eigenfrequency; frequency 
domain; frequency domain, 
modal; wavelength domain; 
frequency domain source 
sweep
Electromagnetic Waves, 
Boundary Elements
ebem
3D, 2D
frequency domain; 
wavelength domain
Electromagnetic Waves, 
Frequency Domain
ewfd
3D, 2D, 2D 
axisymmetric
adaptive frequency sweep; 
boundary mode analysis; 
eigenfrequency; frequency 
domain; frequency domain, 
modal; mode analysis (2D 
and 2D axisymmetric 
models only); wavelength 
domain; frequency domain 
source sweep
Electromagnetic Waves, 
Time Explicit
teew
3D, 2D, 2D 
axisymmetric
time dependent; time 
dependent with FFT
Electromagnetic Waves, 
Transient
ewt
3D, 2D,
```

### Section 14

```
24 ---
24 | 
mode, and an antisymmetric supermode (see Figure 16 and Figure 18), with an 
effective index that is slightly lower than the effective index of the unperturbed 
waveguide mode.
Since the supermodes are the solution to the wave equation, if you excite one of 
them, it will propagate unperturbed through the waveguide. However, if you 
excite both, the symmetric and the antisymmetric mode, which have different 
propagation constants, there will be a beating between these two waves. Thus, you 
will see that the power fluctuates back and forth between the two waveguides as 
the waves propagate through the waveguide structure. You can adjust the length 
of the waveguide structure to get coupling from one waveguide to the other 
waveguide. By adjusting the phase difference between the fields of the two 
supermodes, you can decide which waveguide will initially be excited.
Model Definition
The directional coupler, as shown in Figure 14, consists of two waveguide cores 
embedded in
```

### Section 15

```
25 ---
 | 25
In the simulation, this beat length must be well resolved. Since the waveguide 
length is half of the beat length and the waveguide length is discretized into 20 
subdivisions, the beat length will be very well resolved in the model.
The model uses two numeric ports per input and exit boundary (see Figure 14). 
The two ports define the lowest symmetric and antisymmetric modes of the 
waveguide structure.
In the second part of the modeling procedure, the bidirectional formulation is 
used. In this case, the two wave vectors are codirectional — they point in the same 
direction. However, the magnitude of the wave vectors is given by the 
propagation constants of the two beating modes. Thus, you expect the two waves 
to have almost constant amplitudes, so the mesh can be very coarse in the 
propagation direction.
A problem with the first two procedures is that the numerical procedure returns 
mode fields with an arbitrary phase. Thus, when you superpose the two input port 
mo
```

### Section 16

```
26 ---
26 | 
,
 (4)
where Pin,i is the specified input power for mode i and θin,i is the corresponding 
specified mode phase.
Comparing Equation 1, Equation 3, and Equation 4, we can deduce that
 (5)
or
 (6)
and
.
 (7)
Equation 6 and Equation 7 can now be used for specifying the input power and 
mode phase for the two exciting ports.
Results and Discussion
Figure 15 to Figure 18 show the results of the initial boundary mode analysis. The 
first two modes (those with the largest effective mode index) are both symmetric. 
Figure 15 shows the first mode. This mode has the transverse polarization 
ET i
,
ET0 i
,
Pin i
,
Pi
⁄
eiθin i
,
=
ci
Pin i
,
Pi
⁄
eiθin i
,
=
Pin i
,
ci
2 Pi
1
4 Pi
-----------
ET t
et
arg
,
H∗T0 i
,
×
(
) nˆ
⋅
S
d
A
2
=
=
θin i
,
ci
(
)
arg
1
Pi
-----
ET t
et
arg
,
H∗T0 i
,
×
(
) nˆ
⋅
S
d
A






arg
=
=

=== WaveOpticsModuleUsersGuide.pdf ===
Pages: 286
  TOC:   Contents (p.3)
  TOC:   Introduction (p.9)
  TOC:     About the Wave Optics Module (p.10)
  TOC:  
```

### Section 17

```
3 ---
C O N T E N T S  | 3
C o n t e n t s  
C h a p t e r  1 :  I n t r o d u c t i o n
About the Wave Optics Module 
 10
About the Wave Optics Module .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  10
What Problems Can You Solve?  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  11
The Wave Optics Module Physics Interface Guide  .   .   .   .   .   .   .   .   .   .  12
Common Physics Interface and Feature Settings and Nodes    .   .   .   .   .   .  14
Selecting the Study Type .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  14
The Wave Optics Module Modeling Process   .   .   .   .   .   .   .   .   .   .   .   .  17
Where Do I Access the Documentation and Application Libraries? .   .   .   .  17
Overview of the User’s Guide 
 21
Ch a p t e r  2 :  W av e  O p t i c s  Mo d e l i n g
Preparing for Wave Optics Modeling 
 25
Simplifying Geometries 
 26
2D Models  .   .   .   .   .   .   .   .   .   .   .   .   .   .  
```

### Section 18

```
4 ---
4 | C O N T E N T S
Interface.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  41
The Radiation Pattern Plots .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  42
Modeling with Far-Field Calculations (Far-Field Domain, 
Inhomogeneous) 
 51
Far-Field Domain, Inhomogeneous Support in the Electromagnetic 
Waves, Frequency Domain Interface  .   .   .   .   .   .   .   .   .   .   .   .   .   .  51
The Radiation Pattern Plots .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  52
Maxwell’s Equations 
 54
Maxwell’s Equations.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  54
Constitutive Relations .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  55
Boundary Conditions  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  57
Potentials.   .   .   .   .   .   .   .   .   .   .   .   .   .   .
```

### Section 19

```
5 ---
C O N T E N T S  | 5
Lossy Eigenvalue Calculations 
 88
Eigenfrequency Analysis  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  88
Mode Analysis and Boundary Mode Analysis   .   .   .   .   .   .   .   .   .   .   .   .  90
Material Libraries 
 93
Part Libraries 
 97
Reduced-Order Modeling 
 99
Adaptive Frequency Sweep Using Asymptotic Waveform Evaluation 
(AWE) Method  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .  99
Frequency Domain, Modal Method .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    101
Electromagnetic Quantities 
 102
Ch a p t e r  3 :  W av e  O p t i c s  I n t e r f a c e s
The Electromagnetic Waves, Frequency Domain Interface 
 106
Domain, Boundary, Edge, Point, and Pair Nodes for the 
Electromagnetic Waves, Frequency Domain Interface    .   .   .   .   .   .    119
Wave Equation, Electric  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    121
Initial
```

### Section 20

```
6 ---
6 | C O N T E N T S
Port.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    142
Circular Port Reference Axis  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    154
Diffraction Order    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    154
Orthogonal Polarization  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    157
Periodic Port Reference Point .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    158
Periodic Port   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    159
Electric Field  .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    160
Magnetic Field .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    160
Matched Boundary Condition .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .    161
S
```

