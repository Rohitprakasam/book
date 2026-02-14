---
title: "Chapter 97"
author: "BookForge Draft"
---

### Properties of Air

Air, the invisible yet ever-present medium surrounding us, is a critical component in numerous engineering applications, especially in pneumatic systems. Understanding its properties is essential for designing and operating these systems effectively.

Air is not a single substance, but rather a mixture of various gases. Its composition is approximately 21% oxygen, 78% nitrogen, and 1% other gases, such as argon and carbon dioxide. It is crucial to note that these percentages are based on volume. In addition to these gases, air can also contain up to 4% water vapor, the amount varying depending on the humidity. The percentage of water vapor in atmospheric air is dynamic, changing constantly from hour to hour, even within the same location. This variability in humidity adds another layer of complexity when analyzing and designing pneumatic systems, as water vapor affects the density and compressibility of air.

The concept of "standard air" and "free air" helps to address these variations. Free air is air at normal atmospheric conditions. Since atmospheric pressure and temperature fluctuate daily, so too do the characteristics of free air. Therefore, the term "standard air" is used in pneumatic circuit calculations to provide a fixed reference point. Standard air is defined as sea-level air having a temperature of 68°F (20°C), a pressure of 14.7 psia (101 kPa abs), and a relative humidity of 36%.


> 📊 *Diagram: {"subject": "A pie chart illustrating the volumetric composition of dry air, showing the percentages of Nitrogen, Oxygen, Argon, and Carbon Dioxide.", "type": "pie chart"}*


### Composition of Air in Detail

Let's consider the individual components of air more closely:

- **Nitrogen (N2):**The most abundant gas in the atmosphere, nitrogen, is relatively inert. It serves primarily as a diluent for oxygen, moderating its reactivity. In pneumatic systems, nitrogen's inertness makes it a stable and predictable component of the working fluid (air). Industrially, nitrogen is extracted from air through cryogenic distillation or pressure swing adsorption.
-**Oxygen (O2):**Essential for combustion and respiration, oxygen is the active component in many chemical reactions. Its presence in air supports the operation of pneumatic tools and machinery that rely on combustion processes. The controlled oxidation of fuels provides the energy for these devices.
-**Argon (Ar):**An inert noble gas, argon is a byproduct of air separation processes. It doesn't participate in chemical reactions under normal conditions. Its presence in air is generally inconsequential for most pneumatic applications.
-**Carbon Dioxide (CO2):**A greenhouse gas, carbon dioxide, is a product of combustion and respiration. Its concentration in air, although relatively low, is a subject of increasing environmental concern. In pneumatic systems, CO2 behaves similarly to other gases present and contributes to the overall pressure and density.
-**Water Vapor (H2O):** The amount of water vapor in the air significantly affects its properties. High humidity increases air density and can lead to condensation within pneumatic systems, causing corrosion and malfunction. Dehumidifiers are often used to remove excess moisture from compressed air in industrial applications.

Understanding the composition of air and the role of each component is fundamental to predicting the behavior of pneumatic systems and designing them for optimal performance and reliability.

### Dalton's Law of Partial Pressures

In a mixture of gases, each gas exerts its own pressure as if it were the only gas present in the volume. This pressure is called the partial pressure. Dalton's Law of Partial Pressures states that the total pressure exerted by a mixture of gases is equal to the sum of the partial pressures of each individual gas.

Mathematically, this can be expressed as:

$$p_{total} = \sum_{i=1}^{n} p_i$$

where:

- $p_{total}$ is the total pressure of the gas mixture
- $p_i$ is the partial pressure of the *i*-th gas
- *n* is the number of gases in the mixture

The partial pressure of a gas is related to its mole fraction in the mixture. The mole fraction, $x_i$, of a gas is the ratio of the number of moles of that gas to the total number of moles of all gases in the mixture:

$$x_i = \frac{n_i}{n_{total}}$$

The partial pressure of a gas can then be calculated as:

$$p_i = x_i \cdot p_{total}$$


> 📊 *Diagram: {"subject": "A schematic representation of a closed container with a mixture of gases, illustrating the concept of partial pressure exerted by each gas.", "type": "schematic diagram"}*


**Derivation from First Principles:**Consider a container of volume $V$ containing a mixture of $n$ ideal gases at temperature $T$. Each gas, if present alone, would obey the ideal gas law:

$$p_i V = n_i R T$$

where $p_i$ is the partial pressure of the $i$-th gas, $n_i$ is the number of moles of the $i$-th gas, $R$ is the ideal gas constant, and $T$ is the absolute temperature.

Summing the equations for all gases, we get:

$$\sum_{i=1}^{n} p_i V = \sum_{i=1}^{n} n_i R T$$

$$V \sum_{i=1}^{n} p_i = R T \sum_{i=1}^{n} n_i$$

The total number of moles is $n_{total} = \sum_{i=1}^{n} n_i$.  The total pressure $p_{total}$ of the mixture must also obey the ideal gas law:

$$p_{total} V = n_{total} R T$$

Substituting $n_{total}$ into the previous equation, we get:

$$V \sum_{i=1}^{n} p_i = R T n_{total}$$

Dividing this equation by $V$, we have:

$$\sum_{i=1}^{n} p_i = \frac{R T n_{total}}{V} = p_{total}$$

This result confirms Dalton's Law of Partial Pressures: the total pressure of a gas mixture is the sum of the partial pressures of its components.**Mirror Problems:Problem 1: Partial Pressure Calculation**Dry air has the following approximate mole fractions: Nitrogen (78%), Oxygen (21%), Argon (0.9%), and Carbon Dioxide (0.04%). If the total pressure is 98 kPa, calculate the partial pressure of each gas.**Solution:**Given:

- $x_{N_2} = 0.78$
- $x_{O_2} = 0.21$
- $x_{Ar} = 0.009$
- $x_{CO_2} = 0.0004$
- $p_{total} = 98 \, kPa$

Using the formula $p_i = x_i \cdot p_{total}$:

- $p_{N_2} = 0.78 \cdot 98 \, kPa = 76.44 \, kPa$
- $p_{O_2} = 0.21 \cdot 98 \, kPa = 20.58 \, kPa$
- $p_{Ar} = 0.009 \cdot 98 \, kPa = 0.882 \, kPa$
- $p_{CO_2} = 0.0004 \cdot 98 \, kPa = 0.0392 \, kPa$**Problem 2: Humidity Effect**The relative humidity is 60% and the saturation vapor pressure at 28 °C is 3.78 kPa. Calculate the partial pressure of water vapor in the air. Then, calculate the density of the humid air, given the total pressure is 102 kPa. Assume the density of dry air at this temperature and pressure is 1.18 kg/m³.**Solution:**Given:

- $\phi = 0.60$
- $p_{sat} = 3.78 \, kPa$
- $p_{total} = 102 \, kPa$
- $\rho_{dry} = 1.18 \, kg/m^3$

First, calculate the partial pressure of water vapor:

$p_{H_2O} = \phi \cdot p_{sat} = 0.60 \cdot 3.78 \, kPa = 2.268 \, kPa$

The partial pressure of dry air is:

$p_{dry} = p_{total} - p_{H_2O} = 102 \, kPa - 2.268 \, kPa = 99.732 \, kPa$

To find the density of humid air, we can use the following approximation:

$\rho_{humid} = \rho_{dry} \cdot \frac{p_{dry}}{p_{total}} + \rho_{H_2O} \cdot \frac{p_{H_2O}}{p_{total}}$

We need to estimate the density of water vapor.  Using the ideal gas law $pV = nRT$, we can write $\rho = \frac{m}{V} = \frac{pM}{RT}$, where $M$ is the molar mass of water (18.015 g/mol).  So,

$\rho_{H_2O} = \frac{2268 \, Pa \cdot 0.018015 \, kg/mol}{8.314 \, J/(mol \cdot K) \cdot (28+273.15) \, K} = 0.0165 \, kg/m^3$

Then,

$\rho_{humid} = 1.18 \, kg/m^3 \cdot \frac{99.732}{102} + 0.0165 \, kg/m^3 \cdot \frac{2.268}{102}  = 1.156 \, kg/m^3 + 0.00037 \, kg/m^3 = 1.156 \, kg/m^3$

Therefore, the density of the humid air is approximately 1.156 kg/m³.

### Atmospheric Pressure and Altitude

The Earth is enveloped by a blanket of air known as the atmosphere. Because air has weight, the atmosphere exerts pressure at any point due to the cumulative weight of the air column above that point. This pressure is known as atmospheric pressure or barometric pressure. At sea level, the atmosphere exerts a pressure of approximately 14.7 psi (101 kPa). This is considered standard atmospheric pressure.

The atmospheric pressure decreases with altitude. As we ascend, the weight of the air column above decreases, resulting in lower pressure. For altitudes up to approximately 20,000 ft (6.1 km), the relationship between atmospheric pressure and altitude is nearly linear, with a pressure drop of about 0.5 psi per 1000 ft (11 kPa per km). However, it's important to remember that this is an approximation. The actual relationship is more complex due to variations in temperature and air density at different altitudes.

The measurement of atmospheric pressure is typically performed using a barometer. One of the earliest and most common types of barometer is the mercury barometer, invented by Evangelista Torricelli in the 17th century. It consists of a glass tube closed at one end, filled with mercury, and inverted into a mercury-filled reservoir. The height of the mercury column in the tube is proportional to the atmospheric pressure.


> 📊 *Diagram: {"subject": "A schematic diagram of a mercury barometer, illustrating the pressure balance between the atmospheric pressure and the weight of the mercury column.", "type": "schematic diagram"}*

**Theoretical Explanation of Atmospheric Pressure and Altitude Relationship**Atmospheric pressure is a result of the weight of the air column above a given point. This weight exerts a force on the area below, resulting in pressure. As you move to higher altitudes, the amount of air above you decreases, thus reducing the weight and the corresponding pressure.

The approximately linear relationship between pressure and altitude near the Earth's surface is a consequence of the relatively constant density of air in the lower atmosphere (troposphere). However, as altitude increases significantly, the density of air decreases, and the linear approximation becomes less accurate. The temperature of the air also changes with altitude, further complicating the relationship.


> 📊 *Diagram: {"subject": "A layered depiction of the atmosphere, showing the Troposphere, Stratosphere, Mesosphere, Thermosphere with approximate altitude ranges.", "type": "illustration"}*

**Hydrostatic Pressure Equation Derivation:**Consider a small element of air with thickness $dh$ at a height $h$ above sea level. The pressure at the bottom of the element is $p + dp$, and the pressure at the top is $p$. The density of the air is $\rho$, and the acceleration due to gravity is $g$.

The weight of the air element is $dW = \rho g dV = \rho g A dh$, where A is the area.

The force balance on the air element is:

$(p + dp)A + dW = pA$

Substituting $dW$:

$(p + dp)A + \rho g A dh = pA$

$dp A = -\rho g A dh$

$dp = -\rho g dh$

This is the hydrostatic equation. If we assume $\rho$ and $g$ are constant, we can integrate this equation from sea level ($h=0$, $p=p_0$) to altitude $h$:

$\int_{p_0}^{p(h)} dp = -\int_{0}^{h} \rho g dh$

$p(h) - p_0 = -\rho g h$

$p(h) = p_0 - \rho g h$

This equation provides a linear approximation of how pressure changes with altitude.**Hypsometric Equation:**

The hypsometric equation provides a more accurate relationship between pressure and altitude, taking into account the variation of temperature with altitude. It is derived from the hydrostatic equation and the ideal gas law, assuming a constant temperature lapse rate. The equation is:

$$p(h) = p_0 \cdot \exp\left(-\frac{g M h}{R T}\right)$$

where:

- $p(h)$ is the pressure at altitude *h*
- $p_0$ is the pressure at sea level
- $g$ is the acceleration due to gravity (approximately 9.81 m/s²)
- $M$ is the molar mass of air (approximately 0.0289644 kg/mol)
- $R$ is the ideal gas constant (8.314 J/(mol·K))
- $T$ is the average temperature in Kelvin.


> 📊 *Diagram: {"subject": "A graph showing the variation of atmospheric pressure with altitude, comparing the linear approximation and the barometric formula.", "type": "graph"}*


**Mirror Problems:Problem 1: Pressure Calculation at Altitude**Given the sea-level pressure is 101 kPa, the average air density is 1.2 kg/m³, and the altitude is 1500 m, calculate the atmospheric pressure using the simplified linear relationship.**Solution:**Given:

- $p_0 = 101,000 \, Pa$
- $\rho = 1.2 \, kg/m^3$
- $h = 1500 \, m$
- $g = 9.81 \, m/s^2$

Using the formula $p(h) = p_0 - \rho g h$:

$p(h) = 101,000 \, Pa - (1.2 \, kg/m^3)(9.81 \, m/s^2)(1500 \, m)$
$p(h) = 101,000 \, Pa - 17,658 \, Pa$
$p(h) = 83,342 \, Pa = 83.342 \, kPa$**Problem 2: Altitude Estimation from Pressure**Given the sea-level pressure is 102 kPa and the pressure at a certain location is 88 kPa, estimate the altitude using both the linear approximation and the barometric formula (assuming a constant temperature of 22 °C). Compare the results.**Solution:**Given:

- $p_0 = 102,000 \, Pa$
- $p(h) = 88,000 \, Pa$
- $T = 22 + 273.15 = 295.15 \, K$
- $\rho = 1.2 \, kg/m^3$

Using the linear approximation $p(h) = p_0 - \rho g h$:

$88,000 \, Pa = 102,000 \, Pa - (1.2 \, kg/m^3)(9.81 \, m/s^2)h$

$(1.2)(9.81)h = 102,000 - 88,000$
$11.772h = 14,000$
$h = \frac{14,000}{11.772} = 1189.3 \, m$

Using the barometric formula $p(h) = p_0 \cdot \exp\left(-\frac{g M h}{R T}\right)$:

$88,000 = 102,000 \cdot \exp\left(-\frac{9.81 \cdot 0.0289644 \cdot h}{8.314 \cdot 295.15}\right)$

$\frac{88,000}{102,000} = \exp\left(-\frac{0.28414 h}{2454.6}\right)$

$0.8627 = \exp(-0.0001157h)$

Taking the natural logarithm of both sides:

$\ln(0.8627) = -0.0001157h$
$-0.1477 = -0.0001157h$
$h = \frac{0.1477}{0.0001157} = 1276.6 \, m$

The linear approximation gives an altitude of approximately 1189.3 m, while the barometric formula gives an altitude of approximately 1276.6 m. The barometric formula, which accounts for temperature, provides a more accurate estimation.**Problem 3: Barometer Reading**Calculate the height of a mercury column in a barometer given the atmospheric pressure is 100 kPa and the density of mercury is 13,534 kg/m³.**Solution:**Given:

- $p_{atm} = 100,000 \, Pa$
- $\rho_{Hg} = 13,534 \, kg/m^3$
- $g = 9.81 \, m/s^2$

The pressure at the base of the mercury column is given by $p = \rho g h$. We set this equal to atmospheric pressure:

$p_{atm} = \rho_{Hg} g h$

$100,000 \, Pa = (13,534 \, kg/m^3)(9.81 \, m/s^2)h$

$h = \frac{100,000}{13,534 \cdot 9.81} = \frac{100,000}{132,768.54} = 0.753 \, m = 753 \, mm$

The height of the mercury column is approximately 753 mm.

### Standard Air and Absolute vs. Gage Pressure/Temperature

When performing pneumatic circuit calculations, it is essential to use standardized conditions and consistent units to ensure accurate and reliable results. Two critical concepts in this regard are standard air conditions and the distinction between absolute and gage pressure, as well as absolute and relative temperature.**Standard Air:**As previously mentioned, standard air is defined as air at sea level with a temperature of 68°F (20°C), a pressure of 14.7 psia (101 kPa abs), and a relative humidity of 36%. These values were chosen as representative average conditions at sea level. While actual atmospheric conditions may vary, using standard air provides a consistent reference point for design and analysis.**Absolute vs. Gage Pressure:**-**Gage Pressure:**Gage pressure is the pressure relative to atmospheric pressure. It is the pressure reading that most pressure gauges display. A gage pressure of zero indicates that the pressure is equal to atmospheric pressure.
-**Absolute Pressure:**Absolute pressure is the pressure relative to a perfect vacuum. It is the sum of gage pressure and atmospheric pressure.

The relationship between absolute and gage pressure is given by:

$$p_{abs} = p_{gage} + p_{atm}$$

where:

- $p_{abs}$ is the absolute pressure
- $p_{gage}$ is the gage pressure
- $p_{atm}$ is the atmospheric pressure

In pneumatic circuit calculations, it is crucial to use absolute pressure because the gas laws (Boyle's Law, Charles' Law, etc.) are based on absolute pressure. Using gage pressure in these calculations will lead to incorrect results. For example, consider a closed container with a gage pressure of 0 psig. While the pressure gauge reads zero, the air inside the container still has a pressure equal to atmospheric pressure (approximately 14.7 psia). This pressure is essential for determining the behavior of the air according to the gas laws.**Absolute vs. Relative Temperature:**-**Relative Temperature:**Relative temperature is temperature measured relative to an arbitrary zero point, such as the freezing point of water (0°C or 32°F).
-**Absolute Temperature:**Absolute temperature is temperature measured relative to absolute zero, the temperature at which all molecular motion ceases.

The units of absolute temperature in the English system are degrees Rankine (°R), and in the metric system, they are Kelvins (K). The conversion formulas are:

$$T(K) = T(°C) + 273.15$$
$$T(°R) = T(°F) + 459.67$$

Absolute zero is 0 K (-273.15°C) or 0 °R (-459.67°F). Similar to pressure, gas laws require the use of absolute temperature. Using relative temperature will lead to incorrect calculations.


> 📊 *Diagram: {"subject": "A pressure scale showing the relationship between absolute pressure, gage pressure, and vacuum pressure, with 0 psig clearly marked.", "type": "illustration"}*


> 📊 *Diagram: {"subject": "Two thermometers, one showing Celsius and Kelvin scales, and the other showing Fahrenheit and Rankine scales, aligned to illustrate the conversion relationship.", "type": "illustration"}*

**Mirror Problems:Problem 1: Pressure Conversion**Convert the following gage pressure values to absolute pressure, given atmospheric pressure is 101.3 kPa:

- $p_{gage} = -20 \, kPa$
- $p_{gage} = 150 \, kPa$
- $p_{gage} = 400 \, kPa$**Solution:**Using the formula $p_{abs} = p_{gage} + p_{atm}$:

- $p_{abs} = -20 \, kPa + 101.3 \, kPa = 81.3 \, kPa$
- $p_{abs} = 150 \, kPa + 101.3 \, kPa = 251.3 \, kPa$
- $p_{abs} = 400 \, kPa + 101.3 \, kPa = 501.3 \, kPa$**Problem 2: Temperature Conversion**Convert the following temperatures to Kelvin and Rankine:

- $T = 25 \, °C$
- $T = 80 \, °F$**Solution:**Using the conversion formulas:

- $T(K) = 25 \, °C + 273.15 = 298.15 \, K$
- $T(°R) = 80 \, °F + 459.67 = 539.67 \, °R$**Problem 3: Combined Conversion**A pneumatic cylinder operates at a gage pressure of 300 psig and a temperature of 180°F. Convert these values to absolute pressure in Pascals and absolute temperature in Kelvin. Assume atmospheric pressure is 14.7 psi.**Solution:**First, convert the gage pressure to absolute pressure in psi:

$p_{abs} = 300 \, psig + 14.7 \, psi = 314.7 \, psia$

Convert psia to Pascals:

$p_{abs} = 314.7 \, psi \cdot 6894.76 \, Pa/psi = 2,169,627 \, Pa = 2169.63 \, kPa$

Convert Fahrenheit to Rankine:

$T(°R) = 180 \, °F + 459.67 = 639.67 \, °R$

Convert Rankine to Kelvin:

$T(K) = \frac{5}{9} T(°R) = \frac{5}{9} \cdot 639.67 = 355.37 \, K$

Therefore, the absolute pressure is approximately 2169.63 kPa, and the absolute temperature is approximately 355.37 K.

### Perfect Gas Laws

The behavior of gases, particularly air, under varying conditions of pressure, volume, and temperature, is governed by a set of principles known as the perfect gas laws. These laws, developed by scientists over several centuries, provide a framework for understanding and predicting the behavior of gases in various engineering applications, especially in pneumatic systems.

The term "perfect gas" refers to an idealized gas that perfectly obeys these laws. While real gases do not behave perfectly, air closely approximates this ideal behavior under the pressure and temperature ranges typically encountered in pneumatic systems. Therefore, the perfect gas laws provide a valuable tool for analyzing and designing these systems.

The primary perfect gas laws are:

-**Boyle's Law:**Relates pressure and volume at constant temperature.
-**Charles' Law:**Relates volume and temperature at constant pressure.
-**Gay-Lussac's Law:**Relates pressure and temperature at constant volume.
-**General Gas Law (Ideal Gas Law):**Combines Boyle's and Charles' laws to relate pressure, volume, and temperature.**Boyle's Law:**Boyle's Law states that for a fixed mass of gas at constant temperature, the absolute pressure and volume are inversely proportional. Mathematically, this is expressed as:

$$P_1V_1 = P_2V_2$$

Where:

- $P_1$ is the initial absolute pressure.
- $V_1$ is the initial volume.
- $P_2$ is the final absolute pressure.
- $V_2$ is the final volume.**Charles' Law:**Charles' Law states that for a fixed mass of gas at constant pressure, the volume is directly proportional to the absolute temperature. Mathematically, this is expressed as:

$$V_1/T_1 = V_2/T_2$$

Where:

- $V_1$ is the initial volume.
- $T_1$ is the initial absolute temperature.
- $V_2$ is the final volume.
- $T_2$ is the final absolute temperature.**Gay-Lussac's Law:**Gay-Lussac's Law states that for a fixed mass of gas at constant volume, the absolute pressure is directly proportional to the absolute temperature. Mathematically, this is expressed as:

$$P_1/T_1 = P_2/T_2$$

Where:

- $P_1$ is the initial absolute pressure.
- $T_1$ is the initial absolute temperature.
- $P_2$ is the final absolute pressure.
- $T_2$ is the final absolute temperature.**General Gas Law (Ideal Gas Law):**The General Gas Law, also known as the Ideal Gas Law, combines Boyle's and Charles' laws into a single equation that relates pressure, volume, temperature, and the number of moles of gas:

$$pV = nRT$$

Where:

- $p$ is the absolute pressure
- $V$ is the volume
- $n$ is the number of moles of gas
- $R$ is the ideal gas constant (8.314 J/(mol·K))
- $T$ is the absolute temperature**Boyle's Law Derivation (Qualitative):**Imagine a container filled with gas molecules bouncing randomly off the walls. The pressure exerted by the gas is due to the force of these collisions. If we decrease the volume of the container while keeping the temperature constant, we are squeezing the same number of gas molecules into a smaller space. This means the molecules will collide with the walls more frequently, increasing the force per unit area, and thus increasing the pressure. This inverse relationship between pressure and volume at constant temperature is the essence of Boyle's Law.


> 📊 *Diagram: {"subject": "A cylinder-piston system illustrating Boyle's Law, showing the decrease in volume with increasing pressure at constant temperature.", "type": "illustration"}*

**Charles' Law Derivation (Qualitative):**Temperature is a measure of the average kinetic energy of the gas molecules. If we increase the temperature of the gas while keeping the pressure constant, the molecules will move faster and collide with the container walls with greater force. To maintain constant pressure, the volume of the container must increase to allow the molecules more space to move around, thereby reducing the collision frequency and force per unit area. This direct relationship between temperature and volume at constant pressure is Charles' Law.


> 📊 *Diagram: {"subject": "A balloon illustrating Charles' Law, showing the increase in volume with increasing temperature at constant pressure.", "type": "illustration"}*

**General Gas Law Derivation:**Start with Boyle's Law:  $pV = k_1$ (at constant T and n)

and Charles' Law: $V/T = k_2$ (at constant p and n)

Rearranging Charles' Law: $V = k_2T$

Substitute this expression for $V$ into Boyle's Law:

$p(k_2T) = k_1$

$pT = k_1/k_2 = k_3$ (a new constant)

Now, consider the number of moles, $n$. It's been experimentally found that at constant temperature and pressure, $V$ is proportional to $n$: $V=k_4n$. So $pV=nkT$ where $k$ is a combined proportionality constant that depends on the units of $p, V, T$, and $n$. This constant is $R$, the ideal gas constant:

$$pV = nRT$$


> 📊 *Diagram: {"subject": "A molecular-level representation of gas particles, illustrating the relationship between temperature, pressure, and volume according to the Ideal Gas Law.", "type": "illustration"}*

**Mirror Problems:Problem 1: Boyle's Law Problem**A gas occupies a volume of 0.6 m³ at a pressure of 220 kPa. If the pressure is increased to 410 kPa while keeping the temperature constant, what is the new volume?**Solution:**Given:

- $V_1 = 0.6 \, m^3$
- $P_1 = 220 \, kPa$
- $P_2 = 410 \, kPa$

Using Boyle's Law $P_1V_1 = P_2V_2$:

$220 \, kPa \cdot 0.6 \, m^3 = 410 \, kPa \cdot V_2$

$V_2 = \frac{220 \cdot 0.6}{410} = 0.322 \, m^3$**Problem 2: Charles' Law Problem**A gas occupies a volume of 1.2 m³ at a temperature of 28°C. If the temperature is increased to 95°C while keeping the pressure constant, what is the new volume?**Solution:**Given:

- $V_1 = 1.2 \, m^3$
- $T_1 = 28 \, °C = 28 + 273.15 = 301.15 \, K$
- $T_2 = 95 \, °C = 95 + 273.15 = 368.15 \, K$

Using Charles' Law $V_1/T_1 = V_2/T_2$:

$\frac{1.2}{301.15} = \frac{V_2}{368.15}$

$V_2 = \frac{1.2 \cdot 368.15}{301.15} = 1.467 \, m^3$**Problem 3: General Gas Law Problem**A container with a volume of 0.12 m³ contains air at a pressure of 320 kPa and a temperature of 27°C. How many moles of air are in the container? Then, calculate the mass of the air. Assume the molar mass of air is 28.96 g/mol.**Solution:**Given:

- $V = 0.12 \, m^3$
- $p = 320,000 \, Pa$
- $T = 27 \, °C = 27 + 273.15 = 300.15 \, K$
- $R = 8.314 \, J/(mol \cdot K)$
- $M = 0.02896 \, kg/mol$

Using the Ideal Gas Law $pV = nRT$:

$320,000 \, Pa \cdot 0.12 \, m^3 = n \cdot 8.314 \, J/(mol \cdot K) \cdot 300.15 \, K$

$n = \frac{320,000 \cdot 0.12}{8.314 \cdot 300.15} = 15.36 \, moles$

To find the mass of the air:

$m = n \cdot M = 15.36 \, mol \cdot 0.02896 \, kg/mol = 0.445 \, kg$**Problem 4: Combined Gas Law**
A gas has a volume of 2.5 m^3 at 105 kPa and 290 K. Find the volume V2 if the pressure and temperature are changed to 120 kPa and 310 K, respectively.

Using the combined gas law:
(P1V1)/T1 = (P2V2)/T2
V2 = (P1V1T2)/(P2T1)
V2 = (105kPa * 2.5 m^3 * 310 K)/(120 kPa * 290 K) = (81375)/(34800) m^3
V2 = 2.34 m^3