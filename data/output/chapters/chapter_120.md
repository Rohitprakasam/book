---
title: "Chapter 120"
author: "BookForge Draft"
---

### Logic Gates in Fluid Power Circuits

Fluid power circuits, like their electronic counterparts, rely on logic to control the flow of fluids (hydraulic oil or compressed air) to perform specific tasks. The fundamental logic gates -- OR, NOT, and MEMORY (Set-Reset) -- can be implemented using directional control valves and other pneumatic or hydraulic components. These gates form the building blocks for more complex control systems, enabling automated sequences and safety interlocks. Historically, these circuits predate the widespread use of Programmable Logic Controllers (PLCs), offering a robust, though less flexible, solution for machine control. In many industries, simpler machines still benefit from the simplicity and reliability of these pneumatic logic controls.

### OR Circuit

An OR circuit is a fundamental logic gate where the output is active if *any* of the inputs are active. In fluid power, an active signal translates to the presence of pressure (above a certain threshold). Thus, in an OR circuit, a control signal (pressure) at *any* one of the input ports will result in an output pressure. The output will only be inactive (no pressure) if *all* control signals are off (no pressure). This functionality is achieved through the use of shuttle valves connected in parallel or similar configurations. If any one of the input valves receives a pilot signal (air pressure to the pilot port), it will produce an output at the output port.

This configuration provides a level of redundancy and flexibility. For example, in a safety circuit, multiple sensors might be connected to an OR gate. If *any* of the sensors detect a hazardous condition (e.g., a machine guard is opened), the output of the OR gate will trigger a safety shutdown. The fail-safe nature of this design ensures that the system defaults to a safe state in case of a sensor failure. Specifically, if one sensor fails (fails to provide a pressure signal), the other sensors can still activate the shutdown through the OR logic.


> 📊 *Diagram: {"subject": "Schematic of a hydraulic OR gate using shuttle valves. Show input ports (A, B), output port (P), and shuttle valve movement. Label pressures p_A, p_B, p_P.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Pneumatic OR gate symbol according to ISO 1219.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Cutaway view of a shuttle valve, highlighting the sealing mechanism and flow path.", "type": "technical illustration"}*


Mathematically, we can represent the output pressure of an OR gate, $p_{out}$, as a function of the input pressures $p_1, p_2, ... p_n$. Assuming an ideal OR gate, the output pressure would simply be the maximum of the input pressures. However, in reality, there are always some pressure losses due to friction and flow restrictions within the valve. We can model this as:

$p_{out} = max(p_1, p_2, ... p_n) - p_{loss}$

Where $p_{loss}$ represents the pressure loss within the OR gate. The term "pressure dominance" refers to the input with the highest pressure dictating the output pressure (minus losses). If the pressures are very close, the valve design will dictate behavior.

##### Mirror Problem 1

Two input pressures, $p_1$ and $p_2$, are applied to an OR gate. Calculate the output pressure, $p_{out}$, given the following values and a constant pressure loss $p_{loss} = 0.3$ MPa.

- Case 1: $p_1 = 3$ MPa, $p_2 = 1$ MPa
- Case 2: $p_1 = 2$ MPa, $p_2 = 6$ MPa
- Case 3: $p_1 = 8$ MPa, $p_2 = 8$ MPa

*Solution:*

- *Case 1:* $p_{out} = max(3, 1) - 0.3 = 3 - 0.3 = 2.7$ MPa
- *Case 2:* $p_{out} = max(2, 6) - 0.3 = 6 - 0.3 = 5.7$ MPa
- *Case 3:* $p_{out} = max(8, 8) - 0.3 = 8 - 0.3 = 7.7$ MPa

##### Mirror Problem 2

A safety circuit uses an OR gate. Input 1 is from a machine guard, and Input 2 is from an emergency stop button. If $p > 1$ MPa is considered "safe" and $p < 0.5$ MPa is considered "unsafe," determine whether the machine is safe or unsafe for the following input pressures, assuming $p_{loss} = 0.3$ MPa.

- Case 1: $p_1 = 0.2$ MPa, $p_2 = 0$ MPa
- Case 2: $p_1 = 2$ MPa, $p_2 = 0$ MPa
- Case 3: $p_1 = 0$ MPa, $p_2 = 2$ MPa
- Case 4: $p_1 = 2$ MPa, $p_2 = 2$ MPa

*Solution:*

- *Case 1:* $p_{out} = max(0.2, 0) - 0.3 = 0.2 - 0.3 = -0.1$ MPa (Since pressure cannot be negative, we consider it 0 MPa). Since $p_{out} < 0.5$ MPa, the machine is *unsafe*.
- *Case 2:* $p_{out} = max(2, 0) - 0.3 = 2 - 0.3 = 1.7$ MPa. Since $p_{out} > 1$ MPa, the machine is *safe*.
- *Case 3:* $p_{out} = max(0, 2) - 0.3 = 2 - 0.3 = 1.7$ MPa. Since $p_{out} > 1$ MPa, the machine is *safe*.
- *Case 4:* $p_{out} = max(2, 2) - 0.3 = 2 - 0.3 = 1.7$ MPa. Since $p_{out} > 1$ MPa, the machine is *safe*.

##### Mirror Problem 3

Design an OR gate for a pneumatic system. Given a maximum allowed pressure loss of $p_{loss, max} = 0.2$ bar, and input pressures $p_1, p_2$ in the range of 3-8 bar, find the maximum flow rate, $Q$, that the OR gate can handle. (Assume the pressure loss is linearly proportional to the flow rate: $p_{loss} = kQ$, where $k$ is a constant that depends on the valve geometry and fluid properties).

*Solution*:

This problem requires empirical data or a detailed valve model to determine the constant *k*. Without that information, we can only outline the design process.

1.  **Select a shuttle valve:**Choose a valve with a flow rating appropriate for the application. Consult valve manufacturer catalogs for flow characteristics.
2.**Experimentally Determine k:** Set up an experiment to measure the pressure drop across the selected valve at different flow rates. Plot the data and determine the slope, *k*, of the linear relationship between pressure loss and flow rate.
3.  **Calculate Maximum Flow Rate:** Using the determined value of *k* and the maximum allowed pressure loss $p_{loss, max}$, calculate the maximum flow rate:

    $Q_{max} = \frac{p_{loss, max}}{k}$

    For example, if experimentally determined that $k = 0.005$ bar/lpm, then

    $Q_{max} = \frac{0.2 \text{ bar}}{0.005 \text{ bar/lpm}} = 40 \text{ lpm}$

This means that the selected shuttle valve can handle a maximum flow rate of 40 lpm while maintaining a pressure loss less than 0.2 bar.

### NOT Circuit

In a NOT function, the output is ON (pressure is present) only when the single input control signal A is OFF (no pressure), and vice versa. The output will be OFF (no pressure) if the control signal A is ON (pressure is present). This inverts the input signal. A pneumatic NOT gate typically employs a 3/2 normally closed (NC) valve. A constant pressure supply is connected to the inlet port of the valve. When the input signal (control signal A) is OFF, the valve is in its default state, allowing the supply pressure to pass through to the output port. When the input signal is ON, it actuates the valve, closing the path from the supply to the output and venting the output port to atmosphere.

The time delay associated with NOT gates is an important consideration in circuit design. It takes a finite amount of time for the valve spool to shift in response to the input signal. This switching time depends on the valve's design, the pilot pressure, and the spool's mass.


> 📊 *Diagram: {"subject": "Schematic of a pneumatic NOT gate using a 3/2 normally closed valve. Show supply pressure, input signal, and output. Label pressures p_in, p_out, p_s.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Pneumatic NOT gate symbol according to ISO 1219.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Cutaway view of a 3/2 NC valve used as a NOT gate, highlighting the spool position and flow path in both states.", "type": "technical illustration"}*


Mathematically, we can model a simplified NOT gate as follows:

$p_{out} = \begin{cases}
p_s - p_{loss} & \text{if } p_{in} < p_{threshold} \\
0 & \text{if } p_{in} > p_{threshold}
\end{cases}$

Where $p_{out}$ is the output pressure, $p_{in}$ is the input pressure, $p_s$ is the supply pressure, $p_{loss}$ is the pressure loss when the valve is open, and $p_{threshold}$ is the minimum input pressure required to actuate the valve.

The pressure loss, $p_{loss}$, can be modeled as a function of the flow rate, $Q$, through the valve: $p_{loss} = f(Q)$. A simple linear model could be: $p_{loss} = kQ$, where k is a constant depending on valve geometry and fluid properties.

The switching time, $t_{switch}$, for the valve can be estimated using Newton's Second Law. The force acting on the valve spool is the product of the pilot pressure and the spool area: $F = p_{in} A_{spool}$. The acceleration of the spool is then $a = F/m_{spool} = (p_{in} A_{spool})/m_{spool}$. Assuming constant acceleration over the distance, $x$, the spool needs to travel to switch the valve, the switching time can be estimated as:

$t_{switch} = \sqrt{\frac{2x}{a}} = \sqrt{\frac{2xm_{spool}}{p_{in} A_{spool}}}$

##### Mirror Problem 1

Given an input pressure, $p_{in}$, to a NOT gate, and a supply pressure, $p_s = 6$ MPa, calculate the output pressure, $p_{out}$, taking into account a pressure loss of $p_{loss} = 0.2$ MPa and a threshold pressure of $p_{threshold} = 1$ MPa.

- Case 1: $p_{in} = 0.5$ MPa
- Case 2: $p_{in} = 2$ MPa

*Solution:*

- *Case 1:* Since $p_{in} = 0.5 \text{ MPa} < p_{threshold} = 1 \text{ MPa}$, $p_{out} = p_s - p_{loss} = 6 - 0.2 = 5.8$ MPa.
- *Case 2:* Since $p_{in} = 2 \text{ MPa} > p_{threshold} = 1 \text{ MPa}$, $p_{out} = 0$ MPa.

##### Mirror Problem 2

A NOT gate is used to de-energize a circuit when the input pressure exceeds a certain threshold. The supply pressure is constant at $p_s = 5$ MPa. If the system has a response time requirement of $t_{switch} = 0.02$ seconds, and the spool mass is $m_{spool} = 0.02$ kg, the spool area is $A_{spool} = 30 \text{ mm}^2 = 30 \times 10^{-6} \text{ m}^2$, and the distance to travel is $x = 3 \text{ mm} = 3 \times 10^{-3} \text{ m}$, calculate the minimum input pressure, $p_{in}$, required to actuate the valve within the desired time.

*Solution:*

We can rearrange the switching time equation to solve for $p_{in}$:

$t_{switch} = \sqrt{\frac{2xm_{spool}}{p_{in} A_{spool}}}$

$t_{switch}^2 = \frac{2xm_{spool}}{p_{in} A_{spool}}$

$p_{in} = \frac{2xm_{spool}}{t_{switch}^2 A_{spool}}$

$p_{in} = \frac{2(3 \times 10^{-3} \text{ m})(0.02 \text{ kg})}{(0.02 \text{ s})^2 (30 \times 10^{-6} \text{ m}^2)} = \frac{1.2 \times 10^{-4}}{1.2 \times 10^{-8}} = 10000 \text{ Pa} = 1 \text{ MPa}$

Therefore, the minimum input pressure required to actuate the valve within 0.02 seconds is 1 MPa.

##### Mirror Problem 3

Design a pneumatic NOT gate. Given a supply pressure of $p_s = 7$ bar and a desired output flow rate of $Q = 10$ lpm, determine the appropriate valve size to minimize pressure loss.

*Solution:*

This problem requires consulting valve manufacturer catalogs to find a 3/2 NC valve that meets the specified flow rate and supply pressure requirements while minimizing pressure loss. Valve datasheets typically provide a flow coefficient ($C_v$ or $K_v$) that relates flow rate to pressure drop. The goal is to select a valve with a high flow coefficient for the given flow rate. A larger valve will generally have a lower pressure drop at a given flow rate, but it may also be more expensive and require more space. The specific valve selection depends on the available options and the acceptable trade-offs between cost, size, and performance.

### MEMORY Circuit

A MEMORY circuit, also known as an SR (Set-Reset) latch, "remembers" the last input signal it received. It maintains its output state even after the input signal is removed. This is typically achieved using a double-piloted valve. A brief pressure signal (the "Set" signal) applied to one pilot port shifts the valve to one state, and it remains in that state until a pressure signal (the "Reset" signal) is applied to the other pilot port.

A critical consideration for memory circuits is the possibility of metastability. If both the Set and Reset signals are applied simultaneously, the valve's behavior becomes unpredictable. It may switch to either state, or it may remain in an indeterminate state for a short period. This can lead to unreliable operation of the system. Design strategies, such as ensuring that one signal dominates the other or using interlocking mechanisms, can be implemented to prevent simultaneous activation of both Set and Reset inputs.


> 📊 *Diagram: {"subject": "Schematic of a hydraulic MEMORY circuit using a double-piloted valve. Show set and reset inputs, output, and pilot lines. Label pressures p_set, p_reset, p_out.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Pneumatic MEMORY circuit symbol using two interconnected valves (latching relay equivalent).", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Cutaway view of a double-piloted valve, highlighting the pilot chambers and spool position in both states.", "type": "technical illustration"}*


Modeling the pressure dynamics within the pilot lines of the double-piloted valve is crucial for understanding the circuit's behavior. The pilot pressure, $p_{pilot}$, builds up as a function of the input flow rate, $Q_{pilot}$, and the volume of the pilot chamber, $V_{pilot}$. Assuming ideal gas behavior and isothermal compression (or incompressible fluid)

$\frac{dp_{pilot}}{dt} = \frac{Q_{pilot} p_s}{V_{pilot}}$

This simplified equation shows that the rate of change of pilot pressure is proportional to the pilot flow rate and supply pressure, and inversely proportional to the pilot chamber volume. In reality, the pressure build-up will be slower due to factors such as compressibility of the fluid and leakage.

##### Mirror Problem 1

Given that the pilot pressure required to shift a double-piloted valve is $p_{pilot} = 1$ MPa, the volume of the pilot chamber is $V_{pilot} = 3 \text{ cm}^3 = 3 \times 10^{-6} \text{ m}^3$, the pilot flow rate is $Q_{pilot} = 2 \text{ lpm} = 2 \times 10^{-3} \text{ m}^3/\text{min} = 3.33 \times 10^{-8} \text{ m}^3/\text{s}$, and the supply pressure is $p_s = 6$ MPa, calculate how long it will take to switch the valve.

*Solution:*

Integrating the pressure build-up equation from 0 to $t$:

$\int_{0}^{p_{pilot}} dp = \int_{0}^{t} \frac{Q_{pilot} p_s}{V_{pilot}} dt$

$p_{pilot} = \frac{Q_{pilot} p_s}{V_{pilot}} t$

Solving for t:

$t = \frac{p_{pilot} V_{pilot}}{Q_{pilot} p_s} = \frac{(1 \times 10^6 \text{ Pa})(3 \times 10^{-6} \text{ m}^3)}{(3.33 \times 10^{-8} \text{ m}^3/\text{s})(6 \times 10^6 \text{ Pa})} = \frac{3}{0.1998} \approx 15 \text{ seconds}$

Therefore, it will take approximately 15 seconds to switch the valve.

##### Mirror Problem 2

Analyze the effect of simultaneous inputs to a memory circuit. If both the Set and Reset inputs are activated simultaneously, but the Set input has a slightly higher pressure of 0.05 MPa than the Reset input, and the pilot pressure required to shift the valve is 1 MPa, determine which state the valve will switch to.

*Solution:*

In this case, the valve will switch to the Set state because the Set input has a slightly higher pressure. However, this scenario is highly undesirable due to the possibility of a prolonged transient state. The valve may oscillate briefly or take longer than normal to fully switch, because the *net* pressure differential is only 0.05 MPa as opposed to ~1 MPa normally.

##### Mirror Problem 3

Design a pneumatic memory circuit. Given a specific holding force requirement of 300 N for the output cylinder, and a cylinder bore of 40 mm, determine the minimum pilot pressure required to maintain the valve in the desired state.

*Solution:*

The pressure required in the cylinder to generate the holding force is:

$p_{cylinder} = \frac{F}{A} = \frac{F}{\pi (D/2)^2} = \frac{300 \text{ N}}{\pi (0.04 \text{ m}/2)^2} = \frac{300}{\pi (0.02)^2} \approx 238732 \text{ Pa} \approx 0.24 \text{ MPa}$

This cylinder pressure must be maintained by the pilot pressure of the valve. However, to account for friction and leakage, the pilot pressure must be slightly higher than the cylinder pressure. Therefore, the minimum pilot pressure required would be above 0.24 MPa. A safety factor should also be applied. Valve selection will depend on the porting arrangement to ensure that the cylinder pressure is maintained when the Set or Reset signal is no longer present.

### MPL Control of Fluid Power Circuits

Machine Pneumatic Logic (MPL) control utilizes interconnected pneumatic components to automate sequences of operations in fluid power systems. In MPL circuits, limit switches, pushbuttons, and pilot valves are strategically positioned and connected to control the extension and retraction of cylinders in a predefined sequence. This approach offers a robust and reliable alternative to PLC control, particularly for simpler automated tasks. Compared to PLCs, MPL systems offer greater simplicity and potentially lower cost for basic applications, but they lack the flexibility and programmability of PLCs for complex control strategies. A key design consideration in MPL circuits is avoiding signal conflicts, where multiple valves are simultaneously activated in a manner that disrupts the intended sequence. Cascade design techniques are often employed to prevent such conflicts by dividing the control logic into distinct stages.


> 📊 *Diagram: {"subject": "Detailed schematic of the MPL circuit described in the text, showing all valves, cylinders, limit switches, and interconnections. Label all components clearly. Show flow direction.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Timing diagram illustrating the extension and retraction of each cylinder in the MPL sequence.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Illustration of a limit switch, showing its actuation mechanism and electrical connections.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Shows how an air pilot valve works.", "type": "technical illustration"}*


The timing of each cylinder's extension and retraction is a crucial parameter in MPL circuit design. This timing depends on factors such as the flow rates, cylinder volume, and valve switching times. The cycle time for the entire sequence is the sum of the individual cylinder extension and retraction times.

We can estimate the extension or retraction time, $t$, of a cylinder based on the volumetric flow rate, $Q$, and the cylinder volume, $V$, as:

$t = \frac{V}{Q}$

However, this is a simplified model. In practice, we should account for the effective piston area (subtracting the rod area in the case of retraction), compressibility of the fluid and pressure losses through control valves and piping.

The pressure drop across each valve in the MPL circuit also contributes to the overall system performance. The pressure drop is a function of the flow rate and the valve's flow coefficient. Accurate valve selection is necessary to minimize wasted energy and ensure consistent operation.

##### Mirror Problem 1

Calculate the cycle time for the two-cylinder MPL circuit described in the original text, given the following parameters:

- Cylinder 1: Bore $D_1 = 50$ mm, Stroke $L_1 = 200$ mm
- Cylinder 2: Bore $D_2 = 60$ mm, Stroke $L_2 = 250$ mm
- Flow Rate (both cylinders): $Q = 10$ lpm $= 1.67 \times 10^{-4} \text{ m}^3/\text{s}$
- Valve Switching Time: $t_{switch} = 0.2$ seconds

*Solution:*

1.  **Calculate Cylinder Volumes:**$V_1 = \pi (D_1/2)^2 L_1 = \pi (0.05/2)^2 (0.2) \approx 3.93 \times 10^{-4} \text{ m}^3$

    $V_2 = \pi (D_2/2)^2 L_2 = \pi (0.06/2)^2 (0.25) \approx 7.07 \times 10^{-4} \text{ m}^3$

2.**Calculate Cylinder Extension and Retraction Times (Ideal):**$t_{extend1} = \frac{V_1}{Q} = \frac{3.93 \times 10^{-4} \text{ m}^3}{1.67 \times 10^{-4} \text{ m}^3/\text{s}} \approx 2.35 \text{ s}$

    $t_{extend2} = \frac{V_2}{Q} = \frac{7.07 \times 10^{-4} \text{ m}^3}{1.67 \times 10^{-4} \text{ m}^3/\text{s}} \approx 4.23 \text{ s}$

    We will assume here that the retraction times are identical to the extension times. Note that in practice, the retraction times may be smaller depending on the cylinder rod diameter.

3.**Calculate Total Cycle Time:**

    The sequence is: Cylinder 1 extends, Cylinder 2 extends, Cylinder 1 retracts, Cylinder 2 retracts.

    $t_{cycle} = t_{extend1} + t_{extend2} + t_{retract1} + t_{retract2} + 4 t_{switch} = 2.35 + 4.23 + 2.35 + 4.23 + 4(0.2) \approx 13.96 \text{ seconds}$

##### Mirror Problem 2

Modify the MPL circuit in the original text to include a safety interlock. If a guard is opened during the sequence, the circuit should immediately retract all cylinders. Determine the appropriate placement of sensors and valves to implement this interlock.

*Solution:*

To implement this safety interlock, we need to add a sensor to the machine guard that detects when it is open. This sensor could be a limit switch or a pressure sensor. The output of this sensor should be connected to a valve that, when activated, vents the pilot lines of all valves controlling cylinder extension. A 3/2 NC valve, activated by the guard sensor, can be placed in the pilot lines controlling the cylinder extending valves. When the guard is opened, the valve is actuated, venting these pilot lines to atmosphere and immediately retracting the cylinders. The safety valve should be placed as close as possible to the existing directional control valves to minimize response time.

##### Mirror Problem 3

Design an MPL circuit to control a three-cylinder sequence: Cylinder A extends, Cylinder B extends, Cylinder C extends, Cylinder A retracts, Cylinder B retracts, Cylinder C retracts. Specify the valve types, limit switch locations, and interconnections needed to achieve the desired sequence.

*Solution:*

This design will require a series of directional control valves, limit switches, and pilot valves.

1.  **Cylinders and Valves**: Each cylinder (A, B, and C) will require a double-acting cylinder and a 5/2 directional control valve (DCV) to control its extension and retraction.

2.**Limit Switches**:
    - Cylinder A requires two limit switches: A+ (activated at full extension) and A- (activated at full retraction).
    - Cylinder B requires two limit switches: B+ (activated at full extension) and B- (activated at full retraction).
    - Cylinder C requires two limit switches: C+ (activated at full extension) and C- (activated at full retraction).

3.**MPL Logic**:
    - A START valve initiates the sequence.
    - When the START valve is activated and A- is active, Cylinder A extends.
    - When A+ is active, Cylinder B extends.
    - When B+ is active, Cylinder C extends.
    - When C+ is active, Cylinder A retracts.
    - When A- is active, Cylinder B retracts.
    - When B- is active, Cylinder C retracts.
    - When C- is active, the system is ready for the next cycle.

The DCV for cylinder A is piloted by the START signal and the A- limit switch to extend, and the C+ limit switch to retract. The DCV for cylinder B is piloted by the A+ limit switch to extend, and the A- limit switch to retract. The DCV for cylinder C is piloted by the B+ limit switch to extend, and the B- limit switch to retract. The output signal must be connected to shift the valve controlling the subsequent cylinder, and the last limit switch will prepare the system for the subsequent actuation of the START button.