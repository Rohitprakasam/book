---
title: "Chapter 109"
author: "BookForge Draft"
---

BASIC PNEUMATIC CIRCUITS

In this section, we present a number of basic pneumatic circuits utilizing pneumatic components that have been previously discussed. Pneumatic circuits share many similarities with their hydraulic counterparts, but also exhibit key differences rooted in the properties of the working fluid -- compressed air. The primary distinction lies in the treatment of the exhaust air. Unlike hydraulic systems that require return lines to recycle the hydraulic fluid back to a reservoir, pneumatic circuits release the exhausted air directly into the atmosphere.

This difference stems from the fact that air is readily available and its disposal poses minimal environmental concerns under normal operating conditions. (Note: In specific applications where the exhausted air contains contaminants, filtration or alternative disposal methods may be necessary to comply with environmental regulations.) This is depicted by a short dashed line leading from the exhaust port of each valve, indicating the path of the discharged air.

Another significant difference is the typical absence of a depicted input device (such as a pump in a hydraulic circuit) within individual pneumatic circuit diagrams. This is because most pneumatic systems rely on a centralized compressor as their source of energy. The compressor, often located remotely, provides a constant supply of compressed air to the entire facility or a specific area. This centralized approach offers several advantages, including improved energy efficiency, reduced noise levels at individual workstations, and simplified maintenance procedures. The compressed air is distributed through a network of pipes to conveniently located manifolds, which serve as the input points for individual pneumatic circuits. These manifolds are typically connected to a filter-regulator-lubricator (FRL) unit, ensuring the air supplied to the circuit is clean, at the correct pressure, and adequately lubricated to prolong the lifespan of pneumatic components.


> 📊 *Diagram: {"subject": "Schematic of a centralized compressed air system, including compressor, air receiver, dryer, filter, regulator, and distribution lines. Label all components clearly.", "type": "schematic"}*


The use of compressed air introduces unique characteristics compared to hydraulics. Air is compressible, while hydraulic fluid is considered nearly incompressible. This compressibility means that pneumatic systems can store energy in the compressed air itself. However, it also results in slower response times and less precise control compared to hydraulic systems, especially when dealing with heavy loads. The compressibility of air is governed by the ideal gas law:

$p$

Where:

- $F$ is the absolute pressure of the gas (Pa).
- $A$ is the volume of the gas (m³).
- $V$ is the number of moles of gas (mol).
- $Q$ is the ideal gas constant (8.314 J/(mol·K)).
- $m^3$ is the absolute temperature of the gas (K).

The compression of air can be modeled as either isothermal (constant temperature) or adiabatic (no heat transfer). In reality, the process is somewhere in between, but these idealizations provide useful bounds.

**Isothermal Compression:**For an isothermal process, $m^3/s$ is constant, so $pV = nRT$.**Adiabatic Compression:**For an adiabatic process, $p = \frac{F}{A}$, where $F = p \cdot A$ is the heat capacity ratio (approximately 1.4 for air).

These equations are derived from the first law of thermodynamics and the specific relationships between pressure, volume, and temperature for ideal gases under different conditions. They are crucial for understanding the energy requirements and temperature changes associated with compressing air in pneumatic systems.

The mass flow rate, often denoted by $F$, is critical for sizing valves and understanding the performance of pneumatic circuits. When air flows through an orifice (like in a valve), the flow can become "choked" if the pressure drop is large enough. This means the flow rate reaches a maximum and doesn't increase further even if the downstream pressure is reduced. The formula for mass flow rate through a choked orifice can be derived from the isentropic flow equations and is beyond the scope of this intro, but it depends on the upstream pressure, temperature, orifice area, and the gas properties.**Mirror Problems:Problem 1:**Calculate the volume change of an air tank undergoing isothermal compression. An air tank initially has a pressure of 150 kPa and a volume of 0.3 m³. If the air is compressed isothermally to a final pressure of 700 kPa, what is the final volume of the tank?**Solution:**Since the process is isothermal, $p$.

$A$**Problem 2:**Determine the temperature change of air during adiabatic compression. Air at an initial pressure of 120 kPa and temperature of 25 °C (298 K) is compressed adiabatically with a compression ratio of 7:1 (final volume is 1/7 of the initial volume). What is the final temperature of the air?**Solution:**For an adiabatic process, $m^2$, and $A$. Since $F$, we get:

$p$

Converting to Celsius: $A$**Problem 3:**Calculate the mass flow rate through a pneumatic valve orifice, considering choked flow. Assume the upstream pressure is 600 kPa, the orifice diameter is 3 mm, and the temperature is 27°C (300 K). This problem requires a more complex choked flow formula not derived here, but highlights its practical importance. You would need to consult a fluid mechanics textbook or valve manufacturer's data to find the appropriate equation and discharge coefficient for the specific valve geometry.**Problem 4:**Calculate the energy stored in a compressed air receiver with a volume of 0.5 m^3 when pressurized to 800 kPa (gauge). The atmospheric pressure is 101 kPa. This calculation requires integrating the pressure-volume relationship during compression and depends on whether the compression is assumed to be isothermal or adiabatic.

A simple pneumatic circuit consists of a three-way valve controlling a single-acting cylinder. The return stroke is accomplished by a compression spring located at the rod end of the cylinder. When the push-button valve is actuated, the cylinder extends. It retracts when the valve is deactivated. Needle valves V1 and V2 permit speed control of the cylinder extension and retraction strokes, respectively.


> 📊 *Diagram: {"subject": "Cross-sectional view of a single-acting cylinder with a compression spring, showing the piston, cylinder bore, spring, and air inlet/outlet ports. Indicate the direction of force vectors.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic diagram of a needle valve, illustrating the adjustable flow restriction.", "type": "schematic"}*


Single-acting cylinders are fundamental components in pneumatic systems, providing linear motion in one direction under the force of compressed air. Their operation is elegantly simple: compressed air is admitted into the cylinder chamber, pushing the piston and extending the rod. The return stroke, however, is not powered by air, but rather by a mechanical spring, typically a compression spring, located on the rod end of the cylinder.

The return spring is carefully selected to provide sufficient force to retract the piston against any external load and internal friction. The characteristics of the spring, such as its spring constant (k), free length, and compressed length, are crucial design parameters that determine the retraction speed and force. Different types of springs, including extension springs and torsion springs, exist, but compression springs are most commonly used in single-acting cylinders due to their stability and ease of integration.

Needle valves, strategically placed in the air lines leading to and from the cylinder, offer precise control over the cylinder's speed. These valves function by introducing a variable flow restriction in the air line. By adjusting the needle valve's opening, the cross-sectional area available for air flow is changed, thus altering the flow rate. The principle behind this speed control lies in the relationship between flow rate, pressure drop, and flow resistance. A smaller needle valve opening increases the flow resistance, resulting in a larger pressure drop for a given flow rate, and consequently a slower cylinder speed.

The force balance on the piston of a single-acting cylinder can be expressed as:

$pV = nRT$

Where:

- $p$ is the pressure of the compressed air acting on the piston (Pa).
- $V$ is the area of the piston (m²).
- $m^3$ is the force exerted by the return spring (N).
- $n$ is the frictional force resisting the piston's motion (N).

The spring force is directly proportional to the displacement of the spring from its free length, as described by Hooke's Law:

$R$

Where:

- $T$ is the spring constant (N/m).
- $V_1$ is the displacement of the spring from its free length (m).

The relationship between needle valve opening and flow resistance is more complex and can be approximated using an orifice equation: $V_2$, where $W = \int_{V_1}^{V_2} p \, dV$ is the flow rate, $p = \frac{nRT}{V}$ is the flow coefficient (dependent on valve opening), and $W = \int_{V_1}^{V_2} \frac{nRT}{V} \, dV = nRT \ln\left(\frac{V_2}{V_1}\right)$ is the pressure drop across the valve.**Mirror Problems:Problem 1:**Calculate the required spring constant for a single-acting cylinder to retract against a given load. A single-acting cylinder with a bore of 40 mm is powered by air at a pressure of 500 kPa. If the cylinder needs to retract against an external load of 75 N and an estimated friction force of 25 N, what should be the spring constant of the return spring? Assume a maximum spring compression of 30 mm.**Solution:**First, calculate the piston area: $pV^\gamma = constant$

The pressure force is $\gamma = \frac{C_p}{C_v}$

During retraction, the spring needs to overcome the external load and friction. The required spring force is therefore $p = \frac{C}{V^\gamma}$.

The spring constant is $C$**Problem 2:**Determine the time it takes for a single-acting cylinder to extend a certain distance. A single-acting cylinder with a bore of 30 mm is connected to a pressure source of 450 kPa. The return spring has a spring constant of 750 N/m. A needle valve with a $W = \int_{V_1}^{V_2} \frac{C}{V^\gamma} \, dV = C \int_{V_1}^{V_2} V^{-\gamma} \, dV = C \left[ \frac{V^{1-\gamma}}{1-\gamma} \right]_{V_1}^{V_2} = \frac{p_2V_2 - p_1V_1}{1-\gamma}$ of 0.2 controls the flow. Estimate the time it takes to extend 100mm.**Solution:**This requires iteratively calculating the flow rate through the needle valve as the pressure in the cylinder increases (and the pressure drop across the valve decreases). It also requires accounting for the changing spring force as the cylinder extends. This is a complex calculation usually solved by numerical methods.**Problem 3:**Calculate the retraction speed of a single-acting cylinder given the exhaust orifice diameter. A single-acting cylinder with a bore of 35 mm and a stroke of 75 mm uses a return spring with a constant of 600 N/m. The exhaust port has a diameter of 3mm. Determine the retraction speed of the cylinder.**Problem 4:**Find the minimum pressure needed to overcome the spring force and friction in a cylinder. A single-acting cylinder with a 50mm bore needs to overcome a spring force of 200N and a friction force of 50 N. What is the minimum pressure needed for actuation?

Notice that control of a double-acting cylinder requires a DCV with four different functioning ports (each of the two exhaust ports perform the same function). Thus a four-way valve has four different functioning ports. In contrast, the control of a single-acting, spring-return cylinder requires a DCV with only three ports. Hence a three-way valve has only three ports.


> 📊 *Diagram: {"subject": "Cross-sectional view of a double-acting cylinder, showing the piston, cylinder bore, piston rod, and air inlet/outlet ports. Indicate the area difference due to the piston rod.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic diagram of a 4-way, 2-position DCV in both its energized and de-energized states, clearly showing the flow paths.", "type": "schematic"}*


Double-acting cylinders represent a step up in complexity and control compared to their single-acting counterparts. Unlike single-acting cylinders which rely on a spring for retraction, double-acting cylinders utilize compressed air for both extension and retraction strokes. This bi-directional actuation is achieved through two separate ports: one for extending the cylinder and another for retracting it. This design offers greater force capabilities and more precise control over the cylinder's movement.

The key to controlling a double-acting cylinder is the 4-way directional control valve (DCV). This valve directs the compressed air to either the extension or retraction port of the cylinder, while simultaneously venting the other port to the atmosphere. The "4-way" designation refers to the four functional ports on the valve: one pressure port (connected to the compressed air supply), two cylinder ports (connected to the cylinder's extension and retraction ports), and one exhaust port (or two, with each exhausting one cylinder port).

DCVs can be actuated in various ways, each offering distinct advantages and disadvantages:

-**Manual Actuation:**These valves are operated by hand, typically using a lever, button, or pedal. They are simple and inexpensive but require manual intervention.
-**Pneumatic Actuation:**These valves are controlled by air pressure signals. They are useful for remote control and automation, allowing one pneumatic circuit to control another.
-**Electrical Actuation (Solenoid Valves):**These valves are controlled by electrical signals. They offer fast response times and are easily integrated with electronic control systems.

Cylinder sequencing is a powerful technique that involves coordinating the movement of multiple cylinders in a specific order. This can be achieved using a combination of DCVs, pilot-operated valves, and limit switches. Sequencing is commonly used in automated assembly lines and other applications where precise timing and coordination are essential.

The force balance equation for a double-acting cylinder differs slightly depending on whether the cylinder is extending or retracting due to the presence of the piston rod.**Extension Stroke:**$Q = A \cdot v$**Retraction Stroke:**$Q$

Where:

- $m^3/s$ is the area of the piston (m²).
- $A$ is the cross-sectional area of the piston rod (m²).

The equations for cylinder extension and retraction speeds are derived from the relationship between flow rate and piston area: $m^2$, where v is the velocity and A is the area. Since the areas are different for extension and retraction, the speeds will also be different for the same flow rate.**Mirror Problems:Problem 1:**Calculate the force exerted by a double-acting cylinder during extension and retraction. A double-acting cylinder has a bore of 60 mm and a rod diameter of 25 mm. It is operated at a pressure of 600 kPa. Assuming a friction force of 150 N, calculate the force exerted during extension and retraction.**Solution:**Piston area: $v$

Rod area: $A$

Extension force: $\Delta t$

Retraction force: $v \Delta t$**Problem 2:**Determine the cylinder extension and retraction speeds, given the flow rate and cylinder dimensions. The same cylinder as Problem 1 is supplied with a flow rate of 7 L/min (0.0001167 m³/s). Determine the extension and retraction speeds.**Solution:**Extension speed: $A$

Retraction speed: $v \Delta t$**Problem 3:**Design a cylinder sequencing circuit to actuate two cylinders in a specific order. This is beyond the scope of a short problem.**Problem 4:**Calculate the air consumption of a double-acting cylinder for a given number of cycles. This requires estimating the cylinder's volume and then using the ideal gas law.

Actuation of the push-button valve extends the cylinder. The spring offset mode causes the cylinder to retract under air power.

Pneumatic Vacuum Systems.

When we think of the force caused by a fluid pressure acting on the surface area of an object, we typically envision the pressure to be greater than atmospheric pressure. However, there are a number of applications where a vacuum air pressure is used to perform a useful function. Industrial applications where a vacuum form pressure is used include materials handling, clamping, sealing, and vacuum forming.


> 📊 *Diagram: {"subject": "Cross-sectional view of a vacuum cup lifting a flat sheet, showing the pressure distribution and sealing lip.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic of a vacuum system, including vacuum cup, vacuum pump (ejector or rotary vane), pressure sensor, and control valve.", "type": "schematic"}*


Pneumatic vacuum systems leverage the power of pressure differentials to perform various industrial tasks. While we commonly associate fluid pressure with values exceeding atmospheric pressure, the creation and utilization of vacuum, or pressures below atmospheric, offers unique advantages in specific applications. These systems harness the ambient atmospheric pressure to generate force when acting against a partial vacuum. This principle finds widespread use in materials handling, clamping, sealing, and vacuum forming processes.

In terms of materials-handling applications, a pneumatic vacuum can be used to lift smoothly objects that have a flat surface and are not more than several hundred pounds in weight. Examples of such objects include glass plates, sheet metal, sheets of paper, and floor-covering materials, such as ceramic tile and sheets of linoleum. The weight limitation is due to the fact that the maximum suction pressure equals 1 atm of pressure in magnitude.

Materials-handling application where a vacuum cup (sometimes called a suction cup) is used to establish the force capability to lift a flat sheet. The cup is typically made of a flexible material such as rubber so that a seal can be made where its lip contacts the surface of the flat sheet.

Vacuum generation in pneumatic systems is typically achieved using vacuum pumps. Two common types are:

-**Ejectors (Venturi Pumps):**These pumps use the Venturi effect, where a high-velocity stream of compressed air creates a region of low pressure, drawing air from the vacuum chamber. Ejectors are simple, inexpensive, and have no moving parts, but they are less energy-efficient than other types of vacuum pumps.
-**Rotary Vane Pumps:**These pumps use a rotating vane mechanism to mechanically evacuate air from the vacuum chamber. They are more energy-efficient than ejectors but are more complex and require maintenance.

The theoretical limit of a vacuum system is reaching absolute zero pressure. However, in practice, the maximum achievable vacuum is limited by factors such as leakage, outgassing, and the performance characteristics of the vacuum pump.

The force exerted by a vacuum cup is directly related to the pressure difference between the atmospheric pressure and the vacuum pressure within the cup, multiplied by the effective area of the cup:

$\Delta t$

Where:

- $D = 50 \, mm = 0.05 \, m$ is the atmospheric pressure (Pa).
- $A = \pi r^2 = \pi (D/2)^2 = \pi (0.05/2)^2 = 0.001963 \, m^2$ is the absolute pressure inside the vacuum cup (Pa).
- $p = 0.6 \, MPa = 0.6 \times 10^6 \, Pa$ is the effective area of the vacuum cup (m²).

The time it takes to evacuate a vacuum chamber to a desired pressure, known as the pump-down time, depends on the volume of the chamber and the flow rate of the vacuum pump.

$F = p \cdot A = (0.6 \times 10^6 \, Pa) \cdot (0.001963 \, m^2) = 1177.8 \, N$

This equation assumes a constant pump flow rate, which is often a simplification. In reality, the pump flow rate may decrease as the vacuum pressure increases.**Mirror Problems:Problem 1:**Calculate the lifting force of a vacuum cup given its diameter and the vacuum pressure. A vacuum cup with a diameter of 75 mm is used to lift a flat sheet. The vacuum pressure inside the cup is -60 kPa gauge (relative to atmospheric pressure). Calculate the lifting force of the cup. Assume atmospheric pressure is 101 kPa.**Solution:**First, convert the vacuum pressure to absolute pressure: $D = 120 \, mm = 0.12 \, m$

Calculate the area of the vacuum cup: $A = \pi r^2 = \pi (D/2)^2 = \pi (0.12/2)^2 = 0.01131 \, m^2$

Calculate the lifting force: $p = 0.9 \, MPa = 0.9 \times 10^6 \, Pa$**Problem 2:**Determine the required vacuum pressure to lift a sheet of material with a given weight and vacuum cup area. A sheet of material weighing 30 N needs to be lifted using a vacuum cup with a diameter of 60 mm. What vacuum pressure (gauge) is required to lift the sheet?**Solution:**Calculate the area of the vacuum cup: $F = p \cdot A = (0.9 \times 10^6 \, Pa) \cdot (0.01131 \, m^2) = 10179 \, N$

Calculate the required pressure difference: $D = 63 \, mm = 0.063 \, m$

Calculate the required vacuum pressure (gauge): $s = 200 \, mm = 0.2 \, m$**Problem 3:** Calculate the pump-down time for a vacuum chamber, given the chamber volume and pump flow rate. A vacuum chamber with a volume of 0.03 m³ is evacuated using a vacuum pump with a flow rate of 3 L/min. How long will it take to reduce the pressure in the chamber from atmospheric pressure (101 kPa) to 20 kPa absolute?

F = the upward force the suction cup exerts on the

where

flat sheet (Ib, N),



P
 pressure in absolute units

the atmospheric

atm

(psia, Pa, abs)



A
 the area of the outer circle of the suction cup lip

o

o
D
in
m





2
2
2

=
. ,
4