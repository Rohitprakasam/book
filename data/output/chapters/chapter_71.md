---
title: "Chapter 71"
author: "BookForge Draft"
---

## 1. Linear Actuators (Hydraulic Cylinders)

### 1.1 Introduction

Linear actuators, commonly referred to as hydraulic cylinders, are fundamental components in a wide range of engineering applications. Their primary function is to convert fluid power, typically in the form of pressurized hydraulic oil, into linear mechanical motion. This conversion enables the exertion of significant forces over considerable distances, making hydraulic cylinders indispensable in heavy machinery, construction equipment, manufacturing processes, and more.

The basic construction of a hydraulic cylinder consists of a cylindrical barrel, a piston that slides within the barrel, a piston rod attached to the piston that extends out of the cylinder, seals to prevent fluid leakage, and end caps to enclose the barrel. Pressurized hydraulic fluid is introduced into the cylinder, acting on the piston's surface area. This creates a force that pushes the piston along the barrel, resulting in linear movement of the piston rod. The key advantage of hydraulic systems, and thus hydraulic cylinders, lies in their ability to multiply force. A relatively small amount of pressure applied over a small area can generate a much larger force over a larger area. This force multiplication is directly related to Pascal's Law, which states that pressure applied to a confined fluid is transmitted equally in all directions throughout the fluid. This principle allows hydraulic cylinders to exert tremendous forces, exceeding those achievable by pneumatic or electromechanical actuators of similar size.


> 📊 *Diagram: {"subject": "Cross-sectional view of a double-acting hydraulic cylinder, clearly labeling the barrel, piston, rod, rod seals, piston seals, fluid ports (A and B), and end caps. Show pressure acting on both sides of the piston.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Simplified schematic symbol for a double-acting hydraulic cylinder.", "type": "technical illustration"}*


The relationship between pressure, area, and force in a hydraulic cylinder is governed by the following equation, which is a direct application of Pascal's Law. Pressure is defined as force per unit area. Therefore, the force *F* exerted by a hydraulic cylinder is equal to the pressure *p* of the hydraulic fluid multiplied by the effective area *A* upon which the pressure acts:

$F = pA$

This equation holds true for both the extension and retraction strokes of a double-acting cylinder, but the effective area *A* differs between the two strokes. During extension, the pressurized fluid acts on the entire area of the piston face. During retraction, the pressurized fluid acts on the area of the piston face *minus* the cross-sectional area of the piston rod. This difference in area results in different forces during extension and retraction for the same applied pressure.

The relationship between cylinder displacement, area, and volume is also important. The volume *V* of fluid required to move the piston a distance *x* (the displacement) is given by:

$V = Ax$

Where A is again the effective area upon which the pressure acts. This area may be the entire bore, or the bore minus the rod area.

**Example Problems:**1.**Cylinder Force Problem:** A hydraulic cylinder has a bore diameter ($D_{bore}$) of 100 mm and a rod diameter ($D_{rod}$) of 40 mm. The hydraulic pressure (*p*) is 15 MPa. Calculate the force exerted by the cylinder during extension and retraction.

    - **Extension:**- Area of piston: $A_{ext} = \pi (D_{bore}/2)^2 = \pi (0.1 m / 2)^2 = 0.00785 m^2$
        - Force during extension: $F_{ext} = p A_{ext} = 15 \times 10^6 Pa \cdot 0.00785 m^2 = 117,750 N = 117.75 kN$
    -**Retraction:**- Area of rod: $A_{rod} = \pi (D_{rod}/2)^2 = \pi (0.04 m / 2)^2 = 0.00126 m^2$
        - Effective area during retraction: $A_{ret} = A_{ext} - A_{rod} = 0.00785 m^2 - 0.00126 m^2 = 0.00659 m^2$
        - Force during retraction: $F_{ret} = p A_{ret} = 15 \times 10^6 Pa \cdot 0.00659 m^2 = 98,850 N = 98.85 kN$

2.**Cylinder Pressure Problem:** A hydraulic cylinder with a bore diameter ($D_{bore}$) of 150 mm is required to exert a force (*F*) of 30 kN. Calculate the required hydraulic pressure (*p*).

    - Area of piston: $A = \pi (D_{bore}/2)^2 = \pi (0.15 m / 2)^2 = 0.01767 m^2$
    - Required pressure: $p = F / A = 30,000 N / 0.01767 m^2 = 1,698,925 Pa = 1.7 MPa$

3. **Cylinder Speed Problem:**A cylinder has a bore diameter $D_{bore}$ of 80mm and a rod diameter $D_{rod}$ of 30mm. The flow rate $Q$ is 40 LPM. Calculate the extension and retraction speeds.

    - Extension:
        - Area of the piston: $A_{ext} = \pi * (D_{bore}/2)^2 = \pi * (0.08 m / 2)^2 = 0.00503 m^2$
        - Convert flow rate to $m^3/s$: $Q = 40 \frac{L}{min} * \frac{1 m^3}{1000 L} * \frac{1 min}{60 s} = 0.000667 \frac{m^3}{s}$
        - Extension Speed: $v_{ext} = Q / A_{ext} = 0.000667 \frac{m^3}{s} / 0.00503 m^2 = 0.133 \frac{m}{s}$
    - Retraction:
        - Area of the rod: $A_{rod} = \pi * (D_{rod}/2)^2 = \pi * (0.03 m / 2)^2 = 0.000707 m^2$
        - Effective Area: $A_{ret} = A_{ext} - A_{rod} = 0.00503 m^2 - 0.000707 m^2 = 0.00432 m^2$
        - Retraction Speed: $v_{ret} = Q / A_{ret} = 0.000667 \frac{m^3}{s} / 0.00432 m^2 = 0.154 \frac{m}{s}$

4.**Cylinder Rod Area Problem:** A cylinder with a bore diameter of 120mm needs to have a 2kN force difference between extension and retraction at a pressure of 20 MPa. Calculate the required rod diameter.
    - Area of piston: $A_{ext} = \pi * (D_{bore}/2)^2 = \pi * (0.12 m / 2)^2 = 0.01131 m^2$
    - Force during extension: $F_{ext} = p * A_{ext} = 20 * 10^6 Pa * 0.01131 m^2 = 226200 N$
    - Required Retraction Force: $F_{ret} = F_{ext} - 2000 N = 226200 N - 2000 N = 224200 N$
    - Required retraction area: $A_{ret} = F_{ret} / p = 224200 N / (20 * 10^6 Pa) = 0.01121 m^2$
    - Required Rod Area: $A_{rod} = A_{ext} - A_{ret} = 0.01131 m^2 - 0.01121 m^2 = 0.0001 m^2$
    - Required Rod Diameter: $D_{rod} = \sqrt{4 * A_{rod} / \pi} = \sqrt{4 * 0.0001 m^2 / \pi} = 0.0113 m = 11.3 mm$