---
title: "Chapter 127"
author: "BookForge Draft"
---

4. At the end of the stroke, the inhibit (cancel) limit valve is actuated to cancel the signal in the memory. This stops the extension motion and retracts the cylinder.

It is interesting to note that the signal directional control valve (four-way, double-piloted) can function as a MEMORY device. Also note that for the limit valve to provide the inhibit (cancel) function, the operator must release the manual input A or B.

Set

### Hydraulic Memory Circuits and Limit Valve Control

In hydraulic systems, "memory" refers to the ability of a circuit to maintain a specific state or output even after the initial input signal is removed. This is crucial in applications where continuous operator input is either undesirable, impractical, or poses safety concerns. Imagine a large stamping press; instead of holding a lever for the entire duration of the press cycle, the operator initiates the cycle with a brief input, and the hydraulic memory circuit ensures the press completes its operation.

One common way to achieve hydraulic memory is by using a four-way, double-piloted directional control valve (DCV). Unlike spring-centered valves that return to a neutral position when the input is removed, a double-piloted valve remains in its last shifted position. This is because the spool is held in place by pilot pressure or mechanical detents, effectively "remembering" the last command. This characteristic allows the DCV to function as a memory element. However, this memory must be controlled, which is where limit valves come into play.

Limit valves, strategically placed within the hydraulic circuit, provide feedback based on the position of a cylinder or other actuator. They act as sensors, detecting when a specific point in the stroke has been reached. These valves are crucial for implementing control logic, particularly for inhibiting or canceling the memory signal held by the DCV. They can be either normally closed (NC) or normally open (NO), depending on the desired function. A normally closed valve is closed in its default state and opens when actuated, while a normally open valve is open in its default state and closes when actuated. The selection of NC or NO depends on the specific control requirements of the circuit. The pressure and flow within the hydraulic system are what ultimately actuate these pilot lines, creating the control feedback that determines when the DCV spool shifts, thus controlling the actuator's motion.


> 📊 *Diagram: {"subject": "Schematic of a basic hydraulic memory circuit using a 4-way, double-piloted DCV. Show the manual input valves (A and B), the DCV, and the hydraulic cylinder. Clearly label the pilot lines and pressure source. Highlight the flow path during extension and retraction.", "type": "schematic diagram"}*


> 📊 *Diagram: {"subject": "Detailed cutaway view of a 4-way, double-piloted DCV, highlighting the spool, pilot ports, spring, and detents. Show how pilot pressure shifts the spool.", "type": "technical illustration"}*


> 📊 *Diagram: {"subject": "Circuit diagram showing the addition of a normally closed (NC) limit valve in the pilot line of the DCV, used to inhibit the signal. Illustrate the valve's placement relative to the cylinder and DCV.", "type": "schematic diagram"}*


> 📊 *Diagram: {"subject": "Circuit diagram showing the addition of a normally open (NO) limit valve in the pilot line of the DCV, used to inhibit the signal. Illustrate the valve's placement relative to the cylinder and DCV.", "type": "schematic diagram"}*


> 📊 *Diagram: {"subject": "Combined circuit diagram with both NC and NO limit valves.", "type": "schematic diagram"}*

