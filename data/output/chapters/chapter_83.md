---
title: "Chapter 83"
author: "BookForge Draft"
---

Okay, I understand. I will expand the text to at least 5x the original length, adding more derivations, mirror problems with randomized values, and [NEW_DIAGRAM] tags as specified in the expansion plan. I will also ensure that all the issues identified in the CRITIC FEEDBACK are addressed.


To the pressure at point A, the control piston seats and prevents further pilot flow loss. The main poppet then fully opens, which allows the pressure at both points A and B to rise to higher values simultaneously. Flow may proceed in either direction at this point. The spring cavity of the control cone drains externally from port Y, typically to the hydraulic fluid reservoir (tank). Importantly, this sequence valve can be remotely controlled through the vent port labeled X.

Sequence valves are essential components in hydraulic circuits where operations must occur in a specific order. Consider an automated manufacturing process where a workpiece needs to be clamped securely before a machining operation can begin. A sequence valve ensures the clamping cylinder extends fully and applies sufficient pressure *before* the machining cylinder is activated. Another application is in multi-cylinder systems where one cylinder must extend completely before another starts moving, preventing interference or ensuring stability of a structure. The applications are vast, improving both safety and efficiency in automated systems.

At the heart of sequence valve operation lies a balance of forces. Pilot pressure acting on a control piston must overcome the opposing force of a spring. The valve is designed around these first principles, ensuring reliable and repeatable sequencing.

The relationship between pressure, force, and area is fundamental: $F = p \cdot A$, where *F* represents force, *p* pressure, and *A* area. In the context of a sequence valve, the pilot pressure ($p_{pilot}$) acting on the pilot area ($A_{pilot}$) generates a force ($F_{pilot}$) that opposes the spring force ($F_{spring}$). The spring force, in turn, is determined by the spring constant (*k*) and the spring compression (*x*): $F_{spring} = kx$.

For the valve to actuate, the pilot force must exceed the spring force:

$F_{pilot} > F_{spring}$

Substituting the expressions for each force:

$p_{pilot} A_{pilot} > kx$

The set pressure ($p_{set}$) of the sequence valve, which is the minimum pilot pressure required to open the valve, can be expressed as:

$p_{set} = \frac{kx}{A_{pilot}}$

This equation highlights the key design parameters of a sequence valve: the spring constant, the pilot area, and the desired actuation pressure.

The flow rate (*Q*) through the poppet valve, once it opens, can be approximated using the orifice equation. This equation treats the opening as a restriction in the flow path:

$Q = C_d A_o \sqrt{\frac{2(p_A - p_B)}{\rho}}$

Where:

- $C_d$ is the discharge coefficient (typically between 0.6 and 0.9, depending on the orifice geometry)
- $A_o$ is the area of the orifice (the opening of the poppet valve)
- $p_A$ is the upstream pressure (pressure at port A)
- $p_B$ is the downstream pressure (pressure at port B)
- $\rho$ is the fluid density.


> 📊 *Diagram: {"subject": "Detailed cross-sectional view of a sequence valve, showing the control piston, poppet valve, spring, pilot pressure port (X), spring cavity drain port (Y), primary port (A), and secondary port (B). Show pressure annotations at different points in the valve.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Hydraulic circuit using a sequence valve to control two cylinders in a specific order (e.g., Cylinder 1 extends fully before Cylinder 2 starts extending).", "type": "schematic"}*


**Mirror Problems:**

Problem 1: Determine the required pilot pressure to actuate a sequence valve.

Valve area $A_{pilot} = 125 \text{ mm}^2 = 125 \times 10^{-6} \text{ m}^2$
Spring constant $k = 350 \text{ N/m}$
Spring compression $x = 6 \text{ mm} = 6 \times 10^{-3} \text{ m}$

$p_{set} = \frac{kx}{A_{pilot}} = \frac{350 \text{ N/m} \cdot 6 \times 10^{-3} \text{ m}}{125 \times 10^{-6} \text{ m}^2} = 16800 \text{ Pa} = 0.0168 \text{ MPa}$

Therefore, the required pilot pressure to actuate the sequence valve is 0.0168 MPa.

Problem 2: Calculate the flow rate through a poppet valve in a sequence valve.

Pressure drop $p_A - p_B = 5 \text{ MPa} = 5 \times 10^6 \text{ Pa}$
Orifice area $A_o = 30 \text{ mm}^2 = 30 \times 10^{-6} \text{ m}^2$
Discharge coefficient $C_d = 0.75$
Fluid density $\rho = 850 \text{ kg/m}^3$

$Q = C_d A_o \sqrt{\frac{2(p_A - p_B)}{\rho}} = 0.75 \cdot 30 \times 10^{-6} \text{ m}^2 \cdot \sqrt{\frac{2 \cdot 5 \times 10^6 \text{ Pa}}{850 \text{ kg/m}^3}} \approx 7.7 \times 10^{-4} \text{ m}^3/\text{s} = 0.77 \text{ L/s} = 46.2 \text{ LPM}$

The flow rate through the poppet valve is approximately 46.2 liters per minute.

Problem 3: Design a sequence valve to operate at a specific pressure with a known pilot area.

Target pressure $p_{set} = 12 \text{ MPa} = 12 \times 10^6 \text{ Pa}$
Pilot area $A_{pilot} = 200 \text{ mm}^2 = 200 \times 10^{-6} \text{ m}^2$

Let's choose a spring with a spring constant of $k = 400 \text{ N/m}$.

$p_{set} = \frac{kx}{A_{pilot}}$, therefore, $x = \frac{p_{set} A_{pilot}}{k}$

$x = \frac{12 \times 10^6 \text{ Pa} \cdot 200 \times 10^{-6} \text{ m}^2}{400 \text{ N/m}} = 6 \text{ m}$

This spring compression is unrealistically large. Let's pick a much stiffer spring of $k = 400,000 \text{ N/m}$
$x = \frac{12 \times 10^6 \text{ Pa} \cdot 200 \times 10^{-6} \text{ m}^2}{400,000 \text{ N/m}} = 0.006 \text{ m} = 6 \text{ mm}$

Therefore, a spring with a spring constant of 400,000 N/m compressed by 6 mm will provide the desired set pressure.

Counterbalance valves serve a crucial function: maintaining control of a vertical cylinder, preventing it from uncontrolled descent due to gravity. Without a counterbalance valve, a heavy load supported by a vertically mounted cylinder could drop rapidly and unsafely when the directional control valve is centered, or if a hose were to rupture. This is especially important in applications such as hydraulic lifts, construction equipment, and industrial presses.

The primary port of this valve connects to the bottom (rod end) of the cylinder, while the secondary port connects to the directional control valve (DCV). The pressure setting of the counterbalance valve is deliberately set somewhat higher than the pressure necessary to merely prevent the cylinder load from falling. This margin ensures stable and controlled operation.

As shown conceptually, when pump flow is directed (via the DCV) to the top (cap end) of the cylinder, the cylinder piston is pushed downward. This downward movement increases the pressure at the primary port of the counterbalance valve, which is connected to the rod end. This increased pressure acts against the valve spool, eventually overcoming the spring force and raising the spool. As the spool lifts, it opens a flow path for the hydraulic fluid to discharge through the secondary port, back to the DCV, and then to the tank. When raising the cylinder, an integral check valve opens, allowing free flow for retracting the cylinder without having to overcome the counterbalance valve setting. This ensures efficient and responsive upward motion.

The principle at play is the balancing of forces. The weight of the load creates a force that is counteracted by the hydraulic pressure acting on the cylinder's piston area. This pressure is what the counterbalance valve regulates. An "overrunning load" is any load that, if not controlled, would cause an actuator to move faster than intended by the applied flow rate.

The force balance on the cylinder piston dictates that the load force ($F_{load}$) is equal to the cylinder pressure ($p_{cylinder}$) multiplied by the cylinder area ($A_{cylinder}$):

$F_{load} = p_{cylinder} A_{cylinder}$

Therefore, the pressure at the bottom of the cylinder is directly proportional to the load and inversely proportional to the cylinder area:

$p_{cylinder} = \frac{F_{load}}{A_{cylinder}}$

The required pressure setting ($p_{set}$) of the counterbalance valve must be slightly higher than this pressure to prevent the load from dropping. This margin ensures stable operation and prevents the valve from constantly opening and closing due to minor pressure fluctuations. This margin pressure is often termed $p_{margin}$. The $A_{valve}$ term represents the effective valve spool area.

$p_{set} = \frac{F_{load}}{A_{valve}} + p_{margin}$

The flow rate (*Q*) through the counterbalance valve as it opens can again be described by the orifice equation:

$Q = C_d A_o \sqrt{\frac{2(p_{cylinder} - p_{tank})}{\rho}}$

Where:

- $C_d$ is the discharge coefficient
- $A_o$ is the orifice area (the opening of the counterbalance valve)
- $p_{cylinder}$ is the pressure at the primary port (connected to the cylinder)
- $p_{tank}$ is the tank pressure
- $\rho$ is the fluid density.


> 📊 *Diagram: {"subject": "Detailed cross-sectional view of a counterbalance valve, showing the spool, spring, pilot pressure connection (from the cylinder), check valve, primary port (to the cylinder), and secondary port (to the DCV). Show pressure annotations during holding and descent phases.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Hydraulic circuit illustrating the use of a counterbalance valve to control a vertical cylinder, including the DCV and pump. Highlight flow paths during extension and retraction.", "type": "schematic"}*


**Mirror Problems:**

Problem 1: Determine the required pressure setting for a counterbalance valve.

Load weight $F_{load} = 25 \text{ kN} = 25000 \text{ N}$
Cylinder area $A_{cylinder} = 10000 \text{ mm}^2 = 10000 \times 10^{-6} \text{ m}^2 = 0.01 \text{ m}^2$
Pressure margin $p_{margin} = 1 \text{ MPa} = 1 \times 10^6 \text{ Pa}$
Valve area $A_{valve} = 1200 \text{ mm}^2 = 1200 \times 10^{-6} \text{ m}^2 = 0.0012 \text{ m}^2$

$p_{set} = \frac{F_{load}}{A_{valve}} + p_{margin} = \frac{25000 \text{ N}}{0.0012 \text{ m}^2} + 1 \times 10^6 \text{ Pa} = 20.83 \times 10^6 \text{ Pa} + 1 \times 10^6 \text{ Pa} = 21.83 \text{ MPa}$

The required pressure setting for the counterbalance valve is 21.83 MPa.

Problem 2: Calculate the flow rate through the counterbalance valve during cylinder descent.

Cylinder pressure $p_{cylinder} = 8 \text{ MPa} = 8 \times 10^6 \text{ Pa}$
Tank pressure $p_{tank} = 0.3 \text{ MPa} = 0.3 \times 10^6 \text{ Pa}$
Orifice area $A_o = 25 \text{ mm}^2 = 25 \times 10^{-6} \text{ m}^2$
Discharge coefficient $C_d = 0.7$
Fluid density $\rho = 875 \text{ kg/m}^3$

$Q = C_d A_o \sqrt{\frac{2(p_{cylinder} - p_{tank})}{\rho}} = 0.7 \cdot 25 \times 10^{-6} \text{ m}^2 \cdot \sqrt{\frac{2 \cdot (8 \times 10^6 \text{ Pa} - 0.3 \times 10^6 \text{ Pa})}{875 \text{ kg/m}^3}} \approx 4.71 \times 10^{-4} \text{ m}^3/\text{s} = 0.471 \text{ L/s} = 28.26 \text{ LPM}$

The flow rate through the counterbalance valve is approximately 28.26 liters per minute.

Problem 3: Size a counterbalance valve for a cylinder with a known load and desired descent speed.

Load weight $F_{load} = 40 \text{ kN} = 40000 \text{ N}$
Descent speed $v = 0.05 \text{ m/s}$
Cylinder area $A_{cylinder} = 15000 \text{ mm}^2 = 15000 \times 10^{-6} \text{ m}^2 = 0.015 \text{ m}^2$
Fluid density $\rho = 860 \text{ kg/m}^3$
Discharge coefficient $C_d = 0.65$
Tank Pressure $p_{tank} = 0.2 \text{ MPa} = 0.2 \times 10^6 \text{ Pa}$
Pressure margin $p_{margin} = 0.75 \text{ MPa} = 0.75 \times 10^6 \text{ Pa}$

First calculate the flow rate, $Q = v \cdot A_{cylinder} = 0.05 \text{ m/s} \cdot 0.015 \text{ m}^2 = 7.5 \times 10^{-4} \text{ m}^3/\text{s} = 0.75 \text{ L/s}$

$p_{set} = \frac{F_{load}}{A_{valve}} + p_{margin}$

Choose a valve area $A_{valve} = 1600 \text{ mm}^2 = 0.0016 \text{ m}^2$

$p_{set} = \frac{40000 \text{ N}}{0.0016 \text{ m}^2} + 0.75 \times 10^6 \text{ Pa} = 25.75 \text{ MPa}$

$Q = C_d A_o \sqrt{\frac{2(p_{cylinder} - p_{tank})}{\rho}}$

$A_o = \frac{Q}{C_d \sqrt{\frac{2(p_{cylinder} - p_{tank})}{\rho}}} = \frac{7.5 \times 10^{-4} \text{ m}^3/\text{s}}{0.65 \cdot \sqrt{\frac{2 \cdot (25.75 \times 10^6 - 0.2 \times 10^6) \text{ Pa}}{860 \text{ kg/m}^3}}} = 1.61 \times 10^{-5} \text{ m}^2 = 16.1 \text{ mm}^2$

Therefore, a counterbalance valve with a spool area of 1600 $mm^2$, an opening area of 16.1 $mm^2$, and a pressure setting of 25.75 MPa is appropriate for this application.

Problem 4:  Calculate the pressure at the DCV port to retract the cylinder given the counterbalance valve opening pressure, integral check valve cracking pressure, and cylinder area.

Opening pressure $p_{set} = 10 \text{ MPa}$
Check valve cracking pressure = 0.3 MPa
Cylinder area = 8000 $mm^2$

The DCV must supply enough pressure to overcome both the spring force of the counterbalance valve AND the check valve cracking pressure.

$p_{DCV} = p_{set} + 0.3 \text{ MPa} = 10.3 \text{ MPa}$

Flow control valves are used to regulate the speed of hydraulic cylinders and motors by controlling the flow rate to these actuators. By restricting or throttling the flow of hydraulic fluid, these valves allow precise control over the movement and speed of hydraulically driven components. This is critical in applications requiring smooth, consistent, and repeatable motion, such as in robotic arms, machine tools, and material handling equipment.

They may be as simple as a fixed orifice or an adjustable needle valve. A fixed orifice provides a constant restriction, suitable for applications where a consistent flow rate is required and pressure variations are minimal. However, for more dynamic control, adjustable valves like needle valves are used, allowing for precise calibration of the flow rate.

Needle valves are designed to give fine control of flow in small-diameter piping. Their name is derived from their sharp, pointed conical disk and matching seat. This design allows for very small changes in the flow area, providing excellent resolution and control, particularly at low flow rates. The fine control is essential in applications where even small variations in flow can significantly impact the performance of the hydraulic system.

The stem of a needle valve typically has several color rings, which, in conjunction with a numbered knob, permits reading of a given valve opening. Charts are often available that allow quick determination of the controlled flow rate for given valve settings and pressure drops. These charts are empirically derived and specific to each valve model, providing a convenient way to set the desired flow rate without needing to perform calculations. A locknut is usually provided to prevent unwanted changes in flow due to vibration or accidental adjustment.

There are two basic types of flow control valves: non-pressure-compensated and pressure-compensated. The non-pressure-compensated type is used where system pressures are relatively constant and motor speeds are not too critical. These valves rely on the principle that the flow through an orifice will be constant if the pressure drop across the orifice remains constant. This simplicity makes them cost-effective for applications where load variations are minimal and precise speed control is not essential.

If the load on an actuator changes significantly, system pressure will change appreciably. Thus, the flow rate through a non-pressure-compensated valve will change for the same valve setting. For applications requiring more precise speed control despite varying loads, pressure-compensated flow control valves are necessary. This design incorporates a hydrostat (a pressure-regulating mechanism) that maintains a constant pressure differential across the throttle, which is an adjustable orifice. The orifice area setting determines the flow rate to be controlled. The hydrostat is held normally open by a light spring. However, it starts to close as inlet pressure increases and overcomes the light spring force. This closing action restricts the flow through the hydrostat, blocking off any flow in excess of the throttle setting, thereby maintaining a constant flow rate regardless of pressure fluctuations.

An actual pressure-compensated flow control valve, which has a pressure rating of 3000 psi. Pressure compensation will maintain preset flow within 1 to 5%, depending on the basic flow rate, as long as there is a 150-psi pressure differential between the inlet and outlet ports. The dial is calibrated for easy and repeatable flow setting. Adjustments over the complete valve capacity of, for example, 12 gpm are obtained within a 270-degree arc. A dial key lock prevents tampering with valve settings. A sharp-edged orifice design means that the valve is immune to temperature of fluid viscosity changes because the sharp edge minimizes the impact of viscous drag on the flow.

The fundamental principle governing flow through an orifice, such as in a needle valve, is described by the orifice equation:

$Q = C_d A(x) \sqrt{\frac{2\Delta p}{\rho}}$

Where:

- $Q$ is the flow rate
- $C_d$ is the discharge coefficient (accounts for losses due to friction and flow geometry)
- $A(x)$ is the variable orifice area, which depends on the needle valve stem position *x*
- $\Delta p$ is the pressure drop across the orifice
- $\rho$ is the fluid density

The orifice area, *A(x)*, is a function of the needle valve stem position. Modeling this relationship precisely can be complex, depending on the geometry of the needle and seat. However, for small displacements, it can often be approximated as a linear function: $A(x) \approx k_1 x$, where $k_1$ is a constant that depends on the valve's geometry.

For pressure-compensated valves, the key is maintaining a constant pressure drop ($\Delta p$) across the metering orifice. This is achieved using a hydrostat. The force balance on the hydrostat spool ensures that any increase in inlet pressure is met with a corresponding increase in the force opposing the spring, thus throttling the flow and maintaining a constant $\Delta p$.

If $p_{in}$ is the inlet pressure and $p_{out}$ the outlet pressure, then $\Delta p = p_{in} - p_{out} = constant$.

The relationship between actuator speed (*v*) and flow rate (*Q*) is straightforward:

$v = \frac{Q}{A_{actuator}}$

Where $A_{actuator}$ is the area of the cylinder piston or the displacement of the motor.


> 📊 *Diagram: {"subject": "Detailed cross-sectional view of a needle valve, showing the needle, seat, stem, color rings, and locknut. Include a magnified view of the needle and seat interface.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Cutaway view of a pressure-compensated flow control valve, illustrating the hydrostat, throttle orifice, spring, and pressure sensing ports.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Hydraulic circuit using a flow control valve to regulate the speed of a hydraulic cylinder. Show both meter-in and meter-out configurations.", "type": "schematic"}*


**Mirror Problems:**

Problem 1: Calculate the flow rate through a needle valve.

Pressure drop $\Delta p = 3 \text{ MPa} = 3 \times 10^6 \text{ Pa}$
Needle valve opening $x = 0.8 \text{ mm} = 0.8 \times 10^{-3} \text{ m}$
Discharge coefficient $C_d = 0.7$
Fluid density $\rho = 880 \text{ kg/m}^3$

Assume $A(x) = k_1 x$, and $k_1 = 5 \times 10^{-4}$

$A(x) = 5 \times 10^{-4} \text{ m} \cdot 0.8 \times 10^{-3} \text{ m} = 4 \times 10^{-7} \text{ m}^2$

$Q = C_d A(x) \sqrt{\frac{2\Delta p}{\rho}} = 0.7 \cdot 4 \times 10^{-7} \text{ m}^2 \cdot \sqrt{\frac{2 \cdot 3 \times 10^6 \text{ Pa}}{880 \text{ kg/m}^3}} \approx 1.84 \times 10^{-4} \text{ m}^3/\text{s} = 0.184 \text{ L/s} = 11.04 \text{ LPM}$

The flow rate through the needle valve is approximately 11.04 liters per minute.

Problem 2: Determine the required orifice area of a flow control valve to achieve a desired actuator speed.

Actuator speed $v = 0.1 \text{ m/s}$
Actuator area $A_{actuator} = 5000 \text{ mm}^2 = 5000 \times 10^{-6} \text{ m}^2 = 0.005 \text{ m}^2$
Flow rate $Q = v \cdot A_{actuator} = 0.1 \text{ m/s} \cdot 0.005 \text{ m}^2 = 5 \times 10^{-4} \text{ m}^3/\text{s}$

Now, assume we have a desired pressure drop of 2 MPa and $C_d = 0.65$.

$5 \times 10^{-4} = 0.65 A \sqrt{\frac{2 * 2 \times 10^6}{900}}$

$A = 5 \times 10^{-4} / (0.65 *  \sqrt{\frac{2 * 2 \times 10^6}{900}}) = 8.07 \times 10^{-7} m^2 = 0.807 mm^2$

Problem 3: Analyze the effect of load change on the flow rate through a non-pressure-compensated flow control valve.

Initial pressure drop $\Delta p_1 = 3 \text{ MPa}$
Final pressure drop $\Delta p_2 = 1.5 \text{ MPa}$
Fluid Density $\rho = 900 \text{ kg/m}^3$
Discharge Coefficient $C_d = 0.6$
Orifice area $A = 2 \times 10^{-7} m^2$

The flow rate will change since it's non-pressure compensated

$Q_1 = C_d A \sqrt{\frac{2\Delta p_1}{\rho}}$
$Q_2 = C_d A \sqrt{\frac{2\Delta p_2}{\rho}}$

$Q_1 = 0.6 * 2 \times 10^{-7} \sqrt{\frac{2*3 \times 10^6}{900}} = 3.28 \times 10^{-4} m^3/s$
$Q_2 = 0.6 * 2 \times 10^{-7} \sqrt{\frac{2*1.5 \times 10^6}{900}} = 2.32 \times 10^{-4} m^3/s$

Problem 4: Given an actuator with a known diameter and stroke, choose a non-pressure compensated valve with a certain Cv rating.

Cylinder diameter: 50 mm
Actuator stroke: 200 mm
Pressure: 2000 psi
Fluid: Oil
Cycle time: 10 seconds

Volume = $ \pi r^2 h = \pi * (0.025)^2 * 0.2 = 0.000393 m^3 = 0.393 L$

Flow rate = volume/ time = 0.393/10 = 0.0393 L/s = 2.36 L/min = 0.623 GPM

$C_v = Q / \sqrt{ \frac{\Delta P}{SG} }$
SG of oil = 0.87
Delta P = 2000 psi

$ C_v = 0.623 /  \sqrt{ \frac{2000}{0.87}} = 0.013 $

Therefore, a Cv rating of 0.013 is appropriate. The closest off-the-shelf valve would be approximately 0.02.