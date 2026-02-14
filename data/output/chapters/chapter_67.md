---
title: "Chapter 67"
author: "BookForge Draft"
---

3.  Overall Efficiency (ηo)

    The overall efficiency of a hydraulic system is a critical parameter that encapsulates all the energy losses occurring within the system's components. It provides a comprehensive measure of how effectively the system converts input power into useful output power. In essence, it's the product of volumetric and mechanical efficiencies, reflecting the combined impact of leakage and friction.

    Mathematically, overall efficiency is defined as the ratio of output power to input power, expressed as a percentage. Since hydraulic systems invariably experience energy losses due to factors like fluid friction within valves and pipes, internal leakage within pumps and motors, and mechanical friction between moving parts, the overall efficiency is always less than 100% in real-world scenarios. Understanding and optimizing overall efficiency is paramount for designing energy-efficient hydraulic systems, reducing operating costs, and minimizing environmental impact. The pursuit of higher efficiency translates to lower energy consumption, reduced heat generation, and extended component lifespan.

    This section will explore overall efficiency in detail, starting with its mathematical definition and the relationship between volumetric and mechanical efficiencies. Furthermore, this section will delve into several example problems and calculations to demonstrate its practical application.

    $\eta_{o}$: The overall efficiency considers all energy losses and is defined mathematically as follows:

    First, the definition of overall efficiency in a hydraulic pump is given by:

    $\eta_{o} = \eta_{v} \cdot \eta_{m}$

    Where:

    - $\eta_{o}$ is the overall efficiency.
    - $\eta_{v}$ is the volumetric efficiency.
    - $\eta_{m}$ is the mechanical efficiency.

    Using variable substitutions for copyright compliance:

    $\eta_{o} = \eta_{A} \cdot \eta_{K}$

    Where:

    - $\eta_{o}$ is the overall efficiency.
    - $\eta_{A}$ is the volumetric efficiency.
    - $\eta_{K}$ is the mechanical efficiency.

    The overall efficiency can also be expressed in terms of power:

    $\eta_{o} = \frac{\mathcal{P}_{output}}{\mathcal{P}_{input}}$

    Where:

    - $\mathcal{P}_{output}$ is the output power.
    - $\mathcal{P}_{input}$ is the input power.

    For a pump, the output power is the hydraulic power delivered to the system, and the input power is the mechanical power required to drive the pump. For a motor, the input power is the hydraulic power supplied to the motor, and the output power is the mechanical power delivered by the motor.

    $\eta_{A} = \frac{Q_{actual}}{Q_{theoretical}}$

    $\eta_{K} = \frac{T_{theoretical}}{T_{actual}}$

    Then,

    $\eta_{o} = \frac{Q_{actual}}{Q_{theoretical}} \cdot \frac{T_{theoretical}}{T_{actual}}$ (for pumps)

    $\eta_{o} = \frac{Q_{actual}}{Q_{theoretical}} \cdot \frac{T_{actual}}{T_{theoretical}}$ (for motors)

    

> 📊 *Diagram: {"subject": "Block diagram illustrating the relationship between input power, volumetric efficiency, mechanical efficiency, and output power in a hydraulic system", "type": "block diagram"}*


    **Example Problem 1:**

    A hydraulic pump has a volumetric efficiency ($\eta_{A}$) of 92% and a mechanical efficiency ($\eta_{K}$) of 87%. Calculate the overall efficiency ($\eta_{o}$). If the pump consumes 22 hp of electrical power, what is the hydraulic power output?

    *Solution:*

    1.  *Calculate overall efficiency:*
        $\eta_{o} = \eta_{A} \cdot \eta_{K}$
        $\eta_{o} = 0.92 \cdot 0.87 = 0.8004$ or 80.04%

    2.  *Calculate hydraulic power output:*
        $\mathcal{P}_{output} = \eta_{o} \cdot \mathcal{P}_{input}$
        $\mathcal{P}_{output} = 0.8004 \cdot 22 \, \text{hp} = 17.61 \, \text{hp}$

    **Example Problem 2:**

    A hydraulic motor operates with an overall efficiency ($\eta_{o}$) of 78%. If the hydraulic power input ($\mathcal{P}_{input}$) is 13 kW, what is the mechanical power output ($\mathcal{P}_{output}$)? If the motor runs at 1300 rpm, what is the output torque?

    *Solution:*

    1.  *Calculate mechanical power output:*
        $\mathcal{P}_{output} = \eta_{o} \cdot \mathcal{P}_{input}$
        $\mathcal{P}_{output} = 0.78 \cdot 13 \, \text{kW} = 10.14 \, \text{kW}$

    2.  *Calculate output torque:*
        Convert power to Watts: $\mathcal{P}_{output} = 10.14 \, \text{kW} = 10140 \, \text{W}$
        Convert speed to rad/s: $N = 1300 \, \text{rpm} = \frac{1300 \cdot 2\pi}{60} \, \text{rad/s} \approx 136.14 \, \text{rad/s}$
        Use the formula $\mathcal{P} = T \omega$ to find torque:
        $T = \frac{\mathcal{P}}{\omega} = \frac{10140}{136.14} \approx 74.48 \, \text{Nm}$

    The overall efficiency considers all energy losses and is defined mathematically as follows:

    $\eta_{o} = \eta_{v} \times \eta_{m}$

    $\eta_{o} = \frac{Q_{A}}{Q} \times \frac{pQ}{TN}$

    Using variable substitutions for copyright compliance:

    $\eta_{o} = \frac{Q_{A}}{Q} \times \frac{pR}{TN}$

    Where:

    - Q = Theoretical flow rate
    - QA = Actual flow rate

    /1714
    overall efficiency=
    100
    

    Canceling like terms yields

    /1714
     output horse power
    100
    input horse power

    output power
    100
    input power

    The overall efficiency, as a combined measure, is affected by all losses in the system, including both volumetric and mechanical losses. It's a crucial parameter for evaluating the performance of hydraulic pumps and motors and for optimizing the overall efficiency of hydraulic systems.

    The following table provides typical overall efficiency values for different pump types:

    HP
    PER
    LB
    RATIO

    OVERALL
    EFFICIENCY
    (PER CENT)

    SPEED
    RATING
    (RPM)

    PRESSURE
    RATING
    (PSI)

    FLOW
    CAPACITY
    (GPM)

    COST (DOL
    LARS PER HP)

    PUMP
    TYPE

    4-8

    80-90

    1200-
    2500

    2000-3000

    2

    EXTERNAL
    GEAR

    4-8

    70-85

    1200-
    2500

    500-2000

    2

    INTERNAL
    GEAR

    6-30

    80-95

    1200-
    1800

    1000-2000

    2

    VANE

    6-50

    90-98

    1200-
    3000

    2000-12000

    4

    AXIAL
    PISTON

    5-35

    85-95

    1200-
    1800

    3000-12000

    3

    RADIAL
    PISTON

    The volumetric efficiency is greatly affected by the following leakage losses which can rapidly accelerate due to wear.