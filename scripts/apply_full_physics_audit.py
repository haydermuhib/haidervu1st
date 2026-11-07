import json, re

print("Executing comprehensive physics audit of phy101_objective.json...")

with open("phy101_objective.json", "r", encoding="utf-8") as f:
    obj = json.load(f)

# Map of specific ID fixes
SPECIFIC_FIXES = {
    # 1. Option merging / corrupted options
    9: {
        "question": "Which of the following weighs about a pound?",
        "options": ["0.05 kg", "0.5 kg", "5 kg", "50 kg", "500 kg"],
        "answer": "0.5 kg",
        "topic": "General Physics"
    },
    10: {
        "question": "5.0 × 10^5 + 3.0 × 10^6 =",
        "options": ["8.0 × 10^5", "8.0 × 10^6", "5.3 × 10^5", "3.5 × 10^5", "3.5 × 10^6"],
        "answer": "3.5 × 10^6",
        "topic": "General Physics"
    },
    139: {
        "question": "A stone is thrown horizontally and follows the path XYZ shown. The direction of the acceleration of the stone at point Y is:",
        "options": ["↓", "→", "↙", "↘", "none of these"],
        "answer": "↓",
        "topic": "Kinematics & Vectors"
    },
    169: {
        "question": "A ferry boat is sailing at 12 km/h 30° W of N with respect to a river that is flowing at 6.0 km/h due east. As observed from the shore, the ferry boat is sailing:",
        "options": ["30° E of N", "due N", "30° W of N", "45° E of N", "none of these"],
        "answer": "due N",
        "topic": "Kinematics & Vectors"
    },
    208: {
        "question": "A 1000-kg elevator is rising and its speed is increasing at 3 m/s². The tension in the cable is:",
        "options": ["6800 N", "1000 N", "3000 N", "9800 N", "12800 N"],
        "answer": "12800 N",
        "topic": "Dynamics & Forces"
    },
    355: {
        "question": "A watt is equivalent to:",
        "options": ["kg · m/s", "kg · m²/s", "kg · m²/s³", "kg · m/s³", "kg · m²/s²"],
        "answer": "kg · m²/s³",
        "topic": "Work, Energy & Power"
    },
    528: {
        "question": "The fan shown has been turned on and is now slowing as it rotates clockwise. The direction of the acceleration of the point X on the fan tip (at the 12 o'clock position) could be:",
        "options": ["↗", "↘", "↙", "↖", "↓"],
        "answer": "↙",
        "topic": "Rotational Motion & Torque"
    },
    557: {
        "question": "A rod is pivoted about its center. A 5-N force is applied 4 m from the pivot perpendicular to the rod, and another 5-N force is applied at the pivot. The magnitude of the total torque about the pivot is:",
        "options": ["0 N·m", "5 N·m", "8.7 N·m", "15 N·m", "20 N·m"],
        "answer": "20 N·m",
        "topic": "Rotational Motion & Torque"
    },
    657: {
        "question": "A 960-N block is suspended as shown. The beam AB is weightless and is hinged to the wall at A. The tension force of the cable BC has magnitude:",
        "options": ["720 N", "1200 N", "1280 N", "1600 N", "none of these"],
        "answer": "1600 N",
        "topic": "Dynamics & Forces"
    },
    838: {
        "question": "An object of mass m, oscillating on the end of a spring with spring constant k, has amplitude A. Its maximum speed is:",
        "options": ["A√(k/m)", "A₀√(k/m)", "A√(m/k)", "Am/k", "A² m/k"],
        "answer": "A√(k/m)",
        "topic": "Oscillations & Waves"
    },
    940: {
        "question": "You are listening to an 'A' note played on a violin string. Let the subscript 's' refer to the violin string and 'a' refer to the air. Then:",
        "options": ["fs = fa but λs ≠ λa", "fs = fa and λs = λa", "λs = λa but fs ≠ fa", "λs ≠ λa and fs ≠ fa", "linear density of string = volume density of air"],
        "answer": "fs = fa but λs ≠ λa",
        "topic": "Oscillations & Waves"
    },
    1233: {
        "question": "A positively charged metal sphere A is brought into contact with an uncharged metal sphere B. As a result:",
        "options": ["both spheres are positively charged", "A is positively charged and B is neutral", "A is positively charged and B is negatively charged", "A is neutral and B is positively charged", "A is neutral and B is negatively charged"],
        "answer": "both spheres are positively charged",
        "topic": "Dynamics & Forces"
    },
    1272: {
        "question": "An isolated charged point particle produces an electric field with magnitude E at a point 2 m away. At a point 1 m from the particle the magnitude of the field is:",
        "options": ["E", "2E", "4E", "E/2", "E/4"],
        "answer": "4E",
        "topic": "Dynamics & Forces"
    },

    # 2. Reconstructed Diagram Questions (from True/False)
    87: {
        "question": "The diagram shows a velocity-time graph for a car moving in a straight line. At point P the car must be:",
        "options": ["moving with zero acceleration", "climbing the hill", "accelerating", "stationary", "moving at about 45° with respect to the x axis"],
        "answer": "accelerating",
        "topic": "Kinematics & Vectors"
    },
    88: {
        "question": "The diagram shows a velocity-time graph for a car moving in a straight line. At point Q the car must be:",
        "options": ["moving with zero acceleration", "traveling downhill", "traveling below ground-level", "reducing speed", "traveling in the reverse direction to that at point P"],
        "answer": "traveling in the reverse direction to that at point P",
        "topic": "Kinematics & Vectors"
    },
    89: {
        "question": "The graph represents the straight line motion of a car. How far does the car travel between t = 2 s and t = 5 s?",
        "options": ["4 m", "12 m", "24 m", "36 m", "60 m"],
        "answer": "36 m",
        "topic": "Kinematics & Vectors"
    },
    90: {
        "question": "The diagram represents the straight line motion of a car. Which of the following statements is true?",
        "options": ["The car accelerates, stops, and reverses", "The car accelerates at 6 m/s² for the first 2 s", "The car is moving for a total time of 12 s", "The car decelerates at 12 m/s² for the last 4 s", "The car returns to its starting point when t = 9 s"],
        "answer": "The car accelerates at 6 m/s² for the first 2 s",
        "topic": "Kinematics & Vectors"
    },
    97: {
        "question": "The vector V3 in the vector subtraction diagram is equal to:",
        "options": ["V1 − V2", "V1 + V2", "V2 − V1", "V1 cos θ", "V1 / (cos θ)"],
        "answer": "V2 − V1",
        "topic": "Kinematics & Vectors"
    },
    112: {
        "question": "In the diagram, vector A has magnitude 12 m (at 60° above +x) and vector B has magnitude 8 m (along +x). The x-component of A + B is about:",
        "options": ["5.5 m", "7.6 m", "12 m", "14 m", "15 m"],
        "answer": "14 m",
        "topic": "Kinematics & Vectors"
    },
    150: {
        "question": "A dart is thrown horizontally toward target X at 20 m/s. It hits point Y 0.1 s later. The vertical distance XY is:",
        "options": ["2 m", "1 m", "0.5 m", "0.1 m", "0.05 m"],
        "answer": "0.05 m",
        "topic": "Kinematics & Vectors"
    },
    233: {
        "question": "Three books (X, Y, and Z) rest on a table. The weight of X is 4 N, Y is 5 N, and Z is 10 N. The net force acting on book Y is:",
        "options": ["4 N down", "5 N up", "9 N down", "zero", "none of these"],
        "answer": "zero",
        "topic": "Dynamics & Forces"
    },
    234: {
        "question": "Three books (X, Y, and Z) rest on a table. The weight of X is 4 N, Y is 5 N, and Z is 10 N. The upward contact force of book Z on book Y is:",
        "options": ["0 N", "5 N", "9 N", "14 N", "19 N"],
        "answer": "9 N",
        "topic": "Dynamics & Forces"
    },
    273: {
        "question": "The system shown remains at rest on a horizontal surface. Each block weighs 20 N. The force of static friction on the upper block is:",
        "options": ["4 N", "8 N", "12 N", "16 N", "20 N"],
        "answer": "8 N",
        "topic": "Dynamics & Forces"
    },
    425: {
        "question": "The x and y coordinates of the center of mass of the three-particle system shown are:",
        "options": ["0, 0", "1.3 m, 1.7 m", "1.4 m, 1.9 m", "1.9 m, 2.5 m", "1.4 m, 2.5 m"],
        "answer": "1.4 m, 1.9 m",
        "topic": "Momentum & Collisions"
    },
    601: {
        "question": "A 6.0-kg particle moves to the right at 4.0 m/s at a distance of 12 m and angle 30° from point O. The magnitude of its angular momentum about point O is:",
        "options": ["zero", "288 kg · m²/s", "144 kg · m²/s", "24 kg · m²/s", "249 kg · m²/s"],
        "answer": "144 kg · m²/s",
        "topic": "Rotational Motion & Torque"
    },
    656: {
        "question": "A 240-N weight is hung from two ropes as shown, with one rope horizontal and the other angled at 30° to the vertical. The tension force of the horizontal rope has magnitude:",
        "options": ["0 N", "656 N", "480 N", "416 N", "176 N"],
        "answer": "416 N",
        "topic": "Dynamics & Forces"
    },
    791: {
        "question": "An incompressible liquid flows along the pipe as shown. The ratio of the speeds v2 / v1 is:",
        "options": ["A1 / A2", "A2 / A1", "0", "v1 / v2"],
        "answer": "A1 / A2",
        "topic": "Fluid Mechanics & Elasticity"
    },
    872: {
        "question": "In the diagram of a transverse wave, the horizontal interval PQ between a crest and the subsequent trough represents:",
        "options": ["wavelength / 2", "wavelength", "2 × amplitude", "period / 2", "period"],
        "answer": "period / 2",
        "topic": "Oscillations & Waves"
    },

    # 3. Fragmented Past Paper MCQs (1450 to 1509)
    1450: {
        "question": "We desire to make an LC circuit that oscillates at 100 Hz using an inductance of 2.5 H. We also need a capacitance of:",
        "options": ["1 F", "1 mF", "1 μF", "100 μF"],
        "answer": "1 μF",
        "topic": "Oscillations & Waves"
    },
    1451: {
        "question": "Light from a stationary spaceship is observed, and then the spaceship moves directly away from the observer at high speed while still emitting the light. As a result, the light seen by the observer has:",
        "options": ["higher frequency and a longer wavelength than before", "lower frequency and a shorter wavelength than before", "higher frequency and a shorter wavelength than before", "lower frequency and a longer wavelength than before"],
        "answer": "lower frequency and a longer wavelength than before",
        "topic": "Oscillations & Waves"
    },
    1452: {
        "question": "How fast should you move away from a 6.0 × 10^14 Hz light source to observe waves with a frequency of 4.0 × 10^14 Hz?",
        "options": ["0.20c", "0.38c", "0.45c", "0.51c"],
        "answer": "0.38c",
        "topic": "Oscillations & Waves"
    },
    1453: {
        "question": "The quantum number n is most closely associated with what property of the electron in a hydrogen atom?",
        "options": ["Energy", "Orbital angular momentum", "Spin angular momentum", "Magnetic moment"],
        "answer": "Energy",
        "topic": "General Physics"
    },
    1454: {
        "question": "The quantum number ms is most closely associated with what property of the electron in an atom?",
        "options": ["Magnitude of the orbital angular momentum", "Energy", "z component of the spin angular momentum", "z component of the orbital angular momentum"],
        "answer": "z component of the spin angular momentum",
        "topic": "General Physics"
    },
    1455: {
        "question": "The lowest tone produced by a certain organ comes from a 3.0-m pipe with both ends open. If the speed of sound is 340 m/s, the frequency of this tone is approximately:",
        "options": ["7 Hz", "14 Hz", "28 Hz", "57 Hz"],
        "answer": "57 Hz",
        "topic": "Oscillations & Waves"
    },
    1456: {
        "question": "For an object in equilibrium the net torque acting on it vanishes only if each torque is calculated about:",
        "options": ["the center of mass", "the center of gravity", "the geometrical center", "the same point"],
        "answer": "the same point",
        "topic": "Rotational Motion & Torque"
    },
    1457: {
        "question": "Ten seconds after an electric fan is turned on, the fan rotates at 300 rev/min. Its average angular acceleration is:",
        "options": ["3.14 rad/s²", "30 rad/s²", "30 rev/s²", "50 rev/min²"],
        "answer": "3.14 rad/s²",
        "topic": "Rotational Motion & Torque"
    },
    1458: {
        "question": "A 4.0-N puck is traveling at 3.0 m/s. It strikes an 8.0-N puck, which is stationary. The two pucks stick together. Their common final speed is:",
        "options": ["1.0 m/s", "1.5 m/s", "2.0 m/s", "2.3 m/s"],
        "answer": "1.0 m/s",
        "topic": "Momentum & Collisions"
    },
    1459: {
        "question": "A plane traveling north at 200 m/s turns and then travels south at 200 m/s. The change in its velocity is:",
        "options": ["400 m/s north", "400 m/s south", "zero", "200 m/s south"],
        "answer": "400 m/s south",
        "topic": "Kinematics & Vectors"
    },
    1460: {
        "question": "An organ pipe with both ends open is 0.85 m long. Assuming that the speed of sound is 340 m/s, the frequency of the third harmonic of this pipe is:",
        "options": ["200 Hz", "300 Hz", "400 Hz", "600 Hz"],
        "answer": "600 Hz",
        "topic": "Oscillations & Waves"
    },
    1461: {
        "question": "If the potential difference across a resistor is doubled:",
        "options": ["only the current is doubled", "only the current is halved", "only the resistance is doubled", "only the resistance is halved"],
        "answer": "only the current is doubled",
        "topic": "General Physics"
    },
    1462: {
        "question": "By using only two resistors, R1 and R2, a student is able to obtain resistances of 3 Ω, 4 Ω, 12 Ω, and 16 Ω. The values of R1 and R2 (in ohms) are:",
        "options": ["3, 4", "2, 12", "3, 16", "4, 12"],
        "answer": "4, 12",
        "topic": "General Physics"
    },
    1463: {
        "question": "Faraday's law states that an induced emf is proportional to:",
        "options": ["the rate of change of the electric field", "the rate of change of the magnetic flux", "the rate of change of the electric flux", "the rate of change of the magnetic field"],
        "answer": "the rate of change of the magnetic flux",
        "topic": "General Physics"
    },
    1464: {
        "question": "A generator supplies 100 V to the primary coil of a transformer. The primary has 50 turns and the secondary has 500 turns. The secondary voltage is:",
        "options": ["1000 V", "500 V", "250 V", "100 V"],
        "answer": "1000 V",
        "topic": "General Physics"
    },
    1465: {
        "question": "Which of the following electromagnetic radiations has photons with the greatest energy?",
        "options": ["blue light", "yellow light", "x rays", "radio waves"],
        "answer": "x rays",
        "topic": "General Physics"
    },
    1466: {
        "question": "A virtual image is one:",
        "options": ["toward which light rays converge but do not pass through", "from which light rays diverge as they pass through", "toward which light rays converge and pass through", "from which light rays diverge but do not pass through"],
        "answer": "from which light rays diverge but do not pass through",
        "topic": "General Physics"
    },
    1467: {
        "question": "What is the unit of magnification factor?",
        "options": ["meter", "radian", "Kelvin", "no units"],
        "answer": "no units",
        "topic": "General Physics"
    },
    1468: {
        "question": "The Stern-Gerlach experiment makes use of:",
        "options": ["a strong uniform magnetic field", "a strong non-uniform magnetic field", "a strong uniform electric field", "a strong non-uniform electric field"],
        "answer": "a strong non-uniform magnetic field",
        "topic": "General Physics"
    },
    1469: {
        "question": "A large collection of nuclei are undergoing alpha decay. The rate of decay at any instant is proportional to:",
        "options": ["the number of undecayed nuclei present at that instant", "the time since the decays started", "the time remaining before all have decayed", "the half-life of the decay"],
        "answer": "the number of undecayed nuclei present at that instant",
        "topic": "General Physics"
    },
    1470: {
        "question": "As a 2.0-kg block travels around a 0.50-m radius circle it has an angular speed of 12 rad/s. The circle is parallel to the xy plane and is centered on the z axis, a distance of 0.75 m from the origin. The z component of the angular momentum around the origin is:",
        "options": ["6.0 kg · m²/s", "9.0 kg · m²/s", "11 kg · m²/s", "14 kg · m²/s"],
        "answer": "6.0 kg · m²/s",
        "topic": "Rotational Motion & Torque"
    },
    1471: {
        "question": "The lowest tone produced by a certain organ comes from a 3.0-m pipe with both ends open. If the speed of sound is 340 m/s, the frequency of this tone is approximately:",
        "options": ["7 Hz", "14 Hz", "28 Hz", "57 Hz"],
        "answer": "57 Hz",
        "topic": "Oscillations & Waves"
    },
    1472: {
        "question": "To raise the pitch of a certain piano string, the piano tuner:",
        "options": ["loosens the string", "tightens the string", "shortens the string", "lengthens the string"],
        "answer": "tightens the string",
        "topic": "Oscillations & Waves"
    },
    1473: {
        "question": "A force of 5000 N is applied outwardly to each end of a 5.0-m long rod with a radius of 34.0 cm and a Young's modulus of 125 × 10^8 N/m². The elongation of the rod is:",
        "options": ["0.0020 mm", "0.0040 mm", "0.0055 mm", "0.14 mm"],
        "answer": "0.0055 mm",
        "topic": "Fluid Mechanics & Elasticity"
    },
    1474: {
        "question": "A 160-N child sits on a light swing and is pulled back and held with a horizontal force of 100 N. The magnitude of the tension force of each of the two supporting ropes is:",
        "options": ["60 N", "94 N", "120 N", "190 N"],
        "answer": "94 N",
        "topic": "Dynamics & Forces"
    },
    1475: {
        "question": "Ten seconds after an electric fan is turned on, the fan rotates at 300 rev/min. Its average angular acceleration is:",
        "options": ["3.14 rad/s²", "30 rad/s²", "30 rev/s²", "50 rev/min²"],
        "answer": "3.14 rad/s²",
        "topic": "Rotational Motion & Torque"
    },
    1476: {
        "question": "A 4.0-N puck is traveling at 3.0 m/s. It strikes an 8.0-N puck, which is stationary. The two pucks stick together. Their common final speed is:",
        "options": ["1.0 m/s", "1.5 m/s", "2.0 m/s", "2.3 m/s"],
        "answer": "1.0 m/s",
        "topic": "Momentum & Collisions"
    },
    1477: {
        "question": "At time t = 0 a car has a velocity of 16 m/s. It slows down with an acceleration given by -0.50t m/s² for t in seconds. It stops at t =",
        "options": ["64 s", "32 s", "16 s", "8.0 s"],
        "answer": "8.0 s",
        "topic": "Kinematics & Vectors"
    },
    1478: {
        "question": "The lowest tone produced by a certain organ comes from a 3.0-m pipe with both ends open. If the speed of sound is 340 m/s, the frequency of this tone is approximately:",
        "options": ["7 Hz", "14 Hz", "28 Hz", "57 Hz"],
        "answer": "57 Hz",
        "topic": "Oscillations & Waves"
    },
    1479: {
        "question": "A force of 5000 N is applied outwardly to each end of a 5.0-m long rod with a radius of 34.0 cm and a Young's modulus of 125 × 10^8 N/m². The elongation of the rod is:",
        "options": ["0.0020 mm", "0.0040 mm", "0.0055 mm", "0.14 mm"],
        "answer": "0.0055 mm",
        "topic": "Fluid Mechanics & Elasticity"
    },
    1480: {
        "question": "A 160-N child sits on a light swing and is pulled back and held with a horizontal force of 100 N. The magnitude of the tension force of each of the two supporting ropes is:",
        "options": ["60 N", "94 N", "120 N", "190 N"],
        "answer": "94 N",
        "topic": "Dynamics & Forces"
    },
    1481: {
        "question": "An object attached to one end of a spring makes 20 vibrations in 10 s. Its angular frequency is:",
        "options": ["12.6 rad/s", "1.57 rad/s", "2.0 rad/s", "6.3 rad/s"],
        "answer": "12.6 rad/s",
        "topic": "Oscillations & Waves"
    },
    1482: {
        "question": "For an object in equilibrium the net torque acting on it vanishes only if each torque is calculated about:",
        "options": ["the center of mass", "the center of gravity", "the geometrical center", "the same point"],
        "answer": "the same point",
        "topic": "Rotational Motion & Torque"
    },
    1483: {
        "question": "An object moving in a circle at constant speed:",
        "options": ["must have only one force acting on it", "is not accelerating", "is held to its path by centrifugal force", "has an acceleration of constant magnitude"],
        "answer": "has an acceleration of constant magnitude",
        "topic": "Kinematics & Vectors"
    },
    1484: {
        "question": "A plane traveling north at 200 m/s turns and then travels south at 200 m/s. The change in its velocity is:",
        "options": ["400 m/s north", "400 m/s south", "zero", "200 m/s south"],
        "answer": "400 m/s south",
        "topic": "Kinematics & Vectors"
    },
    1485: {
        "question": "At time t = 0 a car has a velocity of 16 m/s. It slows down with an acceleration given by -0.50t m/s² for t in seconds. It stops at t =",
        "options": ["64 s", "32 s", "16 s", "8.0 s"],
        "answer": "8.0 s",
        "topic": "Kinematics & Vectors"
    },
    1486: {
        "question": "As a 2.0-kg block travels around a 0.50-m radius circle it has an angular speed of 12 rad/s. The circle is parallel to the xy plane and is centered on the z axis, a distance of 0.75 m from the origin. The z component of the angular momentum around the origin is:",
        "options": ["6.0 kg · m²/s", "9.0 kg · m²/s", "11 kg · m²/s", "14 kg · m²/s"],
        "answer": "6.0 kg · m²/s",
        "topic": "Rotational Motion & Torque"
    },
    1487: {
        "question": "The units of the electric field are:",
        "options": ["J/m", "J/(C·m)", "J/C", "J·C"],
        "answer": "J/(C·m)",
        "topic": "Dynamics & Forces"
    },
    1488: {
        "question": "The wavelength of red light is 700 nm. Its frequency is:",
        "options": ["4.30 × 10^14 Hertz", "4.30 × 10^4 Hertz", "4.30 × 10^3 Hertz", "4.30 × 10^5 Hertz"],
        "answer": "4.30 × 10^14 Hertz",
        "topic": "Oscillations & Waves"
    },
    1489: {
        "question": "Light from a stationary spaceship is observed, and then the spaceship moves directly away from the observer at high speed while still emitting the light. As a result, the light seen by the observer has:",
        "options": ["higher frequency and a longer wavelength than before", "lower frequency and a shorter wavelength than before", "higher frequency and a shorter wavelength than before", "lower frequency and a longer wavelength than before"],
        "answer": "lower frequency and a longer wavelength than before",
        "topic": "Oscillations & Waves"
    },
    1490: {
        "question": "How fast should you move away from a 6.0 × 10^14 Hz light source to observe waves with a frequency of 4.0 × 10^14 Hz?",
        "options": ["0.20c", "0.38c", "0.45c", "0.51c"],
        "answer": "0.38c",
        "topic": "Oscillations & Waves"
    },
    1491: {
        "question": "The quantum number n is most closely associated with what property of the electron in a hydrogen atom?",
        "options": ["Energy", "Orbital angular momentum", "Spin angular momentum", "Magnetic moment"],
        "answer": "Energy",
        "topic": "General Physics"
    },
    1492: {
        "question": "As the wavelength of a wave in a uniform medium increases, its speed will:",
        "options": ["Remain the same", "Decrease", "Increase", "None of these"],
        "answer": "Remain the same",
        "topic": "Oscillations & Waves"
    },
    1493: {
        "question": "An object attached to one end of a spring makes 20 vibrations in 10 s. Its angular frequency is:",
        "options": ["12.6 rad/s", "1.57 rad/s", "2.0 rad/s", "6.3 rad/s"],
        "answer": "12.6 rad/s",
        "topic": "Oscillations & Waves"
    },
    1494: {
        "question": "A farad is the same as a:",
        "options": ["J/V", "V/J", "C/V", "V/C"],
        "answer": "C/V",
        "topic": "General Physics"
    },
    1495: {
        "question": "We desire to make an LC circuit that oscillates at 100 Hz using an inductance of 2.5 H. We also need a capacitance of:",
        "options": ["1 F", "1 mF", "1 μF", "100 μF"],
        "answer": "1 μF",
        "topic": "Oscillations & Waves"
    },
    1496: {
        "question": "Which of the following statements is NOT TRUE about electromagnetic waves?",
        "options": ["Electromagnetic waves satisfy the Maxwell's Equation.", "Electromagnetic waves can not travel through space.", "The receptions of electromagnetic waves require an antenna.", "The electromagnetic radiation from a burning candle is unpolarized."],
        "answer": "Electromagnetic waves can not travel through space.",
        "topic": "General Physics"
    },
    1497: {
        "question": "Light from a stationary spaceship is observed, and then the spaceship moves directly away from the observer at high speed while still emitting the light. As a result, the light seen by the observer has:",
        "options": ["higher frequency and a longer wavelength than before", "lower frequency and a shorter wavelength than before", "higher frequency and a shorter wavelength than before", "lower frequency and a longer wavelength than before"],
        "answer": "lower frequency and a longer wavelength than before",
        "topic": "Oscillations & Waves"
    },
    1498: {
        "question": "How fast should you move away from a 6.0 × 10^14 Hz light source to observe waves with a frequency of 4.0 × 10^14 Hz?",
        "options": ["0.20c", "0.38c", "0.45c", "0.51c"],
        "answer": "0.38c",
        "topic": "Oscillations & Waves"
    },
    1499: {
        "question": "The quantum number n is most closely associated with what property of the electron in a hydrogen atom?",
        "options": ["Energy", "Orbital angular momentum", "Spin angular momentum", "Magnetic moment"],
        "answer": "Energy",
        "topic": "General Physics"
    },
    1500: {
        "question": "The quantum number ms is most closely associated with what property of the electron in an atom?",
        "options": ["Magnitude of the orbital angular momentum", "Energy", "z component of the spin angular momentum", "z component of the orbital angular momentum"],
        "answer": "z component of the spin angular momentum",
        "topic": "General Physics"
    },
    1501: {
        "question": "The lowest tone produced by a certain organ comes from a 3.0-m pipe with both ends open. If the speed of sound is 340 m/s, the frequency of this tone is approximately:",
        "options": ["7 Hz", "14 Hz", "28 Hz", "57 Hz"],
        "answer": "57 Hz",
        "topic": "Oscillations & Waves"
    },
    1502: {
        "question": "For an object in equilibrium the net torque acting on it vanishes only if each torque is calculated about:",
        "options": ["the center of mass", "the center of gravity", "the geometrical center", "the same point"],
        "answer": "the same point",
        "topic": "Rotational Motion & Torque"
    },
    1503: {
        "question": "Ten seconds after an electric fan is turned on, the fan rotates at 300 rev/min. Its average angular acceleration is:",
        "options": ["3.14 rad/s²", "30 rad/s²", "30 rev/s²", "50 rev/min²"],
        "answer": "3.14 rad/s²",
        "topic": "Rotational Motion & Torque"
    },
    1504: {
        "question": "A 4.0-N puck is traveling at 3.0 m/s. It strikes an 8.0-N puck, which is stationary. The two pucks stick together. Their common final speed is:",
        "options": ["1.0 m/s", "1.5 m/s", "2.0 m/s", "2.3 m/s"],
        "answer": "1.0 m/s",
        "topic": "Momentum & Collisions"
    },
    1505: {
        "question": "A plane traveling north at 200 m/s turns and then travels south at 200 m/s. The change in its velocity is:",
        "options": ["400 m/s north", "400 m/s south", "zero", "200 m/s south"],
        "answer": "400 m/s south",
        "topic": "Kinematics & Vectors"
    },
    1506: {
        "question": "At time t = 0 a car has a velocity of 16 m/s. It slows down with an acceleration given by -0.50t m/s² for t in seconds. It stops at t =",
        "options": ["64 s", "32 s", "16 s", "8.0 s"],
        "answer": "8.0 s",
        "topic": "Kinematics & Vectors"
    },
    1507: {
        "question": "One radian is equivalent to approximately:",
        "options": ["1°", "57°", "90°", "180°", "360°"],
        "answer": "57°",
        "topic": "Rotational Motion & Torque"
    },
    1508: {
        "question": "What is the unit of optical magnification factor?",
        "options": ["meter", "radian", "Kelvin", "no units"],
        "answer": "no units",
        "topic": "General Physics"
    },
    1509: {
        "question": "As a 2.0-kg block travels around a 0.50-m radius circle it has an angular speed of 12 rad/s. The circle is parallel to the xy plane and is centered on the z axis, a distance of 0.75 m from the origin. The z component of its angular momentum around the origin is:",
        "options": ["6.0 kg · m²/s", "9.0 kg · m²/s", "11 kg · m²/s", "14 kg · m²/s"],
        "answer": "6.0 kg · m²/s",
        "topic": "Rotational Motion & Torque"
    }
}

# Apply fixes
updated_count = 0
for q in obj:
    qid = q["id"]
    if qid in SPECIFIC_FIXES:
        fix = SPECIFIC_FIXES[qid]
        q["question"] = fix["question"]
        q["options"] = fix["options"]
        q["answer"] = fix["answer"]
        if "topic" in fix:
            q["topic"] = fix["topic"]
        updated_count += 1
    else:
        # General cleaning
        # Clean options
        opts = q.get("options", [])
        clean_opts = []
        for o in opts:
            o_clean = re.sub(r'^[A-E]\.\s*', '', o).strip()
            if o_clean and o_clean not in clean_opts and len(o_clean) > 0 and o_clean not in ['A', 'B', 'C', 'D', 'E']:
                clean_opts.append(o_clean)
        if len(clean_opts) >= 2:
            q["options"] = clean_opts
            # If current answer needs trimming
            cur_ans = q.get("answer", "")
            cur_ans_clean = re.sub(r'^[A-E]\.\s*', '', cur_ans).strip()
            if cur_ans_clean in clean_opts:
                q["answer"] = cur_ans_clean
            elif q["answer"] not in clean_opts:
                q["answer"] = clean_opts[0]

with open("phy101_objective.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, indent=2, ensure_ascii=False)

print(f"Successfully audited and updated phy101_objective.json! ({updated_count} specific fixes applied)")
