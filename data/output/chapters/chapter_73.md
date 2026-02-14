---
title: "Chapter 73"
author: "BookForge Draft"
---

# Single-Acting Cylinders: Fundamentals and Applications

Single-acting cylinders are fundamental components in hydraulic systems, characterized by their ability to exert force in one direction only. This unidirectional force generation simplifies their design and operation, making them suitable for various applications where precise control of movement in both directions is not required. In a single-acting cylinder, pressurized hydraulic fluid is introduced into one side of the piston, causing it to extend and perform work. The return stroke, however, is not powered by hydraulic pressure. Instead, it relies on an external force, commonly provided by a spring, gravity, or another mechanical mechanism.

The operational simplicity of single-acting cylinders offers advantages such as lower cost, simpler control systems, and reduced maintenance requirements. However, this simplicity comes at the cost of limited control over the return stroke. The speed and force of retraction are dictated by the external force, which may not always be consistent or controllable. This inherent limitation makes single-acting cylinders unsuitable for applications demanding precise bidirectional motion. Examples of typical uses include clamping devices, simple lifting mechanisms, and linear actuators where a controlled extension is needed, but a less controlled return is acceptable. For example, in a punch press, a single-acting cylinder might provide the force for the punching action, while a spring returns the punch to its initial position. Another application is in hydraulic jacks, where the cylinder lifts the load, and gravity, combined with a release valve, allows for controlled descent.

It's crucial to consider the energy efficiency trade-offs when using single-acting cylinders. Because the return stroke is not powered, the potential energy stored in the compressed spring (or the gravitational potential energy) is dissipated when the fluid is vented from the cylinder. This energy loss can be significant in high-cycle applications.


> 📊 *Diagram: {"subject": "Cross-sectional view of a generic single-acting cylinder with spring return. Label the following components: cylinder body, piston, piston rod, spring, hydraulic fluid inlet, vent, stroke length, bore diameter.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic symbol for a single-acting cylinder (ISO 1219 standard). Label the pressure port.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Simple hydraulic circuit diagram showing a single-acting cylinder controlled by a 3/2 directional control valve. Include a pump, reservoir, pressure relief valve, and connecting lines.", "type": "schematic"}*


## Mathematical Relationships

Understanding the mathematical relationships governing single-acting cylinder operation is crucial for proper design and selection. Key equations relate force, pressure, area, and stroke, allowing engineers to predict performance and optimize system parameters.

### Force Calculation

The force ($F$) exerted by a single-acting cylinder is directly proportional to the fluid pressure ($p$) and the piston area ($A$). This relationship is expressed as:

$F = p \cdot A$

Where:
- $F$ is the force exerted by the cylinder (in Newtons, N).
- $p$ is the hydraulic fluid pressure (in Pascals, Pa, or N/m²).
- $A$ is the area of the piston (in square meters, m²).

The piston area ($A$) is determined by the cylinder bore diameter ($D$) using the following equation, derived from the area of a circle:

$A = \frac{\pi D^2}{4}$

Where:
- $A$ is the area of the piston (in square meters, m²).
- $D$ is the cylinder bore diameter (in meters, m).
- $\pi$ is a mathematical constant approximately equal to 3.14159.

This equation stems from the fundamental definition of a circle's area. Imagine dividing the circular piston face into infinitesimally small sectors. As the number of sectors approaches infinity, the sum of their areas converges to $\pi r^2$, where $r$ is the radius of the circle. Since the diameter ($D$) is twice the radius ($r$), we can substitute $r = \frac{D}{2}$ into the equation, yielding $A = \pi (\frac{D}{2})^2 = \frac{\pi D^2}{4}$.

### Retraction Force (Spring Return)

In spring-return single-acting cylinders, the spring provides the force necessary to retract the piston. The spring force ($F_{spring}$) is proportional to the spring constant ($k$) and the spring compression distance ($x$):

$F_{spring} = k \cdot x$

Where:
- $F_{spring}$ is the force exerted by the spring (in Newtons, N).
- $k$ is the spring constant (in Newtons per meter, N/m).
- $x$ is the spring compression distance (in meters, m).

In practical applications, springs often have a pre-compression, which means they are already compressed to some extent when the cylinder is in its retracted position. The initial retraction force is influenced by this pre-compression. For reliable retraction, the spring force must always be greater than the friction force ($F_{friction}$) within the cylinder.

$F_{spring} > F_{friction}$

### Work Done

The work ($W$) done by the cylinder during extension is the product of the force ($F$) exerted and the distance ($d$) over which the force is applied (stroke length):

$W = F \cdot d = p \cdot A \cdot d$

Where:
- $W$ is the work done (in Joules, J).
- $F$ is the force exerted by the cylinder (in Newtons, N).
- $d$ is the stroke length (in meters, m).
- $p$ is the hydraulic fluid pressure (in Pascals, Pa).
- $A$ is the area of the piston (in square meters, m²).

### Hydraulic Power

The hydraulic power ($\mathcal{P}$) delivered to the cylinder is the product of the pressure ($p$) and the volumetric flow rate ($Q_{in}$) of the hydraulic fluid:

$\mathcal{P} = p \cdot Q_{in}$

Where:
- $\mathcal{P}$ is the hydraulic power (in Watts, W).
- $p$ is the hydraulic fluid pressure (in Pascals, Pa).
- $Q_{in}$ is the volumetric flow rate of the hydraulic fluid (in cubic meters per second, m³/s).

This equation highlights the relationship between pressure and flow rate in determining the power output of the hydraulic system. Higher pressure and flow rates result in greater power.

## Example Problems

Let's illustrate these concepts with a few example problems:

### Cylinder Force Problem

A single-acting cylinder has a bore diameter of 80 mm and is operated with a hydraulic pressure of 10 MPa. Calculate the force exerted by the cylinder.

1.  **Convert units:**- Diameter: $D = 80 \text{ mm} = 0.08 \text{ m}$
    - Pressure: $p = 10 \text{ MPa} = 10 \times 10^6 \text{ Pa}$

2.**Calculate piston area:**- $A = \frac{\pi D^2}{4} = \frac{\pi (0.08 \text{ m})^2}{4} \approx 0.005026 \text{ m}^2$

3.**Calculate force:**- $F = p \cdot A = (10 \times 10^6 \text{ Pa}) \cdot (0.005026 \text{ m}^2) \approx 50260 \text{ N}$

Therefore, the cylinder exerts a force of approximately 50260 N.**Mirror Problem:**A single-acting cylinder has a bore diameter of 120 mm and is operated with a hydraulic pressure of 18 MPa. Calculate the force exerted by the cylinder.

1.**Convert units:**- Diameter: $D = 120 \text{ mm} = 0.12 \text{ m}$
    - Pressure: $p = 18 \text{ MPa} = 18 \times 10^6 \text{ Pa}$

2.**Calculate piston area:**- $A = \frac{\pi D^2}{4} = \frac{\pi (0.12 \text{ m})^2}{4} \approx 0.01131 \text{ m}^2$

3.**Calculate force:**- $F = p \cdot A = (18 \times 10^6 \text{ Pa}) \cdot (0.01131 \text{ m}^2) \approx 203580 \text{ N}$

Therefore, the cylinder exerts a force of approximately 203580 N.

### Spring Selection Problem

A spring-return single-acting cylinder needs to overcome an external load of 300 N and a friction force of 30 N. The maximum spring compression distance is 50 mm. Determine the required spring constant.

1.**Convert units:**- Compression distance: $x = 50 \text{ mm} = 0.05 \text{ m}$

2.**Calculate the required spring force:**The spring force must overcome both the external load and the friction force:
    - $F_{spring} = F_{load} + F_{friction} = 300 \text{ N} + 30 \text{ N} = 330 \text{ N}$

3.**Calculate the spring constant:**- $k = \frac{F_{spring}}{x} = \frac{330 \text{ N}}{0.05 \text{ m}} = 6600 \text{ N/m}$

Therefore, the required spring constant is 6600 N/m.**Mirror Problem:**A spring-return single-acting cylinder needs to overcome an external load of 450 N and a friction force of 45 N. The maximum spring compression distance is 75 mm. Determine the required spring constant.

1.**Convert units:**- Compression distance: $x = 75 \text{ mm} = 0.075 \text{ m}$

2.**Calculate the required spring force:**The spring force must overcome both the external load and the friction force:
    - $F_{spring} = F_{load} + F_{friction} = 450 \text{ N} + 45 \text{ N} = 495 \text{ N}$

3.**Calculate the spring constant:**- $k = \frac{F_{spring}}{x} = \frac{495 \text{ N}}{0.075 \text{ m}} = 6600 \text{ N/m}$

Therefore, the required spring constant is 6600 N/m.

### Cylinder Stroke Problem

A single-acting cylinder needs to perform 50 J of work against a load of 500 N. Calculate the necessary stroke length.

1.**Known values:**- Work: $W = 50 \text{ J}$
    - Force: $F = 500 \text{ N}$

2.**Calculate the stroke length:**- $d = \frac{W}{F} = \frac{50 \text{ J}}{500 \text{ N}} = 0.1 \text{ m}$

Therefore, the necessary stroke length is 0.1 m (or 100 mm).**Mirror Problem:**A single-acting cylinder needs to perform 75 J of work against a load of 600 N. Calculate the necessary stroke length.

1.**Known values:**- Work: $W = 75 \text{ J}$
    - Force: $F = 600 \text{ N}$

2.**Calculate the stroke length:**- $d = \frac{W}{F} = \frac{75 \text{ J}}{600 \text{ N}} = 0.125 \text{ m}$

Therefore, the necessary stroke length is 0.125 m (or 125 mm).

### Hydraulic Power Problem

A single-acting cylinder with a bore diameter of 60 mm is operated at a hydraulic pressure of 14 MPa with a flow rate of 2.5 L/min. Calculate the hydraulic power needed.

1.**Convert units:**- Diameter: $D = 60 \text{ mm} = 0.06 \text{ m}$
    - Pressure: $p = 14 \text{ MPa} = 14 \times 10^6 \text{ Pa}$
    - Flow Rate: $Q_{in} = 2.5 \frac{\text{L}}{\text{min}} = 2.5 \times \frac{10^{-3} \text{m}^3}{60 \text{s}} \approx 4.167 \times 10^{-5} \text{m}^3/\text{s}$

2.**Calculate Hydraulic Power:**- $\mathcal{P} = p \cdot Q_{in} = (14 \times 10^6 \text{ Pa}) \cdot (4.167 \times 10^{-5} \text{m}^3/\text{s}) \approx 583.38 \text{ W}$

Therefore, the hydraulic power needed is approximately 583.38 W.**Mirror Problem:**A single-acting cylinder with a bore diameter of 90 mm is operated at a hydraulic pressure of 16 MPa with a flow rate of 3.5 L/min. Calculate the hydraulic power needed.

1.**Convert units:**- Diameter: $D = 90 \text{ mm} = 0.09 \text{ m}$
    - Pressure: $p = 16 \text{ MPa} = 16 \times 10^6 \text{ Pa}$
    - Flow Rate: $Q_{in} = 3.5 \frac{\text{L}}{\text{min}} = 3.5 \times \frac{10^{-3} \text{m}^3}{60 \text{s}} \approx 5.833 \times 10^{-5} \text{m}^3/\text{s}$

2.**Calculate Hydraulic Power:**
    - $\mathcal{P} = p \cdot Q_{in} = (16 \times 10^6 \text{ Pa}) \cdot (5.833 \times 10^{-5} \text{m}^3/\text{s}) \approx 933.28 \text{ W}$

Therefore, the hydraulic power needed is approximately 933.28 W.