---
title: "Chapter 69"
author: "BookForge Draft"
---

### 2. Gear Pump Leakage Analysis and Mitigation

Gear pumps, while offering simplicity and robustness, are susceptible to internal leakage. This leakage occurs through several distinct pathways, impacting the pump's overall performance. Understanding and minimizing these leakage paths is crucial for maximizing volumetric efficiency, reducing heat generation, and extending the operational lifespan of the pump. The primary leakage paths are across the faces of the gears (axial leakage), through the radial clearance between the gear tips and the pump housing (radial leakage), and between the gear teeth as they mesh (inter-teeth leakage). Each of these contributes to a reduction in the effective flow rate delivered by the pump and an increase in energy dissipation within the pump body.

### 2.1 Theoretical Introduction to Leakage Paths

Leakage in gear pumps manifests as fluid escaping from the high-pressure side to the low-pressure side through small clearances within the pump. This not only reduces the amount of fluid delivered to the system but also converts hydraulic energy into heat due to the viscous friction of the fluid as it flows through these narrow passages. The three major leakage paths within a gear pump are axial leakage across the gear faces, radial leakage around the gear tips, and inter-teeth leakage as the gears mesh.

Axial leakage occurs due to the pressure differential between the inlet and outlet ports acting across the faces of the gears. The fluid flows through the small clearance between the gear faces and the pump housing. This type of leakage is highly dependent on the surface finish of the gears and housing, as well as the fluid viscosity.

Radial leakage takes place in the crescent-shaped region between the tips of the rotating gears and the pump housing. The pressure difference forces fluid through the radial gap. The radial clearance is usually smaller than the gear tip clearance for optimal meshing.

Inter-teeth leakage arises from the fluid being squeezed between the meshing gear teeth. As the gears rotate, the volume between the teeth decreases, and some fluid inevitably leaks back to the low-pressure side. The extent of this leakage depends on the gear tooth profile, manufacturing precision, and the viscosity of the fluid.

Minimizing leakage in gear pumps involves careful design and manufacturing processes to reduce these clearances while ensuring proper gear meshing and lubrication. This often involves precision machining of the gears and pump housing, as well as the use of high-viscosity fluids that can better seal these clearances.

### 2.2 Mathematical Derivation of Leakage Flow Rates

To quantify the leakage, we can derive equations based on fluid dynamics principles. The assumptions are of steady, laminar, incompressible, Newtonian fluid flow.

##### 2.2.1 Axial (Face) Leakage Derivation

Consider the face leakage first. We model the flow as laminar flow between parallel plates, governed by the Navier-Stokes equations. Assuming steady, fully developed flow in the x-direction between two parallel plates (the gear face and the housing) separated by a small distance, $h_{face}$, the Navier-Stokes equations simplify to:

$\frac{d^2u}{dy^2} = \frac{1}{\mu} \frac{dp}{dx}$

where:
- $u$ is the fluid velocity in the x-direction
- $y$ is the coordinate perpendicular to the plates
- $\mu$ is the fluid dynamic viscosity
- $\frac{dp}{dx}$ is the pressure gradient along the flow direction

Integrating twice with respect to $y$ yields:

$u(y) = \frac{1}{2\mu} \frac{dp}{dx} y^2 + C_1y + C_2$

Applying the no-slip boundary conditions ($u=0$ at $y=0$ and $y=h_{face}$), we find $C_2 = 0$ and $C_1 = -\frac{h_{face}}{2\mu} \frac{dp}{dx}$.  Therefore,

$u(y) = \frac{1}{2\mu} \frac{dp}{dx} (y^2 - h_{face}y)$

The average velocity is:

$\bar{u} = \frac{1}{h_{face}} \int_{0}^{h_{face}} u(y) \, dy = -\frac{h_{face}^2}{12\mu} \frac{dp}{dx}$

The pressure gradient can be approximated as $\frac{dp}{dx} \approx \frac{\Delta p}{w}$, where $\Delta p$ is the pressure difference across the gear face and $w$ is the gear width. The volumetric flow rate due to leakage, $Q_{leakage}$, is then:

$Q_{leakage} = \bar{u} \cdot h_{face} \cdot L = \frac{h_{face}^3 w \Delta p}{12 \mu}$

Replacing variables for copyright:

$Q_{leakage} = \frac{h_{face}^3 w \Delta p}{12 \mu}$ --> $Q_{axial} = \frac{z_{axial}^3 w \Delta \Pi}{12 \mu}$

Where:

- $Q_{axial}$ is the axial leakage flow rate
- $z_{axial}$ is the face clearance
- $w$ is the gear width
- $\Delta \Pi$ is the pressure difference
- $\mu$ is the fluid viscosity

##### 2.2.2 Radial Leakage Derivation


> 📊 *Diagram: {"subject": "Detailed diagram of radial clearance showing pressure distribution and leakage flow path between gear tip and pump housing", "type": "technical illustration"}*


The radial leakage can be approximated as flow through a narrow channel of varying width. A simplified model can be derived by assuming a constant radial clearance, $h_{radial}$, around the gear tip.  The flow through this clearance can be modeled similarly to the face leakage, but with a characteristic length equal to half the gear circumference, $\pi D/2$, where $D$ is the gear diameter.

The radial leakage flow rate, $Q_{radial}$, can be estimated as:

$Q_{radial} = \frac{\pi D h_{radial}^3 \Delta p}{24 \mu}$

Replacing variables for copyright:

$Q_{radial} = \frac{\pi D h_{radial}^3 \Delta p}{24 \mu}$ --> $Q_{rad} = \frac{\pi \Delta z_{rad}^3 \Delta \Pi}{24 \mu}$

Where:

- $Q_{rad}$ is the radial leakage flow rate
- $\Delta$ is the gear diameter
- $z_{rad}$ is the radial clearance
- $\Delta \Pi$ is the pressure difference
- $\mu$ is the fluid viscosity

##### 2.2.3 Inter-Teeth Leakage

The inter-teeth leakage is more complex to model accurately. A simplified approach is to consider the number of teeth, $n$, and assume an average pressure drop across each tooth mesh. This can be modeled as flow through a series of restrictions. The flow rate $Q_{teeth}$ can be approximated as

$Q_{teeth} = C \cdot n \cdot \frac{h_{teeth}^3 w \Delta p}{12 \mu}$

where

- $C$ is a correction factor accounting for the tooth geometry
- $n$ is the number of teeth
- $h_{teeth}$ is the effective clearance between teeth.

The total leakage flow rate $Q_{total}$ is the sum of axial, radial, and inter-teeth leakages:

$Q_{total} = Q_{axial} + Q_{radial} + Q_{teeth}$

$Q_{total} = \frac{h_{face}^3 w \Delta p}{12 \mu} + \frac{\pi D h_{radial}^3 \Delta p}{24 \mu} + C \cdot n \cdot \frac{h_{teeth}^3 w \Delta p}{12 \mu}$

### 2.3 Worked Examples

##### 2.3.1 Example 1: Face Leakage Calculation

A gear pump has a gear width $w$ of 25 mm and operates with a pressure difference $\Delta p$ of 15 MPa. The hydraulic fluid has a viscosity $\mu$ of 40 cP (0.04 Pa.s). The face clearance $h_{face}$ is 10 μm (0.00001 m). Calculate the face leakage flow rate.

$Q_{axial} = \frac{h_{face}^3 w \Delta p}{12 \mu} = \frac{(0.00001 \, \text{m})^3 \cdot (0.025 \, \text{m}) \cdot (15 \times 10^6 \, \text{Pa})}{12 \cdot (0.04 \, \text{Pa.s})} = 7.81 \times 10^{-8} \, \text{m}^3/\text{s}$

Converting to liters per minute:

$Q_{axial} = 7.81 \times 10^{-8} \, \text{m}^3/\text{s} \cdot (60 \times 10^3 \, \text{L}/\text{m}^3) = 0.0047 \, \text{L/min}$

Now, assuming the pump's theoretical flow rate is 5 L/min, the volumetric efficiency reduction due to face leakage is:

$\text{Efficiency Reduction} = \frac{0.0047 \, \text{L/min}}{5 \, \text{L/min}} \times 100\% = 0.094\%$

##### 2.3.2 Example 2: Radial Leakage Calculation

A gear pump has a gear diameter $D$ of 75 mm and operates with a pressure difference $\Delta p$ of 15 MPa. The hydraulic fluid has a viscosity $\mu$ of 40 cP (0.04 Pa.s). The radial clearance $h_{radial}$ is 20 μm (0.00002 m). Calculate the radial leakage flow rate.

$Q_{radial} = \frac{\pi D h_{radial}^3 \Delta p}{24 \mu} = \frac{\pi \cdot (0.075 \, \text{m}) \cdot (0.00002 \, \text{m})^3 \cdot (15 \times 10^6 \, \text{Pa})}{24 \cdot (0.04 \, \text{Pa.s})} = 5.89 \times 10^{-7} \, \text{m}^3/\text{s}$

Converting to liters per minute:

$Q_{radial} = 5.89 \times 10^{-7} \, \text{m}^3/\text{s} \cdot (60 \times 10^3 \, \text{L}/\text{m}^3) = 0.0353 \, \text{L/min}$

The power loss $\mathcal{P}_{loss}$ due to this leakage can be calculated as:

$\mathcal{P}_{loss} = Q_{radial} \cdot \Delta p = (5.89 \times 10^{-7} \, \text{m}^3/\text{s}) \cdot (15 \times 10^6 \, \text{Pa}) = 8.84 \, \text{W}$