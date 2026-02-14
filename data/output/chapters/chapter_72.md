---
title: "Chapter 72"
author: "BookForge Draft"
---

## 2. Rotary Actuators (Hydraulic Motors) and Hydraulic Cylinders (Linear Actuators)

Hydraulic systems provide a powerful method for transmitting power and controlling motion. Within these systems, actuators play a critical role in converting fluid power into mechanical work. Actuators can be broadly classified into two main categories: rotary actuators (also known as hydraulic motors) and linear actuators (hydraulic cylinders).

### Rotary Actuators (Hydraulic Motors)

Hydraulic motors are devices that convert hydraulic energy (pressure and flow) into rotational mechanical energy, providing continuous rotational motion. Unlike hydraulic cylinders that provide linear motion over a finite stroke, hydraulic motors can theoretically rotate indefinitely. The fundamental principle behind their operation relies on directing pressurized fluid against vanes, gears, or pistons that are connected to an output shaft. The fluid pressure exerts a force on these components, causing the shaft to rotate. This rotation can then be used to drive various mechanical systems.

Compared to electric motors, hydraulic motors offer distinct advantages in certain applications. One key advantage is their high torque-to-inertia ratio, meaning they can deliver substantial torque even at low speeds. This makes them ideal for applications requiring high starting torques or precise low-speed control. Another advantage is their high power density; hydraulic motors can deliver a significant amount of power for their size and weight. However, hydraulic motors are generally less energy-efficient than electric motors due to losses associated with fluid friction and leakage. They also tend to be noisier in operation and require a more complex hydraulic system infrastructure, including pumps, reservoirs, and control valves. The operation of a hydraulic motor is fundamentally linked to Pascal's Law, which states that pressure applied to a confined fluid is transmitted equally in all directions. This pressure acts on the internal components of the motor, generating torque and causing rotation. Torque is a measure of the twisting force that causes rotation, while angular velocity describes how fast the shaft is rotating.


> 📊 *Diagram: {"subject": "Basic schematic diagram of a hydraulic motor showing the fluid inlet and outlet ports, rotor, and shaft. Include pressure gauges at the inlet and outlet.", "type": "schematic diagram"}*


The theoretical relationships governing hydraulic motor performance can be derived from first principles. The torque ($T$) produced by a hydraulic motor is directly proportional to the pressure ($p$) of the hydraulic fluid and the motor's displacement ($V_d$), which is the volume of fluid required per revolution of the output shaft. We can derive this relationship by considering the work done by the fluid. The work done by the fluid is given by pressure times the swept volume ($W = p \cdot V_d$). This work is converted to rotational work ($W = T \cdot \theta$), where $\theta$ is the angle of rotation in radians. For one revolution, $\theta = 2\pi$. Equating the two expressions for work, we get $p \cdot V_d = T \cdot 2\pi$, which leads to:

$T = \frac{p \cdot V_d}{2\pi}$

Similarly, the angular velocity ($\omega$) of the motor is related to the input flow rate ($Q_{in}$) and the motor's displacement ($V_d$). The relationship is:

$\omega = \frac{Q_{in}}{V_d}$

Where $\omega$ is typically expressed in radians per second, and $Q_{in}$ and $V_d$ must have consistent units (e.g., m³/s and m³/revolution, respectively). Note that $\omega$ in RPM (revolutions per minute) can be calculated using $\omega_{RPM} = \omega \cdot 60 / (2\pi)$.

The power ($\mathcal{P}$) of a hydraulic motor is the product of its torque and angular velocity:

$\mathcal{P} = T \cdot \omega = p \cdot Q_{in}$

In real-world hydraulic motors, losses occur due to internal leakage and friction. These losses are quantified by various efficiency measures. *Volumetric efficiency* ($\eta_{vol}$) represents the ratio of the theoretical flow rate ($Q_{theoretical}$) required to achieve a certain speed to the actual flow rate ($Q_{actual}$) consumed by the motor:

$\eta_{vol} = \frac{Q_{theoretical}}{Q_{actual}}$

*Mechanical efficiency* or *torque efficiency* ($\eta_{mech}$) represents the ratio of the actual output torque ($T_{actual}$) to the theoretical torque ($T_{theoretical}$) that would be produced if there were no frictional losses:

$\eta_{mech} = \frac{T_{actual}}{T_{theoretical}}$

The *overall hydraulic efficiency* ($\eta_{hyd}$) is the product of the volumetric and mechanical efficiencies:

$\eta_{hyd} = \eta_{vol} \cdot \eta_{mech}$

This represents the overall effectiveness of the hydraulic motor in converting fluid power into mechanical power.

**Example Problems:Problem 1 (Torque Calculation):** A hydraulic motor has a displacement of $V_d = 150 \text{ cm}^3/\text{rev}$ and operates at a pressure of $p = 21 \text{ MPa}$. Calculate the output torque.

*Solution:*
1.  Convert displacement to $m^3/rev$: $V_d = 150 \frac{\text{cm}^3}{\text{rev}} \times (\frac{1 \text{ m}}{100 \text{ cm}})^3 = 1.05 \times 10^{-4} \text{ m}^3/\text{rev}$
2.  Convert pressure to Pascals: $p = 21 \text{ MPa} = 21 \times 10^6 \text{ Pa}$
3.  Apply the torque equation: $T = \frac{p \cdot V_d}{2\pi} = \frac{(21 \times 10^6 \text{ Pa}) \cdot (1.5 \times 10^{-4} \text{ m}^3/\text{rev})}{2\pi} \approx 50.18 \text{ Nm}$

Therefore, the output torque is approximately 50.18 Nm.

**Problem 2 (Speed Calculation):** A hydraulic motor has a displacement of $V_d = 100 \text{ cm}^3/\text{rev}$ and is supplied with an input flow rate of $Q_{in} = 30 \text{ L/min}$. Calculate the angular velocity.

*Solution:*
1.  Convert displacement to $m^3/rev$: $V_d = 100 \frac{\text{cm}^3}{\text{rev}} \times (\frac{1 \text{ m}}{100 \text{ cm}})^3 = 1 \times 10^{-4} \text{ m}^3/\text{rev}$
2.  Convert flow rate to $m^3/s$: $Q_{in} = 30 \frac{\text{L}}{\text{min}} \times \frac{1 \text{ m}^3}{1000 \text{ L}} \times \frac{1 \text{ min}}{60 \text{ s}} = 5 \times 10^{-4} \text{ m}^3/\text{s}$
3.  Apply the angular velocity equation: $\omega = \frac{Q_{in}}{V_d} = \frac{5 \times 10^{-4} \text{ m}^3/\text{s}}{1 \times 10^{-4} \text{ m}^3/\text{rev}} = 5 \text{ rev/s} = 5 \times 2\pi \text{ rad/s} \approx 31.42 \text{ rad/s}$
4. Convert to RPM: $\omega_{RPM} = \frac{31.42 rad/s}{2\pi} \cdot 60 \approx 300 RPM$

Therefore, the angular velocity is approximately 300 RPM.

### Hydraulic Cylinders (Linear Actuators)

The hydraulic cylinder, also known as a linear actuator, is a device used to convert fluid power into linear mechanical force and motion. This conversion is achieved by applying pressurized fluid to a piston within a cylindrical barrel. The pressure acts on the piston area, generating a force that causes the piston and its attached rod to move linearly.


> 📊 *Diagram: {"subject": "Schematic diagram of a single-acting hydraulic cylinder showing the fluid inlet port, piston, rod, and spring return mechanism. Arrows indicating the direction of fluid flow and piston movement.", "type": "schematic diagram"}*

