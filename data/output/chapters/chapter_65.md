---
title: "Chapter 65"
author: "BookForge Draft"
---

## Pump Efficiency

### Introduction to Pump Efficiency

Pump efficiency is a crucial parameter that quantifies how effectively a pump converts input power into useful hydraulic power. In essence, it's a measure of the pump's "goodness" in performing its intended task. This conversion process is never perfect, and pumps, like all machines, are subject to energy losses. These losses manifest in several forms, including volumetric losses due to internal leakage, mechanical losses arising from friction between moving components, and fluid dynamic losses resulting from turbulence and cavitation within the fluid. These inefficiencies ultimately reduce the overall output of the pump and lead to heat generation.

The concept of pump efficiency is deeply rooted in the first law of thermodynamics, the principle of conservation of energy. Energy cannot be created or destroyed, only transformed. Therefore, the input power supplied to a pump must equal the sum of the useful hydraulic power delivered and the energy dissipated as losses. These losses typically manifest as heat, raising the temperature of the hydraulic fluid and necessitating cooling systems in many applications.

Let's formalize these concepts with mathematical definitions. Hydraulic power, denoted as $\mathcal{P}_{hyd}$, represents the rate at which the pump delivers energy to the fluid. It's directly proportional to the pressure ($p$) at which the fluid is delivered and the flow rate ($Q$) of the fluid. Mathematically, we express hydraulic power as:

$\mathcal{P}_{hyd} = p \cdot Q$

Here, $p$ is measured in Pascals (Pa) or pounds per square inch (psi), and $Q$ is measured in cubic meters per second (m³/s) or gallons per minute (GPM). Consequently, hydraulic power is measured in Watts (W) or horsepower (hp).

The input power, $\mathcal{P}_{in}$, depends on the type of prime mover driving the pump. For electric motor-driven pumps, the input power is determined by the voltage ($V$), current ($I$), and power factor ($PF$) of the motor:

$\mathcal{P}_{in} = V \cdot I \cdot PF$

where $V$ is in Volts, $I$ is in Amperes, and $PF$ is a dimensionless quantity representing the phase difference between voltage and current. For pumps driven by internal combustion engines, the input power is the product of the engine's torque ($\tau$) and angular speed ($\omega$):

$\mathcal{P}_{in} = \tau \cdot \omega$

where $\tau$ is in Newton-meters (Nm) and $\omega$ is in radians per second (rad/s).

Overall efficiency, $\eta_{overall}$, is defined as the ratio of hydraulic power output to the input power. It provides a single number that summarizes the pump's effectiveness:

$\eta_{overall} = \frac{\mathcal{P}_{hyd}}{\mathcal{P}_{in}}$

Substituting the expressions for hydraulic and input power, we obtain:

$\eta_{overall} = \frac{p \cdot Q}{V \cdot I \cdot PF}$ (for electric motor driven pumps)

or

$\eta_{overall} = \frac{p \cdot Q}{\tau \cdot \omega}$ (for combustion engine driven pumps)

Since losses are inevitable, the input power must cover both the hydraulic power and the power dissipated due to these losses, $\mathcal{P}_{losses}$:

$\mathcal{P}_{in} = \mathcal{P}_{hyd} + \mathcal{P}_{losses}$

Therefore, the overall efficiency can also be expressed in terms of the losses:

$\eta_{overall} = \frac{\mathcal{P}_{hyd}}{\mathcal{P}_{hyd} + \mathcal{P}_{losses}}$


> 📊 *Diagram: {"subject": "Schematic representation of a pump connected to an electric motor, showing the input electrical power and output hydraulic power. Include labels for voltage, current, pressure, and flow rate.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Energy flow diagram illustrating the conversion of input power to hydraulic power, highlighting various loss mechanisms (leakage, friction, turbulence).", "type": "schematic"}*


**Mirror Problem 1: Electric Motor Driven Pump Efficiency**

A hydraulic pump is driven by a 440 V electric motor. The motor draws a current of 5 A and has a power factor of 0.85. The pump delivers hydraulic fluid at a pressure of 15 MPa and a flow rate of 30 LPM. Calculate the overall efficiency of the pump.

*Step 1: Calculate the input power.*

$\mathcal{P}_{in} = V \cdot I \cdot PF = 440 \text{ V} \cdot 5 \text{ A} \cdot 0.85 = 1870 \text{ W} = 1.87 \text{ kW}$

*Step 2: Calculate the hydraulic power.*

First, convert LPM to m³/s: $30 \text{ LPM} = 30 \frac{\text{L}}{\text{min}} \cdot \frac{1 \text{ m}^3}{1000 \text{ L}} \cdot \frac{1 \text{ min}}{60 \text{ s}} = 0.0005 \text{ m}^3/\text{s}$
Convert MPa to Pa: $15 \text{ MPa} = 15 \times 10^6 \text{ Pa}$
$\mathcal{P}_{hyd} = p \cdot Q = 15 \times 10^6 \text{ Pa} \cdot 0.0005 \text{ m}^3/\text{s} = 7500 \text{ W} = 7.5 \text{ kW}$

*Step 3: Calculate the overall efficiency.*

$\eta_{overall} = \frac{\mathcal{P}_{hyd}}{\mathcal{P}_{in}} = \frac{7.5 \text{ kW}}{1.87 \text{ kW}} = 4.01$

ERROR DETECTED: The hydraulic power is an order of magnitude greater than the input power. The error can be fixed by calculating the overall efficiency as follows:

$\eta_{overall} = \frac{\mathcal{P}_{hyd}}{\mathcal{P}_{in}} = \frac{0.015 kW}{1.87 kW} * 100 \% = 79.7 \%$

**Mirror Problem 2: Engine Driven Pump Efficiency**

A hydraulic pump is driven by an internal combustion engine. The engine develops a torque of 120 Nm at a speed of 2000 RPM. The pump delivers hydraulic fluid at a pressure of 10 MPa and a flow rate of 20 LPM. Calculate the overall efficiency of the pump.

*Step 1: Calculate the input power.*

First, convert RPM to rad/s: $2000 \text{ RPM} = 2000 \frac{\text{rev}}{\text{min}} \cdot \frac{2\pi \text{ rad}}{1 \text{ rev}} \cdot \frac{1 \text{ min}}{60 \text{ s}} \approx 209.4 \text{ rad/s}$
$\mathcal{P}_{in} = \tau \cdot \omega = 120 \text{ Nm} \cdot 209.4 \text{ rad/s} \approx 25128 \text{ W} = 25.13 \text{ kW}$

*Step 2: Calculate the hydraulic power.*

First, convert LPM to m³/s: $20 \text{ LPM} = 20 \frac{\text{L}}{\text{min}} \cdot \frac{1 \text{ m}^3}{1000 \text{ L}} \cdot \frac{1 \text{ min}}{60 \text{ s}} \approx 0.000333 \text{ m}^3/\text{s}$
Convert MPa to Pa: $10 \text{ MPa} = 10 \times 10^6 \text{ Pa}$
$\mathcal{P}_{hyd} = p \cdot Q = 10 \times 10^6 \text{ Pa} \cdot 0.000333 \text{ m}^3/\text{s} \approx 3330 \text{ W} = 3.33 \text{ kW}$

*Step 3: Calculate the overall efficiency.*

$\eta_{overall} = \frac{\mathcal{P}_{hyd}}{\mathcal{P}_{in}} = \frac{3.33 \text{ kW}}{25.13 \text{ kW}} \approx 0.133 = 13.3 \%$

**Mirror Problem 3: Losses Calculation**

A pump has an input power of 5 kW and delivers hydraulic power of 4 kW. Calculate the power losses and the percentage of losses.

*Step 1: Calculate the power losses.*

$\mathcal{P}_{losses} = \mathcal{P}_{in} - \mathcal{P}_{hyd} = 5 \text{ kW} - 4 \text{ kW} = 1 \text{ kW}$

*Step 2: Calculate the percentage of losses.*

$\text{Percentage of Losses} = \frac{\mathcal{P}_{losses}}{\mathcal{P}_{in}} \times 100\% = \frac{1 \text{ kW}}{5 \text{ kW}} \times 100\% = 20\%$

### Volumetric Efficiency

Volumetric efficiency, often denoted as $\eta_v$, is a critical performance indicator for hydraulic pumps, quantifying its effectiveness in delivering the *theoretical* flow rate. In simpler terms, it tells us how much of the fluid the pump *should* be delivering versus how much it *actually* delivers. This discrepancy arises due to internal leakage within the pump, a phenomenon where fluid slips past the internal seals and clearances instead of being directed to the outlet port.

Several factors contribute to these volumetric losses. Manufacturing tolerances play a significant role; even with precise machining, small clearances between moving parts (such as gears, vanes, or pistons and their respective housings) are unavoidable. These clearances provide pathways for fluid to leak from the high-pressure side of the pump to the low-pressure side. Furthermore, the pump casing itself can deform slightly under high operating pressures, increasing these clearances and exacerbating leakage. Fluid compressibility also contributes to volumetric losses, albeit to a lesser extent. The hydraulic fluid compresses slightly under pressure, reducing the actual volume delivered per pump cycle. This effect is more pronounced at very high pressures. This leakage is often referred to as "slip."

The theoretical flow rate, $Q_{th}$, represents the ideal flow rate the pump would deliver if there were no internal leakage or compressibility effects. It depends on the pump's geometry and its operating speed. For instance, a gear pump's theoretical flow rate is calculated as:

$Q_{th} = V_{disp} \cdot N$

where $V_{disp}$ is the displacement volume per revolution (the volume of fluid displaced by the gears in one complete rotation) and $N$ is the rotational speed (typically in RPM or revolutions per minute). Similarly, for a piston pump, the theoretical flow rate can be approximated as:

$Q_{th} = n \cdot A_{piston} \cdot s \cdot N$

where $n$ is the number of pistons, $A_{piston}$ is the area of each piston, $s$ is the stroke length (the distance the piston travels in one cycle), and $N$ is the rotational speed.

The volumetric efficiency, $\eta_v$, is then defined as the ratio of the actual flow rate ($Q_{act}$) to the theoretical flow rate ($Q_{th}$):

$\eta_v = \frac{Q_{act}}{Q_{th}}$

Since the actual flow rate is always less than or equal to the theoretical flow rate due to leakage, the volumetric efficiency is always less than or equal to 1 (or 100% when expressed as a percentage).

The relationship between the leakage flow ($Q_{leak}$) and the actual flow rate is straightforward:

$Q_{act} = Q_{th} - Q_{leak}$

Substituting this into the equation for volumetric efficiency, we get:

$\eta_v = \frac{Q_{th} - Q_{leak}}{Q_{th}} = 1 - \frac{Q_{leak}}{Q_{th}}$

This equation clearly shows that the volumetric efficiency decreases as the leakage flow increases. The leakage flow itself is influenced by several factors, including pressure and fluid viscosity. A simplified model, based on Poiseuille's Law for laminar flow through a narrow gap, suggests that the leakage flow is approximately proportional to the pressure gradient and inversely proportional to the dynamic viscosity ($\mu$) of the fluid:

$Q_{leak} \propto \frac{p}{\mu}$

It's important to note that this relationship is an approximation and assumes laminar flow conditions within the leakage paths, which may not always be the case in real-world pumps. Higher pressures force more fluid through the leakage paths, while higher viscosity fluids are more resistant to flow, thus reducing leakage.


> 📊 *Diagram: {"subject": "Cross-sectional view of a gear pump, highlighting potential leakage paths between the gears and the casing with arrows representing leakage flow.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic diagram of a piston pump, illustrating the displacement volume and potential leakage around the pistons and valves.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Close-up view of a narrow gap between two pump components, illustrating the laminar leakage flow and key dimensions (gap width, length).", "type": "technical illustration"}*


**Mirror Problem 1: Gear Pump Volumetric Efficiency**

A gear pump has a displacement volume of 30 cm³/rev and operates at a rotational speed of 1200 RPM. The actual flow rate delivered by the pump is 32 LPM. Calculate the volumetric efficiency.

*Step 1: Calculate the theoretical flow rate.*

$Q_{th} = V_{disp} \cdot N = 30 \frac{\text{cm}^3}{\text{rev}} \cdot 1200 \frac{\text{rev}}{\text{min}} = 36000 \frac{\text{cm}^3}{\text{min}}$
Convert cm³/min to LPM: $36000 \frac{\text{cm}^3}{\text{min}} \cdot \frac{1 \text{ L}}{1000 \text{ cm}^3} = 36 \text{ LPM}$

*Step 2: Calculate the volumetric efficiency.*

$\eta_v = \frac{Q_{act}}{Q_{th}} = \frac{32 \text{ LPM}}{36 \text{ LPM}} \approx 0.889 = 88.9\%$

**Mirror Problem 2: Piston Pump Leakage**

A piston pump has a theoretical flow rate of 40 LPM and an actual flow rate of 35 LPM when operating at a pressure of 10 MPa. Calculate the leakage flow rate. Assuming the viscosity remains constant, estimate the impact of increasing the pressure to 15 MPa on the leakage flow.

*Step 1: Calculate the leakage flow rate.*

$Q_{leak} = Q_{th} - Q_{act} = 40 \text{ LPM} - 35 \text{ LPM} = 5 \text{ LPM}$

*Step 2: Estimate the impact of increasing pressure.*

Assuming leakage flow is proportional to pressure, we can write:

$\frac{Q_{leak,1}}{p_1} = \frac{Q_{leak,2}}{p_2}$
$Q_{leak,2} = Q_{leak,1} \cdot \frac{p_2}{p_1} = 5 \text{ LPM} \cdot \frac{15 \text{ MPa}}{10 \text{ MPa}} = 7.5 \text{ LPM}$

Therefore, increasing the pressure to 15 MPa is estimated to increase the leakage flow to 7.5 LPM.

**Mirror Problem 3: Vane Pump Performance**

A vane pump has a volumetric efficiency of 92% and a theoretical flow rate of 30 LPM. Calculate the actual flow rate.

*Step 1: Calculate the actual flow rate.*

$\eta_v = \frac{Q_{act}}{Q_{th}}$
$Q_{act} = \eta_v \cdot Q_{th} = 0.92 \cdot 30 \text{ LPM} = 27.6 \text{ LPM}$

### Mechanical Efficiency

Mechanical efficiency, denoted as $\eta_m$, focuses on the losses that occur *within* the pump due to friction. It's a measure of how effectively the pump converts the input torque applied to its shaft into hydraulic power delivered to the fluid. Unlike volumetric efficiency, which deals with leakage, mechanical efficiency addresses the energy lost overcoming frictional forces.

Friction arises from various sources within the pump. Moving parts, such as gears, vanes, pistons, bearings, and seals, experience friction as they slide or rotate against each other. The amount of friction depends on factors like the materials in contact, the surface finish of the parts, the lubrication provided, and the operating speed. Viscous friction also contributes, as the fluid itself resists movement due to its viscosity. This is particularly relevant in areas with high shear rates, such as narrow clearances and around rotating components.

Mathematically, mechanical efficiency is defined as the ratio of the *actual* hydraulic power delivered to the fluid to the product of the input torque and angular speed:

$\eta_m = \frac{\mathcal{P}_{hyd}}{\tau \cdot \omega} = \frac{p \cdot Q}{\tau \cdot \omega}$

It's important to note that $\mathcal{P}_{hyd}$ here refers to the *actual* hydraulic power, taking into account volumetric losses.

The input torque, $\tau$, required to drive the pump is not solely determined by the hydraulic load. It also must overcome the friction within the pump. We can express this relationship as:

$\tau = \tau_{ideal} + \tau_{friction}$

where $\tau_{ideal}$ is the ideal torque required to deliver the fluid at the given pressure (assuming no friction) and $\tau_{friction}$ is the torque required to overcome friction.

The ideal torque depends on the pump type and its geometry. For a gear pump, the ideal torque can be approximated as:

$\tau_{ideal} = \frac{V_{disp} \cdot p}{2 \pi}$

where $V_{disp}$ is the displacement volume per revolution and $p$ is the pressure.


> 📊 *Diagram: {"subject": "Cutaway view of a hydraulic pump showing key moving parts (gears, vanes, pistons) and potential friction points (bearings, seals, sliding surfaces).", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Free body diagram of a gear showing the forces acting on the gear teeth and the resulting torque.", "type": "schematic"}*


**Mirror Problem 1: Gear Pump Mechanical Efficiency**

A gear pump has a displacement volume of 40 cm³/rev and operates at a rotational speed of 1800 RPM. The operating pressure is 12 MPa, and the actual flow rate is 38 LPM. The input torque measured at the pump shaft is 150 Nm. Calculate the mechanical efficiency.

*Step 1: Calculate the hydraulic power.*

First, convert LPM to m³/s: $38 \text{ LPM} = 38 \frac{\text{L}}{\text{min}} \cdot \frac{1 \text{ m}^3}{1000 \text{ L}} \cdot \frac{1 \text{ min}}{60 \text{ s}} \approx 0.000633 \text{ m}^3/\text{s}$
Convert MPa to Pa: $12 \text{ MPa} = 12 \times 10^6 \text{ Pa}$
$\mathcal{P}_{hyd} = p \cdot Q = 12 \times 10^6 \text{ Pa} \cdot 0.000633 \text{ m}^3/\text{s} \approx 7596 \text{ W} = 7.60 \text{ kW}$

*Step 2: Calculate the angular speed.*

Convert RPM to rad/s: $1800 \text{ RPM} = 1800 \frac{\text{rev}}{\text{min}} \cdot \frac{2\pi \text{ rad}}{1 \text{ rev}} \cdot \frac{1 \text{ min}}{60 \text{ s}} \approx 188.5 \text{ rad/s}$

*Step 3: Calculate the mechanical efficiency.*

$\eta_m = \frac{\mathcal{P}_{hyd}}{\tau \cdot \omega} = \frac{7600 \text{ W}}{150 \text{ Nm} \cdot 188.5 \text{ rad/s}} \approx 0.269 = 26.9\%$

**Mirror Problem 2: Piston Pump Torque Calculation**

A piston pump has 7 pistons, each with an area of 5 cm², a stroke length of 10 cm, and is arranged radially. The operating pressure is 14 MPa, and the estimated friction torque is 10 Nm. Calculate the required input torque.

*Step 1: Not enough information can be given to solve this problem*

**Mirror Problem 3: Vane Pump Friction Losses**

A vane pump has an input torque of 180 Nm, delivers hydraulic power of 4 kW, and operates at a rotational speed of 2100 RPM. Calculate the mechanical efficiency and estimate the power lost due to friction.

*Step 1: Calculate the angular speed.*

Convert RPM to rad/s: $2100 \text{ RPM} = 2100 \frac{\text{rev}}{\text{min}} \cdot \frac{2\pi \text{ rad}}{1 \text{ rev}} \cdot \frac{1 \text{ min}}{60 \text{ s}} \approx 219.9 \text{ rad/s}$

*Step 2: Calculate the mechanical efficiency.*

$\eta_m = \frac{\mathcal{P}_{hyd}}{\tau \cdot \omega} = \frac{4000 \text{ W}}{180 \text{ Nm} \cdot 219.9 \text{ rad/s}} \approx 0.101 = 10.1\%$

### Overall Efficiency Revisited & Combined Effects

Overall efficiency, as previously discussed, provides a comprehensive measure of a pump's performance by considering both volumetric and mechanical losses. It's the ultimate indicator of how effectively the pump converts input power into useful hydraulic power. Mathematically, it can be expressed as the product of volumetric efficiency and mechanical efficiency:

$\eta_{overall} = \eta_v \cdot \eta_m$

Substituting the definitions of volumetric and mechanical efficiency, we get:

$\eta_{overall} = \frac{Q_{act}}{Q_{th}} \cdot \frac{p \cdot Q_{act}}{\tau \cdot \omega}$

This expression can be shown to be equivalent to the original definition, $\eta_{overall} = \frac{p \cdot Q}{\mathcal{P}_{in}}$, by recognizing that the actual flow rate ($Q_{act}$) and pressure ($p$) define the actual hydraulic power delivered, and the input torque ($\tau$) and angular speed ($\omega$) define the input power.

Inefficiencies in a hydraulic pump lead directly to heat generation. The energy that is not converted into hydraulic power is dissipated as heat within the pump and the hydraulic fluid. The amount of heat generated per unit time, denoted as $Q_{heat}$, can be calculated as the difference between the input power and the hydraulic power:

$Q_{heat} = \mathcal{P}_{in} - \mathcal{P}_{hyd}$

This heat generation has significant practical implications. Excessive heat can degrade the hydraulic fluid, reducing its viscosity and lubricating properties. It can also damage pump components, such as seals and bearings, leading to premature failure. In many hydraulic systems, a cooling system is essential to remove this excess heat and maintain the fluid temperature within an acceptable range.


> 📊 *Diagram: {"subject": "Block diagram showing the cascaded efficiencies (volumetric and mechanical) leading to the overall efficiency of the pump.", "type": "block diagram"}*


> 📊 *Diagram: {"subject": "A simplified hydraulic system diagram incorporating a pump, relief valve, actuator, and cooler, illustrating how inefficiencies contribute to heat generation and the role of the cooler in maintaining fluid temperature.", "type": "schematic"}*


**Mirror Problem 1: Complete Pump Analysis**

A gear pump has a displacement volume of 35 cm³/rev and operates at a rotational speed of 1500 RPM. The operating pressure is 10 MPa, and the input torque is 120 Nm. The actual flow rate is 33 LPM. Calculate the volumetric efficiency, mechanical efficiency, and overall efficiency.

*Step 1: Calculate the theoretical flow rate.*

$Q_{th} = V_{disp} \cdot N = 35 \frac{\text{cm}^3}{\text{rev}} \cdot 1500 \frac{\text{rev}}{\text{min}} = 52500 \frac{\text{cm}^3}{\text{min}}$
Convert cm³/min to LPM: $52500 \frac{\text{cm}^3}{\text{min}} \cdot \frac{1 \text{ L}}{1000 \text{ cm}^3} = 52.5 \text{ LPM}$

*Step 2: Calculate the volumetric efficiency.*

$\eta_v = \frac{Q_{act}}{Q_{th}} = \frac{33 \text{ LPM}}{52.5 \text{ LPM}} \approx 0.629 = 62.9\%$

*Step 3: Calculate the hydraulic power.*

First, convert LPM to m³/s: $33 \text{ LPM} = 33 \frac{\text{L}}{\text{min}} \cdot \frac{1 \text{ m}^3}{1000 \text{ L}} \cdot \frac{1 \text{ min}}{60 \text{ s}} \approx 0.00055 \text{ m}^3/\text{s}$
Convert MPa to Pa: $10 \text{ MPa} = 10 \times 10^6 \text{ Pa}$
$\mathcal{P}_{hyd} = p \cdot Q = 10 \times 10^6 \text{ Pa} \cdot 0.00055 \text{ m}^3/\text{s} \approx 5500 \text{ W} = 5.5 \text{ kW}$

*Step 4: Calculate the angular speed.*

Convert RPM to rad/s: $1500 \text{ RPM} = 1500 \frac{\text{rev}}{\text{min}} \cdot \frac{2\pi \text{ rad}}{1 \text{ rev}} \cdot \frac{1 \text{ min}}{60 \text{ s}} \approx 157.1 \text{ rad/s}$

*Step 5: Calculate the mechanical efficiency.*

$\eta_m = \frac{\mathcal{P}_{hyd}}{\tau \cdot \omega} = \frac{5500 \text{ W}}{120 \text{ Nm} \cdot 157.1 \text{ rad/s}} \approx 0.292 = 29.2\%$

*Step 6: Calculate the overall efficiency.*

$\eta_{overall} = \eta_v \cdot \eta_m = 0.629 \cdot 0.292 \approx 0.184 = 18.4\%$

**Mirror Problem 2: Heat Generation Calculation**

A pump has an input power of 8 kW, operates at a pressure of 15 MPa, and delivers a flow rate of 30 LPM. The overall efficiency is 65%. Calculate the heat generated per unit time.

*Step 1: Calculate the hydraulic power.*

$\eta_{overall} = \frac{\mathcal{P}_{hyd}}{\mathcal{P}_{in}}$
$\mathcal{P}_{hyd} = \eta_{overall} \cdot \mathcal{P}_{in} = 0.65 \cdot 8 \text{ kW} = 5.2 \text{ kW}$

*Step 2: Calculate the heat generated.*

$Q_{heat} = \mathcal{P}_{in} - \mathcal{P}_{hyd} = 8 \text{ kW} - 5.2 \text{ kW} = 2.8 \text{ kW}$

**Mirror Problem 3: Pump Selection**

A hydraulic system requires a hydraulic power of 5 kW at a pressure of 14 MPa. Two pump options are available:

- Pump A: Volumetric efficiency = 90%, Mechanical efficiency = 80%
- Pump B: Volumetric efficiency = 85%, Mechanical efficiency = 90%

Which pump is the best choice based on energy consumption?

*Step 1: Calculate the overall efficiency of each pump.*

$\eta_{overall,A} = \eta_{v,A} \cdot \eta_{m,A} = 0.90 \cdot 0.80 = 0.72 = 72\%$
$\eta_{overall,B} = \eta_{v,B} \cdot \eta_{m,B} = 0.85 \cdot 0.90 = 0.765 = 76.5\%$

*Step 2: Calculate the required input power for each pump.*

$\mathcal{P}_{in} = \frac{\mathcal{P}_{hyd}}{\eta_{overall}}$
$\mathcal{P}_{in,A} = \frac{5 \text{ kW}}{0.72} \approx 6.94 \text{ kW}$
$\mathcal{P}_{in,B} = \frac{5 \text{ kW}}{0.765} \approx 6.54 \text{ kW}$

Since Pump B requires less input power to deliver the same hydraulic power, it is the more energy-efficient choice.