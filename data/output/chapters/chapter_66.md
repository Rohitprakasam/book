---
title: "Chapter 66"
author: "BookForge Draft"
---

## 2. Mechanical Efficiency ($\eta_m$)

Mechanical efficiency indicates the amount of energy losses that occur due to reasons other than leakage. This includes friction in bearings and between other mating parts. It also includes energy losses due to fluid turbulence. Mechanical efficiencies typically run from 90% to 95%.

Before diving into the intricacies of mechanical efficiency, let's first set the stage. In any hydraulic system, energy conversion is never perfectly efficient. A portion of the input energy is inevitably lost due to various factors. While volumetric efficiency addresses losses due to fluid leakage, mechanical efficiency focuses on energy dissipation caused by friction and fluid dynamics *within* the pump itself. These losses manifest as heat, reducing the amount of useful hydraulic power delivered to the system. Understanding and maximizing mechanical efficiency is vital for optimizing system performance, reducing energy consumption, and extending the lifespan of hydraulic components.

The range of 90-95% for mechanical efficiency represents a practical benchmark for well-designed and maintained hydraulic pumps. However, this value can fluctuate depending on pump type, operating conditions, and fluid properties. For instance, a gear pump with relatively simple construction might exhibit slightly lower mechanical efficiency compared to a more sophisticated piston pump designed with advanced friction-reducing features.

### 2.1 Introduction to Pump Efficiency

Hydraulic pump efficiency is a critical parameter that quantifies how effectively a pump converts mechanical input power into hydraulic output power. It's a measure of how well a pump performs its primary function of transferring energy to a fluid. Efficiency is crucial for several reasons: it directly impacts the energy consumption of the hydraulic system, influences the size and cost of the prime mover (e.g., electric motor or engine), and affects the overall system performance and thermal management. A more efficient pump requires less input power to deliver the same hydraulic power, leading to lower operating costs and reduced environmental impact.

There are three primary types of pump efficiency:

- **Mechanical Efficiency ($\eta_m$):**This relates the theoretical power required to operate the pump (assuming no friction or other mechanical losses) to the actual power delivered to the pump shaft. It accounts for energy losses due to friction between moving parts within the pump, such as bearings, gears, pistons, and seals, as well as fluid turbulence and viscous drag.

-**Volumetric Efficiency ($\eta_v$):**This relates the actual flow rate delivered by the pump to the theoretical flow rate that would be delivered if there were no internal leakage. It accounts for fluid losses due to internal leakage within the pump, caused by clearances between moving parts, compressibility of the fluid, and pressure-induced deformation of pump components.

-**Overall Efficiency ($\eta_o$):**This represents the total energy conversion efficiency of the pump and is the product of the mechanical and volumetric efficiencies. It reflects the ratio of hydraulic output power to mechanical input power, encompassing all energy losses within the pump.

Energy losses in a pump are unavoidable consequences of real-world operation. Friction converts mechanical energy into heat, while internal leakage reduces the amount of fluid effectively delivered to the system. These losses reduce the overall efficiency of the pump and must be carefully considered during system design and pump selection. By understanding the different types of efficiency and the factors that influence them, engineers can choose the most appropriate pump for a given application and optimize its performance to minimize energy consumption and maximize system effectiveness.**Example ProblemsProblem 1:** A hydraulic pump consumes 25 kW of electrical power and delivers 22 kW of hydraulic power. Calculate the overall efficiency.

*Solution:* Overall efficiency is given by $\eta_o = \frac{\mathcal{P}_{hydraulic}}{\mathcal{P}_{input}}$.
Substituting the values, we get $\eta_o = \frac{22 \text{ kW}}{25 \text{ kW}} = 0.88 = 88\%$.

**Problem 2:** A hydraulic pump operates with an overall efficiency of 85% and is driven by a 50 hp motor. Determine the hydraulic power output. Note: 1 hp = 0.7457 kW.

*Solution:* $\mathcal{P}_{input} = 50 \text{ hp} \times 0.7457 \frac{\text{kW}}{\text{hp}} = 37.285 \text{ kW}$. We have $\eta_o = \frac{\mathcal{P}_{hydraulic}}{\mathcal{P}_{input}}$, therefore $\mathcal{P}_{hydraulic} = \eta_o \times \mathcal{P}_{input} = 0.85 \times 37.285 \text{ kW} = 31.69 \text{ kW}$.

**Problem 3:** Discuss qualitatively how increasing fluid viscosity or pump speed influences overall efficiency.

*Solution:* Increasing fluid viscosity generally increases frictional losses within the pump, reducing mechanical efficiency. However, it can also reduce internal leakage, improving volumetric efficiency. The overall effect on overall efficiency depends on the balance between these two opposing effects. At low speeds, the reduction in leakage may outweigh the increase in friction, leading to a slight improvement in overall efficiency. At higher speeds, the increased frictional losses typically dominate, resulting in a decrease in overall efficiency.

### 2.2 Mechanical Efficiency (Expanded)

Mechanical efficiency is a critical metric that quantifies the energy losses within a hydraulic pump due to friction and fluid dynamics, *excluding* losses due to leakage. These losses occur in various parts of the pump, converting mechanical energy into heat. Understanding the sources of these losses is crucial for optimizing pump design and operation.

One major source of mechanical loss is friction in bearings. Bearings are used to support rotating shafts and reduce friction, but they are not perfectly frictionless. The friction in bearings depends on the type of bearing (e.g., ball bearing, roller bearing, sleeve bearing), the load on the bearing, the lubrication conditions, and the operating speed. Similarly, seals, which prevent leakage of fluid from the pump, also contribute to friction. The friction in seals depends on the type of seal (e.g., O-ring, lip seal, mechanical seal), the pressure of the fluid, the lubrication conditions, and the relative motion between the seal and the shaft.

Friction also occurs between other mating parts within the pump. For example, in a piston pump, there is friction between the pistons and the cylinder walls. In a gear pump, there is friction between the gear teeth. In a vane pump, there is friction between the vanes and the pump housing. The amount of friction depends on the materials of the mating parts, the surface finish, the lubrication conditions, and the forces pressing the parts together.

Fluid turbulence also contributes to mechanical losses. As the fluid flows through the pump, it encounters restrictions and changes in direction. These disturbances can create turbulence, which dissipates energy as heat. The amount of turbulence depends on the flow rate, the fluid viscosity, and the geometry of the pump.

Viscous dissipation of energy arises from the internal friction within the fluid itself as it is sheared between moving surfaces. This effect is more pronounced at higher fluid viscosities and velocities. The mathematical underpinning relates to viscous forces within the fluid itself.

Consider two surfaces moving relative to each other with a fluid between them. The shear stress, $\tau$, is proportional to the velocity gradient, $\frac{du}{dy}$, where $u$ is the fluid velocity and $y$ is the distance perpendicular to the surfaces. The proportionality constant is the dynamic viscosity, $\mu$:

$\tau = \mu \frac{du}{dy}$.

The force required to overcome this shear stress is $F = \tau A = \mu A \frac{du}{dy}$, where A is the area of the surface. The power dissipated due to this viscous friction is $\mathcal{P} = F u = \mu A (\frac{du}{dy}) u$. This shows how viscosity directly contributes to power loss within the pump.

The mechanical efficiency, $\eta_m$, is defined as the ratio of the theoretical power required to operate the pump (assuming no mechanical losses) to the actual power delivered to the pump:

$\eta_{m} = \frac{\mathcal{P}_{th}}{\mathcal{P}_{act}}$

Since power is the product of torque and angular speed ($\mathcal{P} = T \omega$), we can express mechanical efficiency as:

$\eta_{m} = \frac{T_{th} \omega}{T_{act} \omega} = \frac{T_{th}}{T_{act}}$

Where $T_{th}$ is the theoretical torque and $T_{act}$ is the actual torque. The actual torque is always greater than the theoretical torque due to frictional losses. We can express this as:

$T_{act} = T_{th} + T_{friction}$

Where $T_{friction}$ represents the torque required to overcome friction within the pump. A simple model for $T_{friction}$ is:

$T_{friction} = \beta N$

Where $\beta$ is a friction coefficient that incorporates bearing friction, viscous drag, and other frictional effects, and $N$ is the pump speed in RPM. Substituting this into the equation for actual torque, we get:

$T_{act} = T_{th} + \beta N$

Finally, substituting this expression for $T_{act}$ into the equation for mechanical efficiency, we obtain:

$\eta_m = \frac{T_{th}}{T_{th} + \beta N}$

This equation shows that mechanical efficiency decreases as pump speed increases, given a constant friction coefficient.


> 📊 *Diagram: {"subject": "Cross-sectional view of a generic hydraulic pump highlighting the key areas where friction occurs: bearings, seals, and sliding surfaces. Arrows indicating direction of motion and frictional forces.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Exploded view of a radial piston pump showing the arrangement of pistons, cylinder block, and valve plate, illustrating potential friction points.", "type": "technical illustration"}*


**Example ProblemsProblem 1:** A hydraulic pump has an actual torque of 35 Nm and a theoretical torque of 32 Nm when operating at a speed of 1500 RPM. Calculate the mechanical efficiency.

*Solution:* $\eta_{m} = \frac{T_{th}}{T_{act}} = \frac{32 \text{ Nm}}{35 \text{ Nm}} = 0.914 = 91.4\%$

**Problem 2:** A hydraulic pump has a mechanical efficiency of 92% and an actual torque of 60 Nm when operating at a speed of 2000 RPM. Calculate the theoretical torque.

*Solution:* $\eta_{m} = \frac{T_{th}}{T_{act}}$, so $T_{th} = \eta_{m} \times T_{act} = 0.92 \times 60 \text{ Nm} = 55.2 \text{ Nm}$.

**Problem 3:** A hydraulic pump has a theoretical torque of 50 Nm and operates at a speed of 1200 RPM. The friction coefficient is estimated to be 0.005 Nm/RPM. Calculate the actual torque and mechanical efficiency.

*Solution:* $T_{friction} = \beta N = 0.005 \frac{\text{Nm}}{\text{RPM}} \times 1200 \text{ RPM} = 6 \text{ Nm}$.  Then, $T_{act} = T_{th} + T_{friction} = 50 \text{ Nm} + 6 \text{ Nm} = 56 \text{ Nm}$.  Finally, $\eta_{m} = \frac{T_{th}}{T_{act}} = \frac{50 \text{ Nm}}{56 \text{ Nm}} = 0.893 = 89.3\%$.

### 2.3 Volumetric Efficiency

Volumetric efficiency, denoted as $\eta_v$, is a crucial performance indicator for hydraulic pumps, quantifying the pump's ability to deliver fluid at its intended flow rate without significant losses due to internal leakage. It represents the ratio of the *actual* flow rate delivered by the pump to the *theoretical* flow rate that would be delivered if there were no internal leakage.

Internal leakage is the primary cause of volumetric losses. It occurs due to clearances between moving parts within the pump. These clearances are necessary for lubrication and to prevent seizing, but they also provide a path for fluid to leak from the high-pressure side of the pump to the low-pressure side. Common leakage paths include the clearances between pistons and cylinders in piston pumps, between gear teeth in gear pumps, and between the valve plate and cylinder block in various pump designs.

The rate of internal leakage is influenced by several factors, including the magnitude of the pressure difference between the high and low pressure sides, the size and geometry of the clearances, the viscosity of the fluid, and the temperature of the fluid. Higher pressures generally lead to increased leakage rates, as the pressure differential forces more fluid through the clearances. Larger clearances also result in higher leakage rates, as they provide a less restrictive flow path. Fluid viscosity plays a significant role; more viscous fluids tend to leak less readily than less viscous fluids. Temperature also affects leakage, as fluid viscosity decreases with increasing temperature, leading to higher leakage rates.

The concept of volumetric efficiency is directly related to the principle of mass conservation, often expressed as the continuity equation. In the context of a hydraulic pump, the continuity equation states that the mass flow rate entering the pump must equal the mass flow rate exiting the pump, plus any mass flow rate due to internal leakage. Mathematically, this can be expressed as $Q_{in} = Q_{out} + Q_{leakage}$, where $Q_{in}$ is the mass flow rate entering the pump, $Q_{out}$ is the mass flow rate exiting the pump, and $Q_{leakage}$ is the mass flow rate due to internal leakage. Volumetric efficiency provides a practical measure of how significant $Q_{leakage}$ is relative to $Q_{out}$.

The formal definition of volumetric efficiency is given by:

$\eta_{v} = \frac{Q_{act}}{Q_{th}}$

Where $Q_{act}$ is the actual flow rate delivered by the pump and $Q_{th}$ is the theoretical flow rate. The theoretical flow rate can be calculated as the product of the pump displacement volume, $V_D$ (the volume of fluid displaced per revolution or cycle), and the pump speed, $N$:

$Q_{th} = V_D N$

The actual flow rate is always less than the theoretical flow rate due to internal leakage. Therefore, we can express the actual flow rate as:

$Q_{act} = Q_{th} - Q_{leakage}$

Substituting this into the equation for volumetric efficiency, we get:

$\eta_{v} = \frac{Q_{th} - Q_{leakage}}{Q_{th}} = 1 - \frac{Q_{leakage}}{Q_{th}}$

To further develop this, we can approximate the leakage flow rate as a function of pressure, clearance, and fluid viscosity. Approximating the flow through the small clearances as laminar flow through a narrow channel, we can use a simplified version of Darcy's Law. Assume $Q_{leakage} = \alpha p$, where $\alpha$ is a leakage coefficient that encompasses geometric factors (clearance dimensions, channel length) and fluid viscosity. This is a simplification, as the actual leakage flow may be more complex and influenced by factors not explicitly included in this model. However, it provides a useful approximation for understanding the relationship between pressure and leakage.

Substituting $Q_{leakage} = \alpha p$ into the equation for volumetric efficiency, we get:

$\eta_v = 1 - \frac{\alpha p}{V_D N}$

This equation shows that volumetric efficiency decreases as pressure increases and increases as pump speed increases. It also highlights the importance of minimizing the leakage coefficient, $\alpha$, through tight manufacturing tolerances and proper fluid selection.


> 📊 *Diagram: {"subject": "Schematic diagram illustrating internal leakage paths within a gear pump. Arrows showing direction of leakage flow.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Cutaway view of a piston pump, highlighting the clearance between the piston and cylinder bore, where leakage occurs.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Microscopic view of the clearance between two sliding surfaces, illustrating the fluid flow and pressure distribution within the gap.", "type": "technical illustration"}*


**Example ProblemsProblem 1:** A hydraulic pump delivers an actual flow rate of 35 liters per minute (LPM) while its theoretical flow rate is 40 LPM. Calculate the volumetric efficiency.

*Solution:* $\eta_{v} = \frac{Q_{act}}{Q_{th}} = \frac{35 \text{ LPM}}{40 \text{ LPM}} = 0.875 = 87.5\%$

**Problem 2:** A hydraulic pump has a volumetric efficiency of 95% and a theoretical flow rate of 50 LPM. Calculate the actual flow rate.

*Solution:* $\eta_{v} = \frac{Q_{act}}{Q_{th}}$, so $Q_{act} = \eta_{v} \times Q_{th} = 0.95 \times 50 \text{ LPM} = 47.5 \text{ LPM}$.

**Problem 3:** A hydraulic pump has a displacement volume of 10 cm3/rev and operates at a speed of 1200 RPM. The pump is operating at a pressure of 10 MPa, and the leakage coefficient is estimated to be 5e-12 m5/Ns. Calculate the volumetric efficiency.

*Solution:* First, convert the displacement volume to m3/rev: $V_D = 10 \frac{\text{cm}^3}{\text{rev}} \times (\frac{1 \text{ m}}{100 \text{ cm}})^3 = 10 \times 10^{-6} \frac{\text{m}^3}{\text{rev}}$. Convert the speed to rev/s: $N = 1200 \frac{\text{RPM}}{60 \frac{\text{s}}{\text{min}}} = 20 \frac{\text{rev}}{\text{s}}$. Calculate the theoretical flow rate: $Q_{th} = V_D N = 10 \times 10^{-6} \frac{\text{m}^3}{\text{rev}} \times 20 \frac{\text{rev}}{\text{s}} = 2 \times 10^{-4} \frac{\text{m}^3}{\text{s}}$. Calculate the leakage flow rate: $Q_{leakage} = \alpha p = 5 \times 10^{-12} \frac{\text{m}^5}{\text{Ns}} \times 10 \times 10^6 \text{ Pa} = 5 \times 10^{-5} \frac{\text{m}^3}{\text{s}}$. Finally, calculate the volumetric efficiency: $\eta_v = 1 - \frac{Q_{leakage}}{Q_{th}} = 1 - \frac{5 \times 10^{-5} \frac{\text{m}^3}{\text{s}}}{2 \times 10^{-4} \frac{\text{m}^3}{\text{s}}} = 1 - 0.25 = 0.75 = 75\%$.

### 2.4 Overall Efficiency

Overall efficiency, often denoted as $\eta_o$, represents the comprehensive energy conversion effectiveness of a hydraulic pump. It takes into account *all* energy losses within the pump, encompassing both mechanical and volumetric inefficiencies. Essentially, it reflects the ratio of the useful hydraulic power output to the mechanical power input required to drive the pump.

Mathematically, overall efficiency is simply the product of mechanical efficiency ($\eta_m$) and volumetric efficiency ($\eta_v$):

$\eta_{o} = \eta_{m} \eta_{v}$

This relationship highlights that the overall efficiency is limited by both the frictional losses within the pump (represented by mechanical efficiency) and the internal leakage losses (represented by volumetric efficiency). If either of these efficiencies is low, the overall efficiency will be significantly reduced.

Overall efficiency can also be expressed directly in terms of power. It's defined as the ratio of the hydraulic power output ($\mathcal{P}_{hydraulic}$) to the mechanical power input ($\mathcal{P}_{input}$):

$\eta_{o} = \frac{\mathcal{P}_{hydraulic}}{\mathcal{P}_{input}}$

The hydraulic power output is the product of the pressure ($p$) and the *actual* flow rate ($Q_{act$):

$\mathcal{P}_{hydraulic} = p Q_{act}$

The mechanical power input is the product of the torque ($T_{act}$) applied to the pump shaft and the angular speed ($\omega$) of the shaft:

$\mathcal{P}_{input} = T_{act} \omega$

Substituting these expressions into the equation for overall efficiency, we get:

$\eta_{o} = \frac{p Q_{act}}{T_{act} \omega}$

Combining this with the product of mechanical and volumetric efficiencies, we can write:

$\eta_{o} = \eta_{m} \eta_{v} = \frac{p Q_{act}}{T_{act} \omega}$

This equation provides a direct link between the pump's internal efficiencies and its overall performance characteristics, linking actual measurable parameters ($p$, $Q_{act}$, $T_{act}$, $\omega$) to $\eta_o$.


> 📊 *Diagram: {"subject": "Block diagram showing the energy flow through a hydraulic pump, from input mechanical power to output hydraulic power, illustrating the losses associated with mechanical and volumetric inefficiencies.", "type": "technical illustration"}*


**Example ProblemsProblem 1:** A hydraulic pump has a mechanical efficiency of 90% and a volumetric efficiency of 85%. Calculate the overall efficiency.

*Solution:* $\eta_{o} = \eta_{m} \eta_{v} = 0.90 \times 0.85 = 0.765 = 76.5\%$

**Problem 2:** A hydraulic pump operates with an overall efficiency of 75%, delivering an actual flow rate of 30 LPM at a pressure of 12 MPa. Calculate the required input power in kW.

*Solution:* First, calculate the hydraulic power output: $\mathcal{P}_{hydraulic} = p Q_{act} = 12 \times 10^6 \text{ Pa} \times 30 \frac{\text{L}}{\text{min}} \times \frac{1 \text{ m}^3}{1000 \text{ L}} \times \frac{1 \text{ min}}{60 \text{ s}} = 60,000 \text{ W} = 6 \text{ kW}$. Then, calculate the input power: $\eta_{o} = \frac{\mathcal{P}_{hydraulic}}{\mathcal{P}_{input}}$, so $\mathcal{P}_{input} = \frac{\mathcal{P}_{hydraulic}}{\eta_{o}} = \frac{6 \text{ kW}}{0.75} = 80 \text{ kW}$.

**Problem 3:** A hydraulic pump requires an input torque of 25 Nm and operates at a speed of 1500 RPM. It delivers an actual flow rate of 40 LPM at a pressure of 8 MPa. Calculate the overall efficiency.

*Solution:* First, calculate the hydraulic power output: $\mathcal{P}_{hydraulic} = p Q_{act} = 8 \times 10^6 \text{ Pa} \times 40 \frac{\text{L}}{\text{min}} \times \frac{1 \text{ m}^3}{1000 \text{ L}} \times \frac{1 \text{ min}}{60 \text{ s}} = 5333.33 \text{ W} = 5.33 \text{ kW}$. Then, calculate the input power: $\mathcal{P}_{input} = T_{act} \omega = 25 \text{ Nm} \times 1500 \text{ RPM} \times \frac{2\pi \text{ rad}}{1 \text{ rev}} \times \frac{1 \text{ min}}{60 \text{ s}} = 3926.99 \text{ W} = 3.93 \text{ kW}$. Then, calculate the actual power: $\eta_{o} = \frac{\mathcal{P}_{hydraulic}}{\mathcal{P}_{input}} = \frac{5.33 \text{ kW}}{3.93 \text{ kW}} = 0.738 = 73.8\%$.