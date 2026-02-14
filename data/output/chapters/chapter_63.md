---
title: "Chapter 63"
author: "BookForge Draft"
---

Okay, here is the expanded text based on your instructions:

### Vane Pumps: Principles of Operation

Vane pumps are a type of positive displacement pump commonly used in hydraulic systems. Their primary function is to convert mechanical energy, typically from a rotating shaft driven by an electric motor or internal combustion engine, into hydraulic energy in the form of fluid pressure and flow. They achieve this by creating a sealed volume that expands to draw fluid in and then contracts to positively displace the fluid out to the system. This positive displacement principle distinguishes them from centrifugal pumps, which rely on imparting kinetic energy to the fluid.

The core components of a vane pump are a rotor, vanes, and a cam ring (also sometimes referred to as a housing). The rotor, which is driven by the shaft, has slots cut into it, into which the vanes are inserted. These vanes are free to slide radially within the rotor slots. The rotor is positioned eccentrically within the cam ring, meaning the center of the rotor does not coincide with the center of the cam ring. As the rotor turns, the vanes are forced outwards -- often aided by springs or hydraulic pressure -- to maintain contact with the inner surface of the cam ring. On the intake side of the pump, the volume between adjacent vanes increases as the rotor rotates, creating a vacuum that draws fluid into the chamber. Conversely, on the discharge side, the surface of the cam ring pushes the vanes back into their slots, and the trapped volume is reduced. This positively ejects the trapped fluid through the discharge port. The degree of eccentricity is crucial, as it determines the amount of fluid displaced per revolution.

Vane pumps offer a good balance of cost, efficiency, and pressure capability for many applications. They are often used in mobile hydraulics, industrial machinery, and automotive power steering systems. Compared to gear pumps, vane pumps typically offer higher efficiency and lower noise. While piston pumps offer even higher pressure capabilities and efficiencies, they also come with increased complexity and cost, making vane pumps a good compromise for medium-pressure applications. The displacement, flow rate, and pressure generation of a vane pump are all directly related to its design parameters and operating conditions. Understanding these relationships is crucial for selecting the right pump for a specific hydraulic system.


> 📊 *Diagram: {"subject": "Cross-sectional view of a basic vane pump showing the rotor, vanes, cam ring, inlet port, outlet port, eccentricity (e), rotor diameter (Di), and cam ring diameter (Dc). Annotate the expanding and contracting volumes.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Exploded view of a vane pump showing individual components: rotor, vanes, cam ring, side plates, bearings, shaft.", "type": "technical illustration"}*


The following analysis and nomenclature is applicable to the vane pump:

$D_c$ = Diameter of cam ring (in., m)
$D_i$ = diameter of rotor (in., m)
$L$ = width of rotor (in., m)
$V_D$= displacement volume of pump (in$^3$, m$^3$)
$N$ = rotor rpm
$e$ = eccentricity (in., m)
$e_{max}$= maximum possible eccentricity (in., m)
$V_{Dmax}$=maximum possible volumetric displacement (in$^3$, m$^3$)

From geometry, we can find the maximum possible eccentricity: The eccentricity, denoted as 'e,' is the distance between the center of the rotor and the center of the cam ring. The maximum possible eccentricity, denoted as '$e_{max}$', is geometrically constrained by the diameters of the cam ring and the rotor. If the eccentricity exceeds this maximum value, the rotor would bind against the cam ring, preventing rotation. The maximum eccentricity can be calculated by considering the difference in radii between the cam ring and the rotor.

Imagine a circle representing the cam ring, and a smaller circle representing the rotor placed inside it.  The maximum the rotor can be off-center is when its edge touches the edge of the cam ring on one side. The mathematical expression for this is derived as follows:

$e_{max} = R_c - R_i = \frac{D_c}{2} - \frac{D_i}{2}$

Factoring out the half,

$e_{max} = \frac{D_c - D_i}{2}$

In which $D_c$ is the diameter of the cam ring and $D_i$ is the diameter of the rotor.

c
R
D
D
e



max
2

This maximum value of eccentricity produces a maximum volumetric displacement.

The volumetric displacement, $V_D$, represents the volume of fluid displaced by the pump per revolution of the rotor. The maximum volumetric displacement, $V_{Dmax}$, occurs when the eccentricity is at its maximum value, $e_{max}$. The displaced volume is a function of the area swept by the vanes as they rotate within the cam ring, multiplied by the width of the rotor. To derive the formula for $V_{Dmax}$, consider a single vane chamber. As the rotor rotates, the vane sweeps out an area that is approximately equal to the length of the vane (which is related to the eccentricity) multiplied by the distance it travels along the cam ring.  Accounting for all vanes, we can write the volumetric displacement as:

$V_D = n_{vanes} \cdot A_{vane} \cdot L$

Where $n_{vanes}$ is the number of vanes, $A_{vane}$ is the area swept by a single vane during one revolution, and L is the width of the rotor.  The expression in the textbook simplifies this by relating the swept area to the diameters of the cam ring and rotor and incorporating the maximum eccentricity.

2
2
max
(
)
4
D
c
R
V
D
D
L




Rearranging, we have

max
(
)(
)
4
D
c
R
c
R
V
D
D
D
D
L





Substituting the expression for $e_{max}$ yields

max
max
(
)(2
)
4
D
c
R
V
D
D
e
L




The actual volumetric displacement occurs when $e_{max}=e$:

(
)
2
D
c
R
V
D
D
eL




To fully characterize a vane pump, it is important to know the theoretical flow rate, $Q_{th}$, which represents the volume of fluid the pump *should* displace per unit time, assuming no leakage or losses. It's calculated by multiplying the volumetric displacement by the rotational speed:

$Q_{th} = V_D \cdot N$

Where N is the rotational speed in revolutions per minute (RPM) or revolutions per second (RPS), depending on the desired units for flow rate.

Finally, the theoretical hydraulic power, $\mathcal{P}_{th}$, represents the power delivered by the pump to the fluid. It is calculated by multiplying the system pressure, $p$, by the theoretical flow rate:

$\mathcal{P}_{th} = p \cdot Q_{th}$

This assumes 100% efficiency, which is never achieved in real-world applications due to mechanical and volumetric losses.

Here are some example problems to illustrate these concepts:

**Problem 1: Vane Pump Displacement**A vane pump has a rotor diameter ($D_i$) of 120 mm, a cam ring diameter ($D_c$) of 170 mm, a rotor width (L) of 50 mm, and 8 vanes. Calculate the maximum volumetric displacement ($V_{Dmax}$).

First, convert all dimensions to meters:
$D_i = 0.12 \, m$
$D_c = 0.17 \, m$
$L = 0.05 \, m$

Next, determine the maximum eccentricity, emax:

$e_{max} = (D_c - D_i)/2 = (0.17 \, m - 0.12 \, m) / 2 = 0.025 \, m$

Then, determine the maximum volumetric displacement:

$V_{Dmax} = \frac{\pi}{2} (D_c + D_i) e_{max} L = \frac{\pi}{2} (0.17 \, m + 0.12 \, m) \cdot (0.025 \, m) \cdot (0.05 \, m) = 5.70 \times 10^{-5} \, m^3 = 57.0 \, cm^3$**Problem 2: Vane Pump Flow Rate**Using the same pump parameters as in Problem 1, calculate the theoretical flow rate ($Q_{th}$) in liters per minute if the rotor speed (N) is 1500 RPM.

First, we know from Problem 1 that  $V_{Dmax} = 5.70 \times 10^{-5} \, m^3$.

Convert RPM to revolutions per second (RPS):

$N = 1500 \, RPM = 1500/60 \, RPS = 25 \, RPS$

Calculate the theoretical flow rate in $m^3/s$:

$Q_{th} = V_{Dmax} \cdot N = (5.70 \times 10^{-5} \, m^3) \cdot (25 \, RPS) = 0.001425 \, m^3/s$

Convert $m^3/s$ to liters per minute (L/min):

$Q_{th} = 0.001425 \, m^3/s \cdot (1000 \, L/m^3) \cdot (60 \, s/min) = 85.5 \, L/min$

Some vane pumps have provisions for mechanically varying the eccentricity.
Such a design is called a variable displacement pump. A hand wheel or a pressure
compensator can be used to move the cam ring to change the eccentricity. The
direction of flow through the pump can be reversed by movement of the cam ring on
either side of center.

### Variable Displacement Vane Pumps

Variable displacement vane pumps offer the advantage of being able to adjust the flow rate delivered by the pump without changing the speed of the prime mover (e.g., electric motor). This is achieved by mechanically altering the eccentricity between the rotor and the cam ring. The primary benefit is improved energy efficiency. In systems where the demand for flow varies, a variable displacement pump can be adjusted to match the demand, reducing wasted energy and heat generation. In contrast, a fixed displacement pump would deliver a constant flow rate, with any excess flow being bypassed, which wastes energy. Another significant advantage is more precise flow control, allowing for smoother and more accurate operation of hydraulic actuators.

There are several methods for varying the eccentricity. One common approach involves using a hand wheel connected to a linkage that moves the cam ring relative to the rotor. By rotating the hand wheel, the operator can manually adjust the eccentricity and, consequently, the flow rate.  Another method uses a pressure compensator, which automatically adjusts the eccentricity based on the system pressure.

The relationship between eccentricity, flow rate, and pressure is fundamental to understanding variable displacement pumps. As the eccentricity increases, the volumetric displacement increases, leading to a higher flow rate at a given rotor speed. However, the pressure required to deliver that flow depends on the load imposed by the hydraulic system. By adjusting the eccentricity, the pump can maintain a desired pressure or flow rate, depending on the control strategy. Moreover, by moving the cam ring to either side of the center position, the direction of flow through the pump can be reversed. This is a useful feature in applications where bidirectional movement of hydraulic actuators is required.


> 📊 *Diagram: {"subject": "Schematic of a variable displacement vane pump with a hand wheel control, showing the linkage between the hand wheel and the cam ring.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Schematic of a variable displacement vane pump with a pressure compensator, showing the hydraulic piston, compensator spring, and cam ring.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Graph of flow rate vs. eccentricity for a variable displacement vane pump.", "type": "technical illustration"}*


To quantify the performance of variable displacement vane pumps, we need to define some key efficiency metrics.

Volumetric efficiency ($\eta_v$) represents the ratio of actual flow rate ($Q_{actual}$) to theoretical flow rate ($Q_{th}$):

$\eta_v = \frac{Q_{actual}}{Q_{th}}$

The volumetric efficiency accounts for internal leakage within the pump, such as fluid bypassing the vanes or leaking across seals. A higher volumetric efficiency indicates less leakage and a more effective displacement of fluid.

Overall efficiency ($\eta_o$) represents the ratio of hydraulic power output ($\mathcal{P}_{out}$) to mechanical power input ($\mathcal{P}_{in}$):

$\eta_o = \frac{\mathcal{P}_{out}}{\mathcal{P}_{in}}$

The overall efficiency takes into account both volumetric losses (leakage) and mechanical/hydraulic losses due to friction within the pump. These friction losses arise from the movement of the vanes, the rotor, and the cam ring, as well as the viscous friction of the fluid itself.

We can also express flow rate as a function of eccentricity:

$Q = f(e, N, D_c, D_i, L)$

Substituting the equation for $V_D$ into the equation for $Q_{th}$ and assuming $Q \approx Q_{th}$, then:

$Q = V_D \cdot N = \frac{\pi}{2}(D_c + D_i)eLN$

The actual flow will differ due to volumetric inefficiencies, as seen above.

Here are some example problems to illustrate these concepts:**Problem 1: Flow Rate Control**A variable displacement vane pump has $D_i$ = 80 mm, $D_c$ = 120 mm, L = 40 mm, N = 1200 RPM. If the eccentricity can be varied from 5 mm to 15 mm, calculate the range of flow rates achievable.

First, convert all dimensions to meters:
$D_i = 0.08 \, m$
$D_c = 0.12 \, m$
$L = 0.04 \, m$
$N = 1200 \, RPM = 20 \, RPS$

Calculate the flow rate at e = 5 mm = 0.005 m

$Q_{min} = \frac{\pi}{2} (0.12 + 0.08) (0.005)(0.04)(20) = 0.001257 \, m^3/s$
Convert this to L/min:
$Q_{min} = 0.001257 \, m^3/s * (1000 \, L/m^3) * (60 \, s/min) = 75.4 \, L/min$

Calculate the flow rate at e = 15 mm = 0.015 m
$Q_{max} = \frac{\pi}{2} (0.12 + 0.08) (0.015)(0.04)(20) = 0.00377 \, m^3/s$
Convert this to L/min:
$Q_{max} = 0.00377 \, m^3/s * (1000 \, L/m^3) * (60 \, s/min) = 226.2 \, L/min$

Therefore, the flow range is from 75.4 L/min to 226.2 L/min.**Problem 2: Efficiency Calculation**

A variable displacement vane pump operates at p = 10 MPa and $Q_{actual}$ = 50 L/min. The input torque is 50 Nm at 1500 RPM. Calculate the hydraulic power output, mechanical power input, and overall efficiency ($\eta_o$).

First, convert all units to SI:
p = 10 MPa = $10 \times 10^6 \, Pa$
$Q_{actual}$ = 50 L/min = $50 / (60 \times 1000) \, m^3/s = 8.33 \times 10^{-4} \, m^3/s$
Torque = 50 Nm
N = 1500 RPM = 25 RPS

Hydraulic power output:
$\mathcal{P}_{out} = p Q_{actual} = (10 \times 10^6)(8.33 \times 10^{-4}) = 8330 \, W$

Mechanical power input:
$\mathcal{P}_{in} = \tau \omega = \tau (2\pi N) = (50)(2\pi)(25) = 7854 \, W$

Overall efficiency:
$\eta_o = \frac{\mathcal{P}_{out}}{\mathcal{P}_{in}} = \frac{8330}{7854} = 1.06$. Since the efficiency cannot exceed 100% this implies that the torque value is likely incorrect and should have been higher. If the torque was 53 Nm, the overall efficiency would be 99%.

It is a pressure compensated one in which system pressure acts directly on
the cam ring via a hydraulic piston on the right side. This forces the cam ring
against the compensator spring-loaded piston on the left side of the cam ring. If the
discharge pressure is large enough, it overcomes the compensator spring force and
shift the cam ring to the left. This reduces the eccentricity, which is maximum when
discharge pressure is zero. As the discharge pressure continues to increase, zero
eccentricity is finally achieved, and the pump now becomes zero. Such a pump
basically has its own protection against excessive pressure buildup, as shown in fig.
when the pressure reaches a value called Pcutoff the compensator spring force
equals the hydraulic piston force. As the pressure continues to increase, the
compensator spring is compressed until zero eccentricity is achieved. The
maximum pressure achieved is called Pdeadhead at which point the pump is protected
because it attempts to produce no more flow. As a result there is no horse power
wasted and fluid heating is reduced.
The internal configuration of an actual pressure compensated vane pump.
This design contains a cam ring that rotates slightly during use. Thereby
distributing wear over the entire inner circumference of the ring.

### Pressure Compensated Vane Pumps

Pressure compensated vane pumps are designed to automatically maintain a nearly constant output pressure, regardless of variations in system flow demand. This is achieved through an internal feedback mechanism that adjusts the pump's eccentricity in response to changes in the discharge pressure. The heart of this mechanism is a pressure compensator, which typically consists of a hydraulic piston, a compensator spring, and a control valve.

System pressure acts directly on the cam ring via a hydraulic piston, typically located on one side of the cam ring. This piston is opposed by a spring-loaded piston located on the opposite side.  As the discharge pressure increases, the hydraulic piston exerts a greater force on the cam ring, working against the force exerted by the compensator spring. When the discharge pressure reaches a predetermined value, known as the *cutoff pressure* ($p_{cutoff}$), the force generated by the hydraulic piston equals the opposing force of the compensator spring.

If the discharge pressure continues to increase beyond $p_{cutoff}$, the hydraulic piston overcomes the spring force and shifts the cam ring, reducing the eccentricity. This reduction in eccentricity directly reduces the pump's volumetric displacement and, consequently, the flow rate. Eventually, as the pressure continues to climb, the eccentricity is reduced to zero, and the pump output effectively ceases. The maximum pressure the pump can achieve under these conditions is called the *deadhead pressure* ($p_{deadhead}$). At $p_{deadhead}$, the pump is producing minimal or no flow, preventing excessive pressure buildup in the system.

Pressure compensation provides several significant benefits. First, it improves energy efficiency by reducing flow when demand is low, minimizing wasted energy and heat generation. Second, it provides overload protection for the hydraulic system by limiting the maximum pressure that can be reached. This prevents damage to hydraulic components such as cylinders, valves, and hoses.


> 📊 *Diagram: {"subject": "Cross-sectional view of a pressure compensated vane pump showing the hydraulic piston, compensator spring, cam ring, and pressure tap.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Graph of pressure vs. flow rate for a pressure compensated vane pump, illustrating the cutoff pressure and deadhead pressure.", "type": "technical illustration"}*


Mathematically, the cutoff pressure is defined by the equilibrium between the compensator spring force ($F_{spring}$) and the hydraulic piston force ($F_{piston}$):

$F_{spring} = F_{piston} = p_{cutoff} \cdot A_{piston}$

Where $A_{piston}$ is the area of the hydraulic piston.

Beyond the cutoff pressure, the spring compresses, and the pressure increases further. The relationship is defined by:

$p = p_{cutoff} + \frac{k \cdot x}{A_{piston}}$

where $k$ is the spring constant and $x$ is the spring compression.

Here are some example problems:

**Problem 1: Cutoff Pressure**A pressure compensated vane pump has a hydraulic piston area ($A_{piston}$) of 20 cm$^2$ and a compensator spring force of 4000 N. Calculate the cutoff pressure ($p_{cutoff}$).

First, convert area to $m^2$:

$A_{piston} = 20 \, cm^2 = 20 \times 10^{-4} \, m^2$

The cutoff pressure can be directly calculated as:

$p_{cutoff} = \frac{F_{spring}}{A_{piston}} = \frac{4000 \, N}{20 \times 10^{-4} \, m^2} = 2 \times 10^7 \, Pa = 20 \, MPa$**Problem 2: Spring Constant**

A pressure compensated vane pump has $A_{piston}$ = 15 cm$^2$ and a spring constant (k) of 50 N/mm. If the pressure increases by 2 MPa above $p_{cutoff}$, calculate the spring compression (x).

Convert the area to $m^2$ and spring constant to N/m:
$A_{piston} = 15 \, cm^2 = 15 \times 10^{-4} \, m^2$
$k = 50 \, N/mm = 50000 \, N/m$
$\Delta p = 2 \, MPa = 2 \times 10^6 \, Pa$

The spring compression x can be determined as:

$\Delta p = p - p_{cutoff} = \frac{k \cdot x}{A_{piston}}$
$x = \frac{\Delta p \cdot A_{piston}}{k} = \frac{(2 \times 10^6 \, Pa) \cdot (15 \times 10^{-4} \, m^2)}{50000 \, N/m} = 0.06 \, m = 60 \, mm$

A side load is exerted on the bearings of the vane pump because of
pressure unbalance. This same undesirable side load exists for the gear pump
such pumps are hydraulically unbalanced.

A balanced vane pump is one that has two intake and two outlet ports
diametrically opposite each other. Thus pressure ports are opposite each other,
and a complete hydraulic balance is achieved. One disadvantage of a balanced
vane pump is that it cannot be designed as a variable displacement unit. Instead of
having a circular cam ring, a balanced design vane pump has an elliptical housing,
which forms two separate pumping chambers on opposite sides of the rotor.

### Balanced Vane Pumps

Unbalanced vane pumps, like many gear pumps, are susceptible to side loads on their bearings due to pressure imbalances within the pump housing. This pressure unbalance arises from the fact that the high-pressure discharge port is typically located on one side of the rotor, while the low-pressure inlet port is on the opposite side. This pressure differential creates a net radial force on the rotor, which is transmitted to the bearings, leading to increased wear and reduced pump life.

A *balanced vane pump* addresses this issue by incorporating two intake ports and two outlet ports positioned diametrically opposite each other. This configuration ensures that the pressure forces acting on the rotor are balanced, significantly reducing the radial load on the bearings. In essence, the high-pressure regions are directly opposed by other high-pressure regions, and similarly, the low-pressure regions are opposed by low-pressure regions. This complete hydraulic balance minimizes bearing wear and extends the pump's service life.

One significant trade-off with balanced vane pumps is that they cannot be designed as variable displacement units. This limitation stems from the elliptical shape of the pump housing, which is necessary to create the two separate pumping chambers. In a balanced vane pump, instead of having a circular cam ring, the design incorporates an elliptical housing, effectively forming two distinct pumping chambers on opposite sides of the rotor. Each pumping chamber operates independently, contributing to the overall flow rate of the pump. The elliptical shape, however, makes it impossible to adjust the eccentricity, which is essential for variable displacement functionality.


> 📊 *Diagram: {"subject": "Cross-sectional view of a balanced vane pump showing the elliptical housing, rotor, vanes, two inlet ports, and two outlet ports. Indicate the pressure distribution around the rotor.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Comparison of force vectors acting on the rotor of an unbalanced vane pump versus a balanced vane pump.", "type": "technical illustration"}*


Qualitatively, in an unbalanced vane pump, the pressure distribution around the rotor is uneven, with a higher pressure concentration on the discharge side. This results in a net force vector pointing towards the inlet side. In contrast, in a balanced vane pump, the two discharge ports create two opposing high-pressure regions, effectively canceling out the radial forces on the rotor.

While a rigorous mathematical derivation of the force balance would require complex integration of pressure forces over the rotor surface, a simplified representation can illustrate the concept.

In an unbalanced pump, the net force can be represented as:

$F_{net, unbalanced} = \int_{0}^{\pi} p_{discharge} \cdot r \cdot L \cdot d\theta -  \int_{\pi}^{2\pi} p_{intake} \cdot r \cdot L \cdot d\theta$

Where $p_{discharge}$ and $p_{intake}$ are the average discharge and intake pressures, r is the rotor radius, L is the rotor width, and $\theta$ is the angular position.

In a balanced pump, the net force is ideally zero due to symmetry:

$F_{net, balanced} \approx 0$

Here are some conceptual example problems:

**Problem 1: Force Analysis (Conceptual)**

Explain why a balanced vane pump experiences lower bearing loads compared to an unbalanced vane pump, given the same system pressure and flow rate.

*Answer:* In an unbalanced vane pump, the pressure difference between the inlet and outlet ports creates a net radial force on the rotor, which is directly transferred to the bearings as a side load. In a balanced vane pump, the diametrically opposed inlet and outlet ports create opposing pressure forces that largely cancel each other out, resulting in a much lower net radial force on the rotor and, consequently, reduced bearing loads.

**Problem 2: Application Suitability**

Compare the advantages and disadvantages of using a balanced vane pump versus an unbalanced vane pump in a specific application (e.g., a hydraulic press).

*Answer:*
*Balanced Vane Pump:*
Advantages: Longer bearing life due to reduced bearing loads, potentially lower maintenance costs.
Disadvantages: Cannot be used in applications requiring variable displacement.

*Unbalanced Vane Pump:*
Advantages: Can be designed as a variable displacement unit, allowing for flow control.
Disadvantages: Shorter bearing life due to higher bearing loads, potentially higher maintenance costs.

For a hydraulic press where a constant flow rate is acceptable, a balanced vane pump might be a good choice due to its increased reliability. If flow rate needs to be actively controlled, then an unbalanced vane pump will be the only option, though it will impact the wear characteristics.

### Piston Pumps

Piston pumps represent another category of positive displacement pumps known for their high-pressure capability and efficiency. They are typically more complex and expensive than vane or gear pumps but offer superior performance in demanding applications. Piston pumps operate by using one or more reciprocating pistons to draw fluid into a chamber and then force it out under high pressure.

There are two main types of piston pumps: axial and radial. In *axial piston pumps*, the pistons are arranged parallel to the drive shaft. The pistons reciprocate within cylinders that are part of a rotating cylinder block. The stroke of the pistons is controlled by a swashplate or wobble plate. As the cylinder block rotates, the pistons move back and forth, drawing fluid in during the intake stroke and expelling it during the discharge stroke. Axial piston pumps are commonly used in hydraulic systems requiring high pressure and variable flow.

In *radial piston pumps*, the pistons are arranged radially around the drive shaft. The pistons reciprocate within cylinders that are part of a stationary cylinder block. The stroke of the pistons is controlled by an eccentric cam or rotating ring. As the drive shaft rotates, the pistons move in and out, drawing fluid in and expelling it. Radial piston pumps are also known for their high-pressure capabilities and are often used in applications such as hydrostatic transmissions and heavy machinery.


> 📊 *Diagram: {"subject": "Simple schematic illustrating the basic principle of an axial piston pump.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Simple schematic illustrating the basic principle of a radial piston pump.", "type": "technical illustration"}*

