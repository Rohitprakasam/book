---
title: "Chapter 68"
author: "BookForge Draft"
---

### 1. Leakage Around the Outer Periphery of the Gears

Gear pumps, while relatively simple and robust, are susceptible to leakage, particularly around the outer periphery of the gears. This leakage significantly impacts the pump's volumetric efficiency and overall performance. Understanding the mechanisms driving this leakage is crucial for designing and operating gear pumps effectively. This section will explore the theoretical aspects of leakage, derive relevant equations, and provide practical examples to illustrate the concepts.

### 1.1 Mechanisms of Leakage in Gear Pumps

Leakage in gear pumps primarily occurs due to the pressure difference between the high-pressure (outlet) and low-pressure (inlet) sides of the pump. This pressure differential drives fluid through the small clearances between the gear teeth and the pump housing, as well as between the sides of the gears and the side plates.

Several factors influence the leakage rate. Fluid viscosity plays a crucial role; higher viscosity fluids tend to leak less due to increased resistance to flow. However, viscosity is temperature-dependent, decreasing as temperature increases, which can lead to increased leakage at higher operating temperatures. The size of the clearances is also a critical factor. Even small increases in clearance can significantly increase leakage due to the inverse cube relationship between clearance and flow resistance (derived from the Hagen-Poiseuille equation, as shown later).

Internal leakage refers to fluid that bypasses the intended flow path within the pump and returns to the suction side. External leakage refers to fluid that escapes the pump entirely, usually through seals or joints. The leakage around the outer periphery of the gears is primarily internal leakage, although if the pump housing is not properly sealed, it can also contribute to external leakage.

The surface finish of the gear teeth and the pump housing also plays a role. Rough surfaces create more tortuous flow paths, which can increase resistance to leakage. However, achieving extremely smooth surface finishes can be costly, representing a practical trade-off.


> 📊 *Diagram: {"subject": "Cross-sectional view of a gear pump showing the leakage path between the gear tip and the pump housing. Indicate the pressure difference, radial clearance, gear rotation, and fluid flow direction using arrows. Label: \"High Pressure\", \"Low Pressure\", \"Radial Clearance (h)\", \"Leakage Flow ($Q_{leakage}$)\", \"Gear Tip\", \"Pump Housing\".", "type": "technical illustration"}*


The theoretical limits of leakage reduction are constrained by manufacturing tolerances and material properties. It is impossible to eliminate clearances entirely, and attempting to do so would lead to excessive friction and wear. Therefore, designers must carefully balance the need to minimize leakage with the need to ensure reliable pump operation.

### 1.2 Mathematical Modeling of Leakage

To quantify the leakage, we can model the gap between the gear tip and the housing as a rectangular channel. The flow rate through this channel can be approximated using the Hagen-Poiseuille equation, which is derived from the Navier-Stokes equations for laminar, incompressible flow in a pipe or channel.

We begin with the Navier-Stokes equations for incompressible flow:

$\rho \left( \frac{\partial \mathbf{v}}{\partial t} + \mathbf{v} \cdot \nabla \mathbf{v} \right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \mathbf{f}$

where:
- $\rho$ is the fluid density
- $\mathbf{v}$ is the fluid velocity vector
- $t$ is time
- $p$ is the pressure
- $\mu$ is the dynamic viscosity
- $\mathbf{f}$ is the body force vector (e.g., gravity)

Assuming steady-state flow ($\frac{\partial \mathbf{v}}{\partial t} = 0$), neglecting body forces ($\mathbf{f} = 0$), and assuming the flow is fully developed and unidirectional (only one velocity component, say $v_x$, is non-zero and depends only on the y-coordinate), the Navier-Stokes equations simplify to:

$0 = -\frac{dp}{dx} + \mu \frac{d^2v_x}{dy^2}$

Rearranging and integrating twice with respect to *y*, we get:

$\frac{d^2v_x}{dy^2} = \frac{1}{\mu} \frac{dp}{dx}$

Integrating once:

$\frac{dv_x}{dy} = \frac{1}{\mu} \frac{dp}{dx} y + C_1$

Integrating again:

$v_x(y) = \frac{1}{2\mu} \frac{dp}{dx} y^2 + C_1 y + C_2$

Applying the no-slip boundary conditions at the walls of the channel (i.e., $v_x = 0$ at $y = 0$ and $y = h$, where *h* is the height of the channel):

$v_x(0) = 0 \Rightarrow C_2 = 0$

$v_x(h) = 0 \Rightarrow 0 = \frac{1}{2\mu} \frac{dp}{dx} h^2 + C_1 h \Rightarrow C_1 = -\frac{1}{2\mu} \frac{dp}{dx} h$

Substituting $C_1$ and $C_2$ back into the velocity profile:

$v_x(y) = \frac{1}{2\mu} \frac{dp}{dx} y^2 - \frac{1}{2\mu} \frac{dp}{dx} h y = \frac{1}{2\mu} \frac{dp}{dx} (y^2 - hy)$

The average velocity, $\bar{v}$, is:

$\bar{v} = \frac{1}{h} \int_0^h v_x(y) dy = \frac{1}{h} \int_0^h \frac{1}{2\mu} \frac{dp}{dx} (y^2 - hy) dy = \frac{1}{2\mu h} \frac{dp}{dx} \left[ \frac{y^3}{3} - \frac{hy^2}{2} \right]_0^h$

$\bar{v} = \frac{1}{2\mu h} \frac{dp}{dx} \left( \frac{h^3}{3} - \frac{h^3}{2} \right) = \frac{1}{2\mu h} \frac{dp}{dx} \left( -\frac{h^3}{6} \right) = -\frac{h^2}{12\mu} \frac{dp}{dx}$

The flow rate, $Q_{leakage}$, is then:

$Q_{leakage} = \bar{v} \cdot A = \bar{v} \cdot (wh) = -\frac{h^2}{12\mu} \frac{dp}{dx} wh$

Since $\frac{dp}{dx} \approx -\frac{\Delta p}{L}$, where $\Delta p$ is the pressure difference and $L$ is the length of the channel, we get:

$Q_{leakage} = \frac{w h^3 \Delta p}{12 \mu L}$

Replacing the variables: $Q_{leakage} = \frac{w u^3 \Delta p}{12 \mu L}$.


> 📊 *Diagram: {"subject": "Schematic of the rectangular channel model representing the gap between the gear tip and housing. Label: \"Pressure $p_1$\", \"Pressure $p_2$\", \"Width (w)\", \"Height (u)\", \"Length (L)\", \"Flow Direction\". Show coordinate system.", "type": "diagram"}*


The volumetric efficiency ($\eta_v$) of the pump is defined as the ratio of the actual flow rate ($Q_{actual}$) to the theoretical flow rate ($Q_{theoretical}$). The actual flow rate is the theoretical flow rate minus the leakage flow rate:

$\eta_v = \frac{Q_{actual}}{Q_{theoretical}} = \frac{Q_{theoretical} - Q_{leakage}}{Q_{theoretical}}$

Using the equation for leakage: $\eta_v = \frac{Q_{theoretical} - \frac{w u^3 \Delta p}{12 \mu L}}{Q_{theoretical}}$.

The dynamic viscosity ($\mu$) is temperature-dependent. A common model for this relationship is:

$\mu(T) = \mu_0 e^{\beta(1/T - 1/T_0)}$

Where:
- $\mu_0$ is the viscosity at a reference temperature $T_0$
- $T$ is the current temperature
- $\beta$ is a fluid-specific constant

As temperature *T* increases, the exponent becomes more negative, and the viscosity $\mu(T)$ decreases. This decrease in viscosity leads to an increase in leakage flow rate, as seen in the $Q_{leakage}$ equation. Consequently, the volumetric efficiency decreases.

### 1.3 Example Problems

**Problem 1: Leakage Flow Rate Calculation**

A gear pump has the following dimensions: gear diameter = 75 mm, gear width (*w*) = 35 mm, radial clearance (*u*) = 25 $\mu$m = 25 x 10⁻⁶ m, channel length (*L*) = 5 mm = 0.005 m. The operating pressure ($\Delta p$) is 15 MPa = 15 x 10⁶ Pa. The fluid viscosity ($\mu$) at the operating temperature is 40 cP = 0.04 Pa·s. Calculate the leakage flow rate.

*Solution:*

Using the leakage flow rate equation:

$Q_{leakage} = \frac{w u^3 \Delta p}{12 \mu L}$

$Q_{leakage} = \frac{(0.035 \ m) \cdot (25 \times 10^{-6} \ m)^3 \cdot (15 \times 10^6 \ Pa)}{12 \cdot (0.04 \ Pa \cdot s) \cdot (0.005 \ m)}$

$Q_{leakage} = \frac{0.035 \cdot (1.5625 \times 10^{-14}) \cdot 15 \times 10^6}{12 \cdot 0.04 \cdot 0.005} \ m^3/s$

$Q_{leakage} = \frac{8.203125 \times 10^{-9}}{0.0024} \ m^3/s = 3.418 \times 10^{-6} \ m^3/s$

Converting to liters per minute (L/min):

$Q_{leakage} = 3.418 \times 10^{-6} \ m^3/s \cdot \frac{60 \ s}{1 \ min} \cdot \frac{1000 \ L}{1 \ m^3} = 0.205 \ L/min$

**Problem 2: Volumetric Efficiency Calculation**

A gear pump has a theoretical flow rate ($Q_{theoretical}$) of 25 L/min. The leakage flow rate ($Q_{leakage}$) calculated from the previous problem is 0.205 L/min. Calculate the volumetric efficiency ($\eta_v$).

*Solution:*

Using the volumetric efficiency equation:

$\eta_v = \frac{Q_{theoretical} - Q_{leakage}}{Q_{theoretical}}$

$\eta_v = \frac{25 \ L/min - 0.205 \ L/min}{25 \ L/min}$

$\eta_v = \frac{24.795 \ L/min}{25 \ L/min} = 0.9918$

Therefore, the volumetric efficiency is 99.18%.

### 1.4 Temperature Effect on Volumetric Efficiency

**Problem 3: Temperature effect on Volumetric Efficiency**

A gear pump has a theoretical flow rate ($Q_{theoretical}$) of 25 L/min. The gear pump dimensions are: gear diameter = 75 mm, gear width (*w*) = 35 mm, radial clearance (*u*) = 25 $\mu$m = 25 x 10⁻⁶ m, channel length (*L*) = 5 mm = 0.005 m. The operating pressure ($\Delta p$) is 15 MPa = 15 x 10⁶ Pa. The fluid viscosity reference ($\mu_0$) at reference temperature ($T_0$ = 40 deg C = 313.15 K) is 40 cP = 0.04 Pa·s. The Beta fluid constant ($\beta$) = 0.02. The fluid temperature ($T$) is 60 deg C = 333.15 K. Calculate the volumetric efficiency ($\eta_v$).

*Solution:*

First, calculate the viscosity at 60 deg C:

$\mu(T) = \mu_0 e^{\beta(1/T - 1/T_0)}$

$\mu(T) = 0.04 \ Pa \cdot s \cdot e^{0.02 \cdot (1/333.15 - 1/313.15)}$

$\mu(T) = 0.04 \cdot e^{0.02 \cdot (0.00300 - 0.00319)}$

$\mu(T) = 0.04 \cdot e^{0.02 \cdot (-0.00019)}$

$\mu(T) = 0.04 \cdot e^{-0.0000038} \approx 0.04 \cdot 0.9999962 \approx 0.03999985 \ Pa \cdot s$

Then, calculate leakage flow rate using the new viscosity:

$Q_{leakage} = \frac{w u^3 \Delta p}{12 \mu L} = \frac{(0.035 \ m) \cdot (25 \times 10^{-6} \ m)^3 \cdot (15 \times 10^6 \ Pa)}{12 \cdot (0.03999985 \ Pa \cdot s) \cdot (0.005 \ m)} \approx 0.20500077 \ L/min$

The change is relatively small.

Finally, calculate the volumetric efficiency:

$\eta_v = \frac{Q_{theoretical} - Q_{leakage}}{Q_{theoretical}}$

$\eta_v = \frac{25 - 0.20500077}{25} \approx 0.99179997$

The volumetric efficiency at 60 deg C is approximately 99.18%.

This shows the impact of temperature. A higher temperature decreases the viscosity, which slightly increases the leakage and decreases volumetric efficiency. This example showcases the sensitivity of leakage to changes in operating parameters.