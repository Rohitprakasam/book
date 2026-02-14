---
title: "Chapter 57"
author: "BookForge Draft"
---

## 2. Minor Energy Losses

In the analysis of fluid flow through pipes and hydraulic systems, the Darcy-Weisbach equation is often used to calculate the frictional head loss, also known as major losses, which occur due to the friction between the fluid and the pipe walls along straight sections. However, real-world hydraulic systems are rarely composed of solely straight pipes. They invariably include components such as valves, fittings (elbows, tees, couplings), and changes in pipe diameter. These components introduce disturbances to the flow, leading to additional energy dissipation beyond that predicted by the Darcy-Weisbach equation. These additional energy losses are often termed "minor losses," although it is important to recognize that in many practical fluid power applications, the cumulative effect of these "minor" losses can be significant, sometimes even exceeding the major losses due to pipe friction.

It's crucial to understand that these energy losses are not merely a theoretical concern. They directly impact the performance and efficiency of hydraulic systems. They contribute to the overall pressure drop, which dictates the power required to drive the fluid through the system and deliver the necessary pressure and flow at the actuator. Overlooking these losses can lead to undersized pumps, reduced system performance, and increased energy consumption. The dissipation of energy also results in a temperature rise of the hydraulic fluid, which can negatively influence the fluid's viscosity and the performance of seals, potentially causing premature wear and leakage.

The flow patterns within valves and fittings are often highly complex. Changes in flow direction, sudden expansions or contractions, and obstructions within the flow path create regions of flow separation, recirculation, and increased turbulence. These phenomena disrupt the smooth, streamlined flow that is assumed in the derivation of the Darcy-Weisbach equation. The increased turbulence and recirculation lead to increased shear stresses within the fluid and between the fluid and the component walls, ultimately resulting in the conversion of kinetic energy into thermal energy, which is then dissipated as heat. Computational Fluid Dynamics (CFD) and experimental measurements are usually needed to accurately quantify the head loss for a particular fitting, as analytical solutions are difficult to achieve due to the complex geometry and flow phenomena involved.

### 2.1 Minor Losses: Introduction and Theoretical Basis

The determination of energy losses within a fluid system requires a firm grounding in the principles of thermodynamics and fluid mechanics. Central to this discussion is the concept of *head loss* ($h_L$), a surrogate measure of the energy lost per unit weight of fluid. This loss manifests as a reduction in the fluid's pressure head, velocity head, or elevation head. Minor losses, therefore, contribute directly to the overall pressure drop across a hydraulic system, diminishing the system's capacity to perform work at the desired location.

We can formally establish the relationship between head loss and energy dissipation by invoking the Work-Energy Theorem, which states that the change in kinetic energy ($\Delta KE$) plus the change in potential energy ($\Delta PE$) of a system is equal to the work done *on* the system ($W_{in}$) minus the work done *by* the system to overcome losses ($W_{loss}$):

$\Delta KE + \Delta PE = W_{in} - W_{loss}$

In a hydraulic system, the work done *on* the system is primarily due to the pressure exerted by the pump. This work can be expressed as the integral of pressure ($p$) with respect to volume ($V$):

$W_{in} = \int p dV$

The work done to overcome losses, $W_{loss}$, is related to the head loss, $h_L$.  The relationship is derived as follows:

$W_{loss} = \dot{m} g h_L dt$

where $\dot{m}$ is the mass flow rate, $g$ is the acceleration due to gravity, and $dt$ is the time increment. This equation expresses the rate at which energy is being dissipated due to frictional effects and flow disturbances.

Combining these concepts, it can be shown that the head loss due to minor losses can be empirically expressed in the following form:

$h_L = K \frac{z^2}{2m}$

where:

- $h_L$ represents the head loss due to the fitting or valve (measured in meters or feet).
- $K$ is the dimensionless *K-factor* or loss coefficient, which characterizes the resistance to flow caused by the specific fitting or valve. It is determined experimentally.
- $z$ is the average flow velocity of the fluid upstream or downstream of the fitting (measured in meters per second or feet per second).
- $m$ is the acceleration due to gravity (approximately 9.81 m/s² or 32.2 ft/s²).

The K-factor is a crucial parameter because it encapsulates the complex flow behavior within the fitting. It accounts for the energy dissipation associated with flow separation, recirculation, and turbulence. Because of its empirical nature, the K-factor is usually provided by the manufacturer of the fitting or valve.


> 📊 *Diagram: {"subject": "Schematic of a hydraulic line with various fittings (elbow, tee, valve) labeled. Arrows indicate flow direction. Include pressure taps before and after the fittings to illustrate pressure drop measurement.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Cutaway view of a generic valve, highlighting the flow path and areas of flow constriction and expansion.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Illustration of flow separation and recirculation behind a sudden expansion in a pipe.", "type": "technical illustration"}*


**Example Problems:Problem 1: Single Fitting Pressure Drop**A hydraulic system using oil with a density ($\rho$) of 850 kg/m³ flows through a 90-degree elbow with a K-factor of 0.9. The flow rate ($Q$) is 30 L/min through a pipe with an inner diameter of 25mm. Calculate the pressure drop across the elbow. Assume the viscosity is within the typical range of hydraulic oils.**Solution:**1.**Convert flow rate to m³/s:**$Q = 30 \frac{L}{min} * \frac{1 m^3}{1000 L} * \frac{1 min}{60 s} = 0.0005 m^3/s$

2.**Calculate the cross-sectional area of the pipe:**$A = \pi * (D/2)^2 = \pi * (0.025 m/2)^2 = 0.0004909 m^2$

3.**Calculate the average flow velocity:**$z = Q / A = 0.0005 m^3/s / 0.0004909 m^2 = 1.0185 m/s$

4.**Calculate the head loss:**$h_L = K * \frac{z^2}{2m} = 0.9 * \frac{(1.0185 m/s)^2}{2 * 9.81 m/s^2} = 0.0473 m$

5.**Calculate the pressure drop:**$\Delta p = \rho * m * h_L = 850 kg/m^3 * 9.81 m/s^2 * 0.0473 m = 394.9 Pa$

Therefore, the pressure drop across the 90-degree elbow is approximately 394.9 Pascals.**Problem 2: Series of Fittings**A 1-inch diameter (D = 0.0254 m) hydraulic line contains a gate valve (¾ open, K = 0.9), two 45-degree elbows (K = 0.42 each), and a standard tee (K = 1.8). The flow rate of the hydraulic fluid is 40 L/min. Assuming the fluid has a density of 900 kg/m³, calculate the total head loss due to these fittings.**Solution:**1.**Calculate total K-factor:**$K_{total} = K_{gate\ valve} + 2 * K_{45\ degree\ elbow} + K_{tee} = 0.9 + 2*0.42 + 1.8 = 3.54$

2.**Convert flow rate to m³/s:**$Q = 40 \frac{L}{min} * \frac{1 m^3}{1000 L} * \frac{1 min}{60 s} = 0.000667 m^3/s$

3.**Calculate the cross-sectional area of the pipe:**$A = \pi * (D/2)^2 = \pi * (0.0254 m/2)^2 = 0.0005067 m^2$

4.**Calculate the average flow velocity:**$z = Q / A = 0.000667 m^3/s / 0.0005067 m^2 = 1.316 m/s$

5.**Calculate the total head loss:**$h_L = K_{total} * \frac{z^2}{2m} = 3.54 * \frac{(1.316 m/s)^2}{2 * 9.81 m/s^2} = 0.3136 m$

Therefore, the total head loss due to these fittings is approximately 0.3136 meters.

### 2.2 Minor Losses in Specific Valves and Fittings

The K-factor, as established, represents the dimensionless loss coefficient associated with a given valve or fitting. However, the magnitude of this factor is highly dependent on the specific geometry and internal design of the component. This section delves deeper into the physical mechanisms that give rise to different K-factors for common valves and fittings.**Valves:**-**Globe Valves:**Globe valves are characterized by a tortuous flow path with significant changes in direction. When fully open, the fluid must make two near 90-degree turns. This geometry creates considerable flow resistance, resulting in a high K-factor (typically around 10 for a wide-open globe valve). Partially closing the valve further restricts the flow, increasing the K-factor substantially. The throttling action causes significant turbulence and pressure drop.

-**Gate Valves:**Gate valves, on the other hand, offer a much more streamlined flow path when fully open. The gate retracts fully into the valve body, leaving a relatively unobstructed passage. Consequently, the K-factor for a fully open gate valve is quite low (around 0.19). However, partially closing a gate valve creates a sharp-edged orifice, leading to significant flow contraction and expansion, resulting in a substantial increase in the K-factor. Gate valves are not well-suited for throttling applications due to the high turbulence and potential for cavitation at partial openings.

-**Ball Valves:**Ball valves provide a relatively straight and unobstructed flow path when fully open, similar to gate valves. The K-factor for a fully open ball valve is generally low. The spherical ball with a circular port aligns with the pipe bore, minimizing flow disturbances.

-**Check Valves:**Check valves are designed to allow flow in only one direction. The K-factor depends on the specific type of check valve (e.g., swing check, ball check, lift check). Ball check valves, for example, tend to have higher K-factors than swing check valves due to the flow restriction caused by the ball and its seat.


> 📊 *Diagram: {"subject": "Cross-sectional diagrams of globe valve, gate valve, ball valve, and check valve, showing the flow path in each valve and highlighting the areas of flow restriction.", "type": "technical illustration"}*

**Pipe Fittings:**-**Elbows:**Elbows introduce a change in flow direction, causing flow separation and the formation of secondary flows. The K-factor depends on the bend radius and the angle of the elbow. A sharp 90-degree elbow has a higher K-factor than a long-radius 90-degree elbow because the sharper bend promotes greater flow separation. A 45-degree elbow has a lower K-factor than a 90-degree elbow due to the smaller change in flow direction.

-**Tees:**Tees introduce a division or combination of flow streams, leading to complex flow patterns and significant energy losses. The K-factor for a tee depends on whether the flow is entering or exiting the branch. A tee used to split the flow (flow entering the main run and exiting the branch) generally has a higher K-factor than a tee used to combine the flow (flow entering the branch and the main run and exiting the combined run).


> 📊 *Diagram: {"subject": "Illustration of flow patterns in a 90-degree elbow and a 45-degree elbow, showing the formation of secondary flows and flow separation.", "type": "technical illustration"}*

**Equivalent Length:**

An alternative approach to quantifying minor losses is through the concept of *equivalent length* ($L_e$). The equivalent length represents the length of straight pipe that would produce the same head loss as the fitting under the same flow conditions. This approach allows us to treat the minor losses as if they were additional frictional losses in a straight pipe, simplifying the overall head loss calculation.

The relationship between the K-factor and the equivalent length can be derived by equating the head loss calculated using the K-factor method with the head loss calculated using the Darcy-Weisbach equation:

$h_L = f \frac{L_e}{D} \frac{z^2}{2m} = K \frac{z^2}{2m}$

Solving for $L_e$, we get:

$L_e = \frac{KD}{f}$

where:

- $f$ is the Darcy friction factor, which depends on the Reynolds number and the relative roughness of the pipe.
- $D$ is the inner diameter of the pipe.

The friction factor, $f$, can be determined using the Moody chart or the Colebrook equation, depending on the flow regime (laminar or turbulent). For turbulent flow, the Colebrook equation is commonly used:

$\frac{1}{\sqrt{f}} = -2.0 \log_{10} \left( \frac{\epsilon}{3.7D} + \frac{2.51}{Re \sqrt{f}} \right)$

where:

- $\epsilon$ is the absolute roughness of the pipe wall.
- $Re$ is the Reynolds number, defined as $Re = \frac{\rho z D}{\mu}$.


> 📊 *Diagram: {"subject": "Moody chart with example operating point highlighted to visually determine friction factor.", "type": "graph"}*


**Example Problems:Problem 1: Equivalent Length**A 1.5-inch diameter pipe contains a globe valve (wide open). The K-factor for the valve is 10. Assuming a friction factor of 0.02, calculate the equivalent length of the valve.**Solution:**1.**Convert diameter to feet:**D = 1.5 inches = 1.5/12 feet = 0.125 feet
2.**Calculate the equivalent length:**$L_e = \frac{KD}{f} = \frac{10 * 0.125 \ feet}{0.02} = 62.5 \ feet$

Therefore, the equivalent length of the globe valve is 62.5 feet.**Problem 2: Pressure Drop Comparison**A hydraulic system can be configured with either a standard elbow (K = 0.9) or a 45-degree elbow (K=0.42). Given the flow rate is 25 L/min, fluid density is 870 kg/m3, dynamic viscosity 0.08 Pa.s, and pipe diameter is 20mm, calculate and compare the pressure drop for each configuration.**Solution:**

First, calculate the flow velocity:
$Q = 25 \frac{L}{min} * \frac{1 m^3}{1000 L} * \frac{1 min}{60 s} = 0.000417 m^3/s$
$A = \pi * (0.02m/2)^2 = 0.000314 m^2$
$z = 0.000417 / 0.000314 = 1.328 m/s$

Next, calculate the pressure drop with a standard elbow:
$h_L = K \frac{z^2}{2g} = 0.9 \frac{1.328^2}{2 * 9.81} = 0.0805 m$
$\Delta p = \rho g h_L = 870 * 9.81 * 0.0805 = 687 Pa$

Next, calculate the pressure drop with a 45-degree elbow:
$h_L = K \frac{z^2}{2g} = 0.42 \frac{1.328^2}{2 * 9.81} = 0.0376 m$
$\Delta p = \rho g h_L = 870 * 9.81 * 0.0376 = 321.5 Pa$

Therefore, using a 45-degree elbow yields a significantly lower pressure drop than a standard elbow.

### 2.3 Pumping Theory: Fundamentals and Components

Pumps are at the heart of any hydraulic system, serving as the prime movers that convert mechanical energy into fluid power. This conversion is achieved by increasing the pressure and flow rate of the hydraulic fluid, enabling it to perform work at the desired location.

At its core, pumping theory revolves around the fundamental distinction between *positive displacement* and *non-positive displacement* pumps. Understanding this difference is crucial for selecting the appropriate pump for a given application.

- **Positive Displacement Pumps:**These pumps operate by trapping a fixed volume of fluid and mechanically forcing (displacing) it into the discharge line. Each cycle of the pump delivers the same amount of fluid, regardless of the pressure. Examples include gear pumps, vane pumps, and piston pumps. Because the volume is fixed, small changes in backpressure have minimal effect on flow rate. Positive displacement pumps are self-priming, meaning that they do not need to be filled with fluid before starting. They can handle viscous fluids and high pressures effectively.

-**Non-Positive Displacement Pumps:**These pumps, also known as hydrodynamic pumps, impart kinetic energy to the fluid, which is then converted into pressure. The flow rate depends on the pump speed and the system resistance. Centrifugal pumps are the most common type of non-positive displacement pump. They are generally used for high-volume, low-pressure applications. Backpressure significantly affects flow rate; increased resistance in the system will dramatically decrease flow rate. Because they depend on fluid inertia to operate, these pumps usually require priming.


> 📊 *Diagram: {"subject": "Schematic of a basic hydraulic pumping system, showing the pump, reservoir, suction line, discharge line, pressure gauge, and flow meter.", "type": "schematic"}*

**Key Performance Parameters:**-**Flow Rate (Q):**The volume of fluid delivered by the pump per unit time (e.g., liters per minute, gallons per minute).
-**Pressure (p):**The force exerted by the fluid per unit area (e.g., Pascals, pounds per square inch).
-**Power (𝒫):**The rate at which the pump performs work (e.g., Watts, horsepower).
-**Efficiency (η):**The ratio of useful power output to power input. It reflects the pump's ability to convert mechanical energy into fluid power effectively. Several types of efficiency are important:
    -**Volumetric Efficiency (ηv):**The ratio of actual flow rate to theoretical flow rate. It accounts for internal leakage within the pump.
    -**Mechanical Efficiency (ηm):**The ratio of hydraulic power output to mechanical power input. It accounts for mechanical losses due to friction within the pump.
    -**Overall Efficiency (ηo):**The product of volumetric and mechanical efficiencies. It represents the overall performance of the pump.**Pump Power:**Pump power ($\mathcal{P}$) is directly proportional to the pressure ($p$) and flow rate ($Q$) of the fluid:

$\mathcal{P} = p Q$

In SI units, pressure is measured in Pascals (Pa) and flow rate in cubic meters per second (m³/s), resulting in power in Watts (W). In US customary units, pressure is typically measured in pounds per square inch (psi) and flow rate in gallons per minute (gpm), which requires a conversion factor to obtain power in horsepower (hp).**Pump Efficiencies:**-**Volumetric Efficiency (ηv):**$\eta_v = \frac{Q_{actual}}{Q_{theoretical}}$

-**Mechanical Efficiency (ηm):**$\eta_m = \frac{p Q}{\mathcal{T} \omega}$

    where:
    - $\mathcal{T}$ is the torque applied to the pump shaft.
    - $\omega$ is the angular velocity of the pump shaft.

-**Overall Efficiency (ηo):**$\eta_o = \eta_v \eta_m$


> 📊 *Diagram: {"subject": "Cutaway view of a gear pump, vane pump, and piston pump, showing their internal components and operating principles.", "type": "technical illustration"}*

**Example Problems:Problem 1: Pump Power Calculation**A hydraulic pump delivers oil at a flow rate of 30 L/min and a pressure of 15 MPa. Calculate the hydraulic power output of the pump.**Solution:**1.**Convert flow rate to m³/s:**$Q = 30 \frac{L}{min} * \frac{1 m^3}{1000 L} * \frac{1 min}{60 s} = 0.0005 m^3/s$

2.**Convert pressure to Pascals:**$p = 15 \ MPa = 15 * 10^6 \ Pa$

3.**Calculate hydraulic power:**$\mathcal{P} = pQ = (15 * 10^6 \ Pa) * (0.0005 \ m^3/s) = 7500 \ W = 7.5 \ kW$

Therefore, the hydraulic power output of the pump is 7.5 kW.**Problem 2: Efficiency Calculation**A hydraulic pump has a theoretical flow rate of 40 L/min. The actual flow rate is 38 L/min, and the mechanical power input is 7.5 kW. If the pump is operating at 10 MPa, calculate the volumetric efficiency, mechanical efficiency, and overall efficiency.**Solution:**1.**Convert flow rates to consistent units (m³/s):**$Q_{theoretical} = 40 \frac{L}{min} \times \frac{1 m^3}{1000 L} \times \frac{1 min}{60 s} = 0.000667 m^3/s$
    $Q_{actual} = 38 \frac{L}{min} \times \frac{1 m^3}{1000 L} \times \frac{1 min}{60 s} = 0.000633 m^3/s$

2.**Convert pressure to Pascals:**$p = 10 \ MPa = 10 \times 10^6 \ Pa$

3.**Calculate Volumetric Efficiency:**$\eta_v = \frac{Q_{actual}}{Q_{theoretical}} = \frac{0.000633 m^3/s}{0.000667 m^3/s} = 0.949 = 94.9 \%$

4.**Calculate Mechanical Efficiency:**$\eta_m = \frac{p Q_{actual}}{\mathcal{P}_{input}} = \frac{(10 \times 10^6 \ Pa) \times (0.000633 m^3/s)}{7500 \ W} = \frac{6330 W}{7500 W} = 0.844 = 84.4 \%$

5.**Calculate Overall Efficiency:**$\eta_o = \eta_v \eta_m = 0.949 \times 0.844 = 0.801 = 80.1 \%$

Therefore: volumetric efficiency is 94.9%, mechanical efficiency is 84.4% and overall efficiency is 80.1%.

### 2.4 Pump Classification: Dynamic vs. Positive Displacement Pumps

The fluid power industry broadly categorizes pumps into two primary classes: dynamic (non-positive displacement) and positive displacement pumps. As previously introduced, these classes are distinguished by their fundamental operating principles and resulting performance characteristics. Selecting the appropriate pump type is a critical decision in hydraulic system design, influencing the system's pressure and flow capabilities, efficiency, and overall suitability for the intended application.**Dynamic (Non-Positive Displacement) Pumps:**These pumps impart kinetic energy to the fluid, which is subsequently converted into pressure. Centrifugal pumps are the most common example. The main feature of centrifugal pumps is a rotating impeller housed within a volute casing.

-**Operating Principle:**The impeller accelerates the fluid radially outward, increasing its kinetic energy. The volute casing then gradually converts this kinetic energy into pressure as the fluid decelerates and expands.
-**Characteristics:**- Relatively low pressure capability (typically up to 250-300 psi, although multi-stage centrifugal pumps can achieve higher pressures).
    - High flow rate capacity.
    - Pressure and flow rate are inversely proportional: Increased resistance in the system will dramatically decrease flow rate.
    - Lower viscosity fluid is generally necessary
    - Generally less efficient than positive displacement pumps, particularly at high pressures.**Positive Displacement Pumps:**These pumps operate by trapping a fixed volume of fluid within an enclosed chamber and mechanically displacing it into the discharge line. The flow rate is directly proportional to the pump speed and the displacement volume. Several types of positive displacement pumps are commonly used in hydraulic systems:

-**Gear Pumps:**These pumps use rotating gears to trap and displace fluid. External gear pumps are the simplest and most common type.

    -**Operating Principle:**As the gears rotate, fluid is drawn into the spaces between the gear teeth and carried around the periphery of the gears to the discharge port.
    -**Characteristics:**- Relatively simple and inexpensive.
        - Moderate pressure capability (up to 3000 psi).
        - Good tolerance for contamination.
        - Can be noisy at high speeds.

-**Vane Pumps:**These pumps use rotating vanes that slide in and out of slots in a rotor to trap and displace fluid.

    -**Operating Principle:**As the rotor rotates, the vanes are forced outward by centrifugal force, creating sealed chambers that carry fluid from the suction port to the discharge port.
    -**Characteristics:**- Higher pressure capability than gear pumps (up to 4000 psi).
        - Quieter operation than gear pumps.
        - More sensitive to contamination than gear pumps.

-**Piston Pumps:**These pumps use reciprocating pistons to trap and displace fluid. Axial piston pumps and radial piston pumps are two common types.

    -**Operating Principle:**The pistons move in and out of cylinders, drawing fluid in during the suction stroke and pushing it out during the discharge stroke.
    -**Characteristics:**- Highest pressure capability (up to 10,000 psi or higher).
        - High efficiency.
        - More complex and expensive than gear and vane pumps.
        - Very sensitive to contamination.


> 📊 *Diagram: {"subject": "Cross-sectional diagram of a centrifugal pump, showing the impeller, volute, and diffuser.", "type": "technical illustration"}*

**Theoretical Head Developed by a Centrifugal Pump**The theoretical head ($H$) developed by a centrifugal pump can be estimated using Euler's pump equation:

$H = \frac{1}{m}(v_{e2}n_2 - v_{e1}n_1)$

Where:
- $v_{e2}$ is the whirl velocity at the impeller outlet
- $n_2$ is the blade speed at the impeller outlet
- $v_{e1}$ is the whirl velocity at the impeller inlet
- $n_1$ is the blade speed at the impeller inlet
- $m$ is the acceleration due to gravity


> 📊 *Diagram: {"subject": "Velocity triangles at the inlet and outlet of a centrifugal pump impeller.", "type": "schematic"}*

**Example Problems:Problem 1: Centrifugal Pump Head Calculation**A centrifugal pump has an impeller with an outer diameter of 200 mm and an inner diameter of 100 mm. The impeller rotates at 1750 RPM. The blade angle at the outlet is 30 degrees. Assuming the fluid enters the impeller radially (v_e1 = 0) and the whirl velocity at the outlet is 20 m/s, calculate the theoretical head developed by the pump.**Solution:**

1.  Convert impeller diameters to meters:
    Outer diameter: D2 = 200 mm = 0.2 m
    Inner diameter: D1 = 100 mm = 0.1 m

2.  Calculate blade speed at the outlet:
    n2 = π * D2 * N / 60 = π * 0.2 m * 1750 RPM / 60 = 18.33 m/s

3.  Apply Euler's pump equation:
    H = (1/g) * (ve2 * n2 - ve1 * n1) = (1/9.81 m/s^2) * (20 m/s * 18.33 m/s - 0) = 37.37 m

Therefore, the theoretical head developed by the centrifugal pump is approximately 37.37 meters.

**Problem 2: Positive Displacement Pump Flow Rate**A gear pump has a displacement volume of 12 cm3/revolution. If the pump is operating at 1100 RPM, calculate the theoretical flow rate. If the volumetric efficiency is 93%, what is the actual flow rate?**Solution:**

1.  Convert displacement volume to m³/revolution:
    Vd = 12 cm³/revolution = 12 * 10^-6 m³/revolution

2.  Convert pump speed to revolutions per second (rev/s):
    N = 1100 RPM = 1100/60 rev/s = 18.33 rev/s

3.  Calculate theoretical flow rate:
    Q_theoretical = Vd * N = (12 * 10^-6 m³/revolution) * (18.33 rev/s) = 0.00022 m³/s

4.  Convert to liters per minute:
    Q_theoretical = 0.00022 m³/s * (1000 L/m³) * (60 s/min) = 13.2 L/min

5.  Calculate actual flow rate:
    Q_actual = Q_theoretical * ηv = 13.2 L/min * 0.93 = 12.28 L/min

Therefore, the theoretical flow rate is 13.2 L/min and the actual flow rate is 12.28 L/min.