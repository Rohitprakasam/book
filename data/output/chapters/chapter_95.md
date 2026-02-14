---
title: "Chapter 95"
author: "BookForge Draft"
---

4. The valve spool is attached to the linkage and thus moves with it.

Intensifier Circuit:

An intensifier is a crucial component in hydraulic systems when a high-pressure output is required from a lower-pressure source. These devices are particularly useful in applications where a large force is needed for a relatively short distance or duration. Consider the historical context: intensifiers allowed for the development of more compact and efficient hydraulic machinery, particularly in applications like heavy manufacturing and materials processing. They operate based on Pascal's Law, which states that pressure applied to a confined fluid is transmitted equally in all directions throughout the fluid.  The underlying principle hinges on the conservation of energy (approximately, neglecting losses due to friction and heat).  Essentially, an intensifier trades flow rate for pressure.

Intensifiers, while powerful, have limitations. They don't create energy; instead, they convert low-pressure, high-flow-rate fluid power into high-pressure, low-flow-rate fluid power. This means that while the output pressure is increased, the volume of fluid delivered at that pressure is reduced proportionally. Therefore, they are best suited for applications requiring a brief burst of high-pressure force, such as hydraulic presses, riveting machines, spot welders, metal forming, and specialized clamping systems. Using an intensifier is often more cost-effective than employing a dedicated high-pressure pump, especially when high pressure is only needed intermittently.


> 📊 *Diagram: {"subject": "Cross-sectional view of a basic intensifier", "type": "technical illustration", "description": "Shows two cylinders of different diameters, a common piston, low-pressure inlet, high-pressure outlet, and labels for A0, A1, p0, p1. Dashed lines indicate stroke limits."}*


Let's mathematically derive the pressure intensification ratio. Consider a basic intensifier consisting of two cylinders with different cross-sectional areas connected by a common piston. The force exerted on each side of the piston must be equal (neglecting friction) for the system to be in equilibrium.

Let:
- $p_0$ = Pressure exerted on the large or operating end of the piston (low-pressure side)
- $p_1$ = Pressure exerted by the small end of the piston (high-pressure side)
- $A_0$ = Area of the large end of the piston
- $A_1$ = Area of the small end of the piston
- $F_0$ = Force on the low-pressure side
- $F_1$ = Force on the high-pressure side
- $x_0$ = Displacement of low-pressure side
- $x_1$ = Displacement of high-pressure side
- $\eta_{int}$ = Efficiency of the intensifier

The force on each side can be expressed as:
$F_0 = p_0 A_0$
$F_1 = p_1 A_1$

Since the forces must be equal:
$F_0 = F_1$
$p_0 A_0 = p_1 A_1$

Therefore, the intensification ratio is:
$\frac{p_1}{p_0} = \frac{A_0}{A_1}$

This equation shows that the pressure is increased by the ratio of the larger area to the smaller area.

Now, let's derive the displacement relationship, assuming the fluid is incompressible (which is a reasonable approximation for hydraulic oil):
The volume displaced on each side of the piston must be equal:

$V_0 = A_0 x_0$
$V_1 = A_1 x_1$
$V_0 = V_1$
$A_0 x_0 = A_1 x_1$

Therefore, the displacement relationship is:
$\frac{x_1}{x_0} = \frac{A_0}{A_1}$

Finally, let's look at the ideal work relationship:

$W_0 = p_0 V_0$
$W_1 = p_1 V_1$
$W_0 = W_1$

**Example Problems:**1.**Intensifier Pressure Calculation:**An intensifier has a large piston area ($A_0$) of 800 $cm^2$ and a small piston area ($A_1$) of 100 $cm^2$. If the input pressure ($p_0$) is 5 MPa, what is the output pressure ($p_1$), assuming ideal conditions?

    Solution:
    Using the intensification ratio formula:
    $p_1 = p_0 * \frac{A_0}{A_1}$
    $p_1 = 5 \text{ MPa} * \frac{800 \text{ cm}^2}{100 \text{ cm}^2}$
    $p_1 = 5 \text{ MPa} * 8$
    $p_1 = 40 \text{ MPa}$

2.**Intensifier Displacement Calculation:**An intensifier has a large piston area ($A_0$) of 1200 $cm^2$ and a small piston area ($A_1$) of 80 $cm^2$. If the low-pressure side displacement ($x_0$) is 10 cm, what is the high-pressure side displacement ($x_1$)?

    Solution:
    Using the displacement relationship formula:
    $x_1 = x_0 * \frac{A_0}{A_1}$
    $x_1 = 10 \text{ cm} * \frac{1200 \text{ cm}^2}{80 \text{ cm}^2}$
    $x_1 = 10 \text{ cm} * 15$
    $x_1 = 150 \text{ cm}$

3.**Intensifier Pressure Calculation (Non-Ideal):**An intensifier has a large piston area ($A_0$) of 900 $cm^2$ and a small piston area ($A_1$) of 75 $cm^2$. If the input pressure ($p_0$) is 7 MPa and the intensifier efficiency ($\eta_{int}$) is 85%, what is the output pressure ($p_1$)?

    Solution:
    First, calculate the ideal output pressure:
    $p_{1,ideal} = p_0 * \frac{A_0}{A_1}$
    $p_{1,ideal} = 7 \text{ MPa} * \frac{900 \text{ cm}^2}{75 \text{ cm}^2}$
    $p_{1,ideal} = 7 \text{ MPa} * 12$
    $p_{1,ideal} = 84 \text{ MPa}$

    Now, account for the efficiency:
    $p_1 = p_{1,ideal} * \eta_{int}$
    $p_1 = 84 \text{ MPa} * 0.85$
    $p_1 = 71.4 \text{ MPa}$**Intensifier Press Circuit**

This circuit configuration is frequently employed in punch press applications, where a high force is required for a short duration to perform the punching operation. When the directional control valve (DCV) is shifted to one position (let's say the left position), oil flows to the rod end of the main hydraulic cylinder. This initially causes the cylinder to extend rapidly with relatively low force. Once the cylinder encounters resistance and the pressure builds up to a certain level, the pilot signal from this pressure line opens a check valve in the intensifier circuit. This allows the oil to flow to the return side of the cylinder, causing it to retract.

When the DCV is shifted to the opposite position (the right position in this example), oil flows to the blank end of the cylinder *through* a check valve in the main line. This causes the cylinder to extend again.  As the cylinder extends and contacts the workpiece, the pressure in the cylinder increases. When the pressure in the cylinder reaches the pressure setting of the sequence valve, the intensifier starts to operate. The intensifier increases the pressure of the hydraulic fluid, and this high-pressure output closes the check valve in the main line. This diverts all flow through the intensifier, and the pressurized fluid is directed to the blank end of the cylinder, providing the necessary force to perform the punching operation. The sequence valve setting must be high enough to allow the cylinder to reach the workpiece but low enough to allow for pressure intensification before the punch stalls.

It's crucial to install the intensifier as close as possible to the hydraulic cylinder to minimize the length of the high-pressure lines. Long high-pressure lines increase system response time due to fluid compressibility and can cause significant pressure losses due to friction. Shorter lines result in quicker response times and more efficient energy transfer.


> 📊 *Diagram: {"subject": "Hydraulic circuit diagram of an intensifier press circuit", "type": "schematic", "description": "Shows DCV, check valve, sequence valve, intensifier, hydraulic cylinder, pressure gauges, and connecting lines. DCV is a 4/3 valve with a spring center position."}*


Let's analyze the circuit mathematically.  First, we need to calculate the appropriate setting for the sequence valve.

Let:
- $F_{punch}$ = Punching Force (the force required to perform the punching operation)
- $A_{cylinder}$ = Area of the cylinder piston (blank end)
- $p_{sequence}$ = Sequence Valve Pressure Setting

The sequence valve must be set to a pressure that allows the cylinder to develop sufficient force to contact the workpiece but opens before the cylinder stalls. We approximate this force by $F_{punch}$ and, therefore, the relationship is:

$p_{sequence} = \frac{F_{punch}}{A_{cylinder}}$

Next, calculating the total cycle time requires considering the extension, intensification, and retraction phases.  This is a complex calculation, and we'll make some simplifying assumptions to illustrate the principles. We'll assume constant pump flow and neglect the effects of compressibility and valve response times.

Let:
- $V_{cylinder}$ = Volume of the cylinder (blank end) = $A_{cylinder} * stroke$
- $Q_{pump}$ = Pump flow rate
- $A_{rod}$ = Area of the cylinder rod
- $A_{effective} = A_{cylinder} - A_{rod}$
- $Q_{intensified} = $ Pump flow rate / Intensifier Ratio
- $V_{intensifier}$ = Volume of fluid required from the intensifier to complete the punching stroke = $A_{cylinder} * punch\_depth$
- $t_{extend}$ = Time to extend the cylinder to the workpiece
- $t_{intensify}$ = Time to intensify the pressure and complete the punching operation
- $t_{retract}$ = Time to retract the cylinder

$t_{extend} = \frac{V_{cylinder}}{Q_{pump}} = \frac{A_{cylinder}*stroke}{Q_{pump}}$

$t_{intensify} = \frac{V_{intensifier}}{Q_{intensified}} = \frac{V_{intensifier} * Intensifier Ratio}{Q_{pump}}$

$t_{retract} = \frac{V_{cylinder}}{Q_{pump}}$

Total Cycle Time = $t_{extend} + t_{intensify} + t_{retract}$

It's worth noting that the retraction time can be reduced by using a regenerative circuit.

**Example Problems:**1.**Sequence Valve Setting Calculation:**A punch press requires a punching force of 120 kN. The hydraulic cylinder has a bore of 100 mm. Calculate the required sequence valve pressure setting.

    Solution:
    First, calculate the cylinder area:
    $A_{cylinder} = \pi * (\frac{bore}{2})^2 = \pi * (\frac{100 \text{ mm}}{2})^2 = \pi * (50 \text{ mm})^2 \approx 7854 \text{ mm}^2 = 78.54 \text{ cm}^2$

    Now, calculate the sequence valve pressure setting:
    $p_{sequence} = \frac{F_{punch}}{A_{cylinder}} = \frac{120000 \text{ N}}{78.54 \text{ cm}^2} \approx 1528 \frac{N}{cm^2} = 15.28 \text{ MPa}$

2.**Cycle Time Calculation:** A punch press has a cylinder with a bore of 120 mm, a rod diameter of 60 mm, and a stroke of 10 cm. The pump flow rate is 20 LPM, and the intensifier ratio is 3:1. Calculate the approximate total cycle time. Assume the punch depth is 2 cm.

    Solution:

    First, calculate the cylinder area and rod area:
    $A_{cylinder} = \pi * (\frac{120 \text{ mm}}{2})^2 \approx 11310 \text{ mm}^2 = 113.1 \text{ cm}^2$
    $A_{rod} = \pi * (\frac{60 \text{ mm}}{2})^2 \approx 2827 \text{ mm}^2 = 28.27 \text{ cm}^2$

    Then calculate effective areas:
    $A_{effective} = A_{cylinder} - A_{rod} = 113.1 \text{ cm}^2 - 28.27 \text{ cm}^2 = 84.83 \text{ cm}^2$

    Next, calculate the volumes
    $V_{cylinder} = A_{cylinder} * stroke = 113.1 \text{ cm}^2 * 10 \text{ cm} = 1131 \text{ cm}^3 = 1.131 L$
    $V_{intensifier} = A_{cylinder} * punch\_depth = 113.1 \text{ cm}^2 * 2 \text{ cm} = 226.2 \text{ cm}^3 = 0.2262 L$

    Now convert pump flow to appropriate units:
    $Q_{pump} = 20 \frac{L}{\text{min}} = \frac{20}{60} \frac{L}{s} = 0.333 \frac{L}{s}$

    Calculate the extension time:
    $t_{extend} = \frac{V_{cylinder}}{Q_{pump}} = \frac{1.131 L}{0.333 L/s} \approx 3.39 s$

    Calculate the intensified flow:
    $Q_{intensified} = Q_{pump} / 3 = (0.333 L/s) / 3 \approx 0.111 L/s$

    Calculate the intensification time:
    $t_{intensify} = \frac{V_{intensifier}}{Q_{intensified}} = \frac{0.2262 L}{0.111 L/s} \approx 2.04 s$

    Calculate the retraction time. *Assuming* the DCV simply reverses flow:
    $t_{retract} = \frac{V_{cylinder}}{Q_{pump}} = \frac{1.131 L}{0.333 L/s} \approx 3.39 s$

    Total cycle time:
    $t_{total} = t_{extend} + t_{intensify} + t_{retract} = 3.39 s + 2.04 s + 3.39 s \approx 8.82 s$


> 📊 *Diagram: {"subject": "Detailed hydraulic circuit diagram for the intensifier press circuit", "type": "schematic", "description": "Includes all components (DCV, check valve, sequence valve, intensifier, cylinder), pressure gauges, and connecting lines. The DCV should be a 4/3 valve with a spring center position and the intensifier is near the cylinder."}*


> 📊 *Diagram: {"subject": "Timing diagram illustrating the pressure and position changes during one complete cycle of the intensifier press circuit", "type": "graph", "description": "Shows p0, p1, cylinder position vs time throughout extension, intensification, and retraction."}*


**Regenerative Circuit**

A regenerative circuit is cleverly designed to increase the extending speed of a double-acting hydraulic cylinder. The fundamental concept involves connecting both ends of the hydraulic cylinder in parallel, effectively bypassing the flow control limitations imposed by a standard double-acting cylinder configuration. This parallel connection means that the fluid exiting the rod end of the cylinder during extension is redirected to the blank end, supplementing the pump's flow.  Consider that, normally, the fluid leaving the rod end goes directly to the tank. This effectively "regenerates" the fluid, hence the name.

The primary advantage of a regenerative circuit is the increased extending speed. However, there's a trade-off: the extending force is reduced. Because the fluid from the rod end assists the extension, the effective area on which the pump pressure acts is reduced (it's the difference between the piston area and the rod area). Regenerative circuits are particularly beneficial in applications where rapid traverse movements are needed, and the load during that portion of the cycle is relatively light. Examples include rapid advance strokes in machine tools before cutting, or positioning applications where speed is more important than force during the initial movement.


> 📊 *Diagram: {"subject": "Hydraulic circuit diagram of a regenerative circuit", "type": "schematic", "description": "Shows the DCV, the double-acting cylinder, and the connection between the rod end and blank end of the cylinder during extension. Clearly label Qp, QR, AP, AR. The DCV should be a 4/3 valve."}*


Let's mathematically analyze this circuit. We'll start by deriving the extending speed equation using the continuity equation (conservation of mass).

Let:
- $Q_p$ = Pump flow rate
- $Q_R$ = Regenerative flow rate (flow from the rod end)
- $A_P$ = Piston area (area of the blank end)
- $A_R$ = Rod area
- $V_{EXT}$ = Extending speed
- $V_{RET}$ = Retracting speed
- $F_{EXT}$ = Extending force
- $F_{RET}$ = Retracting force
- $p$ = System pressure

During extension, the total flow entering the blank end of the cylinder is the sum of the pump flow and the regenerative flow:

$Q_p + Q_R = A_P V_{EXT}$

The regenerative flow is equal to the rod area multiplied by the extending speed:

$Q_R = A_R V_{EXT}$

Substituting the second equation into the first:

$Q_p + A_R V_{EXT} = A_P V_{EXT}$

Solving for $V_{EXT}$:

$Q_p = A_P V_{EXT} - A_R V_{EXT}$
$Q_p = (A_P - A_R) V_{EXT}$
$V_{EXT} = \frac{Q_p}{A_P - A_R}$

Now, let's derive the retracting speed equation. During retraction, the pump flow goes directly to the piston area, and the rod side is connected to the tank:

$V_{RET} = \frac{Q_p}{A_P}$

The speed ratio is then:

$\frac{V_{EXT}}{V_{RET}} = \frac{\frac{Q_p}{A_P - A_R}}{\frac{Q_p}{A_P}} = \frac{A_P}{A_P - A_R}$

Now, derive the force equation during extension. The extending force is the pressure multiplied by the *effective* area, which is the piston area minus the rod area:

$F_{EXT} = p (A_P - A_R)$

And, the retracting force:
$F_{RET} = p A_P$

**Example Problems:**1.**Extending Speed Calculation:**A regenerative circuit has a pump flow rate of 25 LPM, a piston area of 78.5 $cm^2$ (100 mm bore), and a rod area of 19.6 $cm^2$ (50 mm rod). Calculate the extending speed.

    Solution:
    Convert flow rate to $cm^3/s$:
    $Q_p = 25 \frac{L}{\text{min}} = \frac{25000 \text{ cm}^3}{60 \text{ s}} \approx 416.67 \frac{\text{cm}^3}{\text{s}}$

    Calculate the extending speed:
    $V_{EXT} = \frac{Q_p}{A_P - A_R} = \frac{416.67 \frac{\text{cm}^3}{\text{s}}}{78.5 \text{ cm}^2 - 19.6 \text{ cm}^2} = \frac{416.67 \frac{\text{cm}^3}{\text{s}}}{58.9 \text{ cm}^2} \approx 7.07 \frac{\text{cm}}{\text{s}} = 0.0707 \frac{m}{s}$

2.**Retracting Speed Calculation:**A regenerative circuit has a pump flow rate of 25 LPM and a piston area of 78.5 $cm^2$. Calculate the retracting speed.

    Solution:
    Using the flow rate from the previous example,
    $V_{RET} = \frac{Q_p}{A_P} = \frac{416.67 \frac{\text{cm}^3}{\text{s}}}{78.5 \text{ cm}^2} \approx 5.31 \frac{\text{cm}}{\text{s}} = 0.0531 \frac{m}{s}$

3.**Speed Ratio Calculation:**A regenerative circuit has a piston area of 78.5 $cm^2$ and a rod area of 19.6 $cm^2$. Calculate the speed ratio.

    Solution:
    $\frac{V_{EXT}}{V_{RET}} = \frac{A_P}{A_P - A_R} = \frac{78.5 \text{ cm}^2}{78.5 \text{ cm}^2 - 19.6 \text{ cm}^2} = \frac{78.5}{58.9} \approx 1.33$

4.**Force Calculation:** A regenerative circuit operates at a system pressure of 14 MPa. The piston area is 78.5 $cm^2$ and the rod area is 19.6 $cm^2$. Calculate the extending and retracting forces.

    Solution:
    Convert pressure to appropriate units:
    $p = 14 \text{ MPa} = 1400 \frac{N}{mm^2} = 14000 \frac{N}{cm^2}$

    Calculate the extending force:
    $F_{EXT} = p (A_P - A_R) = 14000 \frac{N}{cm^2} * (78.5 \text{ cm}^2 - 19.6 \text{ cm}^2) = 14000 \frac{N}{cm^2} * 58.9 \text{ cm}^2 = 824600 N = 82.46 kN$

    Calculate the retracting force:
    $F_{RET} = p A_P = 14000 \frac{N}{cm^2} * 78.5 \text{ cm}^2 = 1099000 N = 109.9 kN$


> 📊 *Diagram: {"subject": "Cutaway diagram showing the flow path within the cylinder and valve during the extension stroke of a regenerative circuit", "type": "technical illustration", "description": "Use arrows to clearly indicate the flow direction of the oil. Label pump inlet, cylinder ports, valve spools."}*


In general, the greater the ratio of piston area to rod area, the greater is the ratio of extending speed to retracting speed. When the piston area equals two times the rod area, the extension speed is twice the retraction speed.

Load carrying capacity:
In accordance with Pascal's law, the same system pressure is acting on both sides of the piston during the extension stroke. During the extension stroke of a regenerative cylinder, the extending force ($F_{EXT}$) is calculated as system pressure ($p$) multiplied by the difference between the piston area ($A_p$) and the rod area ($A_r$).

$F_{EXT} = p * (A_p - A_r)$