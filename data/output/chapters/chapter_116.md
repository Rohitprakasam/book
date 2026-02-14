---
title: "Chapter 116"
author: "BookForge Draft"
---

A command signal from the servo amplifier is directed to the two coils of the permanent magnet torque motor. A differential current is established in the coil which deflects the armature by an amount proportional to the command. The deflection of the armature is mechanically transmitted to the pilot spool by means of a stiff connecting wire. Thus mechanical displacement of the pilot spool is directly proportional to the command received by the torque motor. The direction of movement is determined by the torque motor coil having the larger current.
When the pilot spool moves to the left, a flow of oil is metered to the end N of the main spool. The control pressure acting continuously on area (M) is acting now at both the ends. Since the effective area of the left hand end of the spool is twice that of the right hand end (due to the presence of a rod on the right hand end of the spool), the main spool shifts towards the right. The supply pressure is to be directed to port (A) to actuate the hydraulic cylinder in a direction, proportional to the electrical signal.
The spool in the proportional valve is acted upon by a spring at one end and a proportional solenoid at the other end. Thus, it is possible to control the force on the spool electrically and the orifice size can be varied in accordance to the control current. The flow from the valve is proportional to the current flowing through the solenoid.
Using notched spool or overlap spool in the proportional valve gives better control of the flow rate as the orifice is progressively opened. Due to difficulties in manufacturing zero ,lap spool, i.e., one in which the land on the spool is exactly the same length as the port in the valve body, overlapped spools are used in proportional spool valves. This means that the spool has to move a distance equal to the overlap before any flow occurs through the valve. This gives rise to a 'dead zone' in the valve characteristic.
Spool Position Control.
In order to increase the accuracy of proportional control valves, a linear transducer is fitted to measure the spool position. The output from the transducer is a voltage which is proportional to the spool displacement, continuously varying through the total spool movement. The actual position of the spool is fed back via the transducer to the electrical control system and compared with the required position, the control current being adjusted accordingly.
Proportional Pressure Relief Valves.
In conventional pressure relief valves, a compression spring is used to control the pressure at which the valve operates. This spring is replaced by a DC solenoid in the case of a proportional valve.

--- Page 112 ---

### 1. Torque Motor Fundamentals

### 1.1 Theoretical Introduction:

Torque motors are a specialized type of electric motor designed to deliver high torque at low speeds, or even at a standstill. In the context of proportional valves, they serve as precise actuators, converting an electrical command signal into a mechanical displacement. This displacement, in turn, controls the position of a pilot spool, which regulates the flow of hydraulic fluid. The basic principle behind a torque motor's operation is rooted in the interaction between a magnetic field and an electric current. Specifically, when a current-carrying conductor is placed within a magnetic field, it experiences a force, as described by the Lorentz force law. In a torque motor, this force is harnessed to generate rotational torque.

Permanent magnets play a crucial role in establishing the magnetic field within the torque motor. They offer several advantages, including simplicity (no external power supply required for the field), compactness, and relatively high magnetic field strength. However, they also have limitations, such as the inability to dynamically adjust the magnetic field strength and susceptibility to demagnetization at high temperatures.

The stiff connecting wire that transmits the armature's deflection to the pilot spool is a critical component. Its stiffness directly affects the responsiveness and accuracy of the valve. A stiffer wire provides a more direct and immediate transfer of motion, minimizing backlash and improving the valve's ability to track the command signal. However, excessive stiffness can increase the required torque from the motor and potentially lead to mechanical stress and wear. Finding the optimal stiffness is a key design consideration.

### 1.2 Mathematical Derivations:

The torque ($F_{spring}$) produced by a torque motor can be derived from the fundamental principles of electromagnetism. Consider a single loop of wire carrying a current ($A_{spool}$) placed in a magnetic field ($p_{out}$). The force on a small segment of the wire is given by the Lorentz force law. Integrating this force over the entire loop, and considering that the wire loop has $F_{spring} = p_{out} \times A_{spool}$ turns and an area $k$, one can derive the equation for the torque:

$x$

where:

- $F_{spring} = k \times x$ is the current in amperes (A).
- $k \times x = p_{out} \times A_{spool}$ is the magnetic field strength in teslas (T).
- $p_{out} = (k \times x) / A_{spool}$ is the number of turns in the coil.
- $F_{mag}$ is the area of the coil in square meters (m^2).
- $i$ is the angle between the magnetic field vector and the area vector of the coil.

The angle $F_{mag} = K_{sol} \times i$ plays a critical role. When $K_{sol}$, the torque is maximized, and when $F_{mag} = p_{out} \times A_{spool}$ or $F_{mag}$, the torque is zero.

The torque generated by the motor results in an angular displacement ($K_{sol} \times i = p_{out} \times A_{spool}$) of the armature. The relationship between the torque and the angular displacement is governed by the stiffness ($p_{out} = (K_{sol} \times i) / A_{spool}$) of the connecting wire:

$K_{sol} = 0.3 \, \text{N/mA}$

where:

- $i = 250 \, \text{mA}$ is the torsional stiffness of the connecting wire, measured in Newton-meters per radian (Nm/rad).
- $F_{mag} = K_{sol} \times i$ is the angular displacement of the armature in radians.

Combining these equations, we can relate the current in the coil to the angular displacement of the armature:

$F_{mag} = 0.3 \, \text{N/mA} \times 250 \, \text{mA} = 75 \, \text{N}$

This equation highlights the key parameters that influence the motor's performance. By controlling the current ($75 \, \text{N}$), one can precisely control the angular displacement ($A_{spool} = 15 \, \text{mm}^2$), which in turn controls the position of the pilot spool.

### 1.3 Mirror Problems:

- **Problem 1: Torque Calculation:**A torque motor has the following parameters: $K_{sol} = 0.2 \, \text{N/mA}$ turns, $i = 300 \, \text{mA}$, $A_{spool} = 15 \, \text{mm}^2 = 15 \times 10^{-6} \, \text{m}^2$, $p_{out} = (K_{sol} \times i) / A_{spool}$, and $p_{out} = (0.2 \, \text{N/mA} \times 300 \, \text{mA}) / (15 \times 10^{-6} \, \text{m}^2) = 60 \, \text{N} / (15 \times 10^{-6} \, \text{m}^2) = 4 \times 10^6 \, \text{N/m}^2 = 4 \, \text{MPa}$. Calculate the torque produced by the motor.

    - Solution:
        - $4 \, \text{MPa}$
        - $p_s$
        - $p_s/2$
-**Problem 2: Angular Displacement:**A torque motor has the following parameters: $\delta$ turns, $\Delta p$, $x$, $x = K \Delta p$, $\Delta p = K_{flapper} \times \delta$, and $K_{flapper}$. Calculate the angular displacement of the armature.

    - Solution:
        - $p_s = 20 \, \text{MPa}$
        - $\delta = 0.01 \, \text{mm}$
        - $K_{flapper} = 5 \times 10^8 \, \text{Pa/m}$
-**Problem 3: Stiffness Selection:**A torque motor needs to achieve an angular displacement of $\Delta p = K_{flapper} \times \delta = (5 \times 10^8 \, \text{Pa/m}) \times (0.01 \times 10^{-3} \, \text{m}) = 5 \times 10^3 \, \text{Pa} = 5 \, \text{kPa}$ at a current of $A_{s} = 20 \, \text{mm}^2$. The motor has $\mu=10 \, \text{Ns/m}$ turns, $\Delta p \cdot A_s = \mu \cdot v = \mu \cdot \frac{dx}{dt}$, and $x$, and $m \ddot{x} + \mu \dot{x} + kx = \Delta p A_s$. Find the required wire stiffness $m$.

    - Solution:
        - $x$
        - $k$
        - $x = \Delta p \cdot A_s / k$
        - $v = \frac{\Delta p \cdot A_s}{\mu} = \frac{5 kPa \cdot 20 mm^2}{10 Ns/m} = \frac{5 \cdot 10^3 Pa \cdot 20 \cdot 10^{-6} m^2}{10 Ns/m} = 0.01 m/s$

### 1.4 Diagram Needs:

json
[
  {
    "subject": "Cross-sectional view of a torque motor, showing the permanent magnet, coil, armature, and connecting wire. Indicate the direction of current flow, magnetic field lines, and torque.",
    "type": "technical illustration"
  },
  {
    "subject": "A schematic representation of the torque motor connected to the pilot spool of the valve.",
    "type": "schematic diagram"
  }
]


### 1.5 Variable Consistency Dictionary:

- Current: $Q$
- Magnetic Field Strength: $x$
- Number of Coil Turns: $\Delta p$
- Coil Area: $Q = C_d \cdot A(x) \cdot \sqrt{\frac{2 \Delta p}{\rho}}$
- Torque: $C_d$
- Angular Displacement: $A(x)$
- Connecting Wire Stiffness: $\rho$
- Angle between magnetic field and coil area vector: $V_{in}$

### 2. Proportional Valve Spool Dynamics

### 2.1 Theoretical Introduction:

The main spool within a proportional valve is responsible for directing the flow of hydraulic fluid to the actuator. Its movement is governed by a force balance, which is influenced by several factors, including the pressure acting on both ends of the spool and the presence of a rod on one side. This rod reduces the effective area on one side of the spool, creating an area differential that is crucial for proper valve operation.

The pilot pressure, controlled by the torque motor and pilot spool, acts on one end of the main spool (end N). The control pressure acts on both ends (M), but because of the area differential created by the rod, the net force exerted by the control pressure is different on each end. This differential force, combined with the force from the pilot pressure, determines the net force on the spool and, consequently, its displacement. The area ratio, typically 2:1, is a key design parameter that affects the sensitivity and stability of the valve. A larger area ratio provides a greater force differential for a given pilot pressure, leading to increased sensitivity. However, it can also make the valve more susceptible to instability and oscillations.

### 2.2 Mathematical Derivations:

Let $x$ be the area of the main spool end without the rod, and $x = K_v \cdot V_{in}$ be the area of the main spool end with the rod. In many proportional valves, the design incorporates $K_v$. Let $C_d = 0.7$ be the pressure at end N (pilot pressure) and $x = 2 \, \text{mm}$ be the control pressure acting on both ends. The net force ($A(x) = 10 \, \text{mm}^2$) on the main spool is given by:

$\Delta p = 5 \, \text{MPa}$

Since $\rho = 850 \, \text{kg/m}^3$, the equation simplifies to:

$A(x) = 10 \, \text{mm}^2 = 10 \times 10^{-6} \, \text{m}^2$.

If we introduce a spring with spring constant $\Delta p = 5 \, \text{MPa} = 5 \times 10^6 \, \text{Pa}$, the net force equation becomes:

$Q = C_d \cdot A(x) \cdot \sqrt{\frac{2 \Delta p}{\rho}}$

where $Q = 0.7 \cdot (10 \times 10^{-6} \, \text{m}^2) \cdot \sqrt{\frac{2 \cdot 5 \times 10^6 \, \text{Pa}}{850 \, \text{kg/m}^3}} = 0.7 \cdot (10 \times 10^{-6} \, \text{m}^2) \cdot \sqrt{11764.7 \, \text{m}^2/\text{s}^2} = 0.7 \cdot (10 \times 10^{-6} \, \text{m}^2) \cdot 108.47 \, \text{m/s} = 7.59 \times 10^{-4} \, \text{m}^3/\text{s} = 0.759 \, \text{L/s}$ is the spool displacement. At equilibrium ($0.759 \, \text{L/s}$):

$K_v = 0.5 \, \text{mm/V}$

This equation shows how the spool displacement is directly related to the pilot pressure ($V_{in} = 4 \, \text{V}$) and inversely related to the spring constant ($x = K_v \cdot V_{in}$).

### 2.3 Mirror Problems:

-**Problem 1: Net Force Calculation:**Given $x = 0.5 \, \text{mm/V} \cdot 4 \, \text{V} = 2 \, \text{mm}$, $2 \, \text{mm}$, and %%MATH_78%%, calculate the net force on the main spool.

    - Solution:
        - %%MATH_79%%
	    - %%MATH_80%%
        - %%MATH_81%%
        - %%MATH_82%%
-**Problem 2: Spool Displacement:**Given %%MATH_83%%, %%MATH_84%%, %%MATH_85%%, and %%MATH_86%%, calculate the spool displacement.

    - Solution:
        - %%MATH_87%%
	    - %%MATH_88%%
        - %%MATH_89%%
        - %%MATH_90%%
-**Problem 3: Pressure Required:**Given a desired spool displacement of %%MATH_91%%, %%MATH_92%%, %%MATH_93%%, and %%MATH_94%%, calculate the pressure %%MATH_95%% required to achieve the desired displacement.

    - Solution:
        - %%MATH_96%%
        - %%MATH_97%%
        - %%MATH_98%%
        - %%MATH_99%%
        - %%MATH_100%%
        - %%MATH_101%%

### 2.4 Diagram Needs:

json
[
  {
    "subject": "A cross-sectional view of the main spool, showing the areas %%MATH_102%% and %%MATH_103%%, the pressure %%MATH_104%% acting on area %%MATH_105%%, the pressure %%MATH_106%% acting on the other end and the presence of the rod. Indicate the direction of spool movement for a given %%MATH_107%%.",
    "type": "technical illustration"
  },
  {
    "subject": "Illustrate the effect of the spring on the spool.",
    "type": "schematic diagram"
  }
]


### 2.5 Variable Consistency Dictionary:

- Pressure at end N: %%MATH_108%%
- Control Pressure: %%MATH_109%%
- Area of spool end 1: %%MATH_110%%
- Area of spool end 2: %%MATH_111%%
- Net Force: %%MATH_112%%
- Spool Displacement: %%MATH_113%%
- Spring Constant: %%MATH_114%%

### 3. Proportional Solenoid Valve Characteristics

### 3.1 Theoretical Introduction:

Proportional solenoid valves offer a direct electrical means of controlling hydraulic flow. The core component is a solenoid, an electromagnetic actuator that generates a force proportional to the current flowing through its coil. This force is directly applied to the spool, allowing precise positioning and control of the orifice size within the valve. By varying the current, the solenoid's force changes, resulting in a corresponding change in spool position and, ultimately, the flow rate through the valve.

The relationship between the current and the resulting force is governed by the principles of electromagnetism. The current creates a magnetic field, which in turn exerts a force on a ferromagnetic core (the spool) within the solenoid. The strength of the magnetic field, and therefore the force, is directly proportional to the current and the number of turns in the solenoid coil. This direct relationship allows for accurate and repeatable control of the hydraulic flow.

### 3.2 Mathematical Derivations:

The magnetic field strength (%%MATH_115%%) produced by a solenoid is given by:

%%MATH_116%%

where:

- %%MATH_117%% is the current in the solenoid in amperes (A).
- %%MATH_118%% is the number of turns in the solenoid coil.
- %%MATH_119%% is the length of the solenoid in meters (m).
- %%MATH_120%% is the permeability of free space (%%MATH_121%%).

The force (%%MATH_122%%) exerted by the solenoid on the spool is related to the magnetic field strength and the effective area (%%MATH_123%%) of the solenoid:

%%MATH_124%%

The flow rate (%%MATH_125%%) through the valve is related to the orifice area (%%MATH_126%%) and the pressure drop (%%MATH_127%%) across the valve by the orifice equation:

%%MATH_128%%

where:

- %%MATH_129%% is the discharge coefficient (typically between 0.6 and 0.8).
- %%MATH_130%% is the fluid density in kilograms per cubic meter (kg/m^3).

We also need to relate the orifice area to the spool displacement. We can assume a linear relationship near the operating point such that %%MATH_131%%.

### 3.3 Mirror Problems:

-**Problem 1: Solenoid Force Calculation:**A solenoid has the following parameters: %%MATH_132%%, %%MATH_133%% turns, %%MATH_134%%, and %%MATH_135%%. Calculate the force exerted by the solenoid.

    - Solution:
        - %%MATH_136%%
        - %%MATH_137%%
        - %%MATH_138%%
-**Problem 2: Flow Rate Calculation:**A valve has the following parameters: %%MATH_139%%, %%MATH_140%%, %%MATH_141%%, and %%MATH_142%%. Calculate the flow rate through the valve.

    - Solution:
        - %%MATH_143%%
        - %%MATH_144%%
        - %%MATH_145%%
-**Problem 3: Current Required:** Given a desired flow rate of %%MATH_146%%, %%MATH_147%%, %%MATH_148%%, %%MATH_149%%, %%MATH_150%% where %%MATH_151%%, and the solenoid parameters: %%MATH_152%% turns, %%MATH_153%%, and %%MATH_154%%. We also assume %%MATH_155%% where %%MATH_156%%. Calculate the current %%MATH_157%% required to achieve that flow rate.

    - Solution:
        - %%MATH_158%%
        - %%MATH_159%%
        - %%MATH_160%%
        - %%MATH_161%%
        - %%MATH_162%%
        - %%MATH_163%%

### 3.4 Diagram Needs:

json
[
  {
    "subject": "A cross-sectional view of the proportional solenoid valve, showing the solenoid, spool, orifice, and direction of flow. Indicate the magnetic field lines and force exerted by the solenoid.",
    "type": "technical illustration"
  },
  {
    "subject": "Illustrate the change in orifice area as a function of spool displacement.",
    "type": "graphical representation"
  }
]


### 3.5 Variable Consistency Dictionary:

- Solenoid Current: %%MATH_164%%
- Magnetic Field Strength (Solenoid): %%MATH_165%%
- Number of Solenoid Turns: %%MATH_166%%
- Solenoid Length: %%MATH_167%%
- Permeability of Free Space: %%MATH_168%%
- Solenoid Force: %%MATH_169%%
- Effective Area: %%MATH_170%%
- Flow Rate: %%MATH_171%%
- Orifice Area: %%MATH_172%%
- Pressure Drop: %%MATH_173%%
- Discharge Coefficient: %%MATH_174%%
- Fluid Density: %%MATH_175%%
- Orifice Gain Factor: %%MATH_176%%
- Spool Displacement: %%MATH_177%%
- Spring constant: %%MATH_178%%

### 4. Spool Overlap and Dead Zone

### 4.1 Theoretical Introduction:

Spool overlap is a design feature in proportional valves where the land on the spool is wider than the port in the valve body. This means that the spool has to move a certain distance before any flow is allowed through the valve. The distance the spool must move before flow begins is known as the *overlap distance*. This intentional overlap creates a "dead zone" in the valve's operation, where small changes in the input signal (e.g., control current) do not result in any change in the output flow rate.

The primary reason for using overlapped spools is to improve the valve's stability and prevent leakage when the valve is in the neutral position. In a zero-lap spool valve, where the land and port are exactly the same length, even the slightest spool movement can cause flow, which can lead to instability and oscillations in the system. Additionally, manufacturing a perfect zero-lap spool is extremely difficult and costly. Overlap ensures that the valve is completely closed when the spool is centered, minimizing leakage and improving energy efficiency. However, the dead zone introduced by the overlap can also be a disadvantage, particularly in applications requiring high precision and responsiveness.

### 4.2 Mathematical Derivations:

Let %%MATH_179%% represent the overlap distance. The flow rate (%%MATH_180%%) as a function of spool displacement (%%MATH_181%%) can be described by a piecewise function:

$Q = \begin{cases}
0, & |x| < w_{overlap} \\
P_{d} V_{o}(x) \sqrt{\frac{2 \Delta r}{\rho}}, & x > w_{overlap} \text{ or } x < -w_{overlap}
\end{cases}$

where:

- %%MATH_182%% is the overlap distance.
- %%MATH_183%% is the discharge coefficient.
- %%MATH_184%% is the orifice area as a function of displacement.
- %%MATH_185%% is the pressure drop across the valve.
- %%MATH_186%% is the fluid density.

Assuming a linear relationship between the orifice area and spool displacement beyond the overlap:

%%MATH_187%%

The flow rate can now be expressed as:

$Q = \begin{cases}
0, & |x| < w_{overlap} \\
P_{d} k_A (|x| - w_{overlap}) \sqrt{\frac{2 \Delta r}{\rho}}, & x > w_{overlap} \text{ or } x < -w_{overlap}
\end{cases}$

### 4.3 Mirror Problems:

- **Problem 1: Dead Zone Calculation:**A proportional valve has an overlap distance of %%MATH_188%%. Determine the range of input signals (spool displacement) for which the valve will not produce any flow.  Assuming that the spool displacement is linearly related to the solenoid current with a gain of %%MATH_189%%, what is the corresponding dead zone current range?

    - Solution: The valve will not produce any flow when %%MATH_190%%. This means the dead zone extends from -0.3 mm to +0.3 mm.
    - The gain is %%MATH_191%%. The minimum current is therefore %%MATH_192%%. The current dead zone extends from -0.15 A to +0.15 A.

-**Problem 2: Flow Rate with Overlap:**A valve has %%MATH_193%%, %%MATH_194%%, %%MATH_195%%, %%MATH_196%%, and a spool displacement of %%MATH_197%%. The gain factor is %%MATH_198%%. Calculate the flow rate through the valve.

    - Solution:
	    - %%MATH_199%%
	    - %%MATH_200%%
        - Since %%MATH_201%%, we use the flow rate equation:
        - %%MATH_202%%
        - %%MATH_203%%
        - %%MATH_204%%

-**Problem 3: Overlap Impact:**Compare flow rate vs displacement for a zero-lap spool and an overlapped spool valve with %%MATH_205%% given a pressure drop of 5 MPa = %%MATH_206%%, fluid density of 900 kg/m^3, %%MATH_207%% and %%MATH_208%%. Evaluate flow rate at %%MATH_209%%.

    - Solution:
        -**Zero-Lap Spool:**- %%MATH_210%%
            - At %%MATH_211%%:  %%MATH_212%%
            - At %%MATH_213%%:  %%MATH_214%%
            - At %%MATH_215%%:  %%MATH_216%%
            - At %%MATH_217%%:  %%MATH_218%%
        -**Overlapped Spool:**
            - At %%MATH_219%%:  %%MATH_220%% (since %%MATH_221%%)
            - At %%MATH_222%%:  %%MATH_223%% (since %%MATH_224%%)
            - At %%MATH_225%%:  %%MATH_226%%
            - At %%MATH_227%%:  %%MATH_228%%

### 4.4 Diagram Needs:

json
[
  {
    "subject": "A cross-sectional view of a valve with an overlapped spool, showing the overlap distance %%MATH_229%%. Indicate the dead zone region.",
    "type": "technical illustration"
  },
  {
    "subject": "A graph of flow rate versus spool displacement, illustrating the dead zone caused by the overlap.",
    "type": "graphical representation"
  }
]


### 4.5 Variable Consistency Dictionary:

- Overlap Distance: %%MATH_230%%
- Flow Rate: %%MATH_231%%
- Spool Displacement: %%MATH_232%%
- Discharge Coefficient: %%MATH_233%%
- Pressure Drop: %%MATH_234%%
- Fluid Density: %%MATH_235%%
- Orifice Area as Function of Displacement: %%MATH_236%%
- Orifice Gain Factor: %%MATH_237%%

### 5. Spool Position Control with Feedback

### 5.1 Theoretical Introduction:

To enhance the accuracy and responsiveness of proportional control valves, a spool position control system is often implemented. This system utilizes a linear transducer to continuously measure the actual position of the spool. The transducer generates an electrical signal (voltage) that is proportional to the spool's displacement. This signal is then fed back to the electrical control system, creating a closed-loop control system.

In a closed-loop system, the actual spool position is compared with the desired position (command signal). The difference between these two positions, known as the error signal, is used to adjust the control current applied to the valve's actuator (e.g., solenoid). If the spool is not in the desired position, the control system will adjust the current to move it closer to the target. This continuous feedback loop ensures that the spool accurately tracks the command signal, minimizing errors and improving the valve's overall performance. This is the foundation of closed-loop control, a technique widely used in engineering to achieve precise and stable control of systems.

### 5.2 Mathematical Der