---
title: "Chapter 56"
author: "BookForge Draft"
---

### 1. Major Energy Losses: Friction Losses in Pipes

Hydraulic systems, while efficient in transmitting power, are not without their inefficiencies. A significant portion of energy input is invariably lost during operation, primarily due to friction. This section delves into the major energy losses within hydraulic systems, focusing specifically on frictional losses within pipes, a crucial component responsible for fluid transport.

At the heart of understanding energy loss lies the fundamental principle of energy conservation. Energy cannot be created or destroyed, but it can be transformed from one form to another. In a hydraulic system, the input energy, typically in the form of mechanical energy imparted by a pump, is used to move fluid and perform work. However, as the fluid flows through the pipes, friction between the fluid layers themselves (viscosity) and between the fluid and the pipe walls acts as a resistance to motion. This resistance converts some of the mechanical energy into heat, a form of energy that is typically dissipated and unusable for performing the intended work. This conversion leads to a pressure drop along the length of the pipe, signifying a loss of potential energy that could have been used to do work at the output.

The magnitude of frictional losses is influenced by several key factors: the fluid's viscosity (its resistance to flow), the fluid's velocity, the pipe's diameter, the pipe's internal roughness, and the length of the pipe. Higher viscosity fluids offer greater resistance, leading to increased friction. Similarly, higher velocities exacerbate frictional effects. Narrower pipes increase the fluid's contact with the pipe walls, boosting friction. Rougher pipe surfaces create more turbulence and resistance. Finally, longer pipes provide a greater surface area for friction to act upon, resulting in a larger overall pressure drop. Further, the flow regime, whether laminar (smooth, layered flow) or turbulent (chaotic, swirling flow), dramatically impacts frictional losses. Turbulent flow generally leads to significantly higher friction than laminar flow.

The macroscopic effect of frictional loss is the pressure drop observed along the pipe. However, this macroscopic phenomenon arises from microscopic interactions. Consider the fluid particles near the pipe wall. These particles experience a no-slip condition, meaning they have zero velocity relative to the wall. As we move away from the wall, the velocity of the fluid particles increases. This velocity gradient results in momentum exchange between adjacent fluid layers. In laminar flow, this exchange is orderly and predictable. However, in turbulent flow, the exchange is chaotic, with fluid particles moving randomly in all directions, leading to increased momentum dissipation and thus increased energy loss.


> 📊 *Diagram: {"subject": "Schematic of a straight pipe section with labeled parameters", "type": "diagram"}*


### 1.1 Laminar Flow and the Hagen-Poiseuille Equation

In the realm of fluid dynamics, laminar flow represents a state of orderly fluid motion characterized by smooth, parallel layers, with minimal mixing between them. This regime is dominant at low flow velocities and high fluid viscosities. To quantify the pressure drop associated with laminar flow in a circular pipe, we can employ the Hagen-Poiseuille equation, a cornerstone of fluid mechanics.

The Hagen-Poiseuille equation can be derived from first principles, starting with the Navier-Stokes equations, which describe the motion of viscous fluids. For a fully developed, steady-state, laminar flow in a cylindrical pipe, the Navier-Stokes equations simplify significantly in cylindrical coordinates ($r, \theta, z$). In this case, assuming no swirl ($\theta$ component) and no acceleration in the $z$ direction, the Navier-Stokes equations reduce to:

$\frac{1}{r}\frac{d}{dr}(r\frac{dv_z}{dr}) = \frac{1}{\mu}\frac{dp}{dz}$

where $v_z$ is the velocity in the z-direction (along the pipe axis), $\mu$ is the dynamic viscosity, and $\frac{dp}{dz}$ is the pressure gradient along the pipe.

Integrating this equation once with respect to $r$ gives:

$r\frac{dv_z}{dr} = \frac{1}{2\mu}\frac{dp}{dz}r^2 + C_1$

Dividing by $r$:

$\frac{dv_z}{dr} = \frac{1}{2\mu}\frac{dp}{dz}r + \frac{C_1}{r}$

Integrating again with respect to $r$ yields:

$v_z(r) = \frac{1}{4\mu}\frac{dp}{dz}r^2 + C_1\ln(r) + C_2$

Applying boundary conditions:

1.  The velocity is finite at the center of the pipe ($r = 0$). This implies $C_1 = 0$ since $\ln(0)$ is undefined.
2.  The velocity is zero at the pipe wall ($r = R$, where $R$ is the pipe radius) due to the no-slip condition: $v_z(R) = 0$.

Therefore:

$0 = \frac{1}{4\mu}\frac{dp}{dz}R^2 + C_2$

$C_2 = -\frac{1}{4\mu}\frac{dp}{dz}R^2$

Substituting $C_2$ back into the velocity profile equation:

$v_z(r) = \frac{1}{4\mu}\frac{dp}{dz}r^2 - \frac{1}{4\mu}\frac{dp}{dz}R^2$

$v_z(r) = \frac{1}{4\mu}\frac{dp}{dz}(r^2 - R^2)$

$v_z(r) = -\frac{1}{4\mu}\frac{\Delta p}{L}(R^2 - r^2)$

This equation represents the velocity profile, which is parabolic.

To derive the flow rate $Q$, we integrate the velocity profile over the cross-sectional area of the pipe:

$Q = \int_{0}^{R} v_z(r) 2\pi r dr = \int_{0}^{R} -\frac{1}{4\mu}\frac{\Delta p}{L}(R^2 - r^2) 2\pi r dr$

$Q = -\frac{\pi \Delta p}{2\mu L} \int_{0}^{R} (R^2r - r^3) dr = -\frac{\pi \Delta p}{2\mu L} [\frac{R^2r^2}{2} - \frac{r^4}{4}]_{0}^{R}$

$Q = -\frac{\pi \Delta p}{2\mu L} (\frac{R^4}{2} - \frac{R^4}{4}) = -\frac{\pi \Delta p}{2\mu L} \frac{R^4}{4}$

$Q = \frac{\pi R^4 \Delta p}{8\mu L}$

Expressing this in terms of the pipe diameter $D = 2R$:

$Q = \frac{\pi (\frac{D}{2})^4 \Delta p}{8\mu L} = \frac{\pi D^4 \Delta p}{128\mu L}$

Therefore, the Hagen-Poiseuille equation is:

$\Delta p = \frac{128 \mu L Q}{\pi D^4}$

This equation states that the pressure drop ($\Delta p$) is directly proportional to the viscosity ($\mu$), the length of the pipe ($L$), and the flow rate ($Q$), and inversely proportional to the fourth power of the pipe diameter ($D$). This highlights the significant impact of pipe diameter on pressure drop in laminar flow.

**Example Problem 1 (Laminar Flow):**

A hydraulic system uses oil with a dynamic viscosity of 0.05 Pa.s and a specific gravity of 0.9. The oil flows through a straight pipe with a length of 5 meters and a diameter of 10 mm at a flow rate of 3 L/min. Calculate the pressure drop, assuming laminar flow. Also, verify that the flow is laminar.

*Solution:*

First, convert the flow rate to $m^3/s$:

$Q = 3 \frac{L}{min} = 3 \frac{10^{-3} m^3}{60 s} = 5 \times 10^{-5} m^3/s$

Next, apply the Hagen-Poiseuille equation:

$\Delta p = \frac{128 \mu L Q}{\pi D^4} = \frac{128 \times 0.05 \times 5 \times 5 \times 10^{-5}}{\pi \times (0.01)^4} = \frac{1.6 \times 10^{-5}}{3.14159 \times 10^{-8}} \approx 50929.58 \, Pa$

$\Delta p \approx 50.93 \, kPa$

Now, we must verify that the flow is indeed laminar by calculating the Reynolds number:

$Re = \frac{\rho v D}{\mu}$

We need to find the velocity $v$:

$v = \frac{Q}{A} = \frac{Q}{\pi (\frac{D}{2})^2} = \frac{5 \times 10^{-5}}{\pi \times (0.005)^2} = \frac{5 \times 10^{-5}}{7.854 \times 10^{-5}} \approx 0.6366 \, m/s$

The density $\rho$ can be calculated from the specific gravity:

$\rho = SG \times \rho_{water} = 0.9 \times 1000 \, kg/m^3 = 900 \, kg/m^3$

$Re = \frac{900 \times 0.6366 \times 0.01}{0.05} = \frac{5.7294}{0.05} \approx 114.59$

Since $Re < 2300$, the flow is laminar, and our assumption is valid. The pressure drop is approximately 50.93 kPa.

**Example Problem 2 (Laminar Flow):**A microfluidic device utilizes a channel with a diameter of 20 $\mu m$ and a length of 2 mm to deliver a drug solution with a viscosity of 0.0015 Pa.s. What pressure difference is required to achieve a flow rate of 1 nL/min?

First, convert all parameters to SI units:

$D = 20 \mu m = 20 \times 10^{-6} m$
$L = 2 mm = 2 \times 10^{-3} m$
$Q = 1 nL/min = 1 \times 10^{-9} L/min = \frac{1 \times 10^{-12}}{60} m^3/s = 1.667 \times 10^{-14} m^3/s$
$\mu = 0.0015 \, Pa \cdot s$

Using the Hagen-Poiseuille equation to calculate the pressure drop:
$\Delta p = \frac{128 \mu L Q}{\pi D^4} = \frac{128 (0.0015)(2 \times 10^{-3})(1.667 \times 10^{-14})}{\pi (20 \times 10^{-6})^4}$

$\Delta p = \frac{6.4 \times 10^{-18}}{5.027 \times 10^{-22}} \approx 12731 \, Pa$
$\Delta p \approx 12.73 \, kPa$

Now, let's calculate the Reynolds number to verify laminar flow: Assume the density of the drug solution is close to water, $\rho = 1000 \, kg/m^3$.
$v = \frac{Q}{A} = \frac{1.667 \times 10^{-14}}{\pi (10 \times 10^{-6})^2} = \frac{1.667 \times 10^{-14}}{3.1416 \times 10^{-10}} \approx 5.306 \times 10^{-5} \, m/s$
$Re = \frac{\rho v D}{\mu} = \frac{1000 \times 5.306 \times 10^{-5} \times 20 \times 10^{-6}}{0.0015} = \frac{1.0612 \times 10^{-6}}{0.0015} = 7.07 \times 10^{-4}$

Since Re << 2300, the flow is indeed laminar, and the Hagen-Poiseuille equation is valid. The required pressure difference is approximately 12.73 kPa.

### 1.2 Turbulent Flow and the Darcy-Weisbach Equation

When flow velocities increase and/or fluid viscosities decrease, the flow regime transitions from laminar to turbulent. Turbulent flow is characterized by chaotic, three-dimensional motion, with significant mixing and momentum transfer between fluid layers. In this regime, the Hagen-Poiseuille equation is no longer applicable. Instead, we employ the Darcy-Weisbach equation, a fundamental tool for calculating frictional head loss ($h_L$) in pipe flow, regardless of whether the flow is laminar or turbulent, though it is most commonly used in cases with significant inertial forces and Reynolds numbers.

The Darcy-Weisbach equation is given by:

$h_L = f \frac{L}{D} \frac{v^2}{2g}$

Where:

- $h_L$ is the head loss due to friction (in meters)
- $f$ is the Darcy friction factor (dimensionless)
- $L$ is the length of the pipe (in meters)
- $D$ is the hydraulic diameter of the pipe (in meters). For a circular pipe, the hydraulic diameter is simply the pipe diameter.
- $v$ is the average flow velocity (in m/s)
- $g$ is the acceleration due to gravity (approximately 9.81 m/s²)

The head loss $h_L$ can be related to the pressure drop $\Delta p$ by the following equation:

$\Delta p = \gamma h_L = \rho g h_L$

Where:

- $\gamma$ is the specific weight of the fluid ($\gamma = \rho g$)
- $\rho$ is the density of the fluid.

Substituting the Darcy-Weisbach equation for $h_L$ into the pressure drop equation, we get:

$\Delta p = f \frac{L}{D} \frac{\rho v^2}{2}$

The friction factor $f$ is a dimensionless parameter that accounts for the resistance to flow due to friction. For laminar flow ($Re < 2300$), the friction factor can be calculated directly as:

$f = \frac{64}{Re}$

However, for turbulent flow ($Re > 4000$), the friction factor is a more complex function of the Reynolds number ($Re$) and the relative roughness ($\epsilon/D$), where $\epsilon$ is the average roughness height of the pipe's inner surface. The relationship between $f$, $Re$, and $\epsilon/D$ is typically represented graphically by the Moody chart.


> 📊 *Diagram: {"subject": "Moody Chart -- Friction factor vs. Reynolds number for different relative roughness values", "type": "chart"}*


The Moody chart plots the friction factor $f$ as a function of the Reynolds number $Re$ for various values of the relative roughness $\epsilon/D$. The chart is divided into three distinct regions:

1.  Laminar flow region ($Re < 2300$): In this region, the friction factor is independent of the relative roughness and is given by $f = 64/Re$.
2.  Transition region ($2300 < Re < 4000$): This region is a transition zone between laminar and turbulent flow, and the friction factor is uncertain.
3.  Turbulent flow region ($Re > 4000$): In this region, the friction factor depends on both the Reynolds number and the relative roughness. As the Reynolds number increases, the friction factor generally decreases for a given relative roughness. However, at very high Reynolds numbers, the friction factor becomes independent of the Reynolds number and depends only on the relative roughness.

For turbulent flow, various empirical equations can approximate the friction factor, such as the Colebrook equation (implicit) or the Swamee-Jain equation (explicit). The Colebrook equation is:

$\frac{1}{\sqrt{f}} = -2.0 \log_{10} (\frac{\epsilon}{3.7D} + \frac{2.51}{Re \sqrt{f}})$

The Swamee-Jain equation is:

$f = \frac{0.25}{[log_{10}(\frac{\epsilon}{3.7D} + \frac{5.74}{Re^{0.9}})]^2}$

The Darcy-Weisbach equation provides a link between energy dissipation (represented by head loss) and the fluid flow parameters. The friction factor encapsulates the complex interactions between the fluid and the pipe wall, reflecting the energy required to overcome frictional resistance.**Example Problem 1 (Turbulent Flow, Known Friction Factor):**

Water flows through a 50-meter long pipe with a diameter of 50 mm and a roughness of 0.01 mm. The pressure drop along the pipe is 500 kPa. Assuming a friction factor of 0.02, calculate the flow rate of water through the pipe.

*Solution:*
First, we will solve for velocity, then use it to find the volumetric flow rate

Given: $L = 50 m$, $D = 0.05 m$, $\epsilon = 0.01 mm = 1 \times 10^{-5} m$, $\Delta p = 500 kPa = 500000 Pa$, $f = 0.02$
The density of water is approximately $\rho = 1000 kg/m^3$

$\Delta p = f \frac{L}{D} \frac{\rho v^2}{2}$

$500000 = 0.02 \frac{50}{0.05} \frac{1000 v^2}{2}$

$500000 = 0.02 \times 1000 \times 500 v^2 = 10000 v^2$

$v^2 = \frac{500000}{10000} = 50$

$v = \sqrt{50} \approx 7.071 m/s$

Now calculate flowrate:

$Q = v A = v \pi (\frac{D}{2})^2 = 7.071 \times \pi \times (\frac{0.05}{2})^2$

$Q = 7.071 \times \pi \times (0.025)^2 = 7.071 \times \pi \times 0.000625 \approx 0.0139 m^3/s$

$Q = 0.0139 m^3/s = 13.9 L/s$

Now, check the Reynolds number to validate the turbulent flow assumption:

$Re = \frac{\rho v D}{\mu}$

The dynamic viscosity of water is approximately $\mu = 1 \times 10^{-3} Pa \cdot s$

$Re = \frac{1000 \times 7.071 \times 0.05}{1 \times 10^{-3}} = \frac{353.55}{1 \times 10^{-3}} = 353550$

Since $Re > 4000$, the flow is turbulent, and the assumed friction factor may be a decent first approximation, depending on the accuracy needed. To refine this approximation, compare the calculated Reynolds number and pipe relative roughness with the Moody chart to find a closer value for the friction factor, then perform another iteration using the new value.

**Example Problem 2 (Turbulent Flow, Moody Chart):**

A hydraulic line with a length of 20 meters and a diameter of 25 mm carries oil with a specific gravity of 0.88 and a dynamic viscosity of 0.025 Pa.s at a flow rate of 15 L/min. The pipe has an average roughness of 0.02 mm. Determine the pressure drop in the hydraulic line.

*Solution:*

First, convert all values to SI units:
$L = 20 m$, $D = 0.025 m$, $Q = \frac{15}{60000} m^3/s = 0.00025 m^3/s$, $\epsilon = 0.02 \times 10^{-3} m = 2 \times 10^{-5} m$.
Calculate the density of the oil: $\rho = 0.88 \times 1000 = 880 kg/m^3$
Calculate flow velocity: $v = \frac{Q}{A} = \frac{0.00025}{\pi (0.025/2)^2} = \frac{0.00025}{4.9087 \times 10^{-4}} = 0.5093 m/s$

Now, calculate the Reynolds number:
$Re = \frac{\rho v D}{\mu} = \frac{880 \times 0.5093 \times 0.025}{0.025} = 880 \times 0.5093 = 448.184$
Because $Re$ is less than 2300, the flow is laminar.

The friction factor is then:
$f = \frac{64}{Re} = \frac{64}{448.184} = 0.1428$

$\Delta p = f \frac{L}{D} \frac{\rho v^2}{2} = 0.1428 \frac{20}{0.025} \frac{880 \times (0.5093)^2}{2}$
$\Delta p = 0.1428 \times 800 \times \frac{880 \times 0.2594}{2} = 0.1428 \times 800 \times 114.136 = 130005.3 \, Pa$
$\Delta p = 130005.3 \, Pa = 130.0053 \, kPa \approx 130 \, kPa$

Therefore the pressure drop in the line is approximately 130 kPa.

### 1.3 Reynolds Number and Relative Roughness

The Reynolds number and relative roughness are key dimensionless parameters that govern the nature of fluid flow and the magnitude of frictional losses in pipes.

The Reynolds number ($Re$) is a dimensionless quantity that represents the ratio of inertial forces to viscous forces within a fluid. It is defined as:

$Re = \frac{\rho v D}{\mu}$

Where:

- $\rho$ is the fluid density
- $v$ is the average fluid velocity
- $D$ is the hydraulic diameter of the pipe (equal to the pipe diameter for circular pipes)
- $\mu$ is the dynamic viscosity of the fluid

Inertial forces tend to promote turbulence, while viscous forces tend to dampen it. A low Reynolds number indicates that viscous forces dominate, leading to laminar flow. A high Reynolds number indicates that inertial forces dominate, leading to turbulent flow.

The critical Reynolds number ($Re_{crit}$) is the value at which the flow transitions from laminar to turbulent. For flow in a circular pipe, the critical Reynolds number is approximately 2300. However, it is important to note that this value is not absolute and can vary depending on factors such as the pipe's entrance conditions and the level of disturbances in the flow. Usually, 2300 < Re < 4000 is a transitional area between laminar and turbulent flow and should be avoided if possible.

The relative roughness ($\epsilon/D$) is another dimensionless parameter that characterizes the roughness of the pipe's inner surface relative to its diameter. It is defined as the ratio of the average roughness height ($\epsilon$) to the pipe diameter ($D$). A higher relative roughness indicates a rougher pipe surface.

The relative roughness affects the friction factor in turbulent flow. Rougher pipe surfaces create more turbulence and resistance, leading to higher friction factors and increased pressure drops. For laminar flow, the friction factor is independent of the relative roughness. The Moody chart graphically depicts the relationship between the friction factor, Reynolds number, and relative roughness.