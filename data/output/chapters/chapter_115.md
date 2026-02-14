---
title: "Chapter 115"
author: "BookForge Draft"
---

### Valve Circuit Analysis

### Introduction

Hydraulic circuit analysis involves understanding how individual components, primarily valves, interact to control fluid power. This involves applying principles of fluid mechanics, statics, and control systems to predict and optimize circuit behavior. Key concepts include pressure intensification, flow dividers, pressure compensation, and understanding the pressure drop versus flow rate characteristics of valves. These principles guide the design and troubleshooting of hydraulic systems, ensuring they operate efficiently and safely. Correct design prevents issues such as actuator stalling, overheating, and cavitation.

Pascal's Law forms the foundation for understanding force transmission in hydraulic systems. It states that pressure applied to a confined fluid is transmitted equally in all directions throughout the fluid. Mathematically, this is expressed as:

$p = \frac{F}{A}$

where *p* is pressure, *F* is force, and *A* is area.

This principle allows for force multiplication: a small force applied over a small area can generate a large force over a larger area. This is the fundamental principle behind hydraulic jacks and other force-amplifying devices. Pascal's Law assumes an incompressible fluid and neglects any pressure losses due to friction or elevation changes.


> 📊 *Diagram: {"subject": "Simple diagram illustrating Pascal's Law with a confined fluid and two pistons of different sizes", "type": "schematic"}*


Furthermore, hydraulic circuits can be designed to mimic basic logic gates, such as AND, OR, and NOT gates, using combinations of valves and pressure switches. These logic gates enable automated control sequences based on pressure signals within the hydraulic system.

### Pressure Intensification

Pressure intensification occurs when a hydraulic cylinder with unequal areas is used to increase the pressure. This is based on Pascal's Law. Considering two cylinders connected in series, where Cylinder 1 has area $A_1$ and pressure $p_1$, and Cylinder 2 has area $A_2$ and pressure $p_2$, the force exerted by each cylinder must be equal (neglecting friction):

$F_1 = F_2$

$p_1 A_1 = p_2 A_2$

Therefore, the output pressure $p_2$ is:

$p_2 = p_1 \frac{A_1}{A_2}$

If $A_1 > A_2$, then $p_2 > p_1$, resulting in pressure intensification.


> 📊 *Diagram: {"subject": "Schematic of a hydraulic intensifier circuit with labeled input and output cylinders, including pressure gauges.", "type": "schematic"}*


**Problem 1 (Pressure Intensification):** A hydraulic circuit uses an intensifier. The input cylinder has a bore of 65 mm, and the output cylinder has a bore of 20 mm. If the input pressure is 5 MPa, what is the output pressure, assuming ideal conditions and again accounting for a frictional loss of 10%?

*Solution:*

1.  *Calculate the areas:*

    - Input area, $A_1 = \pi (D_1/2)^2 = \pi (0.065/2)^2 = 0.00332 m^2$
    - Output area, $A_2 = \pi (D_2/2)^2 = \pi (0.020/2)^2 = 0.000314 m^2$
2.  *Calculate the ideal output pressure:*

    - $p_2 = p_1 \frac{A_1}{A_2} = 5 MPa \times \frac{0.00332}{0.000314} = 52.87 MPa$
3.  *Account for frictional loss:*

    - Frictional loss = $10\% \times 52.87 MPa = 5.287 MPa$
    - Actual output pressure = $52.87 MPa - 5.287 MPa = 47.583 MPa$

Therefore, the ideal output pressure is approximately 52.87 MPa, and accounting for a 10% frictional loss, the output pressure is approximately 47.58 MPa.

**Problem 2 (Pressure Intensification):** A hydraulic circuit uses an intensifier. The input cylinder has a bore of 50 mm, and the output cylinder has a bore of 30 mm. If the input pressure is 3 MPa, what is the output pressure, assuming ideal conditions and again accounting for a frictional loss of 15%?

*Solution:*

1. *Calculate the areas:*

    - Input area, $A_1 = \pi (D_1/2)^2 = \pi (0.050/2)^2 = 0.00196 m^2$
    - Output area, $A_2 = \pi (D_2/2)^2 = \pi (0.030/2)^2 = 0.000707 m^2$
2. *Calculate the ideal output pressure:*

    - $p_2 = p_1 \frac{A_1}{A_2} = 3 MPa \times \frac{0.00196}{0.000707} = 8.317 MPa$
3. *Account for frictional loss:*

    - Frictional loss = $15\% \times 8.317 MPa = 1.248 MPa$
    - Actual output pressure = $8.317 MPa - 1.248 MPa = 7.069 MPa$

Therefore, the ideal output pressure is approximately 8.317 MPa, and accounting for a 15% frictional loss, the output pressure is approximately 7.069 MPa.

### Flow Rate Through an Orifice

The flow rate through an orifice is governed by the orifice equation, which relates the flow rate to the pressure drop across the orifice, the orifice area, and the fluid properties. The equation is derived from Bernoulli's principle and incorporates a discharge coefficient to account for energy losses due to friction and flow contraction:

$Q = C_d A_o \sqrt{\frac{2\Delta p}{\rho}}$

where:

- $Q$ is the flow rate
- $C_d$ is the discharge coefficient (typically between 0.6 and 0.8)
- $A_o$ is the orifice area
- $\Delta p$ is the pressure drop across the orifice
- $\rho$ is the fluid density


> 📊 *Diagram: {"subject": "Detailed cross-section of an orifice in a hydraulic valve, showing pressure drop and flow direction.", "type": "technical illustration"}*


**Problem 3 (Orifice Flow):** Oil with a specific gravity of 0.85 flows through an orifice with a diameter of 3 mm in a hydraulic valve. The pressure drop across the orifice is 3 MPa. Calculate the flow rate, assuming a discharge coefficient of 0.7.

*Solution:*

1.  *Calculate the fluid density:*

    - $\rho = SG \times \rho_{water} = 0.85 \times 1000 kg/m^3 = 850 kg/m^3$
2.  *Calculate the orifice area:*

    - $A_o = \pi (D/2)^2 = \pi (0.003/2)^2 = 7.068 \times 10^{-6} m^2$
3.  *Calculate the flow rate:*

    - $Q = C_d A_o \sqrt{\frac{2\Delta p}{\rho}} = 0.7 \times 7.068 \times 10^{-6} \sqrt{\frac{2 \times 3 \times 10^6}{850}} = 0.7 \times 7.068 \times 10^{-6} \times 84.08 m/s= 4.17 \times 10^{-4} m^3/s = 25.02 L/min$

Therefore, the flow rate through the orifice is approximately 25.02 L/min.

**Problem 4 (Orifice Flow):** Oil with a specific gravity of 0.9 flows through an orifice with a diameter of 4 mm in a hydraulic valve. The pressure drop across the orifice is 4 MPa. Calculate the flow rate, assuming a discharge coefficient of 0.6.

*Solution:*

1.  *Calculate the fluid density:*

    - $\rho = SG \times \rho_{water} = 0.9 \times 1000 kg/m^3 = 900 kg/m^3$
2.  *Calculate the orifice area:*

    - $A_o = \pi (D/2)^2 = \pi (0.004/2)^2 = 1.2566 \times 10^{-5} m^2$
3.  *Calculate the flow rate:*

    - $Q = C_d A_o \sqrt{\frac{2\Delta p}{\rho}} = 0.6 \times 1.2566 \times 10^{-5} \sqrt{\frac{2 \times 4 \times 10^6}{900}} = 0.6 \times 1.2566 \times 10^{-5} \times 94.28 m/s = 7.12 \times 10^{-4} m^3/s= 42.72 L/min$

Therefore, the flow rate through the orifice is approximately 42.72 L/min.

### Valve Circuit Analysis

The provided text describes a hydraulic circuit with a directional control valve (DCV-1) controlled by a push-button valve (2) and an overload valve (3). The function of each component and the behavior of the circuit is explained below.

- **DCV-1 (Directional Control Valve):**This valve directs the flow of hydraulic fluid to control the movement of an actuator, typically a cylinder. It has multiple ports and spool positions to allow fluid to flow in different directions.
-**Push-Button Valve-2:**This valve acts as a manual input device. When pressed, it allows pilot pressure to shift the DCV-1 spool.
-**Overload Valve-3:**This valve is a safety device that protects the hydraulic system from excessive pressure. It is designed to open and relieve pressure when the system reaches a predetermined limit.
-**Valve-4:**Senses the pressure at the cylinder, and actuates valve -3.

### Operation

1.**Normal Operation:**When the overload valve (3) is in its spring offset mode, it drains the pilot line of the DCV-1. This means that even if the push-button valve (2) is pressed, the DCV-1 will not shift because the pilot pressure is being bled off.
2.**Overload Condition:**If the cylinder experiences excessive resistance, valve-4 actuates the overload valve (3). This action drains the pilot line of the DCV-1, causing it to return to its spring offset mode. This prevents further pressure buildup and protects the system from damage.
3.**Manual Override:** The push-button valve (2) will only function if the overload valve (3) is manually shifted into a blocked configuration. In this configuration, the pilot line to the DCV-1 is no longer drained when the push-button is pressed, allowing the DCV-1 to shift and control the actuator.

### Pilot Pressure

The pilot pressure required to shift the DCV spool can be calculated using the following formula:

$F = p_{pilot} * A_{spool}$

Where:

- *F* is the force required to shift the spool
- $p_{pilot}$ is the pilot pressure
- $A_{spool}$ is the area of the spool on which the pilot pressure acts


> 📊 *Diagram: {"subject": "Detailed hydraulic circuit diagram of the DCV-1, Push button valve-2, and Overload Valve -3 system, including all pressure lines, spring offsets, and pilot connections. Include numbering for each component.", "type": "schematic"}*


**Problem 1 (Pilot Pressure):** A DCV requires a pilot pressure of 4 MPa to shift. The pilot valve has a bore of 8 mm. What force must be applied to the pilot valve's actuator to shift the DCV?

*Solution:*

1.  *Calculate the area:*

    - $A_{spool} = \pi (D/2)^2 = \pi (0.008/2)^2 = 5.0265 \times 10^{-5} m^2$
2.  *Calculate the force:*

    - $F = p_{pilot} * A_{spool} = 4 \times 10^6 Pa \times 5.0265 \times 10^{-5} m^2 = 201.06 N$

Therefore, a force of 201.06 N must be applied to the pilot valve's actuator to shift the DCV.

**Problem 2 (Pilot Pressure):** A DCV requires a pilot pressure of 3 MPa to shift. The pilot valve has a bore of 10 mm. What force must be applied to the pilot valve's actuator to shift the DCV?

*Solution:*

1.  *Calculate the area:*

    - $A_{spool} = \pi (D/2)^2 = \pi (0.010/2)^2 = 7.854 \times 10^{-5} m^2$
2.  *Calculate the force:*

    - $F = p_{pilot} * A_{spool} = 3 \times 10^6 Pa \times 7.854 \times 10^{-5} m^2 = 235.62 N$

Therefore, a force of 235.62 N must be applied to the pilot valve's actuator to shift the DCV.

### Overload Valve

The pressure at which the overload valve actuates is determined by the spring force and the valve area:

$p_{overload} = \frac{F_{spring}}{A_{valve}}$

Where:

- $p_{overload}$ is the pressure at which the overload valve opens
- $F_{spring}$ is the spring force
- $A_{valve}$ is the area of the valve on which the pressure acts


> 📊 *Diagram: {"subject": "Cutaway view of the overload valve showing the spring, poppet, and pressure inlet/outlet.", "type": "technical illustration"}*


**Problem 3 (Overload Valve Setting):** An overload valve has a spring with a stiffness of 750 N/m. The valve's bore is 12 mm. If the spring is compressed 10 mm at the set pressure, at what pressure will the overload valve open?

*Solution:*

1.  *Calculate the spring force:*

    - $F_{spring} = k \times x = 750 N/m \times 0.010 m = 7.5 N$
2.  *Calculate the valve area:*

    - $A_{valve} = \pi (D/2)^2 = \pi (0.012/2)^2 = 1.131 \times 10^{-4} m^2$
3.  *Calculate the overload pressure:*

    - $p_{overload} = \frac{F_{spring}}{A_{valve}} = \frac{7.5 N}{1.131 \times 10^{-4} m^2} = 66300 Pa = 0.0663 MPa$

Therefore, the overload valve will open at a pressure of 0.0663 MPa.

### Hydrostatic Transmission

A hydrostatic transmission (HST) is a power transmission system that uses hydraulic fluid to transfer power from an engine or motor to a driven component. It consists of a hydraulic pump, a hydraulic motor, and connecting lines. HSTs offer several advantages over mechanical transmissions, including variable speed control, smooth acceleration, and high torque at low speeds. They are commonly used in applications such as construction equipment, agricultural machinery, and material handling systems.

### Open Circuit Drives

In an open-circuit hydrostatic transmission, the hydraulic pump draws fluid from a reservoir, and the pump output is directed to the hydraulic motor. The discharge from the motor returns to the reservoir. This type of system is simpler and less expensive than closed-circuit systems. However, it is generally less efficient due to pressure losses and aeration of the hydraulic fluid.


> 📊 *Diagram: {"subject": "Schematic of an open-circuit hydrostatic transmission, labeling the pump, reservoir, motor, and all connecting lines.", "type": "schematic"}*


### Closed Circuit Drives

In a closed-circuit hydrostatic transmission, the exhaust oil from the motor is returned directly to the pump inlet, forming a closed loop. This design improves efficiency by minimizing fluid aeration and pressure losses. Closed-circuit systems typically include a charge pump to maintain a positive pressure in the loop and compensate for leakage.

### Speed and Torque Ratio

The speed ratio of a hydrostatic transmission is determined by the ratio of the pump displacement to the motor displacement:

$\frac{N_{motor}}{N_{pump}} = \frac{D_{pump}}{D_{motor}}$

Where:

- $N_{motor}$ is the motor speed
- $N_{pump}$ is the pump speed
- $D_{pump}$ is the pump displacement
- $D_{motor}$ is the motor displacement

The torque ratio is determined by the ratio of the motor displacement to the pump displacement and the mechanical efficiency:

$\frac{T_{motor}}{T_{pump}} = \frac{D_{motor}}{D_{pump}} \times \eta_{mech}$

Where:

- $T_{motor}$ is the motor torque
- $T_{pump}$ is the pump torque
- $\eta_{mech}$ is the mechanical efficiency

The overall efficiency is the product of the volumetric and mechanical efficiencies:

$\eta_{overall} = \eta_{vol} \times \eta_{mech}$

### Closed Circuit One-Direction Hydrostatic Transmission

This is a type of closed-circuit hydrostatic transmission that allows motor rotation in only one direction. The motor speed is varied by changing the pump displacement. The torque capacity of the motor is adjusted by the pressure setting of the relief valve.


> 📊 *Diagram: {"subject": "Simplified schematic of a closed-circuit one-direction hydrostatic transmission, highlighting the variable displacement pump and relief valve.", "type": "schematic"}*


### Closed Circuit Reversible Direction Hydrostatic Transmission

To achieve reversible operation in a closed-circuit hydrostatic transmission, an over-center pump is typically used. An over-center pump can displace fluid in either direction, allowing the motor to rotate in both forward and reverse directions. Flushing valves and check valves are used to maintain fluid cleanliness and prevent cavitation.


> 📊 *Diagram: {"subject": "Schematic of a closed-circuit reversible hydrostatic transmission, showing the over-center pump, motor, flushing valve, and check valves. Use different line styles for high-pressure and low-pressure lines.", "type": "schematic"}*


### Mechanical-Hydraulic Servo Valves

A mechanical-hydraulic servo valve uses a mechanical input force to shift the spool of the servo valve, controlling the flow of hydraulic fluid to an actuator. A feedback link connects the actuator rod to the sliding sleeve of the valve, providing closed-loop position control. This ensures that a given input motion produces a specific and controlled amount of output motion. This type of valve is commonly used in hydraulic power steering systems of automobiles.

The relationship between input displacement and cylinder displacement can be expressed as:

$x_{cylinder} = K x_{input}$

Where:

- $x_{cylinder}$ is the cylinder displacement
- $x_{input}$ is the input displacement
- $K$ is the gain factor, determined by the lever arm lengths in the feedback mechanism.


> 📊 *Diagram: {"subject": "Detailed cross-sectional diagram of a mechanical-hydraulic servo valve, labeling the input lever, spool, feedback link, and hydraulic cylinder. Show the direction of oil flow for different input positions.", "type": "technical illustration"}*


### Electro-Hydraulic Servo Valves

An electro-hydraulic servo valve operates by converting an electrical signal into a hydraulic output. The electrical signal is sent to a torque motor, which positions the spool of a directional control valve. The movement of the armature in the torque motor is proportional to the direct current applied to its windings. The signal to the torque motor comes from an electrical device, such as a potentiometer, and is amplified to drive the motor. The hydraulic flow output of the servo valve powers an actuator, which in turn drives the load.

The velocity or position of the load is fed back in electrical form to the input of the servo valve by a feedback device. The feedback signal is compared to the command input signal, and the difference between the two signals is sent to the torque motor as an error signal. This error signal causes the torque motor to adjust the valve spool position until the desired velocity or position is achieved. At this point, the error signal becomes zero.

Electro-hydraulic systems use low-power electrical signals (on the order of 1 W) to control the movements of large hydraulic pistons (delivering 7640 W or more). Typical applications include aircraft controls and numerical control machines.

The relationship between input current and spool displacement can be expressed as:

$x_{spool} = K_t I$

Where:

- $x_{spool}$ is the spool displacement
- $K_t$ is the torque constant of the torque motor
- $I$ is the input current to the torque motor


> 📊 *Diagram: {"subject": "Detailed cross-sectional diagram of an electro-hydraulic servo valve, labeling the torque motor, armature, spool valve, feedback mechanism (if applicable), and hydraulic ports. Show oil flow paths.", "type": "technical illustration"}*


### Single-Stage Servo Valves

In a single-stage servo valve, the armature of the torque motor is connected directly to one end of the valve spool. With equal currents flowing through the two coils of the torque motor, the armature remains centered. Increasing the current in one coil and reducing it in the other causes the armature to move proportionally to the change in current. Thus, the spool also shifts by a distance proportional to the change in current.

### Two-Stage Servo Valves

Two-stage servo valves are more commonly used than single-stage valves because they can handle large flow rates at high pressure with high sensitivity to control changes. These valves have sliding spools in both the pilot and main stages. The pilot stage controls the position of the main stage spool, which in turn controls the flow of hydraulic fluid to the actuator. This two-stage design allows for higher flow capacity and improved performance compared to single-stage valves.


> 📊 *Diagram: {"subject": "Detailed cross-sectional diagram of a two-stage servo valve with a flapper-nozzle pilot stage, labeling all components and showing oil flow paths. Use different colors to distinguish between pilot stage and main stage flows.", "type": "technical illustration"}*

