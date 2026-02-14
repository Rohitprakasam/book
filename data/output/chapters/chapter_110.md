---
title: "Chapter 110"
author: "BookForge Draft"
---

Do = the diameter of the suction cup lip outer circle (in., m)
Psuction = the suction pressure inside the cup cavity in absolute units (psia, Pa, abs)
Ai = the area of the inner circle of the suction cup lip
Di = the diameter of the suction cup inner lip circle (in., m)

Notice the atmospheric pressure on the top and bottom surfaces of the flat sheet cancel out away from the outer area of the cup lip.

Because Patm / P vacuum is a ratio, it is dimensionless. Thus, any desired units can be used fpr Patm and Pvacuum as long as the units are the same and are absolute. For example, inches of mercury absolute could also be used for both pressures instead of using psia or pascals absolute. Thus, for example, if Patm is five times as large as Pvacuum, the pressure ratio will equal 5 no matter what units are used, as long as they are the same units and are absolute.

Discrete Control Logic

### Suction Cup Mechanics: Introduction

Suction cups are deceptively simple devices that rely on fundamental principles of physics to function. Their ability to adhere to surfaces and lift objects stems from the pressure differential created between the inside of the cup and the surrounding atmosphere. This seemingly basic mechanism finds widespread applications in various industries, ranging from simple household uses to sophisticated robotic grippers, medical devices, and advanced manufacturing processes. Understanding the underlying physics is crucial for designing and implementing suction cup systems effectively.

At its core, a suction cup works by creating a partial vacuum within the cup's cavity. When pressed against a surface, the flexible lip of the cup forms a seal, preventing air from entering. As the volume inside the cup increases (due to the cup's shape or an external vacuum source), the air pressure inside decreases. This reduction in pressure creates a pressure difference between the inside of the cup (Psuction) and the outside atmosphere (Patm). The atmospheric pressure, being higher, exerts a force on the outer surface of the object, pressing it against the suction cup and generating a holding force. The magnitude of this force is directly proportional to the pressure difference and the effective area over which this pressure difference acts.

**Mathematical Derivations**

Let's derive the net force on a flat surface to which a suction cup is adhered. First, consider the force exerted by atmospheric pressure on a flat surface. Pressure is defined as force per unit area. Therefore, the force due to atmospheric pressure (p atm) acting on an area (A) is given by:

$p$

Now, consider a suction cup applied to the surface. Let *A<sub>i</sub>* be the area enclosed by the inner lip of the suction cup, and *A<sub>o</sub>* be the area enclosed by the outer lip of the suction cup. Let *p<sub>suction</sub>* be the absolute pressure inside the suction cup. The force due to the suction pressure will be

$F$


> 📊 *Diagram: {"subject": "Cross-sectional view of a suction cup adhering to a flat surface. Label Patm acting on the outside, Psuction inside the cup, Di as the inner diameter, Do as the outer diameter, and indicate the direction of the net force.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Free body diagram of the forces acting on the flat surface under the suction cup. Show the force due to atmospheric pressure and the force due to the suction pressure.", "type": "technical illustration"}*


The net force (Fnet) holding the suction cup to the surface is the difference between the atmospheric force acting on *A<sub>i</sub>* and the suction force:

$A$

Since $V$,

$Q$

We can also describe the forces over *A<sub>o</sub>*. In this case, $m^3$, but accounting for the area difference on either side of the lip will give the same result.

The vacuum level created inside the suction cup is directly related to the suction pressure. A perfect vacuum would correspond to a suction pressure of zero absolute. In reality, achieving a perfect vacuum is impossible, and the suction pressure will always be greater than zero. The relationship between the suction pressure and the vacuum level can be understood through the ideal gas law, which relates pressure, volume, and temperature of a gas.

**Mirror Problems**

Problem 1: Suction Cup Force Calculation

A suction cup has an inner diameter (D<sub>i</sub>) of 100 mm. The atmospheric pressure (p<sub>atm</sub>) is 101.325 kPa, and the suction pressure (p<sub>suction</sub>) inside the cup is 20 kPa. Calculate the net force (F<sub>net</sub>) holding the suction cup to the surface.

Solution:

1.  Convert the diameter to meters: D<sub>i</sub> = 100 mm = 0.1 m
2.  Calculate the area of the inner circle: A<sub>i</sub> = (π/4) * (0.1 m)<sup>2</sup> ≈ 0.00785 m<sup>2</sup>
3.  Calculate the pressure difference: Δp = p<sub>atm</sub> - p<sub>suction</sub> = 101.325 kPa - 20 kPa = 81.325 kPa = 81325 Pa
4.  Calculate the net force: F<sub>net</sub> = Δp * A<sub>i</sub> = 81325 Pa * 0.00785 m<sup>2</sup> ≈ 638.4 N

Problem 2: Suction Cup Diameter Sizing

A suction cup needs to generate a net force (F<sub>net</sub>) of 50 N. The atmospheric pressure (p<sub>atm</sub>) is 101.325 kPa, and the suction pressure (p<sub>suction</sub>) is 30 kPa. Calculate the required inner diameter (D<sub>i</sub>) of the suction cup.

Solution:

1.  Calculate the pressure difference: Δp = p<sub>atm</sub> - p<sub>suction</sub> = 101.325 kPa - 30 kPa = 71.325 kPa = 71325 Pa
2.  Rearrange the net force equation to solve for A<sub>i</sub>: A<sub>i</sub> = F<sub>net</sub> / Δp = 50 N / 71325 Pa ≈ 0.000701 m<sup>2</sup>
3.  Rearrange the area equation to solve for D<sub>i</sub>: D<sub>i</sub> = √(4 * A<sub>i</sub> / π) = √(4 * 0.000701 m<sup>2</sup> / π) ≈ 0.0299 m
4.  Convert the diameter to millimeters: D<sub>i</sub> ≈ 0.0299 m = 29.9 mm

Problem 3: Suction Cup Pressure Requirement

A suction cup of inner diameter (D<sub>i</sub>) 80mm is to generate 30N of force when applied to a surface at sea level (Patm = 101.325 kPa). What suction pressure (Psuction) is required?

Solution:

1. Convert the diameter to meters: D<sub>i</sub> = 80 mm = 0.08 m
2. Calculate the area of the inner circle: A<sub>i</sub> = (π/4) * (0.08 m)<sup>2</sup> ≈ 0.00503 m<sup>2</sup>
3.  Rearrange the net force equation to solve for Psuction: $m^3/s$, becomes $pV = nRT$.
4. Calculate the suction pressure: $p = \frac{F}{A}$

Problem 4: Effects of Altitude on Suction

At sea level Patm is 101.325kPa. However, as one ascends in altitude, the atmospheric pressure decreases. Given an altitude of 2000m, where the atmospheric pressure is approximately 80 kPa, what is the net force for Di = 75mm and Psuction = 25kPa?

Solution:

1. Convert the diameter to meters: D<sub>i</sub> = 75 mm = 0.075 m
2. Calculate the area of the inner circle: A<sub>i</sub> = (π/4) * (0.075 m)<sup>2</sup> ≈ 0.00442 m<sup>2</sup>
3. Calculate the pressure difference: Δp = p<sub>atm</sub> - p<sub>suction</sub> = 80 kPa - 25 kPa = 55 kPa = 55000 Pa
4. Calculate the net force: F<sub>net</sub> = Δp * A<sub>i</sub> = 55000 Pa * 0.00442 m<sup>2</sup> ≈ 243.1 N