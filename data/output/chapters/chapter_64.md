---
title: "Chapter 64"
author: "BookForge Draft"
---

### Axial Design

Piston pumps stand as a cornerstone in numerous hydraulic systems, prized for their ability to deliver high pressures and controlled flow rates. Unlike centrifugal pumps, which rely on kinetic energy transfer, piston pumps operate on the principle of positive displacement, ensuring a consistent volume of fluid is moved with each cycle. This positive displacement characteristic makes them ideal for applications requiring precise control and high-pressure capabilities, such as heavy machinery, aircraft hydraulics, and injection molding. While various types of positive displacement pumps exist, including gear pumps and vane pumps, piston pumps excel in demanding environments where high pressures and accurate flow control are paramount. They are often favored in applications where a constant flow rate is required regardless of pressure variations in the system. Axial piston pumps further refine this technology, offering enhanced efficiency and power density compared to other piston pump designs. There are both fixed displacement and variable displacement designs. Fixed displacement pumps deliver a constant volume of fluid per revolution, while variable displacement pumps can adjust the flow rate based on system demands, optimizing energy consumption and reducing heat generation.


> 📊 *Diagram: {"subject": "Cutaway isometric view of a generic axial piston pump, highlighting the key components: drive shaft, cylinder block, pistons, swash plate/bent axis, inlet/outlet ports. Arrows should indicate the direction of fluid flow.", "type": "technical illustration"}*


The fundamental principle of a piston pump involves a reciprocating piston within a cylinder bore. As the piston retracts, it creates a vacuum, drawing fluid into the cylinder. Conversely, as the piston extends, it forces the fluid out of the cylinder. The challenge lies in mechanizing this reciprocating motion for multiple pistons in a coordinated manner to achieve a continuous flow. Axial piston pumps accomplish this by arranging the pistons parallel to the axis of rotation of the cylinder block. This configuration allows for a compact design and efficient conversion of rotary motion into linear motion. There are two primary configurations for axial piston pumps: the bent-axis design and the swash plate design, each with its own advantages and disadvantages. The selection of an axial piston pump depends on the specific requirements of the application, including pressure, flow rate, and control precision.

The basic question is how to mechanize a series of reciprocating pistons. There are two basic types of piston pumps: axial and radial.

One is the axial design, having pistons that are parallel to the axis of the cylinder block. Axial piston pumps can be either of the bent axis configuration or of the swash plate design. The second type of piston pump is the radial design, which has pistons arranged radically in a cylinder block.

An axial piston pump (bent-axis type) contains a cylinder block rotating with the drive shaft. However, the centerline of the cylinder block is set at an offset angle relative to the centerline of the drive shaft. The cylinder block contains a number of pistons arranged along a circle. The piston rods are connected to the drive shaft flange by ball and socket joints. The pistons are forced in and out of their bores as the distance between the drive shaft flange and cylinder block changes. A universal link connects the block to the drive shaft to provide alignment and positive drive.

The bent-axis axial piston pump is a marvel of engineering, converting rotary motion into linear motion with remarkable efficiency. Its working principle hinges on the angled relationship between the drive shaft and the cylinder block. As the drive shaft rotates, it compels the cylinder block to rotate as well. Because the cylinder block is tilted at an angle with respect to the drive shaft, the pistons, arranged in a circular pattern within the cylinder block, are forced to reciprocate in and out of their bores. The degree of this reciprocation, and consequently the pump's displacement, is directly proportional to the offset angle between the drive shaft and the cylinder block. The connection between the pistons and the drive shaft is typically achieved using ball and socket joints, which allow for the necessary articulation as the pistons move in and out. This design offers several advantages, including its ability to operate at high pressures and its relatively simple construction. However, it can also be larger and heavier than swash plate designs, particularly for high-displacement applications.


> 📊 *Diagram: {"subject": "Detailed cross-sectional view of a bent-axis axial piston pump. Label all key components: drive shaft, cylinder block, pistons, piston rods, ball and socket joints, universal link, inlet port, outlet port, offset angle.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Simplified schematic diagram of a bent-axis pump showing the geometric relationship between the offset angle, piston stroke, and piston circle diameter. This should be a 2D representation for clarity.", "type": "technical illustration"}*


The bent-axis design is particularly well-suited for high-pressure applications due to its robust construction and efficient force transmission. The direct connection between the pistons and the drive shaft minimizes stress and wear, allowing for sustained operation at elevated pressures. However, the size and weight of the bent-axis design can be a limiting factor in some applications, particularly where space is constrained. In contrast, swash plate designs tend to be more compact but may have limitations in terms of maximum pressure capability. The choice between bent-axis and swash plate designs often involves a trade-off between performance, size, and cost.

--- Page 42 ---

The volumetric displacement of the pump varies with the offset angle  no flow is produced when the cylinder block centerline is parallel to the drive shaft centerline.  Can vary from 0 to a maximum of about 30. Fixed displacement units are usually provided with 23Or 30 offset angles.

Variable displacement units are available with a yoke and some external control to change the offset angle.

The following nomenclature and analysis are applicable to an axial piston pump:

 = offset angle ()  
S = piston stroke (in., m) 
D = piston circle diameter (in., m) 
Y = number of pistons, 
A = piston area (in2. m2) 

From trigonometry we have

Tan () = s

D

Or 
 
 
S = D tan () 
 
The total displacement volume equals the number of pistons multiplied by the 
displacement volume preposition: 
 
 
VD = YAS 
Substituting, we have 
 
 
VD = YAD tan () 
From Eq. we obtain upon, substitution and using English units.

tan( )
231
DANY
Q



Similarly, for metric units, we have  
 
 
Q = DANY tan ()

The relationship between the offset angle, piston stroke, and piston circle diameter is fundamental to understanding the kinematics of a bent-axis axial piston pump. Imagine a right triangle formed by the piston stroke ($S$), half of the piston circle diameter ($D/2$), and the offset angle ($\theta$). The piston stroke represents the opposite side of the triangle, while half of the piston circle diameter represents the adjacent side. From basic trigonometry, the tangent of the offset angle is equal to the ratio of the opposite side to the adjacent side.

Therefore, we can write:

$tan(\theta) = \frac{S}{D}$

Which yields:

$S = D \cdot tan(\theta)$

This equation highlights that the piston stroke is directly proportional to the piston circle diameter and the tangent of the offset angle. As the offset angle increases, the piston stroke increases proportionally, leading to a larger displacement volume. When the offset angle is zero (θ = 0), then the piston stroke is zero, and there is no fluid displacement.

The total displacement volume ($V_D$) of the pump represents the volume of fluid displaced by all the pistons during one complete revolution of the cylinder block. To calculate this, we consider the volume displaced by a single piston during one stroke, which is the product of the piston area ($A$) and the piston stroke ($S$). Since there are $Y$ pistons in the pump, the total displacement volume is simply the sum of the volumes displaced by each piston.

Therefore, we can write:

$V_D = Y \cdot A \cdot S$

Substituting the expression for the piston stroke ($S = D \cdot tan(\theta)$), we get:

$V_D = Y \cdot A \cdot D \cdot tan(\theta)$

The theoretical flow rate ($Q$) of the pump is directly proportional to the displacement volume ($V_D$) and the rotational speed ($N$) of the cylinder block, typically measured in revolutions per minute (RPM). The flow rate represents the volume of fluid delivered by the pump per unit time. To obtain the flow rate, we simply multiply the displacement volume by the rotational speed.

$Q = V_D \cdot N$

Substituting the expression for displacement volume, we get:

$Q = Y \cdot A \cdot D \cdot tan(\theta) \cdot N$

Where $Q$ is typically given in units of volume per time (e.g., $m^3/min$ or $L/min$), so the parameters on the right-hand side need to be converted into consistent units. For example, the above equation has units of $m^3/rev$, so it must be multiplied by the pump speed in $rev/min$ to obtain units of $m^3/min$.

**Mirror Problems:**1.**Problem:**A bent-axis axial piston pump has an offset angle of 25 degrees, a piston circle diameter of 120 mm, 7 pistons, and a piston area of 350 mm². Calculate the displacement volume per revolution.

    -**Solution:**- $\theta = 25^\circ$
        - $D = 120 \text{ mm} = 0.12 \text{ m}$
        - $Y = 7$
        - $A = 350 \text{ mm}^2 = 3.5 \times 10^{-4} \text{ m}^2$
        - $V_D = Y \cdot A \cdot D \cdot tan(\theta) = 7 \cdot (3.5 \times 10^{-4} \text{ m}^2) \cdot (0.12 \text{ m}) \cdot tan(25^\circ)$
        - $V_D = 7 \cdot (3.5 \times 10^{-4} \text{ m}^2) \cdot (0.12 \text{ m}) \cdot 0.4663 \approx 1.367 \times 10^{-4} \text{ m}^3$
        - $V_D \approx 136.7 \text{ cm}^3/\text{rev}$

2.**Problem:**A bent-axis pump has a displacement volume of 150 cm³/rev and operates at a speed of 1800 RPM. Calculate the theoretical flow rate in liters per minute.

    -**Solution:**- $V_D = 150 \text{ cm}^3/\text{rev} = 1.5 \times 10^{-4} \text{ m}^3/\text{rev}$
        - $N = 1800 \text{ RPM} = 1800 \text{ rev/min}$
        - $Q = V_D \cdot N = (1.5 \times 10^{-4} \text{ m}^3/\text{rev}) \cdot (1800 \text{ rev/min}) = 0.27 \text{ m}^3/\text{min}$
        - $Q = 0.27 \text{ m}^3/\text{min} \cdot (1000 \text{ L/m}^3) = 270 \text{ L/min}$

3.**Problem:**A bent-axis pump has a known leakage rate of 3 L/min at a pressure of 15 MPa and a speed of 1500 RPM. The theoretical flow rate is 250 L/min. Calculate the volumetric efficiency.

    -**Solution:**- $Q_{leakage} = 3 \text{ L/min}$
        - $Q_{theoretical} = 250 \text{ L/min}$
        - $Q_{actual} = Q_{theoretical} - Q_{leakage} = 250 \text{ L/min} - 3 \text{ L/min} = 247 \text{ L/min}$
        - $\eta_v = \frac{Q_{actual}}{Q_{theoretical}} = \frac{247 \text{ L/min}}{250 \text{ L/min}} = 0.988$
        - $\eta_v = 98.8\%$

4.**Problem:**Determine the required motor power (kW) to drive a bent-axis pump given the desired output pressure of 25 MPa, flow rate of 100 L/min, and overall efficiency of 82%.

    -**Solution:**
        - $p = 25 \text{ MPa} = 25 \times 10^6 \text{ Pa}$
        - $Q = 100 \text{ L/min} = \frac{100}{60000} \text{ m}^3/\text{s} \approx 1.667 \times 10^{-3} \text{ m}^3/\text{s}$
        - $\eta_o = 82\% = 0.82$
        - $\mathcal{P}_{hydraulic} = p \cdot Q = (25 \times 10^6 \text{ Pa}) \cdot (1.667 \times 10^{-3} \text{ m}^3/\text{s}) = 41675 \text{ W}$
        - $\mathcal{P}_{mechanical} = \frac{\mathcal{P}_{hydraulic}}{\eta_o} = \frac{41675 \text{ W}}{0.82} \approx 50823 \text{ W}$
        - $\mathcal{P}_{mechanical} \approx 50.82 \text{ kW}$

--- Page 43 ---

PUMP PERFORMANCE:

The performance delivered by a pump is primarily a function of the precision of its manufacture. Components must be made to close tolerances, which must be maintained while the pump is operating under design conditions. The maintenance of close tolerances is accomplished by designs that have mechanical integrity and balanced pressures.

Theoretically the ideal pump would be one having zero clearance between all mating parts. Although this is infeasible, working clearances should be as small as possible while maintaining proper oil films for lubrication between rubbing parts.

Pump manufacturers run tests to determine performance data for their various types of pumps. The overall efficiency of a pump can be computed by comparing the power available at the output of the pump to the power supplied at the input. Overall efficiency can be broken into two distinct components called volumetric and mechanical efficiencies.

The performance of an axial piston pump hinges critically on the precision of its manufacturing. The intricate internal components, such as pistons, cylinder blocks, and valve plates, must be fabricated to extremely tight tolerances, often measured in micrometers. These close tolerances are essential to minimize internal leakage and maintain optimal volumetric efficiency. Any deviation from these tolerances can lead to a significant reduction in pump performance, resulting in lower flow rates, reduced pressure capabilities, and increased heat generation. Furthermore, these tolerances must be maintained throughout the pump's operating life, even under demanding conditions of high pressure and temperature. This requires robust designs that can withstand the mechanical stresses and thermal expansion associated with hydraulic systems.

The pursuit of optimal pump performance often leads to the theoretical concept of a pump with zero clearance between all mating parts. In such an idealized scenario, there would be no internal leakage, and the pump would achieve perfect volumetric efficiency. However, in reality, achieving zero clearance is not feasible due to manufacturing limitations and the need for lubrication between moving parts. Instead, practical pump designs strive to minimize working clearances while ensuring that adequate oil films are maintained to prevent wear and friction. The optimal balance between minimizing clearance and ensuring adequate lubrication is a critical design consideration for axial piston pumps.

Pump manufacturers routinely conduct rigorous testing to characterize the performance of their pumps. These tests typically involve measuring flow rate, pressure, input power, and output power under various operating conditions. The resulting data is used to generate performance curves that illustrate the pump's capabilities and limitations. These curves provide valuable information for system designers in selecting the appropriate pump for a specific application.

The overall efficiency ($\eta_o$) of a pump is a critical metric that reflects its ability to convert input power into useful hydraulic power. It is defined as the ratio of the hydraulic power output ($\mathcal{P}_{hydraulic}$) to the mechanical power input ($\mathcal{P}_{mechanical}$):

$\eta_o = \frac{\mathcal{P}_{hydraulic}}{\mathcal{P}_{mechanical}}$

The overall efficiency can be further decomposed into two key components: volumetric efficiency ($\eta_v$) and mechanical efficiency ($\eta_m$). Volumetric efficiency reflects the pump's ability to deliver the theoretical flow rate, accounting for internal leakage. It is defined as the ratio of the actual flow rate ($Q_{actual}$) to the theoretical flow rate ($Q_{theoretical}$).

$\eta_v = \frac{Q_{actual}}{Q_{theoretical}}$

Mechanical efficiency, on the other hand, reflects the pump's ability to convert mechanical power into hydraulic power, accounting for frictional losses within the pump. It is defined as the ratio of the theoretical torque required to drive the pump ($\tau_{theoretical}$) to the actual torque required ($\tau_{actual}$).

$\eta_m = \frac{\tau_{theoretical}}{\tau_{actual}}$

The overall efficiency is the product of the volumetric efficiency and the mechanical efficiency:

$\eta_o = \eta_v \cdot \eta_m$

Understanding and optimizing these efficiency components is crucial for maximizing the performance and minimizing the energy consumption of axial piston pumps.

--- Page 44 ---