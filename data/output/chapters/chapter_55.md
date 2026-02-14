---
title: "Chapter 55"
author: "BookForge Draft"
---

## 2. Losses in Fittings

### 2.1 Head Loss Introduction

When a fluid flows through a pipe or a complex piping system, it experiences a reduction in its total head. Total head refers to the sum of the pressure head, velocity head, and elevation head. This reduction is known as head loss ($h_L$) and represents the energy dissipated due to friction within the fluid and between the fluid and the pipe walls. The concept of head loss is fundamentally linked to the first law of thermodynamics, specifically the conservation of energy. As the fluid moves, some of its mechanical energy is converted into internal energy, primarily due to frictional forces arising from viscous effects and turbulence. This conversion manifests as a temperature increase in the fluid, although often negligible.

Friction arises from two primary sources: viscous forces within the fluid itself and the interaction between the fluid and the pipe walls. In laminar flow, viscous forces dominate, leading to a more orderly and predictable energy dissipation. However, in turbulent flow, chaotic mixing and eddy formation significantly increase frictional losses. Head losses are broadly classified into two categories: major losses and minor losses. Major losses occur due to friction along the straight sections of the pipe, while minor losses arise from fittings such as valves, elbows, tees, and changes in pipe diameter.

The flow regime, whether laminar or turbulent, dramatically affects the magnitude of head loss. Laminar flow, characterized by smooth, layered movement of fluid particles, typically results in lower head losses compared to turbulent flow, where chaotic mixing and eddy formation lead to significantly higher frictional losses. Accurate estimation of head loss is crucial in designing efficient piping systems, ensuring adequate flow rates, and minimizing energy consumption.


> 📊 *Diagram: {"subject": "Schematic of a pipe section showing pressure drop, velocity profile, and head loss. Include labels for inlet pressure (p1), outlet pressure (p2), inlet velocity (v1), outlet velocity (v2), pipe diameter (D), and length (L). Add a zoomed-in section showing the velocity gradient near the pipe wall.", "type": "technical illustration"}*


We can derive a basic form of head loss starting from the Work-Energy Theorem.  Consider a fluid element moving through a pipe from point 1 to point 2. The work done on the fluid element is the integral of pressure with respect to volume:

$W = \int_{V_1}^{V_2} p \, dV$

This work is equal to the change in kinetic and potential energy plus the energy dissipated by friction (which is our head loss term):

$W = \Delta KE + \Delta PE + E_{loss}$

Where:
$\Delta KE = \frac{1}{2} m (v_2^2 - v_1^2)$
$\Delta PE = mg(z_2 - z_1)$
$E_{loss} = mgh_L$

Substituting and dividing by mass $m = \rho V = \rho A L$, we obtain a simplified energy equation:

$\frac{p_1}{\rho} - \frac{p_2}{\rho} = \frac{1}{2}(v_2^2 - v_1^2) + g(z_2 - z_1) + gh_L$

Rearranging and dividing by g, we get an expression where all terms are in units of length (head):

$(\frac{p_1}{\rho g} + \frac{v_1^2}{2g} + z_1) - (\frac{p_2}{\rho g} + \frac{v_2^2}{2g} + z_2) = h_L$

This shows that the difference in total head between two points is the head loss.

For Newtonian fluids, the relationship between shear stress ($\tau$) and viscosity ($\mu$) is given by:

$\tau = \mu \frac{du}{dy}$

Where $du/dy$ is the velocity gradient.  This equation highlights that shear stress is proportional to the viscosity of the fluid and the rate of change of velocity with respect to distance.  This relationship is fundamental in understanding how viscous forces contribute to head loss.

For non-circular ducts, we use the concept of hydraulic diameter ($D_h$) to approximate the behavior of circular pipes. The hydraulic diameter is defined as:

$D_h = \frac{4A}{P}$

Where $A$ is the cross-sectional area of the duct and $P$ is the wetted perimeter.  Using the hydraulic diameter allows us to apply equations developed for circular pipes to non-circular geometries, providing a practical approach for engineering calculations.

**Example Problem 1:**Water flows through a horizontal pipe with a diameter of 50 mm. The inlet pressure is 300 kPa, and the inlet velocity is 3 m/s. The outlet velocity is 1.5 m/s. Calculate the head loss between the two points. Assume the density of water is 1000 kg/m³ and g = 9.81 m/s².

1.**Apply the energy equation:**

$(\frac{p_1}{\rho g} + \frac{v_1^2}{2g} + z_1) - (\frac{p_2}{\rho g} + \frac{v_2^2}{2g} + z_2) = h_L$

Since the pipe is horizontal, $z_1 = z_2$, so those terms cancel.  We also know $p_1$ and need to find $p_2$. We can rearrange the equation as:

$h_L = (\frac{p_1 - p_2}{\rho g}) + (\frac{v_1^2 - v_2^2}{2g})$

We are given $p_1$ but not $p_2$.  The problem implies that we can solve *directly* for head loss assuming pressure drops to zero.  In many problems you would need to first find $p_2$. We'll assume $p_2$ is atmospheric pressure for this problem and convert our values.

$p_1 = 300 kPa = 300,000 Pa$

2.  **Calculate the head loss:**$h_L = (\frac{300000 - 101325}{1000 * 9.81}) + (\frac{3^2 - 1.5^2}{2 * 9.81}) = 20.25 + 0.34 = 20.59 m$

The head loss between the two points is 20.59 meters.**Example Problem 2:**Oil (specific gravity = 0.9) flows through an inclined pipe with a diameter of 75 mm. The inlet pressure is 200 kPa, the inlet velocity is 2 m/s, and the inlet elevation is 5 m. The outlet pressure is 150 kPa, and the outlet elevation is 8 m. Calculate the head loss.

1.**Calculate the density of the oil:**$\rho = specific\, gravity * \rho_{water} = 0.9 * 1000 kg/m^3 = 900 kg/m^3$

2.**Apply the energy equation:**

$(\frac{p_1}{\rho g} + \frac{v_1^2}{2g} + z_1) - (\frac{p_2}{\rho g} + \frac{v_2^2}{2g} + z_2) = h_L$

$h_L = (\frac{200000}{900 * 9.81} + \frac{2^2}{2 * 9.81} + 5) - (\frac{150000}{900 * 9.81} + \frac{2^2}{2 * 9.81} + 8) = (22.65 + 0.20 + 5) - (16.99 + 0.20 + 8) = 27.85 - 25.19 = 2.66 m$

The head loss between the two points is 2.66 meters.

### 2.2 Frictional Losses in Laminar Flow

Laminar flow is characterized by the smooth, layered movement of fluid particles, with minimal mixing between adjacent layers. This flow regime typically occurs at relatively low velocities and high viscosities, resulting in a low Reynolds number. The Reynolds number ($Re$) is a dimensionless quantity that represents the ratio of inertial forces to viscous forces within the fluid. In laminar flow, viscous forces dominate, suppressing the formation of turbulence. Understanding and predicting head losses in laminar flow is critical in various engineering applications, including microfluidics, lubrication systems, and the transport of viscous fluids.

The Hagen-Poiseuille equation provides an analytical solution for calculating head loss in laminar flow through circular pipes. This equation is derived from the Navier-Stokes equations under specific assumptions, including: the fluid is Newtonian (meaning its viscosity is constant), the flow is steady (meaning the flow parameters do not change with time), the flow is incompressible (meaning the fluid density is constant), the flow is fully developed (meaning the velocity profile is no longer changing with the pipe length), and the pipe is horizontal. While these assumptions represent an ideal scenario, the Hagen-Poiseuille equation offers a valuable approximation for many practical situations.


> 📊 *Diagram: {"subject": "Schematic of a pipe showing laminar flow, with parabolic velocity profile. Indicate the maximum velocity at the center and zero velocity at the wall. Show pressure gradient along the pipe length. Add labels for pipe diameter (D), length (L), and velocity profile (v(r)).", "type": "schematic"}*


Starting with the Navier-Stokes equations for incompressible flow, we can simplify them based on the assumptions of steady, fully developed laminar flow in a circular pipe. In cylindrical coordinates (r, θ, x), and considering only axial flow (vx) that varies with radius, the Navier-Stokes equations reduce to:

$0 = -\frac{dp}{dx} + \mu (\frac{1}{r}\frac{d}{dr}(r\frac{dv_x}{dr}))$

Integrating this equation twice with respect to *r*, and applying boundary conditions (velocity is finite at r=0, and velocity is zero at r=R, where R is the pipe radius), we obtain the velocity profile:

$v(r) = \frac{1}{4\mu}\frac{dp}{dx}(R^2 - r^2)$

This equation describes a parabolic velocity profile, with the maximum velocity at the center of the pipe (r=0) and zero velocity at the wall (r=R).

To obtain the volumetric flow rate (*Q*), we integrate the velocity profile over the cross-sectional area of the pipe:

$Q = \int_0^R v(r) 2\pi r \, dr = \frac{\pi R^4}{8\mu} (-\frac{dp}{dx})$

Relating the pressure drop ($\Delta p$) to head loss ($h_L$) using the fluid density ($\rho$) and gravitational acceleration (*g*):

$h_L = \frac{\Delta p}{\rho g}$

Substituting the expression for pressure drop from the flow rate equation, we get the Hagen-Poiseuille equation:

$h_L = \frac{32 \mu L v}{\rho g D^2} = \frac{128 \mu L Q}{\pi \rho g D^4}$

Where L is the pipe length, *v* is the average fluid velocity, and D is the pipe diameter.

Finally, the friction factor (*f*) for laminar flow can be derived from the Hagen-Poiseuille equation and Darcy-Weisbach equation. This results in:

$f = \frac{64}{Re}$

Where $Re = \frac{\rho v D}{\mu}$ is the Reynolds number.

**Example Problem 1:**Oil flows laminarly through a horizontal pipe with a diameter of 12 mm and a length of 2 m. The flow rate is 50 mL/min, and the fluid viscosity is 0.2 Pa.s. Calculate the pressure drop and head loss. Assume the density of the oil is 850 kg/m³ and g = 9.81 m/s².

1.**Convert units and calculate the average velocity:**$Q = 50 \frac{mL}{min} = 50 * \frac{10^{-6} m^3}{60 s} = 8.33 * 10^{-7} m^3/s$
$v = \frac{Q}{A} = \frac{8.33 * 10^{-7} m^3/s}{\pi * (0.006 m)^2} = 0.00737 m/s$

2.**Calculate the pressure drop using the Hagen-Poiseuille equation (rearranged):**$\Delta p = \frac{128 \mu L Q}{\pi D^4} = \frac{128 * 0.2 Pa.s * 2 m * 8.33 * 10^{-7} m^3/s}{\pi * (0.012 m)^4} = 7745 Pa$

3.**Calculate the head loss:**$h_L = \frac{\Delta p}{\rho g} = \frac{7745 Pa}{850 kg/m^3 * 9.81 m/s^2} = 0.927 m$

The pressure drop is 7745 Pa, and the head loss is 0.927 meters.**Example Problem 2:**Glycerin flows laminarly through an inclined pipe (15-degree angle with the horizontal) with a diameter of 10 mm and a length of 1.5 m. The pressure drop is 30 kPa, and the fluid viscosity is 1.0 Pa.s. Calculate the flow rate. Assume the density of glycerin is 1260 kg/m³ and g = 9.81 m/s².

1.**Account for the inclination.**The Hagen-Poiseuille equation, as derived, assumes a horizontal pipe. When the pipe is inclined, we must consider the elevation change in the pressure drop calculation. We need to calculate the change in hydrostatic pressure.

$\Delta p_{hydrostatic} = \rho g L sin(\theta) = 1260 kg/m^3 * 9.81 m/s^2 * 1.5 m * sin(15^\circ) = 4804 Pa$

2.**Calculate the pressure drop due to friction only:**$\Delta p_{friction} = \Delta p_{total} - \Delta p_{hydrostatic} = 30000 Pa - 4804 Pa = 25196 Pa$

3.**Calculate the flow rate using the Hagen-Poiseuille equation (rearranged):**

$Q = \frac{\pi D^4 \Delta p_{friction}}{128 \mu L} = \frac{\pi * (0.01 m)^4 * 25196 Pa}{128 * 1.0 Pa.s * 1.5 m} = 4.11 * 10^{-7} m^3/s$

The flow rate is $4.11 * 10^{-7} m^3/s$, or 24.66 mL/min.

### 2.3 Frictional Losses in Turbulent Flow

Turbulent flow is characterized by chaotic, three-dimensional motion of fluid particles, resulting in significant mixing and eddy formation. This flow regime typically occurs at relatively high velocities and low viscosities, leading to a high Reynolds number. In turbulent flow, inertial forces dominate, promoting the instability and breakdown of laminar flow patterns. Modeling turbulent flow analytically is extremely challenging due to its inherent complexity and randomness. As a result, empirical correlations and numerical simulations are often employed to estimate head losses in turbulent flow.

Unlike laminar flow, where the friction factor can be expressed by a simple analytical formula, the friction factor in turbulent flow is a function of both the Reynolds number and the relative roughness of the pipe. The relative roughness represents the ratio of the average height of the roughness elements on the pipe's inner surface (ε) to the pipe's inside diameter (*D*): $\epsilon/D$. The roughness elements disrupt the smooth flow patterns near the pipe wall, increasing the frictional resistance and contributing to higher head losses.


> 📊 *Diagram: {"subject": "Schematic of a pipe showing turbulent flow, with fluctuating velocity profile. Illustrate the turbulent boundary layer and the effect of roughness elements on the flow. Add labels for pipe diameter (D), length (L), roughness height (epsilon), and velocity fluctuations.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "A simplified Moody Chart plotting friction factor (f) vs. Reynolds number (Re) for different relative roughness values (epsilon/D).  Label key regions (laminar, transition, fully turbulent).", "type": "chart"}*


The time-averaged Navier-Stokes equations, also known as the Reynolds-Averaged Navier-Stokes (RANS) equations, are a common approach to modeling turbulent flow. These equations involve time-averaging the flow variables, resulting in additional terms called Reynolds stresses, which represent the effects of turbulence on the mean flow. Solving the RANS equations requires turbulence models to approximate the Reynolds stresses, introducing further complexity and uncertainty.

The roughness of the pipe wall, denoted by *ks* or ε, plays a crucial role in turbulent flow. The relative roughness, defined as $\epsilon/D$, quantifies the impact of these roughness elements on the flow. Roughness elements disrupt the laminar sublayer near the wall, increasing turbulence and energy dissipation.

Empirical correlations, such as the Colebrook equation, are widely used to estimate the friction factor in turbulent flow:

$\frac{1}{\sqrt{f}} = -2 \log_{10} (\frac{\epsilon/D}{3.7} + \frac{2.51}{Re\sqrt{f}})$

The Colebrook equation is implicit in *f*, meaning it must be solved iteratively. Simplified explicit approximations of the Colebrook equation, such as the Swamee-Jain equation, provide a more direct way to estimate the friction factor, although with some loss of accuracy.

**Example Problem 1:**Water flows turbulently through a commercial steel pipe with a diameter of 50 mm and a length of 10 m. The flow rate is 2 L/s. Calculate the pressure drop and head loss using the Moody chart. Use $\epsilon = 0.046 mm$ for commercial steel. Assume the density of water is 1000 kg/m³ and the dynamic viscosity is $1*10^{-3}$ Pa.s, g = 9.81 m/s².

1.**Calculate the average velocity:**$Q = 2 L/s = 0.002 m^3/s$
$v = \frac{Q}{A} = \frac{0.002 m^3/s}{\pi (0.025 m)^2} = 1.018 m/s$

2.**Calculate the Reynolds number:**$Re = \frac{\rho v D}{\mu} = \frac{1000 kg/m^3 * 1.018 m/s * 0.05 m}{1 * 10^{-3} Pa.s} = 50900$

3.**Calculate the relative roughness:**$\frac{\epsilon}{D} = \frac{0.046 * 10^{-3} m}{0.05 m} = 0.00092$

4.**Determine the friction factor using the Moody chart (or Colebrook equation):**From the Moody chart, for $Re = 50900$ and $\frac{\epsilon}{D} = 0.00092$, we estimate $f \approx 0.021$ (approximate since reading from a chart introduces error.)

5.**Calculate the head loss using the Darcy-Weisbach equation:**$h_L = f \frac{L}{D} \frac{v^2}{2g} = 0.021 * \frac{10 m}{0.05 m} * \frac{(1.018 m/s)^2}{2 * 9.81 m/s^2} = 0.219 m$

6.**Calculate the pressure drop:**$\Delta p = \rho g h_L = 1000 kg/m^3 * 9.81 m/s^2 * 0.219 m = 2148 Pa$

The head loss is 0.219 m, and the pressure drop is 2148 Pa.**Example Problem 2:**Air flows through a galvanized iron duct with a diameter of 100 mm and a length of 15 m. The pressure drop is 500 Pa. Calculate the flow rate using the Moody chart. Use $\epsilon = 0.15 mm$ for galvanized iron. Assume the density of air is 1.2 kg/m³ and the dynamic viscosity is $1.8 * 10^{-5}$ Pa.s, g = 9.81 m/s².

1.**Assume a friction factor *f*.**This problem requires iteration. We'll start with an initial guess of $f = 0.02$.

2.**Rearrange the Darcy-Weisbach equation to solve for velocity:**$h_L = \frac{\Delta p}{\rho g} = f \frac{L}{D} \frac{v^2}{2g}$

$v = \sqrt{\frac{2g h_L D}{f L}} = \sqrt{\frac{2 \Delta p D}{\rho f L}}$

$v = \sqrt{\frac{2 * 500 Pa * 0.1 m}{1.2 kg/m^3 * 0.02 * 15 m}} = 23.57 m/s$

3.**Calculate the Reynolds number:**$Re = \frac{\rho v D}{\mu} = \frac{1.2 kg/m^3 * 23.57 m/s * 0.1 m}{1.8 * 10^{-5} Pa.s} = 157133$

4.**Calculate the relative roughness:**$\frac{\epsilon}{D} = \frac{0.15 * 10^{-3} m}{0.1 m} = 0.0015$

5.**Determine the friction factor using the Moody chart (or Colebrook equation) with the calculated Re and relative roughness:**From the Moody chart, for $Re = 157133$ and $\frac{\epsilon}{D} = 0.0015$, we estimate $f \approx 0.022$.

6.**Compare the calculated *f* to the assumed *f*. If they are significantly different, repeat steps 2-5 using the new value of *f*.**In this case, 0.022 is close to our initial guess of 0.02, but to increase precision, we'll iterate once more with f = 0.022.
$v = \sqrt{\frac{2 * 500 Pa * 0.1 m}{1.2 kg/m^3 * 0.022 * 15 m}} = 22.44 m/s$
$Re = \frac{1.2 kg/m^3 * 22.44 m/s * 0.1 m}{1.8 * 10^{-5} Pa.s} = 149600$
From the Moody chart, with the updated Re, we still find f is approximately 0.022.

7.**Calculate the flow rate:**

$Q = v * A = 22.44 m/s * \pi (0.05 m)^2 = 0.176 m^3/s$

The flow rate is approximately 0.176 m³/s.

### 2.4 Minor Losses in Fittings

Minor losses represent the head losses that occur due to flow disturbances created by fittings in a piping system. These fittings include components such as valves, elbows, tees, sudden expansions, and sudden contractions. Unlike major losses, which are distributed along the length of the pipe, minor losses are typically localized at the point where the fitting is located. The magnitude of minor losses depends on the geometry of the fitting and the flow conditions.

Minor losses are often quantified using a loss coefficient, denoted by *K*. The loss coefficient is an empirical parameter that relates the head loss to the kinetic energy of the flow. It essentially captures the resistance to flow caused by the fitting.


> 📊 *Diagram: {"subject": "Schematic of a 90-degree elbow showing the flow separation and recirculation zones. Indicate the pressure drop across the elbow.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Schematic of a gate valve showing the flow restriction and pressure drop. Show different valve opening positions and their corresponding flow patterns.", "type": "schematic"}*


> 📊 *Diagram: {"subject": "Schematic of a sudden contraction in a pipe showing the flow separation and vena contracta.", "type": "schematic"}*


The loss coefficient is primarily determined experimentally, as the complex flow patterns within fittings make analytical modeling difficult. Different types of fittings have different loss coefficients, and the loss coefficient for a particular fitting may also vary depending on the flow rate and other factors. Engineering handbooks and manufacturers' catalogs typically provide tables and charts listing loss coefficients for various fittings.

The loss coefficient ($K$) is defined as:

$K = \frac{h_L}{(v^2/2g)}$

Where $h_L$ is the head loss due to the fitting, *v* is the average flow velocity in the pipe, and *g* is the acceleration due to gravity. This equation shows that the loss coefficient relates the head loss to the kinetic energy of the flow.

The equation for minor losses is given by:

$h_L = K \frac{v^2}{2g}$

This equation allows us to calculate the head loss due to a fitting if we know the loss coefficient and the average flow velocity.

**Example Problem 1:**Water flows through a pipe with a 90-degree elbow. The pipe diameter is 50 mm, and the flow rate is 3 L/s. The loss coefficient for the elbow is 0.9. Calculate the head loss due to the elbow. Assume g = 9.81 m/s².

1.**Calculate the average velocity:**$Q = 3 L/s = 0.003 m^3/s$
$v = \frac{Q}{A} = \frac{0.003 m^3/s}{\pi (0.025 m)^2} = 1.528 m/s$

2.**Calculate the head loss:**$h_L = K \frac{v^2}{2g} = 0.9 * \frac{(1.528 m/s)^2}{2 * 9.81 m/s^2} = 0.107 m$

The head loss due to the elbow is 0.107 meters.**Example Problem 2:**

Air flows through a pipe with a sudden contraction. The upstream diameter is 100 mm, and the downstream diameter is 50 mm. The flow rate is 0.05 m³/s. The loss coefficient for the contraction is 0.4. Calculate the head loss due to the contraction. Assume g = 9.81 m/s². The *downstream* velocity is used for calculating loss in contractions.

1.  **Calculate the downstream velocity:**$A_2 = \pi r_2^2 = \pi (.025 m)^2 = 0.00196 m^2$
$v_2 = \frac{Q}{A_2} = \frac{0.05 m^3/s}{0.00196 m^2} = 25.51 m/s$

2.**Calculate the head loss:**

$h_L = K \frac{v_2^2}{2g} = 0.4 * \frac{(25.51 m/s)^2}{2 * 9.81 m/s^2} = 13.30 m$

The head loss due to the contraction is 13.30 meters.