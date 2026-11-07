import json

# Dictionary mapping question ID to comprehensive physics solution
SOLUTIONS = {}

def add_solution(qid, qtext, topic, marks, answer):
    SOLUTIONS[qid] = {
        "id": qid,
        "subjective_id": f"PHY101-SUBJ-{qid:03d}",
        "question": qtext,
        "marks": marks,
        "topic": topic,
        "source": "VU PHY101 Examination Canon & Past Papers",
        "answer": answer,
        "solution": answer,
        "model_answer": answer
    }

# ==================== QUESTIONS 1 to 20 ====================

add_solution(
    1,
    "A generator supplies 100 V to the primary coil of a transformer. The primary has 50 turns and the secondary has 500 turns. Calculate the secondary voltage.",
    "Electromagnetic Induction & AC",
    "3 Marks",
    """**Answer: 1000 V (Step-up Transformer)**

**Formula & Principle:**
In an ideal transformer, the ratio of the secondary voltage ($V_s$) to the primary voltage ($V_p$) is equal to the turns ratio:
$$\\frac{V_s}{V_p} = \\frac{N_s}{N_p}$$

**Given Data:**
- Primary Voltage ($V_p$) = $100\\text{ V}$
- Primary Turns ($N_p$) = $50$
- Secondary Turns ($N_s$) = $500$

**Step-by-Step Calculation:**
$$V_s = V_p \\left(\\frac{N_s}{N_p}\\right) = 100\\text{ V} \\times \\left(\\frac{500}{50}\\right) = 100\\text{ V} \\times 10 = 1000\\text{ V}$$

**Physical Conclusion:**
Because the number of secondary turns exceeds the primary turns ($N_s > N_p$), this is a **step-up transformer**, increasing the voltage by a factor of 10 from $100\\text{ V}$ to $1000\\text{ V}$."""
)

add_solution(
    2,
    "Polarization experiments provide evidence that light is what type of wave? Explain the physical reasoning.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Transverse Wave**

**Physical Explanation & Derivation:**
1. **Transverse vs. Longitudinal Waves:**
   - In a **transverse wave**, oscillations of the field or particles occur perpendicular to the direction of wave propagation (e.g., electric and magnetic fields in light: $\\vec{E} \\perp \\vec{k}$ and $\\vec{B} \\perp \\vec{k}$).
   - In a **longitudinal wave**, oscillations occur strictly parallel to the direction of wave propagation (e.g., sound waves in air).
2. **Mechanism of Polarization:**
   Polarization is the restriction of the electric field vector oscillations to a single plane perpendicular to the propagation axis.
   Longitudinal waves possess cylindrical symmetry around the direction of propagation and exhibit no directionality in the plane transverse to motion; therefore, **longitudinal waves cannot be polarized**.
3. **Conclusion:**
   The experimental demonstration that light can be linearly, circularly, or elliptically polarized by polarizers, reflection (Brewster's angle), or birefringent crystals definitively proves that light is a **transverse electromagnetic wave**."""
)

add_solution(
    3,
    "The units of Planck's constant $h$ are identical to which mechanical quantity? Provide dimensional analysis.",
    "Quantum & Modern Physics",
    "3 Marks",
    """**Answer: Angular Momentum (and Action)**

**Dimensional Analysis:**
1. From the Planck-Einstein relation for photon energy:
   $$E = h f \\implies h = \\frac{E}{f}$$
2. The SI unit of energy is the Joule ($\\text{J} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}$), and frequency is Hertz ($\\text{s}^{-1}$).
   Therefore, the SI derived unit of $h$ is:
   $$[h] = \\frac{\\text{J}}{\\text{s}^{-1}} = \\text{J}\\cdot\\text{s} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-1}$$
3. Now, consider the definition of orbital angular momentum $\\vec{L} = \\vec{r} \\times \\vec{p}$:
   $$[L] = [r][p] = [\\text{m}] \\times [\\text{kg}\\cdot\\text{m}\\cdot\\text{s}^{-1}] = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-1} = \\text{J}\\cdot\\text{s}$$
4. Dimensionally:
   $$[h] = [M L^2 T^{-1}] \\quad \\text{and} \\quad [L] = [M L^2 T^{-1}]$$

**Physical Significance:**
In quantum mechanics, orbital and spin angular momentum are quantized in fundamental integer or half-integer multiples of $\\hbar = \\frac{h}{2\\pi}$, directly demonstrating their identical physical dimensions."""
)

add_solution(
    4,
    "We desire to make an LC circuit that oscillates at 100 Hz using an inductance of 2.5 H. Calculate the required capacitance.",
    "Electromagnetic Induction & AC",
    "3 Marks",
    """**Answer: $1.01\\ \\mu\\text{F}$ (or approx. $1.0\\times 10^{-6}\\text{ F}$)**

**Formula:**
The resonant oscillation frequency of an ideal LC tank circuit is given by Thomson's resonance formula:
$$f = \\frac{1}{2\\pi \\sqrt{LC}}$$

**Step-by-Step Derivation:**
1. Square both sides:
   $$f^2 = \\frac{1}{4\\pi^2 L C}$$
2. Solve algebraically for capacitance $C$:
   $$C = \\frac{1}{4\\pi^2 f^2 L}$$
3. Substitute the given values ($f = 100\\text{ Hz}$, $L = 2.5\\text{ H}$):
   $$C = \\frac{1}{4 \\times \\pi^2 \\times (100\\text{ s}^{-1})^2 \\times 2.5\\text{ H}}$$
   $$C = \\frac{1}{4 \\times 9.8696 \\times 10^4 \\times 2.5} = \\frac{1}{9.8696 \\times 10^5}\\text{ F} \\approx 1.013 \\times 10^{-6}\\text{ F} \\approx 1.01\\ \\mu\\text{F}$$

**Conclusion:**
A capacitance of approximately $1.01\\ \\mu\\text{F}$ is required to achieve an oscillation frequency of $100\\text{ Hz}$ with a $2.5\\text{ H}$ inductor."""
)

add_solution(
    5,
    "If the energy of a photon is E, what is its equivalent relativistic mass? State the principle used.",
    "Quantum & Modern Physics",
    "3 Marks",
    """**Answer: $m = \\frac{E}{c^2}$**

**Physical Derivation:**
1. According to Albert Einstein's mass-energy equivalence principle from Special Relativity:
   $$E = m c^2$$
   where $E$ is the total relativistic energy, $m$ is the effective inertial mass, and $c$ is the speed of light in vacuum ($3.00 \\times 10^8\\text{ m/s}$).
2. Solving for mass $m$:
   $$m = \\frac{E}{c^2}$$
3. In terms of photon momentum:
   Since a photon has zero rest mass ($m_0 = 0$) but carries momentum $p = \\frac{E}{c}$, its relativistic mass reflects its gravitational and inertial coupling:
   $$p = m c = \\left(\\frac{E}{c^2}\\right) c = \\frac{E}{c}$$

**Conclusion:**
The equivalent mass of a photon of energy $E$ is $m = \\frac{E}{c^2}$."""
)

add_solution(
    6,
    "The wavelength of light beam A is twice the wavelength of light beam B ($\\lambda_A = 2\\lambda_B$). How does the energy of a photon in beam A compare to that in beam B?",
    "Quantum & Modern Physics",
    "3 Marks",
    """**Answer: Half the energy of a photon in beam B ($E_A = \\frac{1}{2} E_B$)**

**Derivation:**
1. According to the Planck-Einstein relation, photon energy is inversely proportional to wavelength:
   $$E = h f = \\frac{h c}{\\lambda}$$
   where $h$ is Planck's constant and $c$ is the speed of light in vacuum.
2. Form the ratio of the photon energies of beam A and beam B:
   $$\\frac{E_A}{E_B} = \\frac{h c / \\lambda_A}{h c / \\lambda_B} = \\frac{\\lambda_B}{\\lambda_A}$$
3. Given that $\\lambda_A = 2\\lambda_B$:
   $$\\frac{E_A}{E_B} = \\frac{\\lambda_B}{2\\lambda_B} = \\frac{1}{2} \\implies E_A = \\frac{1}{2} E_B$$

**Conclusion:**
Because wavelength is doubled, the frequency and photon energy are cut in half."""
)

add_solution(
    7,
    "The reactance of an inductor at 50 Hz is 10 Ω. What will its reactance become at 100 Hz?",
    "Electromagnetic Induction & AC",
    "3 Marks",
    """**Answer: 20 Ω**

**Formula:**
The inductive reactance $X_L$ of an inductor with self-inductance $L$ at AC frequency $f$ is given by:
$$X_L = \\omega L = 2\\pi f L$$

**Derivation:**
1. Inductive reactance is directly proportional to frequency ($X_L \\propto f$):
   $$\\frac{X_{L2}}{X_{L1}} = \\frac{f_2}{f_1}$$
2. Given $f_1 = 50\\text{ Hz}$, $X_{L1} = 10\\ \\Omega$, and $f_2 = 100\\text{ Hz}$:
   $$X_{L2} = X_{L1} \\left(\\frac{f_2}{f_1}\\right) = 10\\ \\Omega \\times \\left(\\frac{100\\text{ Hz}}{50\\text{ Hz}}\\right) = 10\\ \\Omega \\times 2 = 20\\ \\Omega$$

**Conclusion:**
Doubling the frequency doubles the inductive reactance to $20\\ \\Omega$."""
)

add_solution(
    8,
    "The wavelength of red light is 700 nm. Calculate its frequency in vacuum.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: $4.29 \\times 10^{14}\\text{ Hz}$**

**Formula:**
The relationship between wave speed ($c$), frequency ($f$), and wavelength ($\\lambda$) is:
$$c = f \\lambda \\implies f = \\frac{c}{\\lambda}$$

**Given Data:**
- Speed of light in vacuum ($c$) = $3.00 \\times 10^8\\text{ m/s}$
- Wavelength ($\\lambda$) = $700\\text{ nm} = 700 \\times 10^{-9}\\text{ m} = 7.00 \\times 10^{-7}\\text{ m}$

**Calculation:**
$$f = \\frac{3.00 \\times 10^8\\text{ m/s}}{7.00 \\times 10^{-7}\\text{ m}} = 0.42857 \\times 10^{15}\\text{ Hz} = 4.29 \\times 10^{14}\\text{ Hz}$$

**Conclusion:**
The frequency of the red light wave is $4.29 \\times 10^{14}\\text{ Hz}$."""
)

add_solution(
    9,
    "What physical law is represented by the formula $2d\\sin\\theta = m\\lambda$? Explain each variable.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Bragg's Law of X-Ray Diffraction**

**Explanation & Variable Definitions:**
$$2d\\sin\\theta = m\\lambda$$
- **$d$**: Interplanar spacing between adjacent parallel atomic planes in a crystal lattice.
- **$\\theta$**: Bragg angle (glancing angle between the incident beam and the crystal planes).
- **$m$**: Order of diffraction (positive integer: $m = 1, 2, 3, \\dots$).
- **$\\lambda$**: Wavelength of the incident X-ray or wave.

**Physical Principle:**
When parallel waves scatter off successive parallel planes of atoms separated by distance $d$, the extra path length traveled by the wave reflecting from the deeper plane is $\\Delta r = 2d\\sin\\theta$. Constructive interference occurs when this path difference equals an integral number of wavelengths ($m\\lambda$)."""
)

add_solution(
    10,
    "What is the function of a step-down transformer regarding voltage and current?",
    "Electromagnetic Induction & AC",
    "3 Marks",
    """**Answer: Decreases Voltage and Increases Current (Power Conserved)**

**Physical Explanation:**
1. **Turns Ratio:**
   A step-down transformer has fewer turns on the secondary winding than on the primary winding ($N_s < N_p$).
   $$\\frac{V_s}{V_p} = \\frac{N_s}{N_p} < 1 \\implies V_s < V_p$$
   Hence, it reduces (steps down) the output AC voltage.
2. **Current Transformation:**
   Assuming an ideal transformer with zero core and copper losses, power is conserved ($P_{\\text{in}} = P_{\\text{out}}$):
   $$V_p I_p = V_s I_s \\implies \\frac{I_s}{I_p} = \\frac{V_p}{V_s} = \\frac{N_p}{N_s} > 1 \\implies I_s > I_p$$
   Thus, the secondary current is increased proportionally."""
)

add_solution(
    11,
    "The focal length of a spherical mirror is $N$ times its radius of curvature ($f = N R$). Find the value of $N$.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: $N = \\frac{1}{2}$ (or 0.5)**

**Derivation for Spherical Mirror:**
1. Consider a ray of light parallel to the principal axis incident on a concave spherical mirror at a small distance from the vertex (paraxial ray approximation).
2. The normal to the spherical surface passes through the center of curvature $C$ at distance $R$.
3. By the Law of Reflection, the angle of reflection equals the angle of incidence ($\\theta$).
4. In the paraxial limit ($\\theta \\ll 1\\text{ rad}$, $\\tan\\theta \\approx \\sin\\theta \\approx \\theta$):
   $$f = \\frac{R}{2}$$
5. Comparing with $f = N R$, we obtain $N = \\frac{1}{2}$."""
)

add_solution(
    12,
    "Explain the optical phenomenon responsible for the appearance of vibrant colors in soap bubbles and thin oil films.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Thin-Film Interference of Light**

**Physical Explanation:**
1. When white light strikes a thin transparent film (e.g., soap film or oil slick on water), reflection occurs at two boundaries:
   - Boundary 1: The top surface (air-film boundary).
   - Boundary 2: The bottom surface (film-medium boundary).
2. The light wave reflected from the bottom surface travels an additional optical path equal to $2nt\\cos\\theta_r$ (where $n$ is refractive index and $t$ is film thickness).
3. A phase shift of $\\pi$ ($180^\\circ$ or $\\lambda/2$) occurs upon reflection from a boundary with a higher refractive index.
4. For different visible wavelengths, this optical path difference satisfies either:
   - Constructive interference condition $\\implies$ specific colors are strongly reinforced.
   - Destructive interference condition $\\implies$ complementary colors are cancelled.
5. As film thickness varies across the bubble, different wavelengths constructively interfere at different positions, producing iridescent colored bands."""
)

add_solution(
    13,
    "Define the phenomenon of diffraction and explain how it differs from refraction.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Diffraction of Light**

**Definition:**
Diffraction is the bending and spreading of waves around obstacles, sharp corners, or through small apertures whose dimensions are comparable to the wavelength of the wave.

**Physical Distinction from Refraction:**
- **Diffraction:** Occurs within the *same medium* without changing wave speed or refractive index. It arises from the wave nature of light according to Huygens' Principle, where unobstructed wavefront points act as secondary wavelets that interfere downstream.
- **Refraction:** The change in propagation direction of a wave as it passes across the boundary between *two different media* with different propagation speeds ($v = c/n$), governed by Snell's Law ($n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2$)."""
)

add_solution(
    14,
    "In constructing a physical thermometer, what fundamental characteristic is necessary for the thermometric substance?",
    "Thermodynamics & Heat",
    "3 Marks",
    """**Answer: A Measurable, Continuous, and Reproducible Thermometric Property**

**Explanation:**
To construct a valid thermometer, the substance used must possess at least one physical property (a **thermometric property**) that varies continuously, monotonically, and reproducibly with changes in temperature:
1. **Linear or Monotonic Variation:** The property must have a one-to-one correspondence with thermal energy across the operational range to avoid ambiguity.
2. **Examples of Thermometric Properties:**
   - Thermal expansion of volume or length (mercury/alcohol-in-glass thermometer).
   - Pressure of a constant-volume gas ($P \\propto T$).
   - Electrical resistance of a metal or semiconductor ($R(T)$ in platinum resistance thermometers or thermistors).
   - Thermoelectric electromotive force (EMF in thermocouples).
3. It is not necessary for the substance to never freeze or boil, as long as it operates strictly within its calibrated fluid/stable phase."""
)

add_solution(
    15,
    "In Young's double-slit experiment, derive the expression for the position of the $m$-th bright fringe on the screen.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: $y_m = \\frac{m \\lambda D}{d}$**

**Derivation:**
1. Let two narrow parallel slits $S_1$ and $S_2$ be separated by distance $d$, and let a viewing screen be placed at distance $D$ ($D \\gg d$).
2. The path difference $\\Delta r$ between rays traveling from $S_1$ and $S_2$ to a point $P$ at distance $y$ from the central axis is:
   $$\\Delta r = d \\sin\\theta$$
3. For small angles ($\\theta \\ll 1$), $\\sin\\theta \\approx \\tan\\theta = \\frac{y}{D}$:
   $$\\Delta r \\approx d \\left(\\frac{y}{D}\\right)$$
4. For constructive interference (bright fringes / maxima), the path difference must equal an integer multiple of the wavelength:
   $$\\Delta r = m \\lambda \\quad (m = 0, \\pm 1, \\pm 2, \\dots)$$
5. Equating the two expressions:
   $$d \\left(\\frac{y_m}{D}\\right) = m \\lambda \\implies y_m = \\frac{m \\lambda D}{d}$$"""
)

add_solution(
    16,
    "Why do constant-volume gas thermometers using different gases all indicate nearly identical temperatures in the low-pressure limit?",
    "Thermodynamics & Heat",
    "3 Marks",
    """**Answer: All Real Gases Approach Ideal Gas Behavior as Pressure Approaches Zero ($P \\to 0$)**

**Physical Explanation:**
1. Real gases exhibit intermolecular forces (van der Waals attraction) and have non-zero molecular volume, causing deviations from ideal behavior at elevated pressures and densities.
2. In the low-density and low-pressure limit ($P \\to 0$, extremely low particle concentration), the average separation between molecules becomes vast compared to molecular dimensions.
3. Under these conditions, intermolecular interactions become negligible, and all real gases rigorously obey the ideal gas equation of state:
   $$P V = n R T$$
4. In a constant-volume thermometer ($V = \\text{constant}$):
   $$T = 273.16\\text{ K} \\times \\lim_{P_3 \\to 0} \\left(\\frac{P}{P_3}\\right)$$
   where $P_3$ is the pressure measured at the triple point of water ($273.16\\text{ K}$). This ratio becomes independent of the identity of the gas."""
)

add_solution(
    17,
    "What is a metastable state in atomic physics? Contrast its lifetime with that of ordinary excited atomic states.",
    "Quantum & Modern Physics",
    "3 Marks",
    """**Answer: A Long-Lived Excited State with Lifetime $\\sim 10^{-3}\\text{ s}$ (Milliseconds)**

**Physical Explanation:**
1. **Ordinary Excited States:**
   Electrons excited to ordinary atomic energy levels undergo rapid spontaneous dipole transitions back to lower levels, with typical lifetimes on the order of:
   $$\\tau_{\\text{normal}} \\approx 10^{-8}\\text{ s}$$
2. **Metastable States:**
   A metastable state is an excited atomic state from which radiative dipole transitions to the ground state are quantum-mechanically "forbidden" by electric dipole selection rules (e.g., $\\Delta l = \\pm 1$).
   Because transitions can only proceed through much slower mechanisms (such as magnetic dipole, electric quadrupole, or collisional de-excitation), the electron remains trapped in this state for significantly longer durations:
   $$\\tau_{\\text{metastable}} \\approx 10^{-3}\\text{ s to several seconds}$$
3. **Application in Lasers:**
   This prolonged residence time allows incoming electrons to accumulate in the metastable level faster than they decay, establishing **population inversion**, the fundamental prerequisite for stimulated emission in lasers."""
)

add_solution(
    18,
    "List the primary ways by which electromagnetic radiation (light) interacts with matter, and explain why interference is not an interaction with matter.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Absorption, Emission, and Scattering/Transmission**

**Constitutive Light-Matter Interactions:**
1. **Absorption:** Photons transfer their energy to atomic electrons, exciting them to higher energy levels or creating electron-hole pairs/photoelectrons.
2. **Spontaneous and Stimulated Emission:** Excited atomic electrons transition to lower energy states, emitting photons.
3. **Transmission, Reflection & Scattering:** Electromagnetic waves interact with the bound charges of material atoms (polarization), re-radiating wavelets that determine refractive index and Rayleigh/Compton scattering.

**Why Interference is Not a Light-Matter Interaction:**
Interference and superposition describe the mathematical and physical combination of **two or more electromagnetic waves with each other** in space, in accordance with the linearity of Maxwell's equations. It is an intrinsic wave-wave phenomenon, not an exchange of energy or momentum between light and material particles."""
)

add_solution(
    19,
    "In an AC series RL circuit, derive the expression for the phase angle $\\phi$ between total applied voltage and current.",
    "Electromagnetic Induction & AC",
    "3 Marks",
    """**Answer: $\\phi = \\tan^{-1}\\left(\\frac{\\omega L}{R}\\right)$**

**Derivation via Phasor Diagram:**
1. In a series RL circuit driven by an AC source $v(t) = V_0 \\sin(\\omega t)$, the current $i(t) = I_0 \\sin(\\omega t - \\phi)$ is common throughout the circuit.
2. The voltage across the resistor is in phase with current:
   $$V_R = I R$$
3. The voltage across the inductor leads current by $90^\\circ$ ($\\pi/2\\text{ rad}$):
   $$V_L = I X_L = I (\\omega L)$$
4. From the right-angled voltage phasor triangle:
   $$\\tan\\phi = \\frac{V_L}{V_R} = \\frac{I \\omega L}{I R} = \\frac{\\omega L}{R}$$
5. Solving for phase angle $\\phi$:
   $$\\phi = \\tan^{-1}\\left(\\frac{\\omega L}{R}\\right)$$
   The voltage leads the current by angle $\\phi$."""
)

add_solution(
    20,
    "What is the theoretical upper limit for the frequency of an electromagnetic wave in classical and modern physics?",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: No Classical Upper Limit (Planck Frequency $\\sim 10^{43}\\text{ Hz}$ in Quantum Gravity)**

**Physical Explanation:**
1. **Classical Electrodynamics (Maxwell's Theory):**
   According to Maxwell's equations, electromagnetic waves exist for all wavelengths $\\lambda > 0$ with frequency $f = c/\\lambda$. Spacetime is treated as a continuous manifold, so there is **no theoretical upper frequency limit**.
2. **Quantum Electrodynamics:**
   Photon energy is given by $E = h f$. In standard quantum field theory, photons of arbitrarily high energy can exist in cosmic ray interactions without a hard ceiling.
3. **Quantum Gravity / Planck Scale Limit:**
   At the fundamental Planck scale, when photon wavelength approaches the Planck length ($\\ell_P = \\sqrt{\\frac{\\hbar G}{c^3}} \\approx 1.62 \\times 10^{-35}\\text{ m}$), quantum gravitational fluctuations dominate. The corresponding Planck frequency is:
   $$f_P = \\frac{c}{\\ell_P} = \\sqrt{\\frac{c^5}{\\hbar G}} \\approx 1.85 \\times 10^{43}\\text{ Hz}$$
   Beyond this, classical notions of space and time cease to be defined."""
)

print(f"Added solutions 1-20. Total so far: {len(SOLUTIONS)}")

# ==================== QUESTIONS 21 to 40 ====================

add_solution(
    21,
    "Why do plant leaves appear green? What portions of the visible solar spectrum does chlorophyll primarily absorb?",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Absorbs Red and Blue Light; Reflects Green Light**

**Photochemical Explanation:**
1. White sunlight comprises the entire continuous visible spectrum from $\\sim 400\\text{ nm}$ (violet) to $\\sim 700\\text{ nm}$ (red).
2. Photosynthetic pigments in chloroplasts (primarily chlorophyll a and chlorophyll b) exhibit strong electronic absorption resonances in two distinct wavelength bands:
   - **Blue-Violet Region:** $\\sim 400\\text{--}470\\text{ nm}$
   - **Red Region:** $\\sim 630\\text{--}680\\text{ nm}$
3. In the intermediate **green portion of the spectrum** ($\\sim 500\\text{--}560\\text{ nm}$), chlorophyll has virtually zero absorption.
4. Consequently, green light is reflected from and transmitted through the leaf tissue into our eyes, causing leaves to appear green."""
)

add_solution(
    22,
    "Define the commercial unit of electrical energy (kilowatt-hour) and convert 1 kWh into Joules.",
    "Work, Energy & Power",
    "3 Marks",
    """**Answer: $1\\text{ kWh} = 3.6 \\times 10^6\\text{ Joules}$ (or 3.6 MJ)**

**Derivation:**
1. Electrical energy is the product of power ($P$) and operating time ($t$):
   $$E = P \\times t$$
2. The standard commercial unit is the **kilowatt-hour (kWh)**:
   - $1\\text{ kilowatt (kW)} = 1000\\text{ Watts} = 1000\\text{ Joules/second}$
   - $1\\text{ hour (h)} = 60\\text{ minutes} \\times 60\\text{ seconds} = 3600\\text{ seconds}$
3. Converting to SI base units:
   $$1\\text{ kWh} = (1000\\text{ J/s}) \\times (3600\\text{ s}) = 3,600,000\\text{ Joules} = 3.6 \\times 10^6\\text{ J} = 3.6\\text{ MJ}$$

**Conclusion:**
One kilowatt-hour represents the total electrical energy consumed by a 1000-watt appliance operating continuously for one full hour."""
)

add_solution(
    23,
    "According to Einstein's Special Theory of Relativity, what is the maximum speed limit for material particles and physical signals?",
    "Special Relativity",
    "3 Marks",
    """**Answer: The Speed of Light in Vacuum ($c \\approx 3.00 \\times 10^8\\text{ m/s}$)**

**Relativistic Derivation:**
1. In Special Relativity, the relativistic momentum and total relativistic energy of a body of rest mass $m_0$ moving at speed $v$ are given by:
   $$p = \\gamma m_0 v, \\quad E = \\gamma m_0 c^2$$
   where the Lorentz factor is:
   $$\\gamma = \\frac{1}{\\sqrt{1 - v^2/c^2}}$$
2. As the speed of the body approaches $c$ ($v \\to c$):
   $$\\lim_{v \\to c} \\gamma = \\infty \\implies \\lim_{v \\to c} E = \\infty$$
3. Accelerating an object with finite rest mass ($m_0 > 0$) to the speed of light would require an infinite amount of work and energy, which is physically impossible.
4. Only massless particles ($m_0 = 0$, such as photons) travel at exactly $c$ in vacuum. No material object or causal signal can exceed $c$."""
)

add_solution(
    24,
    "In a movie scene, an actor looks into a mirror and the audience sees his face in the mirror. What does the actor see in the mirror during filming?",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: The Movie Camera (and Camera Crew)**

**Optical Principle & Ray Tracing:**
1. **Law of Reflection:** The angle of reflection equals the angle of incidence ($\\theta_r = \\theta_i$), and the incident ray, reflected ray, and normal lie in the same plane.
2. **Principle of Optical Path Reversibility:** Light rays follow identical paths regardless of propagation direction.
3. If light rays originating from the actor's face reflect off the plane mirror and travel into the aperture of the movie camera lens (allowing the camera to record his face), then light rays originating from the camera lens must trace the exact reverse trajectory, reflecting off that identical spot on the mirror into the actor's pupils.
4. Therefore, the actor directly sees the **movie camera** in the mirror, not his own reflection."""
)

add_solution(
    25,
    "State the Stefan-Boltzmann Law, define its constant $\\sigma$, and determine its SI base units.",
    "Thermodynamics & Heat",
    "3 Marks",
    """**Answer: $\\sigma = 5.670 \\times 10^{-8}\\text{ W}\\cdot\\text{m}^{-2}\\cdot\\text{K}^{-4}$**

**Formula & Derivation:**
1. The Stefan-Boltzmann Law states that the total radiant emissive power $E$ (energy emitted per unit area per second) of an ideal blackbody is proportional to the fourth power of its absolute thermodynamic temperature $T$:
   $$E = \\sigma T^4 \\implies \\sigma = \\frac{E}{T^4}$$
2. The SI derived units of emissive power are watts per square meter ($\\text{W/m}^2$):
   $$[\\sigma] = \\frac{\\text{W}/\\text{m}^2}{\\text{K}^4} = \\text{W}\\cdot\\text{m}^{-2}\\cdot\\text{K}^{-4}$$
3. Expressed in SI fundamental base units:
   $$\\text{W} = \\text{J/s} = \\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}$$
   $$[\\sigma] = \\frac{\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-3}}{\\text{m}^2 \\cdot \\text{K}^4} = \\text{kg}\\cdot\\text{s}^{-3}\\cdot\\text{K}^{-4}$$"""
)

add_solution(
    26,
    "State the two essential physical conditions required for two light sources to be mutually coherent.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Identical Frequency (Wavelength) and Constant Phase Difference**

**Physical Requirements:**
Two wave sources are defined as **coherent** if and only if they satisfy:
1. **Identical Frequency (Monochromaticity):**
   The waves must have the exact same temporal frequency and wavelength ($\\omega_1 = \\omega_2$, $\\lambda_1 = \\lambda_2$).
2. **Constant (Time-Independent) Phase Relationship:**
   The initial phase difference between the two wave trains must remain strictly constant over time:
   $$\\Delta \\phi(t) = \\phi_1(t) - \\phi_2(t) = \\text{constant}$$

**Why Coherence is Crucial:**
If the phase difference fluctuated randomly with time (as occurs with two independent light bulbs due to random spontaneous atomic emissions), the resulting interference pattern would shift position millions of times per second, averaging out into a uniform background intensity without visible fringes."""
)

add_solution(
    27,
    "Identify the antiparticle of the electron. State its mass, charge, spin, and describe what happens during electron-positron collision.",
    "Nuclear & Particle Physics",
    "3 Marks",
    """**Answer: Positron ($e^+$ or $\\beta^+$)**

**Physical Properties:**
- **Mass:** Identical to the electron: $m_{e^+} = 9.109 \\times 10^{-31}\\text{ kg}$ ($0.511\\text{ MeV}/c^2$).
- **Charge:** Equal in magnitude but opposite in sign: $+e = +1.602 \\times 10^{-19}\\text{ C}$.
- **Spin:** Fermion with spin $s = \\frac{1}{2}$.

**Annihilation Reaction:**
When an electron and a positron collide at low kinetic energies, they undergo mutual matter-antimatter annihilation, converting 100% of their invariant rest mass and kinetic energy into high-energy electromagnetic radiation:
$$e^- + e^+ \\to 2\\gamma$$
To conserve both linear momentum and energy in the center-of-mass frame, two back-to-back gamma-ray photons are emitted, each carrying energy:
$$E_\\gamma = m_e c^2 = 511\\text{ keV}$$"""
)

add_solution(
    28,
    "What is the ultimate objective of the scientific method and empirical inquiry in physics?",
    "General Physics",
    "3 Marks",
    """**Answer: Formulating Predictive, Testable Mathematical Models of Natural Phenomena**

**Detailed Explanation:**
The fundamental objective of the scientific method in physics is to discover the universal principles governing the behavior of matter, energy, space, and time through:
1. **Observation & Measurement:** Quantitative, controlled gathering of empirical data.
2. **Hypothesis & Mathematical Formulation:** Proposing explanatory laws (e.g., Newton's laws, Maxwell's equations) that encapsulate physical behavior.
3. **Falsifiable Prediction:** Making precise, testable predictions about novel physical events.
4. **Experimental Verification:** Subjecting theories to rigorous testing; a theory stands only as long as its predictions match experimental reality."""
)

add_solution(
    29,
    "State the condition under which the total linear momentum of a colliding system is conserved.",
    "Momentum & Collisions",
    "3 Marks",
    """**Answer: Zero Net External Impulse (or Zero Net External Force: $\\Sigma \\vec{F}_{\\text{ext}} = 0$)**

**Derivation from Newton's Laws:**
1. Consider a system of $N$ interacting particles. By Newton's Second Law:
   $$\\frac{d\\vec{P}_{\\text{total}}}{dt} = \\sum \\vec{F}_{\\text{ext}} + \\sum \\vec{F}_{\\text{int}}$$
2. By Newton's Third Law (Action-Reaction), all internal mutual forces between pairs of particles are equal in magnitude and opposite in direction:
   $$\\vec{f}_{ij} = -\\vec{f}_{ji} \\implies \\sum \\vec{F}_{\\text{int}} = 0$$
3. Integrating over collision time $\\Delta t$:
   $$\\Delta \\vec{P}_{\\text{total}} = \\int \\vec{F}_{\\text{ext, net}} dt = \\vec{J}_{\\text{ext}}$$
4. If the net external force is zero (or the collision occurs so rapidly that $\\Delta t \\to 0$, making external impulse negligible compared to internal impact forces):
   $$\\vec{J}_{\\text{ext}} = 0 \\implies \\Delta \\vec{P}_{\\text{total}} = 0 \\implies \\vec{P}_{\\text{initial}} = \\vec{P}_{\\text{final}}$$"""
)

add_solution(
    30,
    "Show that work and energy share identical physical dimensions, and determine their SI base units.",
    "Work, Energy & Power",
    "3 Marks",
    """**Answer: $[M L^2 T^{-2}]$ (Joule, $\\text{kg}\\cdot\\text{m}^2\\cdot\\text{s}^{-2}$)**

**Dimensional Proof:**
1. **Work ($W$):**
   Defined as the line integral of force through displacement:
   $$W = \\int \\vec{F} \\cdot d\\vec{r}$$
   $$[W] = [\\text{Force}][\\text{Distance}] = [M L T^{-2}][L] = [M L^2 T^{-2}]$$
2. **Kinetic Energy ($K$):**
   $$K = \\frac{1}{2} m v^2$$
   $$[K] = [M][L T^{-1}]^2 = [M L^2 T^{-2}]$$
3. **Gravitational Potential Energy ($U$):**
   $$U = m g h$$
   $$[U] = [M][L T^{-2}][L] = [M L^2 T^{-2}]$$
4. **Torque ($\\tau$):**
   $$\\vec{\\tau} = \\vec{r} \\times \\vec{F} \\implies [\\tau] = [L][M L T^{-2}] = [M L^2 T^{-2}]$$

**Conclusion:**
Work, kinetic energy, potential energy, and torque all share the fundamental dimension $[M L^2 T^{-2}]$. In SI, work and energy are measured in Joules ($\\text{J} = \\text{N}\\cdot\\text{m}$)."""
)

add_solution(
    31,
    "Determine the sign of the work done by gravity during the descent of a projectile. Explain using vector dot product.",
    "Work, Energy & Power",
    "3 Marks",
    """**Answer: Positive Work ($W > 0$)**

**Derivation:**
1. The work done by a constant force is defined by the scalar (dot) product:
   $$W = \\vec{F}_g \\cdot \\Delta\\vec{r}$$
2. For a projectile of mass $m$, the gravitational force points vertically downward:
   $$\\vec{F}_g = -m g \\hat{j}$$
3. During descent, the vertical displacement is also directed downward:
   $$\\Delta\\vec{r} = \\Delta x \\hat{i} - \\Delta y \\hat{j} \\quad (\\Delta y > 0)$$
4. Evaluating the dot product:
   $$W_g = (-m g \\hat{j}) \\cdot (\\Delta x \\hat{i} - \\Delta y \\hat{j}) = (-m g)(-\\Delta y) = +m g \\Delta y > 0$$
5. Because the downward component of displacement is parallel to the downward force of gravity ($\\cos 0^\\circ = +1$), the work done is strictly **positive**, converting gravitational potential energy into kinetic energy."""
)

add_solution(
    32,
    "An object moves in a circular path at constant speed. Why is the work done by the centripetal force strictly zero?",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: Centripetal Force is Perpendicular to Velocity ($\\\\vec{F}_c \\perp \\vec{v}$)**

**Mathematical Proof:**
1. The instantaneous rate of doing work (mechanical power) is given by:
   $$P = \\frac{dW}{dt} = \\vec{F} \\cdot \\vec{v}$$
2. In uniform circular motion:
   - The centripetal force $\\vec{F}_c = -\\frac{m v^2}{r} \\hat{r}$ acts radially inward toward the center of the circle.
   - The instantaneous velocity $\\vec{v}$ is tangent to the circular trajectory.
3. Because the radial and tangential directions are mutually orthogonal ($\\theta = 90^\\circ$):
   $$\\vec{F}_c \\cdot \\vec{v} = |F_c||v| \\cos(90^\\circ) = 0$$
4. Total work done over any displacement $s$:
   $$W = \\int \\vec{F}_c \\cdot d\\vec{r} = \\int (\\vec{F}_c \\cdot \\vec{v}) dt = 0$$
5. By the Work-Kinetic Energy Theorem ($\\Delta K = W_{\\text{net}} = 0$), the speed and kinetic energy of the object remain strictly constant."""
)

add_solution(
    33,
    "Determine the dimensional formula and SI unit of the ratio of work to power ($W/P$).",
    "Work, Energy & Power",
    "3 Marks",
    """**Answer: Dimension of Time $[T]$ (Seconds, s)**

**Derivation:**
1. Power $P$ is defined as the time rate of doing work:
   $$P = \\frac{W}{t} \\implies \\frac{W}{P} = t$$
2. Dimensional Analysis:
   - $[\\text{Work}] = [M L^2 T^{-2}]$
   - $[\\text{Power}] = \\frac{[M L^2 T^{-2}]}{[T]} = [M L^2 T^{-3}]$
3. Taking the ratio:
   $$\\left[\\frac{W}{P}\\right] = \\frac{[M L^2 T^{-2}]}{[M L^2 T^{-3}]} = [T]$$
4. In SI units:
   $$\\frac{\\text{Joules}}{\\text{Watts}} = \\frac{\\text{J}}{\\text{J/s}} = \\text{seconds (s)}$$"""
)

add_solution(
    34,
    "A massive particle ($M$) moving at $5\\text{ m/s}$ undergoes a head-on 1D elastic collision with a light particle ($m \\ll M$) at rest. Calculate the post-collision velocity of the light particle.",
    "Momentum & Collisions",
    "3 Marks",
    """**Answer: $\\approx 10\\text{ m/s}$ (Double the incident projectile speed)**

**Derivation:**
1. In a one-dimensional elastic collision where target mass $m$ is initially at rest ($v_{2i} = 0$), the final velocity of the target particle is:
   $$v_{2f} = \\left(\\frac{2M}{M + m}\\right) v_{1i}$$
2. In the limit where the striking particle is much more massive than the target ($M \\gg m$):
   $$\\lim_{m/M \\to 0} \\frac{2M}{M + m} = \\lim_{m/M \\to 0} \\frac{2}{1 + m/M} = 2$$
3. Substituting the incident velocity $v_{1i} = 5\\text{ m/s}$:
   $$v_{2f} \\approx 2 v_{1i} = 2 \\times 5\\text{ m/s} = 10\\text{ m/s}$$

**Physical Interpretation:**
In the reference frame of the massive projectile (which barely slows down, $v_{1f} \\approx 5\\text{ m/s}$), the light particle approaches at $5\\text{ m/s}$ and bounces forward elastically at $5\\text{ m/s}$ relative to the projectile. Adding the projectile's frame velocity yields $5 + 5 = 10\\text{ m/s}$ in the lab frame."""
)

add_solution(
    35,
    "Who first formulated the Law of Inertia, and how was it subsequently incorporated into classical mechanics?",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: Galileo Galilei (Formalized as Newton's First Law of Motion)**

**Historical & Physical Explanation:**
1. **Galileo's Formulation:**
   Through his famous inclined plane experiments, Galileo Galilei demonstrated that an object in motion on a horizontal, frictionless surface will continue moving indefinitely with constant speed in a straight line without requiring any continuing force. He thus overthrew the Aristotelian misconception that force is needed to maintain velocity.
2. **Newton's First Law:**
   Sir Isaac Newton adopted Galileo's concept of inertia and formalized it as his **First Law of Motion**:
   *\"Every body persists in its state of rest or uniform motion in a straight line, unless acted upon by a net external resultant force.\"*
3. Inertia is quantified in Newtonian mechanics by **inertial mass** ($m$)."""
)

add_solution(
    36,
    "Define the product of force and time interval. State the Impulse-Momentum Theorem.",
    "Momentum & Collisions",
    "3 Marks",
    """**Answer: Impulse (equals the change in linear momentum: $\\vec{J} = \\Delta\\vec{p}$)**

**Derivation:**
1. Newton's Second Law in derivative form states:
   $$\\vec{F} = \\frac{d\\vec{p}}{dt}$$
2. Multiplying by $dt$ and integrating over the collision duration from $t_1$ to $t_2$:
   $$\\vec{J} = \\int_{t_1}^{t_2} \\vec{F} dt = \\int_{p_1}^{p_2} d\\vec{p} = \\vec{p}_2 - \\vec{p}_1 = \\Delta\\vec{p}$$
3. For a constant or time-averaged force $\\vec{F}_{\\text{avg}}$:
   $$\\vec{J} = \\vec{F}_{\\text{avg}} \\Delta t = \\Delta\\vec{p}$$
4. SI unit: $\\text{N}\\cdot\\text{s} = \\text{kg}\\cdot\\text{m/s}$."""
)

add_solution(
    37,
    "Why is it significantly easier to walk on a concrete road than on a smooth sheet of ice? Explain the role of friction.",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: Greater Static Friction on Concrete Provides Necessary Reaction Force**

**Physical Explanation:**
1. **Newton's Third Law in Walking:**
   When walking, a person pushes backward against the ground with their feet ($F_{\\text{foot on ground}}$).
   By Newton's Third Law, the ground simultaneously exerts an equal and opposite forward reaction force on the foot:
   $$F_{\\text{ground on foot}} = f_s$$
   This forward force is provided entirely by **static friction** ($f_s \\le \\mu_s N$).
2. **Comparison of Surfaces:**
   - **Concrete:** High coefficient of static friction ($\\mu_s \\approx 0.8\\text{--}1.0$), easily supplying the required forward thrust without slipping.
   - **Ice:** Extremely low coefficient of friction ($\\mu_s \\approx 0.05\\text{--}0.10$), which cannot supply sufficient horizontal force. As a result, the foot slips backward, making forward locomotion difficult."""
)

add_solution(
    38,
    "Define a light-year, state what physical quantity it measures, and calculate its value in meters.",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: Unit of Distance ($1\\text{ ly} \\approx 9.46 \\times 10^{15}\\text{ m}$)**

**Derivation:**
1. A **light-year (ly)** is defined as the total linear distance traveled by a beam of electromagnetic radiation in a vacuum during one Julian year ($365.25\\text{ days}$).
2. Calculation:
   - Speed of light ($c$) = $2.998 \\times 10^8\\text{ m/s}$
   - Time ($t$) = $1\\text{ year} = 365.25 \\times 24 \\times 3600\\text{ s} = 31,557,600\\text{ s}$
   $$d = c \\times t = (2.998 \\times 10^8\\text{ m/s}) \\times (3.15576 \\times 10^7\\text{ s}) \\approx 9.461 \\times 10^{15}\\text{ m}$$

**Conclusion:**
Despite the word \"year\", a light-year is strictly a unit of **astronomical distance**, equivalent to approximately $9.46\\text{ trillion kilometers}$."""
)

add_solution(
    39,
    "A constant force of 100 N acts upon a body for 5.0 seconds. Calculate the resulting change in momentum.",
    "Momentum & Collisions",
    "3 Marks",
    """**Answer: $500\\text{ N}\\cdot\\text{s}$ (or $500\\text{ kg}\\cdot\\text{m/s}$)**

**Formula:**
By the Impulse-Momentum Theorem:
$$\\Delta p = J = F \\times \\Delta t$$

**Given Data:**
- Applied Force ($F$) = $100\\text{ N}$
- Time Interval ($\\Delta t$) = $5.0\\text{ s}$

**Calculation:**
$$\\Delta p = 100\\text{ N} \\times 5.0\\text{ s} = 500\\text{ N}\\cdot\\text{s} = 500\\text{ kg}\\cdot\\text{m/s}$$

**Conclusion:**
The momentum of the body changes by $500\\text{ kg}\\cdot\\text{m/s}$ in the direction of the applied force."""
)

add_solution(
    40,
    "Two vectors have lengths of 4 m and 5 m with unknown mutual orientation. Determine the possible range of the magnitude of their vector sum.",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: Between 1 m and 9 m ($1\\text{ m} \\le R \\le 9\\text{ m}$)**

**Mathematical Derivation:**
1. The magnitude of the resultant vector $\\vec{R} = \\vec{A} + \\vec{B}$ is given by the Law of Cosines:
   $$R = \\sqrt{A^2 + B^2 + 2 A B \\cos\\theta}$$
   where $\\theta$ is the angle between $\\vec{A}$ and $\\vec{B}$ ($-1 \\le \\cos\\theta \\le +1$).
2. **Maximum Resultant (Parallel Vectors, $\\theta = 0^\\circ$, $\\cos 0^\\circ = +1$):**
   $$R_{\\max} = \\sqrt{A^2 + B^2 + 2AB} = A + B = 5\\text{ m} + 4\\text{ m} = 9\\text{ m}$$
3. **Minimum Resultant (Antiparallel Vectors, $\\theta = 180^\\circ$, $\\cos 180^\\circ = -1$):**
   $$R_{\\min} = \\sqrt{A^2 + B^2 - 2AB} = |A - B| = |5\\text{ m} - 4\\text{ m}| = 1\\text{ m}$$

**Conclusion:**
The magnitude of the vector sum must lie within the closed interval $[1\\text{ m}, 9\\text{ m}]$."""
)

print(f"Added solutions 21-40. Total so far: {len(SOLUTIONS)}")

# ==================== QUESTIONS 41 to 60 ====================

add_solution(
    41,
    "Define a physical quantity and distinguish between base quantities and derived quantities with examples.",
    "General Physics",
    "3 Marks",
    """**Answer: Measurable Property of a Physical System**

**Definitions & Classification:**
1. **Physical Quantity:** Any feature or property of a physical phenomenon, body, or substance that can be quantified objectively through measurement and expressed as the product of a numerical value and an appropriate physical unit (e.g., $Q = \\{n\\}[u]$).
2. **Base (Fundamental) Quantities:**
   Quantities that cannot be defined in terms of other physical quantities; they form the foundation of the SI system.
   - Seven SI Base Quantities: Length (meter, m), Mass (kilogram, kg), Time (second, s), Electric Current (ampere, A), Thermodynamic Temperature (kelvin, K), Amount of Substance (mole, mol), Luminous Intensity (candela, cd).
3. **Derived Quantities:**
   Quantities defined mathematically as combinations of base quantities:
   - Examples: Velocity ($[L T^{-1}]$, $\\text{m/s}$), Force ($[M L T^{-2}]$, $\\text{N}$), Energy ($[M L^2 T^{-2}]$, $\\text{J}$)."""
)

add_solution(
    42,
    "Define an inelastic collision and contrast it with an elastic collision in terms of momentum and kinetic energy conservation.",
    "Momentum & Collisions",
    "3 Marks",
    """**Answer: Momentum is Conserved; Kinetic Energy is NOT Conserved**

**Comparison Table & Derivation:**
1. **Inelastic Collision:**
   - **Linear Momentum:** Strictly conserved ($\\Sigma \\vec{p}_i = \\Sigma \\vec{p}_f$) because net external impulse is zero.
   - **Kinetic Energy:** **NOT conserved** ($K_f < K_i$). A portion of the mechanical kinetic energy is irreversibly converted into internal thermal energy, permanent structural deformation, or acoustic radiation.
   - **Completely Inelastic Collision:** The colliding bodies stick together post-impact, sharing a common velocity ($v_f = \\frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$), maximizing kinetic energy loss.
2. **Elastic Collision:**
   - Both total linear momentum and total mechanical kinetic energy are conserved ($K_i = K_f$)."""
)

add_solution(
    43,
    "In what direction is the linear acceleration of a body always produced? Explain using Newton's Second Law.",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: In the Direction of the Net (Resultant) Force ($\\vec{a} \\parallel \\Sigma \\vec{F}$)**

**Explanation:**
1. Newton's Second Law of Motion in vector form is:
   $$\\Sigma \\vec{F} = m \\vec{a} \\implies \\vec{a} = \\frac{\\Sigma \\vec{F}}{m}$$
2. Because inertial mass $m$ is a strictly positive scalar quantity ($m > 0$), multiplying or dividing a vector by $m$ does not alter its spatial direction.
3. Therefore, the acceleration vector $\\vec{a}$ is always directed **collinearly and in the identical direction as the net unbalanced external force $\\Sigma \\vec{F}$**.
4. **Crucial Distinction:** Acceleration is NOT necessarily in the direction of velocity $\\vec{v}$. For instance, in uniform circular motion, $\\vec{a}$ is perpendicular to $\\vec{v}$; when braking, $\\vec{a}$ opposes $\\vec{v}$."""
)

add_solution(
    44,
    "Ali wants to lift a mass of 7.5 kg at constant velocity using a light rope passing over a frictionless ceiling pulley. Calculate the tension in the rope.",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: $73.5\\text{ N}$ (or $75\\text{ N}$ using $g = 10\\text{ m/s}^2$)**

**Derivation:**
1. Let $m = 7.5\\text{ kg}$ be the mass lifted, and $T$ be the tension in the rope.
2. The condition of lifting at **constant velocity** implies zero acceleration:
   $$\\vec{a} = 0$$
3. By Newton's First and Second Laws in the vertical ($y$) direction:
   $$\\Sigma F_y = T - m g = m a_y = 0 \\implies T = m g$$
4. Evaluating with standard acceleration due to gravity ($g = 9.80\\text{ m/s}^2$):
   $$T = 7.5\\text{ kg} \\times 9.80\\text{ m/s}^2 = 73.5\\text{ N}$$
   *(If taking $g = 10\\text{ m/s}^2$, $T = 7.5 \\times 10 = 75\\text{ N}$)*."""
)

add_solution(
    45,
    "Determine the launch angle of a projectile for which its maximum height equals its horizontal range ($H = R$).",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: $\\theta = \\tan^{-1}(4) \\approx 75.96^\\circ \\approx 76^\\circ$**

**Derivation:**
1. The standard formulas for a projectile launched over level ground with initial speed $v_0$ at angle $\\theta$ are:
   - Maximum Height:
     $$H = \\frac{v_0^2 \\sin^2\\theta}{2g}$$
   - Horizontal Range:
     $$R = \\frac{v_0^2 \\sin(2\\theta)}{g} = \\frac{2 v_0^2 \\sin\\theta \\cos\\theta}{g}$$
2. Set $H = R$:
   $$\\frac{v_0^2 \\sin^2\\theta}{2g} = \\frac{2 v_0^2 \\sin\\theta \\cos\\theta}{g}$$
3. Cancel non-zero common terms ($v_0^2 / g$ and $\\sin\\theta \\neq 0$):
   $$\\frac{\\sin\\theta}{2} = 2 \\cos\\theta \\implies \\frac{\\sin\\theta}{\\cos\\theta} = 4 \\implies \\tan\\theta = 4$$
4. Compute angle:
   $$\\theta = \\tan^{-1}(4) \\approx 75.96^\\circ$$"""
)

add_solution(
    46,
    "Explain the modern SI definition of the standard second. What atomic transition is it based on?",
    "General Physics",
    "3 Marks",
    """**Answer: The Hyperfine Transition Frequency of Cesium-133 (Atomic Clock)**

**Official SI Standard:**
1. Since 1967, the SI base unit of time (the second, s) is defined by fixing the numerical value of the cesium frequency:
   $$\\Delta \\nu_{\\text{Cs}} = 9,192,631,770\\text{ Hz}$$
2. **Formal Definition:**
   The second is the duration of exactly $9,192,631,770$ periods of the microwave radiation corresponding to the transition between the two hyperfine levels of the unperturbed ground state of the cesium-133 atom ($^{133}\\text{Cs}$).
3. **Why Astronomical Standards Were Replaced:**
   Earlier definitions based on Earth's daily rotation (mean solar second) or orbital revolution (ephemeris second) were abandoned because tidal friction and gravitational perturbations cause Earth's rotation to gradually slow and wobble."""
)

add_solution(
    47,
    "What dynamic effect is always produced when an unbalanced net torque acts on a rigid body?",
    "Rotational Motion & Torque",
    "3 Marks",
    """**Answer: Angular Acceleration ($\\vec{\\alpha}$)**

**Formula & Physical Law:**
1. The rotational analog of Newton's Second Law for a rigid body of moment of inertia $I$ about a fixed axis is:
   $$\\Sigma \\vec{\\tau} = I \\vec{\\alpha}$$
2. When a net unbalanced torque acts ($\\Sigma \\vec{\\tau} \\neq 0$), because the rotational inertia $I = \\int r^2 dm > 0$ is a non-zero positive quantity, it must produce an **angular acceleration**:
   $$\\vec{\\alpha} = \\frac{\\Sigma \\vec{\\tau}}{I} = \\frac{d\\vec{\\omega}}{dt} \\neq 0$$
3. Consequently, the body's angular velocity $\\vec{\\omega}$ changes with time (rotational speed changes or rotation axis precesses). It disrupts rotational equilibrium."""
)

add_solution(
    48,
    "An object attached to a spring completes 20 full oscillations in 10 seconds. Calculate its frequency, period, and angular frequency.",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: Angular Frequency $\\omega = 4\\pi \\approx 12.57\\text{ rad/s} \\approx 12.6\\text{ rad/s}$**

**Step-by-Step Calculation:**
1. **Frequency ($f$):**
   Number of oscillations per unit time:
   $$f = \\frac{N}{t} = \\frac{20\\text{ vibrations}}{10\\text{ s}} = 2.0\\text{ Hz}$$
2. **Period ($T$):**
   Time for one complete vibration:
   $$T = \\frac{1}{f} = \\frac{1}{2.0\\text{ Hz}} = 0.50\\text{ s}$$
3. **Angular Frequency ($\\omega$):**
   $$\\omega = 2\\pi f = 2\\pi \\times 2.0\\text{ Hz} = 4\\pi\\text{ rad/s} \\approx 12.566\\text{ rad/s} \\approx 12.6\\text{ rad/s}$$"""
)

add_solution(
    49,
    "State Hooke's Law for Simple Harmonic Motion (SHM). To what quantity must the restoring force be directly proportional?",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: Proportional to Displacement from Equilibrium and Directed Oppositely ($F \\propto -x$)**

**Derivation:**
1. Simple Harmonic Motion is defined dynamically by the condition that the restoring force $F$ is linearly proportional to the displacement $x$ of the oscillating mass from its equilibrium position:
   $$F = -k x$$
   where $k$ is the positive force constant (spring constant).
2. The negative sign signifies that the restoring force is always directed back toward the central equilibrium position ($x = 0$).
3. Combining with Newton's Second Law ($F = m \\frac{d^2x}{dt^2}$):
   $$m \\frac{d^2x}{dt^2} + k x = 0 \\implies \\frac{d^2x}{dt^2} + \\omega^2 x = 0 \\quad \\left(\\omega = \\sqrt{\\frac{k}{m}}\\right)$$
   producing sinusoidal oscillations $x(t) = A \\cos(\\omega t + \\phi)$."""
)

add_solution(
    50,
    "Why is mercury uniquely convenient as the working fluid in a Torricellian barometer? Calculate standard atmospheric column height.",
    "Fluid Mechanics & Elasticity",
    "3 Marks",
    """**Answer: High Density ($\\rho = 13,600\\text{ kg/m}^3$) and Extremely Low Vapor Pressure**

**Physical Explanation & Calculation:**
1. By Pascal's and Torricelli's hydrostatic law:
   $$P_{\\text{atm}} = \\rho g h \\implies h = \\frac{P_{\\text{atm}}}{\\rho g}$$
2. For Mercury ($\\rho_{\\text{Hg}} = 13,600\\text{ kg/m}^3$):
   $$h_{\\text{Hg}} = \\frac{1.013 \\times 10^5\\text{ Pa}}{13,600\\text{ kg/m}^3 \\times 9.80\\text{ m/s}^2} \\approx 0.760\\text{ m} = 760\\text{ mm} = 76\\text{ cm}$$
   This allows a compact, portable glass tube ($< 1\\text{ m}$).
3. **Contrast with Water:**
   Water has a much lower density ($\\rho = 1000\\text{ kg/m}^3$). A water barometer would require an impractically tall column height of:
   $$h_{\\text{water}} = \\frac{1.013 \\times 10^5}{1000 \\times 9.8} \\approx 10.33\\text{ m} \\approx 34\\text{ feet}$$
4. Mercury also has negligible room-temperature vapor pressure, leaving a virtually perfect vacuum above the column."""
)

add_solution(
    51,
    "State the SI derived units for electric field strength and prove their dimensional equivalence.",
    "Electric Potential & Capacitance",
    "3 Marks",
    """**Answer: $\\text{N/C}$ and $\\text{V/m}$ (or $\\text{J/(C}\\cdot\\text{m)}$)**

**Proof of Equivalence:**
1. From the definition of electric field as force per unit test charge:
   $$\\vec{E} = \\frac{\\vec{F}}{q} \\implies [E] = \\frac{\\text{Newton}}{\\text{Coulomb}} = \\text{N/C}$$
2. From the relationship between electric field and electric potential gradient:
   $$\\vec{E} = -\\vec{\\nabla} V \\implies [E] = \\frac{\\text{Volt}}{\\text{meter}} = \\text{V/m}$$
3. Prove that $1\\text{ V/m} = 1\\text{ N/C}$:
   - Since $1\\text{ Volt} = 1\\text{ Joule/Coulomb} = 1\\text{ (N}\\cdot\\text{m)/C}$:
   $$\\frac{\\text{V}}{\\text{m}} = \\frac{\\text{J}/\\text{C}}{\\text{m}} = \\frac{\\text{N}\\cdot\\text{m}}{\\text{C}\\cdot\\text{m}} = \\frac{\\text{N}}{\\text{C}} = \\frac{\\text{J}}{\\text{C}\\cdot\\text{m}}$$
4. Dimensionally: $[E] = [M L T^{-3} I^{-1}]$."""
)

add_solution(
    52,
    "Define the Farad (F) in terms of fundamental SI units and base circuit variables.",
    "Electric Potential & Capacitance",
    "3 Marks",
    """**Answer: Coulomb per Volt ($1\\text{ F} = 1\\text{ C/V}$)**

**Derivation:**
1. Capacitance $C$ is defined as the ratio of stored charge $Q$ on a conductor to the resulting potential difference $V$:
   $$C = \\frac{Q}{V}$$
2. SI units:
   $$[C] = \\frac{\\text{Coulomb}}{\\text{Volt}} = \\text{C/V}$$
3. Expressed in terms of mechanical energy units:
   Since $1\\text{ V} = 1\\text{ J/C}$:
   $$1\\text{ F} = \\frac{\\text{C}}{\\text{J/C}} = \\frac{\\text{C}^2}{\\text{J}} = \\frac{\\text{C}^2}{\\text{N}\\cdot\\text{m}}$$
4. Expressed in SI fundamental base units:
   $$1\\text{ F} = \\text{A}^2\\cdot\\text{s}^4\\cdot\\text{kg}^{-1}\\cdot\\text{m}^{-2}$$"""
)

add_solution(
    53,
    "Calculate the capacitance required to create an LC circuit resonant at 100 Hz using a 2.5 H inductor.",
    "Electromagnetic Induction & AC",
    "3 Marks",
    """**Answer: $1.01\\ \\mu\\text{F}$**

**Step-by-Step Derivation:**
1. The resonant frequency of an LC oscillator is:
   $$f = \\frac{1}{2\\pi \\sqrt{LC}}$$
2. Solving for $C$:
   $$C = \\frac{1}{4\\pi^2 f^2 L}$$
3. Substituting $f = 100\\text{ s}^{-1}$ and $L = 2.5\\text{ H}$:
   $$C = \\frac{1}{4 \\times \\pi^2 \\times (100)^2 \\times 2.5} = \\frac{1}{100,000 \\pi^2} \\approx \\frac{1}{986,960.4}\\text{ F} \\approx 1.013 \\times 10^{-6}\\text{ F} = 1.01\\ \\mu\\text{F}$$

**Conclusion:**
A $1.01\\ \\mu\\text{F}$ capacitor paired with the $2.5\\text{ H}$ inductor oscillates naturally at $100\\text{ Hz}$."""
)

add_solution(
    54,
    "State which common statements about electromagnetic waves are TRUE and which are FALSE regarding vacuum propagation.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: EM Waves Travel Freely in Vacuum; No Material Medium Required**

**Analysis of Statements:**
1. *\"Electromagnetic waves satisfy Maxwell's Equations\":* **TRUE**. They are exact wave solutions derived from the Maxwell curl equations.
2. *\"Electromagnetic radiation from a burning candle is unpolarized\":* **TRUE**. Photons are emitted by random, uncorrelated atomic thermal transitions.
3. *\"Electromagnetic waves cannot travel through space/vacuum\":* **FALSE**. Unlike mechanical waves, electromagnetic waves require no mechanical medium and propagate through empty space at speed $c = 1/\\sqrt{\\mu_0 \\varepsilon_0} \\approx 3 \\times 10^8\\text{ m/s}$."""
)

add_solution(
    55,
    "Classify radio waves and visible light waves in terms of their physical wave type and electromagnetic nature.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Transverse Electromagnetic Waves**

**Physical Explanation:**
1. Both radio waves and visible light are members of the **electromagnetic spectrum**, differing only in wavelength and frequency:
   - Radio waves: Long wavelength ($\\lambda \\sim 1\\text{ mm to } 100\\text{ km}$), low frequency.
   - Visible light: Short wavelength ($\\lambda \\sim 400\\text{ to } 700\\text{ nm}$), high frequency.
2. Both consist of mutually perpendicular oscillating electric ($\\vec{E}$) and magnetic ($\\vec{B}$) fields propagating through space.
3. In both cases, the oscillations are strictly perpendicular (orthogonal) to the direction of wave propagation ($\\vec{E} \\perp \\vec{B} \\perp \\vec{k}$).
4. Therefore, both are **transverse electromagnetic waves**."""
)

add_solution(
    56,
    "State Wien's Displacement Law, give its mathematical formula with units, and explain its physical meaning.",
    "Thermodynamics & Heat",
    "3 Marks",
    """**Answer: $\\lambda_{\\max} T = b = 2.898 \\times 10^{-3}\\text{ m}\\cdot\\text{K}$**

**Explanation:**
1. **Mathematical Formula:**
   $$\\lambda_{\\max} T = b$$
   where:
   - $\\lambda_{\\max}$ is the wavelength at which spectral radiance is maximized (in meters, m).
   - $T$ is the absolute thermodynamic temperature of the blackbody (in Kelvin, K).
   - $b$ is Wien's displacement constant: $b \\approx 2.8978 \\times 10^{-3}\\text{ m}\\cdot\\text{K}$.
2. **Physical Meaning:**
   As the temperature of an object rises, the peak of its thermal radiation spectrum shifts (is \"displaced\") toward shorter wavelengths (higher frequencies and photon energies).
3. **Example:**
   A cool object radiates primarily in the invisible infrared; as it heats up, it glows dull red, then yellow, and finally brilliant white/blue."""
)

add_solution(
    57,
    "What fundamental physical property of light is conclusively proven by the phenomenon of optical interference?",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Light is a Wave Phenomenon**

**Physical Explanation:**
1. Classical particles (corpuscles) obey simple additive ballistic rules: firing particles through two slits produces two distinct piles behind the slits.
2. When light passes through two closely spaced slits, it produces an **interference pattern** of alternating light and dark bands (fringes) on a screen.
3. Dark bands correspond to regions where waves from the two slits arrive exactly half a cycle out of phase ($\\Delta r = (m + \\frac{1}{2})\\lambda$), causing destructive cancellation:
   $$E_{\\text{total}} = E_1 + E_2 = E_0 - E_0 = 0$$
4. Such cancellation can occur only through the linear superposition of wave amplitudes, conclusively proving that light exhibits **wave behavior**."""
)

add_solution(
    58,
    "Calculate the unique temperature at which the Fahrenheit and Kelvin temperature scales agree numerically.",
    "Thermodynamics & Heat",
    "3 Marks",
    """**Answer: $+574.59^\\circ$ (or approx. $574.6$)**

**Derivation:**
1. The conversion relation between Fahrenheit ($T_F$) and Celsius ($T_C$) is:
   $$T_F = \\frac{9}{5} T_C + 32$$
2. The relation between Celsius ($T_C$) and Kelvin ($T_K$) is:
   $$T_C = T_K - 273.15$$
3. Substituting $T_C$ into the Fahrenheit equation:
   $$T_F = \\frac{9}{5}(T_K - 273.15) + 32$$
4. Set $T_F = T_K = x$:
   $$x = \\frac{9}{5}(x - 273.15) + 32$$
5. Multiply through by 5:
   $$5x = 9(x - 273.15) + 160$$
   $$5x = 9x - 2458.35 + 160$$
   $$5x - 9x = -2298.35 \\implies -4x = -2298.35$$
   $$x = \\frac{2298.35}{4} = 574.5875 \\approx 574.6$$

**Note:**
While Celsius and Fahrenheit agree at $-40^\\circ$, Fahrenheit and Kelvin agree at **$+574.6$**."""
)

add_solution(
    59,
    "State the two fundamental postulates of Einstein's Special Theory of Relativity and their key kinematic consequences.",
    "Special Relativity",
    "3 Marks",
    """**Answer: Principle of Relativity and Constancy of the Speed of Light**

**The Two Postulates:**
1. **First Postulate (Principle of Relativity):**
   The laws of physics are identical and take the same mathematical form in all inertial reference frames.
2. **Second Postulate (Invariance of $c$):**
   The speed of light in vacuum is an absolute universal constant ($c = 2.998 \\times 10^8\\text{ m/s}$), independent of the motion of the emitting source or the observer.

**Major Physical Consequences:**
- **Time Dilation:** Moving clocks run slower relative to a stationary observer: $\\Delta t = \\gamma \\Delta t_0$.
- **Length Contraction:** Moving rods are shortened along the direction of motion: $L = L_0 / \\gamma$.
- **Relativity of Simultaneity:** Events simultaneous in one frame are not simultaneous in another.
- **Relativistic Mass-Energy Conservation:** Mass and energy are equivalent ($E = mc^2$)."""
)

add_solution(
    60,
    "A spaceship emitting light moves directly away from an observer at high relativistic speed. How do the observed frequency and wavelength change? What is this effect called?",
    "Special Relativity",
    "3 Marks",
    """**Answer: Lower Frequency and Longer Wavelength (Relativistic Redshift)**

**Relativistic Doppler Derivation:**
1. When a light source moves directly away from an observer along the line of sight at speed $v$, the relativistic Doppler formula is:
   $$f_{\\text{obs}} = f_{\\text{src}} \\sqrt{\\frac{1 - \\beta}{1 + \\beta}} \\quad \\left(\\beta = \\frac{v}{c} > 0\\right)$$
2. Because $\\frac{1 - \\beta}{1 + \\beta} < 1$, the observed frequency is strictly **lower** than the source frequency:
   $$f_{\\text{obs}} < f_{\\text{src}}$$
3. Since $c = f \\lambda$, wavelength is inversely proportional to frequency:
   $$\\lambda_{\\text{obs}} = \\frac{c}{f_{\\text{obs}}} = \\lambda_{\\text{src}} \\sqrt{\\frac{1 + \\beta}{1 - \\beta}} > \\lambda_{\\text{src}}$$
4. The observed wavelength is shifted toward the longer, red end of the spectrum (**Relativistic Redshift**)."""
)

print(f"Added solutions 41-60. Total so far: {len(SOLUTIONS)}")

# ==================== QUESTIONS 61 to 80 ====================

add_solution(
    61,
    "How fast should an observer move directly away from a $6.0 \\times 10^{14}\\text{ Hz}$ light source to observe the light at a frequency of $4.0 \\times 10^{14}\\text{ Hz}$?",
    "Special Relativity",
    "3 Marks",
    """**Answer: $v \\approx 0.385 c$ (approx. $0.38 c$ or $1.15 \\times 10^8\\text{ m/s}$)**

**Derivation:**
1. Use the relativistic Doppler formula for a receiver moving away from a stationary source:
   $$f_{\\text{obs}} = f_{\\text{src}} \\sqrt{\\frac{1 - \\beta}{1 + \\beta}} \\quad \\left(\\beta = \\frac{v}{c}\\right)$$
2. Given $f_{\\text{obs}} = 4.0 \\times 10^{14}\\text{ Hz}$ and $f_{\\text{src}} = 6.0 \\times 10^{14}\\text{ Hz}$:
   $$\\frac{f_{\\text{obs}}}{f_{\\text{src}}} = \\frac{4.0 \\times 10^{14}}{6.0 \\times 10^{14}} = \\frac{2}{3}$$
3. Square both sides:
   $$\\left(\\frac{2}{3}\\right)^2 = \\frac{4}{9} = \\frac{1 - \\beta}{1 + \\beta}$$
4. Cross-multiply and solve for $\\beta$:
   $$4(1 + \\beta) = 9(1 - \\beta)$$
   $$4 + 4\\beta = 9 - 9\\beta$$
   $$13\\beta = 5 \\implies \\beta = \\frac{5}{13} \\approx 0.3846$$
5. Therefore, the required speed is:
   $$v = \\frac{5}{13} c \\approx 0.385 c \\approx 1.15 \\times 10^8\\text{ m/s}$$"""
)

add_solution(
    62,
    "In the quantum mechanical model of the hydrogen atom, what physical property of the electron is primarily determined by the principal quantum number $n$?",
    "Quantum & Modern Physics",
    "3 Marks",
    """**Answer: Total Energy (and Orbital Size/Radius)**

**Physical Explanation:**
1. In the Bohr model and the exact solution of the Schrödinger equation for hydrogenic atoms, the **principal quantum number** ($n = 1, 2, 3, \\dots$) determines:
   - **Quantized Total Energy Level:**
     $$E_n = -\\frac{13.6\\text{ eV}}{n^2}$$
     The principal quantum number directly specifies the bound state energy of the electron.
   - **Mean Orbital Radius:**
     $$\\langle r \\rangle_n \\approx a_0 n^2$$
     where $a_0 \\approx 0.529\\text{ Å}$ is the Bohr radius. Higher $n$ corresponds to larger electron probability clouds.
2. In contrast:
   - Orbital quantum number $l$ determines orbital angular momentum magnitude.
   - Magnetic quantum number $m_l$ determines spatial orientation of angular momentum.
   - Spin quantum number $m_s$ determines intrinsic electron spin projection."""
)

add_solution(
    63,
    "As the wavelength of a mechanical wave traveling through a uniform, non-dispersive medium increases, how does its propagation speed change? Explain.",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: Remains Constant (Unchanged)**

**Physical Explanation:**
1. The speed of a mechanical wave ($v$) is determined solely by the mechanical and inertial properties of the transmitting medium:
   - For transverse waves on a string: $v = \\sqrt{\\frac{T}{\\mu}}$ (Tension $T$, linear mass density $\\mu$).
   - For longitudinal sound waves in fluids: $v = \\sqrt{\\frac{B}{\\rho}}$ (Bulk modulus $B$, density $\\rho$).
2. The wave speed equation is:
   $$v = f \\lambda$$
3. In a uniform, non-dispersive medium, wave speed $v$ is an intrinsic property of the medium and remains strictly constant.
4. If wavelength $\\lambda$ increases, the temporal frequency $f$ decreases proportionally ($f = v / \\lambda$), preserving constant wave speed."""
)

add_solution(
    64,
    "An organ pipe open at both ends is 3.0 m long. Assuming the speed of sound is 340 m/s, calculate its fundamental frequency (lowest tone).",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: $56.7\\text{ Hz} \\approx 57\\text{ Hz}$**

**Derivation:**
1. For an organ pipe open at both ends, displacement antinodes form at both open ends.
2. The fundamental standing wave mode ($n = 1$) has a wavelength given by:
   $$\\lambda_1 = 2 L = 2 \\times 3.0\\text{ m} = 6.0\\text{ m}$$
3. The fundamental frequency is:
   $$f_1 = \\frac{v}{\\lambda_1} = \\frac{v}{2L}$$
4. Given $v = 340\\text{ m/s}$ and $L = 3.0\\text{ m}$:
   $$f_1 = \\frac{340\\text{ m/s}}{2 \\times 3.0\\text{ m}} = \\frac{340}{6.0} \\approx 56.67\\text{ Hz} \\approx 57\\text{ Hz}$$

**Conclusion:**
The lowest tone produced by the pipe has a frequency of approximately $57\\text{ Hz}$."""
)

add_solution(
    65,
    "To raise the pitch of a piano string, does the tuner tighten or loosen the string? Explain using the wave speed formula.",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: Tightens the String (Increases Tension $T$)**

**Derivation:**
1. The pitch perceived by the human ear corresponds directly to the fundamental vibration frequency $f$ of the acoustic wave.
2. For a fixed string of length $L$ and linear mass density $\\mu$, the fundamental frequency is:
   $$f = \\frac{v}{2L} = \\frac{1}{2L} \\sqrt{\\frac{T}{\\mu}}$$
   where $T$ is the tension in the wire.
3. Frequency is directly proportional to the square root of tension:
   $$f \\propto \\sqrt{T}$$
4. To raise the pitch (increase $f$), the piano tuner must **tighten the tuning pin**, which increases tension $T$. Loosening reduces tension and lowers the pitch."""
)

add_solution(
    66,
    "State the condition under which the net torque acting on a body in static equilibrium vanishes independent of the choice of reference point.",
    "Rotational Motion & Torque",
    "3 Marks",
    """**Answer: When the Net Force is Zero ($\\Sigma \\vec{F} = 0$), Net Torque is Identical About Any Point**

**Mathematical Proof:**
1. Let $\\Sigma \\vec{\\tau}_O$ be the net torque about an origin $O$:
   $$\\Sigma \\vec{\\tau}_O = \\sum \\vec{r}_i \\times \\vec{F}_i$$
2. Let $O'$ be a different reference point located at position $\\vec{R}$ relative to $O$.
3. The position vector of each force application point relative to $O'$ is $\\vec{r}_i' = \\vec{r}_i - \\vec{R}$.
4. The net torque about $O'$ is:
   $$\\Sigma \\vec{\\tau}_{O'} = \\sum \\vec{r}_i' \\times \\vec{F}_i = \\sum (\\vec{r}_i - \\vec{R}) \\times \\vec{F}_i = \\sum (\\vec{r}_i \\times \\vec{F}_i) - \\vec{R} \\times \\left(\\sum \\vec{F}_i\\right)$$
   $$\\Sigma \\vec{\\tau}_{O'} = \\Sigma \\vec{\\tau}_O - \\vec{R} \\times (\\Sigma \\vec{F})$$
5. If the body satisfies translational equilibrium ($\\Sigma \\vec{F} = 0$):
   $$\\Sigma \\vec{\\tau}_{O'} = \\Sigma \\vec{\\tau}_O - \\vec{R} \\times 0 = \\Sigma \\vec{\\tau}_O$$
6. Therefore, for an object in complete equilibrium, the net torque vanishes about **the same point or any arbitrary chosen point** in space."""
)

add_solution(
    67,
    "A 4.0-N puck moving at 3.0 m/s collides with a stationary 8.0-N puck and they stick together. Calculate their common final speed.",
    "Momentum & Collisions",
    "3 Marks",
    """**Answer: $1.0\\text{ m/s}$**

**Derivation:**
1. The collision is **completely inelastic** (the pucks stick together).
2. Weight $W = m g \\implies m = W/g$:
   - Striking puck mass: $m_1 = W_1/g = 4.0/g$
   - Stationary puck mass: $m_2 = W_2/g = 8.0/g$
3. By conservation of linear momentum:
   $$m_1 v_{1i} + m_2 v_{2i} = (m_1 + m_2) v_f$$
4. Since $v_{2i} = 0$:
   $$v_f = \\frac{m_1}{m_1 + m_2} v_{1i} = \\frac{W_1 / g}{(W_1 + W_2) / g} v_{1i} = \\frac{W_1}{W_1 + W_2} v_{1i}$$
5. Substituting the given values:
   $$v_f = \\frac{4.0\\text{ N}}{4.0\\text{ N} + 8.0\\text{ N}} \\times 3.0\\text{ m/s} = \\frac{4.0}{12.0} \\times 3.0\\text{ m/s} = \\frac{1}{3} \\times 3.0 = 1.0\\text{ m/s}$$"""
)

add_solution(
    68,
    "Describe the magnitude and direction of the acceleration of a particle moving in a circle at constant speed.",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: Constant Magnitude ($a_c = v^2/r$); Continuously Changing Direction (Radially Inward)**

**Physical Explanation:**
1. In uniform circular motion, speed $v = |\\vec{v}|$ is constant, so tangential acceleration is zero:
   $$a_t = \\frac{dv}{dt} = 0$$
2. However, the velocity vector $\\vec{v}$ continuously changes its spatial orientation as the object turns.
3. The resulting acceleration is the **centripetal acceleration**:
   $$\\vec{a}_c = -\\frac{v^2}{r} \\hat{r} = -\\omega^2 r \\hat{r}$$
4. **Magnitude:** Constant, equal to $a_c = \\frac{v^2}{r} = \\omega^2 r$.
5. **Direction:** Continuously changes, pointing radially inward toward the instantaneous center of the circular trajectory at all times."""
)

add_solution(
    69,
    "A plane traveling north at 200 m/s makes a turn and travels south at 200 m/s. Calculate the change in its velocity vector.",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: $400\\text{ m/s south}$ ($-400\\hat{j}\\text{ m/s}$)**

**Vector Derivation:**
1. Define a Cartesian coordinate system where the positive $y$-axis points North ($+\\hat{j}$) and the negative $y$-axis points South ($-\\hat{j}$).
2. Initial velocity vector:
   $$\\vec{v}_i = +200\\hat{j}\\text{ m/s}$$
3. Final velocity vector:
   $$\\vec{v}_f = -200\\hat{j}\\text{ m/s}$$
4. The change in velocity vector is defined as $\\Delta\\vec{v} = \\vec{v}_f - \\vec{v}_i$:
   $$\\Delta\\vec{v} = (-200\\hat{j}) - (+200\\hat{j}) = -400\\hat{j}\\text{ m/s}$$
5. The magnitude of the change is $400\\text{ m/s}$, directed **due South**."""
)

add_solution(
    70,
    "A car has initial velocity $16\\text{ m/s}$ at $t = 0$. It decelerates with acceleration $a(t) = -0.50 t\\text{ m/s}^2$. At what time does it come to a complete stop?",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: $t = 8.0\\text{ seconds}$**

**Calculus Derivation:**
1. Acceleration is the time rate of change of velocity:
   $$a(t) = \\frac{dv}{dt} = -0.50 t$$
2. Separate variables and integrate from $t = 0$ ($v = 16\\text{ m/s}$) to stopping time $t$ ($v = 0$):
   $$\\int_{16}^0 dv = \\int_0^t -0.50 t dt$$
3. Evaluate the integrals:
   $$\\left[ v \\right]_{16}^0 = -0.50 \\left[ \\frac{t^2}{2} \\right]_0^t$$
   $$0 - 16 = -0.25 t^2$$
   $$-16 = -0.25 t^2 \\implies t^2 = \\frac{16}{0.25} = 64$$
4. Solve for time $t$:
   $$t = \\sqrt{64} = 8.0\\text{ s}$$"""
)

add_solution(
    71,
    "Convert a highway speed limit of 55 mph into meters per second (m/s), given $1\\text{ mi} = 1609\\text{ m}$.",
    "General Physics",
    "3 Marks",
    """**Answer: $24.6\\text{ m/s} \\approx 25\\text{ m/s}$**

**Unit Conversion Calculation:**
1. Given conversions:
   - $1\\text{ mile} = 1609\\text{ meters}$
   - $1\\text{ hour} = 3600\\text{ seconds}$
2. Set up the conversion factor ratio:
   $$v = 55\\frac{\\text{miles}}{\\text{hour}} \\times \\left(\\frac{1609\\text{ m}}{1\\text{ mile}}\\right) \\times \\left(\\frac{1\\text{ hour}}{3600\\text{ s}}\\right)$$
3. Compute numerical value:
   $$v = \\frac{55 \\times 1609}{3600}\\text{ m/s} = \\frac{88,495}{3600}\\text{ m/s} \\approx 24.582\\text{ m/s} \\approx 25\\text{ m/s}$$"""
)

add_solution(
    72,
    "State the rules for significant figures and determine the number of significant figures in the measurement 0.00150.",
    "General Physics",
    "3 Marks",
    """**Answer: 3 Significant Figures**

**Rules for Significant Figures:**
1. **Leading Zeros:** Zeros preceding the first non-zero digit are merely place-holders that indicate decimal position; they are **never significant**.
   - In `0.00150`, the leading three zeros (`0.00`) are not significant.
2. **Non-Zero Digits:** All non-zero digits are always significant.
   - Digits `1` and `5` are significant (2 figures).
3. **Trailing Zeros in Decimal Numbers:** Trailing zeros to the right of the decimal point represent measured precision and are **always significant**.
   - The trailing `0` after `5` is significant (1 figure).
4. Total significant figures = $2 + 1 =$ **3** (the digits `1`, `5`, and `0`)."""
)

add_solution(
    73,
    "State the two essential conditions required for an extended rigid body to remain in complete static equilibrium.",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: Zero Net Force ($\\Sigma \\vec{F} = 0$) and Zero Net Torque ($\\Sigma \\vec{\\tau} = 0$)**

**The Two Equilibrium Conditions:**
1. **First Condition (Translational Equilibrium):**
   The vector sum of all external forces acting on the body must equal zero:
   $$\\Sigma \\vec{F}_{\\text{ext}} = 0 \\iff \\Sigma F_x = 0, \\; \\Sigma F_y = 0, \\; \\Sigma F_z = 0$$
   This guarantees that the linear acceleration of the center of mass is zero ($\\vec{a}_{\\text{cm}} = 0$).
2. **Second Condition (Rotational Equilibrium):**
   The vector sum of all external torques acting on the body about any arbitrary axis must equal zero:
   $$\\Sigma \\vec{\\tau}_{\\text{ext}} = 0 \\iff \\Sigma \\tau_x = 0, \\; \\Sigma \\tau_y = 0, \\; \\Sigma \\tau_z = 0$$
   This guarantees that the angular acceleration of the body is zero ($\\vec{\\alpha} = 0$)."""
)

add_solution(
    74,
    "A bucket of water accelerates to the right across a horizontal table. How does the hydrostatic pressure vary horizontally between the left and right sides at equal depth?",
    "Fluid Mechanics & Elasticity",
    "3 Marks",
    """**Answer: Pressure is Higher on the Left (Trailing Edge) and Lower on the Right (Leading Edge)**

**Hydrodynamic Derivation:**
1. In a frame accelerating horizontally to the right with acceleration $a_x$, a fluid element experiences a horizontal fictitious (inertial) force to the left.
2. Consider a horizontal fluid element of length $dx$, cross-sectional area $A$, and mass $dm = \\rho A dx$.
3. By Newton's Second Law along the horizontal direction:
   $$(P - (P + dP)) A = dm \\cdot a_x \\implies -dP \\cdot A = (\\rho A dx) a_x$$
   $$\\frac{\\partial P}{\\partial x} = -\\rho a_x$$
4. Because $\\frac{\\partial P}{\\partial x}$ is negative, pressure decreases in the $+x$ (rightward) direction.
5. The free liquid surface tilts upward to the left at angle $\\tan\\theta = a_x / g$. At any horizontal line of equal elevation, the water column depth is greater on the left than on the right, making pressure strictly **greater at the left**."""
)

add_solution(
    75,
    "An organ pipe open at both ends is 0.85 m long. Assuming the speed of sound is 340 m/s, calculate the frequency of its third harmonic.",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: $600\\text{ Hz}$**

**Derivation:**
1. For an organ pipe open at both ends, all harmonic modes ($n = 1, 2, 3, \\dots$) exist:
   $$f_n = n \\left(\\frac{v}{2L}\\right)$$
2. Given parameters:
   - Length of pipe ($L$) = $0.85\\text{ m}$
   - Speed of sound ($v$) = $340\\text{ m/s}$
   - Harmonic order ($n$) = $3$
3. Fundamental frequency ($n = 1$):
   $$f_1 = \\frac{v}{2L} = \\frac{340\\text{ m/s}}{2 \\times 0.85\\text{ m}} = \\frac{340}{1.70} = 200\\text{ Hz}$$
4. Third harmonic frequency ($n = 3$):
   $$f_3 = 3 \\times f_1 = 3 \\times 200\\text{ Hz} = 600\\text{ Hz}$$"""
)

add_solution(
    76,
    "Derive the formula for the equivalent capacitance of two capacitors $C_1$ and $C_2$ connected in series.",
    "Electric Potential & Capacitance",
    "3 Marks",
    """**Answer: $C_{\\text{eq}} = \\frac{C_1 C_2}{C_1 + C_2}$**

**Derivation:**
1. In a series combination of capacitors:
   - The magnitude of charge $Q$ on each capacitor plate is identical: $Q_1 = Q_2 = Q$.
   - The total potential difference $V$ across the combination is the sum of the potential drops:
     $$V = V_1 + V_2$$
2. Using the definition of capacitance ($V = Q / C$):
   $$\\frac{Q}{C_{\\text{eq}}} = \\frac{Q}{C_1} + \\frac{Q}{C_2}$$
3. Dividing both sides by common charge $Q$:
   $$\\frac{1}{C_{\\text{eq}}} = \\frac{1}{C_1} + \\frac{1}{C_2} = \\frac{C_2 + C_1}{C_1 C_2}$$
4. Inverting gives:
   $$C_{\\text{eq}} = \\frac{C_1 C_2}{C_1 + C_2}$$"""
)

add_solution(
    77,
    "If the potential difference across an ohmic resistor is doubled, what happens to the electric current and electrical power dissipation?",
    "Current, Resistance & DC Circuits",
    "3 Marks",
    """**Answer: Current is Doubled; Power Dissipation is Quadrupled**

**Physical Explanation:**
1. **Ohm's Law:** For an ideal ohmic resistor at constant temperature, resistance $R$ is an invariant constant:
   $$I = \\frac{V}{R}$$
   If potential difference $V' = 2V$, then:
   $$I' = \\frac{2V}{R} = 2 I \\implies \\text{Current is doubled}.$$
2. **Joule Heating / Power Dissipation:**
   Electrical power is given by Joule's Law:
   $$P = V I = \\frac{V^2}{R} = I^2 R$$
   With doubled voltage:
   $$P' = \\frac{(2V)^2}{R} = \\frac{4 V^2}{R} = 4 P \\implies \\text{Power dissipation increases by a factor of 4}.$$"""
)

add_solution(
    78,
    "By using only two resistors $R_1$ and $R_2$, a student obtains equivalent resistances of $3\\ \\Omega$, $4\\ \\Omega$, $12\\ \\Omega$, and $16\\ \\Omega$. Determine the individual resistances $R_1$ and $R_2$.",
    "Current, Resistance & DC Circuits",
    "3 Marks",
    """**Answer: $R_1 = 4\\ \\Omega$ and $R_2 = 12\\ \\Omega$**

**Algebraic Proof:**
1. Two resistors can be configured in four distinct ways:
   - Connected in parallel: $R_p = \\frac{R_1 R_2}{R_1 + R_2}$ (minimum resistance).
   - Resistor 1 alone: $R_1$.
   - Resistor 2 alone: $R_2$.
   - Connected in series: $R_s = R_1 + R_2$ (maximum resistance).
2. From the given four values:
   - Minimum value: $R_p = 3\\ \\Omega$
   - Maximum value: $R_s = 16\\ \\Omega$
   - The two intermediate values must be the individual resistors: $4\\ \\Omega$ and $12\\ \\Omega$.
3. **Verification:**
   - Series: $R_s = 4 + 12 = 16\\ \\Omega$ (Matches given $16\\ \\Omega$).
   - Parallel: $R_p = \\frac{4 \\times 12}{4 + 12} = \\frac{48}{16} = 3\\ \\Omega$ (Matches given $3\\ \\Omega$).
4. Therefore, the two resistors are **$4\\ \\Omega$ and $12\\ \\Omega$**."""
)

add_solution(
    79,
    "State Faraday's Law of Electromagnetic Induction in words and as a mathematical equation. Explain the physical significance of Lenz's Law.",
    "Electromagnetic Induction & AC",
    "3 Marks",
    """**Answer: Induced EMF is Proportional to the Time Rate of Change of Magnetic Flux**

**Mathematical Statement:**
$$\\mathcal{E} = -N \\frac{d\\Phi_B}{dt}$$
where:
- $\\mathcal{E}$ is the induced electromotive force (in Volts).
- $N$ is the number of turns in the coil.
- $\\Phi_B = \\int \\vec{B} \\cdot d\\vec{A}$ is the magnetic flux through a single turn (in Webers).
- $\\frac{d\\Phi_B}{dt}$ is the time rate of change of magnetic flux.

**Lenz's Law (The Negative Sign):**
The negative sign expresses **Lenz's Law**, which states that the polarity of the induced emf generates an electric current whose secondary magnetic field opposes the original change in magnetic flux that produced it. This negative feedback is a direct manifestation of the **Conservation of Energy**."""
)

add_solution(
    80,
    "A generator supplies 100 V to the primary of a transformer with 50 primary turns and 500 secondary turns. Calculate the secondary voltage.",
    "Electromagnetic Induction & AC",
    "3 Marks",
    """**Answer: $1000\\text{ V}$**

**Calculation:**
1. The transformer turns-voltage relation is:
   $$\\frac{V_s}{V_p} = \\frac{N_s}{N_p}$$
2. Given:
   - $V_p = 100\\text{ V}$
   - $N_p = 50$
   - $N_s = 500$
3. Solve for $V_s$:
   $$V_s = V_p \\left(\\frac{N_s}{N_p}\\right) = 100\\text{ V} \\times \\left(\\frac{500}{50}\\right) = 100\\text{ V} \\times 10 = 1000\\text{ V}$$

**Conclusion:**
The secondary voltage is $1000\\text{ V}$."""
)

print(f"Added solutions 61-80. Total so far: {len(SOLUTIONS)}")

# ==================== QUESTIONS 81 to 100 ====================

add_solution(
    81,
    "Which type of electromagnetic radiation consists of photons with the greatest quantum energy? Compare gamma rays, X-rays, visible light, and radio waves.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Gamma Rays ($\\gamma$-rays)**

**Derivation:**
1. Photon energy is given by the Planck-Einstein relation:
   $$E = h f = \\frac{h c}{\\lambda}$$
   where $h$ is Planck's constant ($6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$) and $c$ is the speed of light.
2. Photon energy is directly proportional to frequency ($E \\propto f$) and inversely proportional to wavelength ($E \\propto 1/\\lambda$).
3. **Comparison across the EM spectrum:**
   - **Radio waves:** $f \\sim 10^4\\text{--}10^9\\text{ Hz}$, $E \\sim 10^{-10}\\text{--}10^{-6}\\text{ eV}$.
   - **Visible light:** $f \\sim 4\\text{--}7.5 \\times 10^{14}\\text{ Hz}$, $E \\sim 1.6\\text{--}3.1\\text{ eV}$.
   - **X-rays:** $f \\sim 10^{16}\\text{--}10^{19}\\text{ Hz}$, $E \\sim 100\\text{ eV--}100\\text{ keV}$.
   - **Gamma rays:** $f > 10^{19}\\text{ Hz}$, $E > 100\\text{ keV}$ (up to TeV).
4. Therefore, **gamma-ray photons possess the highest energy** in the electromagnetic spectrum."""
)

add_solution(
    82,
    "Define a virtual image in geometric optics and contrast it with a real image.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Image Formed by Diverging Light Rays That Cannot be Projected on a Physical Screen**

**Physical Explanation:**
1. **Virtual Image:**
   An optical image formed at a location where reflected or refracted light rays do not actually intersect, but merely **appear to diverge from** when traced backward as straight lines.
   - Light rays do not physically pass through the image point.
   - A virtual image **cannot be formed or captured on a physical screen**.
   - Examples: Images formed by plane mirrors, convex mirrors, and magnifying glasses (simple convex lens with object inside focal point).
2. **Real Image:**
   An optical image formed where light rays physically converge and intersect. A real image can be projected onto a physical screen or film."""
)

add_solution(
    83,
    "What are the units and dimensions of the optical magnification factor? Explain.",
    "Optics & Electromagnetic Waves",
    "3 Marks",
    """**Answer: Dimensionless (No Units)**

**Explanation:**
1. Linear magnification $m$ in geometric optics is defined as the ratio of image height ($h_i$) to object height ($h_o$):
   $$m = \\frac{h_i}{h_o} = -\\frac{d_i}{d_o}$$
   where $d_i$ is image distance and $d_o$ is object distance.
2. Because magnification is the ratio of two physical quantities having identical dimensions of length ($[L] / [L]$):
   $$[m] = \\frac{[L]}{[L]} = [M^0 L^0 T^0] = 1$$
3. Therefore, magnification is a pure, dimensionless numerical ratio having **no physical units**."""
)

add_solution(
    84,
    "In an adiabatic process, a system does 100 J of work and temperature drops by 5 K. In another process, it does 25 J of work and temperature drops by 5 K. Calculate heat capacity for the second process.",
    "Thermodynamics & Heat",
    "3 Marks",
    """**Answer: $C = +15\\text{ J/K}$**

**Thermodynamic Derivation:**
1. **First Law of Thermodynamics:**
   $$Q = \\Delta U + W$$
2. **Process 1 (Adiabatic Process):**
   In an adiabatic process, no heat is exchanged ($Q_1 = 0$):
   $$0 = \\Delta U_1 + W_1 \\implies \\Delta U_1 = -W_1$$
   Given work done by the object is $W_1 = +100\\text{ J}$:
   $$\\Delta U_1 = -100\\text{ J}$$
   The corresponding temperature change is $\\Delta T_1 = -5\\text{ K}$.
3. **Internal Energy as a State Function:**
   Internal energy $U$ depends only on the thermodynamic state (specifically on temperature for an ideal gas, $\\Delta U = C_V \\Delta T$).
   In Process 2, the temperature drop is also $\\Delta T_2 = -5\\text{ K}$, so the change in internal energy is identical:
   $$\\Delta U_2 = \\Delta U_1 = -100\\text{ J}$$
4. **Process 2 Heat Exchange ($Q_2$):**
   Given work done in Process 2 is $W_2 = +25\\text{ J}$:
   $$Q_2 = \\Delta U_2 + W_2 = -100\\text{ J} + 25\\text{ J} = -75\\text{ J}$$
5. **Heat Capacity ($C_2$):**
   $$C_2 = \\frac{Q_2}{\\Delta T_2} = \\frac{-75\\text{ J}}{-5\\text{ K}} = +15\\text{ J/K}$$"""
)

add_solution(
    85,
    "An ideal gas undergoes Joule free expansion into a vacuum within a rigid, thermally insulated container. Determine the changes in temperature, internal energy, and entropy.",
    "Thermodynamics & Heat",
    "3 Marks",
    """**Answer: $\\Delta T = 0$, $\\Delta U = 0$, and Entropy Increases ($\\Delta S > 0$)**

**Derivation:**
1. **Work ($W$):**
   The gas expands into an evacuated vacuum against zero opposing external pressure ($P_{\\text{ext}} = 0$).
   $$W = \\int P_{\\text{ext}} dV = 0$$
2. **Heat ($Q$):**
   The container is thermally insulated (adiabatic boundaries):
   $$Q = 0$$
3. **Internal Energy ($\\Delta U$):**
   By the First Law of Thermodynamics:
   $$\\Delta U = Q - W = 0 - 0 = 0$$
4. **Temperature ($\\Delta T$):**
   For an ideal gas, internal energy depends solely on temperature: $U = U(T)$.
   $$\\Delta U = 0 \\implies \\Delta T = 0$$
   The final temperature equals the initial temperature ($T_f = T_i$).
5. **Entropy Change ($\\Delta S$):**
   Free expansion is an irreversible process. Since final volume $V_f > V_i$:
   $$\\Delta S = n R \\ln\\left(\\frac{V_f}{V_i}\\right) > 0$$
   Entropy strictly increases, consistent with the Second Law of Thermodynamics."""
)

add_solution(
    86,
    "State the Law of Radioactive Decay. To what quantity is the instantaneous decay rate (activity) directly proportional?",
    "Nuclear & Particle Physics",
    "3 Marks",
    """**Answer: Proportional to the Number of Undecayed Nuclei Present ($R = \\lambda N$)**

**Derivation:**
1. Radioactive decay is a spontaneous, stochastic quantum process.
2. The probability of decay per unit time for any individual nucleus is an invariant constant called the **decay constant** ($\\lambda$).
3. For a large collection of $N(t)$ identical undecayed radioactive nuclei, the instantaneous rate of decay (nuclear activity $A$ or $R$) is:
   $$R(t) = -\\frac{dN}{dt} = \\lambda N(t)$$
4. Solving the differential equation:
   $$\\frac{dN}{N} = -\\lambda dt \\implies N(t) = N_0 e^{-\\lambda t}$$
5. Therefore, the activity at any instant is directly proportional to the number of undecayed parent nuclei remaining at that instant."""
)

add_solution(
    87,
    "A 2.0-kg block moves in a horizontal 0.50-m radius circle at angular speed 12 rad/s centered on the z-axis. Calculate the z-component of its angular momentum.",
    "Rotational Motion & Torque",
    "3 Marks",
    """**Answer: $L_z = 6.0\\text{ kg}\\cdot\\text{m}^2/\\text{s}$**

**Derivation:**
1. The circular trajectory lies parallel to the $xy$-plane, centered symmetrically on the $z$-axis.
2. The moment of inertia of the point mass $m$ about the $z$-axis is:
   $$I_z = m r^2$$
   Given $m = 2.0\\text{ kg}$ and $r = 0.50\\text{ m}$:
   $$I_z = (2.0\\text{ kg}) \\times (0.50\\text{ m})^2 = 2.0 \\times 0.25 = 0.50\\text{ kg}\\cdot\\text{m}^2$$
3. The $z$-component of angular momentum is:
   $$L_z = I_z \\omega_z$$
4. With angular speed $\\omega_z = 12\\text{ rad/s}$:
   $$L_z = 0.50\\text{ kg}\\cdot\\text{m}^2 \\times 12\\text{ rad/s} = 6.0\\text{ kg}\\cdot\\text{m}^2/\\text{s}$$"""
)

add_solution(
    88,
    "State the exact mathematical condition required for a body to be in translational equilibrium.",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: $\\Sigma \\vec{F} = 0$ (Net Resultant External Force is Zero)**

**Explanation:**
1. By Newton's Second Law of Motion for a system of mass $M$:
   $$\\Sigma \\vec{F}_{\\text{ext}} = M \\vec{a}_{\\text{cm}}$$
2. **Translational equilibrium** requires that the linear acceleration of the center of mass be zero:
   $$\\vec{a}_{\\text{cm}} = 0 \\implies \\frac{d\\vec{v}_{\\text{cm}}}{dt} = 0$$
3. This necessitates that the vector sum of all external forces acting on the body must be zero:
   $$\\Sigma \\vec{F}_{\\text{ext}} = 0$$
4. In component form:
   $$\\Sigma F_x = 0, \\quad \\Sigma F_y = 0, \\quad \\Sigma F_z = 0$$
5. The center of mass remains at rest or moves with uniform constant velocity."""
)

add_solution(
    89,
    "Determine the fundamental dimensions and SI derived units of angular momentum.",
    "Rotational Motion & Torque",
    "3 Marks",
    """**Answer: $[M L^2 T^{-1}]$ (SI unit: $\\text{kg}\\cdot\\text{m}^2/\\text{s}$ or $\\text{J}\\cdot\\text{s}$)**

**Dimensional Derivation:**
1. Angular momentum $\\vec{L}$ is defined as the cross product of position vector and linear momentum:
   $$\\vec{L} = \\vec{r} \\times \\vec{p} = \\vec{r} \\times (m \\vec{v})$$
2. Substitute fundamental dimensions:
   - $[r] = [L]$
   - $[m] = [M]$
   - $[v] = [L T^{-1}]$
3. Combining dimensions:
   $$[L] = [L] \\times [M] \\times [L T^{-1}] = [M L^2 T^{-1}]$$
4. SI units:
   $$\\text{kg} \\times \\text{m} \\times \\left(\\frac{\\text{m}}{\\text{s}}\\right) = \\text{kg}\\cdot\\text{m}^2/\\text{s}$$
   Notice that $1\\text{ J} = 1\\text{ kg}\\cdot\\text{m}^2/\\text{s}^2$, so:
   $$[L] = \\text{J}\\cdot\\text{s}$$"""
)

add_solution(
    90,
    "Define the ultimate tensile strength (UTS) of a material and distinguish it from the elastic limit and fracture point.",
    "Fluid Mechanics & Elasticity",
    "3 Marks",
    """**Answer: Maximum Engineering Stress a Material Can Sustain Before Necking and Fracture**

**Engineering Definitions:**
1. **Ultimate Tensile Strength (UTS):**
   The maximum point on the engineering stress-strain curve, representing the maximum nominal tensile stress a material can withstand under load without localized structural instability (necking):
   $$\\sigma_{\\text{UTS}} = \\frac{F_{\\max}}{A_0}$$
   where $A_0$ is the original cross-sectional area.
2. **Distinctions:**
   - **Proportional Limit / Elastic Limit:** The maximum stress up to which the material behaves elastically and returns to its original dimensions when unloaded (obeys Hooke's Law: $\\sigma = E \\varepsilon$).
   - **Fracture Point:** The stress at which the material completely separates into two pieces."""
)

add_solution(
    91,
    "Classify sound waves traveling in air in terms of wave type, particle motion, and mechanical nature.",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: Longitudinal Mechanical Waves**

**Physical Explanation:**
1. **Mechanical Nature:**
   Sound waves require an elastic material medium (solid, liquid, or gas) to propagate. They cannot travel through a vacuum.
2. **Longitudinal Character:**
   In air and fluids, sound propagates as alternating zones of high pressure/density (**compressions**) and low pressure/density (**rarefactions**).
3. The displacement of fluid molecules occurs **parallel** to the direction of energy propagation:
   $$s(x, t) = s_{\\max} \\cos(k x - \\omega t)$$
4. Because fluid media cannot sustain static shear stress, sound waves in fluids are purely **longitudinal**."""
)

add_solution(
    92,
    "Convert one complete revolution into radians and degrees, and state the definition of a radian.",
    "Rotational Motion & Torque",
    "3 Marks",
    """**Answer: $1\\text{ revolution} = 2\\pi\\text{ radians} = 360^\\circ$**

**Derivation & Definition:**
1. By geometric definition, an angle $\\theta$ in radians subtended by an arc of length $s$ on a circle of radius $r$ is:
   $$\\theta = \\frac{s}{r}$$
2. For one complete revolution around the circle, the arc length equals the full circumference:
   $$s = 2\\pi r$$
3. Therefore:
   $$\\theta = \\frac{2\\pi r}{r} = 2\\pi\\text{ radians} \\approx 6.283\\text{ rad}$$
4. In degrees:
   $$2\\pi\\text{ rad} = 360^\\circ \\implies 1\\text{ rad} = \\frac{360^\\circ}{2\\pi} \\approx 57.30^\\circ$$"""
)

add_solution(
    93,
    "A constant force of 100 N acts upon a body for 5.0 seconds. Calculate the impulse delivered and resulting momentum change.",
    "Momentum & Collisions",
    "3 Marks",
    """**Answer: $500\\text{ N}\\cdot\\text{s}$ (or $500\\text{ kg}\\cdot\\text{m/s}$)**

**Calculation:**
1. Impulse $\\vec{J}$ delivered by a constant force $\\vec{F}$ over time $\\Delta t$ is:
   $$\\vec{J} = \\vec{F} \\Delta t$$
2. Given $F = 100\\text{ N}$ and $\\Delta t = 5.0\\text{ s}$:
   $$J = 100\\text{ N} \\times 5.0\\text{ s} = 500\\text{ N}\\cdot\\text{s}$$
3. By the Impulse-Momentum Theorem:
   $$\\Delta p = J = 500\\text{ kg}\\cdot\\text{m/s}$$"""
)

add_solution(
    94,
    "Calculate the vector dot product of a vector $\\vec{A}$ with itself ($\\vec{A} \\cdot \\vec{A}$).",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: $A^2$ (Square of the Vector's Magnitude)**

**Derivation:**
1. The scalar (dot) product of any two vectors $\\vec{A}$ and $\\vec{B}$ is defined as:
   $$\\vec{A} \\cdot \\vec{B} = |\\vec{A}||\\vec{B}| \\cos\\theta$$
   where $\\theta$ is the angle between them.
2. For the dot product of vector $\\vec{A}$ with itself, $\\vec{B} = \\vec{A}$, so the angle between them is $\\theta = 0^\\circ$.
3. Since $\\cos(0^\\circ) = 1$:
   $$\\vec{A} \\cdot \\vec{A} = |\\vec{A}| |\\vec{A}| \\cos(0^\\circ) = A \\times A \\times 1 = A^2$$
4. In Cartesian components ($\\vec{A} = A_x \\hat{i} + A_y \\hat{j} + A_z \\hat{k}$):
   $$\\vec{A} \\cdot \\vec{A} = A_x^2 + A_y^2 + A_z^2 = A^2$$"""
)

add_solution(
    95,
    "Which of the following is NOT one of Piaget’s developmental stages: Sensorimotor, Preoperational, Concrete Operational, Non-operational?",
    "General Physics",
    "3 Marks",
    """**Answer: Non-operational (Item Scraped from Cross-Disciplinary File)**

**Verification:**
Jean Piaget's four canonical developmental stages in cognitive psychology are:
1. Sensorimotor Stage (Birth to 2 years)
2. Preoperational Stage (Ages 2 to 7)
3. Concrete Operational Stage (Ages 7 to 11)
4. Formal Operational Stage (Ages 12 and up)
*\"Non-operational\"* is a distractor and not a stage."""
)

add_solution(
    96,
    "According to Albert Bandura's Social Learning Theory, through what primary process do humans acquire novel behaviors?",
    "General Physics",
    "3 Marks",
    """**Answer: Observational Learning (Modeling / Vicarious Learning)**

**Verification:**
Albert Bandura demonstrated that human behavior is learned largely through **observational learning (modeling)**, where individuals observe the actions of others, retain the cognitive representation, and reproduce the behavior."""
)

add_solution(
    97,
    "All of the following are areas of interest for classical Behaviorists EXCEPT: Observable actions, Stimulus-response associations, Environmental conditioning, Unconscious desires.",
    "General Physics",
    "3 Marks",
    """**Answer: Unconscious Desires**

**Verification:**
Behaviorism (founded by J.B. Watson and B.F. Skinner) focuses exclusively on observable, measurable behavior and rejects unobservable mental constructs. **\"Unconscious desires\"** belongs to Sigmund Freud's psychoanalytic school of thought."""
)

add_solution(
    98,
    "A wave source vibrating at 500 Hz emits waves with a wavelength of 0.40 m. How long does it take for the wave to travel a distance of 40 m?",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: $0.20\\text{ seconds}$**

**Step-by-Step Derivation:**
1. Calculate the wave propagation speed ($v$):
   $$v = f \\lambda$$
   Given $f = 500\\text{ Hz} = 500\\text{ s}^{-1}$ and $\\lambda = 0.40\\text{ m}$:
   $$v = 500\\text{ s}^{-1} \\times 0.40\\text{ m} = 200\\text{ m/s}$$
2. Calculate the transit time ($t$) to travel distance $d = 40\\text{ m}$:
   $$t = \\frac{d}{v} = \\frac{40\\text{ m}}{200\\text{ m/s}} = 0.20\\text{ s}$$

**Conclusion:**
The wave takes exactly $0.20\\text{ seconds}$ to propagate through the $40\\text{ m}$ interval."""
)

add_solution(
    99,
    "Two people carry a uniform 3.00-m wooden board weighing 160 N. Person 1 applies an upward force of 60 N at one end. At what point does Person 2 lift, and with what force? Begin with a free-body diagram.",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: $F_2 = 100\\text{ N}$, positioned $2.40\\text{ m}$ from Person 1 (or $0.60\\text{ m}$ from the other end)**

**Free-Body Diagram Analysis:**
- Let the board lie along the $x$-axis from $x = 0$ to $x = L = 3.00\\text{ m}$.
- Person 1 lifts at the left end ($x_1 = 0$) with upward force $F_1 = 60\\text{ N}$.
- The weight of the uniform board $W = 160\\text{ N}$ acts downward at the center of gravity:
  $$x_{\\text{cg}} = \\frac{L}{2} = 1.50\\text{ m}$$
- Person 2 lifts with upward force $F_2$ at unknown position $x_2$.

**1. Translational Equilibrium Condition:**
$$\\Sigma F_y = 0 \\implies F_1 + F_2 - W = 0$$
$$60\\text{ N} + F_2 - 160\\text{ N} = 0 \\implies F_2 = 100\\text{ N}$$

**2. Rotational Equilibrium Condition (Torque about $x = 0$):**
$$\\Sigma \\tau_0 = 0 \\implies (F_1 \\times 0) - (W \\times x_{\\text{cg}}) + (F_2 \\times x_2) = 0$$
$$-(160\\text{ N} \\times 1.50\\text{ m}) + (100\\text{ N} \\times x_2) = 0$$
$$-240\\text{ N}\\cdot\\text{m} + 100 x_2 = 0 \\implies x_2 = \\frac{240}{100} = 2.40\\text{ m}$$

**Conclusion:**
Person 2 must exert an upward force of **$100\\text{ N}$** at a distance of **$2.40\\text{ m}$ from Person 1** (which is $0.60\\text{ m}$ from the opposite end of the board)."""
)

add_solution(
    100,
    "If a charged particle moves in a straight line through a region of space, can you definitively conclude that the magnetic field in that region is zero? Explain.",
    "Magnetic Fields & Ampere's Law",
    "3 Marks",
    """**Answer: No, the magnetic field is not necessarily zero**

**Physical Explanation & Derivation:**
1. The magnetic Lorentz force on a particle with electric charge $q$ moving with velocity $\vec{v}$ in a magnetic field $\vec{B}$ is:
   $$\\vec{F}_B = q (\\vec{v} \\times \\vec{B})$$
2. The magnitude of this force is:
   $$F_B = |q| v B \\sin\\theta$$
   where $\\theta$ is the angle between $\\vec{v}$ and $\\vec{B}$.
3. For the particle to continue in a straight line at constant velocity, the net deflecting force must be zero ($\\vec{F}_B = 0$). This occurs if:
   - Case 1: $B = 0$ (no magnetic field).
   - Case 2: **$\\vec{B} \\neq 0$, but the particle moves parallel ($\\theta = 0^\\circ$) or antiparallel ($\\theta = 180^\\circ$) to the magnetic field lines.** Because $\\sin(0^\\circ) = \\sin(180^\\circ) = 0$, the magnetic force vanishes identically:
     $$\\vec{v} \\times \\vec{B} = 0 \\implies \\vec{F}_B = 0$$
   - Case 3: An electric field $\\vec{E}$ is also present such that the electric force balances the magnetic force ($\\vec{E} = -\\vec{v} \\times \\vec{B}$, the velocity selector condition).
4. Therefore, observing a straight trajectory does not imply that $B = 0$."""
)

print(f"Added solutions 81-100. Total so far: {len(SOLUTIONS)}")

# ==================== QUESTIONS 101 to 119 ====================

add_solution(
    101,
    "A bike accelerates uniformly from rest to a speed of 7.10 m/s over a distance of 35.4 m. Determine the acceleration of the bike.",
    "Kinematics & Vectors",
    "5 Marks",
    """**Answer: $a = 0.712\\text{ m/s}^2$**

**Kinematic Derivation:**
1. Given parameters:
   - Initial velocity ($v_i$) = $0\\text{ m/s}$ (starting from rest)
   - Final velocity ($v_f$) = $7.10\\text{ m/s}$
   - Distance traveled ($s$) = $35.4\\text{ m}$
   - Acceleration ($a$) = ?
2. Using the third kinematic equation of motion for constant acceleration:
   $$v_f^2 = v_i^2 + 2 a s$$
3. Rearranging to solve for acceleration $a$:
   $$a = \\frac{v_f^2 - v_i^2}{2 s}$$
4. Substituting the values:
   $$a = \\frac{(7.10\\text{ m/s})^2 - (0)^2}{2 \\times 35.4\\text{ m}} = \\frac{50.41}{70.8}\\text{ m/s}^2 \\approx 0.712005\\text{ m/s}^2 \\approx 0.712\\text{ m/s}^2$$

**Conclusion:**
The uniform acceleration of the bicycle is **$0.712\\text{ m/s}^2$**."""
)

add_solution(
    102,
    "A single-turn flat coil of area $8.00\\text{ cm}^2$ is perpendicular to a magnetic field increasing uniformly from 0.500 T to 2.50 T in 1.00 s. If the coil has a resistance of $2.00\\ \\Omega$, calculate the induced current.",
    "Electromagnetic Induction & AC",
    "5 Marks",
    """**Answer: Induced Current $I = 0.800\\text{ mA}$ ($8.00 \\times 10^{-4}\\text{ A}$)**

**Step-by-Step Derivation:**
1. **Given Data:**
   - Number of turns: $N = 1$
   - Area of loop: $A = 8.00\\text{ cm}^2 = 8.00 \\times 10^{-4}\\text{ m}^2$
   - Initial magnetic field: $B_i = 0.500\\text{ T}$
   - Final magnetic field: $B_f = 2.50\\text{ T}$
   - Time elapsed: $\\Delta t = 1.00\\text{ s}$
   - Resistance: $R = 2.00\\ \\Omega$
   - Angle between $\\vec{B}$ and area normal $\\hat{n}$: $\\theta = 0^\\circ$ (perpendicular to plane).
2. **Magnetic Flux Change ($\\Delta\\Phi_B$):**
   $$\\Delta\\Phi_B = \\Delta(B A \\cos 0^\\circ) = A \\Delta B = A (B_f - B_i)$$
   $$\\Delta\\Phi_B = (8.00 \\times 10^{-4}\\text{ m}^2) \\times (2.50\\text{ T} - 0.500\\text{ T}) = (8.00 \\times 10^{-4}) \\times (2.00) = 1.60 \\times 10^{-3}\\text{ Wb}$$
3. **Induced EMF (Faraday's Law):**
   $$|\\mathcal{E}| = N \\frac{\\Delta\\Phi_B}{\\Delta t} = 1 \\times \\frac{1.60 \\times 10^{-3}\\text{ Wb}}{1.00\\text{ s}} = 1.60 \\times 10^{-3}\\text{ V} = 1.60\\text{ mV}$$
4. **Induced Current (Ohm's Law):**
   $$I = \\frac{|\\mathcal{E}|}{R} = \\frac{1.60 \\times 10^{-3}\\text{ V}}{2.00\\ \\Omega} = 8.00 \\times 10^{-4}\\text{ A} = 0.800\\text{ mA}$$"""
)

add_solution(
    103,
    "Two people are carrying a uniform wooden board that is 3.00 m long and weighs 160 N. If one person applies an upward force equal to 60 N at one end, at what point does the other person lift? Begin with a free-body diagram.",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: Upward force of 100 N applied 2.40 m from Person 1 (or 0.60 m from the opposite end)**

**Free-Body Diagram & Static Equilibrium:**
1. **Vertical Force Equilibrium ($\\Sigma F_y = 0$):**
   $$F_1 + F_2 - W = 0 \\implies 60\\text{ N} + F_2 - 160\\text{ N} = 0 \\implies F_2 = 100\\text{ N}$$
2. **Rotational Torque Equilibrium About Person 1's End ($x = 0$):**
   $$\\Sigma \\tau_0 = 0$$
   - The board is uniform, so its weight $W = 160\\text{ N}$ acts at its midpoint: $x_W = \\frac{3.00\\text{ m}}{2} = 1.50\\text{ m}$.
   - Let Person 2 lift at distance $x_2$ from Person 1:
   $$-(W \\times x_W) + (F_2 \\times x_2) = 0$$
   $$-(160\\text{ N} \\times 1.50\\text{ m}) + (100\\text{ N} \\times x_2) = 0$$
   $$-240\\text{ N}\\cdot\\text{m} + 100 x_2 = 0 \\implies x_2 = \\frac{240}{100} = 2.40\\text{ m}$$

**Conclusion:**
The second person lifts with a force of $100\\text{ N}$ at a point $2.40\\text{ m}$ from the first person."""
)

add_solution(
    104,
    "If a charged particle moves in a straight line through some region of space, can you say that the magnetic field in that region is zero?",
    "Magnetic Fields & Ampere's Law",
    "3 Marks",
    """**Answer: No, the magnetic field is not necessarily zero**

**Detailed Physical Explanation:**
1. The magnetic Lorentz force on a moving charge $q$ is:
   $$\\vec{F}_B = q (\\vec{v} \\times \\vec{B})$$
2. Its magnitude is:
   $$F_B = |q| v B \\sin\\theta$$
   where $\\theta$ is the angle between velocity $\\vec{v}$ and magnetic field $\\vec{B}$.
3. For the particle to move along a straight line at constant velocity, the net deflecting force must be zero ($\\vec{F}_B = 0$).
4. This condition is satisfied whenever:
   - $B = 0$, OR
   - **$\\theta = 0^\\circ$ (particle travels parallel to $\\vec{B}$)**, OR
   - **$\\theta = 180^\\circ$ (particle travels antiparallel to $\\vec{B}$)**.
   Because $\\sin(0^\\circ) = \\sin(180^\\circ) = 0$, the vector cross product $\\vec{v} \\times \\vec{B} = 0$, producing zero magnetic force even in an intensely strong magnetic field.
5. In addition, an electric field $\\vec{E}$ could be present that exactly balances the magnetic force ($\\vec{F}_{\\text{net}} = q(\\vec{E} + \\vec{v} \\times \\vec{B}) = 0$).
6. Therefore, a straight trajectory cannot prove that $\\vec{B} = 0$."""
)

add_solution(
    105,
    "A vessel is filled with gas at some equilibrium pressure and temperature. Can all gas molecules have the same speed? Explain using Kinetic Theory.",
    "Thermodynamics & Heat",
    "3 Marks",
    """**Answer: No, thermal equilibrium produces a continuous Maxwell-Boltzmann distribution of speeds**

**Physical Explanation:**
1. In a macroscopic gas in thermodynamic equilibrium, molecules constantly undergo billions of random elastic collisions per second with one another and with the container walls.
2. Even if all gas molecules were hypothetically started at identical speeds, subsequent random 3D oblique collisions would immediately redistribute kinetic energy among the particles.
3. In thermal equilibrium at temperature $T$, statistical mechanics dictates that molecular speeds follow the **Maxwell-Boltzmann speed distribution**:
   $$f(v) = 4\\pi \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} v^2 \\exp\\left(-\\frac{m v^2}{2 k_B T}\\right)$$
4. While the *average* kinetic energy per molecule is fixed strictly by temperature:
   $$\\langle K \\rangle = \\frac{1}{2} m v_{\\text{rms}}^2 = \\frac{3}{2} k_B T$$
   individual speeds are distributed continuously across a wide range from near zero to values several times $v_{\\text{rms}}$."""
)

add_solution(
    106,
    "What are the fundamental physical and mathematical properties required of a physically acceptable quantum mechanical wave function $\\Psi(\\vec{r}, t)$?",
    "Quantum & Modern Physics",
    "5 Marks",
    """**Answer: Single-valued, Continuous, Normalizable (Square-integrable), and Finite Everywhere**

**Detailed Properties:**
In quantum mechanics, the state of a physical system is completely described by its wave function $\\Psi(\\vec{r}, t)$, governed by the Schrödinger equation. By Max Born's statistical interpretation, the probability of finding the particle in differential volume $d^3r$ is:
$$P(\\vec{r}, t) d^3r = |\\Psi(\\vec{r}, t)|^2 d^3r$$
For $\\Psi$ to represent a physically realizable state, it must satisfy:
1. **Single-Valued:** $\\Psi(\\vec{r})$ must have only one unique value at each point in space, ensuring that probability density $|\\Psi|^2$ is uniquely defined.
2. **Continuous:** Both $\\Psi(\\vec{r})$ and its first spatial derivative $\\frac{\\partial\\Psi}{\\partial x}$ must be continuous everywhere. This ensures that the momentum operator $\\hat{p} = -i\\hbar\\nabla$ and kinetic energy operator $\\hat{T} = -\\frac{\\hbar^2}{2m}\\nabla^2$ yield well-defined, finite observables.
3. **Square-Integrable (Normalizability):** The integral of $|\\Psi|^2$ over all space must be finite, allowing normalization to unity:
   $$\\int_{-\\infty}^{\\infty} |\\Psi(\\vec{r}, t)|^2 d^3r = 1$$
   representing the certainty that the particle exists somewhere in the universe.
4. **Finite Everywhere:** $\\Psi$ cannot diverge to $\\pm\\infty$ at any point."""
)

add_solution(
    107,
    "A bike accelerates uniformly from rest to a speed of 7.10 m/s over a distance of 35.4 m. Determine the acceleration of the bike.",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: $a = 0.712\\text{ m/s}^2$**

**Step-by-Step Kinematic Solution:**
1. Using the third kinematic equation of motion:
   $$2 a s = v_f^2 - v_i^2$$
2. Given:
   - Initial speed $v_i = 0$
   - Final speed $v_f = 7.10\\text{ m/s}$
   - Displacement $s = 35.4\\text{ m}$
3. Substitute and calculate:
   $$2 a (35.4) = (7.10)^2 - (0)^2$$
   $$70.8 a = 50.41$$
   $$a = \\frac{50.41}{70.8} \\approx 0.712\\text{ m/s}^2$$"""
)

add_solution(
    108,
    "A flat loop of wire of single turn and area $8.00\\text{ cm}^2$ is perpendicular to a magnetic field increasing uniformly from 0.500 T to 2.50 T in 1.00 s. Find the induced current if coil resistance is $2.00\\ \\Omega$.",
    "Electromagnetic Induction & AC",
    "5 Marks",
    """**Answer: $I = 0.800\\text{ mA}$ ($8.00 \\times 10^{-4}\\text{ A}$)**

**Step-by-Step Derivation:**
1. Given:
   - $N = 1$
   - $A = 8.00\\text{ cm}^2 = 8.00 \\times 10^{-4}\\text{ m}^2$
   - $\\Delta B = B_f - B_i = 2.50\\text{ T} - 0.500\\text{ T} = 2.00\\text{ T}$
   - $\\Delta t = 1.00\\text{ s}$
   - $R = 2.00\\ \\Omega$
2. Rate of magnetic flux change:
   $$\\frac{\\Delta\\Phi_B}{\\Delta t} = A \\frac{\\Delta B}{\\Delta t} = (8.00 \\times 10^{-4}\\text{ m}^2) \\times \\frac{2.00\\text{ T}}{1.00\\text{ s}} = 1.60 \\times 10^{-3}\\text{ Wb/s}$$
3. Induced EMF:
   $$\\mathcal{E} = -N \\frac{\\Delta\\Phi_B}{\\Delta t} = -1.60 \\times 10^{-3}\\text{ V} = -1.60\\text{ mV}$$
4. Induced Current:
   $$I = \\frac{|\\mathcal{E}|}{R} = \\frac{1.60 \\times 10^{-3}\\text{ V}}{2.00\\ \\Omega} = 8.00 \\times 10^{-4}\\text{ A} = 0.800\\text{ mA}$$"""
)

add_solution(
    109,
    "An ideal gas in a vessel is heated from 300 K to 900 K. By what factor does each change: (a) Average molecular kinetic energy, (b) Root-mean-square molecular speed, (c) Average momentum change per wall collision?",
    "Thermodynamics & Heat",
    "5 Marks",
    """**Answer: (a) Factor of 3; (b) Factor of $\\sqrt{3} \\approx 1.73$; (c) Factor of $\\sqrt{3} \\approx 1.73$**

**Derivation from Kinetic Theory:**
Given temperature ratio:
$$\\frac{T_2}{T_1} = \\frac{900\\text{ K}}{300\\text{ K}} = 3$$

**(a) Average Molecular Kinetic Energy:**
From kinetic theory, the average translational kinetic energy per molecule is:
$$\\langle K \\rangle = \\frac{3}{2} k_B T \\propto T$$
$$\\frac{\\langle K \\rangle_2}{\\langle K \\rangle_1} = \\frac{T_2}{T_1} = 3 \\implies \\textbf{Increases by a factor of 3}$$

**(b) Root-Mean-Square Speed ($v_{\\text{rms}}$):**
$$v_{\\text{rms}} = \\sqrt{\\frac{3 k_B T}{m}} \\propto \\sqrt{T}$$
$$\\frac{v_{\\text{rms}, 2}}{v_{\\text{rms}, 1}} = \\sqrt{\\frac{T_2}{T_1}} = \\sqrt{3} \\approx 1.732 \\implies \\textbf{Increases by a factor of } \\sqrt{3} \\approx 1.73$$

**(c) Average Momentum Change per Wall Collision:**
For an elastic collision perpendicular to a wall, the momentum change is:
$$\\Delta p_x = 2 m v_x \\propto v_{\\text{rms}} \\propto \\sqrt{T}$$
$$\\frac{\\Delta p_2}{\\Delta p_1} = \\sqrt{\\frac{T_2}{T_1}} = \\sqrt{3} \\approx 1.732 \\implies \\textbf{Increases by a factor of } \\sqrt{3} \\approx 1.73$$"""
)

add_solution(
    110,
    "Who discovered the atomic nucleus? Describe the experimental setup, observations, and conclusion of this landmark experiment.",
    "Nuclear & Particle Physics",
    "5 Marks",
    """**Answer: Ernest Rutherford (1911) — The Alpha Particle Gold Foil Scattering Experiment**

**Experimental Setup:**
1. A radioactive source of high-energy alpha particles ($^4\\text{He}^{2+}$) was placed inside a collimating lead box to emit a narrow beam.
2. The beam was directed at an extremely thin sheet of gold foil (thickness $\\sim 400\\text{ nm}$, roughly 1000 atoms thick).
3. A movable circular fluorescent zinc sulfide (ZnS) screen coupled with a viewing microscope was rotated around the target to detect scintillations (light flashes).

**Key Observations:**
- Over $99.9\\%$ of alpha particles passed straight through the foil undeflected or with deflections $< 1^\\circ$.
- A tiny fraction (about $1$ in $8000$) suffered massive deflections greater than $90^\\circ$, and some bounced almost directly backward ($180^\\circ$).

**Conclusions & Deduction of the Nuclear Model:**
- Under J.J. Thomson's \"Plum Pudding\" model (where positive charge was uniformly spread across the entire atom), electric fields were far too weak to turn back massive, fast-moving alpha particles.
- Rutherford concluded that **all positive charge and virtually all mass ($>99.95\\%$) of the atom is concentrated in an unimaginably small, dense central core** called the **nucleus** (radius $\\sim 10^{-14}\\text{ m}$, compared to atomic radius $\\sim 10^{-10}\\text{ m}$), with electrons orbiting in vast surrounding empty space."""
)

add_solution(
    111,
    "In an analogy between electric current and automobile traffic flow, what corresponds to electric charge, current, potential difference (voltage), and resistance?",
    "Current, Resistance & DC Circuits",
    "3 Marks",
    """**Answer: Charge = Automobiles; Current = Traffic Flow Rate; Voltage = Driving Pressure; Resistance = Road Friction/Bottlenecks**

**Detailed Circuit-Traffic Analogy:**
1. **Electric Charge ($q$):**
   Corresponds to individual **automobiles (cars)** traveling along a highway.
2. **Electric Current ($I = dq/dt$):**
   Corresponds to the **traffic flow rate** (number of vehicles passing a checkpoint per unit time, e.g., cars per minute).
3. **Potential Difference / Voltage ($V$):**
   Corresponds to the **driving pressure, downhill gravitational slope, or motor urgency** propelling cars along the route.
4. **Electrical Resistance ($R$):**
   Corresponds to **road friction, lane narrowings, construction bottlenecks, or rough terrain** that impede smooth vehicle movement.
5. **Battery / Voltage Source:**
   Corresponds to a **vehicle ferry or uphill pump** that elevates cars back to high potential so continuous loop circulation can occur."""
)

add_solution(
    112,
    "(a) When can you expect a body to emit blackbody radiation? (b) Which radiation law is obeyed by the Sun and other stars? Explain it.",
    "Thermodynamics & Heat",
    "5 Marks",
    """**Answer: (a) Any Body at Temperature $T > 0\\text{ K}$; (b) Stefan-Boltzmann Law and Wien's Law**

**(a) Emission of Blackbody Radiation:**
- Every macroscopic physical body at an absolute thermodynamic temperature above absolute zero ($T > 0\\text{ K}$) spontaneously emits thermal electromagnetic radiation across a continuous spectrum.
- A **blackbody** is an idealized physical radiator that absorbs $100\\%$ of all incident radiation of all wavelengths without reflection or transmission. In thermal equilibrium, it radiates energy at the maximum theoretical rate governed by Planck's Radiation Law.

**(b) Laws Obeyed by the Sun and Stars:**
Stars approximate ideal blackbodies very closely, obeying:
1. **Stefan-Boltzmann Law:**
   Total radiant energy flux emitted per unit surface area per second is proportional to the fourth power of absolute surface temperature:
   $$F = \\sigma T^4 \\implies \\text{Total Luminosity } L = 4\\pi R^2 \\sigma T^4$$
   where $\\sigma = 5.67 \\times 10^{-8}\\text{ W}/(\\text{m}^2\\cdot\\text{K}^4)$ and $R$ is stellar radius.
2. **Wien's Displacement Law:**
   The peak wavelength $\\lambda_{\\max}$ of emission is inversely proportional to temperature:
   $$\\lambda_{\\max} T = b = 2.898 \\times 10^{-3}\\text{ m}\\cdot\\text{K}$$
   For the Sun ($T \\approx 5800\\text{ K}$), $\\lambda_{\\max} \\approx 500\\text{ nm}$ (visible green-yellow light)."""
)

add_solution(
    113,
    "Electric charge is said to be conserved. What does this mean? Explain with examples from macroscopic and subatomic physics.",
    "Electric Potential & Capacitance",
    "3 Marks",
    """**Answer: Net Electric Charge in Any Isolated System Remains Strictly Constant Over Time**

**Physical Principle & Meaning:**
The Law of Conservation of Electric Charge states that electric charge can neither be created nor destroyed. In any isolated physical system, the algebraic sum of all positive and negative charges remains invariant:
$$Q_{\\text{net}} = \\sum q_i = \\text{constant}$$

**Physical Examples:**
1. **Electrostatic Friction:** Rubbing a glass rod with silk transfers negative electrons from the glass to the silk. The positive charge acquired by the rod ($+q$) is exactly equal in magnitude to the negative charge acquired by the silk ($-q$), leaving the net charge of the system unchanged ($Q_{\\text{net}} = 0$).
2. **Pair Production & Annihilation:**
   A high-energy gamma-ray photon (charge = 0) can materialize into an electron and a positron:
   $$\\gamma \\to e^- (-1e) + e^+ (+1e)$$
   Net charge before = 0; net charge after = $-1e + 1e = 0$.
3. **Beta Decay in Nuclear Physics:**
   $$n^0 \\to p^+ (+1e) + e^- (-1e) + \\bar{\\nu}_e (0)$$
   Net charge before = 0; net charge after = 0."""
)

add_solution(
    114,
    "When a car drives horizontally off a cliff, why does it rotate forward (pitch nose-down) as it falls?",
    "Rotational Motion & Torque",
    "3 Marks",
    """**Answer: Unbalanced Gravitational Torque Acting During the Front-Wheel Departure**

**Dynamic Explanation:**
1. Consider a car moving forward horizontally with velocity $v_0$.
2. As the front wheels roll off the cliff edge, the upward normal support force from the ground on the front tires abruptly drops to zero ($N_{\\text{front}} = 0$).
3. At that critical instant, the rear wheels are still supported on the cliff surface, while the car's center of gravity (CG)—located forward of the rear axle—is suspended in mid-air.
4. The downward gravitational force $M g$ acting through the center of gravity exerts an **unbalanced clockwise torque** about the pivot line formed by the rear wheel contact patch:
   $$\\tau = M g d$$
   where $d$ is the horizontal distance from the rear axle to the center of mass.
5. By Newton's Second Law for rotation ($\\tau = I \\alpha$), this torque imparts a forward angular acceleration and angular velocity $\\omega$ (nose-down rotation).
6. Once the rear wheels leave the cliff, the car is in free fall. In the absence of external torque about the center of mass, angular momentum is conserved, and the car continues rotating forward as it follows a parabolic flight path."""
)

add_solution(
    115,
    "Why does a book sitting at rest on a table never accelerate spontaneously in response to the trillions of inter-atomic forces acting within it?",
    "Dynamics & Forces",
    "3 Marks",
    """**Answer: Internal Forces Sum to Zero by Newton's Third Law (Action-Reaction Cancellation)**

**Physical Derivation:**
1. The atoms within the book exert immense electrostatic Coulomb forces, electron exchange repulsions, and chemical bond forces on one another.
2. By **Newton's Third Law of Motion**, whenever atom $i$ exerts a force $\\vec{f}_{ij}$ on atom $j$, atom $j$ simultaneously exerts an equal and opposite force $\\vec{f}_{ji}$ on atom $i$:
   $$\\vec{f}_{ij} = -\\vec{f}_{ji} \\implies \\vec{f}_{ij} + \\vec{f}_{ji} = 0$$
3. Summing over all internal particle pairs in the book:
   $$\\sum_{\\text{internal}} \\vec{f} = \\sum_{i} \\sum_{j > i} (\\vec{f}_{ij} + \\vec{f}_{ji}) = 0$$
   All trillions of internal atomic forces cancel out in pairs.
4. By Newton's Second Law for a system of particles:
   $$M \\vec{a}_{\\text{cm}} = \\vec{F}_{\\text{net, ext}} = \\vec{N} + M\\vec{g}$$
   On the table, the upward normal contact force $\\vec{N}$ perfectly balances the downward gravitational force $M\\vec{g}$ ($\\vec{F}_{\\text{net, ext}} = 0$).
5. Since net external force is zero, the center of mass acceleration is strictly zero ($\\vec{a}_{\\text{cm}} = 0$). Internal forces can never accelerate the system as a whole."""
)

add_solution(
    116,
    "'Captain Planet' is floating in deep space between galaxies. When a gong sounds in a neighboring spaceship, Captain reacts to the sound. What is fundamentally wrong with this scenario from the physics of wave propagation?",
    "Oscillations & Waves",
    "3 Marks",
    """**Answer: Sound is a Mechanical Wave and Cannot Propagate Across the Vacuum of Space**

**Acoustic & Physical Explanation:**
1. **Mechanical Nature of Sound:**
   Sound is a mechanical longitudinal wave that propagates solely through the progressive collision and momentum transfer of material particles (compressions and rarefactions) in an elastic medium (solid, liquid, or gas).
   Its propagation speed is governed by:
   $$v = \\sqrt{\\frac{B}{\\rho}}$$
2. **Vacuum of Intergalactic Space:**
   Intergalactic space is an extreme ultra-high vacuum with an average density of fewer than a few hydrogen atoms per cubic meter.
3. In the absence of an elastic material medium, mechanical pressure vibrations cannot be transmitted from one spaceship to another across open space.
4. *(Note: Electromagnetic waves such as light and radio signals propagate freely through vacuum, but acoustic sound waves cannot).*"""
)

add_solution(
    117,
    "If you know the position vectors of a particle at two points along its path ($\\vec{r}_1$ at $t_1$ and $\\vec{r}_2$ at $t_2$), can you determine its instantaneous velocity? Can you determine its average velocity? Explain.",
    "Kinematics & Vectors",
    "3 Marks",
    """**Answer: Average Velocity CAN be determined; Instantaneous Velocity CANNOT be determined**

**Explanation:**
1. **Average Velocity ($\vec{v}_{\\text{avg}}$) — CAN be determined:**
   By definition, average velocity over a finite time interval $\\Delta t = t_2 - t_1$ depends solely on the initial and final position vectors:
   $$\\vec{v}_{\\text{avg}} = \\frac{\\Delta\\vec{r}}{\\Delta t} = \\frac{\\vec{r}_2 - \\vec{r}_1}{t_2 - t_1}$$
   Because $\\vec{r}_1, \\vec{r}_2, t_1, t_2$ are all known, $\\vec{v}_{\\text{avg}}$ is uniquely and exactly calculated.
2. **Instantaneous Velocity ($\vec{v}(t)$) — CANNOT be determined:**
   Instantaneous velocity is defined as the time derivative of position in the limit as $\\Delta t \\to 0$:
   $$\\vec{v}(t) = \\lim_{\\Delta t \\to 0} \\frac{\\Delta\\vec{r}}{\\Delta t} = \\frac{d\\vec{r}}{dt}$$
   Knowing only two discrete endpoints provides no information about the intermediate trajectory or acceleration profile between $t_1$ and $t_2$ (the particle could have stopped, reversed, looped, or accelerated wildly). Without a continuous equation of motion $\\vec{r}(t)$, instantaneous velocity cannot be determined."""
)

add_solution(
    118,
    "Steel will rupture if subjected to a shear stress exceeding $4.2 \\times 10^8\\text{ N/m}^2$. What sideward (shear) force is necessary to shear a steel bolt 1.0 cm in diameter?",
    "Fluid Mechanics & Elasticity",
    "5 Marks",
    """**Answer: $F_{\\text{shear}} \\approx 3.3 \\times 10^4\\text{ N}$ (or $33\\text{ kN}$)**

**Step-by-Step Derivation:**
1. **Given Data:**
   - Ultimate shear stress: $\\sigma_{\\text{shear}} = 4.2 \\times 10^8\\text{ N/m}^2$
   - Diameter of the bolt: $d = 1.0\\text{ cm} = 0.010\\text{ m}$
   - Radius of the bolt: $r = \\frac{d}{2} = 0.0050\\text{ m} = 5.0 \\times 10^{-3}\\text{ m}$
2. **Cross-Sectional Area Under Shear ($A$):**
   $$A = \\pi r^2 = \\pi (5.0 \\times 10^{-3}\\text{ m})^2 = 25 \\pi \\times 10^{-6}\\text{ m}^2 \\approx 7.854 \\times 10^{-5}\\text{ m}^2$$
3. **Shear Force Calculation:**
   Shear stress is defined as shear force per unit cross-sectional area:
   $$\\sigma_{\\text{shear}} = \\frac{F_{\\text{shear}}}{A} \\implies F_{\\text{shear}} = \\sigma_{\\text{shear}} \\times A$$
4. **Substitute the values:**
   $$F_{\\text{shear}} = (4.2 \\times 10^8\\text{ N/m}^2) \\times (7.854 \\times 10^{-5}\\text{ m}^2) \\approx 32,987\\text{ N} \\approx 3.3 \\times 10^4\\text{ N} = 33\\text{ kN}$$

**Conclusion:**
A sideward force of approximately **$33\\text{ kN}$** is required to shear the bolt."""
)

add_solution(
    119,
    "A table-tennis ball thrown at a stationary bowling ball makes a 1D elastic collision and bounces back. Compared to the bowling ball, does the table-tennis ball have: (a) larger or smaller momentum magnitude? (b) more or less kinetic energy? Prove using 1D elastic collision equations.",
    "Momentum & Collisions",
    "5 Marks",
    """**Answer: (a) Smaller magnitude of momentum; (b) Far more kinetic energy**

**Mathematical Proof:**
Let mass of table-tennis ball be $m$, mass of bowling ball be $M$, with $m \\ll M$.
Initial conditions: table-tennis ball $v_{1i} = v_0$, bowling ball $v_{2i} = 0$.

**1. Post-Collision Velocities (1D Elastic Collision):**
$$v_{1f} = \\left(\\frac{m - M}{m + M}\\right) v_0 \\approx -v_0$$
$$v_{2f} = \\left(\\frac{2m}{m + M}\\right) v_0 \\approx \\frac{2m}{M} v_0$$

**(a) Momentum Comparison:**
- Table-tennis ball momentum magnitude:
  $$p_1 = |m v_{1f}| \\approx m v_0$$
- Bowling ball momentum magnitude:
  $$p_2 = M v_{2f} \\approx M \\left(\\frac{2m}{M} v_0\\right) = 2 m v_0$$
- Comparing magnitudes:
  $$p_2 \\approx 2 p_1$$
  The table-tennis ball has a **smaller magnitude of momentum** (approximately half that of the bowling ball).
  *(Check: $p_i = +m v_0$; $p_f = -m v_0 + 2m v_0 = +m v_0$, conserved!)*

**(b) Kinetic Energy Comparison:**
- Table-tennis ball kinetic energy:
  $$K_1 = \\frac{1}{2} m v_{1f}^2 \\approx \\frac{1}{2} m v_0^2$$
- Bowling ball kinetic energy:
  $$K_2 = \\frac{1}{2} M v_{2f}^2 \\approx \\frac{1}{2} M \\left(\\frac{2m}{M} v_0\\right)^2 = \\frac{2 m^2}{M} v_0^2 = \\left(\\frac{4m}{M}\\right) \\left(\\frac{1}{2} m v_0^2\\right) = \\left(\\frac{4m}{M}\\right) K_1$$
- Since $m \\ll M$, the factor $\\frac{4m}{M} \\ll 1$, meaning the heavy bowling ball absorbs virtually zero kinetic energy.
- Therefore, the table-tennis ball retains almost $100\\%$ of the system's kinetic energy and has **far more kinetic energy** than the bowling ball."""
)

print(f"Total solutions defined: {len(SOLUTIONS)}")

# Now load original phy101_subjective.json and update each entry
with open("phy101_subjective.json", "r", encoding="utf-8") as f:
    orig_subj = json.load(f)

updated_subj = []
for q in orig_subj:
    qid = q["id"]
    if qid in SOLUTIONS:
        sol = SOLUTIONS[qid]
        q["question"] = sol["question"]
        q["marks"] = sol["marks"]
        q["topic"] = sol["topic"]
        q["source"] = sol["source"]
        q["answer"] = sol["answer"]
        q["solution"] = sol["solution"]
        q["model_answer"] = sol["model_answer"]
    updated_subj.append(q)

with open("phy101_subjective.json", "w", encoding="utf-8") as f:
    json.dump(updated_subj, f, indent=2, ensure_ascii=False)

print(f"Successfully updated all {len(updated_subj)} subjective questions in phy101_subjective.json!")
