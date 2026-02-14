---
title: "Chapter 82"
author: "BookForge Draft"
---



From the chamber above the piston. For example, this chamber can be vented to the tank via a solenoid directional control valve. When this valve vents the pressure relief to the 20-psi pressure in the bottom chamber overcomes the light spring and unloads the pump to the tank.

### Pressure Relief Valves

Pressure relief valves are essential safety components in hydraulic systems. Their primary function is to limit the maximum pressure in the system, preventing damage to components such as pumps, cylinders, and hoses due to overpressure. Without a pressure relief valve, a hydraulic system could experience catastrophic failure if the pressure exceeds the design limits of its components. This overpressure can arise from various causes, including excessive load on an actuator, a malfunctioning control valve, or thermal expansion of the fluid. The pressure relief valve acts as a fail-safe mechanism, diverting excess flow back to the reservoir when the pressure reaches a predetermined level. This protects the system and ensures safe operation.

The "cracking pressure" is a critical parameter for a pressure relief valve. It represents the pressure at which the valve begins to open and allow fluid to flow through the relief port. This cracking pressure is determined by the balance of forces acting on the valve's poppet or spool.  The spring force, which resists the opening of the valve, is adjustable, allowing the cracking pressure to be set to a desired level. Once the inlet pressure exceeds the cracking pressure, the valve opens proportionally, allowing fluid to bypass the system and return to the reservoir, thereby limiting the pressure.

There are two main types of pressure relief valves: direct-acting and pilot-operated. A **direct-acting relief valve**is a simpler design where the system pressure acts directly on the poppet or spool, opposing the spring force.  A**pilot-operated relief valve**uses a smaller pilot valve to control the opening of a larger main valve. Pilot-operated valves offer improved performance, such as faster response times and more stable pressure control, especially in high-flow systems. They are commonly used in applications where precise pressure regulation and high flow capacity are required.

When a pressure relief valve opens, the high-pressure fluid is diverted back to the reservoir. This process involves a conversion of energy. The potential energy stored in the pressurized fluid is converted into kinetic energy as the fluid flows through the valve's orifice, and then dissipated as heat due to viscous friction.  This heat generation is an unavoidable consequence of the pressure relief process, and it contributes to the overall heat load of the hydraulic system. Efficient system design minimizes the frequency and duration of relief valve operation to reduce energy waste and heat generation, thereby improving the overall efficiency of the hydraulic system.

Consider the force balance on a direct-acting relief valve poppet.  The inlet pressure $p_{in}$ acting on the poppet area $A_{poppet}$ creates an upward force. This force is counteracted by the spring force $F_{spring}$ and the frictional force $F_{friction}$. The spring force is further defined as $F_{spring} = kx + F_{preload}$, where $k$ is the spring constant, $x$ is the displacement of the poppet from its initial position, and $F_{preload}$ is the initial preload on the spring.  The cracking pressure, $p_{cracking}$, is reached when the force due to inlet pressure equals the sum of the spring and friction forces. This can be described as:

$p_{in}A_{poppet} = kx + F_{preload} + F_{friction}$

Solving for $p_{in}$ (which is $p_{cracking}$ at the point of opening):

$p_{in} = \frac{kx + F_{preload} + F_{friction}}{A_{poppet}}$

If there is back pressure, $p_{back}$, acting on the outlet of the valve, it opposes the opening of the valve.  The equation then becomes:

$(p_{in}-p_{back})A_{poppet} = kx + F_{preload} + F_{friction}$

Solving for $p_{in}$:

$p_{in} = \frac{kx + F_{preload} + F_{friction}}{A_{poppet}} + p_{back}$

The flow rate $Q$ through the relief valve is governed by the orifice equation.  The flow rate is proportional to the discharge coefficient $C_d$, the orifice area $A_{orifice}$, and the square root of the pressure drop across the orifice ($p_{in} - p_{back}$) divided by the fluid density $\rho$:

$Q = C_d A_{orifice} \sqrt{\frac{2(p_{in} - p_{back})}{\rho}}$

The power $\mathcal{P}$ dissipated by the relief valve is the product of the pressure drop across the valve and the flow rate through it:

$\mathcal{P} = (p_{in} - p_{back}) Q$


> 📊 *Diagram: {"subject": "Sectional view of a direct-acting pressure relief valve, showing the poppet, spring, adjustment screw, inlet and outlet ports, and flow path when the valve is open.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic symbol for a direct-acting pressure relief valve.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Sectional view of a pilot-operated pressure relief valve, showing the pilot valve, main poppet, and flow paths.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic symbol for a pilot-operated pressure relief valve.", "type": "schematic"}*


### Pressure Relief Valve Example Problems:**Problem 1:** A direct-acting pressure relief valve has a poppet area $A_{poppet}$ of 100 mm$^2$, a spring constant $k$ of 100 N/mm, a preload force $F_{preload}$ of 300 N, and negligible friction. Calculate the required spring compression $x$ to achieve a cracking pressure of 15 MPa.  Assume no back pressure.

*Solution:*

1.  Convert units: $A_{poppet} = 100 \, \text{mm}^2 = 100 \times 10^{-6} \, \text{m}^2$, $k = 100 \, \text{N/mm} = 100 \times 10^3 \, \text{N/m}$, $F_{preload} = 300 \, \text{N}$, $p_{cracking} = 15 \, \text{MPa} = 15 \times 10^6 \, \text{Pa}$.

2.  Use the formula $p_{in}A_{poppet} = kx + F_{preload}$:
    $15 \times 10^6 \times 100 \times 10^{-6} = (100 \times 10^3)x + 300$

3.  Solve for x:
    $1500 = 100000x + 300$
    $x = \frac{1500 - 300}{100000} = \frac{1200}{100000} = 0.012 \, \text{m} = 12 \, \text{mm}$

Therefore, the required spring compression is 12 mm.

**Problem 2:** A hydraulic pump has a displacement $V_d$ of 50 cm$^3$/rev and runs at a speed $N$ of 1000 RPM. The relief valve has a discharge coefficient $C_d$ of 0.6 and must prevent overpressure. What should be the minimum orifice area $A_{orifice}$ of the relief valve, assuming the maximum allowable pressure is reached when the entire pump output flows through the valve, with an oil density $\rho=850 kg/m^3$? Assume negligible back pressure.

*Solution:*

1.  Calculate pump flow rate: $Q = V_d \times N = 50 \frac{\text{cm}^3}{\text{rev}} \times 1000 \frac{\text{rev}}{\text{min}} = 50000 \frac{\text{cm}^3}{\text{min}}$.  Convert to m$^3$/s:
    $Q = 50000 \frac{\text{cm}^3}{\text{min}} \times \frac{1 \, \text{m}^3}{10^6 \, \text{cm}^3} \times \frac{1 \, \text{min}}{60 \, \text{s}} = 8.33 \times 10^{-4} \, \text{m}^3/\text{s}$

2.  Assume the maximum allowable pressure $p_{in}$ is reached. We need a value. Let's assume $p_{in} = 25 MPa = 25 \times 10^6 Pa$.

3. Use the orifice equation:  $Q = C_d A_{orifice} \sqrt{\frac{2(p_{in} - p_{back})}{\rho}}$.  Since $p_{back}$ is negligible:
    $8.33 \times 10^{-4} = 0.6 \times A_{orifice} \sqrt{\frac{2(25 \times 10^6)}{850}}$

4.  Solve for $A_{orifice}$:
    $A_{orifice} = \frac{8.33 \times 10^{-4}}{0.6 \times \sqrt{\frac{50 \times 10^6}{850}}} = \frac{8.33 \times 10^{-4}}{0.6 \times 242.53} = 5.72 \times 10^{-6} \, \text{m}^2$

5. Convert to $mm^2$: $A_{orifice} = 5.72 \times 10^{-6} \, \text{m}^2 = 5.72 \, \text{mm}^2$

Therefore, the minimum orifice area of the relief valve should be 5.72 mm$^2$.

### Pressure-Reducing Valves

Pressure-reducing valves are crucial components in hydraulic systems where different parts of the circuit require different operating pressures. Unlike pressure relief valves, which limit maximum pressure, pressure-reducing valves actively maintain a lower pressure in a secondary circuit, regardless of the pressure in the primary circuit. This is particularly useful when certain actuators or components are designed for lower pressures than the main system pump can supply. For instance, a delicate hydraulic motor might need a lower pressure to prevent damage, while the rest of the system operates at a higher pressure for more demanding tasks.

The operation of a pressure-reducing valve relies on downstream pressure feedback. The valve senses the pressure in the downstream circuit and adjusts its opening to maintain the desired pressure level. The valve is normally open, allowing fluid to flow freely until the downstream pressure reaches the valve's setting. At that point, the valve begins to close, restricting the flow and preventing the downstream pressure from exceeding the set value. This continuous adjustment ensures a stable and controlled pressure in the secondary circuit.

A key feature of pressure-reducing valves is the inclusion of a drain line (also known as a vent line). This drain line serves to remove any leakage that occurs past the valve's spool. Even when the valve is closed, a small amount of fluid can seep past the spool due to manufacturing tolerances. Without a drain line, this leakage would gradually increase the downstream pressure, defeating the purpose of the valve. The drain line provides a path for this leakage to return to the reservoir, ensuring that the downstream pressure remains at the desired level. The drain line is particularly important for maintaining accurate pressure control and preventing pressure buildup when the downstream circuit is not actively consuming fluid.

The stability of pressure-reducing valves is a critical design consideration. Under certain conditions, the valve can oscillate, causing fluctuations in the downstream pressure. These oscillations can be caused by the interaction between the valve's dynamics, the compressibility of the hydraulic fluid, and the characteristics of the downstream circuit. Factors such as the valve's response time, the size of the downstream volume, and the stiffness of the hydraulic lines can all influence the stability of the valve. Proper valve selection and circuit design are essential to minimize the risk of oscillations and ensure stable pressure control.

Consider the force balance on the spool of a pressure-reducing valve. The inlet pressure, $p_{in}$, acts on an area $A_{in}$ of the spool, creating a force that tends to open the valve further. The spring force, $F_{spring}$, which is equal to $kx + F_{preload}$ opposes this opening force.  The outlet pressure, $p_{out}$, acts on an area $A_{out}$ of the spool, creating a force that also opposes the opening of the valve.  The frictional force $F_{friction}$ is present. The force balance equation is then:

$p_{in}A_{in} + F_{spring} = p_{out}A_{out} + F_{friction}$

Substituting $F_{spring} = kx + F_{preload}$:

$p_{in}A_{in} + kx + F_{preload} = p_{out}A_{out} + F_{friction}$

Solving for $p_{out}$:

$p_{out} = \frac{p_{in}A_{in} + kx + F_{preload} - F_{friction}}{A_{out}}$

In the common case where $A_{in} = A_{out} = A$:

$p_{out} = p_{in} + \frac{kx + F_{preload} - F_{friction}}{A}$

The flow rate $Q$ through the pressure-reducing valve is also governed by an orifice equation, similar to the pressure relief valve.  The flow rate depends on the pressure drop across the valve ($p_{in} - p_{out}$), the orifice area (which varies with the spool position), and the fluid properties:

$Q = C_d A_{orifice} \sqrt{\frac{2(p_{in} - p_{out})}{\rho}}$

The concept of "pressure regulation" refers to the ability of the valve to maintain a constant $p_{out}$ despite variations in $p_{in}$ and flow rate. An ideal pressure-reducing valve would maintain a perfectly constant $p_{out}$ regardless of changes in $p_{in}$ or flow demand. However, in practice, there will always be some variation in $p_{out}$ due to factors such as valve dynamics, fluid compressibility, and manufacturing tolerances. The pressure regulation performance of a valve is typically specified in terms of the maximum variation in $p_{out}$ over a given range of $p_{in}$ and flow rates.


> 📊 *Diagram: {"subject": "Sectional view of a pressure-reducing valve, showing the spool, spring, adjustment screw, inlet, outlet, drain line, and downstream pressure feedback path.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic symbol for a pressure-reducing valve.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Illustration showing a pressure-reducing valve used in a hydraulic circuit to supply a lower pressure to a hydraulic motor.", "type": "application diagram"}*


### Pressure Reducing Valve Example Problems:

**Problem 1:** A pressure-reducing valve has $A_{in} = A_{out} = 120 \, \text{mm}^2$, $k = 50 \, \text{N/mm}$, $F_{preload} = 150 \, \text{N}$, and negligible friction. The valve is designed to provide a downstream pressure of 8 MPa when the inlet pressure is 15 MPa. Calculate the required spring compression $x$.

*Solution:*

1. Convert units:  $A = 120 \, \text{mm}^2 = 120 \times 10^{-6} \, \text{m}^2$, $k = 50 \, \text{N/mm} = 50 \times 10^3 \, \text{N/m}$, $F_{preload} = 150 \, \text{N}$, $p_{in} = 15 \times 10^6 \, \text{Pa}$, $p_{out} = 8 \times 10^6 \, \text{Pa}$.

2. Use the formula $p_{out} = p_{in} + \frac{kx + F_{preload} - F_{friction}}{A}$.  Since friction is negligible: $p_{out} = p_{in} + \frac{kx + F_{preload}}{A}$

3. Rearrange and solve for x:
   $p_{out} - p_{in} = \frac{kx + F_{preload}}{A}$
   $(p_{out} - p_{in})A = kx + F_{preload}$
   $x = \frac{(p_{out} - p_{in})A - F_{preload}}{k} = \frac{(8 \times 10^6 - 15 \times 10^6)(120 \times 10^{-6}) - 150}{50 \times 10^3} = \frac{-840 - 150}{50000} = \frac{-990}{50000} = -0.0198 \, \text{m} = -19.8 \, \text{mm}$

Since x is negative, this means the spring is compressed *beyond* its preload position. This is possible and valid in the design of the valve. The spring is initially preloaded, and then further compressed to achieve the desired pressure reduction.

**Problem 2:** A pressure reducing valve has $A_{in}=100mm^2$ and $A_{out}=80mm^2$, $k=40 N/mm$ and $F_{preload}=200 N$. Given an input pressure of $p_{in} = 12 MPa$ what is the output pressure? Assume the spool is compressed by $x=10mm$ and that $F_{friction}=10N$.

*Solution:*

1. Convert Units:
    - $A_{in} = 100 mm^2 = 1.0 \times 10^{-4} m^2$
    - $A_{out} = 80 mm^2 = 8.0 \times 10^{-5} m^2$
    - $k = 40 N/mm = 40 \times 10^3 N/m$
    - $F_{preload} = 200 N$
    - $p_{in} = 12 MPa = 12 \times 10^6 Pa$
    - $x = 10 mm = 0.01 m$
    - $F_{friction} = 10 N$

2. Calculate the Spring Force:
    - $F_{spring} = kx + F_{preload} = (40 \times 10^3 N/m)(0.01 m) + 200 N = 400 N + 200 N = 600 N$

3.  Use the formula $p_{in}A_{in} + F_{spring} = p_{out}A_{out} + F_{friction}$ to solve for $p_{out}$:
    - $p_{out} = (p_{in}A_{in} + F_{spring} - F_{friction}) / A_{out}$
    - $p_{out} = ((12 \times 10^6 Pa)(1.0 \times 10^{-4} m^2) + 600 N - 10 N) / (8.0 \times 10^{-5} m^2)$
    - $p_{out} = (1200 N + 600 N - 10 N) / (8.0 \times 10^{-5} m^2)$
    - $p_{out} = 1790 N / (8.0 \times 10^{-5} m^2)$
    - $p_{out} = 22375000 Pa = 22.375 MPa$

Therefore, the output pressure is approximately 22.375 MPa.

### Unloading Valves

Unloading valves play a vital role in hydraulic systems where energy efficiency is a primary concern. These valves are designed to allow a hydraulic pump to operate at a minimal or zero pressure when full flow is not required. This drastically reduces the amount of power consumed by the pump, leading to significant energy savings, especially in systems with long periods of inactivity or low demand. Without an unloading valve, the pump would continue to deliver full flow at the system's maximum pressure setting (determined by the pressure relief valve), wasting energy and generating excessive heat.

The key to an unloading valve's operation is a remote pilot signal. This signal, typically a pressure signal from another part of the hydraulic circuit, controls the state of the unloading valve. When the pilot pressure is below a certain threshold, the unloading valve remains closed, and the pump delivers flow to the system at the required pressure. However, when the pilot pressure reaches the set point, the unloading valve opens, diverting the pump's output directly back to the reservoir at minimal pressure. This effectively "unloads" the pump, reducing its power consumption to a minimum.

The contrast between unloading valves and pressure relief valves is crucial for understanding energy efficiency. A pressure relief valve continuously dissipates energy by allowing the pump to deliver full flow at the relief pressure, converting the excess energy into heat. In contrast, an unloading valve *prevents* the pump from building up pressure in the first place when flow is not needed. This difference translates directly into lower energy consumption, reduced heat generation, and improved overall system efficiency. Unloading valves are particularly beneficial in applications where the pump spends a significant portion of its time operating at low or zero demand.

Unloading valves are frequently used in accumulator charging circuits. An accumulator is a device that stores hydraulic energy, allowing the system to meet peak demands without requiring a larger pump. When the accumulator is being charged, the unloading valve allows the pump to deliver flow to the accumulator until it reaches its desired pressure. Once the accumulator is fully charged, the pilot signal from the accumulator pressure switch opens the unloading valve, allowing the pump to idle at low pressure until the accumulator needs to be recharged. This cycle of charging and unloading ensures that the system has sufficient energy储备 available while minimizing the pump's energy consumption.

The force balance on an unloading valve spool dictates its operation.  Pilot pressure $p_{pilot}$ acts on the pilot area $A_{pilot}$, creating a force that tends to open the valve (allowing flow to the tank). The spring force $F_{spring} = kx + F_{preload}$ acts in the opposite direction, tending to keep the valve closed.  The inlet pressure, $p_{in}$ (i.e. pump pressure), acts on the inlet area $A_{in}$ to also keep the valve closed. At equilibrium we have:

$p_{pilot}A_{pilot} = p_{in}A_{in} + F_{spring}$

Solving for $p_{in}$:

$p_{in} = \frac{p_{pilot}A_{pilot} - F_{spring}}{A_{in}}$

The horsepower (HP) savings achieved by using an unloading valve compared to a pressure relief valve can be significant. Horsepower is defined as $HP = \frac{pQ}{constant}$. The constant depends on the units used for $p$ and $Q$. If $p$ is in psi and $Q$ is in gpm, the constant is 1714. If $p$ is in Pascals and $Q$ is in $m^3/s$, then $HP = pQ$ in Watts. The valve selection greatly changes the energy wasted. With a pressure relief valve, the pump is constantly delivering flow at the relief pressure, even when no work is being done. With an unloading valve, the pump unloads and operates at near zero pressure when no work is required, drastically reducing the horsepower consumption.


> 📊 *Diagram: {"subject": "Sectional view of an unloading valve, showing the spool, spring, pilot port, inlet, and outlet.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic symbol for an unloading valve.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Hydraulic circuit using an unloading valve to control pump output to an accumulator.", "type": "schematic"}*


### Unloading Valve Example Problems:

**Problem 1:** An unloading valve is used in a hydraulic system with a desired system pressure of 15 MPa. The pilot area of the valve is 300 mm$^2$, and the inlet area $A_{in}=200 mm^2$. If the spring exerts negligible force, what pilot pressure is required to unload the pump?

*Solution:*

1.  Convert units: $p_{in} = 15 \, \text{MPa} = 15 \times 10^6 \, \text{Pa}$, $A_{pilot} = 300 \, \text{mm}^2 = 300 \times 10^{-6} \, \text{m}^2$, $A_{in} = 200 \, \text{mm}^2 = 200 \times 10^{-6} \, \text{m}^2$.

2. Use the formula $p_{pilot}A_{pilot} = p_{in}A_{in} + F_{spring}$, where $F_{spring} = 0$:

$p_{pilot}A_{pilot} = p_{in}A_{in}$

3. Solve for $p_{pilot}$:

$p_{pilot} = \frac{p_{in}A_{in}}{A_{pilot}} = \frac{(15 \times 10^6)(200 \times 10^{-6})}{(300 \times 10^{-6})} = \frac{3000}{300 \times 10^{-6}} \times 10^{-6} = 10 \times 10^6 Pa = 10 \, \text{MPa}$

Therefore, a pilot pressure of 10 MPa is required to unload the pump.

**Problem 2:** A pump delivers 40 L/min at 18 MPa. Calculate the horsepower required when using a pressure relief valve compared to using an unloading valve that unloads the pump when the pressure reaches 16 MPa and flow demand drops to zero. Use units of Pascals and $m^3/s$.

*Solution:*

1. Convert Units:
    - $Q = 40 L/min = 40 \times (1/1000) m^3/L \times (1/60) min/sec = 6.67 \times 10^{-4} m^3/s$
    - $p_{relief} = 18 MPa = 18 \times 10^6 Pa$
    - $p_{unloading} = 0 Pa$ because the pump is unloaded to tank.

2. Horsepower with Pressure Relief Valve:
    - $HP = pQ = (18 \times 10^6 Pa) \times (6.67 \times 10^{-4} m^3/s) = 12006 Watts = 12.0 kW$

3. Horsepower with Unloading Valve (when unloaded):
    - $HP = pQ = (0 Pa) \times (6.67 \times 10^{-4} m^3/s) = 0 Watts$

Therefore, using a pressure relief valve requires approximately 12 kW, while the unloading valve requires 0 kW when unloaded. The horsepower savings is 12 kW.

### Sequence Valves

Sequence valves are essential components in hydraulic systems requiring operations to occur in a specific order. They ensure that one actuator completes its function before another begins, providing controlled and coordinated movements. This sequential operation is crucial in applications where safety, efficiency, or process requirements dictate a precise order of events. Without sequence valves, multiple actuators might attempt to operate simultaneously, leading to unpredictable behavior, potential damage to equipment, or compromised product quality.

The operation of a sequence valve hinges on its ability to sense the pressure at one location in the hydraulic circuit and then, based on that pressure, allow flow to another part of the circuit. The valve monitors the pressure at its inlet port (typically connected to the first actuator in the sequence). Once the pressure at this port reaches a predetermined setting (determined by an adjustable spring), the valve opens, allowing fluid to flow through its outlet port to the next actuator in the sequence. Until the set pressure is reached, the valve remains closed, preventing flow to the subsequent actuator.

Sequence valves find wide application in various industrial settings. One common example is in clamping before machining operations. A sequence valve can be used to ensure that a workpiece is securely clamped in place before the machining process begins. The clamping cylinder is connected to the inlet port of the sequence valve, while the machining cylinder is connected to the outlet port. The sequence valve is set to a pressure that corresponds to the force required to fully clamp the workpiece. Once the clamping cylinder has exerted sufficient force to secure the workpiece, the pressure at the sequence valve's inlet port reaches the set point, causing the valve to open and allowing the machining cylinder to begin its operation.

Another frequent application of sequence valves is in systems involving multiple cylinders that need to extend in a specific order. For instance, in a multi-stage conveyor system, it might be necessary for one section of the conveyor to extend fully before the next section starts moving. A sequence valve can be used to achieve this precise timing. The cylinder controlling the first conveyor section is connected to the sequence valve's inlet, while the cylinder controlling the second conveyor section is connected to the outlet. The sequence valve is set to a pressure that corresponds to the force required to fully extend the first conveyor section. Once the first section is fully extended, the pressure at the valve's inlet reaches the set point, allowing the valve to open and enabling the second conveyor section to extend.

The force balance on the sequence valve poppet determines when the valve opens. The pressure at port A, $p_A$, acts on the poppet area, $A_{poppet}$, generating a force that tends to open the valve. This force is opposed by the spring force, $F_{spring} = kx + F_{preload}$, and the frictional force, $F_{friction}$. At equilibrium, we have:

$p_{A}A_{poppet} = F_{spring} + F_{friction}$

Substituting $F_{spring} = kx + F_{preload}$:

$p_{A}A_{poppet} = kx + F_{preload} + F_{friction}$

Solving for $p_A$ (the pressure at port A required to open the valve):

$p_{A} = \frac{kx + F_{preload} + F_{friction}}{A_{poppet}}$

The pressure at port B is directly related to the load on the actuator connected to that port. The pressure required at B will dictate what occurs downstream of the sequence valve.


> 📊 *Diagram: {"subject": "Sectional view of a sequence valve, showing the poppet, spring, and flow paths.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic symbol for a sequence valve.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Hydraulic circuit using a sequence valve to control the order of operation of two cylinders.", "type": "schematic"}*


### Sequence Valve Example Problems:

**Problem 1:** A sequence valve is used to control two cylinders. Cylinder 1 requires a force of 12 kN and has a bore of 60mm. Cylinder 2 requires 20 kN with bore of 80 mm. If friction is negligible, what should the setting of the sequence valve be to ensure Cylinder 1 extends fully before Cylinder 2 starts to extend?

*Solution:*

1.  Calculate the pressure required for Cylinder 1 to extend:

    *Area* of Cylinder 1: $A_1 = \pi r^2 = \pi (\frac{D}{2})^2 = \pi (\frac{0.06 m}{2})^2 = \pi (0.03 m)^2 = 2.827 \times 10^{-3} m^2$

    *Pressure* required to generate a force of 12 kN:  $p_1 = \frac{F_1}{A_1} = \frac{12000 N}{2.827 \times 10^{-3} m^2} = 4.245 \times 10^6 Pa = 4.245 MPa$

Therefore, the sequence valve should be set to 4.245 MPa.

**Problem 2:** A stamping press uses a sequence valve to control the clamping and stamping operations. The clamping cylinder has to clamp the workpiece before the stamping operation commences. The clamping cylinder has a bore of 130 mm.

If the sequence valve opens at 16 MPa and the pump has an outflow of 60 liters per minute, how long will it take to build up to that pressure and clamp the workpiece?

*Solution*
1. Find cylinder area:
$A= \pi * r^2 = \pi* (\frac{d}{2})^2 = \pi (\frac{0.13}{2})^2 = 0.0133 m^2$
2. Find Volumetric Flow rate:
$Q= \frac{60 Liters}{Min} = \frac{0.06 m^3}{60 s} = 0.001 \frac{m^3}{s}$
3. Set Volume
$V = A * d = 0.0133 * 0.3 = 0.004 m^3$. Here we have to *assume* a stroke length of 30 cm or 0.3 meters.
4. Find the time:
$\frac{0.004 m^3}{0.001 \frac{m^3}{s}} = 4 seconds$

Therefore, at a constant flow, it takes 4 seconds to clamp the workpiece before the sequence valve opens at 16 MPa and commences the stamping operation.