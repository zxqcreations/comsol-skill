"""Fix 6 audit issues: add missing mph code examples and expression references."""
from pathlib import Path

REF = Path(r"D:\ENV\claude\comsol-skill\references")

EXAMPLES = {
    "api_acdc.md": """
## mph API Usage

```python
# Electrostatics
es = comp.physics().create('es', 'Electrostatics', 'geom1')
gnd = es.feature().create('gnd1', 'Ground', 1)
term = es.feature().create('term1', 'Terminal', 1)
term.set('V0', '10[V]')

# Electric Currents
ec = comp.physics().create('ec', 'ElectricCurrents', 'geom1')
ec.feature().create('pot1', 'ElectricPotential', 1).set('V0', '5[V]')

# Magnetic Fields
mf = comp.physics().create('mf', 'MagneticFields', 'geom1')
mf.feature().create('coil1', 'Coil', 2).set('Icoil', '1[A]')
```
""",
    "api_heat_transfer.md": """
## mph API Usage

```python
ht = comp.physics().create('ht', 'HeatTransferInSolids', 'geom1')
ht.feature().create('temp1', 'TemperatureBoundary', 1).set('T0', '373.15[K]')
ht.feature().create('hf1', 'HeatFluxBoundary', 1).set('q0', '1e4[W/m^2]')
model.evaluate('ht.Tmax', 'K')
```
""",
    "api_semiconductor.md": """
## mph API Usage

```python
semi = comp.physics().create('semi', 'Semiconductor', 'geom1')
semi.set('CarrierStatistics', 'MaxwellBoltzmann')
doping = semi.feature().create('dop1', 'DopingProfile', 2)
ohmic = semi.feature().create('oc1', 'OhmicContact', 1)
ohmic.set('V0', '0[V]')
model.evaluate('semi.n', '1/cm^3')
```
""",
    "api_electric_discharge.md": """
## mph API Usage

```python
ed = comp.physics().create('ed', 'ElectricDischarge', 'geom1')
gnd = ed.feature().create('gnd1', 'Ground', 1)
anode = ed.feature().create('pot1', 'ElectricPotential', 1)
anode.set('V0', '10[kV]')
model.evaluate('ed.Ne', '1/m^3')
```
""",
    "api_acoustics_mems.md": """
## mph API Usage

```python
acpr = comp.physics().create('acpr', 'PressureAcoustics', 'geom1')
src = acpr.feature().create('nv1', 'NormalVelocity', 1)
src.set('nvel', '0.01[m/s]')
model.evaluate('acpr.p_t', 'Pa')
```
""",
}

EXPR_SECTIONS = {
    "api_structural.md": """
## Expression Reference

| Expression | Unit | Description |
|-----------|------|-------------|
| `solid.mises` | Pa | von Mises stress |
| `solid.disp` | m | Total displacement |
| `solid.u`, `solid.v`, `solid.w` | m | Displacement components |
| `solid.Ws` | J/m^3 | Strain energy density |
| `solid.sx`, `solid.sy`, `solid.sz` | Pa | Normal stress |
| `solid.ex`, `solid.ey`, `solid.ez` | 1 | Normal strain |
| `solid.epsilonvol` | 1 | Volumetric strain |
| `es.V` | V | Electric potential (piezo) |
| `es.normE` | V/m | Electric field magnitude |
| `es.Dz` | C/m^2 | Electric displacement, z |
""",
}

# Apply mph examples
for fname, content in EXAMPLES.items():
    path = REF / fname
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "```python" not in text:
        text += content
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"{fname}: added mph code examples")

# Apply expression sections
for fname, content in EXPR_SECTIONS.items():
    path = REF / fname
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if "Expression Reference" not in text and "Expression" not in text:
        text += content
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"{fname}: added expression reference")

print("Done!")
