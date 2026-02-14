---
title: "Chapter 126"
author: "BookForge Draft"
---

3.  The output from the AND gate is fed into the MEMORY device, which remembers to keep pressure on the blank end of the cylinder during extension.

### 3.1 AND Gate in Hydraulic Circuits

The AND gate is a fundamental logic element. In digital electronics, an AND gate's output is "true" (1) only when all its inputs are "true" (1).  We can create an analogous function in hydraulic circuits. A hydraulic AND gate ensures that an output pressure is present only when all input pressures are present. This is useful for safety interlocks, where multiple conditions must be met before a machine can operate, and for sequencing operations, ensuring that one action completes before another begins.

Consider Pascal's Law, which states that pressure applied to a confined fluid is transmitted equally in all directions. This principle is fundamental to understanding how hydraulic AND gates function. In an ideal scenario, a hydraulic AND gate receives two or more input pressure signals and outputs the *lowest* of these pressures. This ensures that unless all inputs are pressurized, the output will remain low, preventing actuation of the subsequent device.


> 📊 *Diagram: {"subject": "Schematic of a 2-input hydraulic AND gate, showing the input pressure lines, the internal valve mechanism (e.g., shuttle valve), and the output pressure line. Label all pressures ($p_1$, $p_2$, $p_{out}$) and areas.", "type": "schematic"}*


Mathematically, we can express the behavior of an ideal AND gate. Let $p_1$ and $p_2$ be the input pressures. The output pressure, $p_{out}$, is given by:

$p_{out} = \min(p_1, p_2)$

This equation states that the output pressure is equal to the minimum of the two input pressures. This concept can be extended to an AND gate with 'n' inputs:

$p_{out} = \min(p_1, p_2, ..., p_n)$

In reality, hydraulic components are not ideal. Losses occur due to friction, internal leakage, and other factors. To account for these losses, we introduce an efficiency factor, $\eta_{AND}$ (where $0 < \eta_{AND} \le 1$), into the equation:

$p_{out} = \eta_{AND} \cdot \min(p_1, p_2, ..., p_n)$

The output force, $F_{out}$, produced by a hydraulic cylinder connected to the AND gate's output can be calculated using the output pressure and the cylinder's bore area, $A_{out}$:

$F_{out} = p_{out} \cdot A_{out}$

**Example Problem 1:**Two input pressures, $q_1 = 12 \text{ MPa}$ and $q_2 = 15 \text{ MPa}$, are applied to an AND gate. Calculate the output pressure $q_{out}$, assuming: (a) an ideal AND gate and (b) a non-ideal AND gate with efficiency $\eta_{AND} = 0.9$.

(a) Ideal AND gate:

$q_{out} = \min(q_1, q_2) = \min(12 \text{ MPa}, 15 \text{ MPa}) = 12 \text{ MPa}$

(b) Non-ideal AND gate:

$q_{out} = \eta_{AND} \cdot \min(q_1, q_2) = 0.9 \cdot 12 \text{ MPa} = 10.8 \text{ MPa}$**Example Problem 2:**An AND gate controls a hydraulic cylinder with bore area $B_{out} = 50 \text{ cm}^2$. Calculate the output force $F_{out}$ of the cylinder given two input pressures $q_1 = 10 \text{ MPa}$ and $q_2 = 14 \text{ MPa}$, and the AND gate efficiency $\eta_{AND} = 0.8$.

First, find the output pressure:

$q_{out} = \eta_{AND} \cdot \min(q_1, q_2) = 0.8 \cdot \min(10 \text{ MPa}, 14 \text{ MPa}) = 0.8 \cdot 10 \text{ MPa} = 8 \text{ MPa}$

Convert area to $m^2$: $50 \text{ cm}^2 = 50 \times 10^{-4} \text{ m}^2 = 0.005 \text{ m}^2$

Now, calculate the output force:

$F_{out} = q_{out} \cdot B_{out} = 8 \text{ MPa} \cdot 0.005 \text{ m}^2 = 8 \times 10^6 \text{ Pa} \cdot 0.005 \text{ m}^2 = 40,000 \text{ N} = 40 \text{ kN}$

### 3.2 Memory Devices (Pilot Operated Check Valves) in Hydraulic Circuits

In hydraulic systems, it's often necessary to maintain pressure in a part of the circuit even when the primary pressure source is removed or fluctuates. This "memory" function is crucial for holding a cylinder in position, clamping a workpiece, or maintaining a specific force. Simply relying on a pump to maintain pressure continuously is inefficient, as the pump would constantly cycle on and off, leading to wear and energy waste. Furthermore, any leakage in the system would cause the pressure to drop.

To overcome these limitations, hydraulic systems employ "memory devices," with pilot-operated check valves (POCVs) being a common solution. A POCV is a check valve that allows flow in one direction but blocks flow in the opposite direction unless a pilot pressure signal is applied. The check valve function ensures that pressure is held in the circuit. When a pilot signal is present, it overrides the check valve, allowing flow in the reverse direction. The behavior can be explained by the force balance on the check valve poppet.


> 📊 *Diagram: {"subject": "Schematic of a pilot-operated check valve, showing the inlet, outlet, pilot line, check valve poppet, spring, and pilot piston. Label all pressures ($p_{in}$, $p_{out}$, $p_{pilot}$) and areas ($A_{check}$, $A_{pilot}$).", "type": "schematic"}*


However, even with a POCV, pressure will eventually decay due to the compressibility of the hydraulic fluid and internal leakage. The compressibility is described by the Bulk Modulus of the fluid. A higher bulk modulus indicates a lower compressibility, meaning the fluid resists changes in volume under pressure.

To understand the opening condition of a POCV, consider the forces acting on the check valve poppet. The inlet pressure $p_{in}$ acts on the check valve area $A_{check}$, creating a force that tends to keep the valve closed. The pilot pressure $p_{pilot}$ acts on the pilot area $A_{pilot}$, creating a force that tends to open the valve. For the valve to open, the force due to the pilot pressure must overcome the force due to the inlet pressure:

$p_{pilot} A_{pilot} > p_{in} A_{check}$

We can define the pilot ratio, $\gamma$, as the ratio of the pilot area to the check valve area:

$\gamma = \frac{A_{pilot}}{A_{check}}$

Therefore, the condition for opening the POCV can be rewritten as:

$p_{pilot} > \frac{p_{in}}{\gamma}$

This equation shows that the required pilot pressure is inversely proportional to the pilot ratio. A higher pilot ratio means that a lower pilot pressure is needed to open the valve.

Now, let's consider the pressure decay rate in a hydraulic accumulator (representing the cylinder volume) due to leakage. The bulk modulus, $\beta$, relates the change in pressure to the change in volume:

$\beta = -V \frac{dp}{dV}$

Where:
- $\beta$ is the bulk modulus of the fluid
- $V$ is the volume of the fluid
- $dp$ is the change in pressure
- $dV$ is the change in volume

If we assume a constant leakage rate $Q_{leak}$, then the change in volume over time is simply $dV = Q_{leak} dt$. Substituting this into the bulk modulus equation and rearranging, we get the pressure decay rate:

$\frac{dp}{dt} = -\frac{\beta Q_{leak}}{V}$

This equation indicates that the pressure decay rate is proportional to the leakage rate and the bulk modulus, and inversely proportional to the volume.

To estimate the holding time $t_{hold}$ for a cylinder with volume $V$ and an allowable pressure drop $\Delta p$, we can integrate the pressure decay rate:

$\int_{p_0}^{p_0 - \Delta p} dp = -\frac{\beta Q_{leak}}{V} \int_{0}^{t_{hold}} dt$

Where $p_0$ is the initial pressure. Integrating both sides, we get:

$-\Delta p = -\frac{\beta Q_{leak}}{V} t_{hold}$

Solving for $t_{hold}$, we find:

$t_{hold} = \frac{V \Delta p}{\beta Q_{leak}}$**Example Problem 1:**A pilot-operated check valve has a pilot ratio $\alpha = 5:1$. Calculate the minimum pilot pressure $q_{pilot}$ required to open the valve and allow flow, given the inlet pressure $q_{in} = 20 \text{ MPa}$.

$q_{pilot} > \frac{q_{in}}{\alpha} = \frac{20 \text{ MPa}}{5} = 4 \text{ MPa}$

Therefore, the pilot pressure must be greater than 4 MPa to open the valve.**Example Problem 2:**

A hydraulic cylinder with a volume $V = 2 \text{ liters}$ is held by a POCV at a pressure $q_0 = 15 \text{ MPa}$. Calculate the pressure drop $\Delta q$ after a time $t = 5 \text{ minutes}$ due to leakage at a rate $R_{leak} = 3 \text{ ml/min}$, considering the fluid's bulk modulus $\beta = 2 \text{ GPa}$.

First, convert all units to be consistent:

- $V = 2 \text{ liters} = 2 \times 10^{-3} \text{ m}^3$
- $t = 5 \text{ minutes} = 300 \text{ seconds}$
- $R_{leak} = 3 \text{ ml/min} = 3 \times 10^{-6} \text{ m}^3/\text{min} = \frac{3 \times 10^{-6}}{60} \text{ m}^3/\text{s} = 5 \times 10^{-8} \text{ m}^3/\text{s}$
- $\beta = 2 \text{ GPa} = 2 \times 10^9 \text{ Pa}$

Using the pressure decay rate equation:

$\frac{dq}{dt} = -\frac{\beta R_{leak}}{V} = -\frac{(2 \times 10^9 \text{ Pa}) (5 \times 10^{-8} \text{ m}^3/\text{s})}{2 \times 10^{-3} \text{ m}^3} = -50,000 \text{ Pa/s}$

The pressure drop after 5 minutes is:

$\Delta q = \left| \frac{dq}{dt} \right| t = (50,000 \text{ Pa/s}) (300 \text{ s}) = 15 \times 10^6 \text{ Pa} = 15 \text{ MPa}$

Since the initial pressure was 15 MPa, this calculation suggests the cylinder will completely lose pressure. In realistic scenarios, this linear decay model fails as the pressure approaches zero, since leakage is pressure dependent.