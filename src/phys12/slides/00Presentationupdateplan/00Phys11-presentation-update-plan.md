You are an expert curriculum planner at the BC Ministry of Education. You are given the context of the BC Curriculum document for Physics 11 and Physics 12, the table of contents for the Chosen course textbook and the first draft of lesson slides in the form of latex beamer presentations for both courses. You are tasked with rating the current lessons, progression between documents adherence to curriculum guidelines and full utiliztion of relevant textbook contents. You must also make a list of redundancies and ensure the content is lean enough to ensure gradual content progression for the Physics 12 course.

### Physics 11 Curriculum

<file_contents>
File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/en_science_11_physics_elab.md

```markdown
# BIG IDEAS

An object's motion can be predicted, analyzed, and described.
Forces influence the motion of an object.
Energy is found in different forms, is conserved, and has the ability to do work.
Mechanical waves transfer energy but not matter.

## Learning Standards

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Curricular Competencies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                          Content                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Students are expected to be able to do the following: <br> Questioning and predicting <br> - Demonstrate a sustained intellectual curiosity about a scientific topic or problem <br> of personal, local, or global interest <br> - Make observations aimed at identifying their own questions, including increasingly <br> abstract ones, about the natural world <br> - Formulate multiple hypotheses and predict multiple outcomes <br> Planning and conducting <br> - Collaboratively and individually plan, select, and use appropriate investigation <br> methods, including field work and lab experiments, to collect reliable data <br> (qualitative and quantitative) <br> - Assess risks and address ethical, cultural, and/or environmental issues <br> associated with their proposed methods <br> - Use appropriate SI units and appropriate equipment, including digital technologies, <br> to systematically and accurately collect and record data <br> - Apply the concepts of accuracy and precision to experimental procedures <br> and data: <br> - significant figures <br> - uncertainty <br> - scientific notation | Students are expected to know the following: <br> - vector and scalar quantities <br> - horizontal uniform and accelerated motion <br> - projectile motion <br> - contact forces and the factors that affect magnitude <br> and direction <br> - mass, force of gravity, and apparent weight <br> - Newton's laws of motion and free-body diagrams <br> - balanced and unbalanced forces in systems <br> - conservation of energy; principle of work and energy <br> - power and efficiency <br> - simple machines and mechanical advantage <br> - applications of simple machines by First Peoples <br> - electric circuits (DC), Ohm's law, and Kirchhoff's laws <br> - thermal equilibrium and specific heat capacity <br> - generation and propagation of waves <br> - properties and behaviours of waves <br> - characteristics of sound <br> - resonance and frequency of sound <br> - graphical methods in physics |

## Learning Standards (continued)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Curricular Competencies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Content |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----: |
| Processing and analyzing data and information <br> - Experience and interpret the local environment <br> - Apply First Peoples perspectives and knowledge, other ways of knowing, and local knowledge <br> as sources of information <br> - Seek and analyze patterns, trends, and connections in data, including describing relationships <br> between variables, performing calculations, and identifying inconsistencies <br> - Construct, analyze, and interpret graphs, models, and/or diagrams <br> - Use knowledge of scientific concepts to draw conclusions that are consistent with evidence <br> - Analyze cause-and-effect relationships <br> Evaluating <br> - Evaluate their methods and experimental conditions, including identifying sources of error <br> or uncertainty, confounding variables, and possible alternative explanations and conclusions <br> - Describe specific ways to improve their investigation methods and the quality of their data <br> - Evaluate the validity and limitations of a model or analogy in relation to the phenomenon <br> modelled <br> - Demonstrate an awareness of assumptions, question information given, and identify bias <br> in their own work and in primary and secondary sources <br> - Consider the changes in knowledge over time as tools and technologies have developed <br> - Connect scientific explorations to careers in science <br> - Exercise a healthy, informed skepticism and use scientific knowledge and findings <br> to form their own investigations to evaluate claims in primary and secondary sources <br> - Consider social, ethical, and environmental implications of the findings from their own <br> and others' investigations <br> - Critically analyze the validity of information in primary and secondary sources and evaluate <br> the approaches used to solve problems <br> - Assess risks in the context of personal safety and social responsibility |         |

## Learning Standards (continued)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Curricular Competencies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Content |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----: |
| Applying and innovating <br> - Contribute to care for self, others, community, and world through individual <br> or collaborative approaches <br> - Co-operatively design projects with local and/or global connections and applications <br> - Contribute to finding solutions to problems at a local and/or global level <br> through inquiry <br> - Implement multiple strategies to solve problems in real-life, applied, <br> and conceptual situations <br> - Consider the role of scientists in innovation <br> Communicating <br> - Formulate physical or mental theoretical models to describe a phenomenon <br> - Communicate scientific ideas and information, and perhaps a suggested course <br> of action, for a specific purpose and audience, constructing evidence-based <br> arguments and using appropriate scientific language, conventions, and <br> representations <br> - Express and reflect on a variety of experiences, perspectives, and worldviews <br> through place |         |

- motion:

Sample questions to support inquiry with students:

- How can uniform motion and uniform acceleration be modelled?
- How can the path of a projectile be changed?
- Forces:

Sample questions to support inquiry with students:

- How can forces change the motion of an object?
- How can Newton's laws be used to explain changes in motion?
- Energy:

Sample questions to support inquiry with students:

- What is the relationship between work, energy, and power in a system?
- How are the conservation laws applied in parallel and series circuits?
- Why can't a machine be $100 \%$ efficient?
- waves:

Sample questions to support inquiry with students:

- What are the factors that affect wave behaviours?
- How would you investigate the relationships between the properties of a wave and properties of the medium?
- How can you determine which harmonics are audible in different musical instruments?

## Curricular Competencies - Elaborations

- Questioning and predicting:

Sample opportunities to support student inquiry:

- Make observations to determine the effect that launch angle has on the path of a projectile.
- Generate a hypothesis about the factors that affect the force of friction.
- Find examples of simple machines developed by local First Peoples.
- Observe the similarities and differences between series and parallel circuits.
- Observe waves in natural settings (e.g., lakes, oceans, rivers).

## - Planning and conducting:

Sample opportunities to support student inquiry:

- Choose appropriate equipment and variables to experimentally determine acceleration due to gravity.
- Collect accurate and precise data to determine a spring constant, using correct units.
- Compare weight measurements from a stationary and accelerating elevator (i.e., apparent weight).
- Collect voltage and current data with analog and digital tools using appropriate units.
- Use a calorimeter to collect accurate and precise data needed to determine specific heat capacity.
- What data are needed to determine the speed of sound in air?
- Processing and analyzing data and information:

Sample opportunities to support student inquiry:

- Derive equations and construct diagrams that use graphical vector addition or subtraction to determine a resultant for a physical phenomenon (e.g., displacement of an object, change in velocity or acceleration of an object, $F_{\text {net }}$ equations).
- Compare an experimental result with a theoretical result and calculate $\%$ error or difference (e.g., acceleration due to gravity, coefficient of friction).
- Diagram the orthogonal components of the forces acting on an object on a horizontal surface and an inclined plane.
- Interpret free-body diagrams to develop an equation that describes the motion of an object.
- Create and interpret circuit diagrams.
- Identify wave behaviour patterns in mediums with different properties (e.g., material, fixed/open-end, densities).
- Evaluating:

Sample opportunities to support student inquiry:

- Identify sources of random and systematic error in lab activities.
- Investigate assumptions regarding surface area and the force of friction.
- What are the limitations of free-body diagrams?
- What explanations can you offer when your experimental data show that energy is not conserved?
- Describe ways to improve accuracy and precision when launching projectiles.
- Consider the social and environmental implications of noise pollution generated by sources such as ear buds, cell phones, or sporting events.

## - Applying and innovating:

Sample opportunities to support student inquiry:

- Design and create a carnival game that applies the principles of projectile motion.
- Collaboratively design an obstacle course that demonstrates Newton's laws.
- Using exemplars of First Peoples traditional dwellings, design your own heat-efficient structure.
- Use research to present possible innovations to replace the internal combustion engine.
- How has an understanding of physics influenced innovations in sports (e.g., technical clothing and/or materials, ski design, luge technique, bicycle gears, skate parks)?
- Communicating:

Sample opportunities to support student inquiry:

Curricular Competencies - Elaborations

- Present and defend evidence to prove that an object has uniform or accelerated motion.
- Visually represent the differences between scalar and vector quantities on a local map.
- Model the reduction in friction on an object as the angle of inclination increases.
- Create a model that demonstrates constructive and destructive interference of waves.
- place: Place is any environment, locality, or context with which people interact to learn, create memory, reflect on history, connect with culture, and establish identity. The connection between people and place is foundational to First Peoples perspectives.

Content - Elaborations

- vector and scalar quantities:
- addition and subtraction
- right-angle triangle trigonometry
- uniform and accelerated motion: graphical and quantitative analysis
- projectile motion: 1D and 2D, including:
- vertical launch
- horizontal launch
- angled launch
- contact forces: for example, normal force, spring force, tension force, frictional force
- Newton's laws of motion:
- First: the concept of mass as a measure of inertia
- Second: net force from one or more forces
- Third: actions/reactions happen at the same time in pairs
- forces in systems:
- one-body and multi-body systems
- inclined planes
- angled forces
- elevators
- power and efficiency:
- mechanical and electrical (e.g., light bulbs, simple machines, motors, steam engines, kettle)
- numerical examples (e.g., resistance, power, and efficiency in circuits)
- simple machines: lever, ramp, wedge, pulley, screw, wheel and axle
- electric circuits (DC), Ohm's law, and Kirchhoff's laws: including terminal voltage versus electromotive force (EMF) (e.g., safety, power distribution, fuses/breakers, switches, overload, short circuits, alternators)
- thermal equilibrium: as an application of law of conservation of energy (e.g., calorimeter)
- propagation of waves:
- transverse versus longitudinal
  $-\quad$ linear versus circular
- properties and behaviours:
- properties: differences between the properties of a wave and the properties of the medium, periodic versus pulse
- behaviours: reflection (open and fixed end), refraction, transmission, diffraction, interference, Doppler shift, standing waves, interference patterns, law of superposition
- characteristics: for example, pitch, volume, speed, Doppler effect, sonic boom
- frequency: for example, harmonic, fundamental/natural, beat frequency
- graphical methods:
- plotting of linear relationships given a physical model (e.g., uniform motion, resistance)
- calculation of the slope of a line of best fit, including significant figures and appropriate units
- interpolation and extrapolation data from a constructed graph (e.g., position, instantaneous velocity)
- calculations and interpretations of area under the curve on a constructed graph (e.g., displacement, work)
```

</file_contents>

### Physics 12 Curriculum

<file_contents>
File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/en_science_12_physics_elab.md

```markdown
## BIG IDEAS

## Measurement of motion depends

on our frame of reference.Forces can cause linear and circular motion.
Forces and energy interactions occur within fields.
Momentum is conserved within
a closed and isolated system.

# Learning Standards

## Curricular Competencies

Students are expected to be able to do the following:
Questioning and predicting

- Demonstrate a sustained intellectual curiosity about a scientific topic or problem of personal, local, or global interest
- Make observations aimed at identifying their own questions, including increasingly abstract ones, about the natural world
- Formulate multiple hypotheses and predict multiple outcomes

## Planning and conducting

- Collaboratively and individually plan, select, and use appropriate investigation methods, including field work and lab experiments, to collect reliable data (qualitative and quantitative)
- Assess risks and address ethical, cultural, and/or environmental issues associated with their proposed methods
- Use appropriate SI units and appropriate equipment, including digital technologies, to systematically and accurately collect and record data
- Apply the concepts of accuracy and precision to experimental procedures and data:
- significant figures
- uncertainty
- scientific notation

## Content

Students are expected to know the following:

- frames of reference
- relative motion within a stationary reference frame
- postulates of special relativity
- relativistic effects within a moving reference frame
- static equilibrium
- uniform circular motion:
- centripetal force and acceleration
- changes to apparent weight
- First Peoples knowledge and applications of forces in traditional technologies
- gravitational field and Newton's law of universal gravitation
- gravitational potential energy
- gravitational dynamics and energy relationships
- electric field and Coulomb's law
- electric potential energy, electric potential, and electric potential difference
- electrostatic dynamics and energy relationships
- magnetic field and magnetic force
- electromagnetic induction
- applications of electromagnetic induction
- impulse and momentum
- conservation of momentum and energy in collisions
- graphical methods in physics

## Learning Standards (continued)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Curricular Competencies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Content |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----: |
| Processing and analyzing data and information <br> - Experience and interpret the local environment <br> - Apply First Peoples perspectives and knowledge, other ways of knowing, and local knowledge <br> as sources of information <br> - Seek and analyze patterns, trends, and connections in data, including describing relationships <br> between variables, performing calculations, and identifying inconsistencies <br> - Construct, analyze, and interpret graphs, models, and/or diagrams <br> - Use knowledge of scientific concepts to draw conclusions that are consistent with evidence <br> - Analyze cause-and-effect relationships <br> Evaluating <br> - Evaluate their methods and experimental conditions, including identifying sources of error <br> or uncertainty, confounding variables, and possible alternative explanations and conclusions <br> - Describe specific ways to improve their investigation methods and the quality of their data <br> - Evaluate the validity and limitations of a model or analogy in relation to the phenomenon <br> modelled <br> - Demonstrate an awareness of assumptions, question information given, and identify bias <br> in their own work and in primary and secondary sources <br> - Consider the changes in knowledge over time as tools and technologies have developed <br> - Connect scientific explorations to careers in science <br> - Exercise a healthy, informed skepticism and use scientific knowledge and findings <br> to form their own investigations to evaluate claims in primary and secondary sources <br> - Consider social, ethical, and environmental implications of the findings from their own <br> and others' investigations <br> - Critically analyze the validity of information in primary and secondary sources and evaluate <br> the approaches used to solve problems <br> - Assess risks in the context of personal safety and social responsibility |         |

## Learning Standards (continued)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Curricular Competencies                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Content |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----: |
| Applying and innovating <br> - Contribute to care for self, others, community, and world through individual <br> or collaborative approaches <br> - Co-operatively design projects with local and/or global connections and applications <br> - Contribute to finding solutions to problems at a local and/or global level <br> through inquiry <br> - Implement multiple strategies to solve problems in real-life, applied, and conceptual <br> situations <br> - Consider the role of scientists in innovation <br> Communicating <br> - Formulate physical or mental theoretical models to describe a phenomenon <br> - Communicate scientific ideas and information, and perhaps a suggested course <br> of action, for a specific purpose and audience, constructing evidence-based <br> arguments and using appropriate scientific language, conventions, and <br> representations <br> - Express and reflect on a variety of experiences, perspectives, and worldviews <br> through place |         |

- Measurement of motion:

Sample questions to support inquiry with students:

- When are measurements considered to be relative?
- How is vector addition/subtraction different from scalar addition/subtraction?
- What are the implications of the theory of special relativity?

## - linear and circular motion:

Sample questions to support inquiry with students:

- Under what conditions do forces not cause linear or circular motion?
- Why do you feel a sideways sliding motion when you speed around a corner in a vehicle?
- Why must the "orbiting electron" model of the atom be false?
- fields:

Sample questions to support inquiry with students:

- Why is gravity considered to be a fundamental force?
- Explain the similarities and differences between electrostatic force and gravitational force.
- How are electric fields similar to magnetic and gravitational fields?
- How can a conductor and a magnet be used to generate electricity?
- What is the relationship between the moon orbiting Earth and an apple falling to the ground?
- Momentum:

Sample questions to support inquiry with students:

- Why would you consider an inelastic or an elastic collision to be more dangerous?
- Why does it appear that energy is not conserved during some collisions?
- Why are cars designed with crumple zones and airbags?
- How does a ballistic pendulum demonstrate conservation laws?

| Curricular Competencies - Elaborations                                                                       | SCIENCE - Physics |
| :----------------------------------------------------------------------------------------------------------- | ----------------: |
| - Questioning and predicting:                                                                                |                   |
| Sample opportunities to support student inquiry:                                                             |                   |
| - Predict the age of a sibling who travels to Mars at half the speed of light and returns a few years later. |                   |
| - Observe a variety of ways in which a seesaw can be kept parallel to the ground.                            |                   |
| - Generate a hypothesis about the factors that can be used to increase the magnitude of a field.             |                   |
| - Observe the motion of a ballistics pendulum when different masses are used.                                |                   |

- Planning and conducting:

Sample opportunities to support student inquiry:

- Collaboratively plan a way to determine the upstream angle needed to land a motorized boat directly across a body of moving water in the local area.
- Determine the effect of the impulse delivered by a bumper car as it hits a wall at different angles.
- Processing and analyzing data and information:

Sample opportunities to support student inquiry:

- Construct vector diagrams and derive equations that use vector addition or subtraction to determine a resultant.
- Use the relativistic mass of a particle in a particle accelerator to determine the radius of curvature needed to keep it within the walls of the device.
- How do First Peoples traditional hunting methods apply the principles of relative motion?
- What effect does velocity have on apparent weight (e.g., horizontal circles, vertical circles)?
- Visually represent the electric fields around a variety of point charges and plates.
- Evaluating:

Sample opportunities to support student inquiry:

- Identify sources of random and systematic error in lab experiments.
- Compare an experimental result with a theoretical result and calculate \% error or difference and suggest an explanation for any discrepancies.
- Evaluate the validity of the representation of special relativity in science fiction movies.
- Critically analyze the findings that suggest the existence of gravitational waves.
- What are the social, ethical, and environmental implications of the application of electromagnetic induction technologies
  (e.g., magnetic levitation [mag-lev] trains, hydroelectric dams, high-voltage power lines)?
- Determine whether a collision is elastic or inelastic and identify ways of improving the quality of the data collected.
- Assess the safety features in vehicles designed to protect passengers during a collision.

## - Applying and innovating:

Sample opportunities to support student inquiry:

- Co-operatively design a waterwheel to contribute to aeration of a local waterway.
- Why are roads designed with banked curves?
- Apply static equilibrium to design and build a deadfall trap that could be used in a survival situation.
- How did the discovery of the electron and the development of the cathode ray tube (CRT) form the basis of new technologies (e.g., particle accelerators, smartphones)?
- Investigate methods of providing inexpensive and easily available electricity to rural areas or as part of disaster relief.
- Collaboratively generate possible prevention methods for common sports injuries based on an understanding of force, momentum, and impulse.
- How do G-suits save pilots' lives?

## - Communicating:

Sample opportunities to support student inquiry:

- Visually represent an effect of special relativity.
- Model how activities such as kite-boarding, Ultimate Frisbee, or soccer are affected by relative motion.
- Demonstrate the difference between a beam in static, translational, and rotational equilibrium.
- Visually represent how Inukshuks and cairns demonstrate an application of centre of gravity.
- Present the effects of prolonged cell phone use in the most effective way for a specific audience (e.g., peers, parents).
- Present an evidence-based argument for the requirement of wearing boxing gloves during a boxing match.
- place: Place is any environment, locality, or context with which people interact to learn, create memory, reflect on history, connect with culture, and establish identity. The connection between people and place is foundational to First Peoples perspectives.

Content - Elaborations
Grade 12

- relativistic effects: for example, changes in time, length, and mass
- static equilibrium:
- translational: sum of all forces equals zero (vertical and horizontal)
- rotational: sum of all torques equals zero, location of centre of gravity of a uniform body
- uniform circular motion: both horizontal and vertical circles
- changes to apparent weight: vertical and horizontal circles (e.g., on a string, upside down on a roller coaster, on a Ferris wheel, right-side up over a hill, centrifuges)
- First Peoples knowledge and applications of forces in traditional technologies: for example, Salmon wheel, canoe paddle design, deadfall traps
- gravitational field:
- vector field
- interacts with mass through gravitons
- attractive only
- gravitational dynamics and energy relationships: satellite motion, orbit changes, launch velocity, escape velocity
- electric field:
- vector field
- interacts with positive/negative elementary charge
- attractive or repulsive
- single point charges (non-uniform field) and parallel plates (uniform field)
- electrostatic dynamics and energy relationships:
- relationships between force, charge, and distance on a single point charge:
- 1D and 2D with other charges
- in orbits
- between parallel plates
- application of law of conservation of energy and the principle of work and energy (e.g., cathode ray tube, mass spectrometer, particle accelerator)
- magnetic field:
  $-\quad$ vector field
- induced by moving charges
- interacts with polarity (north/south)
- attractive or repulsive
- permanent magnets, straight wires, and solenoids
- magnetic force:
- acting on a moving charge or current carrying wire within a magnetic field
- right-hand rules
- electromagnetic induction:
- Faraday's law
- Lenz's law
- current induced by a change in magnetic flux
- moving a bar, wire, coil, single charge within a changing magnetic field (strength, polarity, or area)
- applications of electromagnetic induction: back electromotive force (EMF), direct current (DC) motors, generators, transformers
- impulse:
- relation to Newton's second law
- in a closed and isolated system
- collisions:
- elastic, inelastic, and completely inelastic
- multiple objects in 1D and 2D
- ballistic pendulums
- graphical methods:
- graphing a linear, exponential, and inverse relationship given a physical model (e.g., electric and gravitational forces and fields versus distance)
- determining the linear regression that results from exponential and inverse relationships
- calculating the slope of a line of best fit, including significant figures and appropriate units
- interpolating and extrapolating data from a constructed graph
- calculating and interpreting area under the curve on a constructed graph (e.g., impulse)
```

</file_contents>

### Textbook contents

<file_contents>
File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/Phys 11 Table of Contents.md

```markdown
## Contents

Preface ..... 1
CHAPTER 1
What is Physics? ..... 5
Introduction ..... 5
1.1 Physics: Definitions and Applications ..... 5
1.2 The Scientific Methods ..... 14
1.3 The Language of Physics: Physical Quantities and Units ..... 18
Key Terms ..... 40
Section Summary ..... 41
Key Equations ..... 41
Chapter Review ..... 41
Test Prep ..... 46
CHAPTER 2
Motion in One Dimension ..... 53
Introduction ..... 53
2.1 Relative Motion, Distance, and Displacement ..... 54
2.2 Speed and Velocity ..... 62
2.3 Position vs. Time Graphs ..... 67
2.4 Velocity vs. Time Graphs ..... 73
Key Terms ..... 81
Section Summary ..... 81
Key Equations ..... 81
Chapter Review ..... 82
Test Prep ..... 86
CHAPTER 3
Acceleration ..... 93
Introduction ..... 93
3.1 Acceleration ..... 93
3.2 Representing Acceleration with Equations and Graphs ..... 99
Key Terms ..... 109
Section Summary ..... 109
Key Equations ..... 109
Chapter Review ..... 109
Test Prep ..... 112
CHAPTER 4
Forces and Newton's Laws of Motion ..... 115
Introduction ..... 115
4.1 Force ..... 116
4.2 Newton's First Law of Motion: Inertia ..... 118
4.3 Newton's Second Law of Motion ..... 122
4.4 Newton's Third Law of Motion ..... 128
Key Terms ..... 135
Section Summary ..... 135
Key Equations ..... 136
Chapter Review ..... 136
Test Prep ..... 139
CHAPTER 5
Motion in Two Dimensions ..... 143
Introduction ..... 143
5.1 Vector Addition and Subtraction: Graphical Methods ..... 144
5.2 Vector Addition and Subtraction: Analytical Methods ..... 153
5.3 Projectile Motion ..... 162
5.4 Inclined Planes ..... 171
5.5 Simple Harmonic Motion ..... 178
Key Terms ..... 185
Section Summary ..... 185
Key Equations ..... 186
Chapter Review ..... 187
Test Prep ..... 191
CHAPTER 6
Circular and Rotational Motion ..... 197
Introduction ..... 197
6.1 Angle of Rotation and Angular Velocity ..... 198
6.2 Uniform Circular Motion ..... 205
6.3 Rotational Motion ..... 212
Key Terms ..... 220
Section Summary ..... 220
Key Equations ..... 221
Chapter Review ..... 221
Test Prep ..... 223
CHAPTER 7
Newton's Law of Gravitation ..... 229
Introduction ..... 229
7.1 Kepler's Laws of Planetary Motion ..... 229
7.2 Newton's Law of Universal Gravitation and Einstein's Theory of General Relativity ..... 237
Key Terms ..... 246
Section Summary ..... 246
Key Equations ..... 246
Chapter Review ..... 246
Test Prep ..... 249
CHAPTER 8
Momentum ..... 253
Introduction ..... 253
8.1 Linear Momentum, Force, and Impulse ..... 254
8.2 Conservation of Momentum ..... 259
8.3 Elastic and Inelastic Collisions ..... 262
Key Terms ..... 272
Section Summary ..... 272
Key Equations ..... 272
Chapter Review ..... 273
Test Prep ..... 275
CHAPTER 9
Work, Energy, and Simple Machines ..... 279
Introduction ..... 279
9.1 Work, Power, and the Work-Energy Theorem ..... 280
9.2 Mechanical Energy and Conservation of Energy ..... 285
9.3 Simple Machines ..... 290
Key Terms ..... 295
Section Summary ..... 295
Key Equations ..... 295
Chapter Review ..... 296
Test Prep ..... 299
CHAPTER 10
Special Relativity ..... 305
Introduction ..... 305
10.1 Postulates of Special Relativity ..... 305
10.2 Consequences of Special Relativity ..... 312
Key Terms ..... 321
Section Summary ..... 321
Key Equations ..... 321
Chapter Review ..... 322
Test Prep ..... 324
CHAPTER 11
Thermal Energy, Heat, and Work ..... 327
Introduction ..... 327
11.1 Temperature and Thermal Energy ..... 327
11.2 Heat, Specific Heat, and Heat Transfer ..... 332
11.3 Phase Change and Latent Heat ..... 340
Key Terms ..... 348
Section Summary ..... 348
Key Equations ..... 349
Chapter Review ..... 349
Test Prep ..... 351
CHAPTER 12
Thermodynamics ..... 355
Introduction ..... 355
12.1 Zeroth Law of Thermodynamics: Thermal Equilibrium ..... 356
12.2 First law of Thermodynamics: Thermal Energy and Work ..... 358
12.3 Second Law of Thermodynamics: Entropy ..... 366
12.4 Applications of Thermodynamics: Heat Engines, Heat Pumps, and Refrigerators ..... 372
Key Terms ..... 378
Section Summary ..... 378
Key Equations ..... 379
Chapter Review ..... 379
Test Prep ..... 383
CHAPTER 13
Waves and Their Properties ..... 389
Introduction ..... 389
13.1 Types of Waves ..... 390
13.2 Wave Properties: Speed, Amplitude, Frequency, and Period ..... 394
13.3 Wave Interaction: Superposition and Interference ..... 400
Key Terms ..... 406
Section Summary ..... 406
Key Equations ..... 407
Chapter Review ..... 407
Test Prep ..... 409
CHAPTER 14
Sound ..... 415
Introduction ..... 415
14.1 Speed of Sound, Frequency, and Wavelength ..... 416
14.2 Sound Intensity and Sound Level ..... 423
14.3 Doppler Effect and Sonic Booms ..... 430
14.4 Sound Interference and Resonance ..... 434
Key Terms ..... 443
Section Summary ..... 443
Key Equations ..... 444
Chapter Review ..... 444
Test Prep ..... 448
CHAPTER 15
Light ..... 455
Introduction ..... 455
15.1 The Electromagnetic Spectrum ..... 455
15.2 The Behavior of Electromagnetic Radiation ..... 463
Key Terms ..... 469
Section Summary ..... 469
Key Equations ..... 469
Chapter Review ..... 469
Test Prep ..... 472
CHAPTER 16
Mirrors and Lenses ..... 477
Introduction ..... 477
16.1 Reflection ..... 478
16.2 Refraction ..... 487
16.3 Lenses ..... 498
Key Terms ..... 513
Section Summary ..... 513
Key Equations ..... 513
Chapter Review ..... 514
Test Prep ..... 517
CHAPTER 17
Diffraction and Interference ..... 523
Introduction ..... 523
17.1 Understanding Diffraction and Interference ..... 523
17.2 Applications of Diffraction, Interference, and Coherence ..... 532
Key Terms ..... 542
Section Summary ..... 542
Key Equations ..... 542
Chapter Review ..... 543
Test Prep ..... 545
CHAPTER 18
Static Electricity ..... 549
Introduction ..... 549
18.1 Electrical Charges, Conservation of Charge, and Transfer of Charge ..... 550
18.2 Coulomb's law ..... 562
18.3 Electric Field ..... 567
18.4 Electric Potential ..... 572
18.5 Capacitors and Dielectrics ..... 580
Key Terms ..... 591
Section Summary ..... 591
Key Equations ..... 592
Chapter Review ..... 592
Test Prep ..... 596
CHAPTER 19
Electrical Circuits ..... 603
Introduction ..... 603
19.1 Ohm's law ..... 604
19.2 Series Circuits ..... 612
19.3 Parallel Circuits ..... 621
19.4 Electric Power ..... 632
Key Terms ..... 638
Section Summary ..... 638
Key Equations ..... 638
Chapter Review ..... 639
Test Prep ..... 643
CHAPTER 20
Magnetism ..... 649
Introduction ..... 649
20.1 Magnetic Fields, Field Lines, and Force ..... 650
20.2 Motors, Generators, and Transformers ..... 665
20.3 Electromagnetic Induction ..... 672
Key Terms ..... 681
Section Summary ..... 681
Key Equations ..... 682
Chapter Review ..... 682
Test Prep ..... 684
CHAPTER 21
The Quantum Nature of Light ..... 691
Introduction ..... 691
21.1 Planck and Quantum Nature of Light ..... 692
21.2 Einstein and the Photoelectric Effect ..... 698
21.3 The Dual Nature of Light ..... 704
Key Terms ..... 711
Section Summary ..... 711
Key Equations ..... 711
Chapter Review ..... 712
Test Prep ..... 715
CHAPTER 22
The Atom ..... 721
Introduction ..... 721
22.1 The Structure of the Atom ..... 721
22.2 Nuclear Forces and Radioactivity ..... 734
22.3 Half Life and Radiometric Dating ..... 743
22.4 Nuclear Fission and Fusion ..... 747
22.5 Medical Applications of Radioactivity: Diagnostic Imaging and Radiation ..... 757
Key Terms ..... 763
Section Summary ..... 763
Key Equations ..... 764
Chapter Review ..... 765
Test Prep ..... 767
CHAPTER 23
Particle Physics ..... 771
Introduction ..... 771
23.1 The Four Fundamental Forces ..... 772
23.2 Quarks ..... 779
23.3 The Unification of Forces ..... 790
Key Terms ..... 796
Section Summary ..... 797
Chapter Review ..... 797
Test Prep ..... 801

Appendix A Reference Tables 807
Index 831
```

</file_contents>

### Physics 11 Presentations

<file_contents>
File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch18-19_slides_circuits-combined.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Electrostatics \& Circuits]{PHYS11 CH18-19: Electrostatics \& Circuits}
\subtitle{From Electric Forces to Current Flow}
\author[Mr. Gullo]{Mr. Gullo}
\date[April 2025]{April 9, 2025}

% Create outline for navigation
\AtBeginSection[]
{
  \begin{frame}
    \frametitle{Outline}
    \tableofcontents[currentsection]
  \end{frame}
}

\begin{document}

% Title slide
\begin{frame}
    \titlepage
\end{frame}

% Outline slide
\begin{frame}
    \frametitle{Outline}
    \tableofcontents
\end{frame}

% Learning objectives slide
\begin{frame}
    \frametitle{Learning Objectives}
    \begin{block}{By the end of this presentation, you will be able to:}
        \begin{itemize}
            \item Apply Coulomb's law to calculate electrostatic forces between charges
            \item Describe electric fields and their relationship to force
            \item Explain electric potential energy and electric potential
            \item Understand how capacitors store energy and the effect of dielectrics
            \item Apply Ohm's law to calculate voltage, current, or resistance
            \item Analyze series and parallel circuit configurations
            \item Calculate electric power in circuit components
        \end{itemize}
    \end{block}
\end{frame}

\section{Electrostatics Fundamentals}

\begin{frame}
    \frametitle{Coulomb's Law}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{Definition}
            Coulomb's law describes the electrostatic force between charged particles.
        \end{block}

        \begin{block}{Mathematical Form}
            \begin{equation}
                F = k\frac{q_1 q_2}{r^2}
            \end{equation}
            where:
            \begin{itemize}
                \item $F$ = electrostatic force (newtons, N)
                \item $k$ = Coulomb constant (\SI{8.99e9}{\newton\meter\squared\per\coulomb\squared})
                \item $q_1, q_2$ = electric charges (coulombs, C)
                \item $r$ = distance between charges (meters, m)
            \end{itemize}
        \end{block}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
            \begin{figure}
                \centering
                \includegraphics[width=0.75\linewidth]{phys11-electrostatics-coulombs-law-diagram.png}
            \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Coulomb's Law - Key Properties}
    \begin{block}{Inverse Square Law}
        The electrostatic force is inversely proportional to the square of the distance between charges.
    \end{block}

    \begin{block}{Force Magnitude}
        \begin{itemize}
            \item Proportional to each charge magnitude
            \item Inversely proportional to distance squared
        \end{itemize}
    \end{block}

    \begin{block}{Force Direction}
        \begin{itemize}
            \item If $F < 0$ (negative result): attractive force
            \item If $F > 0$ (positive result): repulsive force
            \item Like charges repel, unlike charges attract
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Electric Field}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{Definition}
            The electric field defines the force per unit charge in the space around a charge distribution.
        \end{block}

        \begin{block}{Mathematical Form}
            \begin{equation}
                \vec{E} = \frac{\vec{F}}{q}
            \end{equation}

            For a point charge or uniform sphere:
            \begin{equation}
                E = k\frac{q}{r^2}
            \end{equation}
        \end{block}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
            \begin{figure}
                \centering
                \includegraphics[width=0.75\linewidth]{phys11-electrostatics-field-lines-positive-charge.png}
            \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Electric Field Properties}
    \begin{block}{Electric Field Lines}
        \begin{itemize}
            \item Electric field lines never cross each other
            \item More force is applied in regions with many field lines
            \item Field lines start at positive charges and point away
            \item Field lines end at negative charges and point toward them
        \end{itemize}
    \end{block}

    \begin{columns}
        \column{0.5\textwidth}
        \begin{alertblock}{  1}
            \begin{figure}
                \centering
                \includegraphics[width=1\linewidth]{phys11-electrostatics-field-lines-opposite-charges.png}
            \end{figure}
        \end{alertblock}

        \column{0.5\textwidth}
        \begin{alertblock}{  2}
            \begin{figure}
                \centering
                \includegraphics[width=1\linewidth]{phys11-electrostatics-field-lines-like-charges.png}
            \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Electric Potential}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{Electric Potential Energy}
            Similar to gravitational potential energy: the potential that charges have to do work by virtue of their positions relative to each other.
        \end{block}

        \begin{block}{Electric Potential}
            Electric potential is the electric potential energy per unit charge:
            \begin{equation}
                V = \frac{U}{q}
            \end{equation}

            For a point charge:
            \begin{equation}
                V = k\frac{q}{r}
            \end{equation}
        \end{block}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
            \begin{figure}
                \centering
                \includegraphics[width=1\linewidth]{phys11-electrostatics-electric-potential-point-charge.png}
            \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Electric Potential - Key Properties}
    \begin{block}{Measurement}
        \begin{itemize}
            \item Potential is always measured between two points
            \item One point may be at infinity (reference point)
            \item Measured in volts (V)
        \end{itemize}
    \end{block}

    \begin{block}{Charge Movement}
        \begin{itemize}
            \item Positive charges move from high potential to low potential
            \item Negative charges move from low potential to high potential
            \item Charges move spontaneously to minimize potential energy
        \end{itemize}
    \end{block}

    \begin{block}{Relationship to Electric Field}
        \begin{equation}
            \vec{E} = -\nabla V
        \end{equation}
        The electric field points in the direction of decreasing potential.
    \end{block}
\end{frame}

\section{Capacitors and Dielectrics}

\begin{frame}
    \frametitle{Capacitors}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{Definition}
            A capacitor is a device that stores electric charge and energy in an electric field.
        \end{block}

        \begin{block}{Capacitance}
            Capacitance is the ratio of charge to voltage:
            \begin{equation}
                C = \frac{Q}{V}
            \end{equation}

            For a parallel plate capacitor:
            \begin{equation}
                C = \varepsilon_0 \frac{A}{d}
            \end{equation}
            where $A$ is plate area and $d$ is separation distance.
        \end{block}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
            \begin{figure}
                \centering
                \includegraphics[width=1\linewidth]{phys11-electrostatics-parallel-plate-capacitor.png}
            \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Capacitors - Key Properties}
    \begin{block}{Capacitance Properties}
        \begin{itemize}
            \item Depends only on geometry and materials
            \item Does not depend on voltage across the capacitor
            \item Measured in farads (F)
        \end{itemize}
    \end{block}

    \begin{block}{Energy Storage}
        Capacitors store energy in the electric field between plates:
        \begin{equation}
            U = \frac{1}{2}CV^2 = \frac{1}{2}\frac{Q^2}{C} = \frac{1}{2}QV
        \end{equation}
    \end{block}

    \begin{block}{Electric Field in a Capacitor}
        \begin{equation}
            E = \frac{V}{d}
        \end{equation}
        where $d$ is the separation between plates.
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Dielectrics}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{Definition}
            A dielectric material is an insulator that becomes polarized in an electric field.
        \end{block}

        \begin{block}{Effect on Capacitance}
            Inserting a dielectric between capacitor plates increases capacitance:
            \begin{equation}
                C = \kappa \varepsilon_0 \frac{A}{d}
            \end{equation}
            where $\kappa$ is the dielectric constant (relative permittivity).
        \end{block}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
           \begin{figure}
               \centering
               \includegraphics[width=1\linewidth]{phys11-electrostatics-capacitor-with-dielectric.png}
           \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\section{Electric Circuits}

\begin{frame}
    \frametitle{Introduction to Electric Current}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{itemize}
            \item \textbf{Direct Current (DC)}: Constant over time
            \item \textbf{Alternating Current (AC)}: Alternates smoothly back and forth over time
            \item \textbf{Electrical Resistance}: Causes materials to extract work from current flowing through them
        \end{itemize}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
            \begin{figure}
                \centering
                \includegraphics[width=1\linewidth]{phys11-circuits-ac-dc-current-graph.png}
            \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}
\begin{frame}{}
\begin{figure}
                \centering
                \includegraphics[width=1\linewidth]{phys11-circuits-ac-dc-current-graph.png}
            \end{figure}
\end{frame}
\begin{frame}
    \frametitle{Ohm's Law}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{Definition}
            In ohmic materials, voltage drop along a path is proportional to the current that runs through the path.
        \end{block}

        \begin{block}{Mathematical Form}
            \begin{equation}
                V = IR
            \end{equation}
            where:
            \begin{itemize}
                \item $V$ = voltage (volts, V)
                \item $I$ = current (amperes, A)
                \item $R$ = resistance (ohms, $\Omega$)
            \end{itemize}
        \end{block}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
            \begin{figure}
                \centering
                \includegraphics[width=1\linewidth]{phys11-circuits-simple-diagram.png}
            \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Series Circuits}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{Definition}
            Resistors in series are connected head to tail, with the same current flowing through each resistor.
        \end{block}

        \begin{block}{Key Properties}
            \begin{itemize}
                \item The same current flows through all resistors
                \item Voltage drops across each resistor can be different
                \item Voltage is the same at every point in a given wire
            \end{itemize}
        \end{block}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
           \begin{figure}
               \centering
               \includegraphics[width=1\linewidth]{phys11-circuits-series-resistors.png}
           \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Equivalent Resistance in Series}
    \begin{block}{Formula}
        For resistors in series, the total resistance is the sum of the individual resistances:
        \begin{equation}
            R_{\text{total}} = R_1 + R_2 + R_3 + \ldots + R_n
        \end{equation}
    \end{block}

    \begin{block}{Voltage Drops}
        The voltage drops across each resistor follow Ohm's law:
        \begin{equation}
            V_1 = IR_1, \quad V_2 = IR_2, \quad \ldots
        \end{equation}

        The total voltage across the circuit is the sum of the individual voltage drops:
        \begin{equation}
            V_{\text{total}} = V_1 + V_2 + V_3 + \ldots + V_n
        \end{equation}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Parallel Circuits}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{Definition}
            Resistors in parallel are connected across the same two points in a circuit.
        \end{block}

        \begin{block}{Key Properties}
            \begin{itemize}
                \item Same voltage drop occurs across all resistors
                \item Current through each resistor can differ
                \item More paths for current means lower equivalent resistance
            \end{itemize}
        \end{block}

        \column{0.4\textwidth}
        \begin{alertblock}{ }
           \begin{figure}
               \centering
               \includegraphics[width=1\linewidth]{phys11-circuits-parallel-resistors.png}
           \end{figure}
        \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Equivalent Resistance in Parallel}
    \begin{block}{Formula}
        For resistors in parallel, the reciprocal of the total resistance equals the sum of the reciprocals of the individual resistances:
        \begin{equation}
            \frac{1}{R_{\text{total}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots + \frac{1}{R_n}
        \end{equation}
    \end{block}


    \begin{block}{Important Note}
        The equivalent resistance of parallel resistors is always less than the smallest individual resistance.
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Electric Power}
    \begin{block}{Definition}
        Electric power is the rate at which electrical energy is converted to other forms of energy (heat, light, mechanical work, etc.).
    \end{block}

    \begin{block}{Key Concept}
        Electric power is dissipated in the resistances of a circuit. Capacitors do not dissipate electric power.
    \end{block}

    \begin{block}{Power Formula}
        Electric power is proportional to voltage and current:
        \begin{equation}
            P = VI
        \end{equation}
        where:
        \begin{itemize}
            \item $P$ = power (watts, W)
            \item $V$ = voltage (volts, V)
            \item $I$ = current (amperes, A)
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Power Calculations}
    \begin{block}{Using Ohm's Law}
        Substituting $V = IR$ into $P = VI$:
        \begin{equation}
            P = VI = I(IR) = I^2R
        \end{equation}

        Alternatively, substituting $I = \frac{V}{R}$ into $P = VI$:
        \begin{equation}
            P = VI = V\left(\frac{V}{R}\right) = \frac{V^2}{R}
        \end{equation}
    \end{block}

    \begin{block}{Three Forms of Power Equation}
        \begin{equation}
            P = VI \quad \text{or} \quad P = I^2R \quad \text{or} \quad P = \frac{V^2}{R}
        \end{equation}
    \end{block}
\end{frame}

\section{Important Equations}

\begin{frame}
    \frametitle{Important Equations - Electrostatics}
    \begin{block}{Coulomb's Law}
        \begin{equation}
            F = k\frac{q_1 q_2}{r^2}
        \end{equation}
    \end{block}

    \begin{block}{Electric Field}
        \begin{equation}
            E = k\frac{q}{r^2} \quad \text{and} \quad \vec{E} = \frac{\vec{F}}{q}
        \end{equation}
    \end{block}

    \begin{block}{Electric Potential}
        \begin{equation}
            V = k\frac{q}{r} \quad \text{and} \quad V = \frac{U}{q}
        \end{equation}
    \end{block}

    \begin{block}{Capacitance}
        \begin{equation}
            C = \frac{Q}{V} \quad \text{and} \quad C = \kappa\varepsilon_0\frac{A}{d}
        \end{equation}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Important Equations - Circuits}
    \begin{block}{Ohm's Law}
        \begin{equation}
            V = IR
        \end{equation}
    \end{block}

    \begin{block}{Series Circuits}
        \begin{equation}
            R_{\text{total}} = R_1 + R_2 + R_3 + \ldots + R_n
        \end{equation}
    \end{block}

    \begin{block}{Parallel Circuits}
        \begin{equation}
            \frac{1}{R_{\text{total}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots + \frac{1}{R_n}
        \end{equation}
    \end{block}

    \begin{block}{Electric Power}
        \begin{equation}
            P = VI = I^2R = \frac{V^2}{R}
        \end{equation}
    \end{block}
\end{frame}

\section{Examples}

\begin{frame}
    \frametitle{I Do: Coulomb's Law Application}
    \begin{block}{Problem}
        Two point charges, $q_1 = 3 \,\mu\text{C}$ and $q_2 = -2 \,\mu\text{C}$, are separated by a distance of 15 cm. Calculate the electrostatic force between them.
    \end{block}
    \end{frame}

\begin{frame}
    \begin{block}{Solution}
        Using Coulomb's law: $F = k\frac{q_1 q_2}{r^2}$

        Given:
        \begin{itemize}
            \item $q_1 = 3 \times 10^{-6} \,\text{C}$
            \item $q_2 = -2 \times 10^{-6} \,\text{C}$
            \item $r = 0.15 \,\text{m}$
            \item $k = 8.99 \times 10^9 \,\text{N}\cdot\text{m}^2/\text{C}^2$
        \end{itemize}

        Substituting:
        \begin{align}
            F &= (8.99 \times 10^9) \frac{(3 \times 10^{-6})(-2 \times 10^{-6})}{(0.15)^2} \\
            F &= (8.99 \times 10^9) \frac{-6 \times 10^{-12}}{0.0225} \\
            F &= -2.4 \,\text{N}
        \end{align}

        The negative sign indicates an attractive force.
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{We Do: Electric Potential Problem}
    \begin{block}{Problem}
        A point charge of $5 \,\mu\text{C}$ creates an electric potential. Calculate the electric potential at points 10 cm and 20 cm from the charge.
    \end{block}
    \end{frame}

\begin{frame}
    \begin{block}{Solution - Let's solve together}
        Using the formula for electric potential due to a point charge:
        \begin{equation}
            V = k\frac{q}{r}
        \end{equation}

        At $r_1 = 10 \,\text{cm} = 0.1 \,\text{m}$:
        \begin{align}
            V_1 &= k\frac{q}{r_1} \\
            V_1 &= (8.99 \times 10^9) \frac{5 \times 10^{-6}}{0.1} \\
            V_1 &= ?
        \end{align}

        At $r_2 = 20 \,\text{cm} = 0.2 \,\text{m}$:
        \begin{align}
            V_2 &= k\frac{q}{r_2} \\
            V_2 &= (8.99 \times 10^9) \frac{5 \times 10^{-6}}{0.2} = ?
        \end{align}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{I Do: Series Circuit Analysis}
    \begin{block}{Problem}
        Three resistors of 2 $\Omega$, 4 $\Omega$, and 6 $\Omega$ are connected in series with a 12 V battery. Calculate:
        \begin{enumerate}
            \item The total resistance
            \item The current in the circuit
            \item The voltage drop across each resistor
        \end{enumerate}
    \end{block}
    \end{frame}

\begin{frame}
    \begin{block}{Solution}
        \begin{enumerate}
            \item Total resistance:
            \begin{align}
                R_{\text{total}} &= R_1 + R_2 + R_3 \\
                R_{\text{total}} &= 2\,\Omega + 4\,\Omega + 6\,\Omega = 12\,\Omega
            \end{align}

            \item Current (using Ohm's law):
            \begin{align}
                I &= \frac{V}{R_{\text{total}}} = \frac{12\,\text{V}}{12\,\Omega} = 1\,\text{A}
            \end{align}

            \item Voltage drops:
            \begin{align}
                V_1 &= IR_1 = (1\,\text{A})(2\,\Omega) = 2\,\text{V} \\
                V_2 &= IR_2 = (1\,\text{A})(4\,\Omega) = 4\,\text{V} \\
                V_3 &= IR_3 = (1\,\text{A})(6\,\Omega) = 6\,\text{V}
            \end{align}

            Note that $V_1 + V_2 + V_3 = 2\,\text{V} + 4\,\text{V} + 6\,\text{V} = 12\,\text{V}$, which equals the battery voltage.
        \end{enumerate}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{We Do: Parallel Circuit Problem}
    \begin{block}{Problem}
        Three resistors of 3 $\Omega$, 6 $\Omega$, and 9 $\Omega$ are connected in parallel. Calculate:
        \begin{enumerate}
            \item The equivalent resistance
            \item If this circuit is connected to a 12 V battery, find the total current drawn from the battery
        \end{enumerate}
    \end{block}
    \end{frame}

\begin{frame}
    \begin{block}{Solution - Let's solve together}
        \begin{enumerate}
            \item Equivalent resistance:
            \begin{align}
                \frac{1}{R_{\text{eq}}} &= \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} \\
                \frac{1}{R_{\text{eq}}} &= \frac{1}{3\,\Omega} + \frac{1}{6\,\Omega} + \frac{1}{9\,\Omega} \\
                \frac{1}{R_{\text{eq}}} &= \frac{3 + 1.5 + 1}{9\,\Omega} = \frac{5.5}{9\,\Omega} \\
                R_{\text{eq}} &= \frac{9\,\Omega}{5.5} = ? \,\Omega
            \end{align}

            \item Total current:
            \begin{align}
                I_{\text{total}} &= \frac{V}{R_{\text{eq}}} = \frac{12\,\text{V}}{R_{\text{eq}}} = ?
            \end{align}
        \end{enumerate}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{You Do: Combined Problem}
    \begin{block}{Problem}
        A 12 V battery is connected to a parallel plate capacitor with a separation of 2 mm. The capacitor has a capacitance of 5 $\mu$F.
        \begin{enumerate}
            \item Calculate the electric field between the plates
            \item Calculate the electric energy stored in the capacitor
            \item If a dielectric with $\kappa = 4$ is inserted between the plates, what is the new capacitance?
            \item Calculate the capacitor charge before and after inserting the dielectric
        \end{enumerate}
    \end{block}

    \begin{alertblock}{Hints}
        \begin{itemize}
            \item Electric field in a parallel plate capacitor: $E = \frac{V}{d}$
            \item Energy stored in a capacitor: $U = \frac{1}{2}CV^2$
            \item Capacitance with dielectric: $C = \kappa C_0$
            \item Charge on a capacitor: $Q = CV$
        \end{itemize}
    \end{alertblock}
\end{frame}

\section{Summary}

\begin{frame}
    \frametitle{Summary - Electrostatics}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{block}{Coulomb's Law}
            \begin{itemize}
                \item Inverse square law
                \item $F = k\frac{q_1 q_2}{r^2}$
                \item Like charges repel, unlike attract
            \end{itemize}
        \end{block}

        \begin{block}{Electric Field}
            \begin{itemize}
                \item Force per unit charge
                \item $E = k\frac{q}{r^2}$
                \item Field lines show direction of force
            \end{itemize}
        \end{block}

        \column{0.5\textwidth}
        \begin{block}{Electric Potential}
            \begin{itemize}
                \item Potential energy per unit charge
                \item $V = k\frac{q}{r}$
                \item Charges move to minimize potential energy
            \end{itemize}
        \end{block}

        \begin{block}{Capacitors}
            \begin{itemize}
                \item Store energy in electric field
                \item $C = \frac{Q}{V}$
                \item Dielectrics increase capacitance
            \end{itemize}
        \end{block}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Summary - Electric Circuits}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{block}{Ohm's Law}
            \begin{itemize}
                \item $V = IR$
                \item Direct vs. alternating current
                \item Ohmic materials
            \end{itemize}
        \end{block}

        \begin{block}{Series Circuits}
            \begin{itemize}
                \item Same current through all resistors
                \item $R_{\text{total}} = R_1 + R_2 + \ldots$
                \item Voltage drops can differ
            \end{itemize}
        \end{block}

        \column{0.5\textwidth}
        \begin{block}{Parallel Circuits}
            \begin{itemize}
                \item Same voltage across all resistors
                \item $\frac{1}{R_{\text{total}}} = \frac{1}{R_1} + \frac{1}{R_2} + \ldots$
                \item Currents can differ
            \end{itemize}
        \end{block}

        \begin{block}{Electric Power}
            \begin{itemize}
                \item $P = VI = I^2R = \frac{V^2}{R}$
                \item Power dissipated in resistances
                \item Measured in watts (W)
            \end{itemize}
        \end{block}
    \end{columns}
\end{frame}



\begin{frame}
    \frametitle{Thank You!}
    \begin{center}
        \Large Any questions?

        \vspace{1cm}

        \normalsize For additional practice problems, refer to your textbook Chapters 18-19
    \end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch02_Kinematics-One-Dimension.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../latex-beamer/shared/templates/ds9_theme}


% Title page configuration
\title[Short Title]{PHYS11 CH:2.1-2.4 Kinematics in One Dimension}
\subtitle{Motion, Speed, Velocity, and Graphs}
\author[Mr. Gullo]{Mr. Gullo}
\date[Sep 13, 2025]{September 13, 2025}

\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Learning Objectives}
\framesubtitle{Sections 2.1-2.4}
\begin{block}{By the end of this lesson, you will be able to:}
    \begin{itemize}
        \item \textbf{2.1:} Describe motion in different reference frames, define distance and displacement, and solve problems involving both. \pause
        \item \textbf{2.2:} Calculate the average speed of an object and relate displacement to average velocity. \pause
        \item \textbf{2.3:} Explain the meaning of slope in position vs. time graphs and solve problems using them. \pause
        \item \textbf{2.4:} Explain the meaning of slope and area in velocity vs. time graphs and solve problems using them.
    \end{itemize}
\end{block}
\end{frame}

\section{2.1 Relative Motion, Distance, and Displacement}

\begin{frame}
\frametitle{Key Concepts: Motion is Relative}
\begin{itemize}
    \item \alert{Kinematics}: The study of motion without considering its causes. \pause
    \item \alert{Position}: An object's location at a particular time. \pause
    \item To describe position, you need a \alert{reference frame}: a coordinate system from which positions are measured. \pause
    \item \textbf{Example}: A person on a train is stationary relative to the train, but moving relative to the ground. There is no single "correct" reference frame.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Key Concepts: Distance vs. Displacement}
\begin{columns}[T]
    \column{0.48\textwidth}
    \begin{block}{Distance}
        \begin{itemize}
            \item The total length of the path traveled.
            \item A \alert{scalar} quantity: it has magnitude (size) but \textbf{no direction}.
            \item Example: "I walked 10 meters."
        \end{itemize}
    \end{block}
    \pause
    \column{0.48\textwidth}
    \begin{block}{Displacement ($\Delta \vec{d}$)}
        \begin{itemize}
            \item The change in position from start to end.
            \item A \alert{vector} quantity: it has both \textbf{magnitude and direction}.
            \item Example: "I walked 10 meters \alert{east}."
            \item Formula: $\Delta \vec{d} = \vec{d}_{final} - \vec{d}_{initial}$
        \end{itemize}
    \end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Context}
\framesubtitle{Distance vs. Displacement Example}
\begin{itemize}
    \item Imagine driving from your home to school, a trip of 5 km.
    \pause
    \item After school, your parent drives back home along the same route.
    \pause
    \item We will visualize the \alert{total distance} traveled and the \alert{total displacement} for the entire round trip.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Round Trip}
\begin{alertblock}{[Diagram based on Figure 2.6]}
A diagram showing a car starting at "Home", driving 5 km to "School", and then returning to "Home".
\end{alertblock}
\pause
\begin{itemize}
    \item \textbf{Distance Traveled}:
    \begin{itemize}
        \item To school: 5 km
        \item Back home: 5 km
        \item Total distance = $5 \text{ km} + 5 \text{ km} = \alert{10 \text{ km}}$
    \end{itemize}
    \pause
    \item \textbf{Total Displacement}:
    \begin{itemize}
        \item Initial Position ($d_o$): Home
        \item Final Position ($d_f$): Home
        \item $\Delta d = d_f - d_o = \text{Home} - \text{Home} = \alert{0 \text{ km}}$
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{I Do: Calculating Distance and Displacement}
\framesubtitle{Problem based on Ch. 2, Worked Example p. 14}
\begin{block}{Problem}
A cyclist rides 3 km west and then turns around and rides 2 km east.
\begin{enumerate}
    \item What is her displacement?
    \item What distance does she ride?
\end{enumerate}
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
    \item Let East be the positive (+) direction.
    \item Displacement 1 ($\Delta \vec{d}_1$): 3 km west = -3 km
    \item Displacement 2 ($\Delta \vec{d}_2$): 2 km east = +2 km
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
    \item Total Displacement ($\Delta \vec{d}_{total}$) = ?
    \item Total Distance ($d_{total}$) = ?
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I Do: Calculating Distance and Displacement - Solution}
\begin{block}{E - Equations}
\begin{itemize}
    \item $\Delta \vec{d}_{total} = \Delta \vec{d}_1 + \Delta \vec{d}_2$
    \item $d_{total} = |\Delta \vec{d}_1| + |\Delta \vec{d}_2|$ (sum of magnitudes)
\end{itemize}
\end{block}
\pause
\begin{columns}
\column{0.48\textwidth}
\begin{block}{S - Substitute \& Solve (Displacement)}
\begin{itemize}
    \item $\Delta \vec{d}_{total} = (-3 \text{ km}) + (+2 \text{ km})$
    \item $\Delta \vec{d}_{total} = -1 \text{ km}$
    \item \boxed{\Delta \vec{d}_{total} = 1 \text{ km west}}
\end{itemize}
\end{block}
\column{0.48\textwidth}
\begin{block}{S - Substitute \& Solve (Distance)}
\begin{itemize}
    \item $d_{total} = |-3 \text{ km}| + |+2 \text{ km}|$
    \item $d_{total} = 3 \text{ km} + 2 \text{ km}$
    \item \boxed{d_{total} = 5 \text{ km}}
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{We Do: Practice Together}
\framesubtitle{Problem based on Ch. 2, Practice Problem 1, p. 15}
\begin{block}{Problem}
On an axis where right is positive, a student walks 32 m to the right and then 17 m to the left. What are the displacement and distance?
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
    \item Direction: Right is positive (+)
    \item $\Delta \vec{d}_1 = \alert{+32 \text{ m}}$
    \item $\Delta \vec{d}_2 = \alert{-17 \text{ m}}$
\end{itemize}
\end{block}
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
    \item $\Delta \vec{d}_{total} = ?$
    \item $d_{total} = ?$
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{alertblock}{Your turn!}
Now, let's substitute these into the equations and solve. What do we get?
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{You Do: Independent Practice}
\framesubtitle{Problem based on Ch. 2, Practice Problem 2, p. 15}
\begin{block}{Problem}
Tiana jogs 1.5 km along a straight path (let's call this the positive direction). She then turns and jogs 2.4 km in the opposite direction. Finally, she turns back and jogs 0.7 km in the original direction.
\newline\newline
What are her final displacement and total distance jogged? Use the GUESS method.
\end{block}
\end{frame}

\section{2.2 Speed and Velocity}

\begin{frame}
\frametitle{Key Concepts: Speed vs. Velocity}
\begin{columns}[T]
    \column{0.48\textwidth}
    \begin{block}{Average Speed ($v_{avg}$)}
        \begin{itemize}
            \item Rate of motion.
            \item A \alert{scalar} quantity (magnitude only).
            \item Tells you how fast, but not in what direction.
            \item $v_{avg} = \frac{\text{total distance}}{\text{elapsed time}}$
        \end{itemize}
    \end{block}
    \pause
    \column{0.48\textwidth}
    \begin{block}{Average Velocity ($\vec{v}_{avg}$)}
        \begin{itemize}
            \item Rate of change of position.
            \item A \alert{vector} quantity (magnitude and direction).
            \item Tells you how fast \textbf{and} in what direction.
            \item $\vec{v}_{avg} = \frac{\text{displacement}}{\text{elapsed time}} = \frac{\Delta \vec{d}}{\Delta t}$
        \end{itemize}
    \end{block}
\end{columns}
\note{Emphasize that a car's speedometer shows instantaneous speed, not velocity.}
\end{frame}

\begin{frame}
\frametitle{Essential Equations: Speed and Velocity}
\begin{block}{Average Speed}
\[ v_{avg} = \frac{d}{\Delta t} \]
\begin{itemize}
    \item $d$ is the total distance traveled (a scalar).
    \item $\Delta t$ is the change in time ($t_f - t_o$).
    \item Units: meters per second (m/s), kilometers per hour (km/h).
\end{itemize}
\end{block}
\pause
\begin{block}{Average Velocity}
\[ \vec{v}_{avg} = \frac{\Delta \vec{d}}{\Delta t} = \frac{\vec{d}_f - \vec{d}_o}{t_f - t_o} \]
\begin{itemize}
    \item $\Delta \vec{d}$ is the displacement (a vector).
    \item Direction of velocity is the same as the direction of displacement.
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{I Do: Solving for Displacement}
\framesubtitle{Problem based on Ch. 2, Worked Example p. 26}
\begin{block}{Problem}
Layla jogs with an average velocity of 2.4 m/s east. What is her displacement after 46 seconds?
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
    \item $\vec{v}_{avg} = 2.4$ m/s east
    \item $\Delta t = 46$ s
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
    \item $\Delta \vec{d} = ?$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I Do: Solving for Displacement - Equation and Solution}
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{E - Equation}
\begin{itemize}
    \item Start with: $\vec{v}_{avg} = \frac{\Delta \vec{d}}{\Delta t}$
    \item Rearrange for the unknown:
    \item $\Delta t \cdot \vec{v}_{avg} = \frac{\Delta \vec{d}}{\Delta t} \cdot \Delta t$
    \item \alert{$\Delta \vec{d} = \vec{v}_{avg} \cdot \Delta t$}
\end{itemize}
\end{block}
\column{0.48\textwidth}
\pause
\begin{block}{S - Substitute}
\begin{itemize}
    \item $\Delta \vec{d} = (2.4 \, \text{m/s east}) \cdot (46 \, \text{s})$
\end{itemize}
\end{block}
\pause
\begin{block}{S - Solve}
\begin{itemize}
    \item $\Delta \vec{d} = 110.4 \, \text{m east}$
    \item Apply sig figs (2 s.f.):
    \item \boxed{\Delta \vec{d} = 1.1 \times 10^2 \text{ m east}}
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{We Do: Calculating Average Speed}
\framesubtitle{Problem based on Ch. 2, Practice Problem 9, p. 23}
\begin{block}{Problem}
A pitcher throws a baseball from the pitcher's mound to home plate in 0.46 s. The distance is 18.4 m. What was the average speed of the baseball?
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
    \item $d = \alert{18.4 \text{ m}}$
    \item $\Delta t = \alert{0.46 \text{ s}}$
\end{itemize}
\end{block}
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
    \item $v_{avg} = ?$
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{alertblock}{Your turn!}
Which equation do we need? Is any rearrangement required? Let's solve it.
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{You Do: Independent Practice}
\framesubtitle{Problem based on Ch. 2, Practice Problem 11, p. 27}
\begin{block}{Problem}
A trucker drives along a straight highway for 0.25 h with a displacement of 16 km south. What is the trucker's average velocity?
\newline\newline
Use the GUESS method to find the solution. Be mindful of your units!
\end{block}
\end{frame}

\section{2.3 Position vs. Time Graphs}

\begin{frame}
\frametitle{Key Concepts: Position vs. Time Graphs}
\begin{itemize}
    \item A graph of position (y-axis) versus time (x-axis) provides a visual description of motion.
    \pause
    \item The \alert{slope} of the line is a key piece of information.
    \[ \text{slope} = \frac{\text{rise}}{\text{run}} = \frac{\Delta \text{position}}{\Delta \text{time}} = \frac{\Delta d}{\Delta t} \]
    \pause
    \item Since $\vec{v}_{avg} = \frac{\Delta \vec{d}}{\Delta t}$, the \textbf{slope of a position-time graph is the velocity}.
    \pause
    \item The \alert{y-intercept} of the graph is the object's initial position ($d_o$).
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Interpreting Position-Time Graphs}
\begin{itemize}
    \item \textbf{Straight Line}: The slope is constant, which means the \alert{velocity is constant}.
    \pause
    \item \textbf{Positive Slope}: Object is moving in the positive direction.
    \pause
    \item \textbf{Negative Slope}: Object is moving in the negative direction.
    \pause
    \item \textbf{Zero Slope (Horizontal Line)}: The position is not changing. The object is \alert{at rest} ($v=0$).
    \pause
    \item \textbf{Curved Line}: The slope is changing, which means the \alert{velocity is changing} (the object is accelerating).
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Context}
\framesubtitle{Graphing a Jet Car}
\begin{itemize}
    \item Let's analyze the motion of a jet-powered car.
    \pause
    \item First, we'll look at a simplified case where its velocity is constant. The position-time graph will be a straight line.
    \pause
    \item Then, we will look at the car as it is speeding up. The position-time graph for this motion will be a curve. We will see how to find its velocity at a specific instant.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Constant Velocity}
\begin{alertblock}{[Graph based on Figure 2.12]}
A position vs. time graph for a jet car.
\begin{itemize}
    \item The y-axis is Position (m), x-axis is Time (s).
    \item The graph is a straight line with a positive slope.
    \item The line starts at a y-intercept of $d_o = 400$ m.
    \item The slope is labeled $\bar{v} = \Delta d / \Delta t$.
\end{itemize}
\end{alertblock}
\pause
\textbf{Interpretation}: The car is moving at a constant positive velocity. Its initial position was 400 m from the origin.
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Changing Velocity}
\begin{alertblock}{[Graph based on Figure 2.13]}
A position vs. time graph for a jet car that is speeding up.
\begin{itemize}
    \item The graph is a curve that gets progressively steeper.
    \item Two points, P and Q, are marked on the curve.
    \item A tangent line is drawn at point P, showing a shallow slope.
    \item A tangent line is drawn at point Q, showing a much steeper slope.
\end{itemize}
\end{alertblock}
\pause
\textbf{Interpretation}: The slope is increasing, so the velocity is increasing. To find the \alert{instantaneous velocity} at any point, we find the slope of the line tangent to the curve at that point.
\end{frame}

\begin{frame}
\frametitle{I Do: Calculating Velocity from a Graph}
\framesubtitle{Problem based on Ch. 2, Worked Example p. 36}
\begin{block}{Problem}
Find the average velocity of the car whose position is graphed in Figure 2.12 (the constant velocity graph).
\end{block}
\pause
\begin{block}{Strategy}
Velocity is the slope of the position-time graph. We can pick any two points on the line to calculate the slope.
\end{block}
\pause
\begin{block}{Solution}
\begin{itemize}
    \item Choose two points from the graph:
    \begin{itemize}
        \item Point 1: ($t_i = 0.50$ s, $d_i = 525$ m)
        \item Point 2: ($t_f = 6.4$ s, $d_f = 2000$ m)
    \end{itemize}
    \item Calculate the slope:
    \[ \vec{v}_{avg} = \frac{\Delta d}{\Delta t} = \frac{d_f - d_i}{t_f - t_i} \]
    \[ \vec{v}_{avg} = \frac{2000 \, \text{m} - 525 \, \text{m}}{6.4 \, \text{s} - 0.50 \, \text{s}} = \frac{1475 \, \text{m}}{5.9 \, \text{s}} \]
    \item \boxed{\vec{v}_{avg} \approx 250 \text{ m/s}}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{We Do: Instantaneous Velocity}
\framesubtitle{Problem based on Ch. 2, Worked Example p. 38}
\begin{block}{Problem}
Calculate the instantaneous velocity of the jet car at t = 25 s from the curved graph in Figure 2.13.
\end{block}
\pause
\begin{block}{Strategy}
The instantaneous velocity is the slope of the tangent line at that point. The book provides the endpoints for the tangent line at t=25s.
\end{block}
\pause
\begin{block}{Solution}
\begin{itemize}
    \item The tangent line at t=25s passes through:
    \begin{itemize}
        \item Point 1: ($t_i = 19$ s, $d_i = 1300$ m)
        \item Point 2: ($t_f = 32$ s, $d_f = 3120$ m)
    \end{itemize}
    \item \alert{Let's calculate the slope together:}
    \[ \vec{v}_{inst} = \frac{\Delta d}{\Delta t} = \frac{3120 \, \text{m} - 1300 \, \text{m}}{32 \, \text{s} - 19 \, \text{s}} = ? \]
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{You Do: Independent Practice}
\framesubtitle{Problem based on Ch. 2, Practice Problem 16, p. 39}
\begin{block}{Problem}
Calculate the average velocity of the object shown in the graph below over the whole time interval (0 s to 80 s).
\end{block}
\begin{alertblock}{[Graph from p. 39]}
A position-time graph.
\begin{itemize}
    \item Starts at position 5 m at t=0 s.
    \item Ends at position 25 m at t=80 s.
    \item The line is composed of several straight segments with different slopes.
\end{itemize}
\end{alertblock}
\note{Hint: For average velocity, you only need the start and end points!}
\end{frame}

\section{2.4 Velocity vs. Time Graphs}

\begin{frame}
\frametitle{Key Concepts: Velocity vs. Time Graphs}
A graph of velocity (y-axis) versus time (x-axis) also tells a story.

\begin{columns}[T]
    \column{0.48\textwidth}
    \begin{block}{Slope = Acceleration}
        \begin{itemize}
            \item The slope of a v-t graph is the rate of change of velocity.
            \[ \text{slope} = \frac{\text{rise}}{\text{run}} = \frac{\Delta v}{\Delta t} \]
            \item This is the definition of \alert{acceleration ($a$)}.
            \item A positive slope means speeding up in the positive direction.
            \item A negative slope means slowing down (or speeding up in the negative direction).
            \item A zero slope means \alert{constant velocity}.
        \end{itemize}
    \end{block}
    \pause
    \column{0.48\textwidth}
    \begin{block}{Area = Displacement}
        \begin{itemize}
            \item The area under the v-t graph represents displacement.
            \item Think of `Area = height × width`.
            \item For a v-t graph, this is `v × t`.
            \item Since $d = v \cdot t$, the \alert{area is the displacement ($\Delta d$)}.
            \item For sloped lines, this area might be a triangle or trapezoid.
        \end{itemize}
    \end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: V-T Graph}
\begin{alertblock}{[Graph based on Figure 2.18]}
A velocity vs. time graph for a jet car speeding up.
\begin{itemize}
    \item The y-axis is Velocity (m/s), x-axis is Time (s).
    \item The graph is a straight line with a constant positive slope, starting from a positive y-intercept.
    \item The slope is labeled $a = \Delta v / \Delta t$.
\end{itemize}
\end{alertblock}
\pause
\begin{itemize}
    \item \textbf{To find acceleration}: Calculate the \alert{slope} of the line.
    \item \textbf{To find displacement}: Calculate the \alert{area under the line} (a trapezoid in this case).
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{I Do: Analyzing a V-T Graph}
\framesubtitle{Problem based on Ch. 2, Worked Example p. 46}
\begin{block}{Problem}
Using the v-t graph (Fig 2.18), find (a) the displacement and (b) the acceleration of the jet car.
\end{block}
\pause
\begin{block}{Solution (a): Displacement = Area}
\begin{itemize}
    \item The shape under the graph from t=0 to t=30s is a trapezoid.
    \item Area = $\frac{1}{2}(b_1 + b_2)h$. Here, the "height" is along the time axis.
    \item $b_1$ (initial velocity) $\approx 20$ m/s, $b_2$ (final velocity) $\approx 160$ m/s, $h$ (time) = 30 s.
    \item Area = $\frac{1}{2}(20 + 160)\text{m/s} \cdot 30\text{s} = \frac{1}{2}(180)\text{m/s} \cdot 30\text{s} = \alert{2700 \text{ m}}$.
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\begin{block}{Solution (b): Acceleration = Slope}
\begin{itemize}
    \item Pick two points: (5 s, 40 m/s) and (25 s, 140 m/s).
    \[ a = \frac{\Delta v}{\Delta t} = \frac{140 - 40 \, \text{m/s}}{25 - 5 \, \text{s}} = \frac{100 \, \text{m/s}}{20 \, \text{s}} = \alert{5 \, \text{m/s}^2} \]
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{We Do: Reading a V-T Graph}
\framesubtitle{Problem based on Ch. 2, Practice Problem 20, p. 50}
\begin{block}{Problem}
Consider the velocity vs. time graph of a person in an elevator. What is the instantaneous velocity at t = 10 s and t = 23 s?
\end{block}
\begin{alertblock}{[Graph from p. 50]}
A v-t graph showing three segments:
\begin{itemize}
    \item From 0 to 3s: velocity increases linearly to 3 m/s.
    \item From 3 to 18s: velocity is constant at 3 m/s (horizontal line).
    \item From 18 to 23s: velocity decreases linearly to 0 m/s.
\end{itemize}
\end{alertblock}
\pause
\begin{itemize}
    \item How do we find instantaneous velocity from a v-t graph? \alert{We just read the value off the y-axis!}
    \item At t = 10 s, the velocity is...?
    \item At t = 23 s, the velocity is...?
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{You Do: Independent Practice}
\framesubtitle{Problem based on Ch. 2, Practice Problem 21, p. 51}
\begin{block}{Problem}
Using the same elevator graph, calculate the net displacement and the average velocity for the entire time interval shown (0 to 23 s).
\end{block}
\begin{alertblock}{[Graph from p. 50]}
A v-t graph showing three segments for an elevator ride.
\end{alertblock}
\begin{itemize}
    \item \textbf{Hint for Displacement}: Find the total area under the graph. Break the trapezoid into a triangle, a rectangle, and another triangle.
    \item \textbf{Hint for Avg. Velocity}: Once you have the total displacement, use $\vec{v}_{avg} = \frac{\Delta \vec{d}}{\Delta t}$.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Summary}
\begin{block}{Key Takeaways}
    \begin{itemize}
        \item \textbf{Scalars} have magnitude only (distance, speed). \textbf{Vectors} have magnitude and direction (displacement, velocity). \pause
        \item An object's motion depends on the \textbf{reference frame}. \pause
        \item \textbf{Position vs. Time Graphs}:
        \begin{itemize}
            \item \alert{Slope} is \textbf{velocity}.
        \end{itemize} \pause
        \item \textbf{Velocity vs. Time Graphs}:
        \begin{itemize}
            \item \alert{Slope} is \textbf{acceleration}.
            \item \alert{Area under the graph} is \textbf{displacement}.
        \end{itemize}
    \end{itemize}
\end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch18_slides_current-electricity.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Electric Forces \& Fields]{PHYS11 CH18: Electrostatics}
\subtitle{Charges, Fields, Potential, and Capacitors}
\author[Mr. Gullo]{Mr. Gullo}
\date[May 2025]{May, 2025}

% Define sections for outline
\AtBeginSection[]
{
  \begin{frame}
    \frametitle{Outline}
    \tableofcontents[currentsection]
  \end{frame}
}

\begin{document}

% Title page
\begin{frame}
    \titlepage
\end{frame}

% Outline
\begin{frame}
    \frametitle{Presentation Outline}
    \tableofcontents
\end{frame}

\section{Introduction}

% Learning Objectives
\begin{frame}
    \frametitle{Learning Objectives}
    By the end of this presentation, you will be able to:
    \begin{itemize}
        \item Describe the nature of electric charge and its conservation
        \item Apply Coulomb's law to calculate forces between charges
        \item Define and calculate electric fields around charge distributions
        \item Understand electric potential and potential energy concepts
        \item Explain how capacitors work and calculate their capacitance
        \item Solve problems involving electric forces, fields, potential, and capacitors
    \end{itemize}
\end{frame}

\section{Electrical Charges}

% Electrical Charges
\begin{frame}
    \frametitle{Electrical Charges}
    \begin{block}{Key Concepts}
        \begin{itemize}
                    \item Two varieties: \textbf{positive} and \textbf{negative}
            \item Like charges \textbf{repel}, opposite charges \textbf{attract}
        \end{itemize}
    \end{block}


        \begin{figure}
            \centering
            \includegraphics[width=1\linewidth]{phys11-electrostatics-charge-attraction-repulsion.png}
        \end{figure}


    \begin{block}{Conductors vs. Insulators}
        \begin{itemize}
            \item \textbf{Conductors}: Charges move easily \textbf{Insulators}: Charges cannot move easily
        \end{itemize}
    \end{block}
\end{frame}

% Charge Transfer Methods
\begin{frame}
    \frametitle{Transfer of Charge}
    Three ways to charge objects:
    \begin{enumerate}
        \item \textbf{Charging by contact}
            \begin{itemize}
                \item Direct physical contact between objects
                \item Charges transfer from one object to another
            \end{itemize}
        \item \textbf{Charging by conduction}
            \begin{itemize}
                \item Charges flow through conducting path
            \end{itemize}
        \item \textbf{Charging by induction}
            \begin{itemize}
                \item No contact required
                \item Charge separation due to electric field
            \end{itemize}
    \end{enumerate}


       \begin{figure}
           \centering
           \includegraphics[width=1\linewidth]{phys11-electrostatics-charging-methods.png}
       \end{figure}

\end{frame}

% Polarization
\begin{frame}
    \frametitle{Polarization}
    \begin{block}{Polarized Objects}
        \begin{itemize}
            \item A polarized object may be electrically neutral overall
            \item But its charge is \textbf{unbalanced}:
                \begin{itemize}
                    \item One side has excess \textbf{negative} charge
                    \item The other side has equal magnitude of excess \textbf{positive} charge
                \end{itemize}
        \end{itemize}
    \end{block}


        \begin{figure}
            \centering
            \includegraphics[width=0.75\linewidth]{phys11-electrostatics-polarization.png}
        \end{figure}

\end{frame}

\section{Coulomb's Law}

% Coulomb's Law
\begin{frame}
    \frametitle{Coulomb's Law}
    \begin{block}{Definition}
        Coulomb's law describes the electrostatic force between charged particles:
        \begin{equation}
            \vec{F} = \frac{kq_1q_2}{r^2}\hat{r}
        \end{equation}
        where:
        \begin{itemize}
            \item $k = 9 \times 10^9 \, \text{N} \cdot \text{m}^2/\text{C}^2$ (Coulomb constant)
            \item $q_1, q_2$ are the charges
            \item $r$ is the distance between charges
            \item $\hat{r}$ is the unit vector pointing from $q_1$ to $q_2$
        \end{itemize}
    \end{block}
\end{frame}

% Coulomb's Law Properties
\begin{frame}
    \frametitle{Properties of Coulomb's Law}
    \begin{itemize}
        \item \textbf{Inverse square law}: Force $\propto \frac{1}{r^2}$
        \item Force is \textbf{proportional} to the product of charges
        \item Force interpretation:
            \begin{itemize}
                \item $F < 0$ → \textbf{attractive} force
                \item $F > 0$ → \textbf{repulsive} force
            \end{itemize}
        \item Vector nature: Forces act along the line joining the charges
    \end{itemize}


       \begin{figure}
           \centering
           \includegraphics[width=1\linewidth]{phys11-electrostatics-coulomb-force-types.png}
       \end{figure}

\end{frame}

\section{Electric Field}

% Electric Field Concept
\begin{frame}
    \frametitle{Electric Field Concept}
    \begin{block}{Definition}
        The electric field defines the force per unit charge in the space around a charge distribution:
        \begin{equation}
            \vec{E} = \frac{\vec{F}}{q_{\text{test}}}
        \end{equation}
    \end{block}

    \begin{block}{Point Charge Electric Field}
        For a point charge or sphere of uniform charge:
        \begin{equation}
            E = \frac{kq}{r^2}
        \end{equation}
    \end{block}
    \end{frame}

\begin{frame}

        \begin{figure}
            \centering
            \includegraphics[width=0.8\linewidth]{phys11-electrostatics-electric-field-point-charge.png}
        \end{figure}

\end{frame}

\begin{frame}
    \frametitle{Electric Field Lines}
    Properties of electric field lines:
    \begin{itemize}
        \item Electric field lines \textbf{never cross} each other
        \item More field lines indicate a \textbf{stronger field}
        \item Lines \textbf{start at positive charges} and point away
        \item Lines \textbf{end at negative charges} and point toward them
        \item In free space, field lines extend to infinity
    \end{itemize}


        \begin{figure}
            \centering
            \includegraphics[width=0.5\linewidth]{phys11-electrostatics-field-lines-positive-negative-charges.png}
        \end{figure}

\end{frame}

\section{Electric Potential}

% Electric Potential Energy
\begin{frame}
    \frametitle{Electric Potential Energy}
    \begin{block}{Definition}
        Electric potential energy is the potential that charges have to do work by virtue of their positions relative to each other.
    \end{block}

    \begin{block}{Mathematical Expression}
        For a charge $q$ in the presence of a point charge $Q$:
        \begin{equation}
            U_E = \frac{kqQ}{r}
        \end{equation}

        Change in potential energy in constant field:
        \begin{equation}
            \Delta U_E = -qE(r_f - r_i)
        \end{equation}
    \end{block}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys11-energy-gravitational-vs-electric-potential.png}
\end{figure}
\end{frame}

% Electric Potential
\begin{frame}
    \frametitle{Electric Potential}
    \begin{block}{Definition}
        Electric potential is the electric potential energy per unit charge:
        \begin{equation}
            V = \frac{U_E}{q}
        \end{equation}
    \end{block}

    \begin{block}{Mathematical Expression}
        For a point charge $Q$:
        \begin{equation}
            V = \frac{kQ}{r}
        \end{equation}

        Change in potential in constant field:
        \begin{equation}
            \Delta V = -E(r_f - r_i)
        \end{equation}
    \end{block}
    \end{frame}

\begin{frame}

   \begin{figure}
       \centering
       \includegraphics[width=1\linewidth]{phys11-electrostatics-equipotential-field-lines.png}
   \end{figure}

\end{frame}

% Movement of Charges in Potential
\begin{frame}
    \frametitle{Movement of Charges in Potential}
    \begin{block}{Key Principles}
        \begin{itemize}
            \item Potential is always measured between two points
            \item One reference point may be at infinity ($V = 0$)
            \item Charges move spontaneously to minimize potential energy:
                \begin{itemize}
                    \item \textbf{Positive charges} move from \textbf{high} to \textbf{low} potential
                    \item \textbf{Negative charges} move from \textbf{low} to \textbf{high} potential
                \end{itemize}
        \end{itemize}
    \end{block}
    \end{frame}

\begin{frame}

       \begin{figure}
           \centering
           \includegraphics[width=0.6\linewidth]{phys11-electrostatics-charge-movement-in-potential.png}
       \end{figure}

\end{frame}

\section{Capacitors and Dielectrics}

% Capacitors
\begin{frame}
    \frametitle{Capacitors}
    \begin{block}{Definition}
        A capacitor is a device that stores electric charge and energy in the electric field between its plates.
    \end{block}

    \begin{block}{Capacitance}
        Capacitance is the ratio of charge to potential difference:
        \begin{equation}
            C = \frac{Q}{V}
        \end{equation}

        Capacitance depends only on:
        \begin{itemize}
            \item Geometry of the capacitor
            \item Materials from which it is made
            \item \textbf{Does not} depend on the voltage
        \end{itemize}
    \end{block}
    \end{frame}

\begin{frame}

       \begin{figure}
           \centering
           \includegraphics[width=0.25\linewidth]{phys11-electrostatics-parallel-plate-capacitor-diagram.png}
       \end{figure}

\end{frame}

% Parallel-Plate Capacitor
\begin{frame}
    \frametitle{Parallel-Plate Capacitor}
    \begin{block}{Capacitance Formula}
        For a parallel-plate capacitor:
        \begin{equation}
            C = \epsilon_0 \frac{A}{d}
        \end{equation}
        where:
        \begin{itemize}
            \item $\epsilon_0 = 8.85 \times 10^{-12} \, \text{F/m}$ (permittivity of free space)
            \item $A$ is the area of each plate
            \item $d$ is the separation distance between plates
        \end{itemize}
    \end{block}

    \begin{block}{Energy Storage}
        Energy stored in a capacitor:
        \begin{equation}
            U_E = \frac{1}{2}CV^2
        \end{equation}
    \end{block}
\end{frame}

% Dielectrics
\begin{frame}
    \frametitle{Dielectrics}
    \begin{block}{Definition}
        A dielectric material is an insulator that becomes polarized in an electric field.
    \end{block}

    \begin{block}{Effects of Dielectrics}
        Inserting a dielectric between capacitor plates:
        \begin{itemize}
            \item Increases the capacitance by a factor $\kappa$ (dielectric constant)
            \begin{equation}
                C = \kappa \epsilon_0 \frac{A}{d}
            \end{equation}
            \item Reduces the electric field inside the capacitor
            \item Allows for higher voltage before breakdown
        \end{itemize}
    \end{block}
    \end{frame}

\begin{frame}

      \begin{figure}
          \centering
          \includegraphics[width=0.7\linewidth]{phys11-electrostatics-dielectric-polarization.png}
      \end{figure}

\end{frame}

\section{Key Equations}

% Key Equations Summary
\begin{frame}
    \frametitle{Key Equations Summary}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \textbf{Coulomb's Law:}
            \begin{equation}
                F = \frac{kq_1q_2}{r^2}
            \end{equation}

            \textbf{Electric Field:}
            \begin{equation}
                E = \frac{F}{q_{\text{test}}}
            \end{equation}

            \textbf{Point Charge Field:}
            \begin{equation}
                E = \frac{kq}{r^2}
            \end{equation}
        \end{column}

        \begin{column}{0.5\textwidth}
            \textbf{Electric Potential:}
            \begin{equation}
                V = \frac{kQ}{r}
            \end{equation}

            \textbf{Capacitance:}
            \begin{equation}
                C = \frac{Q}{V}
            \end{equation}

            \textbf{Parallel-Plate Capacitor:}
            \begin{equation}
                C = \epsilon_0 \frac{A}{d}
            \end{equation}

            \textbf{Energy Storage:}
            \begin{equation}
                U_E = \frac{1}{2}CV^2
            \end{equation}
        \end{column}
    \end{columns}
\end{frame}

\section{Examples}

% "I do" Example
\begin{frame}
    \frametitle{"I do" Example: Coulomb's Law}
    \begin{block}{Problem}
        Two point charges $q_1 = +2.0 \, \mu\text{C}$ and $q_2 = -3.0 \, \mu\text{C}$ are separated by a distance of $0.15 \, \text{m}$. Find the magnitude and direction of the electric force between them.
    \end{block}
    \pause
    \begin{block}{Solution}
        Using Coulomb's law: $F = \frac{kq_1q_2}{r^2}$

        $F = \frac{(9 \times 10^9 \, \text{N} \cdot \text{m}^2/\text{C}^2)(2.0 \times 10^{-6} \, \text{C})(-3.0 \times 10^{-6} \, \text{C})}{(0.15 \, \text{m})^2}$

        $F = \frac{(9 \times 10^9)(-6.0 \times 10^{-12})}{0.0225}$

        $F = -2.4 \times 10^{-3} \, \text{N}$

        The negative sign indicates an attractive force. The force on $q_1$ is directed toward $q_2$, and the force on $q_2$ is directed toward $q_1$.
    \end{block}
\end{frame}

% "We do" Example
\begin{frame}
    \frametitle{"We do" Example: Electric Field}
    \begin{block}{Problem}
        Three point charges are arranged on the x-axis: $q_1 = +2.0 \, \mu\text{C}$ at $x = 0$, $q_2 = -3.0 \, \mu\text{C}$ at $x = 0.15 \, \text{m}$, and $q_3 = +1.0 \, \mu\text{C}$ at $x = 0.30 \, \text{m}$. Find the electric field at point P located at $x = 0.45 \, \text{m}$.
    \end{block}
        \pause

    \begin{block}{Solution Approach}
        1. Calculate the electric field due to each charge at point P
        \begin{align}
            E_1 &= \frac{kq_1}{r_1^2} = \frac{k(+2.0 \times 10^{-6})}{(0.45)^2} \text{ (pointing right)} \\
            E_2 &= \frac{kq_2}{r_2^2} = \frac{k(-3.0 \times 10^{-6})}{(0.30)^2} \text{ (pointing left)} \\
            E_3 &= \frac{kq_3}{r_3^2} = \frac{k(+1.0 \times 10^{-6})}{(0.15)^2} \text{ (pointing right)}
        \end{align}

        2. Find the total field by superposition: $\vec{E}_{\text{total}} = \vec{E}_1 + \vec{E}_2 + \vec{E}_3$
    \end{block}
\end{frame}

% "You do" Example
\begin{frame}
    \frametitle{"You do" Example: Capacitor}
    \begin{block}{Problem}
        A parallel-plate capacitor has plates with an area of $0.0025 \, \text{m}^2$ separated by a distance of $0.5 \, \text{mm}$.

        (a) Calculate the capacitance of this capacitor.

        (b) If the capacitor is connected to a $12 \, \text{V}$ battery, determine the charge stored on each plate.

        (c) Calculate the energy stored in the capacitor.

        (d) If a dielectric with $\kappa = 3.0$ is inserted between the plates, find the new capacitance.
    \end{block}

    \begin{block}{Hints}
        \begin{itemize}
            \item Use $C = \epsilon_0 \frac{A}{d}$ for part (a)
            \item Apply $Q = CV$ for part (b)
            \item Use $U_E = \frac{1}{2}CV^2$ for part (c)
            \item Remember that with a dielectric, $C = \kappa\epsilon_0 \frac{A}{d}$
        \end{itemize}
    \end{block}
\end{frame}

\section{Summary}

% Summary
\begin{frame}
    \frametitle{Summary: Key Takeaways}
    \begin{block}{Electrical Charges \& Coulomb's Law}
        \begin{itemize}
            \item Electric charge is conserved; like charges repel, unlike attract
            \item Coulomb's law: $F = \frac{kq_1q_2}{r^2}$
        \end{itemize}
    \end{block}

    \begin{block}{Electric Field \& Potential}
        \begin{itemize}
            \item Electric field: force per unit charge; $E = \frac{F}{q_{\text{test}}}$
            \item Electric potential: potential energy per unit charge; $V = \frac{U_E}{q}$
        \end{itemize}
    \end{block}

    \begin{block}{Capacitors \& Dielectrics}
        \begin{itemize}
            \item Capacitance $C = \frac{Q}{V}$; energy storage $U_E = \frac{1}{2}CV^2$
            \item Parallel-plate capacitor: $C = \epsilon_0 \frac{A}{d}$
            \item Dielectrics increase capacitance by a factor $\kappa$
        \end{itemize}
    \end{block}
\end{frame}

% End Slide
\begin{frame}
    \frametitle{Thank You!}
    \begin{center}
        \Large Questions?

        \vspace{1cm}

        \normalsize Practice problems: Textbook Chapter 18
    \end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch13-14-5-5_slides_electric-potential.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Waves \& Sound]{PHYS11 CH: 5.5, 13, 14}
\subtitle{Oscillations, Waves, and Sound Physics}
\author[Mr. Gullo]{Mr. Gullo}
\date[Mar 2025]{March 24, 2025}
\institute{Physics Department}

% Begin document
\begin{document}

% Title page
\frame{\titlepage}

% Table of contents
\begin{frame}
\frametitle{Outline}
\tableofcontents
\end{frame}

%----------- SECTION: Introduction to Oscillations and Waves -----------
\section{Introduction to Oscillations and Waves}

\begin{frame}
\frametitle{Learning Objectives}
By the end of this presentation, you will be able to:
\begin{itemize}
\item Define and describe simple harmonic motion and its key parameters
\item Identify and explain different types of waves and their properties
\item Understand wave interactions including superposition and interference
\item Apply wave principles to sound phenomena
\item Solve problems involving wave speed, frequency, and wavelength
\item Explain resonance and calculate resonant frequencies
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Simple Harmonic Motion (SHM)}
\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
\item An \textbf{oscillation} is a back and forth motion between two points
\item \textbf{Periodic motion} is a repetitious oscillation
\item \textbf{Period (T)}: Time for one complete oscillation
\item \textbf{Frequency (f)}: Number of oscillations per unit time
\begin{equation}
f = \frac{1}{T}
\end{equation}
\item An oscillation may create a \textbf{wave}, which propagates from its source
\end{itemize}

\column{0.4\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-waves-simple-harmonic-motion-spring.jpg}
\end{figure}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Hooke's Law and SHM}
The simplest oscillations are described by Hooke's Law:
\begin{equation}
F = -kx
\end{equation}
where:
\begin{itemize}
\item $F$ is the restoring force
\item $k$ is the spring constant
\item $x$ is the displacement from equilibrium
\end{itemize}

For a spring-mass system or simple pendulum (small angle):
\begin{align}
\text{Period in SHM: } T &= 2\pi \sqrt{\frac{m}{k}} \\
\text{Frequency in SHM: } f &= \frac{1}{2\pi}\sqrt{\frac{k}{m}} \\
\text{Period of pendulum: } T &= 2\pi \sqrt{\frac{L}{g}}
\end{align}
\end{frame}

%----------- SECTION: Wave Properties and Types -----------
\section{Wave Properties and Types}

\begin{frame}
\frametitle{Types of Waves}
\begin{block}{Definition}
A \textbf{wave} is a disturbance that moves from the point of creation and carries energy but not mass.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\textbf{Based on medium requirement:}
\begin{itemize}
\item \textbf{Mechanical waves} must travel through a medium
\begin{itemize}
\item Sound waves
\item Water waves
\item Earthquake waves
\end{itemize}
\item \textbf{Non-mechanical waves} can travel through vacuum
\begin{itemize}
\item Light waves
\end{itemize}
\end{itemize}

\column{0.5\textwidth}
\textbf{Based on disturbance direction:}
\begin{itemize}
\item \textbf{Transverse waves}: Disturbance perpendicular to propagation
\item \textbf{Longitudinal waves}: Disturbance parallel to propagation
\end{itemize}

\textbf{Based on duration:}
\begin{itemize}
\item \textbf{Periodic waves}: Repeat for several cycles
\item \textbf{Pulse waves}: One or few crests, sudden disturbance
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Wave Properties}
\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
\item \textbf{Wavelength ($\lambda$)}: Distance between adjacent identical parts of the wave
\item \textbf{Amplitude}: Maximum displacement from equilibrium
\item \textbf{Period (T)}: Time for one complete wave cycle
\item \textbf{Frequency (f)}: Number of waves per unit time
\begin{equation}
f = \frac{1}{T}
\end{equation}
\item \textbf{Wave velocity ($v_w$)}: Speed at which wave moves
\begin{equation}
v_w = \frac{\lambda}{T} \text{ or } v_w = f\lambda
\end{equation}
\end{itemize}

\column{0.4\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-waves-properties-wavelength-amplitude.jpg}
\end{figure}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Key Equations for Wave Motion}
\begin{block}{Wave Properties: Speed, Amplitude, Frequency, and Period}
\begin{align}
\text{Wave velocity: } v_w &= \frac{\lambda}{T} \text{ or } v_w = f\lambda \\
\text{Period: } T &= \frac{1}{f} \\
\text{Frequency: } f &= \frac{1}{T}
\end{align}
\end{block}

\begin{itemize}
\item In a given medium at a specific temperature (or density), the speed of a wave is the same for all frequencies and wavelengths
\item The relationship between wave velocity, frequency, and wavelength applies to all types of waves
\end{itemize}
\end{frame}

%----------- SECTION: Wave Interactions -----------
\section{Wave Interactions}

\begin{frame}
\frametitle{Superposition and Interference}
\begin{block}{Principle of Superposition}
When two or more waves overlap, the resultant displacement at any point is the algebraic sum of the displacements of the individual waves.
\end{block}

\begin{columns}
\column{0.5\textwidth}

\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-waves-interference-constructive-destructive.jpg}
\end{figure}

\column{0.5\textwidth}
\textbf{Constructive Interference}
\begin{itemize}
\item Occurs when waves are in phase
\item Amplitudes add together
\item Results in a larger amplitude
\end{itemize}
\textbf{Destructive Interference}
\begin{itemize}
\item Occurs when waves are out of phase
\item Amplitudes subtract
\item Results in a smaller or zero amplitude
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Standing Waves}
\begin{block}{Definition}
A \textbf{standing wave} is produced by the superposition of two identical waves traveling in opposite directions. It varies in amplitude but does not propagate.
\end{block}

\begin{itemize}
\item \textbf{Nodes}: Points where there is no motion
\item \textbf{Antinodes}: Locations of maximum amplitude
\end{itemize}

\begin{columns}
\column{0.6\textwidth}
\textbf{Other Wave Interactions:}
\begin{itemize}
\item \textbf{Reflection}: Wave changes direction
\item \textbf{Inversion}: Wave reflects from a fixed end
\item \textbf{Refraction}: Wave's path bends when passing between media with different densities
\end{itemize}

\column{0.4\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-waves-standing-wave-nodes.jpg}
\end{figure}
\end{columns}
\end{frame}

%----------- SECTION: Sound Waves -----------
\section{Sound Waves}

\begin{frame}
\frametitle{Sound Wave Characteristics}
\begin{block}{Definition}
\textbf{Sound} is a longitudinal mechanical wave created by a disturbance that is transmitted through a medium from its source outward.
\end{block}

\begin{itemize}
\item Sound waves require a medium to travel (cannot propagate in vacuum)
\item The relationship of speed, frequency, and wavelength:
\begin{equation}
v = f\lambda
\end{equation}
\item The speed of sound depends on the medium
\begin{itemize}
\item Air at 20°C: approximately 343 m/s
\item Water: approximately 1480 m/s
\item Steel: approximately 5960 m/s
\end{itemize}
\item In a given medium at specific temperature/density, the speed of sound is the same for all frequencies
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Sound Intensity and Sound Level}
\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
\item \textbf{Sound intensity (I)}: Power per unit area
\begin{equation}
I = \frac{P}{A} = \frac{(\Delta p)^2}{2\rho v_w}
\end{equation}
where $\Delta p$ is pressure variation, $\rho$ is density, and $v_w$ is wave speed

\item \textbf{Sound intensity level} in decibels (dB):
\begin{equation}
\beta \text{ (dB)} = 10 \log_{10}\left(\frac{I}{I_0}\right)
\end{equation}
where $I_0 = 10^{-12}$ W/m² (threshold of hearing)
\end{itemize}

\column{0.4\textwidth}
Some typical sound levels:
\begin{itemize}
\item Whisper: 20 dB
\item Normal conversation: 60 dB
\item Busy traffic: 80 dB
\item Threshold of pain: 120 dB
\item Jet engine: 140 dB
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Doppler Effect and Sonic Booms}
\begin{block}{Doppler Effect}
A shift in the observed frequency of a sound due to motion of either the source or the observer.
\end{block}

\begin{columns}
\column{0.6\textwidth}
\textbf{For a moving source:}
\begin{equation}
f_{obs} = f_s\left(\frac{v_w}{v_w \pm v_s}\right)
\end{equation}

\textbf{For a moving observer:}
\begin{equation}
f_{obs} = f_s\left(\frac{v_w \pm v_{obs}}{v_w}\right)
\end{equation}

Note: Use (+) when moving toward each other and (-) when moving apart

\column{0.4\textwidth}
\textbf{Sonic Boom}
\begin{itemize}
\item Occurs when an object moves faster than sound
\item Creates a shock wave
\item Result of constructive interference
\end{itemize}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-waves-sonic-boom.jpg}
\end{figure}
\end{columns}
\end{frame}

%----------- SECTION: Sound Interference and Resonance -----------
\section{Sound Interference and Resonance}

\begin{frame}
\frametitle{Sound Interference Patterns}
\begin{itemize}
\item Sound waves can interfere constructively or destructively
\item \textbf{Beats}: Occur when waves of slightly different frequencies are superimposed
\begin{equation}
f_B = |f_1 - f_2|
\end{equation}
\item Beats are perceived as periodic variations in loudness
\item Used in tuning musical instruments
\end{itemize}
% \begin{figure}
%     \centering
%     \includegraphics[width=0.5\linewidth]{BEAT.png}
% \end{figure}
% Note: BEAT.png image not found - needs to be replaced or recreated
\end{frame}

\begin{frame}
\frametitle{Resonance in Air Columns}
\begin{block}{Natural Frequency}
The frequency at which a system will oscillate if not affected by driving or damping forces.
\end{block}

\begin{block}{Resonance}
Occurs when a periodic force drives a harmonic oscillator at its natural frequency, resulting in maximum amplitude.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\textbf{Tube closed at one end:}
\begin{equation}
f_n = n\frac{v}{4L}, \: n = 1,3,5...
\end{equation}
\begin{itemize}
\item Fundamental: $f_1 = \frac{v}{4L}$
\item Only odd harmonics
\end{itemize}

\column{0.5\textwidth}
\textbf{Tube open at both ends:}
\begin{equation}
f_n = n\frac{v}{2L}, \: n = 1,2,3...
\end{equation}
\begin{itemize}
\item Fundamental: $f_1 = \frac{v}{2L}$
\item All harmonics possible
\end{itemize}


\end{columns}
\end{frame}

\begin{frame}{}

\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-waves-resonance-closed-tube.png}
\end{figure}

\end{frame}
\begin{frame}{}

\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-waves-resonance-closed-tube.png}
\end{figure}
\end{frame}

%----------- SECTION: Problem-Solving Approach -----------
\section{Problem-Solving Approach}

\begin{frame}
\frametitle{"I do" - Wave Properties Example}
\begin{block}{Problem}
A wave has a frequency of 40 Hz and a wavelength of 0.5 m. Calculate the wave velocity.
\end{block}

\begin{block}{Solution}
Given:
\begin{itemize}
\item Frequency $f = 40 \text{ Hz}$
\item Wavelength $\lambda = 0.5 \text{ m}$
\end{itemize}

Using the wave velocity equation:
\begin{align}
v_w &= f\lambda \\
v_w &= 40 \text{ Hz} \times 0.5 \text{ m} \\
v_w &= 20 \text{ m/s}
\end{align}
\end{block}
\end{frame}

\begin{frame}
\frametitle{"We do" - Speed of Sound Example}
\begin{block}{Problem}
Sound travels at 343 m/s in air. If a sound wave has a frequency of 686 Hz, what is its wavelength?
\end{block}

\begin{block}{Partial Solution}
Given:
\begin{itemize}
\item Speed of sound $v = 343 \text{ m/s}$
\item Frequency $f = 686 \text{ Hz}$
\end{itemize}

Using the wave velocity equation:
\begin{align}
v &= f\lambda \\
343 \text{ m/s} &= 686 \text{ Hz} \times \lambda
\end{align}

Now, solve for $\lambda$...
\end{block}

\end{frame}

\begin{frame}
\frametitle{"You do" - Sound Resonance Example}
\begin{block}{Problem}
A tube open at both ends has a length of 0.85 m. If the speed of sound in air is 343 m/s, what are the frequencies of the fundamental and first two overtones?
\end{block}

\begin{block}{Approach}
1. Identify the type of resonator (open at both ends)
2. Recall the formula for resonant frequencies in an open tube
3. Calculate the fundamental frequency
4. Calculate the frequencies of the first two overtones
\end{block}

\textbf{Try it yourself!} We'll review the solution in a moment.
\end{frame}

\begin{frame}
\frametitle{"You do" - Sound Resonance Solution}
\begin{block}{Solution}
For a tube open at both ends:
\begin{equation}
f_n = n\frac{v}{2L}, \: n = 1,2,3...
\end{equation}

Given:
\begin{itemize}
\item Length $L = 0.85 \text{ m}$
\item Speed of sound $v = 343 \text{ m/s}$
\end{itemize}

Fundamental frequency ($n = 1$):
\begin{equation}
f_1 = \frac{343 \text{ m/s}}{2 \times 0.85 \text{ m}} = 201.8 \text{ Hz}
\end{equation}

First overtone ($n = 2$): $f_2 = 2f_1 = 403.5 \text{ Hz}$

Second overtone ($n = 3$): $f_3 = 3f_1 = 605.3 \text{ Hz}$
\end{block}
\end{frame}

%----------- SECTION: Summary -----------
\section{Summary}

\begin{frame}
\frametitle{Key Concepts Review}
\begin{columns}
\column{0.5\textwidth}
\textbf{Simple Harmonic Motion}
\begin{itemize}
\item Oscillations and periodic motion
\item Period and frequency relationship
\item Hooke's Law systems
\end{itemize}

\textbf{Waves}
\begin{itemize}
\item Types: mechanical/non-mechanical
\item Types: transverse/longitudinal
\item Properties: wavelength, amplitude, frequency
\item Speed-wavelength-frequency relationship
\end{itemize}

\column{0.5\textwidth}
\textbf{Wave Interactions}
\begin{itemize}
\item Superposition principle
\item Constructive/destructive interference
\item Standing waves, nodes, antinodes
\end{itemize}

\textbf{Sound}
\begin{itemize}
\item Longitudinal mechanical wave
\item Intensity and sound level
\item Doppler effect
\item Resonance and harmonics
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Essential Equations}
\begin{columns}
\column{0.5\textwidth}
\textbf{Simple Harmonic Motion}
\begin{align}
F &= -kx \\
T &= 2\pi\sqrt{\frac{m}{k}} \\
T_{pendulum} &= 2\pi\sqrt{\frac{L}{g}}
\end{align}

\textbf{Wave Properties}
\begin{align}
v_w &= \frac{\lambda}{T} \text{ or } v_w = f\lambda \\
T &= \frac{1}{f}
\end{align}

\column{0.5\textwidth}
\textbf{Sound Intensity}
\begin{align}
I &= \frac{P}{A} = \frac{(\Delta p)^2}{2\rho v_w} \\
\beta \text{ (dB)} &= 10 \log_{10}\left(\frac{I}{I_0}\right)
\end{align}

\textbf{Resonance}
\begin{align}
f_B &= |f_1 - f_2| \\
f_n &= n\frac{v}{4L}, \: n = 1,3,5... \text{ (closed)} \\
f_n &= n\frac{v}{2L}, \: n = 1,2,3... \text{ (open)}
\end{align}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Connecting the Concepts}
\begin{itemize}
\item Simple harmonic motion creates oscillations
\item Oscillations can generate waves
\item Waves transport energy without transporting matter
\item Sound is a longitudinal mechanical wave
\item Wave properties (speed, frequency, wavelength) apply to all wave types
\item Wave interactions explain phenomena like resonance and interference
\item Understanding these principles helps explain everyday phenomena:
\begin{itemize}
\item Musical instruments
\item Hearing
\item Doppler radar
\item Medical ultrasound
\item Noise cancellation
\end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Thank You!}
\begin{center}
\Large Questions?
\end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch09_slides_energy-work.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

\title[Work \& Energy]{PHYS11 CH9: Work, Energy, and Energy Conservation}
\subtitle{From Work to Energy Conservation}
\author[Mr. Gullo]{Mr. Gullo}
\date[Feb 2025]{February, 2025}


\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Chapter Sections}
\tableofcontents
\end{frame}

\section{9.1 Work, Power, and the Work-Energy Theorem}

\begin{frame}
\frametitle{9.1 Learning Objectives}
By the end of this section, you will be able to:
\begin{itemize}
\item Describe and apply the work-energy theorem
\item Describe and calculate work and power
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{9.1 Understanding Work}
\begin{block}{Work Definition}
Work = Force × Distance (in direction of force)
$$W = F \cdot d$$
\end{block}

\begin{block}{Key Points About Work}
\begin{itemize}
\item Work is done only when force causes displacement
\item Force must be parallel to displacement
\item Work can be positive or negative:
 \begin{itemize}
 \item Positive: Force in same direction as motion
 \item Negative: Force opposing motion
 \end{itemize}
\item No work is done when:
 \begin{itemize}
 \item Force is perpendicular to motion
 \item No displacement occurs
 \end{itemize}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{9.1 Work and Force Relationships}
\begin{block}{Force and Weight}
$$F = w = mg$$
Where:
\begin{itemize}
\item $F$ = Force (N)
\item $w$ = Weight (N)
\item $m$ = Mass (kg)
\item $g$ = Gravitational acceleration (9.8 m/s²)
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Work and Changes in Gravitational Potential Energy}
\begin{block}{Work and $\Delta PE_g$ Relationship}
$$W = \Delta PE_g = mg\Delta h = mg(h_2 - h_1)$$
Where:
\begin{itemize}
\item $W$ = Work done (J)
\item $\Delta PE_g$ = Change in gravitational potential energy (J)
\item $m$ = Mass of object (kg)
\item $g$ = Gravitational acceleration (9.8 m/s²)
\item $h_2$ = Final height (m)
\item $h_1$ = Initial height (m)
\item $\Delta h$ = Change in height = $h_2 - h_1$ (m)
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\begin{alertblock}{Important Note}
\begin{itemize}
\item Positive work ($\Delta h > 0$): Lifting object against gravity
\item Negative work ($\Delta h < 0$): Object falling with gravity
\item Work done against gravity equals the change in gravitational potential energy of the object
\end{itemize}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{9.1 Work-Energy Theorem}
\begin{block}{Work-Energy Theorem}
$$W = \Delta KE = \frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2$$
\end{block}

\begin{block}{Components}
Where:
\begin{itemize}
\item $W$ = Net work done on object (J)
\item $\Delta KE$ = Change in kinetic energy (J)
\item $m$ = Mass of object (kg)
\item $v_1$ = Initial velocity (m/s)
\item $v_2$ = Final velocity (m/s)
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\begin{alertblock}{Key Concept}
The net work done on an object equals its change in kinetic energy. This means:
\begin{itemize}
\item Positive work increases kinetic energy ($v_2 > v_1$)
\item Negative work decreases kinetic energy ($v_2 < v_1$)
\end{itemize}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{9.1 Power - Rate of Work}
\begin{block}{Power Definition}
$$P = \frac{W}{t}$$
Rate at which work is done or energy is transferred
\end{block}
\end{frame}

\begin{frame}
\begin{block}{Power Relationships}
Alternative forms:
\begin{align*}
P &= \frac{W}{t} = \frac{Fd}{t} = F\cdot v \\[1em]
P &= \frac{\Delta E}{t}
\end{align*}
Where:
\begin{itemize}
\item $P$ = Power (watts, W)
\item $W$ = Work done (joules, J)
\item $t$ = Time interval (seconds, s)
\item $F$ = Force (newtons, N)
\item $v$ = Velocity (m/s)
\item $\Delta E$ = Energy change (J)
\end{itemize}
\end{block}

\begin{exampleblock}{Real-World Applications}
\begin{itemize}
\item Engine power ratings
\item Electrical appliance ratings
\item Human power output in athletics
\end{itemize}
\end{exampleblock}
\end{frame}

\begin{frame}
\frametitle{9.1 Example: Calculating Work}
Problem: Calculate the work done lifting a 2.0 kg book 1.5 m vertically.
\begin{block}{Solution}
\begin{enumerate}
\item Force needed = weight = mg = (2.0 kg)(9.8 m/s²) = 19.6 N
\item Distance = 1.5 m
\item Work = F × d = 19.6 N × 1.5 m = 29.4 J
\end{enumerate}
\end{block}
\end{frame}
\begin{frame}
\frametitle{Units of Work}
\begin{block}{Work = Force × Distance}
$$W = F \cdot d$$
\end{block}

\begin{block}{SI Units}
\begin{itemize}
\item Force (F): Newtons (N)
\item Distance (d): meters (m)
\item Work (W): Newton-meters (N⋅m) = Joules (J)
\end{itemize}
\end{block}

\begin{block}{Unit Analysis}
$$1 \text{ Joule} = 1 \text{ N} \cdot 1 \text{ m} = 1 \text{ kg}\cdot\frac{\text{m}}{\text{s}^2} \cdot \text{m} = 1 \text{ kg}\cdot\frac{\text{m}^2}{\text{s}^2}$$
\end{block}
\end{frame}

\begin{frame}
\frametitle{Units of Power}
\begin{block}{Power = Work ÷ Time}
$$P = \frac{W}{t}$$
\end{block}

\begin{block}{SI Units}
\begin{itemize}
\item Work (W): Joules (J)
\item Time (t): seconds (s)
\item Power (P): Joules per second (J/s) = Watts (W)
\end{itemize}
\end{block}

\begin{block}{Common Power Units}
\begin{itemize}
\item 1 kilowatt (kW) = 1,000 watts
\item 1 horsepower (hp) ≈ 746 watts
\item 1 kilowatt-hour (kWh) = power × time = 3,600,000 joules
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Units in Energy Equations}
\begin{block}{Kinetic Energy}
$$KE = \frac{1}{2}mv^2$$
Units: $\text{kg} \cdot (\frac{\text{m}}{\text{s}})^2 = \text{kg}\cdot\frac{\text{m}^2}{\text{s}^2} = \text{Joules}$
\end{block}

\begin{block}{Gravitational Potential Energy}
$$PE = mgh$$
Units: $\text{kg} \cdot \frac{\text{m}}{\text{s}^2} \cdot \text{m} = \text{kg}\cdot\frac{\text{m}^2}{\text{s}^2} = \text{Joules}$
\end{block}

\begin{exampleblock}{Unit Consistency}
All forms of energy (KE, PE, Work) are measured in Joules, allowing direct comparison and conversion between different forms of energy.
\end{exampleblock}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-energy-watts-industrial-revolution.png}
\end{figure}
\end{frame}

\section{9.2 Mechanical Energy and Conservation of Energy}

\begin{frame}
\frametitle{9.2 Learning Objectives}
By the end of this section, you will be able to:
\begin{itemize}
\item Explain the law of conservation of energy
\item Perform calculations with mechanical energy
\item Apply conservation of energy principles
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{9.2 Types of Mechanical Energy}
\begin{block}{Kinetic Energy (Energy of Motion)}
$$KE = \frac{1}{2}mv^2$$
\end{block}

\begin{block}{Gravitational Potential Energy}
$$PE = mgh$$
\end{block}
\end{frame}

\begin{frame}
\frametitle{9.2 Conservation of Mechanical Energy}
\begin{block}{Energy Conservation Equation}
$$E_{total} = E_{mechanical} = KE + PE = \text{constant}$$
$$\therefore KE_1 + PE_1 = KE_2 + PE_2$$
\end{block}

\begin{alertblock}{What This Means}
In a closed system with no friction:
\begin{itemize}
\item Initial Energy = Final Energy
\item $\frac{1}{2}mv_1^2 + mgh_1 = \frac{1}{2}mv_2^2 + mgh_2$
\end{itemize}
\end{alertblock}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-energy-conservation-roller-coaster.png}
\end{figure}
\begin{block}{Energy Transformations}
\begin{center}
\begin{tabular}{c c c}
\textbf{State 1} & $\rightarrow$ & \textbf{State 2} \\
\hline
High PE, Low KE & $\rightarrow$ & Low PE, High KE \\
(Top of hill) & & (Bottom of hill) \\[1em]
Low PE, High KE & $\rightarrow$ & High PE, Low KE \\
(Bottom of hill) & & (Top of hill)
\end{tabular}
\end{center}
\end{block}
\end{frame}

\begin{frame}
\frametitle{9.2 Energy Conservation Examples}
\begin{block}{Example: Roller Coaster}
\begin{itemize}
\item At top: High PE, Low KE
 $$PE_{max} = mgh, \quad KE \approx 0$$
\item At bottom: Low PE, High KE
 $$PE \approx 0, \quad KE_{max} = \frac{1}{2}mv^2$$
\item Total Energy stays constant:
 $$mgh = \frac{1}{2}mv^2$$
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\begin{exampleblock}{Key Points}
\begin{itemize}
\item Energy is never created or destroyed
\item Energy only transforms from one form to another
\item In real systems, some mechanical energy converts to heat due to friction
\item Total system energy always remains constant
\end{itemize}
\end{exampleblock}
\end{frame}

\begin{frame}
\frametitle{9.2 Example: Energy Conservation}
A roller coaster car (500 kg) starts from rest at height 40 m. What is its speed at height 15 m?
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-energy-conservation-roller-coaster.png}
\end{figure}

\end{frame}


\begin{frame}
\begin{block}{Solution Steps}
\begin{enumerate}
\item Initial PE = mgh₁ = (500)(9.8)(40) = 196,000 J
\item Final PE = mgh₂ = (500)(9.8)(15) = 73,500 J
\item Conservation: PE₁ = PE₂ + KE₂
\item 196,000 = 73,500 + ½(500)v²
\item Solve for v
\end{enumerate}
\end{block}
\end{frame}

\section{9.3 Simple Machines}

\begin{frame}
\frametitle{9.3 Learning Objectives}
By the end of this section, you will be able to:
\begin{itemize}
\item Describe simple and complex machines
\item Calculate mechanical advantage and efficiency
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{9.3 Simple Machines: Basic Mechanical Advantage}
\begin{block}{General Ideal Mechanical Advantage (IMA)}
$$IMA = \frac{F_r}{F_e} = \frac{d_e}{d_r}$$
Where:
\begin{itemize}
\item $F_r$ = Resistance force (output force)
\item $F_e$ = Effort force (input force)
\item $d_e$ = Distance effort moves
\item $d_r$ = Distance resistance moves
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{9.3 Simple Machines: Levers and Wheel-Axle}
\begin{block}{Lever}
$$IMA = \frac{L_e}{L_r}$$
Where:
\begin{itemize}
\item $L_e$ = Length of effort arm
\item $L_r$ = Length of resistance arm
\end{itemize}
\end{block}

\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys11-machines-lever-diagram.png}
\end{figure}
\end{frame}

\begin{frame}
\begin{block}{Wheel and Axle}
$$IMA = \frac{R}{r}$$
Where:
\begin{itemize}
\item $R$ = Radius of wheel
\item $r$ = Radius of axle
\end{itemize}
\end{block}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-machines-axle-diagram.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{9.3 Simple Machines: Inclined Plane and Wedge}
\begin{block}{Inclined Plane}
$$IMA = \frac{L}{h}$$
Where:
\begin{itemize}
\item $L$ = Length of slope
\item $h$ = Vertical height
\end{itemize}
\end{block}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{InclinePlane.png}
\end{figure}

\end{frame}

\begin{frame}


\begin{block}{Wedge}
$$IMA = \frac{L}{t}$$
Where:
\begin{itemize}
\item $L$ = Length of wedge
\item $t$ = Thickness of wedge
\end{itemize}
\end{block}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{InclinePlane.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{9.3 Simple Machines: Pulley and Screw}
\begin{block}{Pulley}
$$IMA = N$$
Where:
\begin{itemize}
\item $N$ = Number of rope sections supporting the load
\end{itemize}
\end{block}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{Pulley.png}
\end{figure}
\end{frame}

\begin{frame}
\begin{block}{Screw}
$$IMA = \frac{2\pi L}{P}$$
Where:
\begin{itemize}
\item $L$ = Length of effort arm
\item $P$ = Pitch (distance between threads)
\item $2\pi$ = Circumference factor
\end{itemize}
\end{block}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-machines-screw-diagram.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{9.3 Work Input and Output}
\begin{block}{Input Work}
$$W_i = F_id_i$$
Where:
\begin{itemize}
\item $W_i$ = Work input (energy put into machine)
\item $F_i$ = Input force (effort force)
\item $d_i$ = Input distance (distance effort moves)
\end{itemize}
\end{block}

\begin{block}{Output Work}
$$W_o = F_od_o$$
Where:
\begin{itemize}
\item $W_o$ = Work output (useful work done by machine)
\item $F_o$ = Output force (resistance force)
\item $d_o$ = Output distance (distance load moves)
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{9.3 Machine Efficiency}
\begin{block}{Efficiency Formula}
$$\text{Efficiency} = \frac{W_o}{W_i} \times 100\%$$
\end{block}

\begin{block}{Important Points}
\begin{itemize}
\item Efficiency is always less than 100% in real machines
\item Energy is lost to:
 \begin{itemize}
 \item Friction between moving parts
 \item Heat generation
 \item Sound production
 \end{itemize}
\item Higher efficiency means less energy waste
\item Efficiency can be improved through:
 \begin{itemize}
 \item Better lubrication
 \item Smoother surfaces
 \item Proper maintenance
 \end{itemize}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Chapter Summary}
\begin{itemize}
\item \textbf{9.1 Work and Power}
  \begin{itemize}
  \item Work is force times distance
  \item Power is rate of doing work
  \end{itemize}
\item \textbf{9.2 Energy Conservation}
  \begin{itemize}
  \item Energy transforms between forms
  \item Total energy is conserved
  \end{itemize}
\item \textbf{9.3 Simple Machines}
  \begin{itemize}
  \item Machines trade force for distance
  \item Efficiency measures useful work output
  \end{itemize}
\end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch12_slides_electric-fields.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}
\setbeamercolor{block title}{bg=ds9blue,fg=white}
\setbeamercolor{block body}{bg=ds9grey!20,fg=black}

% Title page configuration
\title[Thermodynamics]{PHYS11 CH:12.1-12.4}
\subtitle{Laws of Thermodynamics and Applications}
\author[Mr. Gullo]{Mr. Gullo}
\date[March 2025]{March, 2025}
\institute{Physics Department}

\begin{document}

% Title slide
\begin{frame}
    \titlepage
\end{frame}

% Outline slide
\begin{frame}
    \frametitle{Overview}
    \tableofcontents
\end{frame}

% Learning objectives
\begin{frame}
    \frametitle{Learning Objectives}
    \begin{block}{By the end of this lesson, you will be able to:}
        \begin{itemize}
            \item Explain the concept of thermal equilibrium and the zeroth law
            \item Apply the first law of thermodynamics to calculate energy, work, and heat
            \item Understand entropy and the second law of thermodynamics
            \item Describe the working principles of heat engines, heat pumps, and refrigerators
            \item Calculate thermal efficiency of heat engines
            \item Relate thermodynamic principles to real-world applications
        \end{itemize}
    \end{block}
\end{frame}

\section{Zeroth Law of Thermodynamics}

\begin{frame}
    \frametitle{Thermal Equilibrium}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{itemize}
            \item \textbf{Thermal Equilibrium:} Two systems have the same temperature
            \item \textbf{Thermal Contact:} Heat can transfer between objects
            \item Two objects in thermal contact will eventually reach thermal equilibrium
            \item At equilibrium, there is no net heat transfer
        \end{itemize}

        \column{0.4\textwidth}
        \begin{center}
            \begin{figure}
                \centering
                \includegraphics[width=0.75\linewidth]{phys11-thermo-thermal-equilibrium.jpg}
            \end{figure}
        \end{center}
    \end{columns}

    \begin{block}{Important Point}
        Thermal equilibrium occurs when two bodies are in contact with each other and can freely exchange energy.
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{The Zeroth Law of Thermodynamics}
    \begin{block}{Zeroth Law Statement}
        If two systems, A and B, are in thermal equilibrium with each other, and B is in thermal equilibrium with a third system, C, then A is also in thermal equilibrium with C.
    \end{block}

    \begin{center}
        \begin{figure}
            \centering
            \includegraphics[width=0.5\linewidth]{phys11-thermo-zeroth-law.jpg}
        \end{figure}
    \end{center}

    \begin{exampleblock}{Mathematical Analogy}
        Similar to the transitive property in mathematics:

        If A = B and B = C, then A = C
    \end{exampleblock}
\end{frame}

\section{First Law of Thermodynamics}

\begin{frame}
    \frametitle{Pressure and Thermal Expansion}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Pressure:}
        \begin{itemize}
            \item Force per unit area
            \begin{align*}
                P = \frac{F}{A}
            \end{align*}
            \item SI unit: Pascal (Pa) = N/m²
        \end{itemize}

        \column{0.5\textwidth}
        \textbf{Thermal Expansion:}
        \begin{itemize}
            \item Change in size due to temperature change
            \item Results from increased molecular motion
            \item Important in engineering and everyday applications (bridges, thermostats, etc.)
        \end{itemize}
    \end{columns}

    \begin{block}{Why does thermal expansion occur?}
        An increase in temperature causes intermolecular distances to increase as particles gain kinetic energy.
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Ideal Gas Law}
    \begin{alertblock}{Ideal Gas Law}
        \begin{align*}
            PV = NkT
        \end{align*}
        where:
        \begin{itemize}
            \item $P$ = pressure (Pa)
            \item $V$ = volume (m³)
            \item $N$ = number of particles
            \item $k$ = Boltzmann constant ($1.38 \times 10^{-23}$ J/K)
            \item $T$ = absolute temperature (K)
        \end{itemize}
    \end{alertblock}
    \end{frame}

\begin{frame}
    \begin{exampleblock}{Real vs. Ideal Gases}
        A real gas behaves most like an ideal gas at:
        \begin{itemize}
            \item High temperatures
            \item Low pressures
        \end{itemize}
        Under these conditions, particle interactions become negligible.
    \end{exampleblock}
\end{frame}

\begin{frame}
    \frametitle{Energy Transfer: Heat and Work}
    \begin{block}{Two Methods of Energy Transfer}
        \begin{itemize}
            \item \textbf{Heat (Q):} Energy transferred solely due to a temperature difference
            \item \textbf{Work (W):} Energy transfer that doesn't rely on temperature difference
        \end{itemize}
    \end{block}

    \begin{exampleblock}{Pressure-Volume Work}
        \begin{align*}
            W = P\Delta V
        \end{align*}

        \begin{itemize}
            \item Work is done \textit{by} a system when it \textit{expands} ($\Delta V > 0$)
            \item Work is done \textit{on} a system when it is \textit{compressed} ($\Delta V < 0$)
        \end{itemize}
    \end{exampleblock}

    \begin{center}
        \alert{[Diagram showing work done by/on a gas in a piston]}
    \end{center}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.4\linewidth]{phys11-thermo-work-done-by-gas-piston.png}
\end{figure}
\end{frame}

\begin{frame}
    \frametitle{First Law of Thermodynamics}
    \begin{alertblock}{First Law Statement}
        The change in internal energy of a system equals the net heat transferred into the system minus the net work done by the system.

        \begin{align*}
            \Delta U = Q - W
        \end{align*}

        where:
        \begin{itemize}
            \item $\Delta U$ = change in internal energy
            \item $Q$ = net heat transferred into the system
            \item $W$ = net work done by the system
        \end{itemize}
    \end{alertblock}
    \end{frame}

\begin{frame}
    \begin{block}{Key Insights}
        \begin{itemize}
            \item The first law is an application of the conservation of energy
            \item Internal energy ($U$) depends only on the state of the system
            \item $Q$ and $W$ represent energy in transit; only $\Delta U$ represents stored energy
        \end{itemize}
    \end{block}
\end{frame}

\section{Second Law of Thermodynamics}

\begin{frame}
    \frametitle{Entropy}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{block}{What is Entropy?}
            \begin{itemize}
                \item A measure of a system's disorder
                \item The reduced availability of energy to do work
                \item SI unit: joules per kelvin (J/K)
            \end{itemize}
        \end{block}

        \column{0.4\textwidth}
        \begin{center}
            \begin{figure}
                \centering
                \includegraphics[width=0.8\linewidth]{phys11-thermo-entropy-disorder.jpg}
            \end{figure}
        \end{center}
    \end{columns}

    \begin{exampleblock}{Change in Entropy}
        \begin{align*}
            \Delta S = \frac{Q}{T}
        \end{align*}
        where:
        \begin{itemize}
            \item $\Delta S$ = change in entropy
            \item $Q$ = heat transferred
            \item $T$ = absolute temperature
        \end{itemize}
    \end{exampleblock}
\end{frame}

\begin{frame}
    \frametitle{Second Law of Thermodynamics}
    \begin{alertblock}{Second Law Statement}
        For any spontaneous process, the total entropy of a system either increases or remains constant; it never decreases.
    \end{alertblock}

    \begin{block}{Implications of the Second Law}
        \begin{itemize}
            \item Heat flows spontaneously from higher to lower temperature, never the reverse
            \item Energy tends to disperse from concentrated to dispersed states
            \item Perfect heat engines (100\% efficiency) are impossible
            \item All natural processes are irreversible
        \end{itemize}
    \end{block}

    \begin{exampleblock}{Everyday Examples}
        \begin{itemize}
            \item Air freshener molecules dispersing in a room
            \item Ice melting in water
            \item Spreading of salt in water
        \end{itemize}
    \end{exampleblock}
\end{frame}

\section{Applications of Thermodynamics}

\begin{frame}
    \frametitle{Heat Engines}
    \begin{columns}
        \column{0.55\textwidth}
        \begin{itemize}
            \item \textbf{Heat Engine:} Device that converts thermal energy to mechanical work
            \item Uses temperature difference between hot and cold reservoirs
            \item Works through a cyclic process
            \item Examples: steam engines, internal combustion engines, gas turbines
        \end{itemize}

        \column{0.45\textwidth}
        \begin{center}
            \begin{figure}
                \centering
                \includegraphics[width=0.7\linewidth]{phys11-thermo-heat-engine-diagram.png}
            \end{figure}
        \end{center}
    \end{columns}

    \begin{block}{Cyclic Process}
        A process that returns to its original state at the end of every cycle, so that the change in internal energy is zero ($\Delta U = 0$).
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Thermal Efficiency}
    \begin{alertblock}{Thermal Efficiency Formula}
        \begin{align*}
            \text{eff} = \frac{W}{Q_h} = \frac{Q_h - Q_c}{Q_h} = 1 - \frac{Q_c}{Q_h}
        \end{align*}
        where:
        \begin{itemize}
            \item eff = thermal efficiency
            \item $W$ = work output
            \item $Q_h$ = heat input from hot reservoir
            \item $Q_c$ = heat output to cold reservoir
        \end{itemize}
    \end{alertblock}
    \end{frame}

\begin{frame}
    \begin{block}{Important Points}
        \begin{itemize}
            \item Efficiency is always less than 100\%
            \item Some heat is always lost to the environment
            \item Efficiency would be 100\% only if $Q_c = 0$ (impossible due to the second law)
            \item For a cyclical process, work output $W = Q_h - Q_c$
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Heat Pumps and Refrigerators}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Heat Pump:}
        \begin{itemize}
            \item Transfers heat from cold to hot environment
            \item Requires work input
            \item Used for heating buildings
            \item Energy efficient compared to direct heating
        \end{itemize}

        \column{0.5\textwidth}
        \textbf{Refrigerator:}
        \begin{itemize}
            \item A type of heat pump
            \item Removes heat from inside to outside
            \item Components: compressor, condenser, expansion valve, evaporator
        \end{itemize}
    \end{columns}

    \begin{block}{Advantage of Heat Pumps}
        A heat pump supplies energy by heat from the cold, outside air and also from the energy generated by the work done.
    \end{block}

    \begin{center}
        \alert{[Diagram showing heat pump/refrigerator cycle]}
    \end{center}
\end{frame}


\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys11-thermo-heat-pump-refrigerator-cycle.png}
\end{figure}
\end{frame}
\section{Examples and Applications}

\begin{frame}
    \frametitle{"I do" Example}
    \begin{block}{Problem}
        Some amount of energy is transferred by heat into a system. The net work done by the system is 50 J, while the increase in its internal energy is 30 J. What is the amount of net heat?
    \end{block}
    \end{frame}

\begin{frame}
    \begin{exampleblock}{Solution}
        \begin{enumerate}
            \item Use the first law of thermodynamics: $\Delta U = Q - W$
            \item Given information:
            \begin{itemize}
                \item $\Delta U = 30$ J (increase in internal energy)
                \item $W = 50$ J (net work done by the system)
            \end{itemize}

            \item Rearrange the equation to solve for $Q$:
            \begin{align*}
                Q &= \Delta U + W\\
                &= 30 \text{ J} + 50 \text{ J}\\
                &= 80 \text{ J}
            \end{align*}

            \item Therefore, the amount of net heat transferred to the system is 80 J.
        \end{enumerate}
    \end{exampleblock}
\end{frame}

\begin{frame}
    \frametitle{"We do" Example}
    \begin{block}{Problem}
        Assume 310 J of heat enter a system, after which the system does 120 J of work. What is the change in its internal energy? Would this amount change if the energy transferred by heat were added after the work was done instead of before?
    \end{block}
    \pause
    \begin{exampleblock}{Solution Steps}
        \begin{enumerate}
            \item Apply the first law of thermodynamics: $\Delta U = Q - W$
            \item Given information:
            \begin{itemize}
                \item $Q = 310$ J (heat entering the system)
                \item $W = 120$ J (work done by the system)
            \end{itemize}

            \item Calculate the change in internal energy:
            \begin{align*}
                \Delta U &= Q - W \\
                &= 310 \text{ J} - 120 \text{ J} \\
                &= 190 \text{ J}
            \end{align*}
             \end{enumerate}
    \end{exampleblock}

    Let's work through this together!
\end{frame}

\begin{frame}
    \frametitle{"You do" Example}
    \begin{block}{Problem}
        A coal power station functions at 40.0 percent efficiency. What is the amount of work it does if it takes in 4.00×10⁶ J by heat?
    \end{block}
    \pause
    \begin{alertblock}{Hints}
        \begin{itemize}
            \item Use the thermal efficiency formula: $\text{eff} = \frac{W}{Q_h}$
            \item Efficiency is given as a percentage (40.0\%)
            \item Heat input ($Q_h$) is 4.00×10⁶ J
        \end{itemize}
    \end{alertblock}

    Take some time to work this out. Then we'll discuss the solution.

    \pause

    \begin{exampleblock}{Answer}
        The work done by the power station is 1.60×10⁶ J.
    \end{exampleblock}
\end{frame}

\section{Summary}

\begin{frame}
    \frametitle{Key Equations}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{First Law of Thermodynamics:}
        \begin{align*}
            \Delta U &= Q - W \\
            PV &= NkT \\
            P &= \frac{F}{A} \\
            W &= P\Delta V
        \end{align*}

        \column{0.5\textwidth}
        \textbf{Second Law and Applications:}
        \begin{align*}
            \Delta S &= \frac{Q}{T} \\
            \text{eff} &= \frac{W}{Q_h} \\
            W &= Q_h - Q_c
        \end{align*}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Laws of Thermodynamics Summary}
    \begin{block}{Zeroth Law}
        If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.
    \end{block}

    \begin{block}{First Law}
        Energy can be transferred and transformed, but it cannot be created or destroyed.

        $\Delta U = Q - W$
    \end{block}

    \begin{block}{Second Law}
        For any spontaneous process, the total entropy of a system either increases or remains constant; it never decreases.
    \end{block}

    \begin{block}{Practical Applications}
        Heat engines, power plants, refrigerators, heat pumps, and many industrial processes rely on thermodynamic principles.
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Thank You!}
    \begin{center}
        \Huge{Questions?}

        \vspace{1cm}
        \normalsize
        Remember to review the key laws and concepts for the upcoming quiz!
    \end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch11_slides_electric-charge.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Thermal Physics]{PHYS11 CH:11}
\subtitle{Temperature, Heat, and Phase Changes}
\author[Mr. Gullo]{Mr. Gullo}
\date[March 2025]{March, 2025}
\institute{Physics Department}

\begin{document}

% Title slide
\begin{frame}
    \titlepage
\end{frame}

% Outline slide
\begin{frame}
    \frametitle{Overview}
    \tableofcontents
\end{frame}

% Learning objectives
\begin{frame}
    \frametitle{Learning Objectives}
    \begin{block}{By the end of this lesson, you will be able to:}
        \begin{itemize}
            \item Define temperature and explain its relationship to molecular motion
            \item Convert between temperature scales (Celsius, Fahrenheit, and Kelvin)
            \item Explain the difference between heat and temperature
            \item Calculate heat transfer using $Q = mc\Delta T$
            \item Identify the three mechanisms of heat transfer
            \item Describe phase changes and calculate energy using latent heat
        \end{itemize}
    \end{block}
\end{frame}

\section{Temperature and Thermal Energy}

\begin{frame}
    \frametitle{Temperature and Thermal Energy}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{itemize}
            \item \textbf{Temperature:} Quantity measured by a thermometer
            \item Related to the average kinetic energy of atoms and molecules
            \item \textbf{Absolute zero:} Temperature at which there is no molecular motion
            \item Three main temperature scales:
            \begin{itemize}
                \item Celsius (°C)
                \item Fahrenheit (°F)
                \item Kelvin (K)
            \end{itemize}
        \end{itemize}

        \column{0.4\textwidth}
        \begin{center}
            \alert{[Thermometer scales diagram showing comparison of the three temperature scales]}
        \end{center}
    \end{columns}
\end{frame}

\begin{frame}

\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{comparison-three-temperature-scales-vector-16434650-2940992563.jpg}
\end{figure}
\end{frame}


\begin{frame}
    \frametitle{Temperature Scales and Conversion}
    \begin{block}{Temperature Conversion Formulas}
        \begin{align*}
            T_{\text{°F}} &= \frac{9}{5}T_{\text{°C}} + 32 \\
            T_{\text{°C}} &= \frac{5}{9}(T_{\text{°F}} - 32) \\
            T_{\text{K}} &= T_{\text{°C}} + 273.15 \\
            T_{\text{°C}} &= T_{\text{K}} - 273.15
        \end{align*}
    \end{block}

    \begin{exampleblock}{Examples}
        \begin{itemize}
            \item Room temperature: $20\text{°C} = 68\text{°F} = 293.15\text{ K}$
            \item Freezing point of water: $0\text{°C} = 32\text{°F} = 273.15\text{ K}$
            \item Absolute zero: $-273.15\text{°C} = -459.67\text{°F} = 0\text{ K}$
        \end{itemize}
    \end{exampleblock}
\end{frame}

\section{Heat, Specific Heat, and Heat Transfer}

\begin{frame}
    \frametitle{Heat and Specific Heat}
    \begin{block}{Definitions}
        \begin{itemize}
            \item \textbf{Heat (Q):} Thermal energy transferred due to a temperature difference
            \item \textbf{Specific heat (c):} Amount of heat needed to raise the temperature of 1 kg of a substance by 1°C
        \end{itemize}
    \end{block}

    \begin{alertblock}{Heat Transfer Equation}
        \begin{align*}
            Q = mc\Delta T
        \end{align*}
        where:
        \begin{itemize}
            \item $Q$ = heat transferred (J)
            \item $m$ = mass (kg)
            \item $c$ = specific heat (J/kg·°C)
            \item $\Delta T$ = change in temperature (°C or K)
        \end{itemize}
    \end{alertblock}
\end{frame}

\begin{frame}
    \frametitle{Specific Heat of Common Materials}
    \begin{center}
        \begin{tabular}{|l|c|}
            \hline
            \textbf{Material} & \textbf{Specific Heat (J/kg·°C)} \\
            \hline
            Water & 4,186 \\
            \hline
            Ice (at 0°C) & 2,090 \\
            \hline
            Steam (at 100°C) & 2,010 \\
            \hline
            Aluminum & 900 \\
            \hline
            Copper & 385 \\
            \hline
            Gold & 129 \\
            \hline
            Wood & $\approx$ 1,700 \\
            \hline
        \end{tabular}
    \end{center}

    \begin{block}{Note}
        Water has an unusually high specific heat, which is why bodies of water moderate climate.
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Heat Transfer Methods}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{itemize}
            \item \textbf{Conduction:} Transfer between objects in direct contact
            \begin{itemize}
                \item Metals are good conductors
                \item Wood and air are poor conductors (insulators)
            \end{itemize}
            \item \textbf{Convection:} Transfer by movement of mass
            \begin{itemize}
                \item Ocean currents, boiling water, air movement
            \end{itemize}
            \item \textbf{Radiation:} Transfer by electromagnetic waves
            \begin{itemize}
                \item Requires no medium (works in vacuum)
                \item How the Sun's energy reaches Earth
            \end{itemize}
        \end{itemize}

        \column{0.4\textwidth}
        \begin{center}
            \alert{[Diagram showing the three heat transfer mechanisms]}
        \end{center}
    \end{columns}

    \end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys11-thermo-heat-transfer-mechanisms.jpg}
\end{figure}

\end{frame}



\section{Phase Change and Latent Heat}

\begin{frame}
    \frametitle{Phases of Matter}
    \begin{columns}
        \column{0.55\textwidth}
        \begin{itemize}
            \item Four distinct phases:
            \begin{itemize}
                \item \textbf{Solid:} Particles in fixed positions, vibrating
                \item \textbf{Liquid:} Particles close together but can move around
                \item \textbf{Gas:} Particles far apart, moving freely
                \item \textbf{Plasma:} Ionized gas (very high energy)
            \end{itemize}
            \item Gas is the most energetic state
            \item Solid is the least energetic state
        \end{itemize}

        \column{0.45\textwidth}
        \begin{center}
            \alert{[Phase transition diagram showing the four states of matter and the energy relationships between them]}
        \end{center}
    \end{columns}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys11-thermo-phases-of-matter.jpg}
\end{figure}
\end{frame}




\begin{frame}
    \frametitle{Phase Changes}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item \textbf{Melting:} Solid → Liquid
            \item \textbf{Freezing:} Liquid → Solid
            \item \textbf{Vaporization:} Liquid → Gas
            \item \textbf{Condensation:} Gas → Liquid
            \item \textbf{Sublimation:} Solid → Gas
            \item \textbf{Deposition:} Gas → Solid
        \end{itemize}

        \column{0.5\textwidth}
        \begin{block}{Important Points}
            \begin{itemize}
                \item Phase changes occur at fixed temperatures
                \item No temperature change during phase change
                \item Energy breaks bonds between particles
                \item Increases potential energy, not kinetic energy
            \end{itemize}
        \end{block}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Latent Heat}
    \begin{block}{Definition}
        \textbf{Latent heat:} The energy required to change the phase of a substance without changing its temperature
    \end{block}

    \begin{alertblock}{Heat Transfer Equations for Phase Changes}
        \begin{align*}
            Q_{\text{melting/freezing}} &= mL_f \\
            Q_{\text{vaporization/condensation}} &= mL_v
        \end{align*}
        where:
        \begin{itemize}
            \item $Q$ = heat transferred (J)
            \item $m$ = mass (kg)
            \item $L_f$ = latent heat of fusion (J/kg)
            \item $L_v$ = latent heat of vaporization (J/kg)
        \end{itemize}
    \end{alertblock}
\end{frame}

\begin{frame}
    \frametitle{Latent Heat Values}
    \begin{center}
        \begin{tabular}{|l|c|c|}
            \hline
            \textbf{Substance} & \textbf{Latent Heat of Fusion (kJ/kg)} & \textbf{Latent Heat of Vaporization (kJ/kg)} \\
            \hline
            Water & 334 & 2,260 \\
            \hline
            Aluminum & 380 & 11,400 \\
            \hline
            Gold & 64.5 & 1,580 \\
            \hline
            Mercury & 11.8 & 296 \\
            \hline
            Tungsten & 184 & 4,810 \\
            \hline
        \end{tabular}
    \end{center}

    \begin{block}{Note}
        During phase changes, the temperature remains constant while energy is being added or removed.
    \end{block}
\end{frame}

\section{Examples and Applications}

\begin{frame}
    \frametitle{"I do" Example}
    \begin{block}{Problem}
        How much energy would it take to heat 1.00 kg of ice at 0°C to water at 15.0°C?
    \end{block}
    \end{frame}

\begin{frame}
    \begin{exampleblock}{Solution}
        \begin{enumerate}
            \item Energy to melt ice at 0°C to water at 0°C:
            \begin{align*}
                Q_1 &= mL_f = 1.00 \text{ kg} \times 334 \text{ kJ/kg} = 334 \text{ kJ}
            \end{align*}

            \item Energy to heat water from 0°C to 15.0°C:
            \begin{align*}
                Q_2 &= mc\Delta T\\
                &= 1.00 \text{ kg} \times 4,186 \text{ J/(kg·°C)} \times 15.0 \text{ °C}\\
                &= 62,790 \text{ J} = 62.8 \text{ kJ}
            \end{align*}

            \item Total energy required:
            \begin{align*}
                Q_{\text{total}} &= Q_1 + Q_2 = 334 \text{ kJ} + 62.8 \text{ kJ} = 397 \text{ kJ}
            \end{align*}
        \end{enumerate}
    \end{exampleblock}
\end{frame}

\begin{frame}
    \frametitle{"We do" Example}
    \begin{block}{Problem}
        Ice cubes are used to chill a soda with a mass of 0.250 kg at 15.0°C. The ice is at 0°C, and the total mass of the ice cubes is 0.020 kg. Assume that the soda is kept in a foam container so that heat loss can be ignored, and that the soda has the same specific heat as water. Find the final temperature when all ice has melted.
    \end{block}

    \begin{exampleblock}{Solution Steps}
        \begin{enumerate}
            \item Heat lost by soda = Heat gained by ice
            \item Heat lost by soda: $Q_{\text{soda}} = m_{\text{soda}}c_{\text{water}}(T_f - T_i)$
            \item Heat gained by ice: $Q_{\text{ice}} = m_{\text{ice}}L_f + m_{\text{ice}}c_{\text{water}}(T_f - 0\text{°C})$
            \item Set $Q_{\text{soda}} = Q_{\text{ice}}$ and solve for $T_f$
            \item $T_f = 9.03\text{°C}$
        \end{enumerate}
    \end{exampleblock}

\end{frame}

\begin{frame}
    \frametitle{"You do" Example}
    \begin{block}{Problem}
        A certain quantity of water is given 4.0 kJ of heat. This raises its temperature by 30.0°F. What is the mass of the water in grams?
    \end{block}

    \begin{alertblock}{Hints}
        \begin{itemize}
            \item Use the equation $Q = mc\Delta T$
            \item Remember to convert temperature change from °F to °C
            \item The specific heat of water is 4,186 J/(kg·°C)
        \end{itemize}
    \end{alertblock}

    Take some time to work this out. Then we'll discuss the solution.

    \pause

    \begin{exampleblock}{Answer}
        The mass of water is 57 g.
    \end{exampleblock}
\end{frame}

\section{Summary}

\begin{frame}
    \frametitle{Key Equations}
    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Temperature Conversions:}
        \begin{align*}
            T_{\text{°F}} &= \frac{9}{5}T_{\text{°C}} + 32 \\
            T_{\text{°C}} &= \frac{5}{9}(T_{\text{°F}} - 32) \\
            T_{\text{K}} &= T_{\text{°C}} + 273.15
        \end{align*}

        \column{0.5\textwidth}
        \textbf{Heat Transfer:}
        \begin{align*}
            Q &= mc\Delta T \\
            Q_{\text{melting/freezing}} &= mL_f \\
            Q_{\text{vaporization/condensation}} &= mL_v
        \end{align*}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Summary}
    \begin{block}{Temperature and Thermal Energy}
        \begin{itemize}
            \item Temperature relates to average kinetic energy of particles
            \item Three main scales: Celsius, Fahrenheit, Kelvin
            \item Absolute zero: no molecular motion
        \end{itemize}
    \end{block}

    \begin{block}{Heat, Specific Heat, and Heat Transfer}
        \begin{itemize}
            \item Heat is energy transfer due to temperature difference
            \item $Q = mc\Delta T$ relates heat, mass, specific heat, and temperature change
            \item Heat transfer methods: conduction, convection, radiation
        \end{itemize}
    \end{block}

    \begin{block}{Phase Change and Latent Heat}
        \begin{itemize}
            \item Four phases: solid, liquid, gas, plasma
            \item Phase changes occur at constant temperature
            \item Heat added during melting/vaporization, released during freezing/condensation
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Thank You!}
    \begin{center}
        \Huge{Questions?}

        \vspace{1cm}
        \normalsize
        Remember to review the key equations and concepts for the upcoming quiz!
    \end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch06_slides_circular-motion.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Circular and Rotational Motion]{PHYS11 CH:6.1-6.2}
\subtitle{Circular \& Rotational Motion}
\author[Mr. Gullo]{Mr. Gullo}
\date[Oct 2024]{October 2024}

\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Learning Objectives}
By the end of this lesson, you will be able to:
\pause
\begin{itemize}
    \item Calculate angle of rotation ($\Delta\theta$) in radians given arc length and radius
    \pause
    \item Determine angular velocity ($\omega$) from rotational motion data
    \pause
    \item Apply the relationship between tangential velocity and angular velocity
    \pause
    \item Calculate centripetal acceleration for objects in circular motion
    \pause
    \item Determine the centripetal force required to maintain circular motion
    \pause
    \item Solve multi-step problems involving uniform circular motion
\end{itemize}
\end{frame}

\section{Key Concepts and Definitions}

\begin{frame}
\frametitle{Key Terms: Rotational Quantities}
\pause
\textbf{Angle of Rotation} ($\Delta \theta$):
\begin{itemize}
    \item Angular displacement
    \item Measured in radians (rad)
    \item One complete circle = $2\pi$ rad = 360°
\end{itemize}
\pause

\textbf{Arc Length} ($\Delta s$):
\begin{itemize}
    \item Distance traveled along circular path
    \item Related to angle and radius
\end{itemize}
\pause

\textbf{Radius of Curvature} ($r$):
\begin{itemize}
    \item Distance from center to object
    \item Determines size of circular path
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Visualizing Rotational Motion}
\textbf{Understanding the relationship between arc length, angle, and radius:}
\pause
\begin{itemize}
    \item An object moves along a circular path
    \pause
    \item The arc length ($\Delta s$) is the distance it travels
    \pause
    \item The angle ($\Delta\theta$) measures how far it rotates
    \pause
    \item The radius ($r$) determines the size of the circle
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Rotational Motion Diagram}
\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{Screenshot 2024-11-21 125544.png}
    \caption{Arc length, angle, and radius relationship}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Key Terms: Angular Velocity}
\pause
\textbf{Angular Velocity} ($\omega$):
\begin{itemize}
    \item Rate of change of angle with time
    \pause
    \item Units: radians per second (rad/s)
    \pause
    \item Can also be expressed in revolutions per minute (rpm)
    \pause
    \item Describes how fast something rotates
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Understanding Angular Velocity}
\textbf{Before we see the equation:}
\pause
\begin{itemize}
    \item Angular velocity tells us rotation speed
    \pause
    \item Similar to linear velocity, but for rotation
    \pause
    \item Larger $\omega$ means faster spinning
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Angular Velocity Visualization}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.6\linewidth]{Screenshot 2024-11-21 125846.png}
    \caption{Angular velocity definition}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Linear vs Angular Velocity}
\begin{figure}
    \centering
    \includegraphics[width=0.65\linewidth]{Screenshot 2024-11-21 132156.png}
    \caption{Connection between linear and angular motion}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Key Terms: Centripetal Quantities}
\pause
\textbf{Centripetal Acceleration} ($a_c$):
\begin{itemize}
    \item Acceleration directed toward center of circle
    \pause
    \item Changes velocity direction, not speed
    \pause
    \item Always perpendicular to velocity
\end{itemize}
\pause

\textbf{Centripetal Force} ($F_c$):
\begin{itemize}
    \item Net force causing circular motion
    \pause
    \item Points toward center of circle
    \pause
    \item Without it, object moves in straight line
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Understanding Centripetal Force}
\textbf{Key concept:}
\pause
\begin{itemize}
    \item Objects naturally move in straight lines (Newton's 1st Law)
    \pause
    \item To move in a circle requires constant inward force
    \pause
    \item This inward force is the centripetal force
    \pause
    \item Examples: tension in string, friction on tires, gravity
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Centripetal Force Visualization}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{Screenshot 2024-11-21 130344.png}
    \caption{Centripetal acceleration and force directions}
\end{figure}
\end{frame}

\section{Misconceptions}

\begin{frame}
\frametitle{The Fictitious Centrifugal Force}

\begin{columns}[T]
\begin{column}{0.6\textwidth}
\textbf{What is centrifugal "force"?}
\pause
\begin{itemize}
    \item Not a real force!
    \pause
    \item Appears in rotating reference frames
    \pause
    \item Feels like being "thrown outward"
\end{itemize}

\pause
\textbf{Examples in daily life:}
\begin{itemize}
    \item Car turning corner
    \pause
    \item Tea leaves gathering in cup center
    \pause
    \item Clothes in washing machine
\end{itemize}
\end{column}

\begin{column}{0.4\textwidth}
\begin{tikzpicture}[scale=0.8]
    \draw[thick] (0,0) circle (2cm);
    \fill[red] (2,0) circle (0.2cm);
    \draw[->,thick,blue] (2,0) -- (2,1) node[right] {$\vec{v}$};
    \draw[->,thick,red,dashed] (2,0) -- (3,0) node[right] {$F_{fict}$};
    \draw[->,thick,green] (2,0) -- (1,0) node[left] {$F_c$};
    \fill (0,0) circle (0.1cm);
    \draw[->] (1,1.5) arc (45:90:1.5cm);
\end{tikzpicture}
\end{column}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Why Centrifugal Force Isn't Real}
\textbf{Remember:}
\pause
\begin{itemize}
    \item Objects want straight-line motion (inertia)
    \pause
    \item What feels like "outward force" is your body resisting direction change
    \pause
    \item Real force is centripetal (inward), causing circular path
    \pause
    \item No outward force actually exists in inertial reference frame
\end{itemize}
\pause

\vspace{0.5cm}
\small{\url{https://en.wikipedia.org/wiki/Centrifugal_force}}
\end{frame}

\section{Essential Equations}

\begin{frame}
\frametitle{Important Equations}
\pause
\begin{align*}
\text{Angle of Rotation:} & \quad \Delta \theta = \frac{\Delta s}{r} \quad \text{(rad)} \\[0.8em]
\pause
\text{Angular Velocity:} & \quad \omega = \frac{\Delta \theta}{\Delta t} \quad \text{(rad/s)} \\[0.8em]
\pause
\text{Tangential Velocity:} & \quad v = r\omega \quad \text{(m/s)} \\[0.8em]
\pause
\text{Centripetal Acceleration:} & \quad a_c = \frac{v^2}{r} = r\omega^2 \quad \text{(m/s}^2\text{)} \\[0.8em]
\pause
\text{Centripetal Force:} & \quad F_c = \frac{mv^2}{r} = mr\omega^2 \quad \text{(N)}
\end{align*}
\end{frame}

\section{I Do Example}

\begin{frame}
\frametitle{I Do: Problem Statement}
\textbf{Problem:}

A car drives around a circular track of radius 100 m at constant speed of 20 m/s.
\begin{enumerate}
    \item Calculate the centripetal acceleration
    \item Find the centripetal force if car mass is 1500 kg
\end{enumerate}
\end{frame}

\begin{frame}
\frametitle{I Do: Part 1 - G and U}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{G - Givens}
\begin{itemize}
    \item $r = 100$ m
    \item $v = 20$ m/s
    \item $m = 1500$ kg
\end{itemize}

\column{0.48\textwidth}
\textbf{U - Unknown}
\begin{itemize}
    \item Part 1: $a_c = ?$
    \item Part 2: $F_c = ?$
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I Do: Part 1 - E}
\textbf{E - Equation}
\begin{itemize}
    \item Need centripetal acceleration
    \item Use: $a_c = \frac{v^2}{r}$
    \item Already solved for $a_c$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{I Do: Part 1 - S and S}
\textbf{S - Substitute}
\begin{itemize}
    \item $a_c = \frac{(20 \text{ m/s})^2}{100 \text{ m}}$
\end{itemize}

\textbf{S - Solve}
\begin{itemize}
    \item $a_c = \frac{400 \text{ m}^2\text{/s}^2}{100 \text{ m}}$
    \item $a_c = 4$ m/s$^2$
    \item \boxed{a_c = 4 \text{ m/s}^2}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{I Do: Part 2 - E}
\textbf{E - Equation}
\begin{itemize}
    \item Need centripetal force
    \item Use: $F_c = ma_c$
    \item Already solved for $F_c$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{I Do: Part 2 - S and S}
\textbf{S - Substitute}
\begin{itemize}
    \item $F_c = (1500 \text{ kg})(4 \text{ m/s}^2)$
\end{itemize}

\textbf{S - Solve}
\begin{itemize}
    \item $F_c = 6000$ kg·m/s$^2$
    \item $F_c = 6000$ N
    \item \boxed{F_c = 6000 \text{ N}}
\end{itemize}
\end{frame}

\section{We Do Example}

\begin{frame}
\frametitle{We Do: Problem Statement}
\textbf{Let's solve together:}

A CD spins at 300 rpm (revolutions per minute).
\begin{enumerate}
    \item Convert rpm to angular velocity in rad/s
    \item Calculate tangential velocity at $r = 6$ cm
\end{enumerate}
\end{frame}

\begin{frame}
\frametitle{We Do: Part 1 Setup}
\textbf{What do we know?}
\pause
\begin{itemize}
    \item Given: 300 rpm
    \pause
    \item Unknown: $\omega$ in rad/s
    \pause
    \item Need conversion factors
\end{itemize}
\pause

\textbf{Conversion factors needed:}
\begin{itemize}
    \item 1 revolution = $2\pi$ radians
    \item 1 minute = 60 seconds
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{We Do: Part 1 Solution}
\textbf{Your turn: Set up conversion}
\pause

\[ \omega = 300 \frac{\text{rev}}{\text{min}} \times \frac{2\pi \text{ rad}}{1 \text{ rev}} \times \frac{1 \text{ min}}{60 \text{ s}} \]
\pause

\textbf{Calculate:}
\[ \omega = \frac{300 \times 2\pi}{60} = 31.4 \text{ rad/s} \]
\pause

\[\boxed{\omega = 31.4 \text{ rad/s}}\]
\end{frame}

\begin{frame}
\frametitle{We Do: Part 2 Setup}
\textbf{Now find tangential velocity:}
\pause
\begin{itemize}
    \item Given: $r = 6$ cm $= 0.06$ m, $\omega = 31.4$ rad/s
    \pause
    \item Unknown: $v = ?$
    \pause
    \item Equation: $v = r\omega$
\end{itemize}
\pause

\textbf{Your turn: Calculate}
\end{frame}

\begin{frame}
\frametitle{We Do: Part 2 Solution}
\textbf{Substitute and solve:}
\pause

\[ v = r\omega = (0.06 \text{ m})(31.4 \text{ rad/s}) \]
\pause

\[ v = 1.88 \text{ m/s} \]
\pause

\[\boxed{v = 1.88 \text{ m/s}}\]
\end{frame}

\section{You Do Example}

\begin{frame}
\frametitle{You Do: Practice Problem}
\textbf{Solve independently:}

A ball attached to string is swung in horizontal circle with radius 0.5 m. Ball makes one complete revolution in 1.2 seconds.

\textbf{Find:}
\begin{enumerate}
    \item Angular velocity
    \item Centripetal acceleration
    \item Tension in string if ball mass is 0.2 kg
\end{enumerate}

\vspace{0.5cm}
\textbf{Hint:} Use GUESS method. Start with what you know!
\end{frame}

\section{Summary}

\begin{frame}
\frametitle{Summary}
\textbf{Key takeaways:}
\pause
\begin{itemize}
    \item Circular motion requires centripetal force directed toward center
    \pause
    \item $a_c$ and $F_c$ always point inward, never outward
    \pause
    \item Angular quantities ($\theta$, $\omega$) convert to linear ($s$, $v$) using radius
    \pause
    \item Uniform circular motion: constant speed, changing velocity direction
    \pause
    \item Centrifugal "force" is not real - it's inertia resisting direction change
    \pause
    \item Use GUESS method for systematic problem solving
\end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch03_Acceleration-Kinematics.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../latex-beamer/shared/templates/ds9_theme}


% Title page configuration
\title[Acceleration and Kinematics]{PHYS11 CH:3.1 and 3.2}
\subtitle{Understanding Acceleration and the Kinematic Equations}
\author[Mr. Gullo]{Mr. Gullo}
\date[Sept 2025]{September 12, 2025}

\begin{document}
\frame{\titlepage}

\begin{frame}
\frametitle{Learning Objectives}
By the end of this lesson, you will be able to:
\pause
\begin{itemize}
    \item Explain acceleration and determine its direction and magnitude in one dimension.
    \pause
    \item Analyze motion in one dimension using kinematic equations.
    \pause
    \item Explain the kinematic equations related to acceleration and illustrate them with graphs.
    \pause
    \item Apply kinematic equations and related graphs to solve problems involving acceleration.
\end{itemize}
\end{frame}

\section{Defining Acceleration}

\begin{frame}
\frametitle{Key Concepts: What is Acceleration?}
\begin{block}{Definition}
    Acceleration is the rate of change of \textbf{velocity}. It is a measure of how quickly velocity changes.
\end{block}
\pause
\begin{itemize}
    \item \textbf{Vector Quantity:} Acceleration has both magnitude (a size) and direction.
    \pause
    \item \textbf{Units:} The SI unit for acceleration is meters per second squared ($\text{m/s}^2$).
    \pause
    \item \textbf{Average Acceleration Formula:}
    \[ \bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_0}{t_f - t_0} \]
    Where $v_f$ is the final velocity and $v_0$ is the initial velocity.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Key Concepts: Direction of Acceleration}
The direction of acceleration determines if an object is speeding up or slowing down.
\pause
\begin{columns}[T]
    \column{0.48\textwidth}
    \begin{alertblock}{Speeding Up}
        The acceleration vector points in the \textbf{same direction} as the velocity vector.
    \end{alertblock}

    \column{0.48\textwidth}
    \begin{alertblock}{Slowing Down}
        The acceleration vector points in the \textbf{opposite direction} of the velocity vector. This is often called \textit{deceleration}.
    \end{alertblock}
\end{columns}
\pause
\begin{block}{Important Note}
    Negative acceleration does \textit{not} automatically mean slowing down.
    \begin{itemize}
        \item If velocity is negative and acceleration is negative, the object is \textbf{speeding up} in the negative direction!
    \end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Context: Visualizing Acceleration Vectors}
To better understand how acceleration affects motion, we can visualize the velocity ($\vec{v}$) and acceleration ($\vec{a}$) vectors for a moving object.
\pause
\begin{itemize}
    \item When a car speeds up, its velocity increases. The acceleration vector points in the same direction as the velocity.
    \pause
    \item When the car slows down, its velocity decreases. The acceleration vector points opposite to the velocity.
\end{itemize}
\pause
The next slide shows a diagram of this concept.
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Acceleration Vectors}
\begin{alertblock}{[Diagram based on Figure 3.2]}
A diagram showing a car in two scenarios:
\begin{itemize}
    \item \textbf{(a) Speeding Up:} A velocity vector $\vec{v}$ points to the right. A smaller acceleration vector $\vec{a}$ also points to the right, in the same direction.
    \pause
    \item \textbf{(b) Slowing Down:} A velocity vector $\vec{v}$ points to the right. A smaller acceleration vector $\vec{a}$ points to the left, in the opposite direction.
\end{itemize}
This visual shows that the relative direction of acceleration and velocity determines the change in speed.
\end{alertblock}
\end{frame}

\section{Kinematic Equations for Constant Acceleration}

\begin{frame}
\frametitle{Essential Equations: The Kinematics}
These five equations describe motion for an object moving with \textbf{constant acceleration}. They are the main tools for solving motion problems.
\pause
\begin{enumerate}
    \item $d = d_0 + \bar{v}t$ \quad (when acceleration is zero)
    \pause
    \item $\bar{v} = \frac{v_0 + v_f}{2}$
    \pause
    \item $v_f = v_0 + at$
    \pause
    \item $d = d_0 + v_0 t + \frac{1}{2}at^2$
    \pause
    \item $v_f^2 = v_0^2 + 2a(d - d_0)$
\end{enumerate}
\pause
\begin{block}{Variables}
\begin{tabular}{ll}
    $d$ & final position (m) \\
    $d_0$ & initial position (m) \\
    $v_f$ & final velocity (m/s) \\
\end{tabular}
\quad
\begin{tabular}{ll}
    $v_0$ & initial velocity (m/s) \\
    $a$ & constant acceleration (m/s$^2$) \\
    $t$ & time (s) \\
\end{tabular}
\end{block}
\end{frame}

\section{Graphical Analysis of Motion}

\begin{frame}
\frametitle{Context: Graphs of Motion Under Gravity}
Let's consider an object thrown straight up, which then falls back down. Its motion is governed by the constant acceleration of gravity, $g = -9.80 \, \text{m/s}^2$.
\pause
\begin{itemize}
    \item How will its \textbf{position} change over time?
    \pause
    \item How will its \textbf{velocity} change over time?
    \pause
    \item What will its \textbf{acceleration} look like over time?
\end{itemize}
\pause
The next slide shows the three graphs that describe this motion.
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Motion Under Gravity}
\begin{alertblock}{[Graphs based on Figure 3.13]}
Three graphs showing the motion of a rock thrown upward:
\begin{itemize}
    \item \textbf{Position vs. Time:} An inverted parabola. The rock goes up, reaches a peak, and comes back down.
    \pause
    \item \textbf{Velocity vs. Time:} A straight line with a negative slope. The velocity starts positive, decreases to zero at the peak, and becomes negative as it falls. The slope of this line is the acceleration due to gravity.
    \pause
    \item \textbf{Acceleration vs. Time:} A horizontal line at $-9.80 \, \text{m/s}^2$. This shows that the acceleration is constant throughout the motion.
\end{itemize}
\end{alertblock}
\end{frame}

\section{Problem Solving with GUESS}

\begin{frame}
\frametitle{I Do: Accelerating Subway Train - Problem Setup}
\framesubtitle{Problem based on Ch. 3, page 6}
\begin{block}{Problem}
A subway train accelerates from rest to 30.0 km/h in 20.0 s. What is its average acceleration during that time interval?
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
    \item $v_0 = 0 \, \text{m/s}$ (from rest)
    \item $v_f = 30.0 \, \text{km/h}$
    \item $\Delta t = 20.0 \, \text{s}$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
    \item $\bar{a} = ?$ (in m/s$^2$)
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I Do: Accelerating Subway Train - Equation}
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
    \item $v_0 = 0 \, \text{m/s}$
    \item $v_f = 30.0 \, \text{km/h}$
    \item $\Delta t = 20.0 \, \text{s}$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
    \item $\bar{a} = ?$ (in m/s$^2$)
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{E - Equation}
\begin{itemize}
    \item Select: $\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_0}{\Delta t}$
    \item No rearrangement needed.
    \item \alert{First, must convert units!}
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I Do: Accelerating Subway Train - Solution}
\begin{block}{S - Substitute (with unit conversion)}
\begin{itemize}
    \item Convert km/h to m/s:
    \[ v_f = 30.0 \, \frac{\text{km}}{\text{h}} \times \frac{1000 \, \text{m}}{1 \, \text{km}} \times \frac{1 \, \text{h}}{3600 \, \text{s}} = 8.333 \, \text{m/s} \]
    \pause
    \item Plug values into the equation:
    \[ \bar{a} = \frac{8.333 \, \text{m/s} - 0 \, \text{m/s}}{20.0 \, \text{s}} \]
\end{itemize}
\end{block}
\pause
\begin{block}{S - Solve}
\begin{itemize}
    \item Calculate the final answer:
    \[ \bar{a} = \frac{8.333 \, \text{m/s}}{20.0 \, \text{s}} = 0.41665 \, \text{m/s}^2 \]
    \pause
    \item Apply sig figs (3 sig figs from givens):
    \item \boxed{\bar{a} = 0.417 \, \text{m/s}^2}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{We Do: Acceleration of a Dragster}
\framesubtitle{Problem based on Ch. 3, page 22}
\begin{block}{Problem}
A dragster accelerates from rest at a constant $26.0 \, \text{m/s}^2$ for a quarter mile (402 m). What is the final velocity of the dragster?
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
    \item $v_0 = 0 \, \text{m/s}$ (from rest)
    \item $a = 26.0 \, \text{m/s}^2$
    \item $\Delta d = 402 \, \text{m}$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
    \item $v_f = ?$
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{alertblock}{Question: Which kinematic equation should we use? (Hint: We don't know time)}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{We Do: Acceleration of a Dragster - Solution}
\begin{block}{E - Equation}
The best equation is the one without time ($t$):
\[ v_f^2 = v_0^2 + 2a\Delta d \]
\pause
This equation is almost ready. How do we isolate $v_f$?
\begin{itemize}
    \item \alert{Take the square root of both sides!}
    \[ v_f = \sqrt{v_0^2 + 2a\Delta d} \]
\end{itemize}
\end{block}
\pause
\begin{block}{S - Substitute}
Let's plug in the values:
\[ v_f = \sqrt{(0 \, \text{m/s})^2 + 2(26.0 \, \text{m/s}^2)(402 \, \text{m})} \]
\end{block}
\pause
\begin{block}{S - Solve}
What is the final velocity?
\[ v_f = \sqrt{20904 \, \text{m}^2/\text{s}^2} = \ ? \]
\pause
\boxed{v_f \approx 145 \, \text{m/s}}
\end{block}
\end{frame}

\begin{frame}
\frametitle{You Do: Olympic Sprinter}
\framesubtitle{Problem based on Ch. 3, Problem 7, page 24}
\begin{block}{Problem}
An Olympic-class sprinter starts a race with an acceleration of $4.50 \, \text{m/s}^2$. Assuming she can maintain that acceleration, what is her speed 2.40 s later?
\end{block}
\vfill
\begin{alertblock}{Your Turn}
Use the GUESS method to solve this problem on your own.
\begin{itemize}
    \item What are the Givens? (Note: "starts a race" implies $v_0 = 0$)
    \item What is the Unknown?
    \item Which Equation will you use?
    \item Substitute and Solve for the final answer.
\end{itemize}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Reading Homework}
To ensure you have a strong foundation for the concepts we discussed today, please review the sections from Chapter 3.
\end{frame}

\begin{frame}
\frametitle{Summary}
\begin{itemize}
    \item \textbf{Acceleration} is the rate of change of velocity ($\vec{a} = \Delta\vec{v} / \Delta t$) and is a vector.
    \pause
    \item The direction of acceleration relative to velocity determines if an object \textbf{speeds up} (same direction) or \textbf{slows down} (opposite directions).
    \pause
    \item For motion with \textbf{constant acceleration}, we use the kinematic equations to solve for unknown quantities like displacement, velocity, or time.
    \pause
    \item \textbf{Motion graphs} provide a powerful visual tool:
    \begin{itemize}
        \item The slope of a velocity-time graph is \alert{acceleration}.
        \item The area under a velocity-time graph is \alert{displacement}.
    \end{itemize}
\end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch05-4_slides_friction.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Friction and Inclined Planes]{PHYS11 CH:5.4}
\subtitle{Static and Kinetic Friction}
\author[Mr. Gullo]{Mr. Gullo}
\date[Nov 2024]{November 2024}

\begin{document}

\frame{\titlepage}

\section{Introduction to Friction}

\begin{frame}
\frametitle{Learning Objectives}
By the end of this lesson, you will be able to:
\pause
\begin{itemize}
    \item Define friction and distinguish between static and kinetic friction
    \pause
    \item Apply friction formulas: $f_s \leq \mu_s N$ and $f_k = \mu_k N$
    \pause
    \item Resolve weight into components on inclined planes
    \pause
    \item Solve problems involving friction on horizontal and inclined surfaces
    \pause
    \item Use free body diagrams with rotated coordinate systems
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{What is Friction?}
\begin{block}{Definition}
\textbf{Friction} is a force that opposes motion or attempted motion between surfaces in contact.
\end{block}
\pause

\vspace{1em}
\textbf{Key characteristics:}
\begin{itemize}
    \item Acts parallel to contact surface
    \pause
    \item Direction: opposes motion (or attempted motion)
    \pause
    \item Magnitude: depends on surface properties and normal force
    \pause
    \item \textbf{Surprising fact}: Independent of contact area!
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Types of Friction}
\begin{itemize}
    \item \textbf{Static Friction} ($f_s$): Acts on objects at rest
    \begin{itemize}
        \item Variable force: adjusts to prevent motion
        \item Has maximum value: $f_{s,max} = \mu_s N$
    \end{itemize}
    \pause

    \vspace{0.5em}
    \item \textbf{Kinetic Friction} ($f_k$): Acts on objects in motion
    \begin{itemize}
        \item Constant force: $f_k = \mu_k N$
        \item Usually less than maximum static friction
        \item Independent of sliding speed
    \end{itemize}
    \pause

    \vspace{0.5em}
    \item \textbf{Important relationship}: $f_{s,max} > f_k$ (always!)
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Friction Behavior Visualization}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\linewidth]{Screenshot 2024-11-11 110912.png}
\end{figure}

Notice: Static friction increases until maximum, then drops to kinetic friction when motion begins.
\end{frame}

\section{Friction Formulas and Coefficients}

\begin{frame}
\frametitle{Friction Formulas}
\begin{block}{Static Friction}
\[ f_s \leq \mu_s N \]
\textbf{Variables:}
\begin{itemize}
    \item $f_s$ = static friction force (N)
    \item $\mu_s$ = coefficient of static friction (no units)
    \item $N$ = normal force (N)
\end{itemize}
\end{block}
\pause

\begin{block}{Kinetic Friction}
\[ f_k = \mu_k N \]
\textbf{Variables:}
\begin{itemize}
    \item $f_k$ = kinetic friction force (N)
    \item $\mu_k$ = coefficient of kinetic friction (no units)
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Coefficients of Friction - Real Materials}
\begin{table}
\centering
\begin{tabular}{|l|c|c|}
\hline
\textbf{System} & $\mu_s$ & $\mu_k$ \\
\hline
Rubber on dry concrete & 1.0 & 0.7 \\
Wood on wood & 0.5 & 0.3 \\
Steel on steel (dry) & 0.6 & 0.3 \\
Steel on steel (oiled) & 0.05 & 0.03 \\
Ice on ice & 0.1 & 0.03 \\
\hline
\end{tabular}
\end{table}

\pause
\vspace{0.5em}
\textbf{Observations:}
\begin{itemize}
    \item High friction: rubber on concrete (vehicle safety!)
    \pause
    \item Low friction: ice on ice (explains ice skating)
    \pause
    \item Lubrication effect: oil reduces friction by 10x+
\end{itemize}
\end{frame}

\section{Inclined Planes}

\begin{frame}
\frametitle{Why Study Inclined Planes?}
\textbf{Real-world applications:}
\pause
\begin{itemize}
    \item Skiing and snowboarding
    \pause
    \item Vehicle motion on hills
    \pause
    \item Ramps and accessibility
    \pause
    \item Rock slides and avalanches
\end{itemize}

\vspace{1em}
\pause
\textbf{Key challenge:} Weight acts vertically, but motion is along slope. We need to decompose forces!
\end{frame}

\begin{frame}
\frametitle{Forces on an Inclined Plane}
On a slope at angle $\theta$, weight has two components:
\pause

\begin{block}{Parallel Component (down the slope)}
\[ w_\parallel = mg\sin\theta \]
This component causes motion down the slope.
\end{block}
\pause

\begin{block}{Perpendicular Component (into the slope)}
\[ w_\perp = mg\cos\theta \]
This component is balanced by normal force: $N = mg\cos\theta$
\end{block}
\pause

\vspace{0.5em}
\textbf{Note:} Friction acts parallel to surface, opposing motion: $f = \mu N$
\end{frame}

\begin{frame}
\frametitle{Inclined Plane Force Diagram}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\linewidth]{Screenshot 2024-11-11 110923.png}
\end{figure}

Key: Rotate coordinate system to align with slope direction.
\end{frame}

\begin{frame}
\frametitle{Problem Solving Strategy}
\textbf{Step-by-step approach:}

\begin{enumerate}
    \item Draw sketch of physical situation
    \pause
    \item Identify all known and unknown quantities
    \pause
    \item Draw free body diagram with rotated axes
    \pause
    \item Decompose forces into components
    \pause
    \item Apply Newton's second law:
    \begin{itemize}
        \item If no acceleration: $F_{net} = 0$
        \item If accelerating: $F_{net} = ma$
    \end{itemize}
    \pause
    \item Solve algebraically, then substitute values
    \pause
    \item Check answer for reasonableness (units, magnitude, direction)
\end{enumerate}
\end{frame}

\section{Problem Solving with GUESS Method}

\begin{frame}
\frametitle{Example Problem: Skier on a Slope}
\begin{block}{Problem Statement}
A 62 kg skier slides down a snowy slope inclined at 25°. The kinetic friction force is 45.0 N. Find the coefficient of kinetic friction $\mu_k$.
\end{block}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\linewidth]{Screenshot 2024-11-11 110959SansFBD.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Free Body Diagram}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{Screenshot 2024-11-11 110959.png}
\end{figure}

Notice: Axes rotated to align with slope.
\end{frame}

\begin{frame}
\frametitle{Solution: G and U}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{G - Givens}
\begin{itemize}
    \item $m = 62$ kg
    \item $\theta = 25°$
    \item $f_k = 45.0$ N
    \item $g = 9.80$ m/s²
\end{itemize}

\column{0.48\textwidth}
\textbf{U - Unknown}
\begin{itemize}
    \item $\mu_k = ?$
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Solution: E - Equation}
\textbf{E - Equation}

We know: $f_k = \mu_k N$

On incline: $N = mg\cos\theta$

Therefore: $f_k = \mu_k mg\cos\theta$

\textbf{Rearrange for unknown:}
\[ \mu_k = \frac{f_k}{mg\cos\theta} \]
\end{frame}

\begin{frame}
\frametitle{Solution: S - Substitute and Solve}
\textbf{S - Substitute}
\[ \mu_k = \frac{45.0\text{ N}}{(62\text{ kg})(9.80\text{ m/s}^2)\cos(25°)} \]

\pause
\textbf{S - Solve}

First calculate denominator:
\[ N = (62)(9.80)\cos(25°) = 551\text{ N} \]

Then:
\[ \mu_k = \frac{45.0}{551} = 0.082 \]

\vspace{0.5em}
\boxed{\mu_k = 0.082}

\pause
\textbf{Check:} Value is reasonable (between 0 and 1, close to ice on ice).
\end{frame}

\begin{frame}
\frametitle{Example: Acceleration Without Friction}
\begin{block}{Problem - Part A}
What is the skier's acceleration if friction is negligible?
\end{block}

\pause
\textbf{Quick solution:}

Only force down slope: $F = mg\sin\theta$

Apply $F = ma$:
\[ ma = mg\sin\theta \]
\[ a = g\sin\theta \]

\pause
\textbf{Substitute:}
\[ a = (9.80\text{ m/s}^2)\sin(25°) = 4.14\text{ m/s}^2 \]

\boxed{a = 4.14\text{ m/s}^2 \text{ down the slope}}
\end{frame}

\section{Practice Problems}

\begin{frame}
\frametitle{"We Do" Problem: Acceleration with Friction}
\begin{block}{Problem - Part B}
What is the skier's acceleration with 45.0 N friction force?
\end{block}

\pause
\textbf{Setup (together):}

Forces down slope: $F_{down} = mg\sin\theta$

Forces up slope: $F_{up} = f_k$

Net force: $F_{net} = mg\sin\theta - f_k$

\pause
\textbf{You try:} Apply Newton's second law and solve for $a$.

\pause
\textbf{Answer:} $a = 3.39$ m/s² down the slope
\end{frame}

\begin{frame}
\frametitle{"We Do" Solution}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.2\linewidth]{Screenshot 2024-11-11 111003.png}
\end{figure}

\textbf{Complete solution:}
\[ F_{net} = mg\sin\theta - f_k = ma \]
\[ a = g\sin\theta - \frac{f_k}{m} \]
\[ a = (9.80)\sin(25°) - \frac{45.0}{62} \]
\[ a = 4.14 - 0.73 = 3.41\text{ m/s}^2 \]

\textbf{Observation:} Friction reduces acceleration by about 18\%.
\end{frame}

\begin{frame}
\frametitle{"You Do" Problem}
\begin{block}{Independent Practice}
A 5.0 kg wooden block rests on a wooden incline. The coefficient of static friction is $\mu_s = 0.5$.

\vspace{0.5em}
\textbf{Find:} The maximum angle $\theta_{max}$ before the block starts to slide.

\vspace{0.5em}
\textbf{Hint:} At maximum angle, static friction equals its maximum value and net force is zero.
\end{block}

\vspace{1em}
\pause
\textbf{Try this on your own!} Use the GUESS method.
\end{frame}

\section{Summary}

\begin{frame}
\frametitle{Key Takeaways}
\textbf{Friction concepts:}
\begin{itemize}
    \item Static friction: variable, maximum $f_s \leq \mu_s N$
    \pause
    \item Kinetic friction: constant, $f_k = \mu_k N$
    \pause
    \item Always: $\mu_s > \mu_k$ (harder to start than to keep moving)
\end{itemize}

\pause
\vspace{0.5em}
\textbf{Inclined planes:}
\begin{itemize}
    \item Parallel component: $w_\parallel = mg\sin\theta$ (causes motion)
    \pause
    \item Perpendicular component: $w_\perp = mg\cos\theta$ (balanced by $N$)
    \pause
    \item Friction: $f = \mu N = \mu mg\cos\theta$
\end{itemize}

\pause
\vspace{0.5em}
\textbf{Problem solving:} Use rotated coordinate system and GUESS method!
\end{frame}

\begin{frame}
\frametitle{Friction Force vs Applied Force}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.9\linewidth]{Friction-Plot-980x724.png}
\end{figure}

\textbf{Remember:} Static friction increases until maximum, then drops to kinetic friction when motion begins.
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch01-2_GUESS_WrittenProficiency.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

\title[Assessment Tips and Proficiency]{Assessment Strategy and Written Work Proficiency}
\subtitle{Show Clear Thinking on Every Question}
\author[Mr. Gullo]{Mr. Gullo}
\date[2024-25]{2024-25 School Year}

\begin{document}

\frame{\titlepage}

\section{Introduction: Two Types of Assessment}

\begin{frame}{Learning Objectives}
By the end of this presentation, you will be able to:
\begin{itemize}
\item Know the difference between math and thinking questions \pause
\item Use the Written Work Proficiency Scale on all questions \pause
\item Use the G.U.E.S.S. method for math questions \pause
\item Use sketches and diagrams when helpful \pause
\item Show clear, organized thinking \pause
\item Move from Emerging to Extending level
\end{itemize}
\end{frame}

\begin{frame}{Assessment for Learning and Written Work}
\begin{itemize}

\item -The Assessment for Learning category is worth 0 of your grade. It is for practice and feedback only. \pause
\item -On quizzes, you must show your work. If your steps are correct, you can get partial marks even if the final answer is wrong. \pause
\item On unit tests, midterm and final exam, written work will be worth 30 of the score.  \pause Up to three questions specified will be checked for written work.
\end{itemize}
\end{frame}


\section{Method 1: G.U.E.S.S. for Problem-Solving}

\begin{frame}{G.U.E.S.S. Method Review}
For calculation-based questions, use the systematic G.U.E.S.S. approach:

\pause
\vspace{0.5cm}
\begin{flushleft}
\textbf{G} - Givens \& Diagram \pause \\
\textbf{U} - Unknowns \& Plan \pause \\
\textbf{E} - Equations \pause \\
\textbf{S} - Substitute \& Solve \pause \\
\textbf{S} - Solution \& Statement \\
\end{flushleft}

\pause
\vspace{0.5cm}
\textbf{Perfect for:} Questions with numerical values, formulas, and calculations
\end{frame}

\begin{frame}{The Challenge: Two Question Types}
\begin{columns}
\begin{column}{0.5\textwidth}
\begin{block}{Calculation-Based Questions}
\begin{itemize}
\item Require numerical problem-solving \pause
\item Use formulas and equations \pause
\item Show mathematical work \pause
\item \textcolor{ds9blue}{G.U.E.S.S. method applies perfectly}
\end{itemize}
\end{block}
\end{column} \pause
\begin{column}{0.5\textwidth}
\begin{block}{Concept-Focused Questions}
\begin{itemize}
\item Test understanding of principles \pause
\item Require explanation and reasoning \pause
\item No calculations involved \pause
\item \textcolor{ds9blue}{G.U.E.S.S. method can still help organize thinking}
\end{itemize}
\end{block}
\end{column}
\end{columns}

\pause
\vspace{0.5cm}
\textbf{Today's Goal:} Show clear thinking on ALL question types!
\end{frame}



\section{Understanding the Written Work Proficiency Scale}

\begin{frame}{The Four Proficiency Levels}
\begin{block}{Emerging}
\textcolor{ds9red}{Just starting to show your thinking}
\end{block}

\pause
\begin{block}{Developing}
\textcolor{orange}{Getting better at organized thinking}
\end{block}
\end{frame}

\begin{frame}{The Four Proficiency Levels (continued)}
\begin{block}{Proficient}
\textcolor{ds9blue}{Clear, organized thinking shown consistently}
\begin{itemize}
\item Lists all important information clearly \pause
\item Shows logical steps throughout all work \pause
\item Uses units consistently on all work \pause
\item Makes clear, labeled sketches when helpful
\end{itemize}
\end{block}

\pause
\begin{block}{Extending}
\textcolor{ds9blue}{Exceptional clarity and deep thinking}
\begin{itemize}
\item Includes hidden details and assumptions \pause
\item Plans approach before starting \pause
\item Uses units and checks them for accuracy \pause
\item Uses multiple sketches when helpful
\end{itemize}
\end{block}
\end{frame}



\section{What "Showing Your Work" Means}

\begin{frame}{Two Types of Questions}
\begin{columns}
\begin{column}{0.5\textwidth}
\begin{block}{Math Questions}
\begin{itemize}
\item List what you know \pause
\item Include sketch when helpful \pause
\item Show each calculation step \pause
\item Include units \pause
\item Write final answer clearly
\end{itemize}
\end{block}
\end{column} \pause
\begin{column}{0.5\textwidth}
\begin{block}{Thinking Questions}
\begin{itemize}
\item State what question asks \pause
\item Include sketch when helpful \pause
\item Explain your reasoning step-by-step \pause
\item Use science vocabulary \pause
\item Address all parts of question
\end{itemize}
\end{block}
\end{column}
\end{columns}

\pause
\vspace{0.5cm}
\textbf{Key Point:} Both types need organized, clear thinking!
\end{frame}






\section{Proficiency Examples with Real Questions}

\begin{frame}{Example 1: Classical Physics Application}
\textbf{Question:} Can classical physics be used to accurately describe a satellite moving at 7,500 m/s?

\textbf{Options:}
\begin{itemize}
\item[\textbf{A.}] Yes, because the satellite is moving much slower than light speed and is not in a strong gravitational field.
\item[\textbf{B.}] No, because the satellite is moving much slower than light speed and is not in a strong gravitational field.
\item[\textbf{C.}] No, because the satellite is moving much slower than light speed and is in a strong gravitational field.
\item[\textbf{D.}] Yes, because the satellite is moving much slower than light speed and is in a strong gravitational field.
\end{itemize}

\pause
\begin{block}{Emerging Level Response}
A. Yes because it's slow.
\end{block}

\pause
\begin{block}{Developing Level Response}
A. Yes, because 7,500 m/s is much slower than the speed of light so classical physics works.
\end{block}
\end{frame}

\begin{frame}{Example 1: Higher Proficiency Levels}
\begin{block}{Proficient Level Response}
Answer A. Classical physics works for this satellite. The satellite speed is 7,500 m/s, which is much slower than light speed ($3 \times 10^8$ m/s). Also, Earth's gravity is weak, not strong. Both conditions are met for classical physics to work.
\end{block}

\pause
\begin{block}{Extending Level Response}
Answer A. Classical physics applies when two conditions are met: (1) speeds less than 1\% of light speed, and (2) weak gravitational fields. For condition 1: 7,500 m/s ÷ ($3 \times 10^8$ m/s) = 0.0025\% of light speed, well below the 1\% threshold. For condition 2: Earth's gravitational field is weak compared to extreme objects like neutron stars. Options B and C incorrectly conclude "No" despite meeting both conditions. Option D incorrectly describes Earth's gravity as "strong." Only A correctly identifies both conditions are satisfied.
\end{block}
\end{frame}

\begin{frame}{Example 2: Scientific Method}
\textbf{Question:} Which statement is a testable hypothesis about why ants gather in a specific area?

\textbf{Options:}
\begin{itemize}
\item[\textbf{A.}] There may be some food particles lying there.
\item[\textbf{B.}] The worker ants thought it was a nice location.
\item[\textbf{C.}] The worker ants may have to find a spot for the queen to lay eggs.
\item[\textbf{D.}] The worker ants are supposed to group together at a place.
\end{itemize}

\pause
\begin{block}{Emerging Level Response}
A. There may be food particles there.
\end{block}

\pause
\begin{block}{Developing Level Response}
A. There may be food particles there because you can test if there's food there.
\end{block}
\end{frame}

\begin{frame}{Example 2: Higher Proficiency Levels}
\begin{block}{Proficient Level Response}
Answer A: Food particles. A good hypothesis must be testable. We can test for food by looking for it and measuring it. This makes it a good scientific hypothesis.
\end{block}

\pause
\begin{block}{Extending Level Response}
Answer A: Food particles. A testable hypothesis must be both observable and measurable with controlled experiments. Option A allows me to design a test: remove ants, clean the area, place different substances (food vs. non-food), then measure ant response. Options B, C, and D all contain subjective elements: B refers to ant "thoughts," C assumes ant "intentions" for egg-laying, and D implies ants are "supposed" to behave certain ways. These subjective concepts cannot be objectively measured, controlled, or falsified in scientific experiments. Only A meets the empirical criteria for scientific testability.
\end{block}
\end{frame}

\begin{frame}{Example 3: Math Question}
\textbf{Question:} A bathroom scale reads 65 kg with 3\% uncertainty. What is the uncertainty in kg?

\textbf{Options:}
\begin{itemize}
\item[\textbf{A.}] 2 kg
\item[\textbf{B.}] 98 kg
\item[\textbf{C.}] 5 kg
\item[\textbf{D.}] 0 kg
\end{itemize}

\pause
\begin{block}{Proficient Level - G.U.E.S.S. Approach}
\begin{flushleft}
\textbf{G:} Mass = 65 kg, \% uncertainty = 3\% \\
\textbf{U:} Uncertainty in kg \\
\textbf{E:} Uncertainty = (3/100) × 65 kg \\
\textbf{S:} (0.03)(65) = 1.95 kg \\
\textbf{S:} Answer A: 2 kg (rounded appropriately)
\end{flushleft}
\end{block}
\end{frame}

\begin{frame}{Example 3: Extending Level}
\begin{block}{Extending Level - Enhanced G.U.E.S.S. Approach}
\begin{flushleft}
\textbf{G:} Mass = 65 kg, relative uncertainty = 3\% (assuming this is the standard uncertainty) \\
\textbf{U:} Absolute uncertainty in kg, with proper significant figures \\
\textbf{E:} Absolute uncertainty = relative uncertainty × measured value = (3.0/100) × 65 kg \\
\textbf{S:} (0.030)(65) = 1.95 kg \\
\textbf{S:} Answer A: 2.0 kg (rounded to 2 sig figs to match the precision of the 3\% uncertainty)
\end{flushleft}
\textbf{Check:} Answer A is correct. Option B (98 kg) appears to be 65 + 33, likely from adding instead of finding percentage. Option C (5 kg) might result from rounding errors or using 5% instead of 3\%. Option D (0 kg) is impossible since all measurements have uncertainty. Final answer: 65 ± 2 kg, indicating range is 63-67 kg.
\end{block}

\pause
\textbf{Key Point:} Use G.U.E.S.S. method for all math questions!
\end{frame}

\section{Strategic Application Guide}


\begin{frame}{Proficiency Scale Checklist}
\begin{block}{Moving from Developing to Proficient}
\begin{itemize}
\item $\checkmark$ Use G.U.E.S.S. method for math questions consistently \pause
\item $\checkmark$ Show all reasoning steps clearly \pause
\item $\checkmark$ Address all parts of the question \pause
\item $\checkmark$ Use proper physics terminology
\end{itemize}
\end{block}

\pause
\begin{block}{Moving from Proficient to Extending}
\begin{itemize}
\item $\checkmark$ Include implicit information and assumptions \pause
\item $\checkmark$ Explain the "why" behind your reasoning \pause
\item $\checkmark$ Connect to broader physics principles \pause
\item $\checkmark$ Consider alternative approaches or perspectives \pause
\item $\checkmark$ Check your reasoning for consistency
\end{itemize}
\end{block}
\end{frame}

\section{Summary and Final Strategy}

\begin{frame}{Your Assessment Strategy Toolkit}
\begin{block}{Before You Start}
\begin{itemize}
\item Read the question carefully - identify the type \pause
\item Use G.U.E.S.S. method for math questions \pause
\item Plan your response structure
\end{itemize}
\end{block}

\pause
\begin{block}{During Your Response}
\begin{itemize}
\item Follow your chosen method systematically \pause
\item Show all thinking steps clearly \pause
\item Use proper physics language and concepts \pause
\item Connect reasoning to the final answer
\end{itemize}
\end{block}

\pause
\begin{block}{Aiming for Extending}
\begin{itemize}
\item Include hidden assumptions and details \pause
\item Explain the deeper physics principles \pause
\item Check your reasoning multiple ways
\end{itemize}
\end{block}
\end{frame}

\begin{frame}{Final Reminders}
\begin{center}
\Large
\textcolor{ds9blue}{\textbf{Stay Systematic}} \\
\vspace{0.3cm}
\textcolor{ds9gold}{\textbf{Show Your Thinking}} \\
\vspace{0.3cm}
\textcolor{ds9blue}{\textbf{Choose the Right Method}} \\
\vspace{0.3cm}
\textcolor{ds9red}{\textbf{Aim for Understanding}} \\
\end{center}

\vspace{1cm}

\begin{center}
\textbf{Use G.U.E.S.S. for math, clear thinking for concepts!}
\end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch19_slides_circuits.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Electric Circuits]{PHYS11 CH:19.1-19.4}
\subtitle{Ohm's Law, Series \& Parallel Circuits, and Electric Power}
\author[Mr. Gullo]{Mr. Gullo}
\date[May 2025]{May, 2025}

\begin{document}

% Title slide
\begin{frame}
\titlepage
\end{frame}

% Table of contents
\begin{frame}
\frametitle{Outline}
\tableofcontents
\end{frame}

\section{Learning Objectives}

\begin{frame}
\frametitle{Learning Objectives}
By the end of this lesson, you will be able to:
\begin{itemize}
\item State and apply Ohm's law to simple circuits
\item Distinguish between series and parallel circuit configurations
\item Calculate equivalent resistance for resistors in series and parallel
\item Analyze current flow and voltage drops in different circuit configurations
\item Compute electric power dissipation in resistive elements
\end{itemize}
\end{frame}

\section{Ohm's Law}

\begin{frame}
\frametitle{Current and Resistance}
\begin{block}{Electric Current}
Electric current is the rate of charge flow:
\begin{align}
I = \frac{\Delta Q}{\Delta t}
\end{align}
where:
\begin{itemize}
\item $I$ is the current (measured in amperes, A)
\item $\Delta Q$ is the charge that passes (measured in coulombs, C)
\item $\Delta t$ is the time interval (measured in seconds, s)
\end{itemize}
\end{block}

\begin{block}{Definition of Ampere}
\begin{align}
1 \text{ A} = 1 \text{ C/s}
\end{align}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Ohm's Law}
\begin{block}{Ohm's Law Statement}
For ohmic materials, the voltage drop along a path is proportional to the current that runs through the path, with resistance as the constant of proportionality.
\end{block}

\begin{block}{Mathematical Form}
\begin{align}
V = IR
\end{align}
where:
\begin{itemize}
\item $V$ is the voltage drop (measured in volts, V)
\item $I$ is the current (measured in amperes, A)
\item $R$ is the resistance (measured in ohms, $\Omega$)
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Ohm's Law}
\begin{alertblock}{}
\begin{figure}
    \centering
    \includegraphics[width=0.7\linewidth]{phys11-circuits-ohms-law-resistor-graph.png}
\end{figure}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Direct vs. Alternating Current}
\begin{columns}
\column{0.5\textwidth}
\begin{block}{Direct Current (DC)}
\begin{itemize}
\item Constant over time
\item Flows in one direction
\item Example: Batteries
\end{itemize}
\end{block}

\column{0.5\textwidth}
\begin{block}{Alternating Current (AC)}
\begin{itemize}
\item Alternates back and forth over time
\item Changes direction periodically
\item Example: Household electricity
\end{itemize}
\end{block}
\end{columns}

\begin{alertblock}{Current Types Visualization}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-circuits-ac-vs-dc-graph.png}
\end{figure}
\end{alertblock}
\end{frame}

\section{Series Circuits}

\begin{frame}
\frametitle{Series Circuits: Characteristics}
\begin{block}{Definition}
Resistors in series are connected head to tail, forming a single path for current flow.
\end{block}

\begin{columns}
\column{0.6\textwidth}
\begin{block}{Key Properties}
\begin{itemize}
\item Same current flows through all resistors
\item Voltage drop can be different across each resistor
\item Voltage is the same at every point in a given wire
\item Total voltage equals sum of individual voltage drops
\end{itemize}
\end{block}

\column{0.4\textwidth}
\begin{alertblock}{Series Circuit}
\alert{}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-circuits-series-resistors.png}
\end{figure}
\end{alertblock}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Series Circuits: Equivalent Resistance}
\begin{block}{Equivalent Resistance Formula}
For $N$ resistors connected in series:
\begin{align}
R_{\text{equiv}} = R_1 + R_2 + \cdots + R_N
\end{align}
\end{block}

\begin{block}{Interpretation}
\begin{itemize}
\item The equivalent resistance is always greater than any individual resistance
\item Adding resistors in series increases the total resistance
\item Current is limited by the sum of all resistances
\end{itemize}
\end{block}


\end{frame}

\section{Parallel Circuits}

\begin{frame}
\frametitle{Parallel Circuits: Characteristics}
\begin{block}{Definition}
Resistors in parallel provide multiple paths for current flow, with one end of each resistor connected to a common point.
\end{block}

\begin{columns}
\column{0.6\textwidth}
\begin{block}{Key Properties}
\begin{itemize}
\item Same voltage across all resistors
\item Current through each resistor can differ
\item Total current equals sum of individual currents
\item More paths available for current flow
\end{itemize}
\end{block}

\column{0.4\textwidth}
\begin{alertblock}{Parallel Circuit}
\alert{}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-circuits-parallel-resistors.png}
\end{figure}
\end{alertblock}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Parallel Circuits: Equivalent Resistance}
\begin{block}{Equivalent Resistance Formula}
For $N$ resistors connected in parallel:
\begin{align}
\frac{1}{R_{\text{equiv}}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots + \frac{1}{R_N}
\end{align}
\end{block}

\begin{block}{Special Case: Identical Resistors}
For $N$ identical resistors each with resistance $R$ connected in parallel:
\begin{align}
R_{\text{equiv}} = \frac{R}{N}
\end{align}
\end{block}

\begin{block}{Interpretation}
\begin{itemize}
\item The equivalent resistance is always less than the smallest individual resistance
\item Adding resistors in parallel decreases the total resistance
\end{itemize}
\end{block}
\end{frame}

\section{Electric Power}

\begin{frame}
\frametitle{Electric Power: Basic Concept}
\begin{block}{Definition}
Electric power is the rate at which energy is transferred or converted in an electric circuit.
\end{block}

\begin{block}{Key Points}
\begin{itemize}
\item Electric power is dissipated in resistances of a circuit
\item Capacitors do not dissipate electric power
\item Power dissipation often manifests as heat
\item Measured in watts (W), where 1 W = 1 J/s
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\begin{alertblock}{Power Dissipation}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys11-circuits-heating-effect-of-resistance.png}
\end{figure}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Electric Power: Mathematical Expressions}
\begin{block}{Basic Power Formula}
Power is proportional to voltage and current:
\begin{align}
P = IV
\end{align}
\end{block}

\begin{block}{Alternative Expressions (Using Ohm's Law)}
Without current term:
\begin{align}
P = \frac{V^2}{R}
\end{align}

Without voltage term:
\begin{align}
P = I^2R
\end{align}
\end{block}
\end{frame}

\begin{frame}
\begin{alertblock}{Equivalent Expressions}
\begin{figure}
    \centering
    \includegraphics[width=0.7\linewidth]{phys11-circuits-ohms-law-power-wheel.png}
\end{figure}
\end{alertblock}
\end{frame}

\section{Examples}

\begin{frame}
\frametitle{I Do: Ohm's Law Example}
\begin{exampleblock}{Problem}
A resistor with resistance $R = 10 \, \Omega$ is connected to a voltage source of $V = 12 \, \text{V}$. Calculate the current flowing through the resistor.
\end{exampleblock}
\pause
\begin{block}{Solution}
Using Ohm's law: $V = IR$

Rearranging to solve for current: $I = \frac{V}{R}$

Substituting the values:
\begin{align}
I &= \frac{12 \, \text{V}}{10 \, \Omega} \\
&= 1.2 \, \text{A}
\end{align}

Therefore, the current flowing through the resistor is $1.2 \, \text{A}$.
\end{block}
\end{frame}

\begin{frame}
\frametitle{We Do: Series Circuit Analysis}
\begin{exampleblock}{Problem}
Three resistors are connected in series: $R_1 = 5 \, \Omega$, $R_2 = 10 \, \Omega$, $R_3 = 15 \, \Omega$. If connected to a $30 \, \text{V}$ source:
\begin{enumerate}
\item Calculate the equivalent resistance
\item Find the current through the circuit
\item Calculate the voltage drop across each resistor
\end{enumerate}
\end{exampleblock}

\begin{block}{Partial Solution}
1. Equivalent resistance:
\begin{align}
R_{\text{equiv}} &= R_1 + R_2 + R_3 \\
&= 5 \, \Omega + 10 \, \Omega + 15 \, \Omega \\
&= 30 \, \Omega
\end{align}


\end{block}
\end{frame}

\begin{frame}
\frametitle{We Do: Series Circuit Analysis (continued)}
\begin{block}{Complete the Solution}


2. Circuit current:
\begin{align}
I &= \frac{V}{R_{\text{equiv}}} \\
&= \frac{30 \, \text{V}}{30 \, \Omega} \\
&= 1 \, \text{A}
\end{align}
3. Voltage drops across each resistor:

For $R_1$: $V_1 = I \times R_1 = 1 \, \text{A} \times 5 \, \Omega = $ ?

For $R_2$: $V_2 = I \times R_2 = 1 \, \text{A} \times 10 \, \Omega = $ ?

For $R_3$: $V_3 = I \times R_3 = 1 \, \text{A} \times 15 \, \Omega = $ ?
\\
Let's work through these calculations together.
\end{block}


\end{frame}

\begin{frame}
\frametitle{You Do: Parallel Circuit Problem}
\begin{exampleblock}{Problem}
Three resistors are connected in parallel: $R_1 = 6 \, \Omega$, $R_2 = 12 \, \Omega$, $R_3 = 4 \, \Omega$. If connected to a $24 \, \text{V}$ source:
\begin{enumerate}
\item Calculate the equivalent resistance
\item Find the total current from the source
\item Calculate the current through each resistor
\end{enumerate}
\end{exampleblock}

Work on this problem independently, and we'll review the solution together afterward.
\end{frame}

\section{Summary}

\begin{frame}
\frametitle{Key Concepts Summary}
\begin{columns}
\column{0.5\textwidth}
\begin{block}{Ohm's Law}
\begin{itemize}
\item $V = IR$
\item Linear relationship for ohmic materials
\end{itemize}
\end{block}

\begin{block}{Series Circuits}
\begin{itemize}
\item Same current through all resistors
\item $R_{\text{equiv}} = R_1 + R_2 + \cdots + R_N$
\end{itemize}
\end{block}

\column{0.5\textwidth}
\begin{block}{Parallel Circuits}
\begin{itemize}
\item Same voltage across all resistors
\item $\frac{1}{R_{\text{equiv}}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots + \frac{1}{R_N}$
\end{itemize}
\end{block}

\begin{block}{Electric Power}
\begin{itemize}
\item $P = IV = I^2R = \frac{V^2}{R}$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Practice Questions}
\begin{block}{Consider This}
\begin{enumerate}
\item How does adding more resistors in series affect the total current in a circuit?
\item Why is the equivalent resistance in a parallel circuit always less than the smallest individual resistor?
\item In what ways can you reduce power consumption in an electrical circuit?
\item How does current distribute in a parallel circuit? Why?
\end{enumerate}
\end{block}

\begin{block}{Next Steps}
We will explore more complex circuit configurations and apply these principles to practical problems in our next lesson.
\end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch01_Slides_intro_SigFigs.tex

```latex
\documentclass{beamer}
% Required packages
\usepackage{amsmath}
\usepackage{physics}
\usepackage{graphicx}
\usepackage{siunitx}
\usepackage{xcolor}
\graphicspath{{../images/}}
% Define custom colors for DS9 theme
\definecolor{ds9blue}{RGB}{25,25,112}
\definecolor{ds9gold}{RGB}{218,165,32}
\definecolor{ds9grey}{RGB}{105,105,105}
\definecolor{ds9red}{RGB}{178,34,34}
% Set up the Madrid theme with custom colors
\usetheme{Madrid}
\usecolortheme{whale}
\setbeamercolor{palette primary}{bg=ds9blue,fg=white}
\setbeamercolor{palette secondary}{bg=ds9grey,fg=white}
\setbeamercolor{palette tertiary}{bg=ds9gold,fg=black}
\setbeamercolor{palette quaternary}{bg=ds9red,fg=white}
\setbeamercolor{structure}{fg=ds9blue}
\setbeamercolor{title}{fg=ds9gold}
\setbeamercolor{subtitle}{fg=ds9gold}
\setbeamercolor{frametitle}{bg=ds9blue,fg=white}
\setbeamercolor{block title}{bg=ds9blue,fg=white}
\setbeamercolor{block body}{bg=ds9grey!20,fg=black}

\title[CH 1.3]{PHYS11 CH:1.3}
\subtitle{The Language of Physics: Physical Quantities and Units}
\author[Mr. Gullo]{Mr. Gullo}
\date[Sept 2025]{September 5, 2025}

\begin{document}

\begin{frame}
    \titlepage
    \centering
\end{frame}

\begin{frame}
    \frametitle{Outline}
    \tableofcontents
\end{frame}

\section{Learning Objectives}
\begin{frame}
    \frametitle{Learning Objectives}
    By the end of this section, you will be able to:
    \pause
    \begin{itemize}
        \item Associate physical quantities with their International System of Units (SI) and perform conversions among SI units using scientific notation.
        \pause
        \item Relate measurement uncertainty to significant figures and apply the rules for using significant figures in calculations.
        \pause
        \item Correctly create, label, and identify relationships in graphs using mathematical relationships (e.g., slope, y-intercept).
    \end{itemize}
\end{frame}

\section{Key Concepts}
\begin{frame}
    \frametitle{SI Units \& Scientific Notation}
    \begin{block}{Physical Quantities and Units}
        Physics relies on making measurements, which are expressed in terms of \textbf{units}.
        \pause
        \begin{itemize}
            \item \textbf{Base Units:} The seven fundamental units of the SI system (meter, kilogram, second, ampere, kelvin, mole, candela).
            \pause
            \item \textbf{Derived Units:} Combinations of base units (e.g., speed in \(\text{m/s}\)).
        \end{itemize}
    \end{block}
    \pause
    \begin{block}{Scientific Notation}
        A method for writing very large or small numbers.
        \pause
        \begin{itemize}
            \item Format: \(x \times 10^y\)
            \pause
            \item Example: The number \(840,000,000,000,000\) is written as \(8.40 \times 10^{14}\).
            \pause
            \item The power of 10 is called the \textbf{order of magnitude}.
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Accuracy, Precision, and Uncertainty}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \begin{block}{Definitions}
                \begin{itemize}
                    \item \textbf{Accuracy:} How close a measurement is to the correct or accepted value.
                    \pause
                    \item \textbf{Precision:} How well repeated measurements generate the same or similar results.
                    \pause
                    \item \textbf{Uncertainty:} A "disclaimer" for your measured value, often written as a \(\pm\) amount. E.g., \(11.0 \pm 0.2\) inches.
                \end{itemize}
            \end{block}
        \end{column}
        \begin{column}{0.5\textwidth}
            \begin{figure}
    \centering
    \includegraphics[width=0.8\linewidth]{phys11-accuracy-precision-targets.png}
    \caption{Four targets showing different combinations of accuracy and precision}
\end{figure}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Significant Figures}
    \begin{block}{What are they?}
        The number of significant figures in a measurement indicates the \textbf{precision} of the measuring tool. It includes all digits measured reliably plus one estimated digit.
    \end{block}
    \pause

    \begin{figure}
        \centering
        \includegraphics[width=0.8\linewidth]{phys11-rulers-significant-figures.png}
        \caption{Three rulers showing different levels of measurement precision}
    \end{figure}
\end{frame}

\begin{frame}
     \begin{figure}
        \centering
        \includegraphics[width=0.8\linewidth]{phys11-rulers-significant-figures.png}
    \end{figure}
    \begin{block}{Rules for Zeros}
        \begin{itemize}
            \item Zeros between non-zero digits are significant (e.g., 101 has 3 sig figs).
            \pause
            \item Leading zeros are not significant (e.g., 0.053 has 2 sig figs).
            \pause
            \item Trailing zeros are ambiguous. Use scientific notation to clarify (e.g., \(1.30 \times 10^3\) has 3 sig figs, while \(1.3 \times 10^3\) has 2).
        \end{itemize}
    \end{block}
\end{frame}

\section{Equations and Rules}
\begin{frame}
    \frametitle{Key Equations \& Calculation Rules}
    \begin{block}{Percent Uncertainty}
        One method of expressing uncertainty is as a percent of the measured value.
        \pause
        \[ \% \text{ uncertainty} = \frac{\delta A}{A} \times 100\% \]
        \pause
        Where \(A\) is the measurement and \(\delta A\) is the uncertainty in the measurement.
    \end{block}
    \pause
    \begin{block}{Rules for Significant Figures in Calculations}
        \begin{itemize}
            \item \textbf{Multiplication and Division:} The answer should have the same number of significant figures as the starting value with the \textit{fewest} significant figures.
            \pause
            \item \textbf{Addition and Subtraction:} The answer should have the same number of decimal places as the starting value with the \textit{fewest} decimal places.
        \end{itemize}
    \end{block}
\end{frame}

\section{Examples}
\begin{frame}
    \frametitle{I Do: Unit Conversion}
    \begin{exampleblock}{Problem: A Short Drive Home}
        Suppose you drive the \SI{10.0}{km} from your university to home in \SI{20.0}{min}. Calculate your average speed in (a) kilometers per hour (km/h) and (b) meters per second (m/s).
    \end{exampleblock}
    \pause
    \begin{block}{Solution (a): km/h}
        Average speed = \(\frac{\SI{10.0}{km}}{\SI{20.0}{min}}\). We need to convert minutes to hours.
        \pause
        \[ \text{speed} = \frac{\SI{10.0}{km}}{\SI{20.0}{min}} \times \left( \frac{\SI{60}{min}}{\SI{1}{h}} \right) = \SI{30.0}{km/h} \]
    \end{block}
    \pause
    \begin{block}{Solution (b): m/s}
        We can convert the result from part (a).
        \pause
        \[ \text{speed} = \frac{\SI{30.0}{km}}{\SI{1}{h}} \times \left( \frac{\SI{1000}{m}}{\SI{1}{km}} \right) \times \left( \frac{\SI{1}{h}}{\SI{3600}{s}} \right) = \SI{8.33}{m/s} \]
        \pause
        Note that all answers are given to three significant figures.
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{We Do: Calculating Uncertainty}
    \begin{alertblock}{Problem}
        A bathroom scale reads a person's mass as \SI{65}{kg} with a \SI{3}{\percent} uncertainty. What is the uncertainty in their mass in kilograms? (Question 48)
    \end{alertblock}
    \pause
    \begin{block}{Setup}
        \begin{enumerate}
            \item Identify the given values:
            \begin{itemize}
                \item Mass \( (A) = \SI{65}{kg} \)
                \item Percent Uncertainty = \SI{3}{\percent}
            \end{itemize}
            \pause
            \item Start with the formula: \( \% \text{ uncertainty} = \frac{\delta A}{A} \times 100\% \)
            \pause
            \item Rearrange to solve for the uncertainty, \(\delta A\):
            \[ \delta A = \frac{\% \text{ uncertainty}}{100\%} \times A \]
        \end{enumerate}
    \end{block}
    \pause
    \begin{exampleblock}{Let's Solve It!}
        Now, plug in the numbers. What do you get for the uncertainty \(\delta A\)?
        \[ \delta A = \frac{3\%}{100\%} \times \SI{65}{kg} = \textbf{?} \]
        \pause
        The answer is \SI{1.95}{kg}, which we can round to \SI{2}{kg} (Option a).
    \end{exampleblock}
\end{frame}

\begin{frame}
    \frametitle{You Do: Metric Prefixes}
    \begin{alertblock}{Problem}
        Which of the following would describe a length that is \(2.0 \times 10^{-3}\) of a meter? (Question 47)
    \end{alertblock}
    \pause
    \begin{itemize}
        \item[a.] \SI{2.0}{kilometers}
        \pause
        \item[b.] \SI{2.0}{megameters}
        \pause
        \item[c.] \SI{2.0}{millimeters}
        \pause
        \item[d.] \SI{2.0}{micrometers}
    \end{itemize}
    \pause
    \begin{block}{Hint}
        What metric prefix corresponds to the factor \(10^{-3}\)?
    \end{block}
    \pause
    \begin{beamercolorbox}[rounded=true,center,wd=\textwidth]{block body}
        The correct answer is \textbf{c. \SI{2.0}{millimeters}}. The prefix "milli-" means \(10^{-3}\).
    \end{beamercolorbox}
\end{frame}

\section{Tips for Mixed Operations}
\begin{frame}
    \frametitle{Significant Figures in Mixed Operations}
    \begin{block}{When You Have Both Multiplication and Addition}
        \textbf{Key Strategy:} Follow the order of operations, keeping track of significant figures at each step.
    \end{block}
    \pause
    \begin{exampleblock}{Example Problem: Calculate \(a \times b + c\)}
        Given: \(a = 2.5\), \(b = 3.42\), \(c = 0.876\)
    \end{exampleblock}
    \pause
    \begin{block}{Step-by-Step Approach}
        \begin{enumerate}
            \item \textbf{First:} Perform multiplication \(a \times b = 2.5 \times 3.42\)
            \begin{itemize}
                \item 2.5 has 2 sig figs, 3.42 has 3 sig figs
                \item Result: \(8.55\) → Round to \textbf{2 sig figs} = \textbf{8.6}
            \end{itemize}
            \pause
            \item \textbf{Second:} Perform addition \(8.6 + 0.876\)
            \begin{itemize}
                \item 8.6 has 1 decimal place, 0.876 has 3 decimal places
                \item Result: \(9.476\) → Round to \textbf{1 decimal place} = \textbf{9.5}
            \end{itemize}
        \end{enumerate}
    \end{block}
\end{frame}

\section{Summary}
\begin{frame}
    \frametitle{Summary}
    \begin{itemize}
        \item Physics is a quantitative science, requiring a standard system of units (SI units).
        \pause
        \medskip
        \item \textbf{Accuracy} is about correctness, while \textbf{precision} is about consistency.
        \pause
        \medskip
        \item \textbf{Significant figures} communicate the precision of our measurements and must be handled correctly in calculations.
        \pause
        \begin{itemize}
            \item Multiplication/Division: Fewest total sig figs.
            \pause
            \item Addition/Subtraction: Fewest decimal places.
        \end{itemize}
        \pause
        \medskip
        \item \textbf{Unit conversion} is a fundamental skill used to ensure calculations are performed with consistent units.
    \end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch04_slides_forces-fbd.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[System \& Free Body Diagrams]{System and Free Body Diagrams}
\subtitle{A Systematic Approach to Force Diagrams\\http://newsletter.oapt.ca/files/Systems-and-FB-Diagrams.html}
\author[E. Haller]{Eric Haller}
\date[2015]{Originally published: October 25, 2015}



\AtBeginSection[]
{
  \begin{frame}
    \frametitle{Table of Contents}
    \tableofcontents[currentsection]
  \end{frame}
}

\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Opening Quote}
\begin{quote}
``When asked to draw a force diagram for some simple situation, most students emerging from any level of introductory physics course are likely to draw objects which look like a porcupine shot by an Indian hunting party—the number and direction of pointed entities being essentially stochastic.''
\end{quote}
\pause
\vspace{0.5cm}
\hfill -- Arnold Arons (1979)
\pause
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\linewidth]{Porcupinebros.jpg}
\end{figure}
\end{frame}

\section{System Diagrams}

\begin{frame}
\frametitle{How can we simplify complex systems?}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\linewidth]{Musculoskeletal-System.png}
\end{figure}
\pause
\begin{itemize}
    \item Complex systems have many interacting parts
    \pause
    \item We need a systematic way to analyze forces
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{How to Draw System Diagrams}
\begin{enumerate}
    \item \textbf{Draw a simple sketch}
    \pause
    \begin{itemize}
        \item Keep it simple
        \item Use stick figures when possible
        \item Include important elements (ground, ropes, springs)
    \end{itemize}
    \pause
    \item \textbf{Draw a closed curve}
    \pause
    \begin{itemize}
        \item Enclose object of interest
        \item Curve should hug object closely
        \item Label inside as "system", outside as "environment"
    \end{itemize}
\end{enumerate}
\pause
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{Screenshot 2024-11-07 105535.png}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{System Diagrams (continued)}
\begin{enumerate}\setcounter{enumi}{2}
    \item \textbf{Label contact forces}
    \pause
    \begin{itemize}
        \item Identify forces at system-environment boundary
        \item Name both objects involved
        \item Multiple forces may exist at one point
    \end{itemize}
    \pause
    \item \textbf{Label non-contact forces}
    \pause
    \begin{itemize}
        \item Include gravity
        \item Include electromagnetic forces
        \item Write these as an aside
    \end{itemize}
\end{enumerate}
\pause
\begin{itemize}
    \item This systematic approach prevents missing forces
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{System Diagrams (continued)}
\begin{enumerate}\setcounter{enumi}{2}
    \item \textbf{Label contact forces}
    \pause
    \begin{itemize}
        \item Identify forces at system-environment boundary
        \item Name both objects involved
        \item Multiple forces may exist at one point
    \end{itemize}
    \pause
    \item \textbf{Label non-contact forces}
    \pause
    \begin{itemize}
        \item Include gravity
        \item Include electromagnetic forces
        \item Write these as an aside
    \end{itemize}
\end{enumerate}
\pause
\begin{figure}[H]
    \centering
    \includegraphics[width=0.3\linewidth]{Screenshot 2024-11-07 105554.png}
\end{figure}
\end{frame}

\begin{frame}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\linewidth]{Screenshot 2024-11-07 105535.png}
\end{figure}
\pause
\begin{figure}[H]
    \centering
    \includegraphics[width=0.3\linewidth]{Screenshot 2024-11-07 105554.png}
\end{figure}
\pause
\begin{itemize}
    \item Notice the clear separation between system and environment
\end{itemize}
\end{frame}

\section{Free Body Diagrams}

\begin{frame}
\frametitle{How to Draw Free Body Diagrams}
\begin{enumerate}
    \item \textbf{Draw a dot}
    \pause
    \begin{itemize}
        \item Represents "the system"
        \item Makes all diagrams uniform
        \item Easier to grade and understand
    \end{itemize}
    \pause
    \item \textbf{Draw force arrows}
    \pause
    \begin{itemize}
        \item Start from the central dot
        \item Draw to scale when possible
        \item Include only forces from system diagram
        \item Label each force clearly
    \end{itemize}
\end{enumerate}
\pause
\begin{figure}
    \centering
    \includegraphics[width=0.2\linewidth]{Screenshot 2024-11-07 105554.png}
\end{figure}
\end{frame}

\section{Why System \& Free Body Diagrams Matter}

\begin{frame}
\frametitle{Why Do We Need These Diagrams?}
\begin{columns}
\column{0.6\textwidth}
\textbf{Key Benefits:}
\pause
\begin{enumerate}
    \item They help us organize our thoughts about forces
    \pause
    \item They prevent us from forgetting forces
    \pause
    \item They make solving problems easier
\end{enumerate}
\pause

\vspace{0.3cm}
\textbf{Remember:}
\begin{itemize}
    \item Always choose your system first
    \item Label ALL forces clearly
    \item Show contact and non-contact forces
\end{itemize}

\end{columns}
\end{frame}

\begin{frame}
\frametitle{Tips for Success}
\textbf{Your Diagram Checklist:}
\pause
\begin{enumerate}
    \item Start with a simple sketch
    \pause
    \begin{itemize}
        \item[\Square] Keep it neat
        \item[\Square] Include only what matters
    \end{itemize}
    \pause

    \item Label everything clearly
    \pause
    \begin{itemize}
        \item[\Square] All forces named
        \item[\Square] Direction shown
    \end{itemize}
    \pause

    \item Check your work
    \pause
    \begin{itemize}
        \item[\Square] Did you include gravity?
        \item[\Square] Are contact points marked?
    \end{itemize}
\end{enumerate}
\pause
\begin{itemize}
    \item Following this checklist will improve your force diagrams
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Example Application}
\textbf{Tow Truck Scenario:}
\begin{itemize}
    \item System: Car being towed
\end{itemize}
\pause
\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{towtruck.png}
\end{figure}
\pause
\begin{itemize}
    \item Let's identify all forces acting on the car
\end{itemize}
\end{frame}

\begin{frame}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\linewidth]{towtruck.png}
\end{figure}
\pause
\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\linewidth]{CraigFBD.png}
\end{figure}
\pause
\begin{itemize}
    \item Notice how the FBD simplifies the real-world scenario
\end{itemize}
\end{frame}


\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{Screenshot 2024-11-11 130750.png}
\end{figure}
\pause
\begin{itemize}
    \item This example shows multiple systems and their interactions
\end{itemize}
\end{frame}


\begin{frame}
\frametitle{Newton's Third Law - Statement}
\begin{itemize}
    \item \textbf{Key Principle:} For every action force, there is an equal and opposite reaction force
    \pause
    \item When a first body exerts a force on a second body:
    \pause
    \begin{itemize}
        \item The second body exerts an equal force back
        \item The forces are equal in magnitude
        \item The forces act in opposite directions
    \end{itemize}
\end{itemize}
\pause
\begin{alertblock}{Important}
    Action-reaction pairs always act on different objects
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Example: Physics Teacher with Cart}
\begin{block}{Problem Setup}
\begin{itemize}
    \item Teacher mass: 65.0 kg
    \item Cart mass: 12.0 kg
    \item Equipment mass: 7.0 kg
    \pause
    \item Applied force: 150 N backward
    \item Friction force: 24.0 N
\end{itemize}
\end{block}
\pause
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\linewidth]{Picture.png}
\end{figure}
\pause
\begin{itemize}
    \item What happens if we treat all three as one system?
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Solution Strategy}
\begin{itemize}
    \item Define the system:
    \pause
    \begin{itemize}
        \item Teacher + Cart + Equipment
    \end{itemize}
    \pause
    \item External forces:
    \pause
    \begin{itemize}
        \item Floor's forward force: 150 N
        \item Friction force: -24.0 N
    \end{itemize}
    \pause
    \item Net force calculation:
    \pause
    \[\mathbf{F}_{\text{net}} = \mathbf{F}_{\text{floor}} - f = 150\text{ N} - 24.0\text{ N} = 126\text{ N}\]
\end{itemize}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{Picture.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Common Mistakes to Avoid}
\begin{alertblock}{Important Notes}
\begin{itemize}
    \item Don't include internal forces in net force calculations
    \pause
    \item Internal forces cancel out within the system
    \pause
    \item Examples of internal forces:
    \pause
    \begin{itemize}
        \item Force between teacher's hands and cart
        \item Force between cart and equipment
    \end{itemize}
    \pause
    \item System definition is crucial for problem-solving
\end{itemize}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Tips for Success}
\begin{block}{Key Points}
\begin{itemize}
    \item Always identify the system clearly
    \pause
    \item Draw a free-body diagram
    \pause
    \item Label all external forces
    \pause
    \item Remember:
    \pause
    \begin{itemize}
        \item Action and reaction forces act on different objects
        \item Forces between system components cancel out
        \item Net force considers only external forces
    \end{itemize}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Practice Problem}
An astronaut in space wants to move upward. Which direction should they throw an object?
\pause
\begin{itemize}
    \item Think about Newton's Third Law...
    \item Action-reaction pairs
    \item Conservation of momentum
\end{itemize}
\end{frame}

\begin{frame}
\begin{itemize}
    \item \textbf{Correct Answer:} Downward
    \pause
    \item \textbf{Explanation:}
    \pause
    \begin{itemize}
        \item Action: Astronaut throws object downward
        \item Reaction: Object pushes astronaut upward
        \item Forces are equal in magnitude, opposite in direction
    \end{itemize}
    \pause
    \begin{alertblock}{Application}
        This is how rockets work in space!
    \end{alertblock}
\end{itemize}
\end{frame}



\begin{frame}
\frametitle{Acknowledgments}
\begin{itemize}
    \item Original article published in Ontario Association of Physics Teachers newsletter
    \pause
    \item Author: Eric Haller, Physics Teacher at Bond Schools International
    \pause
    \item Reference: Knight, R.D., "FIVE EASY LESSONS: Strategies for Successful Physics Teaching"
\pause
\end{itemize}
\begin{center}
    \Large{Questions?}
\end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/review_exam-prep.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

\title[Physics Final Strategy]{PHYS11/12: Final Exam Strategy}
\author[Mr. Gullo]{Mr. Gullo}
\date[June 2025]{June 2025}

\begin{document}

\frame{\titlepage}

\section{Introduction and Proficiency Scale}

\begin{frame}{Learning Objectives}
By the end of this presentation, you will be able to:
\begin{itemize}
\item Understand the proficiency scale used for grading open-ended questions
\item Apply strategic time management techniques during the exam
\item Use the G.U.E.S.S. method systematically for problem-solving
\item Distinguish between Proficient and Extending level responses
\item Demonstrate clear, logical thinking in your solutions
\end{itemize}
\end{frame}

\begin{frame}{Understanding the Proficiency Scale}
\begin{block}{Four Levels of Understanding}
\begin{itemize}
\item \textcolor{ds9red}{\textbf{Emerging:}} Limited understanding, incomplete solutions
\item \textcolor{orange}{\textbf{Developing:}} Partial understanding, some correct elements
\item \textcolor{green}{\textbf{Proficient:}} Clear understanding, systematic approach
\item \textcolor{ds9blue}{\textbf{Extending:}} Deep understanding, sophisticated reasoning
\end{itemize}
\end{block}

\vspace{0.5cm}

\textbf{Key Point:} \emph{How} you solve a problem is as important as your final answer!
\end{frame}

\section{Strategic Test-Taking}

\begin{frame}{The First Five Minutes: Strategic Setup}
\begin{enumerate}
\item \textbf{Brain Dump (30 seconds):} Write essential formulas, constants, and rules on scrap paper
\item \textbf{Survey the Battlefield (2 minutes):} Scan the entire exam, identify open-response questions
\item \textbf{Internalize the Goal:} Remember to be clear, systematic, and logical
\end{enumerate}

\vspace{0.5cm}

\begin{block}{Pro Tip}
Get worried formulas out of your head and onto paper immediately!
\end{block}
\end{frame}

\begin{frame}{The Three-Pass Strategy}
\textbf{Don't do the exam in order!} Maximize your points.

\begin{block}{Pass 1: Quick Wins (10-15 min)}
Answer all easy multiple-choice questions you know instantly. Circle harder questions and move on.
\end{block}
\begin{block}{Pass 2: The Deep Dive (45-50 min)}
Focus on open-response questions using the G.U.E.S.S. method. Spend quality time here.
\end{block}
\begin{block}{Pass 3: The Finish Line (10-15 min)}
Attempt remaining questions, review work, transfer answers carefully.
\end{block}


\end{frame}

\section{G.U.E.S.S. Problem-Solving Method}

\begin{frame}{Introducing the G.U.E.S.S. Method}
Your roadmap to \textbf{Proficient} level responses:

\vspace{0.5cm}
\begin{left}

\textbf{G} - Givens \& Diagram \\
\textbf{U} - Unknowns \& Plan \\
\textbf{E} - Equations \\
\textbf{S} - Substitute \& Solve \\
\textbf{S} - Solution \& Statement \\
\end{left}

\vspace{0.5cm}

\textbf{Remember:} This systematic approach demonstrates your thinking process!
\end{frame}

\begin{frame}{G - Givens \& Diagram}
\begin{block}{What to Include}
\begin{itemize}
\item List all knowns and unknowns clearly
\item Example: $V = 16\,\text{V}$, $I_{\text{off}} = 0.40\,\text{A}$, $I_{\text{on}} = 0.90\,\text{A}$, $P_{\text{screen}} = ?$
\item Make a clear, labeled diagram
\end{itemize}
\end{block}

\begin{block}{Diagram Types}
\begin{itemize}
\item \textbf{Circuits:} Redraw the circuit clearly
\item \textbf{Forces:} Draw free-body diagrams
\item \textbf{Kinematics:} Sketch the motion path
\end{itemize}
\end{block}

\textbf{Key:} This directly addresses the "Proficient" criterion for clear organization.
\end{frame}

\begin{frame}{U - Unknowns \& Plan}
\begin{block}{State Your Strategy}
\begin{itemize}
\item Clearly state what you need to find
\item Explain how you will solve it
\end{itemize}
\end{block}

\begin{block}{Example Planning Statement}
"To find the power of the screen, I will first find the current used by the screen alone. Then I will use the power formula $P = IV$."
\end{block}

\textbf{Impact:} This single sentence elevates your response from "Developing" to "Proficient" by showing logical planning!

\end{frame}

\begin{frame}{E - Equations}
\begin{block}{Best Practices}
\begin{itemize}
\item Write base formulas \emph{before} plugging in numbers
\item Show the physics principles you're using
\item Examples: $P = IV$, $V = IR$, $F_{\text{net}} = ma$
\end{itemize}
\end{block}

\begin{block}{Why This Matters}
Demonstrates you understand the relevant physics concepts, not just arithmetic.
\end{block}

\end{frame}

\begin{frame}{S - Substitute \& Solve}
\begin{block}{Show Logical Steps}
\begin{itemize}
\item Work line-by-line, vertically down the page
\item Use units consistently in every step
\item Don't show scattered calculations
\end{itemize}
\end{block}

\begin{columns}
\begin{column}{0.5\textwidth}
\textcolor{green}{\textbf{Good Example:}}
\begin{align}
I_{\text{screen}} &= I_{\text{on}} - I_{\text{off}} \\
&= 0.90\,\text{A} - 0.40\,\text{A} \\
&= 0.50\,\text{A}
\end{align}
\end{column}
\begin{column}{0.5\textwidth}
\textcolor{red}{\textbf{Bad Example:}}
\begin{align}
0.9 - 0.4 = 0.5
\end{align}
\end{column}
\end{columns}

\vspace{1cm}

\textbf{Units are a major differentiator between "Developing" and "Proficient"!}
\end{frame}

\begin{frame}{S - Solution \& Statement}
\begin{block}{Final Presentation}
\begin{itemize}
\item \textbf{Box your final answer}
\item Write a concluding statement with units
\item Example: "Therefore, the power used by the screen alone is 8.0 W."
\end{itemize}
\end{block}

\begin{block}{Complete Solution Format}
\vspace{0.5cm}
\boxed{P_{\text{screen}} = 8.0\,\text{W}}
\\
\vspace{0.5cm}
\\
"Therefore, the power used by the screen alone is 8.0 W."
\end{block}

\end{frame}

\section{Achieving Proficient and Extending Levels}

\begin{frame}{Reaching the 'Extending' Level}
\textbf{Extending} = Sophisticated understanding and complete command of physics

\begin{block}{Three Key Strategies}
\begin{enumerate}
\item \textbf{Find Hidden Details:} State implied information explicitly
\item \textbf{Explain the Physics:} Don't just show math, explain why
\item \textbf{Check Your Answer:} Sense-check, units, alternative methods
\end{enumerate}
\end{block}

\begin{block}{Hidden Details Examples}
\begin{itemize}
\item "starts from rest" $\rightarrow$ $v_i = 0$
\item "on the moon" $\rightarrow$ use $g_{\text{moon}}$
\item "no atmosphere" $\rightarrow$ no air resistance
\end{itemize}
\end{block}
\end{frame}
% Add this to your preamble if you don't have it already


\begin{frame}{Proficient vs. Exemplary: Capacitor Circuit}

\begin{columns}[T] % Aligns the tops of the columns
    \begin{column}{0.3\textwidth}
        \textbf{Question:} For a given circuit, what is the voltage across and current through the capacitor a long time after the switch is closed?

    \end{column}
    \begin{column}{0.65\textwidth}
        \begin{block}{Proficient Answer}
            After a long time, the capacitor is fully charged. \\
            $I_C = 0$ A     $V_C = 12$ V
        \end{block}

       \begin{alertblock}{Extending Answer}
    After a long time, the capacitor is fully charged and acts like an \textbf{open circuit}.

    \begin{itemize}
        \item \textbf{Current ($I_C$):} Because the circuit is open, no current can flow. Therefore, $\mathbf{I_C = 0}$ \textbf{A}.

        \item \textbf{Voltage ($V_C$):} With zero current, there is no voltage drop across the resistor ($V_R = I \cdot R = 0$). All of the battery's voltage must be across the capacitor. Therefore, $\mathbf{V_C = 12}$ \textbf{V}.
    \end{itemize}
\end{alertblock}

    \end{column}
\end{columns}

\end{frame}

\section{Practice Examples}

\begin{frame}{I Do: Complete G.U.E.S.S. Example}
\textbf{Problem:} A laptop uses 0.40 A when off and 0.90 A when on. If the voltage is 16 V, what power does the screen use?
\pause
\vspace{0.5cm}

\textbf{G - Givens:} $V = 16\,\text{V}$, $I_{\text{off}} = 0.40\,\text{A}$, $I_{\text{on}} = 0.90\,\text{A}$ \\
\pause
\textbf{U - Plan:} Find current used by screen alone, then use $P = IV$ \\
\pause
\textbf{E - Equations:} $I_{\text{screen}} = I_{\text{on}} - I_{\text{off}}$, $P = IV$ \\
\pause
\textbf{S - Solve:}
$I_{\text{screen}} = 0.90\,\text{A} - 0.40\,\text{A} = 0.50\,\text{A}$
$P = (16\,\text{V})(0.50\,\text{A}) = 8.0\,\text{W}$ \\
\pause
\textbf{S - Statement:} $\boxed{\therefore P_{\text{screen}} = 8.0\,\text{W}}$
\end{frame}


\section{Summary and Final Tips}

\begin{frame}{Summary: Your Path to Success}
\begin{block}{Remember the Strategy}
\begin{itemize}
\item \textbf{First 5 minutes:} Brain dump, survey, internalize goals
\item \textbf{Three-pass approach:} Quick wins → Deep dive → Finish line
\item \textbf{G.U.E.S.S. method:} Your systematic problem-solving framework
\end{itemize}
\end{block}

\begin{block}{Proficient → Extending}
\begin{itemize}
\item Find hidden details and state assumptions
\item Explain the physics, not just the math
\item Always check your answers multiple ways
\end{itemize}
\end{block}

\textbf{Final Reminder:} Show your thinking process clearly – that's what the rubric measures!
\end{frame}

\begin{frame}{Final Words of Encouragement}
\begin{center}
\Large
\textcolor{ds9gold}{\textbf{Stay Calm}} \\
\textcolor{ds9blue}{\textbf{Be Systematic}} \\
\textcolor{ds9red}{\textbf{Show What You Know}} \\
\end{center}



\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-exam-prep-add-oil-motivation.jpg}
\end{figure}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch05_slides_vector-analysis.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[ Vector Analysis]{PHYS11 CH:5.1-5.3}
\subtitle{Vector Analysis and Applications }
\author[Mr. Gullo]{Mr. Gullo}
\date[Oct 2024]{October 2024}

% Table of contents at the beginning of each section
\AtBeginSection[]
{
  \begin{frame}
    \frametitle{Table of Contents}
    \tableofcontents[currentsection]
  \end{frame}
}

% Add logo
\logo{\includegraphics[width=0.1\linewidth]{cinec_logo.png}}

\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Introduction to Vector Analysis}
\begin{itemize}
    \item Vectors are essential in physics for describing quantities with magnitude and direction
    \item Key topics:
    \begin{itemize}
        \item Vector addition and subtraction
        \item Resolving vectors into components
        \item Vector applications in real-world problems
    \end{itemize}
\end{itemize}
\end{frame}

\section{Vector Operations}

\begin{frame}
\frametitle{Trig Review}
\begin{columns}[T] % Top-aligned columns
    \column{0.48\textwidth}
    \begin{figure}
        \centering
        \includegraphics[width=\linewidth]{phys11-math-trigonometry-sohcahtoa.png}
        \caption{SOHCAHTOA mnemonic}
    \end{figure}

    \column{0.48\textwidth}
    \begin{figure}
        \centering
        \includegraphics[width=\linewidth]{phys11-math-sine-cosine-laws.png}
        \caption{Sine and Cosine Laws}
    \end{figure}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Vector Addition and Subtraction}
\begin{itemize}
    \item Vector addition:
- Tip-to-tail method
- Parallelogram method

\item Vector subtraction:
- Add the negative of the vector: $\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$

\item Resultant vector: $\vec{R} = \vec{A} + \vec{B}$
 \\
- For n vectors: $\vec{R} = \vec{A} + \vec{B} + \vec{C} + ... + \vec{N}$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Vector Addition and Subtraction}
\begin{itemize}
\item Magnitude of resultant:\\
- General case: $|\vec{R}| = \sqrt{A^2 + B^2 + 2AB\cos\theta}$\\
- For perpendicular vectors: $|\vec{R}| = \sqrt{A^2 + B^2}$

\item Direction of resultant:\\
- Using magnitudes and angle: $\tan\phi = \frac{B\sin\theta}{A + B\cos\theta}$\\
- Using components: $\tan\phi = \frac{A_y + B_y}{A_x + B_x}$,

\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Resolving Vectors into Components}
\begin{itemize}
    \item Any vector can be resolved into x and y components
    \item $A_x = A\cos\theta$, $A_y = A\sin\theta$
    \item Magnitude: $A = \sqrt{A_x^2 + A_y^2}$
    \item Direction: $\tan\theta = \frac{A_y}{A_x}$
\end{itemize}
\end{frame}

\section{Vector Applications}

\begin{frame}
\frametitle{Example 1: River Crossing Problem}
Problem: A river flows SW to NE at 7.1 m/s. A boat moving at 13 m/s wants to reach a point due east.


\end{frame}
\begin{frame}
\frametitle{Example 1: River Crossing Problem}
Problem: A river flows SW to NE at 7.1 m/s. A boat moving at 13 m/s wants to reach a point due east.\\

Solution:
\begin{itemize}
    \item River velocity components: $v_{rx} = v_{ry} = 7.1\cos45° = 5.02$ m/s
    \item Boat must counteract river's y-component: $v_{by} = -5.02$ m/s
    \item Angle of boat's heading: $\theta = \arcsin(-5.02/13) \approx -22.6°$
\end{itemize}
Answer: The boat should head 22.6° south of east.
\end{frame}

\begin{frame}
\frametitle{Example 2: Displacement Problem}
Problem: A person walks 10.0 m north, then 2.0 m east. Find the resultant displacement.

\end{frame}

\begin{frame}
\frametitle{Example 2: Displacement Problem}
Problem: A person walks 10.0 m north, then 2.0 m east. Find the resultant displacement.

Solution:
\begin{itemize}
    \item Use Pythagorean theorem: $R = \sqrt{10.0^2 + 2.0^2} \approx 10.2$ m
    \item Angle: $\theta = \arctan(10.0/2.0) \approx 78.7°$ north of east
\end{itemize}
Answer: $\vec{R} = 10.2$ m, 78.7° north of east
\end{frame}
\section{Projectile Motion}

\begin{frame}
\frametitle{Projectile Motion Basics}
\begin{itemize}
    \item Combination of horizontal and vertical motion
    \item Horizontal motion: constant velocity (neglecting air resistance)
    \item Vertical motion: constant acceleration due to gravity
    \item Key equations:
    \begin{itemize}
        \item Range: $R = \frac{v_0^2 \sin(2\theta)}{g}$
        \item Maximum height: $h_{\max} = \frac{v_0^2 \sin^2\theta}{2g}$
        \item Time of flight: $t = \frac{2v_0 \sin\theta}{g}$
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Example 3: Projectile Motion Problem}
Problem: A water-balloon cannon fires at 30 m/s, 50° above horizontal. Find the range.

\end{frame}
\begin{frame}
\frametitle{Example 3: Projectile Motion Problem}
Problem: A water-balloon cannon fires at 30 m/s, 50° above horizontal. Find the range.

Solution:
\begin{itemize}
    \item Use range equation: $R = \frac{v_0^2 \sin(2\theta)}{g}$
    \item $R = \frac{(30 \text{ m/s})^2 \sin(2 * 50°)}{9.8 \text{ m/s}^2} \approx 90.44$ m
\end{itemize}
Answer: The water balloon will fall approximately 90.44 m away.
\end{frame}
\begin{frame}
\frametitle{Conclusion}
\begin{itemize}
    \item Vector analysis is crucial for understanding motion in physics
    \item Key concepts covered:
    \begin{itemize}
        \item Vector addition and subtraction
        \item Resolving vectors into components
        \item Applications in real-world problems
        \item Basics of projectile motion
    \end{itemize}
    \item These concepts help analyze complex motions and solve practical problems
    \item Practice with various examples to master vector analysis
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Global Angles}

\begin{block}{Problem}
What is the global angle of 20° south of west?
\end{block}

\begin{center}
\begin{tikzpicture}[scale=1.2]
    % Draw main circle
    \draw (0,0) circle (2);

    % Draw axes
    \draw[->] (-2.5,0) -- (2.5,0) node[right] {East (0°)};
    \draw[->] (0,-2.5) -- (0,2.5) node[above] {North (90°)};

    % Draw compass directions
    \node[above] at (0,2) {N (90°)};
    \node[left] at (-2,0) {W (180°)};
    \node[right] at (2,0) {E (0°)};
    \node[below] at (0,-2) {S (270°)};

    % Draw the angle
    \draw[->, thick, red] (0,0) -- ({2*cos(200)}, {2*sin(200)});
    \draw[red] (1,0) arc (0:200:1);

    % Label the angle
    \node[red] at (1.2,-0.8) {200°};

    % Show the "south of west" reference
    \draw[blue, dashed] (-2,0) -- (-2,-0.8) node[left] {20° south};

\end{tikzpicture}
\end{center}
\end{frame}

\begin{frame}
\frametitle{River Crossing Problem}
\begin{block}{Problem}
A person attempts to cross a river in a straight line by navigating a boat at $15 \mathrm{~m} / \mathrm{s}$. If the river flows at $5.0 \mathrm{~m} / \mathrm{s}$ from left to right, what would be:
\begin{itemize}
    \item The magnitude of the boat's resultant velocity?
    \item The direction relative to the straight line across the river?
\end{itemize}
\end{block}

\begin{center}
\begin{tikzpicture}[scale=0.7]
    % River banks
    \draw[thick, brown] (-4,2) -- (4,2);
    \draw[thick, brown] (-4,-2) -- (4,-2);

    % River flow arrows
    \draw[->, blue, thick] (-3,0) -- (-2,0);
    \draw[->, blue, thick] (-1,0) -- (0,0);
    \draw[->, blue, thick] (1,0) -- (2,0);

    % Boat's intended direction
    \draw[->, thick, red] (0,-2) -- (0,2);

    % Resultant motion
    \draw[->, thick, purple] (0,-2) -- (1.5,2);

    % Labels
    \node[blue] at (0,0.5) {River flow: $5.0 \mathrm{~m}/\mathrm{s}$};
    \node[red] at (-0.5,0) {$15 \mathrm{~m}/\mathrm{s}$};
\end{tikzpicture}
\end{center}

\end{frame}

\begin{frame}
\frametitle{River Crossing Solution}

The correct solution:
\begin{itemize}
    \item Resultant velocity: $15.8 \mathrm{~m} / \mathrm{s}$
    \item Direction: $18.4^{\circ}$ to the right
\end{itemize}


Using the Pythagorean theorem:
\[v_\text{resultant} = \sqrt{(5.0)^2 + (15.0)^2} = 15.8 \mathrm{~m}/\mathrm{s}\]

The angle is given by:
\[\theta = \tan^{-1}\left(\frac{5.0}{15.0}\right) = 18.4^\circ\]

\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch03_slides_vectors.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Acceleration and Motion]{PHYS11 CH3:}
\subtitle{ Acceleration and Motion}
\author[Mr. Gullo]{Mr. Gullo}
\date[Sept 2024]{September 2024}

% Table of contents at the beginning of each section
\AtBeginSection[]
{
  \begin{frame}
    \frametitle{Table of Contents}
    \tableofcontents[currentsection]
  \end{frame}
}
\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Introduction}
\begin{itemize}
    \item Understanding motion is crucial in physics
    \item Acceleration: a fundamental concept
    \item Key topics:
    \begin{itemize}
        \item Average acceleration
        \item Kinematic equations
        \item Graphical analysis
        \item Vector directions
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Acceleration: Definition}
\begin{itemize}
    \item Acceleration: rate of change of velocity with time
    \item Vector quantity (magnitude and direction)
    \item Formula:
    \[\vec{a} = \frac{\Delta \vec{v}}{\Delta t}\]
    where:
    \begin{itemize}
        \item $\vec{a}$ is acceleration
        \item $\Delta \vec{v} = \vec{v} - \vec{v}_0$ is change in velocity
        \item $\Delta t = t - t_0$ is change in time
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Average Acceleration}
\begin{itemize}
    \item Average acceleration over a time interval:
    \[\vec{a}_{\text{avg}} = \frac{\vec{v} - \vec{v}_0}{t - t_0}\]
    \item Useful for calculating overall change in motion
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Kinematic Equations for Uniform Acceleration}
For constant acceleration:
\begin{align*}
\vec{v} &= \vec{v}_0 + \vec{a}t \\
\vec{x} &= \vec{x}_0 + \vec{v}_0 t + \tfrac{1}{2} \vec{a} t^2 \\
v^2 &= v_0^2 + 2a (x - x_0)
\end{align*}
where:
\begin{itemize}
    \item $\vec{v}$: final velocity
    \item $\vec{v}_0$: initial velocity
    \item $\vec{a}$: acceleration
    \item $t$: time
    \item $\vec{x}$: final position
    \item $\vec{x}_0$: initial position
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Graphical Analysis: Velocity vs. Time}
\begin{itemize}
    \item Slope represents acceleration
    \item Straight line: constant acceleration
    \item Curved line: changing acceleration
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Graphical Analysis: Displacement vs. Time}
\begin{itemize}
    \item Slope represents velocity
    \item Straight line: constant velocity (zero acceleration)
    \item Curved line: changing velocity (non-zero acceleration)
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Vectors and Direction}
\begin{itemize}
    \item Acceleration, velocity, and displacement are vector quantities
    \item Direction is significant:
    \begin{itemize}
        \item Positive acceleration: vector points in positive direction
        \item Negative acceleration: vector points in negative direction
        \item Positive and negative vectors are 180° apart
    \end{itemize}
    \item \textbf{Important note:} We use "negative acceleration" instead of "deceleration"
    \begin{itemize}
        \item This emphasizes that acceleration is a vector quantity
        \item It reinforces the concept that slowing down is just acceleration in the opposite direction
        \item Helps avoid misconceptions about the nature of acceleration
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Example 1: Calculating Average Acceleration}
Problem: Velocity increases from 0 to 20 m/s in 10 s. What is the average acceleration?

Solution:
\begin{align*}
\vec{a}_{\text{avg}} &= \frac{\vec{v} - \vec{v}_0}{t} \\
&= \frac{20 \, \text{m/s} - 0 \, \text{m/s}}{10 \, \text{s}} \\
&= 2 \, \text{m/s}^2
\end{align*}

Answer: The average acceleration is $2 \, \text{m/s}^2$.
\end{frame}

\begin{frame}
\frametitle{Example 2: Interpreting Velocity vs. Time Graphs}
Problem: Show that the acceleration of a jet car is $5.0 \, \text{m/s}^2$ at any point on the graph.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\linewidth]{2024_09_22_d75bb9ada91612339d1ag-12.jpg}
\caption{Velocity vs. Time Graph for a Jet Car}
\end{figure}

\end{frame}

\begin{frame}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\linewidth]{2024_09_22_d75bb9ada91612339d1ag-12.jpg}
\caption{Velocity vs. Time Graph for a Jet Car}
\end{figure}
\begin{itemize}
    \item Slope of v-t graph represents acceleration
    \item Straight line indicates constant acceleration
    \item Slope = $\frac{\Delta \vec{v}}{\Delta t} = \frac{\vec{v}}{t} = 5.0 \, \text{m/s}^2$
\end{itemize}

Answer: The acceleration is $5.0 \, \text{m/s}^2$ at any point on the graph.
\end{frame}
\begin{frame}
\frametitle{Car Acceleration Problem: Two-Phase Motion}
\textbf{Problem Statement:}
A car undergoes two-phase motion:
\begin{itemize}
\item Phase 1: Accelerates from rest at $3.0 , \text{m/s}^2$ to $21.0 , \text{m/s}$
\item Phase 2: Decelerates at $4.0 , \text{m/s}^2$ until stopping
\end{itemize}
\vspace{0.5cm}
\textbf{Question:} Find the total time of travel.
\end{frame}
\begin{frame}
\frametitle{Solution: Total Time and Visualization}
\begin{tikzpicture}[scale=0.65]
\draw[->] (0,0) -- (7,0) node[right] {Time (s)};
\draw[->] (0,0) -- (0,4) node[above] {Velocity (m/s)};
\draw[thick, blue] (0,0) -- (3.5,3.5) -- (7,0);
\draw[dashed] (3.5,0) -- (3.5,3.5);
\draw[dashed] (0,3.5) -- (3.5,3.5);
\node[left] at (0,3.5) {21};
\node[below] at (3.5,0) {$t_1$};
\node[below] at (7,0) {$t_2$};
\node[above, blue, rotate=35] at (1.75,1.75) {$a = 3.0 , \text{m/s}^2$};
\node[above, blue, rotate=-35] at (5.25,1.75) {$a = -4.0 , \text{m/s}^2$};
\end{tikzpicture}
\end{frame}
\begin{frame}
\frametitle{Solution: Phase 1 - Acceleration}
\textbf{Phase 1 (Acceleration):}
\begin{itemize}
\item Initial velocity: $v_0 = 0 , \text{m/s}$
\item Final velocity: $v = 21.0 , \text{m/s}$
\item Acceleration: $a = 3.0 , \text{m/s}^2$
\end{itemize}
Using the equation: $v = v_0 + at_1$
\begin{align*}
21 &= 0 + 3t_1 \
t_1 &= \frac{21}{3} = 7.0 , \text{s}
\end{align*}
\textbf{Time for Phase 1: $7.0 , \text{s}$}
\end{frame}
\begin{frame}
\frametitle{Solution: Phase 2 - Deceleration}
\textbf{Phase 2 (Deceleration):}
\begin{itemize}
\item Initial velocity: $v_0 = 21.0 , \text{m/s}$
\item Final velocity: $v = 0 , \text{m/s}$
\item Deceleration: $a = -4.0 , \text{m/s}^2$
\end{itemize}
Using the equation: $v = v_0 + at_2$
\begin{align*}
0 &= 21 + (-4)t_2 \
4t_2 &= 21 \
t_2 &= \frac{21}{4} = 5.25 , \text{s}
\end{align*}
\textbf{Time for Phase 2: $5.25 , \text{s}$}

\textbf{Total time:}
\begin{align*}
t_{\text{total}} &= t_1 + t_2 \
&= 7.0 , \text{s} + 5.25 , \text{s} \
&= 12.25 , \text{s}
\end{align*}
\textbf{Answer:} The total time of travel is $12.25 , \text{s}$ (approximately $12 , \text{s}$)


\end{frame}

\begin{frame}
\frametitle{Conclusion}
\begin{itemize}
    \item Understanding acceleration is essential in physics
    \item Key concepts covered:
    \begin{itemize}
        \item Definition of acceleration
        \item Average acceleration
        \item Kinematic equations
        \item Graphical analysis
        \item Vector directions
    \end{itemize}
    \item These concepts help analyze real-world situations
    \item Practice with examples to master the material
    \item Remember: "Negative acceleration" instead of "deceleration" emphasizes the vector nature of acceleration
\end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/review_exam-howto.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

\title[NOPS Exam Guide]{Scannable Exam Guide}
\subtitle{How to Successfully Complete Your NOPS Answer Sheet}
\author[Mr. Gullo]{Mr. Gullo}
\date[June 2025]{June, 2025}

\begin{document}

\frame{\titlepage}

\section{Introduction to NOPS Exams}

\begin{frame}{Learning Objectives}
\frametitle{Learning Objectives}
By the end of this presentation, you will be able to:
\begin{itemize}
\item Properly handle and maintain your NOPS answer sheet
\item Correctly fill out your personal information and registration number
\item Mark multiple-choice answers using the proper technique
\item Follow correct procedures for written responses
\item Apply appropriate error correction protocols
\item Complete a final checklist before submission
\end{itemize}
\end{frame}

\begin{frame}{What is a NOPS Exam?}
\frametitle{What is a NOPS Exam?}
\begin{block}{NOPS Definition}
NOPS stands for \textbf{Network Optical Processing System} - a computer-based grading system that scans your answer sheet optically.
\end{block}

\textbf{Key Features:}
\begin{itemize}
\item Computer scanner reads your markings
\item Extremely sensitive to marks and placement
\item Requires precise technique for accurate grading
\item Any errors in marking can result in incorrect scoring
\end{itemize}

\end{frame}

\section{Answer Sheet Procedures}

\begin{frame}{Answer Sheet Handling}
\frametitle{Answer Sheet Handling}
\begin{block}{Critical Rule}
The scanner is \textbf{very sensitive} - treat your answer sheet with extreme care!
\end{block}

\textbf{DO:}
\begin{itemize}
\item Keep the sheet clean, dry, and flat
\item Handle with clean hands
\item Place on a flat, stable surface when marking
\end{itemize}

\textbf{DO NOT:}
\begin{itemize}
\item Fold, crease, or tear the sheet
\item Spill liquids or get the sheet wet
\item Write notes or doodles outside designated areas
\item Rest your hand heavily on the sheet while marking
\end{itemize}
\end{frame}

\section{Filling Information}

\begin{frame}{Required Materials}
\frametitle{Required Materials}
\begin{block}{Pen Requirement}
Use \textbf{ONLY} a blue or black pen as instructed on the answer sheet.
\end{block}

\textbf{Why pen only?}
\begin{itemize}
\item Pencil marks may be too light for scanner detection
\item Erasures leave marks that confuse the scanner
\item Pen provides consistent, dark marks
\end{itemize}

\textbf{Personal Information:}
\begin{itemize}
\item Write your name clearly in the designated space
\item Add your signature where indicated
\item Use legible handwriting
\end{itemize}
\end{frame}

\begin{frame}

\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-exam-prep-nops-answer-sheet.png}
\end{figure}
\end{frame}

\begin{frame}{Registration Number Process}
\frametitle{Registration Number - CRITICAL STEP}
This is a \textbf{two-step process} that must be completed perfectly:

\begin{block}{Step A: Write the Digits}
Carefully write your registration number in the boxes at the top of the grid, placing \textbf{one digit per box}.
\end{block}

\begin{block}{Step B: Mark the Bubbles}
For each digit you wrote, find the matching bubble in the column directly below and mark with a clear \textbf{'X'}.
\end{block}

\textbf{Example:} If your registration number is 12345:
\begin{itemize}
\item Write "1" in first box, mark "1" bubble below
\item Write "2" in second box, mark "2" bubble below
\item Continue for all digits
\end{itemize}
\end{frame}

\begin{frame}{Pre-Filled Sections}
\frametitle{Pre-Filled Sections}
\begin{block}{Important Warning}
You will see sections labeled "Exam ID," "Type," and "Scrambling" that are already filled out.
\end{block}

\textbf{DO NOT:}
\begin{itemize}
\item Make any changes to these sections
\item Add any marks or annotations
\item Write over existing marks
\item Attempt to "correct" what appears to be errors
\end{itemize}

These sections are pre-configured for your specific exam and any changes will cause scoring errors.

\end{frame}

\section{Answering Questions}

\begin{frame}{Multiple-Choice Technique}
\frametitle{Multiple-Choice Answering}
\begin{block}{Marking Technique}
Mark your chosen answer with a clear \textbf{'X'} that fits completely inside the designated box.
\end{block}

\textbf{Step-by-step process:}
\begin{enumerate}
\item Find the question number on the answer grid
\item Locate your chosen answer (a, b, c, or d)
\item Make a clear 'X' mark inside the box
\item Ensure the 'X' does not extend outside the box boundaries
\end{enumerate}

\textbf{Critical Rule:} Mark \textbf{ONLY ONE} answer per question. Multiple marks will be scored as incorrect, even if one of them is the right answer.
\end{frame}

\begin{frame}{Written Response Guidelines}
\frametitle{Written Response Guidelines}
For questions requiring written solutions:

\begin{block}{Answer Location}
Use the separate answer page with large, numbered boxes corresponding to each open-response question.
\end{block}

\textbf{Writing Requirements:}
\begin{itemize}
\item Write your \textbf{entire answer} inside the designated box
\item Include all work, calculations, and explanations
\item Keep all writing within the box borders
\item Use clear, legible handwriting
\end{itemize}

\textbf{Important:} The scanner will \textbf{not read} anything written outside the box boundaries.

\end{frame}

\section{Error Correction}

\begin{frame}{Correcting Mistakes}
\frametitle{How to Correct a Mistake}
\begin{block}{The Problem}
Since you must use a pen, you \textbf{cannot erase} your marks.
\end{block}

\textbf{WRONG Ways to Fix Mistakes:}
\begin{itemize}
\item Crossing out the wrong answer
\item Scribbling over incorrect marks
\item Writing "wrong" next to mistakes
\item Attempting to white-out errors
\end{itemize}

\begin{block}{The ONLY Correct Solution}
Raise your hand and ask the exam supervisor for a \textbf{new answer sheet}.
\end{block}

The scanner will interpret any additional marks as errors, so a clean sheet is your only option.
\end{frame}

\section{Practice Examples}

\begin{frame}{I Do: Registration Number Example}
\frametitle{I Do: Registration Number Demonstration}
Let me show you how to properly fill out registration number \textbf{67890}:

\textbf{Step 1 - Write the digits:}
\begin{itemize}
\item Box 1: Write "6"
\item Box 2: Write "7"
\item Box 3: Write "8"
\item Box 4: Write "9"
\item Box 5: Write "0"
\end{itemize}

\textbf{Step 2 - Mark the bubbles:}
\begin{itemize}
\item Column 1: Mark the "6" bubble with clear X
\item Column 2: Mark the "7" bubble with clear X
\item Continue for remaining digits...
\end{itemize}

\end{frame}


\section{Final Checklist}

\begin{frame}{Before You Submit}
\frametitle{Final Submission Checklist}
Complete this checklist before turning in your exam:

\begin{block}{Personal Information}
\begin{itemize}
\item[$\square$] Name written clearly
\item[$\square$] Signature provided
\item[$\square$] Registration number digits written correctly
\item[$\square$] Registration number bubbles marked correctly
\end{itemize}
\end{block}

\begin{block}{Answer Quality}
\begin{itemize}
\item[$\square$] Every multiple-choice question has exactly one X
\item[$\square$] All marks are dark and clear
\item[$\square$] Written responses are inside designated boxes
\end{itemize}
\end{block}

\begin{block}{Physical Condition}
\begin{itemize}
\item[$\square$] Answer sheet is clean and undamaged
\end{itemize}
\end{block}
\end{frame}

\begin{frame}{Quick Reference: Dos and Don'ts}
\frametitle{Quick Reference Guide}
\begin{columns}
\begin{column}{0.5\textwidth}
\textbf{✅ DO:}
\begin{itemize}
\item Use blue or black pen
\item Mark with clear X inside boxes
\item Fill registration number perfectly
\item Keep answers in designated areas
\item Ask for new sheet if you make mistakes
\item Handle sheet carefully
\end{itemize}
\end{column}

\begin{column}{0.5\textwidth}
\textbf{❌ DON'T:}
\begin{itemize}
\item Fold, crease, or damage paper
\item Mark more than one answer per question
\item Cross out mistakes
\item Write outside answer areas
\item Use pencil or erasers
\item Modify pre-filled sections
\end{itemize}
\end{column}
\end{columns}

\begin{block}{Remember}
When in doubt, ask your exam supervisor for help!
\end{block}
\end{frame}

\begin{frame}{Summary}
\frametitle{Key Takeaways}
\textbf{Success with NOPS exams requires:}
\begin{enumerate}
\item Careful handling of your answer sheet
\item Precise completion of personal information
\item Proper marking technique for all answers
\item Following error correction protocols
\item Thorough final review before submission
\end{enumerate}

\begin{block}{Final Thought}
The computer scanner is precise but unforgiving. Your attention to detail in following these procedures will ensure your knowledge is accurately reflected in your exam score.
\end{block}

\textbf{Good luck on your exam!}

\end{frame}


\begin{frame}{Frame Title}
    $\omega$
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch08_slides_momentum.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page information
\title[Understanding Momentum]{PHYS11 CH8: Understanding Momentum}
\subtitle{From Everyday Motion to Conservation Laws}
\author[Mr. Gullo]{Mr. Gullo}
\date[]{}
\institute{}

\begin{document}

% Title frame
\begin{frame}
\titlepage
\end{frame}

% Opening Question Frame
\begin{frame}{Think About This...}
\begin{block}{Opening Scenario}
Why is it harder to stop...
\begin{itemize}
\item A heavy truck moving slowly, or
\item A light car moving quickly?
\end{itemize}
\end{block}
\begin{itemize}
\item This question introduces us to the concept of \textbf{momentum}
\item By the end of this lesson, you'll understand exactly why both situations are challenging!
\end{itemize}
\end{frame}

% Learning Objectives
\begin{frame}{Learning Objectives}
\begin{block}{By the end of this lesson, you will be able to:}
\begin{itemize}
\item \textbf{Explain} momentum using everyday examples
\item \textbf{Calculate} the momentum of moving objects
\item \textbf{Describe} how force and time relate to changing momentum
\item \textbf{Apply} conservation of momentum to real situations
\item \textbf{Analyze} different types of collisions
\end{itemize}
\end{block}
\end{frame}

% What is Momentum? Conceptual Introduction
\begin{frame}{Understanding Momentum: The Basics}
\begin{block}{Momentum: A Measure of Motion}
Think of momentum as an object's "motion strength"
\end{block}

\begin{itemize}
\item Like a moving bowling ball vs. a moving ping pong ball
\item Two factors determine momentum:
    \begin{itemize}
    \item How much stuff is moving (mass)
    \item How fast it's moving (velocity)
    \end{itemize}
\item More mass OR more velocity = more momentum
\end{itemize}

\begin{alertblock}{Key Point}
Momentum combines MASS and VELOCITY into a single measure of motion
\end{alertblock}
\end{frame}

% Mathematical Definition
\begin{frame}{The Mathematics of Momentum}
\begin{block}{Definition}
Momentum ($\vec{p}$) = mass × velocity
$$\vec{p} = m\vec{v}$$
\end{block}

\begin{columns}
\column{0.5\textwidth}
\textbf{Units:}
\begin{itemize}
\item Mass (kg)
\item Velocity (m/s)
\item Momentum (kg⋅m/s)
\end{itemize}

\column{0.5\textwidth}
\textbf{Remember:}
\begin{itemize}
\item Momentum is a vector
\item Direction matters!
\item Same direction as velocity
\end{itemize}
\end{columns}
\end{frame}

% Real-World Examples Frame
\begin{frame}{Momentum in Real Life}
\begin{block}{Sports Examples}
\begin{itemize}
\item Football player running (large mass, moderate velocity)
\item Baseball pitch (small mass, high velocity)
\item Ice skater gliding (medium mass, low velocity)
\end{itemize}
\end{block}

\begin{block}{Transportation Examples}
\begin{itemize}
\item Heavy truck at highway speed
\item Bicycle commuter
\item High-speed train
\end{itemize}
\end{block}
\end{frame}

% I Do: Worked Example
\begin{frame}{Example: Understanding Momentum (I Do)}
\begin{block}{Problem}
A 75 kg football player runs at 8 m/s. Calculate their momentum.
\end{block}

\pause

\begin{block}{Step-by-Step Solution}
1. Identify what we know:
   \begin{itemize}
   \item Mass (m) = 75 kg
   \item Velocity (v) = 8 m/s
   \end{itemize}

   \pause

2. Apply the momentum formula:
   $$\vec{p} = m\vec{v} = (75\text{ kg})(8\text{ m/s}) = 600\text{ kg⋅m/s}$$
\end{block}
\end{frame}

% We Do: Interactive Example
\begin{frame}{Let's Try Together (We Do)}
\begin{block}{Problem}
A 0.145 kg baseball is thrown at 40 m/s. Calculate:
\begin{itemize}
\item The ball's momentum
\item Compare it to the football player's momentum
\end{itemize}
\end{block}

\pause

\begin{block}{Solution Steps}
1. Calculate baseball momentum:
   $$\vec{p} = (0.145\text{ kg})(40\text{ m/s}) = 5.8\text{ kg⋅m/s}$$

2. Compare:
   \begin{itemize}
   \item Baseball: 5.8 kg⋅m/s
   \item Football player: 600 kg⋅m/s
   \end{itemize}
\end{block}
\end{frame}

% Impulse Introduction
\begin{frame}{Changing Momentum: Understanding Impulse}
\begin{block}{Key Concept: Impulse}
Impulse = Force × Time = Change in Momentum
$$F\Delta t = \Delta p$$
\end{block}

\begin{itemize}
\item Same effect can be achieved by:
    \begin{itemize}
    \item Large force for short time
    \item Small force for long time
    \end{itemize}
\item Examples:
    \begin{itemize}
    \item Catching a baseball (extend arms to increase time)
    \item Car airbags (increase collision time)
    \item Karate board break (large force, very short time)
    \end{itemize}
\end{itemize}
\end{frame}

% Conservation of Momentum Introduction
\begin{frame}{Conservation of Momentum}
\begin{block}{The Big Idea}
In an isolated system (no external forces), total momentum stays constant
\end{block}

\pause

\begin{columns}
\column{0.5\textwidth}
\textbf{Before Collision}
\begin{itemize}
\item Object 1 momentum
\item Object 2 momentum
\item Total = $p_1 + p_2$
\end{itemize}

\pause

\column{0.5\textwidth}
\textbf{After Collision}
\begin{itemize}
\item Object 1 new momentum
\item Object 2 new momentum
\item Total = $p'_1 + p'_2$
\end{itemize}
\end{columns}

\pause

\begin{alertblock}{Key Equation}
$$p_1 + p_2 = p'_1 + p'_2$$
\end{alertblock}
\end{frame}

% Types of Collisions
\begin{frame}{Understanding Collisions}
\begin{columns}
\column{0.5\textwidth}
\textbf{Elastic Collisions}
\begin{itemize}
\item Objects bounce apart
\item Kinetic energy preserved
\item Example: Pool balls
\item Perfect elasticity rare
\end{itemize}

\column{0.5\textwidth}
\textbf{Inelastic Collisions}
\begin{itemize}
\item Objects stick together
\item Energy converted to heat/sound
\item Example: Car crashes
\item More common in real life
\end{itemize}
\end{columns}

\pause

\begin{alertblock}{Remember}
Momentum is conserved in BOTH types of collisions!
\end{alertblock}
\end{frame}

% You Do: Practice Problem
\begin{frame}{Your Turn! (You Do)}
\begin{block}{Challenge Problem}
A 1200 kg car moving at 15 m/s collides with a stationary 800 kg car. They stick together.
What is their final velocity?
\end{block}

\begin{block}{Hints}
\begin{itemize}
\item This is an inelastic collision (they stick together)
\item Use conservation of momentum
\item Remember: mass$_1$v$_1$ + mass$_2$v$_2$ = (mass$_1$ + mass$_2$)v$_\text{final}$
\end{itemize}
\end{block}

\pause

\begin{block}{Solution Framework}
$(1200)(15) + (800)(0) = (1200 + 800)v_\text{final}$
\end{block}
\end{frame}

% Real-World Applications
\begin{frame}{Momentum in the Real World}
\begin{block}{Safety Applications}
\begin{itemize}
\item Vehicle crumple zones
\item Sports padding and helmets
\item Playground surface materials
\end{itemize}
\end{block}

\begin{block}{Engineering Applications}
\begin{itemize}
\item Rocket propulsion
\item Impact testing
\item Vehicle design
\end{itemize}
\end{block}
\end{frame}

% Summary Frame
\begin{frame}{Key Takeaways}
\begin{block}{Main Concepts}
\begin{itemize}
\item Momentum = mass × velocity
\item Impulse changes momentum
\item Momentum is conserved in isolated systems
\item Collisions can be elastic or inelastic
\end{itemize}
\end{block}

\begin{alertblock}{Why This Matters}
Understanding momentum helps us:
\begin{itemize}
\item Design safer vehicles
\item Improve sports equipment
\item Predict motion in collisions
\item Solve real-world problems
\end{itemize}
\end{alertblock}
\end{frame}

% Questions Frame
\begin{frame}{Questions to Consider}
\begin{block}{Think About}
\begin{itemize}
\item Why do heavy vehicles need longer to stop?
\item How do martial artists break boards?
\item Why do catchers "give" with the ball?
\item How do airbags protect us?
\end{itemize}
\end{block}

\begin{block}{Next Steps}
\begin{itemize}
\item Practice with example problems
\item Connect concepts to daily life
\item Observe momentum in action
\end{itemize}
\end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/ch03_Lab_ReactionAcceleration-Kinematics.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../latex-beamer/shared/templates/ds9_theme}

% Title page configuration
\title[Reaction Time Lab]{PHYS11 CH: Reaction Time Lab}
\subtitle{Measuring Human Reaction Time with Kinematics}
\author[Mr. Gullo]{Mr. Gullo}
\date[Sep 27, 2025]{September 27, 2025}

\begin{document}

\frame{\titlepage}

\section{Introduction}

\begin{frame}
\frametitle{Learning Objectives}
\framesubtitle{What You Will Accomplish Today}
    \begin{itemize}
        \item \textbf{Apply Kinematics:} Use kinematic equations to calculate an unknown variable (time) from experimental data.
        \item \textbf{Connect Concepts:} Understand the connection between a physical measurement (distance) and a calculated physics quantity (reaction time).
        \item \textbf{Improve Lab Skills:} Practice making careful measurements, collecting multiple trials, and identifying sources of experimental uncertainty.
    \end{itemize}
\end{frame}

\begin{frame}
\frametitle{Video: The Science of Reaction Time}
    \vfill
    \begin{alertblock}{Media}
        Play the context video about reaction time in sports.
    \end{alertblock}
    \vfill
\end{frame}

\begin{frame}
\frametitle{Summary: What is Reaction Time?}
\framesubtitle{Key Ideas from the Video}
    \begin{block}{Definition}
        Reaction time is the total delay between detecting a stimulus and executing a physical response.
    \end{block}
    \pause
    \begin{itemize}
        \item The process involves a signal traveling from your senses (eyes) to your brain, and then from your brain to your muscles. \pause
        \item This delay, though short, is measurable and critical in high-speed situations. \pause
        \item In sports, even a few hundredths of a second can determine the outcome.
    \end{itemize}
\end{frame}


\begin{frame}
\frametitle{Video: The Science of Hitting a Fastball}
    \vfill
    \begin{alertblock}{Media}
        Play the video on hitting a fastball.
    \end{alertblock}
    \vfill
\end{frame}

\begin{frame}
\frametitle{Summary: Factors Affecting Reaction Time}
\framesubtitle{What Makes You Faster or Slower?}
    As the videos showed, your reaction time is not always the same. Several factors can influence it:
    \begin{columns}[T]
        \column{0.48\textwidth}
            \begin{block}{Physiological Factors}
                \begin{itemize}
                    \item \textbf{Alertness:} Tiredness slows down nerve signals.
                    \item \textbf{Stimulants:} Caffeine can temporarily shorten reaction time.
                \end{itemize}
            \end{block}

        \column{0.48\textwidth}
            \begin{block}{Cognitive Factors}
                \begin{itemize}
                    \item \textbf{Distractions:} Loud noises or other tasks increase the brain's processing time.
                    \item \textbf{Prediction:} Elite athletes "see into the future" by anticipating the trajectory of a ball based on the pitcher's body language.
                \end{itemize}
            \end{block}
    \end{columns}
    \vfill
    \begin{alertblock}{Think About This:}
    As you do the lab, consider which of these factors might be affecting your own results today.
    \end{alertblock}
\end{frame}

\section{The Physics of the Experiment}

\begin{frame}
\frametitle{The Physics of the Ruler Drop}
\framesubtitle{The Equation We Will Use}
    We will use the derivation from this kinematic equation:
    \[ \Delta x = v_0 t + \frac{1}{2} a t^2 \]
    \pause
    Since the ruler is dropped ($v_0=0$) and in free fall ($a=g$), it simplifies and we can solve for time ($t$).

    \begin{block}{Your Reaction Time Equation}
        \[ t = \sqrt{\frac{2 \Delta x}{g}} \]
    \end{block}
    \pause
    \vfill
    \begin{columns}[T]
        \column{0.5\textwidth}
            \textbf{Variables:}
            \begin{itemize}
                \item $t$ = reaction time
                \item $\Delta x$ = distance ruler fell
                \item $g = 9.8 \, \text{m/s}^2$
            \end{itemize}
        \column{0.5\textwidth}
            \textbf{Units:}
            \begin{itemize}
                \item $t$ in \textbf{seconds (s)}
                \item $\Delta x$ must be in \textbf{meters (m)!}
                \item $g$ in \textbf{m/s$^2$}
            \end{itemize}
    \end{columns}
\end{frame}

\begin{frame}
\frametitle{Lab Procedure: Setup}
\framesubtitle{Equipment and Safety}
    \begin{columns}[T]
        \column{0.48\textwidth}
        \textbf{Equipment:}
            \begin{itemize}
                \item One 30 cm ruler
                \item A partner
                \item Paper and pencil for recording data
            \end{itemize}

        \column{0.48\textwidth}
        \textbf{Safety First!}
            \begin{alertblock}{}
                Move slowly and carefully. Do not grab at the ruler too quickly or you might hit your partner's hand.
            \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
\frametitle{Lab Procedure: Data Collection}
\framesubtitle{How to Do the Lab}
    \begin{enumerate}
        \item \textbf{Hold:} Your partner holds the ruler vertically. The 0 cm mark should be at the bottom.
        \item \textbf{Ready:} Place your thumb and index finger around the 0 cm mark, but \textit{do not touch} the ruler.
        \item \textbf{Drop:} Your partner will drop the ruler without warning.
        \item \textbf{Catch:} As soon as you see it fall, catch it!
        \item \textbf{Measure:} Read the distance in centimeters at the top edge of your fingers. This is $\Delta x$ for this trial.
        \item \textbf{Record:} Write this distance in your data table.
        \item \textbf{Repeat:} Perform a total of 5 trials to get a good average.
    \end{enumerate}
\end{frame}

\begin{frame}
\frametitle{Data Analysis Steps}
\framesubtitle{From Distance to Time}
    Once you have your 5 distance measurements:

    \begin{enumerate}
        \item \textbf{Find the Average:} Add your 5 distances together and divide by 5. This gives you an average distance in \textbf{cm}. \pause

        \item \alert{\textbf{Convert Units!}} Take your average distance in cm and divide by 100 to convert it to \textbf{meters (m)}. This is your final $\Delta x$. \pause

        \item \textbf{Calculate Time:} Plug your $\Delta x$ (in meters) into the equation to find your reaction time in seconds.
            \[ t = \sqrt{\frac{2 \times \Delta x}{9.8}} \]
    \end{enumerate}
\end{frame}

\begin{frame}
\frametitle{Homework: Analysis \& Discussion}
\framesubtitle{Thinking About Your Results}
    After you calculate your reaction time, answer these questions in your lab notebook.
    \begin{itemize}
        \item Are your measurements for each trial exactly the same? Why or why not? What does this tell you about measurement?
        \item What do you think were the biggest sources of error in this experiment? How could you make it more accurate?
        \item If you performed this experiment on Jupiter ($g \approx 25 \, \text{m/s}^2$), would the ruler fall a longer or shorter distance during the same reaction time? Explain your answer.
        \item How could you apply what you learned about reaction time to a real-world situation (e.g., driving, sports)?
    \end{itemize}
\end{frame}

\begin{frame}
\frametitle{Summary}
\framesubtitle{Key Takeaways}
    \begin{itemize}
        \item Human reaction time is a physical delay that can be measured using physics. \pause
        \item By measuring the \textbf{distance} an object falls in free fall, we can calculate the \textbf{time} it was falling. \pause
        \item We used the principles of kinematics for an object in \textbf{free fall} ($v_0 = 0$, $a=g$) to derive our key lab equation:
    \end{itemize}
    \begin{center}
    \begin{block}{}
        \[ t = \sqrt{\frac{2 \Delta x}{g}} \]
    \end{block}
    \end{center}
    \vfill
    \begin{alertblock}{}
        This lab is a perfect example of how we use physics models to understand and quantify the world around us.
    \end{alertblock}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump11/review_exam-shorter.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

\title[NOPS Guide]{NOPS Answer Sheet Guide}
\subtitle{Professional Exam Completion Standards}
\author[Mr. Gullo]{Mr. Gullo}
\date[June 2025]{June, 2025}

\begin{document}

\frame{\titlepage}

\begin{frame}{Learning Objectives}
\frametitle{Learning Objectives}
By the end of this guide, you will be able to:
\begin{itemize}
\item Properly handle and maintain your NOPS answer sheet
\item Complete personal information and registration accurately
\item Apply correct marking techniques for optimal scanning
\item Follow appropriate error correction protocols
\end{itemize}
\end{frame}

\begin{frame}{Essential Requirements}
\frametitle{NOPS System Requirements}
\begin{block}{Critical Materials}
\begin{itemize}
\item \textbf{Blue or black pen only} (no pencils or erasers)
\item Clean, flat working surface
\item Careful attention to detail
\end{itemize}
\end{block}

\begin{block}{Answer Sheet Care}
\begin{itemize}
\item Keep sheet clean, dry, and flat at all times
\item Avoid folding, creasing, or damaging the paper
\item Handle with clean hands only
\end{itemize}
\end{block}
\end{frame}

\begin{frame}{Registration Number Process}
\frametitle{Two-Step Registration Procedure}
\begin{block}{Step 1: Write Digits}
Carefully write your registration number in the boxes at the top of the grid, placing one digit per box.
\end{block}

\begin{block}{Step 2: Mark Bubbles}
For each digit written above, locate the corresponding bubble in the column directly below and mark with a clear X.
\end{block}

\textbf{Example:} Registration number 12345
\begin{itemize}
\item Write "1" in first box → Mark "1" bubble below
\item Write "2" in second box → Mark "2" bubble below
\item Continue for all five digits
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Answer Sheet Reference}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys11-exam-prep-nops-answer-sheet.png}
\end{figure}
\end{frame}

\begin{frame}{Answer Marking Standards}
\frametitle{Proper Marking Technique}
\begin{block}{Multiple Choice Answers}
\begin{itemize}
\item Mark exactly \textbf{one} answer per question
\item Use a clear X that fits completely inside the designated box
\item Ensure marks are dark and legible
\item Do not extend marks outside box boundaries
\end{itemize}
\end{block}

\begin{block}{Written Responses}
\begin{itemize}
\item Use designated answer boxes on separate page
\item Keep all work within box boundaries
\item Write legibly in blue or black pen
\item Include complete solutions and explanations
\end{itemize}
\end{block}
\end{frame}

\begin{frame}{Error Correction Protocol}
\frametitle{Managing Mistakes}
\begin{block}{Important: No Erasures Allowed}
Since pen marks cannot be erased, any marking errors require immediate attention.
\end{block}

\textbf{Incorrect approaches:}
\begin{itemize}
\item Crossing out wrong answers
\item Scribbling over incorrect marks
\item Using correction fluid or tape
\end{itemize}

\textbf{Correct procedure:}
\begin{itemize}
\item Raise your hand immediately
\item Request a new answer sheet from the exam supervisor
\item Transfer all correct answers to the new sheet
\end{itemize}
\end{frame}

\begin{frame}{Pre-Submission Checklist}
\frametitle{Quality Assurance Review}
\begin{columns}
\begin{column}{0.5\textwidth}
\textbf{Personal Information:}
\begin{itemize}
\item[$\square$] Name written clearly
\item[$\square$] Signature provided
\item[$\square$] Registration number complete
\item[$\square$] Bubbles marked correctly
\end{itemize}
\end{column}

\begin{column}{0.5\textwidth}
\textbf{Answer Quality:}
\begin{itemize}
\item[$\square$] One mark per question
\item[$\square$] All marks clear and dark
\item[$\square$] No stray marks present
\item[$\square$] Sheet undamaged
\end{itemize}
\end{column}
\end{columns}

\begin{block}{Final Step}
Review your completed answer sheet thoroughly before submission to ensure optimal scanning results.
\end{block}
\end{frame}

\end{document}
```

</file_contents>

### Physics 12 Presentations

<file_contents>
File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch04_slides_motion.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../latex-beamer/shared/templates/ds9_theme}

% Title page configuration
\title[Newton's Laws and Systems]{PHYS12 CH: 4.1-4.4, 4.6-4.8}
\subtitle{Force, Mass, Systems, and Fundamental Forces}
\author[Mr. Gullo]{Mr. Gullo}
\date[Sep 2024]{September 17, 2024}

\begin{document}
\frame{\titlepage}

\section{Introduction}

\begin{frame}
\frametitle{Learning Objectives}
\begin{itemize}
    \item Understand the definition of \textbf{force} as a vector. \pause
    \item Define \textbf{mass} and \textbf{inertia}. \pause
    \item State and apply Newton's First, Second, and Third Laws of Motion. \pause
    \item Define a \textbf{system of interest} and distinguish between \textbf{external} and \textbf{internal} forces. \pause
    \item Draw and use \textbf{Free-Body Diagrams (FBDs)} to solve problems. \pause
    \item Apply Newton's laws to solve problems for both single objects and multi-body systems. \pause
    \item Analyze complex two-dimensional force problems with vector addition. \pause
    \item Identify and describe the \textbf{four fundamental forces} of nature and their properties. \pause
    \item Understand how forces act at a distance through \textbf{force fields} and particle exchange.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{From Physics 11 to Physics 12}
\begin{columns}[T]
\column{0.48\textwidth}
\begin{alertblock}{Review from Physics 11}
\begin{itemize}
    \item Newton's Laws for a \textbf{single object}.
    \item Drawing a Free-Body Diagram for one object.
    \item Identifying forces like gravity ($\vec{w}$), normal force ($\vec{N}$), and tension ($\vec{T}$).
    \item Solving for acceleration or force on one object using $\sum \vec{F} = m\vec{a}$.
\end{itemize}
\end{alertblock}

\column{0.48\textwidth}
\begin{exampleblock}{New in Physics 12}
\begin{itemize}
    \item Applying Newton's Laws to \textbf{systems of multiple objects}.
    \item Strategically choosing the "system of interest" to simplify problems.
    \item Understanding how internal forces cancel out within a system.
    \item Solving for forces between connected objects.
\end{itemize}
\end{exampleblock}
\end{columns}
\end{frame}

\section{Fundamental Concepts Review}

\begin{frame}
\frametitle{Concept: What is a Force?}
\begin{itemize}
    \item A force is fundamentally a \textbf{push} or a \textbf{pull}. \pause
    \item It is a \textbf{vector quantity}, meaning it has both \alert{magnitude} (how strong it is) and \alert{direction}. \pause
    \item The standard unit of force is the \textbf{Newton (N)}.
    \begin{itemize}
        \item 1 N = 1 kg $\cdot$ m/s$^2$
    \end{itemize} \pause
    \item Forces are added together using vector addition to find the \textbf{net force} ($\vec{F}_{net}$).
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Concept: The Free-Body Diagram (FBD)}
A Free-Body Diagram is a simplified drawing used to analyze the forces on an object or system.
\begin{itemize}
    \item The system of interest is represented by a single \textbf{dot}. \pause
    \item We draw vector arrows representing all \textbf{external forces} acting \textit{on} the system. \pause
    \item We do \textbf{not} draw internal forces or forces exerted \textit{by} the system. \pause
    \item The FBD is the most critical first step for solving almost any dynamics problem.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Context: Visualizing Net Force}
\begin{itemize}
    \item Let's visualize how forces on an object combine to produce a net force using a Free-Body Diagram.
    \pause
    \item We will use the example of two ice skaters pushing a third skater from Figure 4.3 in your textbook.
    \pause
    \item The two pushes ($\vec{F}_1$ and $\vec{F}_2$) are individual external forces. The \textbf{net force} ($\vec{F}_{tot}$) is their vector sum, which determines the direction of acceleration.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Visualization: Adding Forces on an FBD}
\begin{alertblock}{[Diagram based on Figure 4.3]}
\begin{columns}[T]
\column{0.5\textwidth}
    \textbf{Physical Situation:}
    \begin{itemize}
        \item An overhead view shows two skaters applying forces $\vec{F}_1$ and $\vec{F}_2$ to a third skater.
    \end{itemize}
    \alert{[Image of two skaters pushing a third skater]}
\column{0.5\textwidth}
    \textbf{Free-Body Diagram:}
    \begin{itemize}
        \item The third skater is a dot.
        \item $\vec{F}_1$ and $\vec{F}_2$ are drawn tail-to-dot.
        \item The resultant vector $\vec{F}_{tot}$ shows the net force.
    \end{itemize}
    \alert{[FBD showing two force vectors from a point]}
\end{columns}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Newton's First Law: The Law of Inertia}
\begin{itemize}
    \item "A body at rest remains at rest, or, if in motion, remains in motion at a constant velocity unless acted on by a \textbf{net external force}." \pause
    \item This means an object's velocity \textbf{will not change} if the net force on it is zero ($\vec{F}_{net} = 0$). \pause
    \item \textbf{Inertia} is the property of an object to resist changes in its state of motion. \pause
    \item \textbf{Mass (m)} is the quantitative measure of inertia. More mass means more inertia.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Newton's Third Law: Action-Reaction}
\begin{itemize}
    \item "Whenever one body exerts a force on a second body, the first body experiences a force that is equal in magnitude and opposite in direction to the force that it exerts." \pause
    \item Mathematically: $\vec{F}_{A \text{ on } B} = -\vec{F}_{B \text{ on } A}$ \pause
    \item \alert{CRITICAL POINT}: The two forces in an action-reaction pair always act on \textbf{different objects}. \pause
    \begin{itemize}
        \item Therefore, they \textbf{never} cancel each other out when analyzing the motion of a single object.
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Context: Visualizing Action-Reaction}
\begin{itemize}
    \item Let's visualize how action-reaction pairs work. The key is to see that the forces act on different systems. \pause
    \item We will look at a swimmer pushing off the wall of a pool (based on Figure 4.9). \pause
    \item The "action" is the swimmer pushing on the wall.
    \item The "reaction" is the wall pushing on the swimmer. Only the reaction force affects the swimmer's motion.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Visualization: Swimmer at the Wall}
\begin{alertblock}{[Diagram based on Figure 4.9]}
    \begin{itemize}
        \item \textbf{Force 1 (Action):} The swimmer's feet exert a force $\vec{F}_{feet\_on\_wall}$ on the wall. This force acts ON THE WALL.
        \pause
        \item \textbf{Force 2 (Reaction):} The wall exerts an equal and opposite force $\vec{F}_{wall\_on\_feet}$ on the swimmer. This force acts ON THE SWIMMER.
        \pause
        \item The swimmer accelerates because the net external force on \textit{her} (from the wall) is not zero.
    \end{itemize}
    \alert{[Image showing swimmer pushing off a wall, with force vectors on both swimmer and wall]}
\end{alertblock}
\end{frame}

\section{The Concept of a System}

\begin{frame}
\frametitle{The "System": A Key Problem-Solving Tool}
\begin{itemize}
    \item In physics, a \textbf{system} is the object or collection of objects we choose to analyze. \pause
    \item \textbf{External forces} act on the system from the outside.
    \begin{itemize}
        \item These are the forces that cause the system to accelerate.
        \item They are the only forces shown on an FBD of the system.
    \end{itemize} \pause
    \item \textbf{Internal forces} are forces that objects within the system exert on each other.
    \begin{itemize}
        \item These forces always come in action-reaction pairs and cancel out, so they \textbf{do not affect the system's overall acceleration}.
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Context: Choosing a System}
\begin{itemize}
    \item The choice of system is a strategic decision that can make a problem much easier to solve. \pause
    \item Let's see how changing the system changes which forces are external. \pause
    \item We'll use the example of a professor pushing a cart from Figure 4.10.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Visualization: Professor and Cart Systems}
\begin{alertblock}{[Diagram based on Figure 4.10]}
\begin{columns}[T]
\column{0.48\textwidth}
    \textbf{System 1: (Professor + Cart)}
    \begin{itemize}
        \item External forces: Force from floor on feet, friction.
        \item Internal force: Professor pushing cart, cart pushing professor. These cancel.
    \end{itemize}
\column{0.48\textwidth}
    \textbf{System 2: (Cart Only)}
    \begin{itemize}
        \item External forces: Force from professor on cart, friction.
        \item No internal forces to consider.
    \end{itemize}
\end{columns}
\alert{[Image showing a professor pushing a cart, with boxes drawn around "System 1" and "System 2"]}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Newton's Second Law: The Law of Acceleration}
\begin{itemize}
    \item "The acceleration of a system is directly proportional to and in the same direction as the \textbf{net external force} acting on the system, and is inversely proportional to its total mass." \pause
    \item This is the central, quantitative law of dynamics. It connects force, mass, and motion.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Essential Equations}
\begin{block}{Newton's Second Law}
\centering
$\vec{F}_{net} = m\vec{a}$
\begin{itemize}
    \item $\vec{F}_{net}$ is the vector sum of all \textit{external} forces on the system.
    \item $m$ is the total mass of the system.
    \item $\vec{a}$ is the acceleration of the system.
\end{itemize}
\end{block}
\pause
\begin{block}{Weight (Force of Gravity)}
\centering
$\vec{w} = m\vec{g}$
\begin{itemize}
    \item $\vec{w}$ is the force of gravity on an object.
    \item $m$ is the object's mass.
    \item $\vec{g}$ is the acceleration due to gravity (approx. 9.8 m/s$^2$ down on Earth).
\end{itemize}
\end{block}
\end{frame}

\section{Problem Solving with Systems}

\begin{frame}
\frametitle{I Do: Getting up to Speed (Example 4.3)}
\begin{block}{Problem}
A professor (65.0 kg) pushes a cart (12.0 kg) with equipment (7.0 kg). She exerts a 150 N backward force on the floor. All forces opposing the motion total 24.0 N. Calculate the acceleration.
\end{block}
\pause
\begin{alertblock}{System of Interest}
For this question, our system is the \textbf{professor + cart + equipment} because we want the acceleration of everything together.
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{I Do: GUESS Method (G \& U)}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{G - Givens}
\begin{itemize}
\item $m_{prof} = 65.0$ kg
\item $m_{cart} = 12.0$ kg
\item $m_{equip} = 7.0$ kg
\item Force on floor = 150 N
\item $\implies F_{floor\_on\_prof} = 150$ N [forward]
\item $f = 24.0$ N [backward]
\end{itemize}

\column{0.48\textwidth}
\textbf{U - Unknown}
\begin{itemize}
\item Acceleration, $a = ?$
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I Do: GUESS Method (E)}
\textbf{E - Equation}
\begin{itemize}
    \item Start with Newton's Second Law for the whole system:
    \[ F_{net} = m_{total} a \] \pause
    \item The net external force is the forward force from the floor minus the backward friction:
    \[ F_{net} = F_{floor\_on\_prof} - f \] \pause
    \item The total mass is the sum of all parts:
    \[ m_{total} = m_{prof} + m_{cart} + m_{equip} \] \pause
    \item Rearrange for the unknown, $a$:
    \[ a = \frac{F_{net}}{m_{total}} = \frac{F_{floor\_on\_prof} - f}{m_{prof} + m_{cart} + m_{equip}} \]
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{I Do: GUESS Method (S \& S)}
\textbf{S - Substitute}
\begin{itemize}
    \item First, calculate total mass:
    \[ m_{total} = 65.0 + 12.0 + 7.0 = 84.0 \text{ kg} \]
    \item Now substitute into the acceleration equation:
    \[ a = \frac{150 \text{ N} - 24.0 \text{ N}}{84.0 \text{ kg}} \]
\end{itemize}
\pause
\textbf{S - Solve}
\begin{itemize}
    \item Calculate the final value:
    \[ a = \frac{126 \text{ N}}{84.0 \text{ kg}} = 1.5 \text{ m/s}^2 \]
    \item \boxed{a = 1.5 \text{ m/s}^2 \text{ [forward]}}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{We Do: Force on the Cart (Example 4.4)}
\begin{block}{Problem}
Using the data from the previous problem, calculate the force the professor exerts on the cart.
\end{block}
\pause
\begin{alertblock}{New System of Interest}
Now, our system must be the \textbf{cart + equipment} because the force from the professor is an \textit{external force} on this new system.
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{We Do: GUESS Method (G \& U)}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{G - Givens}
\begin{itemize}
\item $m_{cart} = 12.0$ kg
\item $m_{equip} = 7.0$ kg
\item $m_{sys2} = 19.0$ kg
\item $a = 1.5$ m/s$^2$ (from "I do")
\item $f_{total} = 24.0$ N (The problem states this friction applies to cart wheels and air resistance, so it acts on the cart system).
\end{itemize}

\column{0.48\textwidth}
\textbf{U - Unknown}
\begin{itemize}
\item Force from professor on cart, $F_{prof} = ?$
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{We Do: GUESS Method (E)}
\textbf{E - Equation}
\begin{itemize}
    \item Apply Newton's Second Law to our new system (the cart + equipment):
    \[ F_{net} = m_{sys2} a \]
    \pause
    \item \textbf{Question:} What forces make up $F_{net}$ for this system?
    \begin{itemize}
        \item \textit{Answer: The forward push from the professor ($F_{prof}$) and the backward friction ($f$).}
        \[ F_{prof} - f = m_{sys2} a \]
    \end{itemize}
    \pause
    \item \textbf{Question:} How do we rearrange for the unknown, $F_{prof}$?
    \begin{itemize}
        \item \textit{Answer: Add friction $f$ to both sides.}
        \[ F_{prof} = m_{sys2} a + f \]
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{We Do: GUESS Method (S \& S)}
\textbf{S - Substitute}
\begin{itemize}
    \item Now we plug in the values for our system.
    \pause
    \item \textbf{Question:} What values should we use for $m_{sys2}$, $a$, and $f$?
    \begin{itemize}
        \item $m_{sys2} = 19.0$ kg
        \item $a = 1.5$ m/s$^2$
        \item $f = 24.0$ N
    \end{itemize}
    \[ F_{prof} = (19.0 \text{ kg})(1.5 \text{ m/s}^2) + 24.0 \text{ N} \]
\end{itemize}
\pause
\textbf{S - Solve}
\begin{itemize}
    \item Let's calculate the result.
    \[ F_{prof} = 28.5 \text{ N} + 24.0 \text{ N} = 52.5 \text{ N} \]
    \item \boxed{F_{prof} = 53 \text{ N}}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{You Do: Drag Force on a Barge (Example 4.7)}
\begin{block}{Problem}
Two tugboats push on a barge. Tugboat 1 exerts a force of $2.7 \times 10^5$ N in the x-direction. Tugboat 2 exerts a force of $3.6 \times 10^5$ N in the y-direction. The mass of the barge is $5.0 \times 10^6$ kg and its acceleration is observed to be $7.5 \times 10^{-2}$ m/s$^2$ in the direction of the net applied force from the tugboats.
\newline
\newline
What is the drag force of the water on the barge resisting the motion?
\end{block}

\begin{alertblock}{Hint}
1. Find the magnitude and direction of the total applied force from the tugboats.
2. Calculate the net force needed to cause the observed acceleration ($F_{net}=ma$).
3. The drag force is the difference between the applied force and the net force.
\end{alertblock}
\end{frame}

\section{Additional Worked Examples}

\begin{frame}
\frametitle{Example: Rugby Players (Problem 16)}
A rugby player (90.0 kg) is accelerating at $1.20 \mathrm{~m} / \mathrm{s}^{2}$ backward while being pushed by an opposing player exerting 800 N.
\begin{itemize}
    \item[(a)] What is the force of friction between the losing player's feet and the grass?
    \item[(b)] What force must the winning player (110 kg) exert on the ground to move forward at the same acceleration?
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 16 - Solution (a)}
\begin{columns}[T]
    \column{0.5\textwidth}
        \begin{block}{System of Interest: Losing Player}
            \begin{itemize}
                \item $F_{\text{net}} = F_{push} - f = ma$
                \item $f = F_{push} - ma$
                \item $f = 800 \text{ N} - (90.0 \text{ kg})(1.20 \text{ m/s}^2)$
                \item $f = 800 \text{ N} - 108 \text{ N}$
                \item \boxed{f = 692 \text{ N}}
            \end{itemize}
        \end{block}
    \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.7\linewidth]{Screenshot 2024-10-18 111640.png}
        \end{figure}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Problem 16 - Solution (b)}
\begin{columns}[T]
    \column{0.5\textwidth}
        \begin{block}{System of Interest: Both Players}
            \begin{itemize}
                \item Let $F_{ground}$ be the force the winner exerts on the ground.
                \item $F_{net} = F_{ground} - f = (m_1+m_2)a$
                \item $F_{ground} = (m_1+m_2)a + f$
                \item $F_{ground} = (90.0+110)\text{kg}(1.20 \text{m/s}^2) + 692 \text{N}$
                \item $F_{ground} = 240 \text{N} + 692 \text{N}$
                \item \boxed{F_{ground} = 932 \text{N}}
            \end{itemize}
        \end{block}
    \column{0.5\textwidth}
        \begin{figure}
            \centering
            \includegraphics[width=0.7\linewidth]{Screenshot 2024-10-18 111809.png}
        \end{figure}
\end{columns}
\end{frame}

\section{Conclusion}

\section{Section 4.7: Further Applications}

\begin{frame}
\frametitle{Section 4.7: Further Applications of Newton's Laws}
\framesubtitle{Complex Systems and Multi-Dimensional Forces}
\begin{itemize}
    \item Newton's laws apply to more complex scenarios: \pause
    \begin{itemize}
        \item Two-dimensional force problems with vector addition
        \item Objects with multiple forces at different angles
        \item Real-world applications with drag and resistance
    \end{itemize} \pause
    \item These problems integrate kinematics with dynamics \pause
    \item Strategic use of coordinate systems and trigonometry is essential
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Example: Drag Force on a Barge (Example 4.7)}
\begin{block}{Problem Summary}
Two tugboats push a barge at perpendicular angles ($F_1 = 2.7 \times 10^5$ N in x-direction, $F_2 = 3.6 \times 10^5$ N in y-direction). The barge (mass $5.0 \times 10^6$ kg) accelerates at $7.5 \times 10^{-2}$ m/s$^2$. Find the drag force.
\end{block}
\pause
\begin{alertblock}{Solution Approach}
\begin{itemize}
    \item Find total applied force: $F_{app} = \sqrt{F_1^2 + F_2^2} = 4.5 \times 10^5$ N
    \item Apply Newton's 2nd Law: $F_{net} = F_{app} - F_D = ma$
    \item Result: $F_D = 7.5 \times 10^4$ N (opposite to motion direction)
\end{itemize}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Visualization: Barge Problem (Figure 4.21)}
\begin{alertblock}{[Diagram based on Figure 4.21]}
\textbf{Two-Dimensional Force Analysis:}
\begin{itemize}
    \item Two tugboats apply perpendicular forces to a barge
    \item Force vectors add using Pythagorean theorem
    \item Resultant $\vec{F}_{app}$ points at angle: $\theta = \tan^{-1}(F_2/F_1) = 53°$
    \item Drag force $\vec{F}_D$ opposes motion (fluid resistance)
    \item Net force determines acceleration via $\vec{F}_{net} = m\vec{a}$
\end{itemize}
\alert{[Image: Top view of barge with two tugboat force vectors and drag]}
\end{alertblock}
\end{frame}

\section{Section 4.8: Four Basic Forces}

\begin{frame}
\frametitle{Section 4.8: The Four Basic Forces}
\framesubtitle{Understanding the Fundamental Forces of Nature}
\begin{itemize}
    \item One of the most remarkable simplifications in physics: \pause
    \item \alert{Only four distinct forces account for ALL known phenomena} \pause
    \item Nearly all forces we experience directly are due to ONE basic force: the electromagnetic force \pause
    \item The gravitational force is the only other force we experience directly
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{The Four Basic Forces}
\begin{enumerate}
    \item \textbf{Gravitational Force} \pause
    \item \textbf{Electromagnetic Force} \pause
    \item \textbf{Weak Nuclear Force} \pause
    \item \textbf{Strong Nuclear Force}
\end{enumerate}
\pause
\vspace{1em}
\begin{alertblock}{Key Concept}
All forces act through the exchange of microscopic carrier particles. The characteristics of basic forces are determined by the types of particles exchanged.
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Properties of the Four Basic Forces}
\begin{table}
\scriptsize
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Force} & \textbf{Strength} & \textbf{Range} & \textbf{Type} & \textbf{Carrier} \\
\hline
Gravitational & $10^{-38}$ & $\infty$ & Attractive only & Graviton \\
\hline
Electromagnetic & $10^{-2}$ & $\infty$ & Both & Photon \\
\hline
Weak Nuclear & $10^{-6}$ & $< 10^{-18}$ m & Both & $W^+, W^-, Z^0$ \\
\hline
Strong Nuclear & $1$ & $\approx 10^{-15}$ m & Both & Gluons \\
\hline
\end{tabular}
\end{table}
\pause
\vspace{0.5em}
\begin{itemize}
    \item Strengths are \textbf{relative} to the strong nuclear force
    \item Nuclear forces act over extremely short ranges (size of nucleus or less)
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Gravitational Force}
\begin{itemize}
    \item \textbf{Weakest} of all forces (relative strength: $10^{-38}$) \pause
    \item Always \textbf{attractive} — this is why we notice it despite its weakness \pause
    \item \textbf{Long-range}: acts over infinite distances \pause
    \item Dominant force on astronomical scales (planets, stars, galaxies) \pause
    \item Affects the nature of space and time (general relativity) \pause
    \item \textbf{Carrier particle}: Graviton (proposed but not yet observed)
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Electromagnetic Force}
\begin{itemize}
    \item Combination of electrical forces and magnetic forces \pause
    \item Can be \textbf{attractive or repulsive} \pause
    \item \textbf{Long-range}: acts over extremely large distances \pause
    \item Forces nearly cancel for macroscopic objects \pause
    \begin{itemize}
        \item If they didn't cancel, they would overwhelm gravitational force
    \end{itemize} \pause
    \item Responsible for friction, tension, and all other everyday forces (except gravity) \pause
    \item \textbf{Carrier particle}: Photon
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Real-World Connection: Electromagnetic Dominance}
\begin{itemize}
    \item \textbf{Static electricity}: When you rub a balloon on your hair, electromagnetic forces cause attraction \pause
    \item \textbf{Friction}: Electromagnetic interactions between atoms prevent surfaces from sliding \pause
    \item \textbf{Tension}: Electromagnetic bonds in rope or wire resist being pulled apart \pause
    \item \textbf{Chemistry}: All chemical reactions are electromagnetic interactions between electrons
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Nuclear Forces}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Weak Nuclear Force}
\begin{itemize}
    \item Relative strength: $10^{-6}$
    \item Range: $< 10^{-18}$ m
    \item Responsible for radioactive decay
    \item Determines nuclear stability
    \item Carrier: $W^+$, $W^-$, $Z^0$ bosons
\end{itemize}

\column{0.48\textwidth}
\textbf{Strong Nuclear Force}
\begin{itemize}
    \item \textbf{Strongest} force (reference: 1)
    \item Range: $\approx 10^{-15}$ m
    \item Holds protons and neutrons together in nucleus
    \item Determines relative abundance of elements
    \item Carrier: Gluons (8 types)
\end{itemize}
\end{columns}
\pause
\vspace{1em}
\begin{alertblock}{Important}
We don't experience nuclear forces directly, but they determine the structure of all matter.
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Concept: Action at a Distance}
\begin{itemize}
    \item All forces act at a distance (no physical contact required) \pause
    \item Example: Earth and Moon interact without touching \pause
    \item How is force "carried" between objects? \pause
    \item Answer: Through a \textbf{force field}
\end{itemize}
\pause
\begin{block}{Force Field}
A force field surrounds an object that creates a force. A second object placed in this field experiences a force that depends on its location. The field itself "carries" the force from one object to another.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Context: Visualizing Force Fields}
\begin{itemize}
    \item A force field is a characteristic of the object creating it \pause
    \item The field does NOT depend on test objects placed in it \pause
    \item Example: Earth's gravitational field is a function of Earth's mass and distance from its center \pause
    \item We can write equations for force fields and calculate motions
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Visualization: Electric Force Field (Figure 4.24)}
\begin{alertblock}{[Diagram based on Figure 4.24]}
\textbf{Electric field between opposite charges:}
\begin{itemize}
    \item Field lines show the direction of force on a positive test charge
    \item Between a positive and negative charge, field lines point from positive to negative
    \item Closer field lines indicate stronger force
    \item When a test charge is placed in the field, it experiences a force along the field line direction
    \item This visualizes how electromagnetic force acts at a distance
\end{itemize}
\alert{[Image showing electric field lines between positive and negative charges]}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Particle Exchange Model}
\begin{itemize}
    \item Modern theory (Yukawa, 1935): All forces transmitted by exchange of elementary particles \pause
    \item Analogy: Two people passing a basketball back and forth \pause
    \begin{itemize}
        \item Person throwing exerts force on ball toward other person
        \item Person throwing feels reaction force away from other person
        \item Person catching exerts force to stop the ball
        \item Both feel a force without touching each other!
    \end{itemize} \pause
    \item This is how subatomic carrier particles transmit forces
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Visualization: Particle Exchange (Figure 4.25)}
\begin{alertblock}{[Diagram based on Figure 4.25]}
\textbf{Exchange of masses resulting in repulsive forces:}
\begin{itemize}
    \item Person 1 throws basketball toward Person 2
    \item Force $\vec{F}_{p1}$ on ball creates reaction force $\vec{F}_B$ pushing Person 1 backward
    \item Person 2 catches ball and exerts force $\vec{F}_{p2}$ to stop it
    \item Force $\vec{F}_{p2}$ creates reaction pushing Person 2 backward
    \item Both people experience repulsive force without direct contact
    \item Microscopic version: Particles exchange carrier particles (photons, gluons, etc.)
\end{itemize}
\alert{[Image: Two people exchanging basketball with force vectors shown]}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Unification of Forces}
\begin{itemize}
    \item Scientists seek to find connections between forces \pause
    \item \textbf{Grand Unified Theories (GUTs)}: Attempts to unify all forces into one \pause
    \item \textbf{Success so far}: Under extreme conditions (early universe), electromagnetic and weak nuclear forces are indistinguishable \pause
    \item Combined: \textbf{Electroweak Force} \pause
    \item \textbf{Challenge}: Including gravitational force, which affects space and time itself
\end{itemize}
\pause
\begin{alertblock}{Profound Simplicity}
The universe exhibits remarkable simplicity beneath its apparent complexity. Four forces explain everything we observe.
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Modern Research: Large Hadron Collider (Figure 4.26)}
\begin{alertblock}{[Diagram based on Figure 4.26]}
\textbf{World's largest particle accelerator (Switzerland-France border):}
\begin{itemize}
    \item 27-kilometer circular tunnel underground
    \item Two high-energy proton beams travel in opposite directions
    \item Collisions occur at nearly the speed of light
    \item Energy: 14 trillion electron volts available
    \item \textbf{Goal}: Detect new particles and force carriers
    \item Notable discovery: Higgs boson (explains why particles have mass)
    \item External magnets control beam path
\end{itemize}
\alert{[Image: Cross-section of LHC collision tube with beam paths]}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Detecting Gravitational Waves: LISA Project (Figure 4.27)}
\begin{alertblock}{[Diagram based on Figure 4.27]}
\textbf{Space-based gravitational wave detector:}
\begin{itemize}
    \item Three satellites in space above Earth
    \item Arranged in equilateral triangle (5,000,000 km sides!)
    \item Measures relative positions to detect passing gravitational waves
    \item Required accuracy: within 10\% of atomic size
    \item Predicted launch: 2030s
    \item Will confirm predictions of general relativity
    \item Graviton (carrier particle) not yet directly observed
\end{itemize}
\alert{[Image: LISA satellite triangle configuration orbiting Earth]}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Black Hole Imaging: Event Horizon Telescope (Figure 4.28)}
\begin{alertblock}{[Diagram based on Figure 4.28]}
\textbf{Supermassive black hole at center of M87 galaxy:}
\begin{itemize}
    \item Image shows polarization from powerful magnetic fields
    \item Demonstrates electromagnetic force at extreme scales
    \item Created by combining data from telescopes worldwide
    \item Black hole's gravity (weakest force!) dominates at massive scales
    \item Event horizon: boundary where gravity prevents light escape
    \item Magnetic fields (electromagnetic force) create jets of material
\end{itemize}
\alert{[Image: Polarized light around M87 black hole showing magnetic field structure]}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Reading Homework}
Please read the following section from Chapter 4 in your textbook:
\begin{itemize}
    \item \textbf{Section 4.5: Normal, Tension, and Other Examples of Forces}
    \begin{itemize}
        \item Detailed examples of Normal Force on inclines and Tension in various scenarios
        \item These are specific applications of the electromagnetic force
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Summary}
\begin{itemize}
    \item \textbf{Newton's First Law} defines inertia and the condition for constant velocity ($\vec{F}_{net}=0$). \pause
    \item \textbf{Newton's Third Law} describes action-reaction pairs, which act on different objects. \pause
    \item \textbf{Newton's Second Law ($\vec{F}_{net}=m\vec{a}$)} is the core problem-solving tool that links forces to motion. \pause
    \item The key to solving complex dynamics problems is to correctly \alert{define the system of interest}. \pause
    \item \textbf{All forces in nature} can be explained by just four fundamental forces. \pause
    \item Every analysis should begin with a \textbf{Free-Body Diagram} for your chosen system.
\end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch03-00_twodmnkinematics.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Short Title]{PHYS12 CH:2.1-2.8 and 3.1-3.5}
\subtitle{Kinematics in One and Two Dimensions}
\author[Mr. Gullo]{Mr. Gullo}
\date[Sep 12, 2025]{September 12, 2025}

\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Learning Objectives}
\begin{columns}[T]
    \begin{column}{0.5\textwidth}
        \textbf{1D Kinematics:}
        \begin{itemize}
            \item Define position, displacement, distance, velocity, speed, and acceleration.
            \item Distinguish between scalar and vector quantities.
            \item Interpret graphs of position, velocity, and acceleration vs. time.
            \item Use kinematic equations to solve problems for objects with constant acceleration.
            \item Describe the motion of objects in free fall.
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \textbf{2D Kinematics:}
        \begin{itemize}
            \item Understand the independence of horizontal and vertical motions.
            \item Add and subtract vectors graphically and analytically.
            \item Resolve vectors into perpendicular components.
            \item Apply kinematic equations to solve projectile motion problems.
            \item Use vector addition to solve relative velocity problems.
        \end{itemize}
    \end{column}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{From Physics 11 to Physics 12}
\begin{block}{Building on Foundations}
This course builds directly upon the concepts you learned in Physics 11. We'll quickly review Chapter 2 (1D kinematics) and extend to 2D motion.
\end{block}

\begin{columns}[T]
    \begin{column}{0.5\textwidth}
        \alert{From Chapter 2 (1D)}
        \begin{itemize}
            \item<2-> Position, displacement, distance
            \item<3-> Scalars vs. vectors (+/- directions)
            \item<4-> Kinematic equations for constant acceleration
            \item<5-> Free fall and graphical analysis
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \alert{New in 2D}
        \begin{itemize}
            \item<2-> Vector components and trigonometry
            \item<3-> Independence of horizontal/vertical motion
            \item<4-> Projectile motion analysis
            \item<5-> Relative velocity problems
        \end{itemize}
    \end{column}
\end{columns}
\end{frame}

\section{1D Kinematics Review}

\begin{frame}
\frametitle{Reference to Chapter 2: 1D Kinematics}
\framesubtitle{Foundation for 2D Motion}
\begin{block}{Quick Reference}
For detailed explanations of 1D kinematics concepts, see \textbf{Chapter 2 slides}:
\begin{itemize}
    \item Position, displacement, and distance
    \item Scalars vs. vectors with detailed examples
    \item Full derivation of kinematic equations
    \item Free fall motion and analysis
    \item Graphical analysis with worked examples
    \item GUESS method for problem solving
\end{itemize}
\end{block}
\begin{alertblock}{This Chapter}
We'll focus on extending these concepts to 2D motion using vector components!
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{1D Kinematics: Essential Review}
\framesubtitle{Building on Chapter 2 Foundations}
\begin{block}{Core Concepts (From Chapter 2)}
\begin{itemize}
    \item \textbf{Position vs. Displacement}: $\Delta x = x_f - x_0$ (vector)
    \item \textbf{Distance}: Total path length (scalar, always positive)
    \item \textbf{Velocity}: $\bar{v} = \Delta x / \Delta t$ (vector)
    \item \textbf{Speed}: Distance/time (scalar)
    \item \textbf{Acceleration}: $\bar{a} = \Delta v / \Delta t$ (vector)
\end{itemize}
\end{block}
\alert{Key 2D Extension}: In 1D, direction was simple (+ or -). In 2D, we need full vector mathematics!
\end{frame}

\begin{frame}
\frametitle{Vectors in 1D vs. 2D: Quick Review}
\framesubtitle{From Simple Signs to Full Components}
\begin{columns}[T]
    \begin{column}{0.5\textwidth}
        \alert{1D Motion (Chapter 2)}
        \begin{itemize}
            \item Direction: + or - sign
            \item Example: $v = +5$ m/s or $v = -3$ m/s
            \item Vector addition: Simple algebra
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \alert{2D Motion (This Chapter)}
        \begin{itemize}
            \item Direction: Angle and magnitude
            \item Example: $\vec{v} = 5$ m/s at 30°
            \item Vector addition: Components needed
        \end{itemize}
    \end{column}
\end{columns}
\vspace{1em}
\begin{block}{Why This Matters}
In 2D, we can't just use + and - to represent all possible directions. We need trigonometry and vector components!
\end{block}
\end{frame}

\begin{frame}
\frametitle{Acceleration: Quick Review}
\framesubtitle{The Bridge to 2D Motion}
\begin{block}{From Chapter 2}
\begin{itemize}
    \item \textbf{Acceleration}: Rate of velocity change, $\bar{a} = \Delta v / \Delta t$
    \item \textbf{Key Insight}: In 2D, acceleration can change speed, direction, or both!
    \item \textbf{Free Fall}: $a = -g = -9.80$ m/s² (constant downward)
\end{itemize}
\end{block}
\begin{alertblock}{2D Challenge}
How do we handle acceleration that's not aligned with our motion direction? This is where vector components become essential!
\end{alertblock}
\end{frame}

\section{Kinematic Equations: Quick Reference}

\begin{frame}
\frametitle{Kinematic Equations: Review and Extension}
\framesubtitle{From 1D to 2D Applications}
\begin{block}{The Four Equations (From Chapter 2)}
For constant acceleration only:
\begin{align*}
    v_f &= v_0 + at \\
    \Delta x &= \frac{1}{2}(v_0 + v_f)t \\
    \Delta x &= v_0 t + \frac{1}{2}at^2 \\
    v_f^2 &= v_0^2 + 2a\Delta x
\end{align*}
\end{block}
\begin{alertblock}{2D Strategy}
We'll apply these equations \textbf{separately} to x and y components!
\end{alertblock}
\end{frame}

\section{Free Fall: Review and 2D Extension}

\begin{frame}
\frametitle{Free Fall: Essential Concepts}
\framesubtitle{Building on Chapter 2 for Projectile Motion}
\begin{block}{Key Review (From Chapter 2)}
\begin{itemize}
    \item \textbf{Free Fall}: Motion under gravity only ($a = -g = -9.80$ m/s²)
    \item \textbf{Sign Convention}: Up = positive, so $a_y = -9.80$ m/s²
    \item \textbf{Key Insight}: All objects fall at same rate (neglecting air resistance)
\end{itemize}
\end{block}
\begin{alertblock}{2D Application}
In projectile motion, only the \textbf{vertical component} follows free fall. The \textbf{horizontal component} has no acceleration!
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Free Fall Graphs: Quick Review}
\framesubtitle{Essential Patterns for Projectile Motion}
\begin{columns}[T]
    \begin{column}{0.33\textwidth}
        \textbf{Position vs. Time}
        \begin{itemize}
            \item Parabolic shape
            \item Slope = velocity
        \end{itemize}
    \end{column}
    \begin{column}{0.33\textwidth}
        \textbf{Velocity vs. Time}
        \begin{itemize}
            \item Straight line
            \item Slope = $-g$
            \item Area = $\Delta y$
        \end{itemize}
    \end{column}
    \begin{column}{0.33\textwidth}
        \textbf{Acceleration vs. Time}
        \begin{itemize}
            \item Constant: $-g$
            \item Always downward
        \end{itemize}
    \end{column}
\end{columns}
\vspace{1em}
\begin{block}{2D Connection}
These same patterns apply to the \textbf{vertical component} of projectile motion!
\end{block}
\end{frame}

\section{Graphical Analysis: Essential Review}

\begin{frame}
\frametitle{Motion Graphs: Key Relationships}
\framesubtitle{Quick Review from Chapter 2}
\begin{columns}[T]
    \begin{column}{0.5\textwidth}
        \textbf{Position-Time Graph}
        \begin{itemize}
            \item \alert{Slope} = velocity
            \item Curved = acceleration
            \item Steeper = faster
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \textbf{Velocity-Time Graph}
        \begin{itemize}
            \item \alert{Slope} = acceleration
            \item \alert{Area} = displacement
            \item Horizontal = constant velocity
        \end{itemize}
    \end{column}
\end{columns}
\vspace{1em}
\begin{block}{2D Application}
We'll analyze x and y components separately using these same principles!
\end{block}
\end{frame}

\section{1D Problem Solving: Quick Reference}

\begin{frame}
\frametitle{Problem Solving: GUESS Method Review}
\framesubtitle{From Chapter 2 to 2D Applications}
\begin{block}{The GUESS Method (Chapter 2)}
\begin{itemize}
    \item \textbf{G} - \alert{Givens}: List known quantities, define coordinate system
    \item \textbf{U} - \alert{Unknown}: Identify what to find
    \item \textbf{E} - \alert{Equation}: Choose appropriate kinematic equation
    \item \textbf{S} - \alert{Substitute}: Plug in values with units
    \item \textbf{S} - \alert{Solve}: Calculate and check units/significant figures
\end{itemize}
\end{block}
\begin{alertblock}{2D Extension}
For 2D problems: Apply GUESS \textbf{separately} to x and y components!
\end{alertblock}
\end{frame}

\part{Part 2: Two-Dimensional Kinematics}
\section{2D Motion Concepts}

\begin{frame}
\frametitle{2D Motion: The Independence of Motion}
\begin{block}{The Most Important Concept in 2D Kinematics}
The horizontal and vertical components of two-dimensional motion are \textbf{independent} of each other.
\end{block}
\begin{itemize}
    \item Motion in the horizontal direction does not affect motion in the vertical direction, and vice versa.
    \item This allows us to break complex 2D problems into two simpler 1D problems: one for the x-direction and one for the y-direction.
    \item The only variable that connects the two separate motions is \alert{time ($t$)}.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Independence of Motion (Context)}
\begin{block}{Scenario: The Two-Ball Drop}
Imagine two identical balls at the same height.
\begin{itemize}
    \item Ball 1 is dropped straight down.
    \item Ball 2 is launched horizontally at the exact same moment.
\end{itemize}
\textbf{Question:} Which ball hits the ground first?
\end{block}
Let's visualize their motion. The result demonstrates the independence of vertical and horizontal motion.
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Independence of Motion}
\begin{alertblock}{[Diagram based on Figure 3.6]}
A composite image showing the motion of two balls.
\begin{itemize}
    \item The red ball is dropped vertically from rest.
    \item The blue ball is projected horizontally with an initial velocity.
    \item Strobe flashes at equal time intervals show that both balls have the same vertical position at any given moment.
    \item This demonstrates that the horizontal motion of the blue ball does not affect its vertical motion due to gravity. They hit the ground at the same time.
\end{itemize}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Visualization: Dropped vs. Fired Ball Experiment}
\begin{center}
\includegraphics[width=0.8\linewidth]{phys12-projectile-motion-trajectory-analysis.png}
\end{center}
\begin{block}{Key Observation}
The strobe images show both balls at the same vertical positions at each time interval, demonstrating that horizontal motion does not affect vertical motion under gravity.
\end{block}
\end{frame}

\section{Vectors in 2D}

\begin{frame}
\frametitle{Vector Addition: Head-to-Tail Method}
\begin{block}{Graphical Method for Adding Vectors}
To add vectors graphically, we draw them one after another.
\end{block}
\begin{enumerate}
    \item Draw the first vector to scale and in the correct direction.
    \item Draw the second vector starting from the head (tip) of the first vector.
    \item Continue for all vectors.
    \item The \textbf{resultant vector} ($\vec{R}$) is the vector drawn from the tail (start) of the first vector to the head of the last vector.
\end{enumerate}
\vfill
\begin{alertblock}{[Diagram illustrating the head-to-tail method for adding vectors $\vec{A}$ and $\vec{B}$, showing the resultant vector $\vec{R}$. Based on Figure 3.10]}
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Visualization: Vector Addition Example}
\begin{center}
\includegraphics[width=0.7\linewidth]{phys12-vectors-vector-addition-figure-4.png}
\end{center}
\begin{block}{Key Observation}
The resultant vector $\vec{R} = \vec{A} + \vec{B}$ is drawn from the tail of the first vector to the head of the second vector.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Analytical Method: Vector Components}
\begin{block}{Using Trigonometry for Precision}
Any 2D vector can be broken down into two perpendicular components. We typically use x and y axes.
\end{block}
\begin{itemize}
    \item For a vector $\vec{A}$ with magnitude $A$ and at an angle $\theta$ (measured from the positive x-axis):
    \begin{itemize}
        \item The x-component is $A_x = A \cos \theta$
        \item The y-component is $A_y = A \sin \theta$
    \end{itemize}
    \item This process is called \textbf{resolving the vector}.
    \item To add vectors $\vec{A}$ and $\vec{B}$ to get $\vec{R}$:
    \begin{itemize}
        \item Add the x-components: $R_x = A_x + B_x$
        \item Add the y-components: $R_y = A_y + B_y$
    \end{itemize}
    \item Then, find the magnitude and direction of $\vec{R}$ using its components.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Advanced Topic: Rotated Coordinate Systems}
\begin{columns}
\column{0.6\textwidth}
\begin{block}{When Axes Are Rotated}
Sometimes we need to resolve vectors along axes that are not aligned with the standard x-y coordinate system.
\begin{itemize}
    \item Common in navigation and engineering
    \item The trigonometric principles remain the same
    \item Adjust angles relative to the new axes
\end{itemize}
\end{block}

\column{0.4\textwidth}
\begin{figure}
\centering
\includegraphics[width=0.9\textwidth]{phys12-vectors-vector-addition-figure-21.png}
\caption{Vector components along rotated axes}
\end{figure}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Vector Components (Context)}
\begin{block}{Breaking a Vector Apart}
Let's visualize how a single vector $\vec{A}$ can be represented as the sum of its perpendicular components, $\vec{A}_x$ and $\vec{A}_y$.
\vfill
This is the reverse of adding vectors and is a crucial first step for solving almost any 2D physics problem.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Vector Components}
\begin{columns}
\column{0.5\textwidth}
\begin{figure}
\begin{tikzpicture}[scale=1.5, thick]
    % Axes
    \draw[->] (0,0) -- (4,0) node[below] {$x$};
    \draw[->] (0,0) -- (0,3) node[left] {$y$};

    % Vector A
    \draw[->, ds9blue, line width=1.5pt] (0,0) -- (3,2) node[midway, above left] {$\vec{A}$};
    \draw (0.5,0) arc (0:33.7:0.5) node[midway, right] {$\theta$};

    % Components
    \draw[->, ds9red, dashed, line width=1.2pt] (0,0) -- (3,0) node[midway, below] {$A_x = A \cos\theta$};
    \draw[->, ds9red, dashed, line width=1.2pt] (3,0) -- (3,2) node[midway, right] {$A_y = A \sin\theta$};

    % Right angle
    \draw (2.7,0) -- (2.7,0.3) -- (3,0.3);
\end{tikzpicture}
\caption{Mathematical representation of vector components}
\end{figure}

\column{0.5\textwidth}
\begin{figure}
\centering
\includegraphics[width=0.8\textwidth]{phys12-vectors-vector-components.png}
\caption{Alternative visualization of vector components}
\end{figure}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Trigonometry Reference for Vector Components}
\begin{columns}[T]
    \column{0.48\textwidth}
    \begin{figure}
        \centering
        \includegraphics[width=\linewidth]{math-trigonometry-sohcahtoa.png}
        \caption{SOHCAHTOA mnemonic for finding vector components}
    \end{figure}

    \column{0.48\textwidth}
    \begin{figure}
        \centering
        \includegraphics[width=\linewidth]{math-sine-cosine-laws.png}
        \caption{Sine and cosine laws for non-right triangles}
    \end{figure}
\end{columns}
\begin{block}{Key Applications}
These trigonometric relationships are essential for:
\begin{itemize}
    \item Resolving vectors into components
    \item Finding magnitude and direction from components
    \item Solving vector addition problems
\end{itemize}
\end{block}
\end{frame}

\section{Projectile Motion}

\begin{frame}
\frametitle{Key Concepts: Projectile Motion}
\begin{block}{Applying 2D Kinematics}
A \textbf{projectile} is any object that is thrown or launched and then moves subject only to gravity.
\end{block}
\textbf{Analysis Steps:}
\begin{enumerate}
    \item Set up a coordinate system (usually origin at launch, +y is up).
    \item Resolve the initial velocity ($v_0$) into components:
    \begin{itemize}
        \item $v_{0x} = v_0 \cos \theta_0$
        \item $v_{0y} = v_0 \sin \theta_0$
    \end{itemize}
    \item Treat as two independent 1D motion problems:
    \begin{itemize}
        \item \textbf{Horizontal (x):} Constant velocity ($a_x = 0$)
        \item \textbf{Vertical (y):} Constant acceleration ($a_y = -g$)
    \end{itemize}
    \item Use the kinematic equations for each direction. Time ($t$) is the same for both.
\end{enumerate}
\end{frame}

\section{Relative Velocity}

\begin{frame}
\frametitle{Key Concepts: Relative Velocity}
\begin{block}{Motion Depends on the Observer}
Velocity is always measured \textit{relative} to a frame of reference.
\end{block}
\begin{itemize}
    \item The velocity of an object can have different values when measured by different observers.
    \item We use vector addition to find the velocity of an object relative to a stationary observer (e.g., the ground).
    \item \textbf{Subscript Notation} is very helpful:
    \begin{itemize}
        \item $\vec{v}_{PG}$ = Velocity of the \textbf{P}lane relative to the \textbf{G}round.
        \item $\vec{v}_{PA}$ = Velocity of the \textbf{P}lane relative to the \textbf{A}ir.
        \item $\vec{v}_{AG}$ = Velocity of the \textbf{A}ir relative to the \textbf{G}round (i.e., the wind).
    \end{itemize}
    \item \textbf{Relative Velocity Equation}: $\vec{v}_{PG} = \vec{v}_{PA} + \vec{v}_{AG}$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Visualization: Train Relative Velocity Example}
\begin{center}
\includegraphics[width=0.8\linewidth]{phys12-relative-velocity-train.png}
\end{center}
\begin{block}{Understanding the Diagram}
\begin{itemize}
    \item The train moves with velocity $\vec{v}_{train/ground}$ relative to the ground
    \item The person walks with velocity $\vec{v}_{person/train}$ relative to the train
    \item The person's velocity relative to the ground is the vector sum: $\vec{v}_{person/ground} = \vec{v}_{person/train} + \vec{v}_{train/ground}$
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Boat in a River (Context)}
\begin{block}{Scenario: Crossing a Current}
A boat tries to travel straight across a river. However, the river's current carries the boat downstream.
\begin{itemize}
    \item $\vec{v}_{bw}$: Velocity of the \textbf{b}oat relative to the \textbf{w}ater.
    \item $\vec{v}_{wg}$: Velocity of the \textbf{w}ater relative to the \textbf{g}round (the current).
    \item $\vec{v}_{bg}$: Velocity of the \textbf{b}oat relative to the \textbf{g}round (its actual path).
\end{itemize}
The boat's actual velocity is the vector sum of its velocity in the water and the water's velocity.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Boat in a River}
\begin{alertblock}{[Diagram based on Figure 3.40]}
A diagram showing a river with a current flowing to the right.
\begin{itemize}
    \item A vector labeled $\vec{v}_{bw}$ points straight across the river.
    \item A vector labeled $\vec{v}_{wg}$ points downstream, parallel to the banks.
    \item The resultant vector $\vec{v}_{bg} = \vec{v}_{bw} + \vec{v}_{wg}$ points diagonally downstream, showing the boat's true path relative to the ground.
\end{itemize}
\end{alertblock}
\end{frame}

\section{2D Problem Solving}

\begin{frame}
\frametitle{I do: Fireworks Projectile (Ex. 3.4)}
\begin{block}{Problem}
A firework is shot with an initial speed of 70.0 m/s at an angle of 75.0° above the horizontal. (a) Calculate the height at which it explodes (its apex). (b) How much time passes until it explodes?
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item $v_0 = 70.0$ m/s
\item $\theta_0 = 75.0^\circ$
\item $y_0 = 0$ m, $x_0 = 0$ m
\item $a_y = -9.80$ m/s$^2$
\item $a_x = 0$ m/s$^2$
\item At apex: $v_{fy} = 0$ m/s
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item (a) $y_f = ?$
\item (b) $t = ?$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I do: Fireworks Projectile (Ex. 3.4)}

\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item $v_0 = 70.0$ m/s
\item $\theta_0 = 75.0^\circ$
\item $y_0 = 0$ m, $x_0 = 0$ m
\item $a_y = -9.80$ m/s$^2$
\item $a_x = 0$ m/s$^2$
\item At apex: $v_{fy} = 0$ m/s
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item (a) $y_f = ?$
\item (b) $t = ?$
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{E - Equation}
\begin{itemize}
\item $v_{0y} = v_0 \sin\theta_0$
\item $v_{fy}^2 = v_{0y}^2 + 2a_y\Delta y$
\item \textbf{Rearranged}: $y_f = y_0 + \frac{v_{fy}^2 - v_{0y}^2}{2a_y}$
\item $v_{fy} = v_{0y} + a_y t$
\item \textbf{Rearranged}: $t = \frac{v_{fy} - v_{0y}}{a_y}$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I do: Fireworks Projectile (Ex. 3.4)}

\begin{block}{S - Substitute}
\begin{itemize}
\item $v_{0y} = (70.0 \text{ m/s})\sin(75.0^\circ) = 67.6$ m/s
\item $y_f = 0 + \frac{(0)^2 - (67.6)^2}{2(-9.80)}$
\item $t = \frac{0 - 67.6}{-9.80}$
\end{itemize}
\end{block}
\pause
\begin{block}{S - Solve}
\begin{itemize}
\item $y_f = \frac{-4570}{-19.6} = 233$ m
\item $t = \frac{-67.6}{-9.80} = 6.90$ s
\item \boxed{y_f = 233 \text{ m}} and \boxed{t = 6.90 \text{ s}}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{We do: Hot Rock Projectile (Ex. 3.5)}
\begin{block}{Problem}
A rock is ejected from a volcano with speed 25.0 m/s at 35.0° above the horizontal. It strikes the side of the volcano 20.0 m \textit{lower} than its starting point. (a) Calculate the time it takes.
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item $v_0 = 25.0$ m/s
\item $\theta_0 = 35.0^\circ$
\item $y_0 = 0$ m
\item $y_f = -20.0$ m
\item $a_y = -9.80$ m/s$^2$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item $t = ?$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{We do: Hot Rock Projectile (Ex. 3.5)}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item $v_0 = 25.0$ m/s
\item $\theta_0 = 35.0^\circ$
\item $y_0 = 0$ m
\item $y_f = -20.0$ m
\item $a_y = -9.80$ m/s$^2$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item $t = ?$
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{E - Equation}
\begin{itemize}
\item $v_{0y} = v_0 \sin\theta_0$
\item $\Delta y = v_{0y}t + \frac{1}{2}a_y t^2$
\item \textbf{Rearranged}: $\frac{1}{2}a_y t^2 + v_{0y}t - \Delta y = 0$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{We do: Hot Rock Projectile (Ex. 3.5)}

\begin{block}{S - Substitute}
\begin{itemize}
\item $v_{0y} = (25.0)\sin(35.0^\circ) = 14.3$ m/s
\item $\Delta y = -20.0 - 0 = -20.0$ m
\item $-20.0 = (14.3)t + \frac{1}{2}(-9.80)t^2$
\item $4.90t^2 - 14.3t - 20.0 = 0$
\end{itemize}
\end{block}
\pause
\begin{block}{S - Solve}
\begin{itemize}
\item $t = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
\item $a = 4.90$, $b = -14.3$, $c = -20.0$
\item $t = \frac{14.3 \pm \sqrt{204.49 + 392}}{9.80} = \frac{14.3 \pm 24.4}{9.80}$
\item $t = 3.95$ s
\item \boxed{t = 3.95 \text{ s}}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{You do: Projectile Launch}
\begin{block}{Problem (Ch.3, Q.25)}
A projectile is launched at ground level with an initial speed of 50.0 m/s at an angle of 30.0° above the horizontal. It strikes a target 3.00 seconds later.
\begin{enumerate}
    \item What is the horizontal distance ($x$) to the target?
    \item What is the vertical distance ($y$) to the target?
\end{enumerate}
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item $v_0 = 50.0$ m/s
\item $\theta_0 = 30.0^\circ$
\item $x_0 = 0$ m, $y_0 = 0$ m
\item $t = 3.00$ s
\item $a_x = 0$ m/s$^2$
\item $a_y = -9.80$ m/s$^2$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item (a) $x_f = ?$
\item (b) $y_f = ?$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{You do: Projectile Launch}


\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item $v_0 = 50.0$ m/s
\item $\theta_0 = 30.0^\circ$
\item $x_0 = 0$ m, $y_0 = 0$ m
\item $t = 3.00$ s
\item $a_x = 0$ m/s$^2$
\item $a_y = -9.80$ m/s$^2$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item (a) $x_f = ?$
\item (b) $y_f = ?$
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{E - Equation}
\begin{itemize}
\item $v_{0x} = v_0 \cos\theta_0$, $v_{0y} = v_0 \sin\theta_0$
\item $x_f = x_0 + v_{0x}t + \frac{1}{2}a_x t^2$
\item $y_f = y_0 + v_{0y}t + \frac{1}{2}a_y t^2$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{You do: Projectile Launch}
\begin{block}{S - Substitute}
\end{block}
\pause

\begin{block}{S - Solve}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Reading Homework}
\begin{block}{Practice and Deeper Understanding}
To solidify your understanding, please work through the following sections in your textbook:
\end{block}
\begin{itemize}
    \item \textbf{Chapter 2: 1D Kinematics}
    \begin{itemize}
        \item Conceptual Questions (Page 73)
        \item Problems \& Exercises (Page 82)
    \end{itemize}
    \vfill
    \item \textbf{Chapter 3: 2D Kinematics}
    \begin{itemize}
        \item Conceptual Questions (Page 156)
        \item Problems \& Exercises (Page 163)
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Summary of Key Concepts}
\begin{itemize}
    \item \textbf{1D Motion}: We describe motion using scalars (distance, speed) and vectors (displacement, velocity, acceleration). The kinematic equations are our primary tool for solving problems with \alert{constant acceleration}.
    \vfill
    \item \textbf{Graphical Analysis}: The slope and area of motion graphs have physical meaning. (Slope of x-t is v, slope of v-t is a, area of v-t is $\Delta x$).
    \vfill
    \item \textbf{2D Motion}: The key is the \alert{independence of motion}. We break 2D problems into two 1D problems (horizontal and vertical) connected by time.
    \vfill
    \item \textbf{Projectile Motion}: A classic case of 2D motion where $a_x = 0$ (constant velocity) and $a_y = -g$ (constant acceleration).
    \vfill
    \item \textbf{Relative Velocity}: All velocities are relative to a reference frame. We use vector addition to find resultant velocities.
\end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch01-03_review_test-prep.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Unit 1 Review]{PHYS12 CH123:}
\subtitle{Test Prep}
\author[Mr. Gullo]{Mr. Gullo}
\date[Oct 2024]{October 2024}


\begin{document}

\frame{\titlepage}

\section{Introduction}

\begin{frame}
\frametitle{Overview}
\begin{itemize}
    \item Review of key concepts from Chapters 1-3
    \item Practice problems with step-by-step solutions
    \item Focus on:
    \begin{itemize}
        \item Significant figures and uncertainties
        \item Unit conversions
        \item Velocity and displacement calculations
        \item Vector addition
    \end{itemize}
\end{itemize}
\end{frame}

\section{Chapter 1: Measurement and Problem Solving}
\begin{frame}
\frametitle{Problem 1: Significant Figures and Uncertainties}
\begin{block}{Question}
(a) How many significant figures are in the numbers 99 and 100?\\
(b) If the uncertainty in each number is 1, what is the percent uncertainty in each?\\
(c) Which is a more meaningful way to express the accuracy of these two numbers, significant figures or percent uncertainties?
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 1: Solution (Part a)}
\begin{block}{Question}
(a) How many significant figures are in the numbers 99 and 100?\\
\end{block}
\begin{block}{Solution}
(a) 99 has \underline{2} sig. figs.; 100 has \underline{3} sig. figs. at most
\end{block}
\begin{block}{Explanation}
\begin{itemize}
\item For 99: Both digits are non-zero, so both are significant.
\item For 100: The 1 is non-zero, so it's significant. The zeros to the right of a non-zero digit are potentially significant. If this is an exact number, it has 1 sig. fig. If it's a measurement, it could have up to 3 sig. figs.
\item Always clarify with the context whether trailing zeros are significant.
\end{itemize}
\end{block}
\end{frame}
\begin{frame}
\frametitle{Significant Figures in 100}

\begin{columns}[T]
\column{0.33\textwidth}
\begin{exampleblock}{3 Significant Figures}
\textbf{Example:} Digital scale reads 100 g
\begin{itemize}
\item All digits significant
\item Precise to nearest gram
\item Written as 1.00 × 10² g
\end{itemize}
\end{exampleblock}

\column{0.33\textwidth}
\begin{exampleblock}{1 Significant Figure}
\textbf{Example:} About 100 people
\begin{itemize}
\item Only 1 is significant
\item Estimate or rounding
\item Written as 1 × 10² people
\end{itemize}
\end{exampleblock}

\column{0.33\textwidth}
\begin{exampleblock}{Infinite Significant Figures}
\textbf{Example:} Exact numbers
\begin{itemize}
\item 100 cents in a dollar
\item 100 years in a century
\item Defined, not measured
\end{itemize}
\end{exampleblock}
\end{columns}
\end{frame}


\begin{frame}
\frametitle{Problem 1: Solution (Part b)}
\begin{block}{Question}
(b) If the uncertainty in each number is 1, what is the percent uncertainty in each?\\
\end{block}
\begin{block}{Solution}
(b) For 99: $\frac{1}{99} \times 100 = 1.01\% = \underline{1.0\%}$\\
   For 100: $\frac{1}{100} \times 100 = \underline{1.00\%}$ (if all zeros are significant)
\end{block}
\begin{block}{Explanation}
\begin{itemize}
\item Percent uncertainty = $\frac{\text{absolute uncertainty}}{\text{measured value}} \times 100\%$
\item For 99: $\frac{1}{99} \times 100 = 1.01\%$, rounded to 1.0\% (2 sig. figs.)
\item For 100: $\frac{1}{100} \times 100 = 1.00\%$ (3 sig. figs. if all zeros are significant)
\item Note: The uncertainty in the result should not be more precise than the given uncertainty (1).
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 1: Solution (Part c)}
\begin{block}{Question}
(c) Which is a more meaningful way to express the accuracy of these two numbers, significant figures or percent uncertainties?
\end{block}
\begin{block}{Solution}
(c) Percent uncertainties are a more meaningful way to express the accuracy of these two numbers.
\end{block}
\begin{block}{Explanation}
\begin{itemize}
\item Significant figures give a rough idea of precision, but can be ambiguous (e.g., for 100).
\item Percent uncertainty provides a clear, quantitative measure of relative accuracy.
\item In this case, percent uncertainty shows that both numbers have similar accuracy (about 1\%), which isn't clear from sig. figs. alone.
\item Percent uncertainty is particularly useful for comparing measurements with different magnitudes.
\end{itemize}
\end{block}
\end{frame}\begin{frame}
\frametitle{Problem 1: Solution (Part c)}
\begin{block}{Solution}
(c) Percent uncertainties are a more meaningful way to express the accuracy of these two numbers.
\end{block}
\begin{block}{Explanation}
\begin{itemize}
\item Significant figures give a rough idea of precision, but can be ambiguous (e.g., for 100).
\item Percent uncertainty provides a clear, quantitative measure of relative accuracy.
\item In this case, percent uncertainty shows that both numbers have similar accuracy (about 1\%), which isn't clear from sig. figs. alone.
\item Percent uncertainty is particularly useful for comparing measurements with different magnitudes.
\end{itemize}
\end{block}
\end{frame}
\begin{frame}
\frametitle{Problem 2: Percent Uncertainty}
\begin{block}{Question}
(a) A person's blood pressure is measured to be $120 \pm 2$ mm Hg. What is its percent uncertainty?\\
(b) Assuming the same percent uncertainty, what is the uncertainty in a blood pressure measurement of 80 mm Hg?
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 2: Solution (Part a)}
\begin{block}{Solution}
(a) $\% unc = \frac{2 \text{ mm Hg}}{120 \text{ mm Hg}} \times 100\% = 1.7\% = \underline{2\%}$\\
(1 sig. fig because of 2 mm Hg)
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 2: Solution (Part b)}
\begin{block}{Solution}
(b) $\delta bp = \frac{1.7\%}{100\%} \times 80 \text{ mm Hg} = 1.3 \text{ mm Hg} = \underline{1 \text{ mm Hg}}$\\
(1 sig. fig because of 2 mm Hg)
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 3: Uncertainty and Unit Conversion}
\begin{block}{Question}
(a) A car speedometer has a 5.0\% uncertainty. What is the range of possible speeds when it reads 90 km/h?\\
(b) Convert this range to miles per hour. (1 km = 0.6214 mi)
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 3: Solution (Part a)}
\begin{block}{Solution}
(a) $\delta v = \frac{5.0\%}{100\%} \times 90.0 \text{ km/h} = 4.5 \text{ km/h}$\\
Thus, the range = $90.0 \pm 5 \text{ km/h} = 85 \text{ to } 95 \text{ km/h}$.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 3: Solution (Part b)}
\begin{block}{Solution}
(b) Converting to miles per hour:
\begin{align*}
\frac{85.5 \text{ km}}{1 \text{ h}} \times \frac{0.6214 \text{ mi}}{1 \text{ km}} &= 53.1 \text{ mi/h}\\
\frac{94.5 \text{ km}}{1 \text{ h}} \times \frac{0.6214 \text{ mi}}{1 \text{ km}} &= 58.7 \text{ mi/h}
\end{align*}
So the range is 53.1 to 58.7 mi/h
\end{block}
\end{frame}

\section{Chapter 2 and 3: Motion in One and Two Dimensions}

\begin{frame}
\frametitle{Problem 4: Displacement and Time}
\begin{block}{Question}
Land west of the San Andreas fault in southern California is moving at an average velocity of about 6 cm/y northwest relative to land east of the fault. Los Angeles is west of the fault and may thus someday be at the same latitude as San Francisco, which is east of the fault. How far in the future will this occur if the displacement to be made is 590 km northwest, assuming the motion remains constant?
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 4: Visualization}

\begin{tikzpicture}[scale=0.7]
    \draw[thick, ->] (0,0) -- (-10,0) node[left] {West};
    \draw[thick, ->] (0,0) -- (0,6) node[above] {North};

    % San Andreas Fault
    \draw[red, thick] (-1,-0.5) -- (-5,6.5);
    \node[red] at (-2.5,6) {San Andreas Fault};

    % Los Angeles
    \filldraw[blue] (-2,1) circle (2pt) node[below] {LA};

    % San Francisco
    \filldraw[green] (-6,5) circle (2pt) node[above] {SF};

    % Motion vector
    \draw[->, thick, orange] (-2,1) -- (-6,5);
    \node[orange] at (-5,3.5) {590 km};

    % Velocity vector
    \draw[->, thick, purple] (-2,1) -- (-2.3,1.3);
   \node[purple] at (-3.7,1.5) {6 cm/y};

    % Simple Compass Rose
    \draw[thick] (8,5) -- (8,6) node[above] {N};
    \draw[thick] (8,5) -- (7,5) node[left] {W};
    \draw[thick] (8,5) -- (9,5) node[right] {E};
    \draw[thick] (8,5) -- (8,4) node[below] {S};
\end{tikzpicture}
\end{frame}

\begin{frame}
\frametitle{Problem 4: Solution}
\begin{block}{Equations}
Velocity equation: $v = \frac{\Delta x}{\Delta t}$
Rearranged for time: $\Delta t = \frac{\Delta x}{v}$
\end{block}
\begin{block}{Solution}
\begin{align*}
\Delta t &= \frac{\Delta x}{v} = \frac{590 \text{ km}}{6 \text{ cm/year}} \times \frac{100000 \text{ cm}}{1 \text{ km}}\\
&= \frac{5.90 \times 10^5 \text{ m}}{6 \text{ cm/year}} \times \frac{100 \text{ cm}}{1 \text{ m}}\\
&= 9.83 \times 10^6 \text{ years} = 1 \times 10^7 \text{ years}\\
&= \underline{10 \text{ million years}}
\end{align*}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 5: Relative Motion (Part 1)}
\begin{block}{Question}
A seagull flies at a velocity of 9.00 m/s straight into the wind.
(a) If it takes the bird 20.0 min to travel 6.00 km relative to the Earth, what is the velocity of the wind?\\
(b) If the bird turns around and flies with the wind, how long will he take to return 6.00 km?\\
(c) Discuss how the wind affects the total round-trip time compared to what it would be with no wind.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 5: Visualization}
\begin{tikzpicture}[scale=0.7]
    \draw[thick, ->] (0,3) -- (10,3) node[right] {Direction of flight};
    \draw[thick, <-] (0,1) -- (10,1) node[right] {Wind direction};

    % Seagull
    \node[draw, circle, fill=gray!30] at (2,3) (seagull) {\textbf{S}};
    \draw[->, thick, blue] (seagull) -- ++(2,0) node[above] {$\vec{v}_{\text{SA}} = 9.00$ m/s};

    % Wind
    \draw[->, thick, red] (4,1) -- ++(2,0) node[below] {$\vec{v}_{\text{AG}}$};

    % Ground velocity
    \draw[->, thick, green] (2,2) -- ++(1,0) node[below] {$\vec{v}_{\text{SG}} = 5.00$ m/s};

    % Labels
    \node at (1,4) {S: Seagull, A: Air, G: Ground};
\end{tikzpicture}
\end{frame}

\begin{frame}
\frametitle{Problem 5: Solution (Part a)}
\begin{block}{Equations}
Relative velocity: $\mathbf{v}_{\mathbf{SG}} = \mathbf{v}_{\mathbf{SA}} + \mathbf{v}_{\mathbf{AG}}$
Rearranged for wind velocity: $\mathbf{v}_{\mathbf{AG}} = \mathbf{v}_{\mathbf{SG}} - \mathbf{v}_{\mathbf{SA}}$
Velocity from displacement and time: $v = \frac{x}{t}$
\end{block}
\begin{block}{Solution}
(a) Let A = air, S = seagull, G = ground
\begin{align*}
v_{\text{SG}} &= \frac{x_{\text{SG}}}{t} = \frac{6.00 \times 10^3 \text{ m}}{(20 \text{ min})(60 \text{ s/1 min})} = 5.00 \text{ m/s}\\
v_{AG} &= v_{\text{SG}} - v_{\text{SA}} = 5.00 \text{ m/s} - 9.00 \text{ m/s} = -4.00 \text{ m/s}
\end{align*}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 5: Solution (Part b)}
\begin{block}{Equations}
Relative velocity (with wind): $v_{\text{SG}} = v_{\text{SA}} - v_{\text{AG}}$
Time from displacement and velocity: $t = \frac{x}{v}$
\end{block}
\begin{block}{Solution}
(b) Flying with the wind:
\begin{align*}
v_{\text{SG}} &= v_{\text{SA}} - v_{\text{AG}} = 9.00 \text{ m/s} - (-4.00 \text{ m/s}) = 13.00 \text{ m/s}\\
t &= \frac{x_{\text{SG}}}{v_{\text{SG}}} = \frac{6.00 \times 10^3 \text{ m}}{13.00 \text{ m/s}} = 462 \text{ s} = \underline{7 \text{ min} \text{ 42 s}}
\end{align*}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 5: Solution (Part c)}
\begin{block}{Solution}
(c) The wind will always slow down the round trip time, relative to having no wind present.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 6: Vector Addition (Part 1)}
\begin{block}{Question}
A football quarterback is moving straight backward at a speed of 2.00 m/s when he throws a pass to a player 18.0 m straight downfield. The ball is thrown at an angle of 25.0° relative to the ground and is caught at the same height as it is released. \\What is the initial velocity of the ball relative to the quarterback?
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 6: Visualization}
\begin{tikzpicture}[scale=0.7]
    \draw[thick, ->] (0,0) -- (10,0) node[right] {Downfield};
    \draw[thick, ->] (0,0) -- (0,6) node[above] {Height};

    % Quarterback
    \node[draw, circle, fill=red!30] at (1,1) (qb) {\textbf{QB}};
    \draw[->, thick, red] (qb) -- ++(-0.5,0) node[below] {$\vec{v}_{QB} = 2.00$ m/s};

    % Ball trajectory
    \draw[->, thick, blue] (qb) -- ++(8,3.73) node[above] {$\vec{v}_{ball/ground}$};

    % Angle
    \draw[thick] (1,1) -- ++(1,0) arc (0:25:1);
    \node at (2.3,1.3) {25.0°};

    % Receiver
    \node[draw, circle, fill=green!30] at (9,1) (receiver) {\textbf{R}};

    % Distance
    \draw[<->, thick] (1,0.5) -- (9,0.5) node[midway, below] {18.0 m};
\end{tikzpicture}
\end{frame}

\begin{frame}
\frametitle{Problem 6: Vector Addition Visualization}
\begin{tikzpicture}[scale=0.7]
    \draw[thick, ->] (0,0) -- (10,0) node[right] {x};
    \draw[thick, ->] (0,0) -- (0,6) node[above] {y};

    % Quarterback's velocity vector
    \draw[->, thick, red] (0,0) -- (-2,0) node[below] {$\vec{v}_{QB}$};

    % Ball's velocity vector relative to ground
    \draw[->, thick, blue] (0,0) -- (7.9,3.21) node[above] {$\vec{v}_{ball/ground}$};

    % Ball's velocity vector relative to quarterback
    \draw[->, thick, green] (-2,0) -- (7.9,3.21) node[right] {$\vec{v}_{ball/QB}$};

    % Angle
    \draw[thick] (0,0) -- (2,0) arc (0:22.1:2);
    \node at (2.5,0.5) {$\phi$};

    % Labels
    \node at (4,-1) {Vector addition: $\vec{v}_{QB} + \vec{v}_{ball/QB} = \vec{v}_{ball/ground}$};
\end{tikzpicture}
\end{frame}

\begin{frame}
\frametitle{Problem 6: Solution (Part 1)}
\begin{block}{Equations}
Vector addition: $\vec{v}_{QB} + \vec{v}_{ball/QB} = \vec{v}_{ball/ground}$\\
Component equations:\\
$v_{QB_x} + v_{ball/QB_x} = v_{ball/ground_x} = v_{ball/ground} \cos \phi$\\
$v_{QB_y} + v_{ball/QB_y} = v_{ball/ground_y} = v_{ball/ground} \sin \phi$
\end{block}
\begin{block}{Solution}
(relative to ground)
\begin{align*}
v_{QB_x} + v_{ball/QB_x} &= v_{ball/ground} \cos \phi \\
-2 \text{ m/s} + v_{ball/QB_x} &= (15.2 \text{ m/s}) \cos 25.0^{\circ} \Rightarrow v_{ball/QB_x} = 15.8 \text{ m/s}\\
v_{QB_y} + v_{ball/QB_y} &= v_{ball/ground} \sin \phi \\
0 + v_{ball/QB_y} &= (15.2 \text{ m/s}) \sin 25.0^{\circ} \Rightarrow v_{ball/QB_y} = 6.42 \text{ m/s}
\end{align*}
\end{block}
\end{frame}

% Title page configuration
\title[Projectile Motion Analysis]{PHYS11 CH4:}
\subtitle{Projectile Motion Analysis: Quarterback Problem}
\author[Mr. Gullo]{Mr. Gullo}
\date[Oct 2024]{October 2024}


\begin{frame}
\frametitle{Quarterback Velocity Problem}
\begin{block}{Problem Context}
\begin{itemize}
    \item Quarterback moving backward at 2.00 m/s
    \item Ball thrown at 25.0° angle relative to ground
    \item Ball travels 18.0 m downfield
\end{itemize}
\end{block}

\begin{block}{Calculation Steps}
\begin{enumerate}
    \item Use projectile motion equation: $R = \frac{v^2 \sin(2\theta)}{g}$
    \item Rearrange to solve for v: $v = \sqrt{\frac{R g}{\sin(2\theta)}}$
    \item Given: $R = 18.0$ m, $\theta = 25.0^{\circ}$, $g = 9.8$ m/s$^2$
    \item Calculate: $v \approx 15.2$ m/s
\end{enumerate}
\end{block}

\begin{alertblock}{Key Point}
The calculated velocity (15.2 m/s) is relative to the ground, not the quarterback.
\end{alertblock}
\end{frame}



\begin{frame}
\frametitle{Problem 6: Solution (Part 2)}
\begin{block}{Equations}
Magnitude of velocity vector: $v = \sqrt{v_x^2 + v_y^2}$
Angle of velocity vector: $\theta = \tan^{-1}\left(\frac{v_y}{v_x}\right)$
\end{block}
\begin{block}{Solution}
\begin{align*}
v_{ball/QB} &= \sqrt{v_{ball/QB_x}^2 + v_{ball/QB_y}^2} = \sqrt{(15.8 \text{ m/s})^2 + (6.42 \text{ m/s})^2} = \\\underline{17.0 \text{ m/s}}\\
\theta &= \tan^{-1}\left(\frac{v_{ball/QB_y}}{v_{ball/QB_x}}\right) = \tan^{-1}\left(\frac{6.42}{15.8}\right) = \underline{22.1^{\circ}}
\end{align*}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 6: Vector Addition Visualization}
\begin{tikzpicture}[scale=0.7]
    \draw[thick, ->] (0,0) -- (10,0) node[right] {x};
    \draw[thick, ->] (0,0) -- (0,6) node[above] {y};

    % Quarterback's velocity vector
    \draw[->, thick, red] (0,0) -- (-2,0) node[below] {$\vec{v}_{QB}$};

    % Ball's velocity vector relative to ground
    \draw[->, thick, blue] (0,0) -- (7.9,3.21) node[above] {$\vec{v}_{ball/ground}$};

    % Ball's velocity vector relative to quarterback
    \draw[->, thick, green] (-2,0) -- (7.9,3.21) node[right] {$\vec{v}_{ball/QB}$};

    % Angle
    \draw[thick] (0,0) -- (2,0) arc (0:22.1:2);
    \node at (2.5,0.5) {22.1°};

    % Labels
    \node at (4,-1) {Vector addition: $\vec{v}_{QB} + \vec{v}_{ball/QB} = \vec{v}_{ball/ground}$};
\end{tikzpicture}
\end{frame}

\section{Conclusion}

\begin{frame}
\frametitle{Key Takeaways}
\begin{itemize}
    \item Importance of significant figures and uncertainties in measurements
    \item Proper use of unit conversions
    \item Understanding relative motion and vector addition
    \item Practice solving multi-step problems
    \item Always check units and reasonableness of answers
\end{itemize}
\end{frame}

\section{Problem 37: Tennis Serve}

\begin{frame}
\frametitle{Problem 37: Tennis Serve}
\begin{block}{Question}
A tennis player serves at a speed of $170 \mathrm{~km} / \mathrm{h}$ from a height of 2.5 m and an angle $\boldsymbol{\theta}$ below the horizontal. The baseline is 11.9 m from the net, which is 0.91 m high.\\
What is the angle $\theta$ such that the ball just crosses the net?\\
Will the ball land in the service box, which has an outermost service line 6.40 m from the net?
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 37: Solution (Part 1)}
\begin{itemize}
    \item Convert initial velocity:
    $$v_{0}=170 \mathrm{~km} / \mathrm{h}=47.2 \mathrm{~m} / \mathrm{s}$$
    \item Calculate vertical distance to net:
    $$y=2.50 \mathrm{~m}-0.91 \mathrm{~m}=1.59 \mathrm{~m}$$
    \item Use kinematic equation:
    $$y=v_{0y} t+\frac{1}{2} a t^{2}$$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 37: Solution (Part 2)}
\begin{itemize}
    \item In x-direction:
    $$x=11.9 \mathrm{m}=(47.2 \mathrm{~m} / \mathrm{s})(\cos \theta) t$$
    $$t= \frac{0.252}{\cos \theta}$$
    \item Substitute into kinematic equation:
    $$1.59 \mathrm{~m}=(11.9 \mathrm{~m}) \tan \theta+(0.311 \mathrm{~m})(1+\tan ^{2} \theta)$$
    \item Solve for $\theta$:
    $$\tan \theta=0.107 \text{ or } \underline{\theta}=6.1^{\circ}$$
\end{itemize}
\end{frame}

\begin{frame}

\frametitle{Problem 37: Solution (Part 3)}
\begin{itemize}
    \item Calculate time for ball to fall 2.5 m:
    $$t=0.366 \mathrm{~s}$$
    \item Calculate range:
    $$R=v_{x} t= 17.2 \mathrm{~m}$$
    \item Answer: Yes, the ball lands 5.3 m from the net, within the service box.
\end{itemize}
\end{frame}

\section{Problem 39: Gun Sights}

\begin{frame}
\frametitle{Problem 39: Gun Sights}
\begin{block}{Question}
(a) A gun is sighted to hit targets at the same height, 100.0 m away. How low will the bullet hit if aimed at a target 150.0 m away? The muzzle velocity is $275 \mathrm{~m} / \mathrm{s}$.\\

(b) Discuss qualitatively how a larger muzzle velocity would affect this problem and what would be the effect of air resistance.
\end{block}

\end{frame}

\begin{frame}
\frametitle{Problem 39: Gun Sights}
\begin{block}{Question}
(a) A gun is sighted to hit targets at the same height, 100.0 m away. How low will the bullet hit if aimed at a target 150.0 m away? The muzzle velocity is $275 \mathrm{~m} / \mathrm{s}$.\\

(b) Discuss qualitatively how a larger muzzle velocity would affect this problem and what would be the effect of air resistance.
\end{block}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\linewidth]{phys12-projectile-gun_sights_diagram.jpg}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{Problem 39: Solution (Part 1)}
\begin{itemize}
    \item Use range equation to find initial angle:
    $$R=\frac{v_{0}^{2} \sin 2 \theta_{0}}{g}$$
    $$\theta_{0}=\frac{1}{2} \sin ^{-1}\left(\frac{g R}{v_{0}^{2}}\right)$$
    $$\theta_{0}=\frac{1}{2} \sin ^{-1}\left[\frac{\left(9.80 \mathrm{~m} / \mathrm{s}^{2}\right)(100 \mathrm{m})}{(275 \mathrm{~m} / \mathrm{s})^{2}}\right]=0.3712^{\circ}$$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 39: Solution (Part 2)}
\begin{itemize}
    \item Calculate time to travel 150 m:
    $$x-x_{0}=150 \mathrm{~m}=v_{0} \cos \theta_{0} t$$
    $$t=\frac{x-x_{0}}{v_{0} \cos \theta_{0}}=\frac{150 \mathrm{m}}{(275 \mathrm{~m} / \mathrm{s}) \cos 0.3712^{\circ}}=0.5455 \mathrm{~s}$$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 39: Solution (Part 3)}
\begin{itemize}
    \item Calculate vertical displacement:
    $$y-y_{0}=v_{0y} t-\frac{1}{2} g t^{2}$$
    $$=(275 \mathrm{~m} / \mathrm{s}) \sin 0.3712^{\circ}(0.5455 \mathrm{~s})-\frac{1}{2}(9.80 \mathrm{m} / \mathrm{s}^{2})(0.5455 \mathrm{~s})^2$$
    $$=-0.730 \mathrm{~m}$$
    \item The bullet hits 0.730 m below the target.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 39: Qualitative Discussion}
\begin{block}{(b) Effects of larger muzzle velocity and air resistance}
\begin{itemize}
    \item Larger muzzle velocity:
    \begin{itemize}
        \item Flatter trajectory
        \item Less vertical drop
        \item Bullet would hit closer to the target
    \end{itemize}
    \item Air resistance:
    \begin{itemize}
        \item Reduces horizontal velocity
        \item Increases vertical drop
        \item Bullet would hit lower than calculated
    \end{itemize}
\end{itemize}
\end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch20-21_slides_electric-current.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Electric Circuits]{PHYS12 CH: 20, 21}
\subtitle{Electric Circuits: Principles, Applications, and Safety}
\author[Mr. Gullo]{Mr. Gullo}
\date[Apr 2025]{April 8, 2025}
\institute[Physics Dept.]{Physics Department}

\begin{document}

% Title page
\begin{frame}
    \titlepage
\end{frame}

% Table of contents
\begin{frame}
    \frametitle{Lesson Overview}
    \tableofcontents
\end{frame}

% Learning objectives
\section{Introduction}
\begin{frame}
    \frametitle{Learning Objectives}
    \begin{block}{By the end of this lesson, you will be able to:}
        \begin{itemize}
            \item Define current, resistance, and voltage and explain their relationships
            \item Apply Ohm's law to simple circuits
            \item Calculate equivalent resistance for series and parallel circuits
            \item Calculate electric power and energy in circuits
            \item Distinguish between AC and DC circuits and their properties
            \item Describe electric hazards and bioelectrical applications
            \item Explain how measuring instruments work in DC circuits
            \item Understand null measurement techniques
            \item Describe the behavior of RC circuits during charging and discharging
            \item Solve complex circuit problems using Kirchhoff's rules
        \end{itemize}
    \end{block}
\end{frame}

% Current and Ohm's Law section
\section{Current and Ohm's Law}
\begin{frame}
    \frametitle{Electric Current}
    \begin{block}{Definition}
        Electric current is the rate at which charge flows:
        \[ I = \frac{\Delta Q}{\Delta t} \]
        where $\Delta Q$ is the amount of charge passing through an area in time $\Delta t$.
    \end{block}
    \begin{itemize}
        \item SI unit: ampere (A), where 1 A = 1 C/s
        \item Conventional current: direction of positive charge movement
        \item Current is the flow of free charges (electrons, ions)
        \item Related to drift velocity: $I = nqAv_d$
    \end{itemize}
    \end{frame}
    \begin{frame}{}
    \begin{figure}
        \centering
        \includegraphics[width=1\linewidth]{phys12-circuits-charge-carrier-drift.png}
    \end{figure}
\end{frame}

\begin{frame}
    \frametitle{Ohm's Law and Simple Circuits}
    \begin{block}{Ohm's Law}
        For a simple circuit with a single voltage source and resistance:
        \[ I = \frac{V}{R} \]
    \end{block}
    \begin{itemize}
        \item Resistance ($R$): opposition to current flow
        \item Unit: ohm ($\Omega$), where 1 $\Omega$ = 1 V/A
        \item Voltage drop across a resistor: $V = IR$
    \end{itemize}
    \begin{center}
        \begin{figure}
            \centering
            \includegraphics[width=0.5\linewidth]{phys12-gravity-newtons-law-of-universal-gravitation-formula.jpg}
        \end{figure}
    \end{center}
\end{frame}

\begin{frame}
    \frametitle{Resistance and Resistivity}
    \begin{block}{Resistance Formula}
        For a cylindrical conductor:
        \[ R = \rho\frac{L}{A} \]
        where $\rho$ is resistivity, $L$ is length, and $A$ is cross-sectional area.
    \end{block}
    \begin{itemize}
        \item Materials classified as conductors, semiconductors, or insulators
        \item Temperature affects resistivity: $\rho = \rho_0(1 + \alpha\Delta T)$
        \item Temperature affects resistance: $R = R_0(1 + \alpha\Delta T)$
        \item $\alpha$ is the temperature coefficient of resistivity
    \end{itemize}
\end{frame}
\begin{frame}{}
    \begin{figure}
        \centering
        \includegraphics[width=1\linewidth]{phys12-circuits-rc-circuit-diagram.png}
    \end{figure}
\end{frame}

\begin{frame}
    \frametitle{Electric Power and Energy}
    \begin{block}{Electric Power}
        Rate at which electrical energy is supplied or dissipated:
        \[ P = IV = \frac{V^2}{R} = I^2R \]
    \end{block}
    \begin{itemize}
        \item Energy used: $E = Pt$
        \item Units: Watts (W) for power, Joules (J) for energy
        \item Example: A 60W light bulb connected to 120V draws 0.5A
    \end{itemize}
    \vspace{0.5cm}
    \begin{alertblock}{Power Comparison}
        Different power ratings lead to different brightness in bulbs,
        different amounts of heat generated in resistors, etc.
    \end{alertblock}
\end{frame}

\begin{frame}
    \frametitle{AC vs. DC}
    \begin{block}{Direct Current (DC)}
        \begin{itemize}
            \item Current flows in only one direction
            \item Source voltage is constant
            \item Examples: batteries, solar cells, DC power supplies
        \end{itemize}
    \end{block}
    \begin{block}{Alternating Current (AC)}
        \begin{itemize}
            \item Voltage varies sinusoidally: $V = V_0 \sin 2\pi ft$
            \item Current varies sinusoidally: $I = I_0 \sin 2\pi ft$
            \item $V_0$ and $I_0$ are peak values, $f$ is frequency in Hz
            \item Examples: household electricity, power transmission
        \end{itemize}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{AC Power and RMS Values}
    \begin{block}{Average AC Power}
        \[ P_{ave} = \frac{1}{2}I_0V_0 = I_{rms}V_{rms} \]
    \end{block}
    \begin{itemize}
        \item RMS (Root Mean Square) values:
        \[ I_{rms} = \frac{I_0}{\sqrt{2}} \quad \text{and} \quad V_{rms} = \frac{V_0}{\sqrt{2}} \]
        \item Ohm's Law for AC: $I_{rms} = \frac{V_{rms}}{R}$
        \item Power formulas (similar to DC):
        \[ P_{ave} = I_{rms}V_{rms} = \frac{V_{rms}^2}{R} = I_{rms}^2R \]
    \end{itemize}
  \end{frame}

\begin{frame}
\begin{figure}
      \centering
      \includegraphics[width=0.75\linewidth]{phys12-circuits-rms-voltage-ac.png}
  \end{figure}
\end{frame}

\begin{frame}
    \frametitle{Electric Hazards and the Human Body}
    \begin{block}{Types of Electric Hazards}
        \begin{itemize}
            \item Thermal hazards: Excessive power causing burns or fires
            \item Shock hazards: Current flowing through a person
        \end{itemize}
    \end{block}
    \begin{block}{Shock Severity Factors}
        \begin{itemize}
            \item Current magnitude
            \item Current path through body
            \item Duration of exposure
            \item AC frequency
        \end{itemize}
    \end{block}
    \begin{center}
        \begin{tabular}{|c|l|}
            \hline
            \textbf{Current (mA)} & \textbf{Effect on Human Body} \\
            \hline
            1 & Threshold of perception \\
            5 & Painful shock, can cause muscle contraction \\
            10-20 & Cannot let go, respiratory paralysis \\
            100-300 & Ventricular fibrillation, potential death \\
            \hline
        \end{tabular}
    \end{center}
\end{frame}

\begin{frame}
    \frametitle{Nerve Conduction and Bioelectricity}
    \begin{block}{Bioelectricity Basics}
        \begin{itemize}
            \item Electric potentials in neurons created by ionic concentration differences
            \item Semipermeable membranes separate different ionic concentrations
            \item Stimuli change membrane permeability, creating action potentials
            \item Action potentials propagate along neurons as electrical signals
        \end{itemize}
    \end{block}
    \begin{block}{Electrocardiogram (ECG)}
        \begin{itemize}
            \item Records electrical activity of the heart
            \item Measures voltage differences on body surface
            \item Helps diagnose heart conditions and abnormalities
        \end{itemize}
    \end{block}

\end{frame}
\begin{frame}{}
    \begin{figure}
        \centering
        \includegraphics[width=1\linewidth]{phys12-circuits-ecg-waveform.png}
    \end{figure}
\end{frame}

% Complex Circuits section
\section{Complex Circuits}
\begin{frame}
    \frametitle{Resistors in Series}
    \begin{block}{Series Configuration}
        Resistors are in series when they are connected end-to-end.
        \[ R_s = R_1 + R_2 + R_3 + \ldots \]
    \end{block}
    \begin{itemize}
        \item Same current flows through each resistor
        \item Voltage is divided among resistors: $V = V_1 + V_2 + V_3 + \ldots$
        \item Individual voltage drops: $V_1 = IR_1$, $V_2 = IR_2$, etc.
    \end{itemize}
    \begin{center}
       \begin{figure}
           \centering
           \includegraphics[width=0.75\linewidth]{phys12-circuits-resistors-in-series.png}
       \end{figure}
    \end{center}
\end{frame}

\begin{frame}
    \frametitle{Resistors in Parallel}
    \begin{block}{Parallel Configuration}
        Resistors are in parallel when they share the same two endpoints.
        \[ \frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \ldots \]
    \end{block}
    \begin{itemize}
        \item Same voltage across each resistor
        \item Current divides among resistors: $I = I_1 + I_2 + I_3 + \ldots$
        \item Individual currents: $I_1 = \frac{V}{R_1}$, $I_2 = \frac{V}{R_2}$, etc.
    \end{itemize}
    \begin{center}
        \begin{figure}
            \centering
            \includegraphics[width=0.5\linewidth]{phys12-circuits-rc-circuit-diagram.png}
        \end{figure}
    \end{center}
\end{frame}

\begin{frame}
    \frametitle{Electromotive Force and Terminal Voltage}
    \begin{block}{Voltage Source Components}
        A real voltage source has:
        \begin{itemize}
            \item Electromotive force (emf): potential difference when no current flows
            \item Internal resistance ($r$): resistance within the source
        \end{itemize}
    \end{block}
    \begin{itemize}
        \item Terminal voltage: $V = \text{emf} - Ir$
        \item Series voltage sources: internal resistances add, emfs add algebraically
        \item Solar cells: series for increased voltage, parallel for increased current
    \end{itemize}

\end{frame}
\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-circuits-internal-resistance.png}
\end{figure}
\end{frame}
\begin{frame}
    \frametitle{Kirchhoff's Rules}
    \begin{block}{Junction Rule (First Rule)}
        The sum of all currents entering a junction must equal the sum of all currents leaving the junction.
        \[ \sum I_{\text{in}} = \sum I_{\text{out}} \]
    \end{block}
    \begin{block}{Loop Rule (Second Rule)}
        The algebraic sum of potential changes around any closed circuit path (loop) must be zero.
        \[ \sum \Delta V = 0 \]
    \end{block}
    \begin{itemize}
        \item Based on conservation of charge and energy
        \item Essential for analyzing complex circuits
    \end{itemize}
    \end{frame}
    \begin{frame}{}

    \begin{figure}
        \centering
        \includegraphics[width=1\linewidth]{phys12-circuits-kirchhoffs-junction-rule.jpg}
    \end{figure}
\end{frame}

\begin{frame}
    \frametitle{DC Voltmeters and Ammeters}
    \begin{block}{Measuring Instruments}
        \begin{itemize}
            \item Voltmeters measure voltage (potential difference)
            \item Ammeters measure current
        \end{itemize}
    \end{block}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \textbf{Voltmeter Characteristics:}
            \begin{itemize}
                \item Connected in parallel with component
                \item Must have very high resistance
                \item Minimizes impact on circuit
            \end{itemize}
        \end{column}
        \begin{column}{0.5\textwidth}
            \textbf{Ammeter Characteristics:}
            \begin{itemize}
                \item Connected in series with circuit
                \item Must have very low resistance
                \item Minimizes voltage drop
            \end{itemize}
        \end{column}
    \end{columns}
    \begin{figure}
        \centering
        \includegraphics[width=0.3\linewidth]{phys12-circuits-ammeter-voltmeter-connection.jpg}
    \end{figure}
\end{frame}

\begin{frame}
    \frametitle{Null Measurements}
    \begin{block}{Null Measurement Technique}
        \begin{itemize}
            \item Achieves greater accuracy by balancing a circuit
            \item No current flows through measuring device at balance point
            \item Used for precise voltage and resistance measurements
        \end{itemize}
    \end{block}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \textbf{Potentiometer:}
            \begin{itemize}
                \item Determines voltage precisely
                \item Uses a calibrated variable resistance
                \item Balances unknown voltage against known voltage
            \end{itemize}
        \end{column}
        \begin{column}{0.5\textwidth}
            \textbf{Wheatstone Bridge:}
            \begin{itemize}
                \item Determines resistance precisely
                \item Uses ratio of resistances
                \item At balance: $\frac{R_1}{R_2} = \frac{R_x}{R_3}$
            \end{itemize}

    \begin{figure}
        \centering
        \includegraphics[width=0.5\linewidth]{phys12-circuits-wheatstone-bridge.jpg}
    \end{figure}
         \end{column}
    \end{columns}
\end{frame}

% RC Circuits section
\section{RC Circuits}
\begin{frame}
    \frametitle{RC Circuits Basics}
    \begin{block}{RC Circuit Definition}
        A circuit containing both a resistor and a capacitor.
    \end{block}
    \begin{itemize}
        \item Time constant: $\tau = RC$
        \item Determines the rate of charging or discharging
        \item Units: seconds (s)
    \end{itemize}

        \begin{figure}
            \centering
            \includegraphics[width=0.65\linewidth]{phys12-circuits-kirchhoffs-junction-rule.jpg}
        \end{figure}

\end{frame}

\begin{frame}
    \frametitle{Charging and Discharging RC Circuits}
    \begin{block}{Charging a Capacitor}
        When an initially uncharged capacitor ($V_0 = 0$ at $t = 0$) is charged:
        \[ V = \text{emf}(1-e^{-t/RC}) \]
    \end{block}
    \begin{block}{Discharging a Capacitor}
        When a capacitor with initial voltage $V_0$ is discharged:
        \[ V = V_0e^{-t/RC} \]
    \end{block}
    \begin{itemize}
        \item Charging: voltage rises by 0.632 of remaining value per time constant
        \item Discharging: voltage falls by 0.368 of remaining value per time constant
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{RC Circuits: Graphical Representation}
    \begin{center}
        \begin{tabular}{cc}
            \begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys12-circuits-capacitor-discharge-curve.png}
\end{figure}
&
\begin{figure}
                \centering
                \includegraphics[width=0.4\linewidth]{phys12-electrostatics-charge-interactions.png}
            \end{figure} \\


                        Charging: $V = \text{emf}(1-e^{-t/RC})$ & Discharging: $V = V_0e^{-t/RC}$
        \end{tabular}
    \end{center}
    \begin{itemize}
        \item Both processes are asymptotic
        \item Full charging/discharging theoretically takes infinite time
        \item Practically complete (99.99\%) after 5 time constants
    \end{itemize}
\end{frame}

% Examples section
\section{Examples}
\begin{frame}
    \frametitle{I Do: Equivalent Resistance Calculation}
    \begin{block}{Problem}
        Calculate the equivalent resistance of a circuit with three resistors: $R_1 = 2.0~\Omega$ and $R_2 = 4.0~\Omega$ in parallel, and $R_3 = 3.0~\Omega$ in series with the parallel combination.
    \end{block}
    \begin{block}{Solution}
        Step 1: Find the equivalent resistance of $R_1$ and $R_2$ in parallel.
        \begin{align*}
            \frac{1}{R_p} &= \frac{1}{R_1} + \frac{1}{R_2} = \frac{1}{2.0~\Omega} + \frac{1}{4.0~\Omega}\\
            &= 0.5~\Omega^{-1} + 0.25~\Omega^{-1} = 0.75~\Omega^{-1}\\
            R_p &= \frac{1}{0.75~\Omega^{-1}} = 1.33~\Omega
        \end{align*}

        Step 2: Find the total resistance by adding $R_p$ and $R_3$ in series.
        \begin{align*}
            R_{total} &= R_p + R_3 = 1.33~\Omega + 3.0~\Omega = 4.33~\Omega
        \end{align*}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{We Do: Current and Power in a Parallel Circuit}
    \begin{block}{Problem}
        For the circuit shown with a 12V battery, $R_1 = 4\Omega$ and $R_2 = 8\Omega$ in parallel, calculate:
        \begin{enumerate}[(a)]
            \item The equivalent resistance
            \item The total current from the battery
            \item The current through each resistor
            \item The voltage across each resistor
            \item The power dissipated by each resistor
        \end{enumerate}
    \end{block}
    \begin{figure}
        \centering
        \includegraphics[width=0.5\linewidth]{phys12-circuits-parallel-circuit-with-battery.jpg}
    \end{figure}
\end{frame}

\begin{frame}
    \frametitle{We Do: Current and Power in a Parallel Circuit}
    \begin{block}{Partial Solution}
        (a) Equivalent resistance:
        \begin{align*}
            \frac{1}{R_{eq}} &= \frac{1}{R_1} + \frac{1}{R_2} = \frac{1}{4\Omega} + \frac{1}{8\Omega}\\
            &= 0.25\Omega^{-1} + 0.125\Omega^{-1} = 0.375\Omega^{-1}\\
            R_{eq} &= \frac{1}{0.375\Omega^{-1}} = 2.67\Omega
        \end{align*}

        (b) Total current from the battery:
        \begin{align*}
            I_{total} &= \frac{V}{R_{eq}} = \frac{12V}{2.67\Omega} = 4.5A
        \end{align*}

        (c) Current through each resistor:
        \begin{align*}
            I_1 &= \frac{V}{R_1} = \frac{12V}{4\Omega} = 3A\\
            I_2 &= \text{?} \quad \text{(complete this step)}
        \end{align*}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{We Do: Current and Power in a Parallel Circuit}
    \begin{block}{Partial Solution (cont.)}
        (d) Voltage across each resistor:
        \begin{align*}
            V_1 &= \text{?} \quad \text{(complete this step)}\\
            V_2 &= \text{?} \quad \text{(complete this step)}
        \end{align*}

        (e) Power dissipated by each resistor:
        \begin{align*}
            P_1 &= \text{?} \quad \text{(complete this step)}\\
            P_2 &= \text{?} \quad \text{(complete this step)}
        \end{align*}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{You Do: Terminal Voltage and Power}
    \begin{block}{Problem}
        A circuit contains a 9V battery with internal resistance $r = 0.5\Omega$ connected to a resistor $R = 5.5\Omega$.
        \begin{enumerate}[(a)]
            \item Calculate the terminal voltage.
            \item Calculate the current in the circuit.
            \item Calculate the power dissipated in the resistor.
            \item Calculate the power dissipated in the battery's internal resistance.
            \item Calculate the power supplied by the battery's emf.
        \end{enumerate}
    \end{block}
    \end{frame}

% Summary section
\section{Summary}
\begin{frame}
    \frametitle{Key Equations}
    \begin{columns}
        \begin{column}{0.5\textwidth}
            \textbf{Current and Resistance:}
            \begin{itemize}
                \item $I = \frac{\Delta Q}{\Delta t}$
                \item $I = \frac{V}{R}$ (Ohm's Law)
                \item $R = \rho\frac{L}{A}$
            \end{itemize}

            \textbf{Power and Energy:}
            \begin{itemize}
                \item $P = IV = \frac{V^2}{R} = I^2R$
                \item $E = Pt$
            \end{itemize}

            \textbf{AC Circuits:}
            \begin{itemize}
                \item $V = V_0 \sin 2\pi ft$
                \item $I_{rms} = \frac{I_0}{\sqrt{2}}$
                \item $V_{rms} = \frac{V_0}{\sqrt{2}}$
            \end{itemize}
        \end{column}
        \begin{column}{0.5\textwidth}
            \textbf{Circuit Analysis:}
            \begin{itemize}
                \item $R_s = R_1 + R_2 + R_3 + \ldots$
                \item $\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \ldots$
                \item $V = \text{emf} - Ir$
                \item $\sum I_{\text{in}} = \sum I_{\text{out}}$
                \item $\sum \Delta V = 0$
            \end{itemize}

            \textbf{RC Circuits:}
            \begin{itemize}
                \item $\tau = RC$
                \item $V = \text{emf}(1-e^{-t/RC})$ (charging)
                \item $V = V_0e^{-t/RC}$ (discharging)
            \end{itemize}

            \textbf{Null Measurements:}
            \begin{itemize}
                \item $\frac{R_1}{R_2} = \frac{R_x}{R_3}$ (Wheatstone bridge)
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}

\begin{frame}
    \frametitle{Concept Review}
    \begin{itemize}
        \item Current is the rate of charge flow; resistance opposes current.
        \item Ohm's Law relates current, voltage, and resistance in simple circuits.
        \item Power measures the rate of energy transfer in circuits.
        \item DC provides constant voltage; AC varies sinusoidally with time.
        \item Series resistance increases; parallel resistance decreases.
        \item Real voltage sources have internal resistance that affects terminal voltage.
        \item Kirchhoff's rules help analyze complex circuits using conservation principles.
        \item Proper measuring instrument connection is crucial for accurate readings.
        \item Null measurement techniques provide greater accuracy for precise measurements.
        \item RC circuits show exponential charging and discharging behavior characterized by the time constant $\tau$.
        \item Electrical safety requires understanding current thresholds and shock hazards.
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{Questions?}
    \begin{center}
        \Large Thank you for your attention!

        \vspace{1cm}

        Any questions?
    \end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch01-02_IntroPhysics_one-kinematics.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[1D Kinematics Review]{PHYS12 CH:1.1-1.4, 2.1-2.8}
\subtitle{Progression from Physics 11 to Physics 12: Advanced Kinematics}
\author[Mr. Gullo]{Mr. Gullo}
\date[Aug 28, 2025]{August 28, 2025}

\begin{document}
\frame{\titlepage}

\section{Introduction and Objectives}

\begin{frame}
\frametitle{Learning Objectives}
\framesubtitle{Reviewing the Fundamentals of Motion}
After this lesson, you will be able to:
\begin{itemize}
    \item Define position, displacement, distance, velocity, speed, and acceleration.
    \item Differentiate between vector and scalar quantities.
    \item Analyze one-dimensional motion under constant acceleration.
    \item Apply the kinematic equations to solve problems involving motion.
    \item Interpret position-time and velocity-time graphs to describe motion.
    \item Describe the motion of objects in free-fall.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Physics 11 to Physics 12 Progression}
\framesubtitle{Building on Your Foundation}
\begin{itemize}
    \item \alert{Physics 11 Foundation}: Basic kinematic concepts, graphical analysis, and problem-solving methods
    \pause
    \item \alert{Physics 12 Enhancement}: More complex applications, vector analysis, and real-world scenarios
    \pause
    \item \alert{Key Progression Areas}:
    \begin{itemize}
        \item Multi-dimensional motion analysis
        \item Vector decomposition and composition
        \item Advanced problem-solving strategies
        \item Real-world applications and limitations
    \end{itemize}
\end{itemize}
\end{frame}

\section{Key Concepts}

\begin{frame}
\frametitle{Key Concepts}
\framesubtitle{Position, Displacement, and Distance}
\begin{description}
    \item[Position ($x$)] The location of an object at a particular time. It is a vector quantity.
    \pause
    \item[Displacement ($\Delta x$)] The change in an object's position. It is a vector pointing from the initial position ($x_0$) to the final position ($x_f$).
    \begin{center}
        $\Delta x = x_f - x_0$
    \end{center}
    \pause
    \item[Distance Traveled] The total length of the path traveled between two positions. It is a scalar quantity and is always positive.
\end{description}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization}
\framesubtitle{Context: Displacement vs. Distance}
Imagine walking from your home to school.
\begin{itemize}
    \item The winding path you take along sidewalks represents the \alert{distance traveled}.
    \item A straight line drawn directly from your home to the school represents your \alert{displacement}.
\end{itemize}
\vspace{1em}
These two values are often different. Displacement only cares about the start and end points, not the path taken.
\end{frame}

\begin{frame}
\frametitle{Concept Visualization}
\framesubtitle{Displacement vs. Distance Traveled}
\begin{figure}
    \centering
    \includegraphics[width=0.7\linewidth]{phys12-mechanics-distance-displacement-diagram.png}
    \caption{Displacement is the shortest path, while distance is the actual path taken.}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Key Concepts}
\framesubtitle{Scalars vs. Vectors}
In physics, we use two types of quantities to describe the world:
\begin{columns}[T]
    \begin{column}{0.5\textwidth}
        \alert{Scalar}
        \begin{itemize}
            \item A quantity described by \textbf{magnitude} (a numerical value) only.
            \item Examples:
            \begin{itemize}
                \item Distance (5 m)
                \item Speed (10 m/s)
                \item Time (15 s)
                \item Mass (2 kg)
            \end{itemize}
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \alert{Vector}
        \begin{itemize}
            \item A quantity described by both \textbf{magnitude and direction}.
            \item Examples:
            \begin{itemize}
                \item Displacement (5 m, East)
                \item Velocity (10 m/s, North)
                \item Acceleration (9.8 m/s$^2$, Down)
                \item Force (20 N, Up)
            \end{itemize}
        \end{itemize}
    \end{column}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Key Concepts}
\framesubtitle{Velocity, Speed, and Acceleration}
\begin{description}
    \item[Average Speed] The total distance traveled divided by the elapsed time. A scalar.
    \pause
    \item[Average Velocity ($\bar{v}$)] Displacement divided by elapsed time. A vector.
    \[ \bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_0}{t_f - t_0} \]
    \pause
    \item[Acceleration ($a$)] The rate at which velocity changes. A vector.
    \[ \bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_0}{t_f - t_0} \]
    \textit{Deceleration} is simply acceleration in the direction opposite to the velocity.
\end{description}
\end{frame}

\begin{frame}
\frametitle{Key Concepts}
\framesubtitle{Free Fall}
\begin{itemize}
    \item An object in \alert{free-fall} is one that is moving under the influence of gravity alone (air resistance is considered negligible).
    \pause
    \item On Earth, all free-falling objects experience a constant downward acceleration, known as the \alert{acceleration due to gravity ($g$)}.
    \begin{center}
        $g = 9.80 \, \text{m/s}^2$
    \end{center}
    \pause
    \item The sign of acceleration depends on your chosen coordinate system. Conventionally, "up" is positive, which makes acceleration $a = -g = -9.80 \, \text{m/s}^2$.
\end{itemize}
\end{frame}

\section{The Kinematic Equations}

\begin{frame}
\frametitle{Essential Equations}
\framesubtitle{For Motion with Constant Acceleration}
These equations are the foundation for solving problems in 1D kinematics. They are only valid when acceleration \textit{a} is constant.
\begin{align*}
    v &= v_0 + at \\
    \Delta x &= v_0 t + \frac{1}{2}at^2 \\
    v^2 &= v_0^2 + 2a\Delta x \\
    \Delta x &= \frac{v_0 + v}{2} t
\end{align*}
\vspace{1em}
\begin{columns}[T]
    \begin{column}{0.5\textwidth}
        \textbf{Variables}
        \begin{itemize}
            \item $\Delta x$: displacement (m)
            \item $t$: elapsed time (s)
            \item $v_0$: initial velocity (m/s)
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \begin{itemize}
            \item $v$: final velocity (m/s)
            \item $a$: constant acceleration (m/s$^2$)
        \end{itemize}
    \end{column}
\end{columns}
\end{frame}

\section{Graphical Analysis}

\begin{frame}
\frametitle{Graphical Analysis of Motion}
\framesubtitle{Context: Position vs. Time Graph}
A graph of an object's position ($x$) as a function of time ($t$) provides a wealth of information about its motion.
\begin{itemize}
    \item The \alert{slope} of the line reveals the object's velocity.
    \item A straight line means constant velocity.
    \item A curved line means the velocity is changing (i.e., there is acceleration).
\end{itemize}
\vspace{1em}
On the next slide, we will visualize the difference between \alert{average velocity} (slope between two points) and \alert{instantaneous velocity} (slope at a single point).
\end{frame}

\begin{frame}
\frametitle{Graphical Analysis of Motion}
\framesubtitle{Visualization: Position vs. Time}
\begin{figure}
\begin{tikzpicture}
\begin{axis}[
    width=\textwidth,
    height=0.75\textheight,
    axis lines=left,
    xlabel={Time, $t$ (s)},
    ylabel={Position, $x$ (m)},
    xmin=0, xmax=5,
    ymin=0, ymax=14,
    xtick={0,1,2,3,4,5},
    ytick={0,2,4,6,8,10,12,14},
    legend pos=north west,
    label style={font=\large},
    tick label style={font=\small},
]
% Main curve: x = 0.5*t^2 + t
\addplot[ds9blue, thick, domain=0:4.5, samples=100, line width=1.5pt] {0.5*x^2 + x} node[right, pos=0.9] {$x(t)$};

% Secant line for average velocity between t=1 and t=4
\addplot[ds9gold, dashed, domain=1:4, line width=1.5pt] {2.5*x - 1};
\node[ds9gold] at (axis cs:3, 8) [above] {Avg. Velocity};
\fill[black] (axis cs:1, 1.5) circle (2pt);
\fill[black] (axis cs:4, 12) circle (2pt);

% Tangent line for instantaneous velocity at t=2
\addplot[ds9red, dotted, domain=0.5:3.5, line width=1.5pt] {3*x - 2};
\node[ds9red] at (axis cs:1.5, 1) [below] {Inst. Velocity};
\fill[black] (axis cs:2, 4) circle (2pt);

\end{axis}
\end{tikzpicture}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Graphical Analysis of Motion}
\framesubtitle{Context: Velocity vs. Time Graph}
A graph of velocity ($v$) versus time ($t$) also tells a detailed story.
\begin{itemize}
    \item The \alert{slope} of the line is the object's \textbf{acceleration}.
    \item The \alert{area under the curve} is the object's \textbf{displacement} ($\Delta x$).
\end{itemize}
\vspace{1em}
Next, we will see these two concepts illustrated for an object with constant positive acceleration.
\end{frame}

\begin{frame}
\frametitle{Graphical Analysis of Motion}
\framesubtitle{Visualization: Velocity vs. Time}
\begin{figure}
\begin{tikzpicture}
\begin{axis}[
    width=\textwidth,
    height=0.75\textheight,
    axis lines=left,
    xlabel={Time, $t$ (s)},
    ylabel={Velocity, $v$ (m/s)},
    xmin=0, xmax=5,
    ymin=0, ymax=12,
    xtick={0,1,2,3,4,5},
    ytick={0,2,4,6,8,10,12},
    legend pos=north west,
    label style={font=\large},
    tick label style={font=\small},
]
% Velocity line: v = 2*t + 1
\addplot[ds9blue, thick, domain=0:5, samples=2, line width=1.5pt] {2*x + 1} node[right, pos=0.8, anchor=south west] {$v(t)$};

% Annotate slope
\draw[ds9red, line width=1pt, <->] (axis cs:4.2, 5) -- (axis cs:4.2, 7) node[midway, right] {$\Delta v$};
\draw[ds9red, line width=1pt, <->] (axis cs:2, 5) -- (axis cs:3, 5) node[midway, below] {$\Delta t$};
\node[ds9red, align=center] at (axis cs:1.5, 8) {Slope = $a$};

% Shade area for displacement
\addplot[ds9gold!30, fill=ds9gold!30] coordinates {(0,1) (4,9) (4,0) (0,0)};
\node[black] at (axis cs:2, 2.5) {Area = $\Delta x$};

\end{axis}
\end{tikzpicture}
\end{figure}
\end{frame}

\section{Problem Solving Practice}

\begin{frame}
\frametitle{Problem Solving}
\framesubtitle{The GUESS Method}
We will use a structured method to solve physics problems.
\begin{itemize}
    \item \textbf{G} - \alert{Givens}: List all known quantities from the problem, with variables and units. Define your coordinate system (e.g., up is positive).
    \item \textbf{U} - \alert{Unknown}: Identify what quantity you need to find.
    \item \textbf{E} - \alert{Equation}: Choose a kinematic equation that relates your givens and unknown.
    \item \textbf{S} - \alert{Substitute}: Plug your known values into the equation, including units.
    \item \textbf{S} - \alert{Solve}: Calculate the answer and make sure it has the correct units and significant figures.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{I Do: Freeway Acceleration - Problem Setup}
\framesubtitle{Problem based on Ch. 2, Problem 24}
\begin{block}{Problem}
A car enters a freeway, accelerating from rest at a rate of $2.40 \, \text{m/s}^2$ for $12.0 \, \text{s}$. How far does the car travel in this time?
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item Direction of motion: positive
\item $\vec{a} = +2.40 \, \text{m/s}^2$, $t = 12.0 \, \text{s}$
\item $\vec{v}_0 = 0 \, \text{m/s}$ (starts from rest)
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item $\Delta \vec{x} = ?$ (displacement)
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I Do: Freeway Acceleration - Equation Selection}
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item Direction of motion: positive
\item $\vec{a} = +2.40 \, \text{m/s}^2$, $t = 12.0 \, \text{s}$
\item $\vec{v}_0 = 0 \, \text{m/s}$ (starts from rest)
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item $\Delta \vec{x} = ?$ (displacement)
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{E - Equation}
\begin{itemize}
\item Select: $\Delta x = v_0 t + \frac{1}{2}at^2$
\item Already solved for displacement
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{I Do: Freeway Acceleration - Solution}
\begin{block}{S - Substitute}
\begin{itemize}
\item Plug values with units:
\[ \Delta x = (0 \, \text{m/s})(12.0 \, \text{s}) + \frac{1}{2}(2.40 \, \text{m/s}^2)(12.0 \, \text{s})^2 \]
\end{itemize}
\end{block}
\pause
\begin{block}{S - Solve}
\begin{itemize}
\item Calculate with unit analysis:
\[ \Delta x = 0 + \frac{1}{2}(2.40 \, \text{m/s}^2)(144 \, \text{s}^2) \]
\[ \Delta x = (1.20 \, \text{m/s}^2)(144 \, \text{s}^2) = 172.8 \, \text{m} \]
\item Apply sig figs: $\alert{173 \, \text{m}}$
\item \boxed{173 \, \text{m}}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{We Do: Dolphin's Jump}
\framesubtitle{Problem based on Ch. 2, Problem 45}
\begin{block}{Problem}
A dolphin in an aquatic show jumps straight up out of the water at a velocity of $13.0 \, \text{m/s}$. How high does it rise above the water?
\end{block}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item Upwards is positive
\item $\vec{v}_0 = +13.0 \, \text{m/s}$, $\vec{a} = -9.80 \, \text{m/s}^2$
\item At max height: $\vec{v} = 0 \, \text{m/s}$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item $\Delta \vec{y} = ?$ (height)
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{G - Givens}
\begin{itemize}
\item Upwards is positive
\item $\vec{v}_0 = +13.0 \, \text{m/s}$, $\vec{a} = -9.80 \, \text{m/s}^2$
\item At max height: $\vec{v} = 0 \, \text{m/s}$
\end{itemize}
\end{block}
\pause
\column{0.48\textwidth}
\begin{block}{U - Unknown}
\begin{itemize}
\item $\Delta \vec{y} = ?$ (height)
\end{itemize}
\end{block}
\end{columns}
\pause
\begin{columns}[T]
\column{0.48\textwidth}
\begin{block}{E - Equation}
\begin{itemize}
\item Select: $v^2 = v_0^2 + 2a\Delta y$
\item Rearrange: $\Delta y = \frac{v^2 - v_0^2}{2a}$
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\begin{block}{S - Substitute}
\begin{itemize}
    \item Plug values: $\Delta y = \frac{(0)^2 - (13.0)^2}{2(-9.80)}$
\end{itemize}
\end{block}
\pause
\begin{block}{S - Solve}
\begin{itemize}
    \item Calculate: $\Delta y = \frac{0 - 169}{-19.6} = \frac{-169}{-19.6}$
    \item $\Delta y = 8.62 \, \text{m}$
    \item \boxed{8.62 \, \text{m}}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{You Do: Swan's Takeoff}
\framesubtitle{Problem based on Ch. 2, Problem 31}
\begin{block}{Problem}
A swan on a lake accelerates from rest at an average rate of $0.350 \, \text{m/s}^2$ to take off. It must reach a velocity of $6.00 \, \text{m/s}$ to get airborne.
\end{block}
\begin{enumerate}
    \item How far does it travel before becoming airborne?
    \item How long does this take?
\end{enumerate}

\begin{block}{Your Turn}
    Use the GUESS method to solve this problem on your own.
    \begin{itemize}
        \item List your givens and what you need to find for each part.
        \item Choose the appropriate equation for each part.
        \item Solve for one unknown at a time.
    \end{itemize}
\end{block}

\pause

\begin{beamercolorbox}[rounded=true,shadow=true]{info}
\centering
\textbf{Solution Check:} Your final answers should be (a) $\approx 51.4$ m and (b) $\approx 17.1$ s.
\end{beamercolorbox}

\end{frame}


\section{Conclusion}

\begin{frame}
\frametitle{Reading Homework}
\framesubtitle{Foundational Physics Concepts}
Please review these foundational sections for our next class:

\begin{itemize}
    \item \textbf{Section 1.5}: Physical Quantities and Units
    \item \textbf{Section 1.6}: Vector Addition and Subtraction
    \item \textbf{Section 1.7}: Vector Components
    \item \textbf{Section 1.8}: Relative Velocity
\end{itemize}

\begin{beamercolorbox}[rounded=true,shadow=true]{info}
\centering
\textbf{Focus on:} Understanding vector operations and relative motion concepts. These will be essential for our upcoming 2D motion unit.
\end{beamercolorbox}
\end{frame}

\begin{frame}
\frametitle{Summary}
\framesubtitle{Key Takeaways from 1D Kinematics}
\begin{itemize}
    \item \textbf{Scalars vs. Vectors}: Distance and speed are scalars; displacement, velocity, and acceleration are vectors (direction matters!).
    \pause
    \item \textbf{Constant Acceleration}: The kinematic equations are powerful tools, but they only apply when acceleration is constant. Free-fall is a key example ($a = -g$).
    \pause
    \item \textbf{Graphical Analysis}: Graphs provide a visual understanding of motion.
    \begin{itemize}
        \item Slope of position-time graph $\rightarrow$ velocity
        \item Slope of velocity-time graph $\rightarrow$ acceleration
        \item Area under velocity-time graph $\rightarrow$ displacement
    \end{itemize}
    \pause
    \item \textbf{Problem Solving}: A structured approach like the GUESS method is crucial for success.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Homework: Physics 11 Review}
\framesubtitle{Essential Preparation for Advanced Topics}

To ensure success in Physics 12, please review these fundamental concepts from Physics 11:

\begin{itemize}
    \item \textbf{Chapter 1 Review}: Units, measurements, and significant figures
    \item \textbf{Chapter 2 Review}: Kinematic equations and problem-solving methods
    \item \textbf{Graphical Analysis}: Position-time and velocity-time graphs
    \item \textbf{Vector Basics}: Adding and subtracting vectors graphically
\end{itemize}

\begin{beamercolorbox}[rounded=true,shadow=true]{info}
\centering
\textbf{Focus on:} Mastering the GUESS method and understanding the difference between scalars and vectors. These skills will be critical for our upcoming 2D motion unit.
\end{beamercolorbox}

\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch22-23_slides_electromagnetic-induction.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Magnetism \& EM Induction]{PHYS11 CH: 22-23}
\subtitle{Magnetism and Electromagnetic Induction}
\author[Mr. Gullo]{Mr. Gullo}
\date[April 2025]{April 10, 2025}
\institute[Physics]{PHYS11 - College Physics}

\begin{document}

% Title slide
\frame{\titlepage}

% Outline slide
\begin{frame}
\frametitle{Outline}
\tableofcontents
\end{frame}

\section{Introduction to Magnetism}

\begin{frame}
\frametitle{Learning Objectives}
\begin{block}{By the end of this presentation, you will be able to:}
\begin{itemize}
    \item Describe the properties of magnets and magnetic fields
    \item Apply the right hand rules to determine directions of magnetic forces and fields
    \item Calculate magnetic forces on moving charges and current-carrying conductors
    \item Explain electromagnetic induction and apply Faraday's law
    \item Understand the operation of generators, motors, and transformers
    \item Calculate inductance and analyze RL and RLC circuits
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Magnets and Magnetic Fields}
\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
    \item Magnets have north and south poles
    \item North pole: attracted to Earth's geographic north
    \item Like poles repel, unlike poles attract
    \item Poles always occur in pairs (no magnetic monopoles)
    \item All magnetism is created by electric current
\end{itemize}
\column{0.4\textwidth}
\alert{[Image of bar magnets showing attraction between opposite poles and repulsion between like poles]}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Magnetic Field Lines}
\begin{block}{Properties of Magnetic Field Lines}
\begin{enumerate}
    \item Field is tangent to the magnetic field line
    \item Field strength is proportional to line density
    \item Field lines cannot cross
    \item Field lines are continuous loops
\end{enumerate}
\end{block}
\alert{[Diagram showing magnetic field lines around a bar magnet]}
\end{frame}

\begin{frame}
\frametitle{Ferromagnets and Electromagnets}
\begin{columns}
\column{0.5\textwidth}
\textbf{Ferromagnetic Materials:}
\begin{itemize}
    \item Iron, cobalt, nickel, gadolinium
    \item Atoms act like small magnets
    \item Form domains where magnetic moments align
    \item Curie temperature: above this temperature, ferromagnetism disappears
\end{itemize}
\column{0.5\textwidth}
\textbf{Electromagnets:}
\begin{itemize}
    \item Current through a wire creates magnetic field
    \item Adding ferromagnetic core increases field strength
    \item Applications: motors, generators, MRI machines
\end{itemize}
\end{columns}
\alert{[Image showing magnetic domains in a ferromagnetic material]}
\end{frame}

\section{Magnetic Forces}

\begin{frame}
\frametitle{Force on a Moving Charge}
\begin{block}{Magnetic Force Formula}
\begin{equation}
\vec{F} = q\vec{v} \times \vec{B} \quad \text{or} \quad F = qvB\sin\theta
\end{equation}
\end{block}
\begin{itemize}
    \item $q$ = charge (C)
    \item $v$ = velocity (m/s)
    \item $B$ = magnetic field strength (T)
    \item $\theta$ = angle between $\vec{v}$ and $\vec{B}$
    \item Direction determined by Right Hand Rule 1 (RHR-1)
\end{itemize}
\alert{[Illustration of Right Hand Rule 1]}
\end{frame}

\begin{frame}
\frametitle{Right Hand Rule 1 (RHR-1)}
\begin{block}{RHR-1 for Force on a Moving Charge}
Point the thumb of your right hand in the direction of the velocity $\vec{v}$, fingers in the direction of the magnetic field $\vec{B}$, and the force $\vec{F}$ is perpendicular to the palm.
\end{block}
\begin{itemize}
    \item For negative charges, force is in opposite direction
    \item Force is always perpendicular to both $\vec{v}$ and $\vec{B}$
    \item When $\vec{v}$ and $\vec{B}$ are parallel, $\vec{F} = 0$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Motion of Charged Particles in Magnetic Fields}
\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
    \item When velocity perpendicular to field, particles move in circular path
    \item Radius of circular path: $r = \frac{mv}{qB}$
    \item Magnetic force provides centripetal force
    \item Period of revolution independent of speed
    \item Helical path when velocity has component parallel to field
\end{itemize}
\column{0.4\textwidth}
\alert{[Diagram showing circular motion of charged particle in magnetic field]}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Force on Current-Carrying Conductors}
\begin{block}{Magnetic Force on a Current-Carrying Conductor}
\begin{equation}
\vec{F} = I\vec{l} \times \vec{B} \quad \text{or} \quad F = IlB\sin\theta
\end{equation}
\end{block}
\begin{itemize}
    \item $I$ = current (A)
    \item $l$ = length of conductor (m)
    \item $B$ = magnetic field strength (T)
    \item $\theta$ = angle between $\vec{l}$ and $\vec{B}$
    \item Direction follows RHR-1 with thumb in direction of current
\end{itemize}
\alert{[Diagram showing force on a current-carrying wire in a magnetic field]}
\end{frame}

\begin{frame}
\frametitle{Torque on Current Loops}
\begin{block}{Torque on a Current Loop}
\begin{equation}
\tau = NIAB\sin\theta
\end{equation}
\end{block}

\begin{itemize}
    \item $N$ = number of turns
    \item $I$ = current (A)
    \item $A$ = area of loop (m$^2$)
    \item $B$ = magnetic field strength (T)
    \item $\theta$ = angle between loop normal and $\vec{B}$
\end{itemize}

\textbf{Applications:} Electric motors, meters
\alert{[Diagram of a current loop in a magnetic field showing torque]}
\end{frame}

\section{Magnetic Fields from Currents}

\begin{frame}
\frametitle{Magnetic Fields Produced by Currents}
\begin{block}{Magnetic Field from a Long Straight Wire}
\begin{equation}
B = \frac{\mu_0 I}{2\pi r}
\end{equation}
\end{block}

\begin{itemize}
    \item $\mu_0 = 4\pi \times 10^{-7}$ T$\cdot$m/A (permeability of free space)
    \item $I$ = current (A)
    \item $r$ = distance from wire (m)
    \item Direction determined by Right Hand Rule 2 (RHR-2)
\end{itemize}
\alert{[Diagram showing magnetic field lines around a current-carrying wire]}
\end{frame}

\begin{frame}
\frametitle{Right Hand Rule 2 (RHR-2)}
\begin{block}{RHR-2 for Magnetic Field from Current}
Point the thumb of your right hand in the direction of the current, and your fingers curl in the direction of the magnetic field lines.
\end{block}
\begin{itemize}
    \item Field lines form concentric circles around a straight wire
    \item Field strength decreases with distance from wire
    \item Total field from any current path is the vector sum of fields from all segments
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Magnetic Fields from Loops and Solenoids}
\begin{columns}
\column{0.5\textwidth}
\textbf{Circular Loop:}
\begin{equation}
B = \frac{\mu_0 I}{2R} \quad \text{(at center)}
\end{equation}
\begin{itemize}
    \item $R$ = radius of loop (m)
    \item Direction from RHR-2
\end{itemize}
\column{0.5\textwidth}
\textbf{Solenoid:}
\begin{equation}
B = \mu_0 n I \quad \text{(inside)}
\end{equation}
\begin{itemize}
    \item $n$ = number of turns per unit length
    \item Field inside is uniform
\end{itemize}
\end{columns}
\alert{[Diagram comparing field patterns of loop and solenoid]}
\end{frame}

\section{Electromagnetic Induction}

\begin{frame}
\frametitle{Magnetic Flux}
\begin{block}{Magnetic Flux Definition}
\begin{equation}
\Phi = BA\cos\theta
\end{equation}
\end{block}
\begin{itemize}
    \item $B$ = magnetic field strength (T)
    \item $A$ = area (m$^2$)
    \item $\theta$ = angle between $\vec{B}$ and area normal
    \item Units: T$\cdot$m$^2$ or weber (Wb)
    \item Flux measures the amount of magnetic field passing through an area
\end{itemize}
\alert{[Diagram illustrating magnetic flux through a loop]}
\end{frame}

\begin{frame}
\frametitle{Faraday's Law of Induction}
\begin{block}{Faraday's Law}
\begin{equation}
\text{emf} = -N\frac{\Delta\Phi}{\Delta t}
\end{equation}
\end{block}
\begin{itemize}
    \item emf = induced electromotive force (voltage)
    \item $N$ = number of turns in coil
    \item $\Delta\Phi/\Delta t$ = rate of change of magnetic flux
    \item Minus sign represents Lenz's law
    \item Electromagnetic induction: process of inducing emf through changing magnetic flux
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Lenz's Law}
\begin{block}{Lenz's Law}
The induced emf creates a current that produces a magnetic field that opposes the change in flux that produced it.
\end{block}
\begin{itemize}
    \item Conservation of energy principle
    \item Determines direction of induced current
    \item Represented by minus sign in Faraday's law
\end{itemize}
\alert{[Diagram showing Lenz's law - induced current creating opposing magnetic field]}
\end{frame}

\begin{frame}
\frametitle{Motional Emf}
\begin{block}{Motional Emf Formula}
\begin{equation}
\text{emf} = Blv \quad \text{(}B, l, \text{ and } v \text{ perpendicular)}
\end{equation}
\end{block}
\begin{itemize}
    \item $B$ = magnetic field strength (T)
    \item $l$ = length of conductor (m)
    \item $v$ = velocity (m/s)
    \item Special case of Faraday's law
    \item Induced when conductor moves through magnetic field
\end{itemize}
\alert{[Diagram of a conductor moving through a magnetic field]}
\end{frame}

\begin{frame}
\frametitle{Eddy Currents and Magnetic Damping}
\begin{itemize}
    \item \textbf{Eddy currents}: current loops induced in moving conductors
    \item Produced when conductors move through non-uniform magnetic fields
    \item \textbf{Magnetic damping}: drag force created by eddy currents
    \item Applications:
    \begin{itemize}
        \item Electromagnetic brakes
        \item Metal detectors
        \item Induction stoves
        \item Damping in moving-coil meters
    \end{itemize}
\end{itemize}
\alert{[Diagram showing eddy currents in a conductor moving through a magnetic field]}
\end{frame}

\section{Applications}

\begin{frame}
\frametitle{Electric Generators}
\begin{block}{Induced EMF in a Generator}
\begin{equation}
\text{emf} = NAB\omega\sin\omega t
\end{equation}
\end{block}
\begin{itemize}
    \item $N$ = number of turns
    \item $A$ = area of coil (m$^2$)
    \item $B$ = magnetic field strength (T)
    \item $\omega$ = angular velocity (rad/s)
    \item Peak emf: $\text{emf}_0 = NAB\omega$
    \item Converts mechanical energy to electrical energy
\end{itemize}
\alert{[Diagram of a simple AC generator]}
\end{frame}

\begin{frame}
\frametitle{Back EMF in Motors}
\begin{itemize}
    \item Motors are generators running in reverse
    \item Rotating coil in motor induces its own emf
    \item \textbf{Back emf}: induced emf that opposes the applied voltage
    \item Limits current through motor
    \item Proportional to motor's rotation speed
    \item Low back emf during startup → high current draw
\end{itemize}
\alert{[Diagram illustrating back emf in a motor]}
\end{frame}

\begin{frame}
\frametitle{Transformers}
\begin{block}{Transformer Equations}
\begin{align}
\frac{V_s}{V_p} &= \frac{N_s}{N_p} \\
\frac{I_s}{I_p} &= \frac{N_p}{N_s}
\end{align}
\end{block}
\begin{itemize}
    \item Use induction to change voltage levels
    \item $V_p$, $V_s$ = primary and secondary voltages
    \item $N_p$, $N_s$ = primary and secondary turns
    \item $I_p$, $I_s$ = primary and secondary currents
    \item Step-up: $N_s > N_p$, increases voltage
    \item Step-down: $N_s < N_p$, decreases voltage
    \item Power is conserved: $V_pI_p = V_sI_s$
\end{itemize}
\alert{[Diagram of transformer showing primary and secondary coils]}
\end{frame}

\begin{frame}
\frametitle{Electrical Safety Systems}
\begin{columns}
\column{0.5\textwidth}
\textbf{Three-Wire System:}
\begin{itemize}
    \item Live/hot wire
    \item Neutral wire
    \item Ground wire
    \item Grounds appliance case
\end{itemize}

\textbf{Circuit Breakers/Fuses:}
\begin{itemize}
    \item Interrupt excessive currents
    \item Prevent thermal hazards
\end{itemize}
\column{0.5\textwidth}
\textbf{GFI (Ground Fault Interrupter):}
\begin{itemize}
    \item Detects current imbalance
    \item Protects against shock
    \item Uses induction principles
\end{itemize}

\textbf{Isolation Transformer:}
\begin{itemize}
    \item Insulates device from source
    \item Prevents ground loops
\end{itemize}
\end{columns}
\end{frame}

\section{Inductance and AC Circuits}

\begin{frame}
\frametitle{Inductance}
\begin{block}{Self-Inductance}
\begin{equation}
\text{emf} = -L\frac{\Delta I}{\Delta t}
\end{equation}
\end{block}
\begin{itemize}
    \item \textbf{Inductance}: property describing how effectively a device induces emf
    \item $L$ = self-inductance (H, henry)
    \item $\Delta I/\Delta t$ = rate of current change (A/s)
    \item 1 H = 1 $\Omega\cdot$s
    \item Self-inductance of a solenoid: $L = \frac{\mu_0N^2A}{l}$
    \item Energy stored in inductor: $E_{ind} = \frac{1}{2}LI^2$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{RL Circuits}
\begin{columns}
\column{0.6\textwidth}
\textbf{Current when turning on:}
\begin{equation}
I = I_0(1 - e^{-t/\tau})
\end{equation}

\textbf{Current when turning off:}
\begin{equation}
I = I_0e^{-t/\tau}
\end{equation}

\textbf{Time constant:} $\tau = \frac{L}{R}$
\column{0.4\textwidth}
\begin{itemize}
    \item $I_0 = \frac{V}{R}$ is final current
    \item Current rises to $0.632I_0$ in first time constant
    \item Current falls to $0.368I_0$ in first time constant
\end{itemize}
\end{columns}
\alert{[Graph showing current vs. time for RL circuit turning on and off]}
\end{frame}

\begin{frame}
\frametitle{Reactance in AC Circuits}
\begin{columns}
\column{0.5\textwidth}
\textbf{Inductive Reactance:}
\begin{equation}
X_L = 2\pi fL
\end{equation}
\begin{itemize}
    \item In inductors, voltage leads current by 90°
    \item Reactance increases with frequency
\end{itemize}
\column{0.5\textwidth}
\textbf{Capacitive Reactance:}
\begin{equation}
X_C = \frac{1}{2\pi fC}
\end{equation}
\begin{itemize}
    \item In capacitors, voltage lags current by 90°
    \item Reactance decreases with frequency
\end{itemize}
\end{columns}
\alert{[Phasor diagrams showing phase relationships between voltage and current]}
\end{frame}

\begin{frame}
\frametitle{RLC Series Circuits}
\begin{block}{Impedance in RLC Circuit}
\begin{equation}
Z = \sqrt{R^2 + (X_L - X_C)^2}
\end{equation}
\end{block}
\begin{itemize}
    \item \textbf{Impedance}: AC equivalent of resistance
    \item \textbf{Resonant frequency}: $f_0 = \frac{1}{2\pi\sqrt{LC}}$
    \item At resonance: $X_L = X_C$ and $Z = R$
    \item \textbf{Phase angle}: $\cos\phi = \frac{R}{Z}$
    \item \textbf{Average power}: $P_{ave} = I_{rms}V_{rms}\cos\phi$
    \item \textbf{Power factor}: $\cos\phi$ (ranges from 0 to 1)
\end{itemize}
\alert{[Graph showing impedance vs. frequency with resonance peak]}
\end{frame}

\section{Example Problems}

\begin{frame}
\frametitle{I Do: Force on a Moving Charge}
\begin{block}{Example Problem}
An electron (charge $q = -1.6 \times 10^{-19}$ C) is moving at $v = 2.0 \times 10^7$ m/s perpendicular to a magnetic field of $B = 0.5$ T. Calculate the magnetic force on the electron.
\end{block}

\begin{align}
F &= |q|vB\sin\theta \\
&= (1.6 \times 10^{-19} \text{ C})(2.0 \times 10^7 \text{ m/s})(0.5 \text{ T})(\sin 90°) \\
&= (1.6 \times 10^{-19})(2.0 \times 10^7)(0.5)(1) \\
&= 1.6 \times 10^{-12} \text{ N}
\end{align}

Direction: Use RHR-1, but reverse direction since electron is negatively charged.
\end{frame}

\begin{frame}
\frametitle{We Do: Circular Motion in Magnetic Field}
\begin{block}{Example Problem}
A proton (mass $m = 1.67 \times 10^{-27}$ kg, charge $q = 1.6 \times 10^{-19}$ C) is moving at $v = 3.0 \times 10^6$ m/s perpendicular to a magnetic field of $B = 0.2$ T. Calculate the radius of its circular path.
\end{block}

\begin{align}
r &= \frac{mv}{qB} \\
&= \frac{(1.67 \times 10^{-27} \text{ kg})(3.0 \times 10^6 \text{ m/s})}{(1.6 \times 10^{-19} \text{ C})(0.2 \text{ T})} \\
&= ?
\end{align}

Let's work through this together...
\end{frame}

\begin{frame}
\frametitle{You Do: Faraday's Law Application}
\begin{block}{Example Problem}
A 200-turn circular coil with area $0.25 \text{ m}^2$ is in a magnetic field that changes from 0.5 T to 0.8 T perpendicular to the coil over a time of 0.1 s. Calculate the magnitude of the induced emf.
\end{block}

\begin{align}
\text{emf} &= -N\frac{\Delta\Phi}{\Delta t} \\
&= -N\frac{\Delta(BA\cos\theta)}{\Delta t} \\
&= ? \text{ V}
\end{align}

Try solving this problem yourself!
\end{frame}

\section{Summary}

\begin{frame}
\frametitle{Key Equations}
\begin{columns}
\column{0.5\textwidth}
\textbf{Magnetic Forces:}
\begin{align}
F &= qvB\sin\theta \\
F &= IlB\sin\theta \\
\tau &= NIAB\sin\theta
\end{align}

\textbf{Magnetic Fields:}
\begin{align}
B &= \frac{\mu_0I}{2\pi r} \text{ (straight wire)} \\
B &= \frac{\mu_0I}{2R} \text{ (loop center)} \\
B &= \mu_0nI \text{ (solenoid)}
\end{align}
\column{0.5\textwidth}
\textbf{Electromagnetic Induction:}
\begin{align}
\Phi &= BA\cos\theta \\
\text{emf} &= -N\frac{\Delta\Phi}{\Delta t} \\
\text{emf} &= Blv \text{ (motional)}
\end{align}

\textbf{AC Circuits:}
\begin{align}
X_L &= 2\pi fL \\
X_C &= \frac{1}{2\pi fC} \\
Z &= \sqrt{R^2 + (X_L - X_C)^2}
\end{align}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Key Concepts}
\begin{itemize}
    \item Magnetic fields exert forces on moving charges and current-carrying conductors
    \item The direction of magnetic forces and fields can be determined using right hand rules
    \item Changing magnetic fields induce emfs (electromagnetic induction)
    \item Lenz's law: induced effects oppose the change that caused them
    \item Applications include generators, motors, and transformers
    \item Inductors oppose changes in current
    \item In AC circuits, impedance combines resistance and reactance
    \item At resonance, inductive and capacitive reactances cancel
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Thank You!}
\begin{center}
\Large{Questions?}

\vspace{1cm}
\normalsize{Next class: Electromagnetic Waves}
\end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch07-1_slides_energy-part1-2.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{/Users/joelgullo/dev/latex-beamer/shared/templates/ds9_theme}

% Title page configuration
\title[PHYS12 CH7]{Work and Energy}
\subtitle{Chapter 7.1-7.6: Conservative and Nonconservative Forces}
\author[Mr. Gullo]{Mr. Gullo}
\date[Nov 2024]{November 2024}

\begin{document}

\frame{\titlepage}

% NEW: Progression Context Frames
\begin{frame}
\frametitle{Unit 3: Work, Energy and Power}
\begin{block}{Unit Overview}
This unit reframes the conservation of energy principle with a more sophisticated understanding of nonconservative forces.
\end{block}
\pause

\begin{block}{What You Already Know (Physics 11)}
\begin{itemize}
    \item Definition of Work: $W = Fd\cos\theta$
    \item Kinetic Energy: $KE = \frac{1}{2}mv^2$
    \item Work-Energy Theorem: $W_{net} = \Delta KE$
    \item Gravitational Potential Energy: $PE_g = mgh$
    \item Conservation of Mechanical Energy (no friction): $KE_i + PE_i = KE_f + PE_f$
    \item Power: $P = W/t = Fv$
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{What's New in Physics 12}
\begin{block}{New Concepts}
\begin{itemize}
    \item Formal classification of forces as \textbf{Conservative} (gravity, elastic) and \textbf{Nonconservative} (friction, drag)
    \pause
    \item \textbf{Generalized Conservation of Energy} principle accounting for work done by nonconservative forces:
    \[W_{nc} = \Delta KE + \Delta PE\]
\end{itemize}
\end{block}
\pause

\begin{block}{Application Focus}
Solving energy conservation problems where mechanical energy is NOT conserved. Calculate work done by friction (or other nonconservative forces) and account for it as loss of mechanical energy from the system, typically dissipated as heat.
\end{block}
\end{frame}

\section{Review: Work and Energy Fundamentals}

\begin{frame}
\frametitle{Work: Quick Review}
\begin{itemize}
    \item Work is transfer of energy by a force acting on an object as it is displaced
    \item Mathematical definition: $W = F d \cos\theta$
    \pause
    \item Where:
    \begin{itemize}
        \item $W$ is work (joules, J)
        \item $F$ is force (newtons, N)
        \item $d$ is displacement (meters, m)
        \item $\theta$ is angle between force and displacement
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{When is Work Positive, Negative, or Zero?}
\begin{itemize}
    \item Work is \textbf{zero} when:
    \begin{itemize}
        \item Force and displacement are perpendicular ($\theta = 90$)
        \item There is no displacement ($d = 0$)
    \end{itemize}
    \pause
    \item Work is \textbf{positive} when:
    \begin{itemize}
        \item Force and displacement are in same direction ($\theta < 90$)
    \end{itemize}
    \pause
    \item Work is \textbf{negative} when:
    \begin{itemize}
        \item Force and displacement are in opposite directions ($90 < \theta \leq 180$)
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Kinetic Energy Review}
\begin{itemize}
    \item Kinetic energy is energy of motion
    \item Formula: $KE = \frac{1}{2}mv^2$
    \pause
    \item Where:
    \begin{itemize}
        \item $m$ is mass (kg)
        \item $v$ is velocity (m/s)
    \end{itemize}
    \pause
    \item Work-Energy Theorem: $W_{net} = \Delta KE$
    \item Net work equals change in kinetic energy
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Gravitational Potential Energy Review}
\begin{itemize}
    \item Energy due to position in a gravitational field
    \item Formula: $PE_g = mgh$
    \pause
    \item Where:
    \begin{itemize}
        \item $m$ is mass (kg)
        \item $g$ is acceleration due to gravity (9.8 m/s²)
        \item $h$ is height (m)
    \end{itemize}
    \pause
    \item Depends only on vertical height change
    \item Reference level can be chosen arbitrarily
\end{itemize}
\end{frame}

\section{Example: Review Problems}

\begin{frame}
\frametitle{Example 7.1: Calculating Work You Do to Push a Lawn Mower}
A person pushing a lawn mower exerts a constant force of 75.0 N at an angle 35 below the horizontal.
\pause
The lawn mower is pushed 25.0 m on level ground.
\pause

\begin{figure}
    \centering
    \includegraphics[width=0.5\textwidth]{../images/mower-energy.jpg}
\end{figure}
\vspace{0.5cm}
\end{frame}

\begin{frame}
\textbf{Solution:}
\begin{align}
    W &= Fd\cos\theta \nonumber \\
    W &= (75.0\text{ N})(25.0\text{ m})\cos(35.0) \nonumber \\
    W &= 1536\text{ J} = 1.54 \times 10^3\text{ J} \nonumber \\
    \text{Convert to kcal:} &= 0.367\text{ kcal} \nonumber \\
    \text{Ratio to daily intake:} &= 1.53 \times 10^{-4} \nonumber
\end{align}
\end{frame}

\begin{frame}
\frametitle{Example 7.2: Calculating the Kinetic Energy of a Package}
A 30.0-kg package on a roller belt conveyor system moves at 0.500 m/s. Calculate the Kinetic Energy of the Package.
\pause
\vspace{0.5cm}
\begin{center}
		\includegraphics[width=0.7\linewidth]{pasted-images/ch07-1_slides_energy-part1-2-07-23-40.png}
	\end{center}
\end{frame}

\begin{frame}
\textbf{Solution Steps:}
\begin{enumerate}
    \item KE = $\frac{1}{2}mv^2$
    \pause
    \item KE = $0.5(30.0\text{ kg})(0.500\text{ m/s})^2$
    \pause
    \item KE = $3.75\text{ kg}\cdot\text{m}^2/\text{s}^2 = 3.75\text{ J}$
\end{enumerate}
\end{frame}

\section{7.4 Conservative Forces and Potential Energy}

\begin{frame}
\frametitle{Conservative Forces:}
\begin{block}{Definition}
A force is \textbf{conservative} if the work done by it on a particle is independent of the path taken.
\end{block}
\pause

\begin{itemize}
    \item Work depends ONLY on initial and final positions
    \pause
    \item Energy can be stored and fully recovered
    \pause
    \item Path doesn't matter, only endpoints
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Examples of Conservative Forces}
\begin{columns}[T]
\begin{column}{0.5\textwidth}
\textbf{Conservative Forces:}
\begin{itemize}
    \item Gravitational force
    \pause
    \item Elastic force (springs)
    \pause
    \item Electrostatic force
\end{itemize}
\pause

\end{column}

\pause

\begin{column}{0.5\textwidth}
\textbf{Key Properties:}
\begin{itemize}
    \item Work can be recovered
    \pause
    \item Path-independent
    \pause
    \item Associated with potential energy
    \pause
    \item Closed loop: $W_{total} = 0$
\end{itemize}
\end{column}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Visualizing Conservative Forces: Path Independence}
\begin{figure}
    \centering
    \includegraphics[width=0.5\textwidth]{../images/path-indep.png}
\end{figure}
\pause

\begin{block}{Key Insight}
For conservative forces, ALL paths between points A and B require the same work. Only the vertical height change matters for gravity.
\end{block}

\pause
\textbf{VIDEO:} Pendulum showing continuous KE $\leftrightarrow$ PE conversion (30-60 sec)
\end{frame}

\begin{frame}
\frametitle{Potential Energy and Conservative Forces}
\begin{itemize}
    \item Potential energy: energy stored due to position or configuration
    \pause
    \item For conservative forces:
    \[\Delta PE = -W_{\text{cons}}\]
    \pause
    \item Where:
    \begin{itemize}
        \item $\Delta PE$ is change in potential energy
        \item $W_{\text{cons}}$ is work done by conservative force
        \item Negative sign: force does positive work, PE decreases
    \end{itemize}
    \pause
    \item Types we'll use:
    \begin{itemize}
        \item Gravitational potential energy: $PE_g = mgh$
        \item Elastic potential energy: $PE_s = \frac{1}{2}kx^2$
    \end{itemize}
\end{itemize}
\end{frame}

\section{7.5 Conservation of Mechanical Energy}

\begin{frame}
\frametitle{Conservation of Mechanical Energy}
\begin{block}{When Only Conservative Forces Act}
Total mechanical energy remains constant:
\[E_{\text{total}} = KE + PE = \text{constant}\]
\end{block}
\pause

\begin{block}{Mathematical Expression}
\[KE_i + PE_i = KE_f + PE_f\]
\pause
Or equivalently:
\[\frac{1}{2}mv_i^2 + mgh_i = \frac{1}{2}mv_f^2 + mgh_f\]
\end{block}
\pause

\begin{alertblock}{Critical Condition}
This ONLY works when no nonconservative forces (like friction) do work on the system.
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Energy Transformation Diagram}
\begin{center}
\begin{center}
		\includegraphics[width=0.5\linewidth]{pasted-images/ch07-1_slides_energy-part1-2-07-29-45.png}
	\end{center}
\pause

\begin{itemize}
    \item Energy transforms between KE and PE
    \pause
    \item Total mechanical energy constant
    \pause
    \item At maximum height: all PE, no KE
\end{itemize}
\end{center}
\end{frame}

\section{7.6 Nonconservative Forces}

\begin{frame}
\frametitle{Nonconservative Forces:}
\begin{block}{Definition}
A force is \textbf{nonconservative} if the work done depends on the path taken.
\end{block}
\pause

\begin{itemize}
    \item Work depends on path, not just endpoints
    \pause
    \item Energy cannot be fully recovered
    \pause
    \item Mechanical energy is NOT conserved
    \pause
    \item Energy typically converted to heat, sound, or other forms
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Examples of Nonconservative Forces}
\begin{columns}[T]
\begin{column}{0.5\textwidth}
\textbf{Nonconservative Forces:}
\begin{itemize}
    \item Friction (kinetic)
    \pause
    \item Air resistance/drag
    \pause
    \item Tension (in most cases)
    \pause
    \item Applied forces from people/motors
\end{itemize}

\pause
\vspace{0.5cm}
\begin{center}
		\includegraphics[width=0.6\linewidth]{pasted-images/ch07-1_slides_energy-part1-2-07-48-38.png}
	\end{center}
\end{column}

\pause

\begin{column}{0.5\textwidth}
\textbf{Key Properties:}
\begin{itemize}
    \item Work cannot be recovered
    \pause
    \item Path-dependent
    \pause
    \item NOT associated with PE
    \pause
    \item Closed loop: $W_{total} \neq 0$
    \pause
    \item Dissipate mechanical energy
\end{itemize}
\end{column}
\end{columns}

\end{frame}

\begin{frame}
\frametitle{Visual Comparison: Conservative vs Nonconservative}
\begin{center}
\begin{center}
		\includegraphics[width=0.6\linewidth]{pasted-images/ch07-1_slides_energy-part1-2-12-22-12.png}
	\end{center}
\end{center}
\pause

\begin{columns}[T]
\begin{column}{0.5\textwidth}
\textbf{Conservative:}
\begin{itemize}
    \item Energy conserved
    \item Reversible motion
    \item Path independent
\end{itemize}
\end{column}

\begin{column}{0.5\textwidth}
\textbf{Nonconservative:}
\begin{itemize}
    \item Energy lost from system
    \item Irreversible
    \item Path dependent
\end{itemize}
\end{column}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Generalized Conservation of Energy}
\begin{block}{With Nonconservative Forces}
Change in mechanical energy equals work done by nonconservative forces:
\[\Delta E = W_{nc}\]
\pause
Or:
\[W_{nc} = \Delta KE + \Delta PE\]
\pause
Expanded form:
\[W_{nc} = (KE_f - KE_i) + (PE_f - PE_i)\]
\end{block}
\pause

\begin{alertblock}{Key Insight}
$W_{nc}$ is typically negative (friction removes energy from system). Mechanical energy decreases, converted to heat.
\end{alertblock}
\end{frame}

\begin{frame}
\frametitle{Energy Flow with Friction}
\begin{center}
\begin{center}
		\includegraphics[width=0.6\linewidth]{pasted-images/ch07-1_slides_energy-part1-2-12-25-24.png}
	\end{center}
\end{center}
\pause

\begin{block}{What Happens to "Lost" Energy?}
\begin{itemize}
    \item Converted to thermal energy (heat)
    \pause
    \item Sound energy
    \pause
    \item Deformation of materials
    \pause
    \item NOT destroyed (total energy still conserved)
    \pause
    \item Just no longer useful mechanical energy
\end{itemize}
\end{block}
\end{frame}

\section{Example Problems}

\begin{frame}
\frametitle{Guided Example: Spring and Projectile Motion}
A 2 kg mass is attached to a spring (k = 100 N/m) and compressed 0.3 m. What height will it reach when released?
\pause

\begin{figure}
\centering
\begin{center}
		\includegraphics[width=0.4\linewidth]{pasted-images/ch07-1_slides_energy-part1-2-12-26-59.png}
	\end{center}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Solution: Spring Problem}
\textbf{Step 1:} Initial energy (compressed spring)
\pause
\[\frac{1}{2}kx^2 = \frac{1}{2}(100)(0.3)^2 = 4.5 \text{ J}\]
\pause

\textbf{Step 2:} At maximum height (all gravitational PE)
\pause
\[PE_g = mgh = 4.5 \text{ J}\]
\pause

\textbf{Step 3:} Solve for h
\pause
\[h = \frac{4.5}{(2)(9.8)} = 0.23 \text{ m}\]
\pause

\textbf{Key:} Elastic PE converted entirely to gravitational PE (conservative forces only).
\end{frame}

\begin{frame}
\frametitle{You Do: Practice Problem}
\begin{block}{Problem}
A 0.5 kg ball is thrown upward with initial velocity 15 m/s. Calculate:
\begin{enumerate}
    \item Maximum height reached
    \item Velocity when it returns to half the maximum height
\end{enumerate}
Use conservation of energy principles!
\end{block}
\pause

\begin{block}{Hints}
\begin{itemize}
    \item Start with: $\frac{1}{2}mv_i^2 = mgh_{\max}$
    \item For part 2: $\frac{1}{2}mv_i^2 = \frac{1}{2}mv_f^2 + mg(h_{\max}/2)$
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{You Do: Solution}
\textbf{Part 1: Maximum height}
\pause
\[h_{\max} = 11.5 \text{ m}\]
\pause

\textbf{Part 2: Velocity at half max height}
\pause
\[v_f = 10.6 \text{ m/s}\]
\end{frame}
\begin{comment}
\begin{frame}
\frametitle{Example with Friction: Block Sliding Down Ramp}
\begin{block}{Problem Setup}
A 5 kg block slides down a 30 ramp from height 4 m. Coefficient of kinetic friction $\mu_k = 0.2$. Find final velocity at bottom.
\end{block}
\pause

\begin{center}
\begin{center}
		\includegraphics[width=0.6\linewidth]{pasted-images/ch07-1_slides_energy-part1-2-12-28-17.png}
	\end{center}
\end{center}
\end{frame}

\begin{frame}
\frametitle{Solution: Block with Friction}
\textbf{Step 1:} Without friction (conservative only)
\pause
\[v = \sqrt{2gh} = \sqrt{2(9.8)(4)} = 8.85 \text{ m/s}\]
\pause

\textbf{Step 2:} Calculate work by friction
\pause
\begin{itemize}
    \item Normal force: $N = mg\cos(30) = 5(9.8)(0.866) = 42.4$ N
    \pause
    \item Friction force: $f = \mu_k N = 0.2(42.4) = 8.48$ N
    \pause
    \item Distance along ramp: $d = h/\sin(30) = 4/0.5 = 8$ m
    \pause
    \item Work by friction: $W_f = -fd = -8.48(8) = -67.8$ J
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Solution: Block with Friction (continued)}
\textbf{Step 3:} Apply generalized energy conservation
\pause
\[W_{nc} = \Delta KE + \Delta PE\]
\pause
\[-67.8 = \frac{1}{2}(5)v_f^2 - 0 + 0 - 5(9.8)(4)\]
\pause
\[-67.8 = 2.5v_f^2 - 196\]
\pause
\[2.5v_f^2 = 128.2\]
\pause
\[v_f = 7.16 \text{ m/s}\]
\pause

\textbf{Compare:} Without friction: 8.85 m/s. With friction: 7.16 m/s. Energy lost to heat: 67.8 J.
\end{frame}
\end{comment}
\section{Common Misconceptions}

\begin{frame}
\frametitle{Common Mistakes: Conservative vs Nonconservative Forces}
\begin{alertblock}{Misconception 1}
"Tension is always a conservative force"
\end{alertblock}
\pause
\textbf{Reality:} Tension is typically nonconservative. It does path-dependent work.
\pause

\begin{alertblock}{Misconception 2}
"If energy is lost, conservation of energy is violated"
\end{alertblock}
\pause
\textbf{Reality:} Mechanical energy may not be conserved, but TOTAL energy (including heat, sound) is always conserved. Energy transforms, never disappears.
\end{frame}

\begin{frame}
\frametitle{Common Mistakes: Applying Energy Conservation}
\begin{alertblock}{Misconception 3}
"I can use $KE_i + PE_i = KE_f + PE_f$ for any problem"
\end{alertblock}
\pause
\textbf{Reality:} This ONLY works when no nonconservative forces do work. Must check for friction, air resistance first.
\pause

\begin{alertblock}{Misconception 4}
"Work by friction is always $W = \mu_k mg d$"
\end{alertblock}
\pause
\textbf{Reality:} This only works on horizontal surfaces. On ramps: $W = \mu_k N d$ where $N = mg\cos\theta$, not $mg$.
\end{frame}

\begin{frame}
\frametitle{Common Mistakes: Sign Errors}
\begin{alertblock}{Misconception 5}
"Work by friction should be positive since it's a force"
\end{alertblock}
\pause
\textbf{Reality:} Work by friction is negative because friction opposes motion ($\theta = 180$, so $\cos\theta = -1$).
\pause

\begin{alertblock}{Misconception 6}
"The negative sign in $\Delta PE = -W_{\text{cons}}$ means PE always decreases"
\end{alertblock}
\pause
\textbf{Reality:} Sign depends on direction. If conservative force does positive work (object moves in direction of force), PE decreases. If you do work against the force, PE increases.
\end{frame}

\begin{frame}
\frametitle{Common Mistakes: Problem Solving}
\begin{alertblock}{Misconception 7}
"Path matters for all forces"
\end{alertblock}
\pause
\textbf{Reality:} Path only matters for nonconservative forces. For conservative forces, only initial and final positions matter.
\pause

\begin{alertblock}{Misconception 8}
"Energy lost to friction just vanishes"
\end{alertblock}
\pause
\textbf{Reality:} Energy lost from mechanical energy system is converted to thermal energy (heat). It's still energy, just not useful for doing mechanical work. You can sometimes feel surfaces warm up after friction.
\end{frame}

\begin{frame}
\frametitle{Key Takeaways}
\begin{itemize}
    \item \textbf{Conservative forces:}
    \begin{itemize}
        \item Path-independent work
        \item Enable potential energy definition
        \item Mechanical energy conserved
    \end{itemize}
    \pause
    \item \textbf{Nonconservative forces:}
    \begin{itemize}
        \item Path-dependent work
        \item Convert mechanical energy to other forms
        \item Must account for in energy calculations
    \end{itemize}
    \pause
    \item \textbf{Problem-solving strategy:}
    \begin{itemize}
        \item Identify all forces (conservative vs nonconservative)
        \item If only conservative: use $KE_i + PE_i = KE_f + PE_f$
        \item If nonconservative present: use $W_{nc} = \Delta KE + \Delta PE$
    \end{itemize}
\end{itemize}
\end{frame}

\end{document}

```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch18_slides_electric-fields.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Electric Charge \& Field]{PHYS12 CH 18: Electric Charge and Electric Field}
\subtitle{Understanding fundamental electrostatic principles}
\author[Mr. Gullo]{Mr. Gullo}
\date[Mar 2025]{March, 2025}
\institute{Physics Department}

% Create some useful commands
\newcommand{\highlight}[1]{\textcolor{ds9red}{#1}}
\newcommand{\eqnlabel}[1]{\textcolor{ds9blue}{(#1)}}

% Begin document
\begin{document}

% Title page
\frame{\titlepage}

% Table of contents
\begin{frame}
    \frametitle{Outline}
    \tableofcontents
\end{frame}

% Learning objectives
\section{Learning Objectives}
\begin{frame}
    \frametitle{Learning Objectives}

    \begin{block}{By the end of this presentation, you will be able to:}
        \begin{itemize}
            \item Describe the fundamental properties of electric charge
            \item Distinguish between conductors and insulators
            \item Apply Coulomb's Law to calculate electrostatic forces
            \item Explain the concept of an electric field
            \item Interpret electric field lines and their meaning
            \item Understand electrostatic equilibrium in conductors
            \item Identify practical applications of electrostatics
        \end{itemize}
    \end{block}
\end{frame}

% Section: Static Electricity and Charge
\section{Static Electricity and Conservation of Charge}

\begin{frame}{Electric Charge}

        \begin{itemize}
            \item Only \highlight{two types of charge} exist:
                \begin{itemize}
                    \item Positive charge (protons)
                    \item Negative charge (electrons)
                \end{itemize}
            \item \highlight{Like charges repel}, \highlight{unlike charges attract}
            \item Force decreases with the \highlight{square of distance}
            \item Smallest unit of charge: \highlight{elementary charge}
                \begin{itemize}
                    \item $e = 1.60 \times 10^{-19}$ C
                \end{itemize}
        \end{itemize}

\end{frame}

\begin{frame}{Charge Interaction}

        \centering
        \begin{figure}
            \centering
            \includegraphics[width=0.9\linewidth]{phys12-electrostatics-field-lines-repulsion.png}
            \vspace{0.5cm}
            \includegraphics[width=0.9\linewidth]{phys12-electrostatics-charge-repulsion.png}
            \caption{Charge repulsion visualization}
        \end{figure}
\end{frame}

\begin{frame}
    \frametitle{Conservation of Charge}

    \begin{block}{Law of Conservation of Charge}
        \centering
        The net charge of an isolated system remains constant.\\
        \vspace{0.5em}
        \highlight{Charge cannot be created or destroyed.}
    \end{block}

    \begin{itemize}
        \item When an object becomes charged, it's due to a \highlight{transfer} of charge
        \item Common range for static electricity: nanocoulombs to microcoulombs
        \item Most charging results from \highlight{separation} of existing charges
        \item Example: Rubbing two neutral objects can transfer electrons
    \end{itemize}

    \begin{alertblock}{Important Equation}
        $Q_{system} = \sum q_i = \text{constant}$
    \end{alertblock}
\end{frame}

\begin{frame}{Charge Notation and Sources}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{itemize}
            \item \textbf{Big Q} ($Q$):
                \begin{itemize}
                    \item Represents total or net charge
                    \item Measured in coulombs (C)
                    \item Used for describing overall charge of objects or systems
                    \item Source: Accumulation of multiple elementary charges
                \end{itemize}
            \item \textbf{Little q} ($q$):
                \begin{itemize}
                    \item Represents individual charge or point charge
                    \item Used in force calculations between charges
                    \item Source: Individual charged particles or concentrated charge
                \end{itemize}
            \item \textbf{Point charge} (a particle having a charge):
                \begin{itemize}
                    \item Idealized model where charge is concentrated at a single point
                    \item Creates an electric field in surrounding space
                    \item Exerts force on other charges according to Coulomb's law
                \end{itemize}
            \item \textbf{Test charge} ($q_0$):
                \begin{itemize}
                    \item Small positive charge used to measure electric fields
                    \item Assumed small enough not to disturb the existing field
                    \item Used to define electric field: $\vec{E} = \frac{\vec{F}}{q_0}$
                \end{itemize}
            \item \textbf{Elementary charge} ($e$):
                \begin{itemize}
                    \item Smallest discrete unit of charge
                    \item $e = 1.60 \times 10^{-19}$ C
                    \item Source: Electrons (negative) and protons (positive)
                \end{itemize}
        \end{itemize}

        \column{0.4\textwidth}
        \centering
        \begin{align}
            Q &= N \cdot e\\
            F &= k\frac{q_1 q_2}{r^2}\\
            \vec{E} &= \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{r}
        \end{align}
        \vspace{0.5cm}
    \end{columns}
\end{frame}

% Section: Conductors and Insulators
\section{Conductors and Insulators}

\begin{frame}
    \frametitle{Conductors vs. Insulators}

    \begin{columns}
        \column{0.5\textwidth}
        \textbf{Conductors:}
        \begin{itemize}
            \item Allow \highlight{free movement} of charge
            \item Electrons move easily through material
            \item Examples: metals (copper, aluminum)
            \item Excess charge distributes on surface
        \end{itemize}

        \column{0.5\textwidth}
        \textbf{Insulators:}
        \begin{itemize}
            \item \highlight{Restrict movement} of charge
            \item Electrons tightly bound to atoms
            \item Examples: rubber, plastic, glass
            \item Charge remains at placement location
        \end{itemize}
    \end{columns}

    \vspace{1em}
    \begin{block}{Semiconductors}
        Materials with properties between conductors and insulators
        (e.g., silicon, germanium)
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{Polarization and Charging Methods}

    \textbf{Polarization:}
    \begin{itemize}
        \item Separation of positive and negative charges in a neutral object
        \item Induced by external electric field
        \item Creates local charge imbalances without overall charging
    \end{itemize}

    \vspace{0.5em}
    \textbf{Charging Methods:}
    \begin{itemize}
        \item \highlight{Charging by contact:}
            \begin{itemize}
                \item Direct touch transfers charge
                \item Objects acquire same type of charge
            \end{itemize}
        \item \highlight{Charging by induction:}
            \begin{itemize}
                \item No direct contact required
                \item Requires grounding during process
                \item Objects acquire opposite type of charge
            \end{itemize}
    \end{itemize}
\end{frame}

% Section: Coulomb's Law
\section{Coulomb's Law}

\begin{frame}
    \frametitle{Coulomb's Law}

    \begin{block}{Coulomb's Law}
        The electrostatic force between two point charges is:
        \begin{equation}
            \vec{F} = k\frac{|q_1 q_2|}{r^2}\hat{r} \eqnlabel{18.1}
        \end{equation}
        where:
        \begin{itemize}
            \item $k = 8.99 \times 10^9$ N$\cdot$m$^2$/C$^2$ (Coulomb constant)
            \item $q_1, q_2$ are charges in coulombs
            \item $r$ is the distance between charges in meters
            \item $\hat{r}$ is the unit vector pointing from $q_1$ to $q_2$
        \end{itemize}
    \end{block}

    \begin{itemize}
        \item \highlight{Inverse-square} relationship with distance
        \item Similar to gravitational force, but \highlight{much stronger}
        \item Can be \highlight{attractive} (opposite charges) or \highlight{repulsive} (like charges)
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{I Do: Coulomb's Law Example}

    \begin{exampleblock}{Example Problem}
        What is the repulsive force between two pith balls that are 8.00 cm apart and have equal charges of $-30.0$ nC?
    \end{exampleblock}
    \pause

    \begin{figure}
        \centering
        \includegraphics[width=0.4\linewidth]{phys12-electrostatics-pith-ball-electroscope.png}
    \end{figure}
\end{frame}


    \begin{frame}
    \frametitle{I Do: Coulomb's Law Example}

    \begin{exampleblock}{Example Problem}
        What is the repulsive force between two pith balls that are 8.00 cm apart and have equal charges of $-30.0$ nC?
    \end{exampleblock}
    \begin{block}{Solution}
        \begin{align}
            F &= k\frac{|q_1 q_2|}{r^2}\\
            &= (8.99 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2) \frac{(30.0 \times 10^{-9} \text{ C})^2}{(0.0800 \text{ m})^2}\\
            &= (8.99 \times 10^9) \frac{9.00 \times 10^{-16}}{6.40 \times 10^{-3}}\\
            &= 1.264 \times 10^{-3} \text{ N} \approx \highlight{1.27 \times 10^{-3} \text{ N}}
        \end{align}
    \end{block}

    \begin{itemize}
        \item The force is \highlight{repulsive} because the charges have the same sign
        \item This is a very small force, but measurable with sensitive equipment
    \end{itemize}
\end{frame}

% Section: Electric Field Concept
\section{Electric Field Concept}

\begin{frame}
    \frametitle{The Electric Field}

    \begin{block}{Electric Field Definition}
        The electric field $\vec{E}$ at a point in space is defined as the electric force $\vec{F}$ per unit charge that would act on a small positive test charge $q_0$ placed at that point:
        \begin{equation}
            \vec{E} = \frac{\vec{F}}{q_0} \eqnlabel{18.2}
        \end{equation}
    \end{block}

    \begin{itemize}
        \item Units: N/C (newtons per coulomb)
        \item A \highlight{vector} quantity with magnitude and direction
        \item Direction is the same as force on a \highlight{positive} test charge
        \item Exists at all points in space around charged objects
        \item Multiple electric fields \highlight{add vectorially}
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{Electric Field of a Point Charge}

    \begin{block}{Electric Field of a Point Charge}
        The electric field created by a point charge $Q$ at a distance $r$ is:
        \begin{equation}
            \vec{E} = k\frac{|Q|}{r^2}\hat{r} \eqnlabel{18.3}
        \end{equation}
        where $\hat{r}$ points away from a positive charge or toward a negative charge.
    \end{block}

    \begin{itemize}
        \item Field strength \highlight{decreases} with the square of distance
        \item Field extends to infinity, but becomes weaker with distance
        \item The field of multiple charges is the \highlight{vector sum} of individual fields:
        \begin{equation}
            \vec{E}_{total} = \vec{E}_1 + \vec{E}_2 + \vec{E}_3 + \ldots \eqnlabel{18.4}
        \end{equation}
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{We Do: Electric Field Example}

    \begin{exampleblock}{Example Problem}
        What is the magnitude and direction of an electric field that exerts a $2.00 \times 10^{-5}$ N upward force on a $-1.75$ μC charge?
    \end{exampleblock}
    \end{frame}

\begin{frame}
    \begin{block}{Let's Solve Together}
        Using the definition of electric field: $\vec{E} = \frac{\vec{F}}{q}$
        \begin{align}
            E &= \frac{F}{|q|}\\
            &= \frac{2.00 \times 10^{-5} \text{ N}}{1.75 \times 10^{-6} \text{ C}}\\
            &= 11.4 \text{ N/C}
        \end{align}

        For direction: Since the charge is \highlight{negative} and the force is \highlight{upward}, the electric field must be \highlight{downward}.

        Remember: $\vec{F} = q\vec{E}$, and negative charges experience force in the direction \highlight{opposite} to the electric field.
    \end{block}
\end{frame}

% Section: Electric Field Lines
\section{Electric Field Lines}

\begin{frame}
    \frametitle{Electric Field Lines: Visualization}

    \begin{block}{Electric Field Lines}
        Visual representation of electric fields with the following properties:
    \end{block}

    \begin{itemize}
        \item Start on \highlight{positive} charges, end on \highlight{negative} charges
        \item Direction of field is \highlight{tangent} to the line at any point
        \item Density of lines proportional to field \highlight{strength}
        \item Number of lines from/to a charge proportional to charge \highlight{magnitude}
        \item Lines \highlight{never cross} (field has unique direction at any point)
    \end{itemize}

    \begin{figure}
        \centering
        \includegraphics[width=1\linewidth]{phys12-electrostatics-point-charge-field-lines.png}
        \caption{Fig. 18.20}
    \end{figure}
\end{frame}

\begin{frame}
\begin{figure}
            \centering
\includegraphics[width=1\linewidth]{phys12-electrostatics-field-lines-repulsion.png}
            \vspace{0.5cm}

        \end{figure}
\end{frame}

\begin{frame}
    \frametitle{Field Line Patterns}

    \begin{columns}[t]
        \column{0.5\textwidth}
        \textbf{Single Point Charge:}
        \begin{itemize}
            \item Positive charge: lines point \highlight{outward}
            \item Negative charge: lines point \highlight{inward}
            \item Radially symmetric pattern
        \end{itemize}

        \textbf{Two Like Charges:}
        \begin{itemize}
            \item Lines repel each other
            \item Field-free point between charges
        \end{itemize}

        \column{0.5\textwidth}
        \textbf{Two Unlike Charges:}
        \begin{itemize}
            \item Lines connect charges
            \item Concentrated between charges
            \item Form dipole field at distance
        \end{itemize}

        \textbf{Electric Dipole:}
        \begin{itemize}
            \item Equal + and - charges separated by small distance
            \item Important in molecular interactions
        \end{itemize}
    \end{columns}
\end{frame}

% Section: Conductors in Electrostatic Equilibrium
\section{Conductors in Electrostatic Equilibrium}

\begin{frame}
    \frametitle{Conductors in Electrostatic Equilibrium}

    \begin{block}{Key Properties}
        When a conductor reaches electrostatic equilibrium:
    \end{block}

    \begin{itemize}
        \item The electric field \highlight{inside} the conductor is \highlight{zero}
        \item Any excess charge resides \highlight{entirely on the surface}
        \item The electric field at the surface is \highlight{perpendicular} to the surface
        \item Charge concentrates at surfaces with greater \highlight{curvature}
        \item Charge density is highest at \highlight{sharp points} and edges
    \end{itemize}

    \begin{alertblock}{Implications}
        This explains why lightning rods have sharp points and why Faraday cages shield their interiors from external fields.
    \end{alertblock}
\end{frame}

\begin{frame}
    \frametitle{Lightning Rods and Faraday Cages}

    \textbf{Lightning Rods:}
    \begin{itemize}
        \item Metal rod with \highlight{sharp point}
        \item Facilitates charge \highlight{dissipation} into air
        \item Provides safe path to ground for lightning
    \end{itemize}

    \vspace{0.5em}
    \textbf{Faraday Cages:}
    \begin{itemize}
        \item Conducting enclosure shields interior from external field
        \item External charges induce surface charges that \highlight{cancel} internal field
        \item Applications: elevators, cars, microwave ovens, sensitive equipment
        \item \highlight{Protection} during lightning storms
    \end{itemize}
\end{frame}

% Section: Applications of Electrostatics
\section{Applications of Electrostatics}

\begin{frame}
    \frametitle{Practical Applications of Electrostatics}

    \begin{columns}[t]
        \column{0.5\textwidth}
        \textbf{Van de Graaff Generator:}
        \begin{itemize}
            \item Research and educational tool
            \item Generates high voltage, low current
            \item Can produce millions of volts
        \end{itemize}

        \textbf{Photocopiers \& Laser Printers:}
        \begin{itemize}
            \item Use charged drum
            \item Toner particles attracted to charged regions
            \item Heat fuses toner to paper
        \end{itemize}

        \column{0.5\textwidth}
        \textbf{Ink-Jet Printers:}
        \begin{itemize}
            \item Electrically charge ink droplets
            \item Deflect droplets to precise positions
        \end{itemize}

        \textbf{Electrostatic Air Filters:}
        \begin{itemize}
            \item Charge air particles
            \item Attract charged particles to plates
            \item Remove pollutants from air
        \end{itemize}
    \end{columns}
\end{frame}

\begin{frame}{}
    \begin{figure}
        \centering
        \includegraphics[width=0.6\linewidth]{phys12-electrostatics-van-de-graaff-generator.png}
    \end{figure}
\end{frame}

\begin{frame}
    \frametitle{You Do: Coulomb's Law Challenge}

    \begin{exampleblock}{Problem to Solve}
        Two point charges are brought closer together, increasing the force between them by a factor of 25. By what factor was their separation decreased?
    \end{exampleblock}

    \begin{itemize}
        \item Step 1: Recall Coulomb's law: $F = k\frac{|q_1 q_2|}{r^2}$
        \item Step 2: Set up ratio of forces: $\frac{F_2}{F_1} = 25$
        \item Step 3: Consider how distance affects the force
        \item Step 4: Solve for the ratio of distances
    \end{itemize}

    \begin{alertblock}{Work on this for 2 minutes}
        We'll discuss the solution afterward.
    \end{alertblock}
\end{frame}

\begin{frame}
    \frametitle{You Do: Solution}

    \begin{block}{Solution}
        From Coulomb's law:
        \begin{align}
            F_1 &= k\frac{|q_1 q_2|}{r_1^2} \quad \text{and} \quad F_2 = k\frac{|q_1 q_2|}{r_2^2}\\
            \frac{F_2}{F_1} &= \frac{r_1^2}{r_2^2} = 25\\
            \frac{r_1}{r_2} &= \sqrt{25} = 5
        \end{align}
    \end{block}

    \begin{itemize}
        \item Since $\frac{r_1}{r_2} = 5$, the separation was \highlight{decreased by a factor of 5}
        \item Remember: Force is inversely proportional to distance \highlight{squared}
        \item This is why the force increases so dramatically with small distance changes
    \end{itemize}
\end{frame}

% Summary slide
\begin{frame}
    \frametitle{Summary: Key Concepts}

    \begin{columns}[t]
        \column{0.5\textwidth}
        \textbf{Electric Charge:}
        \begin{itemize}
            \item Two types: positive and negative
            \item Like charges repel; unlike attract
            \item Conserved in isolated systems
        \end{itemize}

        \textbf{Coulomb's Law:}
        \begin{itemize}
            \item $F = k\frac{|q_1 q_2|}{r^2}$
            \item Inverse-square relationship
        \end{itemize}

        \column{0.5\textwidth}
        \textbf{Electric Field:}
        \begin{itemize}
            \item $E = \frac{F}{q}$ (force per unit charge)
            \item $E = k\frac{|Q|}{r^2}$ for point charge
            \item Field lines visualize direction and strength
        \end{itemize}

        \textbf{Conductors:}
        \begin{itemize}
            \item Excess charge on surface
            \item Zero field inside at equilibrium
            \item Charge concentrates at sharp points
        \end{itemize}
    \end{columns}


\end{frame}

% End slide
\begin{frame}
    \frametitle{Questions?}

    \begin{center}
        \Large{\highlight{Thank you for your attention!}}


    \end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch05_slides_forces.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../latex-beamer/shared/templates/ds9_theme}

% Title page configuration
\title[Friction, Drag, and Elasticity]{PHYS12 CH: 5.1, 5.2, and 5.3}
\subtitle{Further Applications of Newton's Laws}
\author[Mr. Gullo]{Mr. Gullo}
\date[Fall 2025]{September 17, 2025}

\begin{document}
\frame{\titlepage}

\begin{frame}
\frametitle{Learning Objectives}
\begin{itemize}
    \item By the end of this lesson, you will be able to: \pause
    \item \textbf{Friction (5.1)}
    \begin{itemize}
        \item Discuss the general characteristics of friction. \pause
        \item Describe static vs. kinetic friction. \pause
        \item Calculate the magnitude of static and kinetic friction.
    \end{itemize} \pause
    \item \textbf{Drag Forces (5.2)}
    \begin{itemize}
        \item Express the drag force mathematically. \pause
        \item Define and determine terminal velocity.
    \end{itemize} \pause
    \item \textbf{Elasticity (5.3)}
    \begin{itemize}
        \item State Hooke's law and explain it using stress and strain. \pause
        \item Describe Young's modulus, shear modulus, and bulk modulus. \pause
        \item Determine the change in length of an object under tension or compression.
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Building on Physics 11}
\begin{block}{Review from Physics 11}
\begin{itemize}
    \item The model for static friction ($f_s \leq \mu_s N$) and kinetic friction ($f_k = \mu_k N$). \pause
    \item Applying friction forces to problems, especially on inclined planes. \pause
    \item Hooke's Law ($F = kx$) for ideal springs.
\end{itemize}
\end{block} \pause

\begin{block}{New Concepts in Physics 12}
\begin{itemize}
    \item \textbf{Drag Forces}: Introducing forces that depend on velocity ($F_D \propto v^2$). \pause
    \item \textbf{Elasticity}: A deeper look at material properties using Stress and Strain. \pause
    \item \textbf{Terminal Velocity}: The concept of a maximum speed in freefall when drag balances gravity.
\end{itemize}
\end{block}
\end{frame}

\section{5.1 Friction}

\begin{frame}
\frametitle{Key Concepts: Friction}
\begin{itemize}
    \item Friction is a force that opposes relative motion or attempted motion between surfaces in contact. \pause
    \item It acts parallel to the surface. \pause
    \item There are two main types:
    \begin{description}
        \item[Static Friction ($f_s$)] Acts on stationary objects. It is a \alert{responsive force} that matches the applied force up to a maximum value. \pause
        \item[Kinetic Friction ($f_k$)] Acts on moving objects. It is generally a constant value for a given speed and is \alert{less than} the maximum static friction.
    \end{description}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Essential Equations: Friction}
\begin{alertblock}{Static Friction}
The magnitude of static friction $f_s$ can have any value up to a maximum:
\[ f_s \leq \mu_s N \]
where $\mu_s$ is the coefficient of static friction and $N$ is the normal force. Motion begins when the applied force exceeds $f_{s(\text{max})} = \mu_s N$.
\end{alertblock} \pause

\begin{exampleblock}{Kinetic Friction}
Once an object is moving, the friction force is kinetic friction:
\[ f_k = \mu_k N \]
where $\mu_k$ is the coefficient of kinetic friction. Typically, $\mu_k < \mu_s$.
\end{exampleblock}
\end{frame}

\begin{frame}
\frametitle{The Static-Kinetic Friction Threshold}
\begin{center}
\includegraphics[width=0.6\textwidth]{../images/thresholdstatic-kinetic-friction.png}
\end{center}
\begin{block}{The Activation Energy Threshold}
This graph illustrates the critical transition point where static friction (higher resistance) gives way to kinetic friction (lower resistance). The ``drop'' represents the activation energy needed to overcome the initial barrier -- once this threshold is crossed, motion becomes sustained with less effort.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Video Activity: The 5-Second Rule}
\begin{alertblock}{Motivational Video Prompt}
Watch \textbf{How to Stop Screwing Yourself Over} by Mel Robbins (TEDxSF)
\begin{itemize}
    \item \textbf{Time segment}: 9:00 - 13:30
    \item Focus on: The science behind activation energy and taking action
    \item Connect to: How this relates to overcoming static friction in physics
\end{itemize}
\end{alertblock}

\begin{exampleblock}{The 5-Second Rule}
\textbf{If you have an impulse to act on a goal, you must physically move within 5 seconds or your brain will kill the idea.} This countdown creates the activation energy needed to overcome static friction and get started.
\end{exampleblock}

\end{frame}

\begin{frame}
\frametitle{Life Lesson: The Threshold of Getting Started}
\begin{alertblock}{The Physics of Procrastination}
The relationship $\mu_k < \mu_s$ teaches us a profound lesson about human behavior:
\begin{itemize}
    \item \textbf{Static friction ($\mu_s$)}: The resistance to starting something new
    \begin{itemize}
        \item Starting a new project, habit, or exercise routine
        \item The initial effort feels much harder than maintaining momentum
        \item This is why "getting started" is often the hardest part
    \end{itemize} \pause
    \item \textbf{Kinetic friction ($\mu_k$)}: The resistance once you're already moving
    \begin{itemize}
        \item Continuing an established habit or routine
        \item Much easier to maintain once you've overcome the initial threshold
        \item Momentum becomes your ally
    \end{itemize}
\end{itemize}
\end{alertblock} \pause

\begin{exampleblock}{Application to Life}
Just like objects in motion tend to stay in motion, people in motion tend to stay in motion. The key is applying enough initial force to overcome static friction -- then let momentum carry you forward!
\end{exampleblock}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization Context: Microscopic Friction}
\begin{itemize}
    \item Why does friction exist? \pause
    \item Even surfaces that look smooth to the naked eye are very rough on a microscopic or atomic level. \pause
    \item Friction arises from two main effects:
    \begin{enumerate}
        \item The interlocking of these microscopic hills and valleys. \pause
        \item Adhesive forces between the molecules of the two surfaces.
    \end{enumerate} \pause
    \item The next slide shows a visual representation of this idea.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Microscopic Friction}
\begin{alertblock}{[Diagram based on Figure 5.2]}
A magnified view of two surfaces in contact.
\begin{itemize}
    \item The surfaces are shown with rough, jagged profiles, even if they seem smooth macroscopically.
    \item The actual points of contact are only at the tips of the highest "peaks".
    \item When a horizontal force is applied, these peaks must either be broken off or lifted over each other for motion to occur.
    \item A larger normal force ($N$) pushes the surfaces together, increasing the contact area and the force required to move them.
\end{itemize}
\end{alertblock}
\end{frame}

\section{5.2 Drag Forces}

\begin{frame}
\frametitle{Key Concepts: Drag Force}
\begin{itemize}
    \item The drag force ($F_D$) is a resistive force that acts on an object moving through a fluid (like air or water). \pause
    \item It always opposes the direction of the object's velocity. \pause
    \item For most large objects at moderate to high speeds, the drag force is proportional to the square of the velocity ($F_D \propto v^2$). \pause
    \item This means drag increases significantly as an object speeds up.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Key Concepts: Terminal Velocity}
\begin{itemize}
    \item Consider an object falling from rest (e.g., a skydiver). \pause
    \item Initially, its velocity is zero, so the drag force is zero. The only force is gravity ($F_g = mg$), and it accelerates downwards at $g$. \pause
    \item As velocity increases, the drag force ($F_D$) increases. The net downward force ($F_{net} = mg - F_D$) decreases, so acceleration decreases. \pause
    \item Eventually, the object is moving so fast that the upward drag force becomes equal in magnitude to the downward force of gravity.
    \[ F_D = mg \] \pause
    \item At this point, $F_{net} = 0$, so acceleration is zero. The object stops accelerating and falls at a constant velocity called \alert{terminal velocity ($v_t$)}.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Essential Equations: Drag Force}
\begin{alertblock}{Drag Force Equation}
For many objects (cars, baseballs, skydivers), the drag force is given by:
\[ F_D = \frac{1}{2} C \rho A v^2 \]
\begin{itemize}
    \item $C$: Drag coefficient (a dimensionless number based on shape)
    \item $\rho$: Density of the fluid (e.g., air $\approx 1.21$ kg/m$^3$)
    \item $A$: Cross-sectional area of the object facing the fluid
    \item $v$: Speed of the object
\end{itemize}
\end{alertblock} \pause
\begin{exampleblock}{Terminal Velocity Equation}
By setting $F_D = mg$ and solving for $v$, we get terminal velocity:
\[ v_t = \sqrt{\frac{2mg}{C \rho A}} \]
\end{exampleblock}
\end{frame}

\section{5.3 Elasticity}

\begin{frame}
\frametitle{Key Concepts: Stress and Strain}
When a force is applied to a solid object, it can deform (change its shape). \pause
\begin{description}
    \item[Stress] A measure of the applied force per unit area. It quantifies the internal forces within the object.
    \[ \text{Stress} = \frac{F}{A} \quad (\text{Units: N/m}^2 \text{ or Pascals}) \] \pause
    \item[Strain] A measure of the degree of deformation. It is the fractional change in the object's length.
    \[ \text{Strain} = \frac{\Delta L}{L_0} \quad (\text{Unitless}) \] \pause
\end{description}
For small deformations, most materials obey \textbf{Hooke's Law}: Stress is proportional to Strain.
\end{frame}

\begin{frame}
\frametitle{Essential Equations: Elasticity}
\begin{alertblock}{Hooke's Law}
For a spring-like object, the force is proportional to the deformation:
\[ F = k \Delta L \]
where $k$ is the spring constant.
\end{alertblock} \pause

\begin{exampleblock}{Young's Modulus (Y)}
A material property that measures stiffness in response to tension or compression. It is the ratio of stress to strain.
\[ Y = \frac{\text{Stress}}{\text{Strain}} = \frac{F/A}{\Delta L/L_0} \] \pause
This can be rearranged to find the change in length:
\[ \Delta L = \frac{1}{Y} \frac{F}{A} L_0 \]
\end{exampleblock}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization Context: Stress-Strain Curve}
\begin{itemize}
    \item We can plot stress vs. strain to understand a material's behavior. \pause
    \item In the \alert{elastic region}, the material follows Hooke's Law (linear graph) and returns to its original shape when the stress is removed. \pause
    \item If the stress is too large, the material enters the \alert{plastic region}, where it deforms permanently. \pause
    \item At the \alert{fracture point}, the material breaks. \pause
    \item The next slide visualizes this relationship.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Concept Visualization: Stress-Strain Curve}
\begin{alertblock}{[Graph based on Figure 5.11: Deformation vs. Applied Force]}
A graph with Deformation ($\Delta L$) on the y-axis and Applied Force ($F$) on the x-axis.
\begin{itemize}
    \item \textbf{Linear Region}: The graph starts as a straight line from the origin. In this region, Hooke's law is obeyed. The material is elastic. \pause
    \item \textbf{Permanent Deformation}: The graph starts to curve. If the force is removed in this region, the object will not return to its original length. \pause
    \item \textbf{Fracture Point}: The graph ends abruptly where the material breaks.
\end{itemize}
\end{alertblock}
\end{frame}

\section{I do, We do, You do}

\begin{frame}
\frametitle{"I Do": Skiing Exercise (Friction)}
\begin{block}{Problem (Example 5.1)}
A skier with a mass of 62 kg is sliding down a snowy slope angled at $25^\circ$. The force of kinetic friction resisting their motion is known to be 45.0 N.
\newline\newline
Find the coefficient of kinetic friction, $\mu_k$, between the skis and the snow.
\end{block}
\begin{center}
\alert{[Free-body diagram of skier on an incline]}
\end{center}
\end{frame}

\begin{frame}
\frametitle{"I Do": Skiing Exercise - G \& U}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{G - Givens}
\begin{itemize}
    \item Mass, $m = 62$ kg
    \item Angle, $\theta = 25^\circ$
    \item Kinetic friction force, $f_k = 45.0$ N
    \item Acceleration due to gravity, $g = 9.80$ m/s$^2$
\end{itemize}

\column{0.48\textwidth}
\textbf{U - Unknown}
\begin{itemize}
    \item Coefficient of kinetic friction, $\mu_k = ?$
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{"I Do": Skiing Exercise - E}
\textbf{E - Equation}
\begin{itemize}
    \item Start with the definition of kinetic friction: $f_k = \mu_k N$. \pause
    \item The normal force $N$ on an incline balances the perpendicular component of weight: $N = w_{\perp} = mg \cos\theta$. \pause
    \item Substitute for $N$: $f_k = \mu_k (mg \cos\theta)$. \pause
    \item \textbf{Rearrange} for the unknown, $\mu_k$:
    \[ \mu_k = \frac{f_k}{mg \cos\theta} \]
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{"I Do": Skiing Exercise - S \& S}
\textbf{S - Substitute}
\begin{itemize}
    \item Plug in the known values with their units:
    \[ \mu_k = \frac{45.0 \text{ N}}{(62 \text{ kg})(9.80 \text{ m/s}^2) \cos(25^\circ)} \]
\end{itemize} \pause
\textbf{S - Solve}
\begin{itemize}
    \item Calculate the denominator: $(62)(9.80)(0.9063) \approx 550.5$ N.
    \item $\mu_k = \frac{45.0}{550.5} \approx 0.08174$
    \item Apply significant figures (3 sig figs from 45.0 N and 62 kg):
    \item \boxed{\mu_k = 0.082}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{"We Do": Terminal Velocity (Drag)}
\begin{block}{Problem (Example 5.2)}
Find the terminal velocity of an 85-kg skydiver falling in a spread-eagle position.
\newline\newline
Estimate the frontal area as $A = 0.70 \text{ m}^2$, the drag coefficient as $C=1.0$, and use the density of air $\rho=1.21 \text{ kg/m}^3$.
\end{block}
\end{frame}

\begin{frame}
\frametitle{"We Do": Terminal Velocity - G \& U}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{G - Givens}
\begin{itemize}
    \item $m = 85$ kg
    \item $A = 0.70 \text{ m}^2$
    \item $C = 1.0$
    \item $\rho = 1.21 \text{ kg/m}^3$
    \item $g = 9.80$ m/s$^2$
\end{itemize}

\column{0.48\textwidth}
\textbf{U - Unknown}
\begin{itemize}
    \item Terminal velocity, $v_t = ?$
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{"We Do": Terminal Velocity - E}
\textbf{E - Equation}
\begin{itemize}
    \item What is our starting equation for terminal velocity? \pause
    \[ v_t = \sqrt{\frac{2mg}{C \rho A}} \] \pause
    \item Is any algebraic rearrangement needed? (No) \pause
    \item Now, let's get ready to substitute our values.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{"We Do": Terminal Velocity - S \& S}
\textbf{S - Substitute}
\begin{itemize}
    \item Let's plug in the numbers together:
    \[ v_t = \sqrt{\frac{2(85 \text{ kg})(9.80 \text{ m/s}^2)}{(1.0)(1.21 \text{ kg/m}^3)(0.70 \text{ m}^2)}} \]
\end{itemize} \pause
\textbf{S - Solve}
\begin{itemize}
    \item Calculate the value inside the square root. What do you get?
    \item Numerator: $2 \times 85 \times 9.80 = 1666$
    \item Denominator: $1.0 \times 1.21 \times 0.70 \approx 0.847$ \pause
    \item $v_t = \sqrt{\frac{1666}{0.847}} = \sqrt{1967} \approx 44.35$ m/s
    \item \boxed{v_t \approx 44 \text{ m/s}}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{"You Do": Bone Compression (Elasticity)}
\begin{block}{Problem (Example 5.4)}
Calculate the change in length of the upper leg bone (femur) when a 70.0 kg man supports 62.0 kg of his mass on it.
\newline
\begin{itemize}
    \item \textbf{Givens}:
    \item Mass supported, $m = 62.0$ kg
    \item Original length, $L_0 = 40.0$ cm $= 0.400$ m
    \item Radius, $r = 2.00$ cm $= 0.0200$ m
    \item Young's modulus (bone compression), $Y = 9 \times 10^9$ N/m$^2$
\end{itemize}
\vspace{0.3cm}
Use the GUESS method to find the amount the bone shortens, $\Delta L$.
\end{block}
\end{frame}

\begin{frame}
\frametitle{Reading Homework}
\begin{itemize}
    \item Please ensure you read through Sections 5.1, 5.2, and 5.3 in your textbook. \pause
    \item Pay special attention to:
    \begin{itemize}
        \item The table of coefficients of friction (Table 5.1).
        \item The table of drag coefficients for various shapes (Table 5.2).
        \item Stokes' Law for drag at very low speeds.
        \item Shear Modulus and Bulk Modulus concepts.
    \end{itemize} \pause
    \item The concepts discussed in these sections are important for a full understanding and may appear on assessments.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Summary}
\begin{itemize}
    \item \textbf{Friction} is a contact force that opposes motion. We distinguish between static ($f_s \le \mu_s N$) and kinetic ($f_k = \mu_k N$) friction. \pause
    \item \textbf{Drag} is a resistive force from a fluid that depends on velocity ($F_D \propto v^2$). This leads to a \textbf{Terminal Velocity} when the drag force balances gravity. \pause
    \item \textbf{Elasticity} describes how objects deform. \textbf{Stress} ($F/A$) is the applied force per area, and \textbf{Strain} ($\Delta L/L_0$) is the resulting fractional deformation. These are related by a material's \textbf{Young's Modulus}, $Y$. \pause
    \item These concepts provide more realistic models for applying Newton's Laws to complex, everyday situations.
\end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch19_slides_electric-potential.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title information
\title[Electric Potential \& Capacitors]{PHYS12 CH19: Electric Potential and Electric Field}
\subtitle{Electric Potential, Fields, and Capacitors}
\author[Mr. Gullo]{Mr. Gullo}
\date[Feb 2025]{February, 2025}
\institute{Physics Department}

\begin{document}

% Title slide
\begin{frame}
    \titlepage
\end{frame}

% Outline slide
\begin{frame}
    \frametitle{Outline}
    \tableofcontents
\end{frame}

\section{Introduction}

\begin{frame}
    \frametitle{Learning Objectives}
    By the end of this presentation, you will be able to:
    \begin{itemize}
        \item Define electric potential and explain how it relates to potential energy
        \item Calculate potential difference between points in an electric field
        \item Relate electric field strength to potential gradient
        \item Calculate the electric potential due to a point charge
        \item Understand the concept of equipotential lines
        \item Explain how capacitors work and calculate capacitance
        \item Determine the equivalent capacitance of series and parallel combinations
        \item Calculate the energy stored in a capacitor
    \end{itemize}
\end{frame}

\section{Electric Potential Energy and Potential Difference}

\begin{frame}
    \frametitle{Electric Potential Energy vs. Electric Potential}

    \begin{block}{Electric Potential Energy}
        \begin{itemize}
            \item Energy possessed by a charge in an electric field
            \item Depends on both the field and the amount of charge
            \item Measured in joules (J)
        \end{itemize}
    \end{block}

    \begin{block}{Electric Potential}
        \begin{itemize}
            \item Electric potential energy per unit charge
            \item Independent of the test charge being used
            \item Measured in volts (V), where 1 V = 1 J/C
            \item A property of the electric field at a point
        \end{itemize}
    \end{block}


\end{frame}

\begin{frame}
    \frametitle{Potential Difference and Voltage}

    \begin{block}{Potential Difference}
        \begin{itemize}
            \item The change in potential energy per unit charge when moving from point A to point B
            \item Commonly called voltage
        \end{itemize}
    \end{block}

    \begin{align}
        \Delta V &= \frac{\Delta PE}{q} \\
        \Delta PE &= q \Delta V
    \end{align}

    \begin{itemize}
        \item Work must be done to move a positive charge from a low potential to a high potential
        \item A positive charge naturally moves from high potential to low potential (releasing energy)
        \item A negative charge naturally moves from low potential to high potential
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{The Electron Volt}

    \begin{block}{Definition}
        The electron volt (eV) is the energy given to a fundamental charge accelerated through a potential difference of 1 V.
    \end{block}

    \begin{align}
        1 \text{ eV} &= (1.60 \times 10^{-19} \text{ C})(1 \text{ V}) \\
        &= (1.60 \times 10^{-19} \text{ C})(1 \text{ J/C}) \\
        &= 1.60 \times 10^{-19} \text{ J}
    \end{align}

    \begin{itemize}
        \item Useful unit for atomic and nuclear physics
        \item Common multiples: keV, MeV, GeV
        \item Example: A 12 V battery can give an electron 12 eV of energy
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{Conservation of Energy in Electric Fields}

    \begin{block}{Mechanical Energy}
        \begin{itemize}
            \item The sum of kinetic energy and potential energy of a system
            \item $E_{mechanical} = \text{KE} + \text{PE}$
            \item This sum is constant in a conservative field
        \end{itemize}
    \end{block}

    \begin{block}{Applications}
        \begin{itemize}
            \item When a charge moves in an electric field, energy is converted between kinetic and potential forms
            \item $\Delta \text{KE} = -\Delta \text{PE} = -q\Delta V$
            \item Can find the final speed of a charged particle accelerated through a potential difference
        \end{itemize}
    \end{block}
\end{frame}

\section{Electric Potential in a Uniform Field}

\begin{frame}
    \frametitle{Electric Potential in a Uniform Field}

    In a uniform electric field (like between parallel plates):
    \begin{align}
        V_{AB} &= Ed \\
        E &= \frac{V_{AB}}{d}
    \end{align}
    where:
    \begin{itemize}
        \item $E$ is the electric field strength (V/m or N/C)
        \item $d$ is the distance from A to B (m)
        \item $V_{AB}$ is the potential difference (V)
    \end{itemize}
    \end{frame}

\begin{frame}
    \begin{figure}
        \centering
        \includegraphics[width=0.4\linewidth]{phys12-electrostatics-parallel-plates-electric-field.png}
        \caption{Fig 19.5}
    \end{figure}
\end{frame}

\begin{frame}
    \frametitle{Relationship Between Electric Field and Potential}

    \begin{block}{General Relationship}
        \begin{align}
            E &= -\frac{\Delta V}{\Delta s}
        \end{align}
        where $\Delta s$ is the distance over which the change in potential $\Delta V$ takes place
    \end{block}

    \begin{itemize}
        \item The negative sign indicates that E points in the direction of decreasing potential
        \item Electric field is the gradient (slope) of the electric potential
        \item Units check: $\text{V/m} = \text{N/C}$
        \item Stronger electric fields create steeper potential gradients
    \end{itemize}
\end{frame}

\section{Electric Potential Due to a Point Charge}

\begin{frame}
    \frametitle{Electric Potential Due to a Point Charge}

    \begin{block}{Point Charge Potential}
        The electric potential at a distance $r$ from a point charge $Q$ is:
        \begin{align}
            V = k\frac{Q}{r}
        \end{align}
        where $k = 9.0 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2$
    \end{block}

    \begin{itemize}
        \item Potential is positive for positive charges and negative for negative charges
        \item Decreases with distance $r$ from the charge
        \item Reference: $V = 0$ at $r = \infty$
        \item Note: $E = k\frac{Q}{r^2}$, so $E = -\frac{dV}{dr}$
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{Superposition of Potentials}

    \begin{block}{Key Concept}
        Electric potential is a scalar quantity, so potentials from multiple charges add algebraically:
        \begin{align}
            V_{total} = V_1 + V_2 + V_3 + \cdots = \sum_i V_i = k\sum_i \frac{Q_i}{r_i}
        \end{align}
    \end{block}

    \begin{itemize}
        \item This is simpler than adding electric fields (which are vectors)
        \item Makes it easier to solve some complex electrostatic problems
        \item Calculate the total potential, then find the electric field by taking the gradient
    \end{itemize}
\end{frame}

\section{Equipotential Lines}

\begin{frame}
    \frametitle{Equipotential Lines and Surfaces}

    \begin{block}{Definition}
        An equipotential line is a line along which the electric potential is constant.
    \end{block}

    \begin{itemize}
        \item An equipotential surface is the 3D version of equipotential lines
        \item No work is done moving a charge along an equipotential
        \item Equipotential lines are always perpendicular to electric field lines
        \item For a point charge, equipotentials are concentric spheres
        \item For a uniform field, equipotentials are parallel planes
    \end{itemize}
\end{frame}

\begin{frame}{}


\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys12-electrostatics-equipotential-lines.png}
\end{figure}
\end{frame}

\begin{frame}
    \frametitle{Equipotential Lines and Grounding}

    \begin{block}{Properties of Equipotentials}
        \begin{itemize}
            \item All points on a conductor in electrostatic equilibrium are at the same potential
            \item The surface of a conductor is an equipotential surface
            \item No electric field exists inside a conductor in electrostatic equilibrium
        \end{itemize}
    \end{block}


    \begin{block}{Grounding}
        \begin{itemize}
            \item Grounding is the process of connecting a conductor to the Earth with a good conductor
            \item This fixes the conductor at zero volts (Earth's reference potential)
            \item Important for safety in electrical systems
        \end{itemize}
    \end{block}
\end{frame}

\section{Capacitors and Dielectrics}

\begin{frame}
    \frametitle{What is a Capacitor?}

    \begin{block}{Definition}
        A capacitor is a device used to store electric charge and energy in an electric field.
    \end{block}

    \begin{itemize}
        \item Typically consists of two conductors (plates) separated by an insulator (dielectric)
        \item When connected to a voltage source, equal and opposite charges appear on the conductors
        \item The electric field is confined mostly to the region between the conductors
        \item Common forms: parallel plate, cylindrical, spherical
    \end{itemize}
    \end{frame}

\begin{frame}{Capacitors}
    \begin{figure}
        \centering
        \includegraphics[width=1\linewidth]{phys12-circuits-capacitor-types.png}
    \end{figure}
\end{frame}

\begin{frame}
   \begin{figure}
       \centering
       \includegraphics[width=0.3\linewidth]{phys12-circuits-capacitor-symbol.png}
       \caption{fig 19.13}
   \end{figure}
\end{frame}

\begin{frame}
    \frametitle{Capacitance}

    \begin{block}{Capacitance Definition}
        Capacitance (C) is the amount of charge stored per volt of potential difference:
        \begin{align}
            C = \frac{Q}{V}
        \end{align}
    \end{block}

    \begin{itemize}
        \item Unit: Farad (F), where 1 F = 1 C/V
        \item Typical values: pF to μF range
        \item Depends only on physical characteristics (geometry, materials)
        \item Does NOT depend on charge or voltage (for linear capacitors)
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{Parallel Plate Capacitor}

    \begin{block}{Capacitance Formula}
        The capacitance of a parallel plate capacitor in a vacuum or air:
        \begin{align}
            C = \epsilon_0 \frac{A}{d}
        \end{align}
        where:
        \begin{itemize}
            \item $\epsilon_0 = 8.85 \times 10^{-12}$ F/m (permittivity of free space)
            \item $A$ = area of plates
            \item $d$ = separation distance between plates
        \end{itemize}
    \end{block}

    \begin{itemize}
        \item Larger plate area → greater capacitance
        \item Smaller separation → greater capacitance
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{Dielectrics in Capacitors}

    \begin{block}{Effect of Dielectrics}
        Inserting a dielectric material between capacitor plates:
        \begin{align}
            C = \kappa\epsilon_0 \frac{A}{d}
        \end{align}
        where $\kappa$ is the dielectric constant of the material
    \end{block}

    \begin{block}{Common Dielectric Constants}
        \begin{itemize}
            \item Air: $\kappa \approx 1.00059$
            \item Paper: $\kappa \approx 2-4$
            \item Glass: $\kappa \approx 4-10$
            \item Teflon: $\kappa \approx 2.1$
            \item Water: $\kappa \approx 80$
        \end{itemize}
    \end{block}


\end{frame}

\section{Capacitors in Series and Parallel}

\begin{frame}
    \frametitle{Capacitors in Series}

    \begin{block}{Series Combination}
        When capacitors are connected in series:
        \begin{align}
            \frac{1}{C_S} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \cdots
        \end{align}
    \end{block}

    \begin{itemize}
        \item All capacitors in series have the same charge magnitude
        \item The total voltage is divided among the capacitors
        \item Equivalent capacitance is less than any individual capacitance
        \item Similar to resistors in parallel
    \end{itemize}

    \begin{center}
        \begin{figure}
            \centering
            \includegraphics[width=0.3\linewidth]{phys12-circuits-capacitor-in-series.png}
        \end{figure}
    \end{center}
\end{frame}

\begin{frame}
    \frametitle{Capacitors in Parallel}

    \begin{block}{Parallel Combination}
        When capacitors are connected in parallel:
        \begin{align}
            C_P = C_1 + C_2 + C_3 + \cdots
        \end{align}
    \end{block}

    \begin{itemize}
        \item All capacitors in parallel have the same voltage
        \item The total charge is divided among the capacitors
        \item Equivalent capacitance is greater than any individual capacitance
        \item Similar to resistors in series
    \end{itemize}

    \begin{center}

      \begin{figure}
          \centering
          \includegraphics[width=0.5\linewidth]{phys12-circuits-capacitors-in-parallel.png}
      \end{figure}
    \end{center}
\end{frame}

\begin{frame}
    \frametitle{Combined Series-Parallel Networks}

    \begin{block}{Strategy for Solving Combined Networks}
        \begin{enumerate}
            \item Identify series and parallel parts in the circuit
            \item Compute the equivalent capacitance for each part
            \item Combine the results to find the total capacitance
        \end{enumerate}
    \end{block}

    \begin{center}
 \begin{figure}
        \centering
        \includegraphics[width=0.3\linewidth]{phys12-circuits-series-parallel-capacitor-combo.png}
    \end{figure}


    \end{center}
\end{frame}

\section{Energy Stored in Capacitors}

\begin{frame}
    \frametitle{Energy Storage in Capacitors}

    \begin{block}{Energy Formula}
        The energy stored in a capacitor can be expressed in three equivalent ways:
        \begin{align}
            E_{cap} &= \frac{QV}{2} \\
            E_{cap} &= \frac{CV^2}{2} \\
            E_{cap} &= \frac{Q^2}{2C}
        \end{align}
    \end{block}

    \begin{itemize}
        \item Energy is stored in the electric field between the plates
        \item Units: joules (J)
        \item Work must be done to charge a capacitor
        \item The stored energy can be recovered when the capacitor discharges
    \end{itemize}
\end{frame}

\begin{frame}
    \frametitle{Applications of Capacitors}

    \begin{block}{Common Applications}
        \begin{itemize}
            \item Energy storage (backup power supplies)
            \item Filtering in power supplies
            \item Timing circuits
            \item Coupling and decoupling in electronic circuits
            \item Flash lamps in cameras
            \item Defibrillators in medical equipment
            \item Touch screens and sensors
        \end{itemize}
    \end{block}

    \begin{block}{Energy Density}
        The energy density in a capacitor's electric field is:
        \begin{align}
            u = \frac{1}{2}\epsilon_0 E^2 \quad \text{(J/m³)}
        \end{align}
    \end{block}
\end{frame}

\section{Example Problems}

\begin{frame}
    \frametitle{"I Do" Example - Electron Acceleration}

    \begin{block}{Problem}
        An evacuated tube uses an accelerating voltage of 40 kV to accelerate electrons to hit a copper plate and produce X-rays. What would be the maximum speed of these electrons? (Non-relativistic calculation)
    \end{block}

    \begin{block}{Solution}
        Use energy conservation: electrical potential energy is converted to KE
        \begin{align}
            qV &= \frac{1}{2}mv^2 \\
            v &= \sqrt{\frac{2qV}{m}} \\
            v &= \sqrt{\frac{2(1.6 \times 10^{-19} \text{ C})(4.0 \times 10^4 \text{ V})}{9.11 \times 10^{-31} \text{ kg}}} \\
            v &= 1.17 \times 10^8 \text{ m/s}
        \end{align}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{"We Do" Example - Capacitor with Dielectric}

    \begin{block}{Problem}
        A parallel plate capacitor has plates of area 5.00 m² separated by 0.100 mm of Teflon (dielectric constant κ = 2.1). What is the capacitance?
    \end{block}

    \begin{block}{Solution}
        Use the formula for a parallel plate capacitor with a dielectric:
        \begin{align}
            C &= \kappa\epsilon_0 \frac{A}{d} \\
            C &= (2.1)(8.85 \times 10^{-12} \text{ F/m})\frac{5.00 \text{ m}^2}{0.100 \times 10^{-3} \text{ m}} \\
            C &= (2.1)(8.85 \times 10^{-12} \text{ F/m})(5.00 \times 10^4 \text{ m}) \\
            C &= 9.29 \times 10^{-7} \text{ F} = 0.929 \text{ μF}
        \end{align}
    \end{block}
\end{frame}

\begin{frame}
    \frametitle{"You Do" Example - Energy in a Capacitor}

    \begin{block}{Problem}
        A 180 μF capacitor is charged to 120 V.
        \begin{enumerate}
            \item How much charge is stored in the capacitor?
            \item How much energy is stored in the capacitor?
        \end{enumerate}
    \end{block}

    \begin{block}{Hints}
        \begin{itemize}
            \item Use $Q = CV$ to find the charge
            \item Use $E_{cap} = \frac{1}{2}CV^2$ to find the energy
            \item Pay attention to the units ($μF = 10^{-6} F$)
        \end{itemize}
    \end{block}

    Try solving this problem on your own!
\end{frame}

\begin{frame}
    \frametitle{Summary}

    \begin{block}{Key Concepts}
        \begin{itemize}
            \item Electric potential: $V = \frac{PE}{q}$
            \item Potential difference: $\Delta V = \frac{\Delta PE}{q}$
            \item Electric field in a uniform field: $E = \frac{V}{d}$
            \item Electric field and potential relationship: $E = -\frac{\Delta V}{\Delta s}$
            \item Point charge potential: $V = k\frac{Q}{r}$
            \item Capacitance: $C = \frac{Q}{V}$
            \item Parallel plate capacitor: $C = \kappa\epsilon_0 \frac{A}{d}$
            \item Series capacitors: $\frac{1}{C_S} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots$
            \item Parallel capacitors: $C_P = C_1 + C_2 + \cdots$
            \item Energy stored: $E_{cap} = \frac{1}{2}CV^2$
        \end{itemize}
    \end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch09_slides_equilibrium.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../shared/templates/ds9_theme}

% Title page configuration
\title[Statics and Torque]{PHYS12 CH: 9}
\subtitle{Statics and Torque}
\author{Mr. Gullo}
\date{November 2024}

\begin{document}

\frame{\titlepage}

\section{Key Concepts and Definitions}
\begin{frame}
\frametitle{Equilibrium Conditions}

\begin{block}{First Condition for Equilibrium}
\begin{itemize}
    \item Net external force must be zero ($\sum \vec{F} = \vec{0}$)
    \pause
    \item Applies to both linear and rotational motion
    \pause
    \item Required for absence of acceleration
\end{itemize}
\end{block}

\begin{figure}
    \centering
    \includegraphics[width=0.8\linewidth]{Screenshot 2024-11-04 115835.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Torque and Rotational Equilibrium}

\begin{block}{Understanding Torque}
Torque ($\tau$) is the rotational equivalent of force:
\begin{itemize}
    \item Measures effectiveness of force in changing angular velocity
    \pause
    \item Represents rotational acceleration capability
    \pause
    \item Defined as: $\tau = rF\sin\theta$
    \pause
    \item where:
    \begin{itemize}
        \item $r$ is distance from pivot to force application point
        \item $F$ is magnitude of force
        \item $\theta$ is angle between force and position vector
    \end{itemize}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Understanding the Angle $\theta$ in Torque}

\begin{block}{Definition of $\theta$}
\begin{itemize}
    \item $\theta$ is the angle between the force vector ($\vec{F}$) and the position vector ($\vec{r}$) from pivot to point of application
    \pause
    \item As illustrated in Figure 9.6 and Figure 9.7
    \pause
    \item \textbf{Tip:} Always identify the shortest rotation needed to align the force with the position vector
\end{itemize}
\end{block}

\begin{block}{Key Insight}
The torque magnitude depends on how effectively the force can produce rotation - maximum when $\theta = 90^\circ$, zero when $\theta = 0^\circ$ or $180^\circ$
\end{block}
\end{frame}

\begin{frame}
\frametitle{Figure 9.6 - Torque Angle Visualization}
\begin{figure}
    \centering
    \includegraphics[width=0.3\linewidth]{fig9.6.png}
    \caption{9.6: (d) The force produces a clockwise torque. (e) A smaller counterclockwise torque is produced by the same magnitude force acting at the same point but in a different direction. Here, $\theta$ is less than $90^{\circ}$. (f) Torque is zero here since the force just pulls on the hinges, producing no rotation. In this case, $\theta=0^{\circ}$.}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Figure 9.7 - Torque Angle Examples}
\begin{figure}
    \centering
    \includegraphics[width=0.4\linewidth]{fig9.7.png}
    \caption{9.7: The three factors $\mathbf{r}, \mathbf{F}$, and $\theta$ for pivot point A on a body are shown here- $\mathbf{r}$ is the distance from the chosen pivot point to the point where the force $\mathbf{F}$ is applied, and $\theta$ is the angle between $\mathbf{F}$ and the vector directed from the point of application to the pivot point. If the object can rotate around point A , it will rotate counterclockwise. This means that torque is counterclockwise relative to pivot $A$.}
\end{figure}
\end{frame}

\begin{frame}
\begin{block}{Second Condition for Equilibrium}
\begin{itemize}
    \item Net external torque must be zero ($\sum \vec{\tau} = \vec{0}$)
    \pause
    \item Torque ($\vec{\tau}$) = $rF \sin \theta$
    \pause
    \item Where $\vec{r}$ is position vector from pivot point, $\vec{F}$ is force vector
    \pause
    \item Perpendicular lever arm ($r_\perp$) is shortest distance from pivot to force line
\end{itemize}
\end{block}

\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{Screenshot 2024-11-04 120123.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Types of Equilibrium}
\begin{itemize}
    \item \textbf{Stable Equilibrium}
    \begin{itemize}
        \item When displaced, experiences force/torque opposing displacement
        \item System returns to original position
    \end{itemize}
    \pause
    \item \textbf{Unstable Equilibrium}
    \begin{itemize}
        \item When displaced, experiences force/torque in same direction as displacement
        \item System moves further from original position
    \end{itemize}
    \pause
    \item \textbf{Neutral Equilibrium}
    \begin{itemize}
        \item Equilibrium independent of displacement
        \item System remains in new position when displaced
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Simple Machines}
\begin{itemize}
    \item \textbf{Basic Principles}
    \begin{itemize}
        \item Devices that multiply or augment applied forces
        \pause
        \item Trade-off between force and distance
        \pause
        \item Examples: lever, nail puller, wheelbarrow, crank
    \end{itemize}
    \end{itemize}
\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{Screenshot 2024-11-04 120252.png}
\end{figure}

\end{frame}



\begin{frame}
\frametitle{Mechanical Advantage}
\begin{itemize}
    \item \textbf{Mechanical Advantage}
    \begin{itemize}
        \item Ratio of output force to input force
        \pause
        \item Key measure of machine effectiveness
    \end{itemize}
\end{itemize}
\begin{figure}[H]
    \centering
    \includegraphics[width=1\linewidth]{Screenshot 2024-11-04 120504.png}
\end{figure}

\end{frame}

\section{Problems and Solutions}

\section{9.2 THE SECOND CONDITION FOR EQUILIBRIUM}

\begin{frame}
\frametitle{Problem 2}
When tightening a bolt, you push perpendicularly on a wrench with a force of 165 N at a distance of 0.140 m from the center of the bolt.
\begin{itemize}
    \item[(a)] How much torque are you exerting in newton $\times$ meters (relative to the center of the bolt)?
    \pause
    \item[(b)] Convert this torque to foot-pounds.
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 2 - Solution}
\textbf{Solution:}
\begin{itemize}
    \item[(a)] Using the torque equation $\tau = r_\perp F$:
    \begin{itemize}
        \item $\tau = 0.140 \text{ m} \times 165 \text{ N} = 23.1 \text{ N} \cdot \text{m}$
    \end{itemize}
    \pause
    \item[(b)] Converting to foot-pounds:
    \begin{itemize}
        \item $\tau = 23.1 \text{ N}\cdot\text{m} \times \frac{0.738 \text{ ft}\cdot\text{lb}}{1 \text{ N}\cdot\text{m}} = 17.0 \text{ ft}\cdot\text{lb}$
    \end{itemize}
\end{itemize}
\end{frame}

\section{9.3 STABILITY}

\begin{frame}
\frametitle{Problem 10}
A 17.0-m-high and 11.0-m-long wall under construction and its bracing are shown in Figure 9.30. The wall is in stable equilibrium without the bracing but can pivot at its base. Calculate the force exerted by each of the 10 braces if a strong wind exerts a horizontal force of 650 N on each square meter of the wall. Assume that the net force from the wind acts at a height halfway up the wall and that all braces exert equal forces parallel to their lengths. Neglect the thickness of the wall.
\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\linewidth]{Screenshot 2024-11-04 122251.png}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{Problem Statement}
A wall under construction with bracing:
\begin{itemize}
    \item Wall dimensions:
    \begin{itemize}
        \item Height: 17.0 m
        \item Length: 11.0 m
    \end{itemize}
    \pause
    \item Wind force: 650 N per square meter
    \pause
    \item 10 braces at 35° angle
    \pause
    \item Wind acts at half height
    \pause
    \item Wall can pivot at base
    \pause
    \item All braces exert equal forces
\end{itemize}
\pause
\textbf{Goal:} Calculate force exerted by each brace
\end{frame}

\begin{frame}
\frametitle{Problem Analysis}
\begin{itemize}
    \item Key considerations:
    \begin{itemize}
        \item Take pivot point at wall base
        \pause
        \item Neglect wall thickness
        \pause
        \item Forces acting:
        \begin{itemize}
            \item $$F_{brace} \times 10$$
            \item Weight of wall (w)
            \item Normal force (N)
        \end{itemize}
    \end{itemize}
    \pause
    \item Using second condition for equilibrium:
    $$\text{net}\tau = 0 \Rightarrow \text{net}\tau_{\text{cw}} = -\text{net}\tau_{\text{ccw}}$$
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Mathematical Solution}
\begin{align*}
\text{net}\tau_{\text{cw}} &= -\text{net}\tau_{\text{ccw}}\\
(8.5\text{ m}) \times F_{\text{wind}} &= rF_b \times 10 = (8.5\text{ m})\sin 35^\circ \times F_b \times 10 \\
F_{\text{wind}} &= 10\sin 35^\circ F_b \\
F_b &= \frac{F_{\text{wind}}}{10\sin 35^\circ}
\end{align*}

Wind force calculation:
\begin{align*}
F_{\text{wind}} &= \frac{F}{A} \times A = 650\text{ N/m}^2 \times 11.0\text{ m} \times 17.0\text{ m} \\
&= 121,550\text{ N}
\end{align*}
\pause
\end{frame}

\begin{frame}
\frametitle{Final Result}
Therefore:
\begin{equation*}
F_b = \frac{121,550\text{ N}}{10 \times 0.5736} = 2.12 \times 10^4\text{ N}
\end{equation*}

\begin{itemize}
    \item Each brace must exert a force of 21.2 kN
    \pause
    \item This significant force demonstrates:
    \begin{itemize}
        \item Importance of proper bracing in construction
        \pause
        \item Impact of wind loads on tall structures
        \pause
        \item Need for careful engineering calculations
    \end{itemize}
\end{itemize}
\end{frame}



\section{9.4 APPLICATIONS OF STATICS, INCLUDING PROBLEM-SOLVING STRATEGIES}


\begin{itemize}
    \item \url{https://www.youtube.com/watch?v=pK_oW62-zrc}
    \item \url{https://www.youtube.com/shorts/CxRw2n3lD7I}
    \item \url{https://www.youtube.com/shorts/sdC36VK_tY0}
\end{itemize}

\begin{frame}
\frametitle{Problem 18}
The center of gravity of a 5.0 kg pole held by a pole vaulter is 2.00 m from the left hand, and the hands are 0.700 m apart. Calculate the force exerted by:
\begin{itemize}
    \item[(a)] his right hand
    \pause
    \item[(b)] his left hand
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\linewidth]{Screenshot 2024-11-07 130412.png}
\end{figure}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 18 - Solution}
\textbf{Solution:}
Using the center of gravity as reference:
\begin{itemize}
    \item[(a)] Taking pivot at left hand:
    \begin{itemize}
        \item net $\tau = 0$
        \pause
        \item $F_R(0.7 \text{ m}) = (5.0 \text{ kg})(9.80 \text{ m/s}^2)(2.0 \text{ m})$
        \pause
        \item $F_R = 140 \text{ N}$
    \end{itemize}
    \pause
    \item[(b)] Total weight must be supported:
    \begin{itemize}
        \item $F_L + F_R = (5.0 \text{ kg})(9.80 \text{ m/s}^2)$
        \pause
        \item $F_L = 49 \text{ N}$
    \end{itemize}
\end{itemize}
\end{frame}

\section{9.5 SIMPLE MACHINES}

\begin{frame}
\frametitle{Problem 22}
A typical car has an axle with 2.0 cm radius driving a tire with a radius of 30.0 cm. What is its mechanical advantage assuming the very simplified model in Figure 9.23(b)?
\begin{figure}[H]
    \centering
    \includegraphics[width=0.7\linewidth]{Screenshot 2024-11-04 122444.png}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{Problem 22 - Solution}
\textbf{Solution:}
Mechanical advantage = $r_2/r_1 = 30.0 \text{ cm}/2.0 \text{ cm} = 15$

Step-by-step explanation:
\begin{enumerate}
    \item Identify radii:
    \begin{itemize}
        \item Inner radius $(r_1) = 2.0 \text{ cm}$
        \item Outer radius $(r_2) = 30.0 \text{ cm}$
    \end{itemize}
    \pause
    \item Calculate mechanical advantage:
    \begin{itemize}
      \item $\text{MA}=\frac{F_{\text{o}}}{F_{\text{i}}}=\frac{l_{\text{i}}}{l_{\text{o}}}$
        \pause
        \item $\text{MA} = r_2/r_1$
        \pause
        \item $\text{MA} = 30.0/2.0 = 15$
    \end{itemize}
\end{enumerate}
\end{frame}

\section{9.6 FORCES AND TORQUES IN MUSCLES AND JOINTS}

\begin{frame}
\frametitle{Problem 26}
Verify that the force in the elbow joint in Example 9.4 is 407 N, as stated in the text.
\begin{figure}
    \centering
    \includegraphics[width=0.7\linewidth]{Screenshot 2024-11-04 122655.png}
    \caption{FIGURE 9.25 (a) The figure shows the forearm of a person holding a book. The biceps exert a force $\mathbf{F}_{\mathrm{B}}$ to support the weight of the forearm and the book. The triceps are assumed to be relaxed.}
\end{figure}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.7\linewidth]{Screenshot 2024-11-04 122703.png}
    \caption{ (b) Here, you can view an approximately equivalent mechanical system with the pivot at the elbow joint as seen in Example 9.4.}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Problem Statement}
\textbf{Problem 26:} Verify that the force in the elbow joint in Example 9.4 is 407 N.

\begin{block}{Given Values}
\begin{align*}
F_{\text{B}} &= 470 \text{ N} & r_1 &= 4.00 \text{ cm} \\
m_{\text{a}} &= 2.50 \text{ kg} & r_2 &= 16.0 \text{ cm} \\
m_{\text{b}} &= 4.00 \text{ kg} & r_3 &= 38.0 \text{ cm}
\end{align*}
\end{block}
\end{frame}


\begin{frame}
\frametitle{Detailed Derivation}

Starting from torque balance(second condition of equilibrium):
\begin{align*}
\tau_{\text{Bicep}}=\tau_{\text{arm}}+\tau_{\text{book}} \\
F_B r_1 &= w_a r_2 + w_B r_3
\end{align*}

Solving for $F_B$:
\begin{align*}
F_B &= \frac{w_a r_2 + w_B r_3}{r_1}
\end{align*}

For equilibrium of forces(first condition of equilibrium):
\begin{align*}
F_e &= w_a + w_B - F_B \\
&= w_a + w_B - \frac{w_a r_2 + w_B r_3}{r_1} \\
&= w_a\left(1 - \frac{r_2}{r_1}\right) + w_B\left(1 - \frac{r_3}{r_1}\right) \\
&= w_a\left(\frac{r_2}{r_1} - 1\right) + w_B\left(\frac{r_3}{r_1} - 1\right)
\end{align*}
\end{frame}
\begin{frame}
Multiply both sides by $r_1$:
\begin{equation*}
F_e \times r_1 = w_a\left(\frac{r_2}{r_1} - 1\right) + w_B\left(\frac{r_3}{r_1} - 1\right)
\end{equation*}
\end{frame}

\begin{frame}
\frametitle{Calculation}
Substituting the values:
\begin{align*}
F_E \times r_1 &= (2.50 \text{ kg})(9.80 \text{ m/s}^2)\left(\frac{16.0 \text{ cm}}{4.0 \text{ cm}}-1\right) \\
&+ (4.00 \text{ kg})(9.80 \text{ m/s}^2)\left(\frac{38.0 \text{ cm}}{4.00 \text{ cm}}-1\right)
\end{align*}
\pause

\begin{block}{Final Result}
Therefore:
\[F_E = 407 \text{ N}\]
This verifies the stated value in Example 9.4
\end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch23_slides_electromagnetic-waves.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[EM Induction]{PHYS12 CH: 23.1-23.7}
\subtitle{Electromagnetic Induction and Its Applications}
\author[Mr. Gullo]{Mr. Gullo}
\date[April 2025]{April, 2025}

\begin{document}

% Title page
\begin{frame}
\titlepage
\end{frame}

% Table of contents
\begin{frame}
\frametitle{Outline}
\tableofcontents
\end{frame}

\section{Learning Objectives}

\begin{frame}
\frametitle{Learning Objectives}
By the end of this presentation, you will be able to:
\begin{itemize}
    \item Define magnetic flux and explain electromagnetic induction
    \item State and apply Faraday's Law and Lenz's Law
    \item Calculate motional emf in a conductor moving through a magnetic field
    \item Explain the concepts of eddy currents and magnetic damping
    \item Describe the operation of electric generators
    \item Understand the concept of back emf in motors
    \item Analyze transformer operation and calculate voltage/current relationships
\end{itemize}
\end{frame}

\section{Magnetic Flux and Induction}

\begin{frame}
\frametitle{Magnetic Flux}
\begin{block}{Definition}
Magnetic flux ($\Phi$) is a measure of the total magnetic field passing through a given area.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{align}
\Phi &= BA\cos\theta \\
\text{where:} \\
B &= \text{magnetic field strength} \\
A &= \text{area} \\
\theta &= \text{angle with perpendicular}
\end{align}

\column{0.5\textwidth}
\begin{itemize}
\item Units: Tesla·meter² (T·m²)
\item Maximum when $\theta = 0°$ (field perpendicular to area)
\item Zero when $\theta = 90°$ (field parallel to area)
\end{itemize}
\end{columns}


\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.8\linewidth]{phys12-magnetism-magnetic-field-angle.png}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{Electromagnetic Induction}
\begin{block}{Fundamental Principle}
Any change in magnetic flux induces an electromotive force (emf).
\end{block}

\begin{itemize}
\item Discovered independently by Michael Faraday and Joseph Henry
\item The induced emf can drive current through a circuit
\item The induced current creates its own magnetic field
\item Basis for generators, transformers, and many electrical devices
\end{itemize}

\begin{alertblock}{Key Insight}
It's the \textbf{change} in magnetic flux that induces emf, not the flux itself.
\end{alertblock}

\alert{[\href{https://phet.colorado.edu/en/simulations/faraday}{PHET showing a magnet moving through a coil and the resulting induced current}]}
\end{frame}

\section{Faraday's Law and Lenz's Law}

\begin{frame}
\frametitle{Faraday's Law of Induction}
\begin{block}{Mathematical Form}
\begin{align}
\text{emf} = -N\frac{\Delta\Phi}{\Delta t}
\end{align}
\end{block}

\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
\item $N$ = number of turns in a coil
\item $\Delta\Phi$ = change in magnetic flux
\item $\Delta t$ = time interval for the change
\item The negative sign is due to Lenz's Law
\end{itemize}

\column{0.4\textwidth}
\begin{itemize}
\item Ways to change flux:
\begin{itemize}
    \item Change $B$ (field strength)
    \item Change $A$ (area)
    \item Change $\theta$ (orientation)
\end{itemize}
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys12-magnetism-magnetic-flux-through-loop.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Lenz's Law}
\begin{block}{The Minus Sign in Faraday's Law}
The induced emf creates a current that produces a magnetic field opposing the change in flux that induced it.
\end{block}

\begin{itemize}
\item Conservation of energy principle
\item If flux is increasing, induced field opposes the increase
\item If flux is decreasing, induced field opposes the decrease
\item Works against the cause of the flux change
\end{itemize}

\begin{alertblock}{Important Note}
Lenz's Law explains why work must be done against the induced magnetic force to maintain flux changes.
\end{alertblock}


\end{frame}

\section{Types of Induced EMF}

\begin{frame}
\frametitle{Motional EMF}
\begin{block}{Definition}
EMF induced by motion of a conductor through a magnetic field.
\end{block}

\begin{columns}
\column{0.5\textwidth}
For a straight conductor:
\begin{align}
\text{emf} = B\ell v
\end{align}

\begin{itemize}
\item $B$ = magnetic field strength
\item $\ell$ = length of conductor
\item $v$ = velocity of conductor
\end{itemize}

\column{0.5\textwidth}
\begin{itemize}
\item Applies when $B$, $\ell$, and $v$ are mutually perpendicular
\item Causes charge separation in the conductor
\item Creates potential difference across the conductor
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys12-magnetism-electromagnetic-field-magnitude.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Eddy Currents}
\begin{block}{Definition}
Current loops induced in moving conductors or changing magnetic fields.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
\item Occur in solid conductors moving through magnetic fields
\item Flow in closed loops within the conductor
\item Can cause significant heating (I²R losses)
\item Used in induction heating and cooking
\end{itemize}

\column{0.5\textwidth}
\begin{itemize}
\item \textbf{Magnetic Damping}:
\begin{itemize}
    \item Drag force from eddy currents
    \item Opposes the motion that created it
    \item Used in braking systems
    \item Can be reduced by slotting conductors
\end{itemize}
\end{itemize}
\end{columns}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{phys12-magnetism-eddy-currents.png}
\end{figure}

\end{frame}

\section{Devices Based on Induction}

\begin{frame}
\frametitle{Electric Generators}
\begin{block}{Working Principle}
A coil rotating in a magnetic field induces a time-varying emf.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{align}
\text{emf} &= NAB\omega\sin(\omega t) \\
\text{where:} \\
N &= \text{number of turns} \\
A &= \text{area of coil} \\
B &= \text{magnetic field strength} \\
\omega &= \text{angular velocity}
\end{align}

\column{0.5\textwidth}
\begin{itemize}
\item Peak emf: $\text{emf}_0 = NAB\omega$
\item Produces sinusoidal AC voltage
\item Converts mechanical energy to electrical energy
\item Basis for power generation worldwide
\end{itemize}
\end{columns}

\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.6\linewidth]{phys12-magnetism-electric-generator-diagram.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Back EMF in Motors}
\begin{block}{Definition}
Induced emf in a motor that opposes the applied voltage.
\end{block}

\begin{itemize}
\item Motors are generators in reverse: convert electrical to mechanical energy
\item When a motor rotates, it also acts as a generator
\item This self-generated emf opposes the applied voltage
\item Magnitude increases with motor speed
\item Limits current in a running motor
\item Back emf = 0 when motor is first starting (why starting current is high)
\end{itemize}

\begin{alertblock}{Safety Note}
The high starting current is why motors need special starters or current limiters.
\end{alertblock}

\end{frame}

\begin{frame}
\frametitle{Transformers}
\begin{block}{Basic Purpose}
Transform AC voltage from one value to another using electromagnetic induction.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\textbf{Voltage Relationship:}
\begin{align}
\frac{V_s}{V_p} = \frac{N_s}{N_p}
\end{align}

\textbf{Current Relationship:}
\begin{align}
\frac{I_s}{I_p} = \frac{N_p}{N_s}
\end{align}

\column{0.5\textwidth}
\begin{itemize}
\item Primary coil: Connected to AC source
\item Secondary coil: Delivers transformed voltage
\item $N_p, N_s$: Number of turns in primary and secondary
\item $V_p, V_s$: Primary and secondary voltages
\item $I_p, I_s$: Primary and secondary currents
\end{itemize}
\end{columns}

\begin{itemize}
\item \textbf{Step-up transformer:} $N_s > N_p$ (increases voltage, decreases current)
\item \textbf{Step-down transformer:} $N_s < N_p$ (decreases voltage, increases current)
\end{itemize}

\alert{[Cross-sectional diagram of a transformer showing primary and secondary coils]}
\end{frame}

\section{Practical Applications}

\begin{frame}
\frametitle{Example Problem: "I do"}
\begin{block}{Motional EMF Problem}
A metal rod of length 1.0 m moves at 2.0 m/s perpendicular to a magnetic field of 0.50 T. Calculate the induced emf.
\end{block}

\begin{itemize}
\item \textbf{Given:}
\begin{itemize}
    \item Length of rod: $\ell = 1.0 \text{ m}$
    \item Speed of rod: $v = 2.0 \text{ m/s}$
    \item Magnetic field: $B = 0.50 \text{ T}$
\end{itemize}
\item \textbf{Find:} The induced emf
\end{itemize}

\pause

\begin{align}
\text{emf} &= B\ell v \\
&= (0.50 \text{ T})(1.0 \text{ m})(2.0 \text{ m/s}) \\
&= 1.0 \text{ V}
\end{align}


\end{frame}

\begin{frame}
\frametitle{Example Problem: "We do"}
\begin{block}{Generator Problem}
A generator has 100 turns of wire in a coil with area 0.05 m² and rotates in a magnetic field of 0.75 T at 60 Hz. Calculate the peak emf.
\end{block}

\begin{itemize}
\item \textbf{Given:}
\begin{itemize}
    \item Number of turns: $N = 100$
    \item Area of coil: $A = 0.05 \text{ m}^2$
    \item Magnetic field: $B = 0.75 \text{ T}$
    \item Frequency: $f = 60 \text{ Hz}$
\end{itemize}
\item \textbf{Find:} The peak emf ($\text{emf}_0$)
\end{itemize}

Let's work through this together:
\begin{align}
\omega &= 2\pi f = 2\pi(60 \text{ Hz}) = 377 \text{ rad/s} \\
\text{emf}_0 &= NAB\omega \\
&= 100 \times 0.05 \text{ m}^2 \times 0.75 \text{ T} \times 377 \text{ rad/s} \\
&= ?
\end{align}
\end{frame}

\begin{frame}
\frametitle{Example Problem: "You do"}
\begin{block}{Transformer Problem}
A transformer has 400 primary turns and 100 secondary turns. If the primary voltage is 120 V, what is the secondary voltage?
\end{block}

\begin{itemize}
\item \textbf{Given:}
\begin{itemize}
    \item Primary turns: $N_p = 400$
    \item Secondary turns: $N_s = 100$
    \item Primary voltage: $V_p = 120 \text{ V}$
\end{itemize}
\item \textbf{Find:} Secondary voltage ($V_s$)
\end{itemize}

\begin{alertblock}{Hint}
Use the voltage relationship for transformers: $\frac{V_s}{V_p} = \frac{N_s}{N_p}$
\end{alertblock}

Try to solve this problem on your own!
\end{frame}

\section{Summary}

\begin{frame}
\frametitle{Key Equations}
\begin{table}
\begin{tabular}{ll}
\hline
\textbf{Concept} & \textbf{Equation} \\
\hline
Magnetic Flux & $\Phi = BA\cos\theta$ \\
Faraday's Law & $\text{emf} = -N\frac{\Delta\Phi}{\Delta t}$ \\
Motional EMF & $\text{emf} = B\ell v$ \\
Generator EMF & $\text{emf} = NAB\omega\sin(\omega t)$ \\
Peak Generator EMF & $\text{emf}_0 = NAB\omega$ \\
Transformer Voltage & $\frac{V_s}{V_p} = \frac{N_s}{N_p}$ \\
Transformer Current & $\frac{I_s}{I_p} = \frac{N_p}{N_s}$ \\
\hline
\end{tabular}
\end{table}
\end{frame}

\begin{frame}
\frametitle{Summary of Key Concepts}
\begin{itemize}
\item \textbf{Electromagnetic Induction:} Process by which changing magnetic flux induces an emf
\item \textbf{Faraday's Law:} Quantifies the relationship between changing flux and induced emf
\item \textbf{Lenz's Law:} Determines the direction of induced current to oppose the change
\item \textbf{Motional EMF:} Produced when a conductor moves through a magnetic field
\item \textbf{Eddy Currents:} Closed loops of current induced in solid conductors
\item \textbf{Generators:} Convert mechanical energy to electrical energy using induction
\item \textbf{Back EMF:} Self-induced voltage in motors that opposes applied voltage
\item \textbf{Transformers:} Convert AC voltage levels using mutual induction
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Real-World Applications}
\begin{columns}
\column{0.5\textwidth}
\begin{block}{Power Generation \& Distribution}
\begin{itemize}
\item Electric generators in power plants
\item Step-up transformers at power plants
\item Step-down transformers near consumers
\end{itemize}
\end{block}

\begin{block}{Transportation}
\begin{itemize}
\item Electric motors in vehicles
\item Magnetic braking systems
\item Induction sensors
\end{itemize}
\end{block}

\column{0.5\textwidth}
\begin{block}{Consumer Electronics}
\begin{itemize}
\item Induction cooktops
\item Wireless charging systems
\item Microphones and speakers
\end{itemize}
\end{block}

\begin{block}{Medical Technology}
\begin{itemize}
\item MRI machines
\item Electromagnetic flow meters
\item Transcranial magnetic stimulation
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{Questions?}
\begin{center}
\Large Thank you for your attention!

\vspace{1cm}

Any questions?
\end{center}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch22_slides_magnetism.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[CH22 Magnetism]{PHYS12 CH22: Magnetism}
\subtitle{Sections 22.1-22.8}
\author[Mr. Gullo]{Mr. Gullo}
\date[April 2025]{April, 2025}

\begin{document}

% Title slide
\begin{frame}
\titlepage
\end{frame}

% Learning objectives
\begin{frame}{Learning Objectives}
\begin{block}{By the end of this presentation, you should be able to:}
\begin{itemize}
\item Describe the basic properties of magnets and magnetic fields
\item Explain ferromagnetism and how electromagnets work
\item Understand magnetic field lines and their properties
\item Calculate the force on a moving charge in a magnetic field
\item Apply the right-hand rule to determine the direction of magnetic forces
\item Explain the Hall effect and its applications
\item Calculate the force on a current-carrying conductor in a magnetic field
\item Determine the torque on a current loop in a magnetic field
\end{itemize}
\end{block}
\end{frame}

% Outline slide
\begin{frame}{Outline}
\tableofcontents
\end{frame}

\section{Magnets and Magnetic Fields}

% Basic concepts of magnetism
\begin{frame}{Basic Concepts of Magnetism}
\begin{block}{Magnetism}
Properties of magnets, effect of magnetic force on moving charges and currents, and creation of magnetic fields by currents.
\end{block}

\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
\item Two types of magnetic poles:
  \begin{itemize}
  \item North magnetic pole
  \item South magnetic pole
  \end{itemize}
\item North magnetic poles are attracted toward Earth's geographic north pole
\item Like poles repel, unlike poles attract
\item Magnetic poles always occur in pairs—cannot be isolated
\end{itemize}

\column{0.4\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-magnetism-magnetic-field-generator.png}
\end{figure}
\end{columns}
\end{frame}

% Ferromagnets and Electromagnets
\begin{frame}{Ferromagnets and Electromagnets}
\begin{columns}
\column{0.5\textwidth}
\textbf{Ferromagnetic Materials}
\begin{itemize}
\item Materials exhibiting strong magnetic effects (e.g., iron)
\item Atoms act like small magnets (due to internal currents)
\item Form millimeter-sized regions called \textbf{domains}
\item Domains can align to create permanent magnets
\item Above Curie temperature, thermal agitation destroys alignment
\end{itemize}

\column{0.5\textwidth}
\textbf{Electromagnets}
\begin{itemize}
\item Use electric currents to make magnetic fields
\item Often aided by induced fields in ferromagnetic materials
\item Field strength depends on current and number of turns
\item Field can be turned on and off
\end{itemize}
\end{columns}

\end{frame}

% Magnetic field lines
\begin{frame}{Magnetic Field Lines}
\begin{block}{Magnetic Field Representation}
Magnetic fields can be pictorially represented by magnetic field lines.
\end{block}

\begin{columns}
\column{0.6\textwidth}
\textbf{Properties of magnetic field lines:}
\begin{enumerate}
\item The field is tangent to the magnetic field line
\item Field strength is proportional to line density
\item Field lines cannot cross
\item Field lines are continuous loops
\end{enumerate}

\column{0.4\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-magnetism-magnetic-force-on-wire.png}
\end{figure}
\end{columns}
\end{frame}

\section{Magnetic Forces on Charges and Currents}

% Force on moving charge
\begin{frame}{Force on Moving Charge in Magnetic Field}
\begin{block}{Magnetic Force Formula}
The magnitude of the magnetic force on a moving charge $q$ is:
\begin{equation}
F = qvB\sin\theta
\end{equation}
where $\theta$ is the angle between the directions of $\vec{v}$ and $\vec{B}$.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
\item SI unit for magnetic field $B$: tesla (T)
\item $1 \text{ T} = \frac{1 \text{ N}}{\text{A}\cdot\text{m/s}} = \frac{1 \text{ N}}{\text{A}\cdot\text{m}}$
\item Force direction given by right hand rule 1 (RHR-1)
\item Force is perpendicular to plane formed by $\vec{v}$ and $\vec{B}$
\item Force is zero if $\vec{v}$ is parallel to $\vec{B}$
\end{itemize}

\column{0.5\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys12-magnetism-magnetic-field-lines-generator.png}
\end{figure}
\end{columns}
\end{frame}


\begin{frame}{Force on Moving Charge in Magnetic Field}
    \begin{figure}
        \centering
        \includegraphics[width=0.75\linewidth]{phys12-magnetism-right-hand-rule-force.png}
    \end{figure}
\end{frame}
\begin{frame}{Force on Moving Charge in Magnetic Field}

\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-magnetism-right-hand-rule-current.png}
\end{figure}
\end{frame}

% Applications of force on moving charge
\begin{frame}{Applications of Force on Moving Charges}
\begin{block}{Circular Motion in Magnetic Field}
Magnetic force can supply centripetal force causing charged particles to move in circular paths with radius:
\begin{equation}
r = \frac{mv}{qB}
\end{equation}
where $v$ is the component of velocity perpendicular to $\vec{B}$.
\end{block}

\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
\item Basis for many applications:
  \begin{itemize}
  \item Mass spectrometers
  \item Cyclotrons
  \item Synchrotrons
  \item Particle detectors
  \end{itemize}
\item Only affects moving charges
\item Direction changes with charge polarity
\end{itemize}

\column{0.4\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-magnetism-magnetic-force-on-current-loop.png}
\end{figure}
\end{columns}
\end{frame}

% Hall Effect
\begin{frame}{The Hall Effect}
\begin{block}{Hall Effect Definition}
The creation of voltage $\varepsilon$ (Hall emf) across a current-carrying conductor by a magnetic field.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
\item Hall emf is given by:
\begin{equation}
\varepsilon = Blv
\end{equation}
\item $B$, $l$, and $v$ must be mutually perpendicular
\item For conductor of width $l$ with charges moving at speed $v$
\item Applications:
  \begin{itemize}
  \item Measuring magnetic fields
  \item Determining charge carrier type and density
  \item Hall effect sensors
  \end{itemize}
\end{itemize}

\column{0.5\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-magnetism-hall-effect.png}
\end{figure}
\end{columns}
\end{frame}

% Force on current-carrying conductor
\begin{frame}{Magnetic Force on a Current-Carrying Conductor}
\begin{block}{Force Formula}
The magnetic force on a current-carrying conductor is:
\begin{equation}
F = IlB\sin\theta
\end{equation}
where $I$ is the current, $l$ is the length of the conductor, $B$ is the magnetic field strength, and $\theta$ is the angle between $\vec{I}$ and $\vec{B}$.
\end{block}


\begin{itemize}
\item Direction follows RHR-1 with thumb in direction of $\vec{I}$
\item Maximum force when conductor is perpendicular to field
\item No force when conductor is parallel to field
\item Basis for electric motors
\end{itemize}


\end{frame}

% Torque on current loop
\begin{frame}{Torque on a Current Loop: Motors and Meters}
\begin{block}{Torque Formula}
The torque on a current-carrying loop in a uniform magnetic field is:
\begin{equation}
\tau = NIAB\sin\theta
\end{equation}
where $N$ is the number of turns, $I$ is the current, $A$ is the loop area, $B$ is the magnetic field strength, and $\theta$ is the angle between the perpendicular to the loop and the magnetic field.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
\item Maximum torque when loop is parallel to field
\item Zero torque when loop is perpendicular to field
\item Applications:
  \begin{itemize}
  \item Electric motors
  \item Galvanometers
  \item Ammeters
  \item Voltmeters
  \end{itemize}
\end{itemize}

\column{0.5\textwidth}
\begin{figure}
    \centering
    \includegraphics[width=0.9\linewidth]{phys12-magnetism-torque-on-current-loop.png}
\end{figure}
\end{columns}
\end{frame}

\section{Example Problems}

% I do example
\begin{frame}{Example 1: "I do"}
\begin{block}{Problem}
Calculate the force on an electron moving at $5.0 \times 10^6$ m/s perpendicular to a magnetic field of 0.50 T.
\end{block}
\pause
\begin{block}{Solution}
Given:
\begin{itemize}
\item Charge of electron: $q = -1.60 \times 10^{-19}$ C
\item Velocity: $v = 5.0 \times 10^6$ m/s
\item Magnetic field: $B = 0.50$ T
\item Angle: $\theta = 90°$ (perpendicular)
\end{itemize}

The negative sign indicates the force is in the direction opposite to that given by RHR-1 for a positive charge.
\end{block}
\end{frame}

\begin{frame}{Example 1: "I do"}

\begin{block}{Solution}
Given:
\begin{itemize}
\item Charge of electron: $q = -1.60 \times 10^{-19}$ C
\item Velocity: $v = 5.0 \times 10^6$ m/s
\item Magnetic field: $B = 0.50$ T
\item Angle: $\theta = 90°$ (perpendicular)
\end{itemize}

Using the formula $F = qvB\sin\theta$:

\pause

\begin{align}
F &= (-1.60 \times 10^{-19} \text{ C})(5.0 \times 10^6 \text{ m/s})(0.50 \text{ T})(\sin 90°) \\
F &= (-1.60 \times 10^{-19})(5.0 \times 10^6)(0.50)(1) \\
F &= -4.0 \times 10^{-13} \text{ N}
\end{align}

The negative sign indicates the force is in the direction opposite to that given by RHR-1 for a positive charge.
\end{block}
\end{frame}

% We do example
\begin{frame}{Example 2: "We do"}
\begin{block}{Problem}
Find the radius of the circular path of a proton with speed $3.0 \times 10^6$ m/s in a magnetic field of 0.75 T when the proton velocity is perpendicular to the field.
\end{block}
\pause

\begin{block}{Solution}
Given:
\begin{itemize}
\item Mass of proton: $m = 1.67 \times 10^{-27}$ kg
\item Charge of proton: $q = 1.60 \times 10^{-19}$ C
\item Velocity: $v = 3.0 \times 10^6$ m/s
\item Magnetic field: $B = 0.75$ T
\end{itemize}

\end{block}
\end{frame}
\begin{frame}{Example 2: "We do"}
\pause
\begin{block}{Solution}
Given:
\begin{itemize}
\item Mass of proton: $m = 1.67 \times 10^{-27}$ kg
\item Charge of proton: $q = 1.60 \times 10^{-19}$ C
\item Velocity: $v = 3.0 \times 10^6$ m/s
\item Magnetic field: $B = 0.75$ T
\end{itemize}

Using the formula $r = \frac{mv}{qB}$:

\pause

\begin{align}
r &= \frac{(1.67 \times 10^{-27} \text{ kg})(3.0 \times 10^6 \text{ m/s})}{(1.60 \times 10^{-19} \text{ C})(0.75 \text{ T})} \\
r &= \frac{5.01 \times 10^{-21}}{1.20 \times 10^{-19}} \\
r &= 4.2 \times 10^{-2} \text{ m} = 4.2 \text{ cm}
\end{align}
\end{block}
\end{frame}


% You do example
\begin{frame}{Example 3: "You do"}
\begin{block}{Problem}
A straight wire carrying a 5.0 A current is placed in a uniform magnetic field of 0.25 T. If the wire is 10 cm long and makes an angle of 30° with the field, what is the magnetic force on the wire?
\end{block}
\pause
\begin{block}{Hints}
\begin{itemize}
\item Use the formula $F = IlB\sin\theta$
\item Convert all units to SI
\item Remember to calculate the sine of the angle
\end{itemize}
\end{block}
\pause
\begin{block}{Answer (to check your work)}
$F = 0.125$ N
\end{block}
\end{frame}

% Key Equations summary
\begin{frame}{Key Equations}
\begin{block}{Magnetic Forces}
\begin{align}
F &= qvB\sin\theta & \text{(Force on moving charge)} \\
r &= \frac{mv}{qB} & \text{(Radius of circular path)} \\
\varepsilon &= Blv & \text{(Hall emf)} \\
F &= IlB\sin\theta & \text{(Force on current-carrying conductor)} \\
\tau &= NIAB\sin\theta & \text{(Torque on current loop)}
\end{align}
\end{block}

\begin{block}{Right-Hand Rules}
\begin{itemize}
\item RHR-1 for force direction: thumb in direction of $\vec{v}$ (or $\vec{I}$), fingers in direction of $\vec{B}$, palm indicates force direction
\end{itemize}
\end{block}
\end{frame}

% Summary
\begin{frame}{Summary}
\begin{itemize}
\item Magnets have north and south poles; like poles repel, unlike poles attract
\item Magnetic poles always come in pairs and cannot be isolated
\item All magnetism is created by electric current
\item Ferromagnetic materials contain domains of aligned atomic magnets
\item Magnetic fields are represented by field lines with specific properties
\item Magnetic forces act on moving charges and current-carrying conductors
\item The Hall effect creates voltage across a current-carrying conductor in a magnetic field
\item Torque on current loops in magnetic fields is the basis for motors and meters
\end{itemize}

\begin{block}{Applications}
Electromagnets, electric motors, generators, particle accelerators, mass spectrometers, Hall effect sensors, magnetic resonance imaging (MRI)
\end{block}
\end{frame}

% References slide
\begin{frame}{References}
\begin{block}{Textbook}
OpenStax Physics, Chapter 22: Magnetism, Sections 22.1-22.8
\end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch04-05-09_review.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[Unit 2 Review]{PHYS12 CH459:}
\subtitle{Test Prep}
\author[Mr. Gullo]{Mr. Gullo}
\date[Nov 2024]{November 2024}

% Add logo
\logo{\includegraphics[width=0.1\linewidth]{phys12-shared-cinec-logo.png}}

% Table of contents at the beginning of each section
\AtBeginSection[]
{
  \begin{frame}
    \frametitle{Table of Contents}
    \tableofcontents[currentsection]
  \end{frame}
}


\begin{document}

\frame{\titlepage}


\section{Circus Performer Problem}

\begin{frame}
\frametitle{Problem 1: Circus Performance}
\begin{block}{Problem Statement}
During a circus act:
\begin{itemize}
    \item One performer hangs upside down from trapeze
    \item Holds another performer by the legs
    \item Upward force is three times the lower performer's weight
    \item Calculate the stretch in the upper legs (femurs)
\end{itemize}
\end{block}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{CH9.5 4,5,9 Review/Screenshot 2024-11-12 100229.png}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{Problem 1: Given Information}
\begin{itemize}
    \item Mass of performer = 60.0 kg
    \item Each femur:
    \begin{itemize}
        \item Length ($L_0$) = 35.0 cm = 0.350 m
        \item Radius = 1.80 cm = 0.0180 m
    \end{itemize}
    \item Young's modulus ($Y$) = $1.6 \times 10^{10}$ N/m²
    \item Force = 3 times weight
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 1: Solution Approach}
Key equation for elastic deformation:
$$\Delta L = \frac{1}{Y} \frac{F}{A} L_0$$
where:
\begin{itemize}
    \item $\Delta L$ = change in length
    \item $Y$ = Young's modulus
    \item $F$ = applied force
    \item $A$ = cross-sectional area
    \item $L_0$ = original length
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem 1: Calculations}
\begin{enumerate}
    \item Calculate total force:
    $$F_{\text{tot}} = 3mg = 3(60.0\text{ kg})(9.80\text{ m/s}^2) = 1764\text{ N}$$
    \item Force per leg:
    $$F_{\text{leg}} = F_{\text{tot}}/2 = 882\text{ N}$$
    \item Cross-sectional area:
    $$A = \pi r^2 = \pi(0.0180\text{ m})^2 = 1.018 \times 10^{-3}\text{ m}^2$$
\end{enumerate}
\end{frame}

\begin{frame}
\frametitle{Problem 1: Final Result}
Substituting into the equation:
$$\Delta L = \frac{1}{1.6 \times 10^{10}\text{ N/m}^2} \frac{882\text{ N}}{1.018 \times 10^{-3}\text{ m}^2}(0.350\text{ m})$$
$$\Delta L = 1.90 \times 10^{-5}\text{ m}$$
Or in centimeters:
$$\Delta L = 1.90 \times 10^{-3}\text{ cm}$$
\end{frame}

\section{Aircraft Towing Problem}

\begin{frame}
\frametitle{Problem 2: Aircraft Towing}
\begin{block}{Problem Statement}
A tractor pushes an airplane:
\begin{itemize}
    \item Tractor mass = 1800 kg
    \item Force on pavement = $1.75 \times 10^4$ N backward
    \item Total resistance = 2400 N
    \item Acceleration = 0.150 m/s²
\end{itemize}
Find: (a) airplane mass, (b) force on airplane
\end{block}
\end{frame}
\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{CH9.5 4,5,9 Review/Screenshot 2024-11-12 092937.png}
\end{figure}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{CH9.5 4,5,9 Review/Screenshot 2024-11-12 092940.png}

\end{figure}
\end{frame}

\begin{frame}
\frametitle{Problem 2: Solution Part (a)}
Using Newton's Second Law:
\begin{align*}
\text{net }F &= Ma = (m_a + m_t)a = F - f\\
m_a &= \frac{F-f}{a} - m_t\\
m_a &= \frac{1.75 \times 10^4\text{ N} - 2400\text{ N}}{0.150\text{ m/s}^2} - 1800\text{ kg}\\
m_a &= 9.89 \times 10^4\text{ kg}
\end{align*}
\end{frame}

\begin{frame}
\frametitle{Problem 2: Solution Part (b)}
Force on airplane:
\begin{align*}
\text{net }F &= F' - f' = m_aa\\
F' &= m_aa + f'\\
F' &= (9.89 \times 10^4\text{ kg})(0.150\text{ m/s}^2) + 2200\text{ N}\\
F' &= 1.70 \times 10^4\text{ N}
\end{align*}\end{frame}



\section{Car Acceleration Problem}

\begin{frame}
\frametitle{Problem 3: Car Acceleration}
\begin{block}{Problem Statement}
A car accelerates forward:
\begin{itemize}
    \item Wheels exert 2100 N backward on road
    \item Friction force = 250 N
    \item Acceleration = 1.80 m/s²
\end{itemize}
Find the mass of car plus occupants
\end{block}
\end{frame}

\begin{frame}
\frametitle{Problem 3: Solution}
Using Newton's Second Law:
\begin{align*}
\text{net }F &= F - f = ma\\
m &= \frac{F-f}{a}\\
m &= \frac{2100\text{ N} - 250\text{ N}}{1.80\text{ m/s}^2}\\
m &= 1.03 \times 10^3\text{ kg}
\end{align*}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.5\linewidth]{CH9.5 4,5,9 Review/Screenshot 2024-11-12 092952.png}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{Key Takeaways}
\begin{itemize}
    \item Elastic deformation depends on material properties and geometry
    \item Newton's laws apply to complex systems like aircraft-tractor combinations
    \item Free-body diagrams help organize force analysis
    \item Always check units and magnitudes for reasonable results
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Problem: Forces on Head at Drafting Board}
\begin{block}{Problem Statement}
A person working at a drafting board holds her head at an angle:
\begin{itemize}
    \item Three major forces act on the head:
    \begin{itemize}
        \item Weight ($w$) = 50.0 N
        \item Muscle force ($F_M$) = 60.0 N at 33°
        \item Vertebrae force ($F_V$) at unknown angle $\theta$
    \end{itemize}
    \item All forces act through center of mass
    \item Head is stationary (in equilibrium)
\end{itemize}
Find direction ($\theta$) and magnitude of vertebrae force ($F_V$).
\end{block}
\begin{figure}
    \centering
    \includegraphics[width=0.2\linewidth]{CH9.5 4,5,9 Review/Screenshot 2024-11-11 143247.png}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{Solution Approach}
\begin{itemize}
    \item Since head is stationary, sum of forces = 0
    \item Break forces into x and y components:
    \begin{align*}
    \hat{x}&: F_M \cos 33° = F_V \cos \theta\\
    \hat{y}&: w + F_M \sin 33° = F_V \sin \theta
    \end{align*}
    \item Use these equations to find $\theta$ and $F_V$
\end{itemize}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{CH9.5 4,5,9 Review/Screenshot 2024-11-12 103435.png}
\end{figure}

\end{frame}

\begin{frame}
\frametitle{Solution: Finding the Angle}
\begin{itemize}
    \item Divide y-equation by x-equation to find $\theta$:
    \[\tan \theta = \frac{w + F_M \sin 33°}{F_M \cos 33°}\]
    \item Substitute known values:
    \[\tan \theta = \frac{50.0\text{ N} + (60.0\text{ N})\sin 33°}{(60.0\text{ N})\cos 33°} = 1.643\]
    \item Solve for $\theta$:
    \[\theta = \tan^{-1}(1.643) = 58.7° \approx 59°\]
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Solution: Finding the Force Magnitude}
\begin{itemize}
    \item Use x-component equation:
    \[F_V = \frac{F_M \cos 33°}{\cos 58.7°}\]
    \item Substitute values:
    \[F_V = \frac{(60.0\text{ N})\cos 33°}{\cos 58.7°} = 97\text{ N}\]
    \item Therefore:
    \begin{itemize}
        \item Direction: $\theta = 59°$ from horizontal
        \item Magnitude: $F_V = 97$ N
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Physical Interpretation}
\begin{itemize}
    \item The vertebrae must supply a significant force (97 N) to maintain head position
    \item Force is nearly 2 times the weight of the head
    \item Angle is determined by:
    \begin{itemize}
        \item Head position (33° muscle angle)
        \item Need to balance both vertical and horizontal components
        \item Requirement that force passes through center of mass
    \end{itemize}
    \item Demonstrates why poor posture can lead to muscle strain
\end{itemize}
\end{frame}




\begin{frame}
\frametitle{Problem: Leg Exercise Device}
\begin{block}{Problem Statement}
An exercise device for the upper leg muscle:
\begin{itemize}
    \item Mass of 10.0 kg attached via pulleys
    \item System maintained at constant speed
    \item Lever arm distances:
    \begin{itemize}
        \item $r_\perp = 35.0$ cm (perpendicular distance to tension force)
        \item $r'_\perp = 2.00$ cm (perpendicular distance to muscle force)
    \end{itemize}
\end{itemize}
Calculate the force exerted by the upper leg muscle.
\end{block}
\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{CH9.5 4,5,9 Review/Screenshot 2024-11-12 134327.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Analysis Strategy}
Key physics concepts:
\begin{itemize}
    \item Constant speed implies:
    \begin{itemize}
        \item Acceleration $a = 0$
        \item Net force = 0
        \item Net torque $\tau = 0$
    \end{itemize}
    \item Torque relationship:
    \begin{itemize}
        \item $\tau = F r_\perp$ (force × perpendicular distance)
        \item Sum of torques = 0 for equilibrium
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Solution Steps}
\begin{enumerate}
    \item Calculate tension force from weight:
    \[T = w = (10.0\text{ kg})(9.80\text{ m/s}^2) = 98.0\text{ N}\]
    \item Use torque equilibrium about pivot:
    \[F_m r'_\perp - T r_\perp = 0\]
    \item Solve for muscle force:
    \[F_m = T\frac{r_\perp}{r'_\perp}\]
\end{enumerate}
\end{frame}

\begin{frame}
\frametitle{Final Calculation}
Substituting values:
\begin{align*}
F_m &= 98.0\text{ N} \times \frac{35.0\text{ cm}}{2.00\text{ cm}}\\
&= 98.0\text{ N} \times 17.5\\
&= 1715\text{ N}\\
&= 1.72 \times 10^3\text{ N}
\end{align*}
\end{frame}

\begin{frame}
\frametitle{Physical Interpretation}
\begin{itemize}
    \item The muscle must exert a force of 1715 N
    \item This large force results from mechanical disadvantage:
    \begin{itemize}
        \item Muscle attachment point (2.00 cm) much closer to pivot
        \item Than weight attachment point (35.0 cm)
        \item Creates a force multiplier of 17.5
    \end{itemize}
    \item Demonstrates why leg muscles need to be very strong
    \item Shows importance of lever arms in biomechanics
\end{itemize}
\end{frame}


\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch22_slides_magnetism-v2.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page configuration
\title[CH22 Magnetism]{PHYS12 CH22: Magnetism}
\subtitle{Sections 22.1-22.8}
\author[Mr. Gullo]{Mr. Gullo}
\date[April 2025]{April, 2025}

\begin{document}

% Title slide
\begin{frame}
\titlepage
\end{frame}

% Learning objectives
\begin{frame}{Learning Objectives}
\begin{block}{By the end of this presentation, you should be able to:}
\begin{itemize}
\item Describe magnets, magnetic fields, and magnetism
\item Understand magnetic field lines and their properties
\item Calculate the force on charges and currents in magnetic fields
\item Apply the right-hand rule for magnetic forces
\item Explain the Hall effect and practical applications
\item Calculate torque on current loops in magnetic fields
\end{itemize}
\end{block}
\end{frame}

% Outline slide
\begin{frame}{Outline}
\tableofcontents
\end{frame}

\section{Magnets and Magnetic Fields}

% Basic concepts of magnetism
\begin{frame}{Basic Concepts of Magnetism}
\begin{block}{Magnetism}
Properties of magnets and their interaction with moving charges and currents.
\end{block}

\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
\item Magnetic poles: North and South
\item Like poles repel, unlike poles attract
\item Poles always occur in pairs—cannot be isolated
\item North poles point toward Earth's geographic north
\end{itemize}

\column{0.4\textwidth}
\begin{figure}
\centering
\includegraphics[width=0.8\linewidth]{phys12-magnetism-magnetic-field-generator.png}
\end{figure}
\end{columns}
\end{frame}

% Ferromagnets and Electromagnets
\begin{frame}{Ferromagnets and Electromagnets}
\begin{columns}
\column{0.5\textwidth}
\textbf{Ferromagnetic Materials}
\begin{itemize}
\item Materials with strong magnetic effects (iron)
\item Form regions called \textbf{domains}
\item Domains align to create permanent magnets
\item Lose magnetism above Curie temperature
\end{itemize}

\column{0.5\textwidth}
\textbf{Electromagnets}
\begin{itemize}
\item Use electric currents to create magnetic fields
\item Field strength depends on current and coil turns
\item Can be turned on and off
\end{itemize}
\end{columns}
\end{frame}

% Magnetic field lines
\begin{frame}{Magnetic Field Lines}
\begin{block}{Magnetic Field Representation}
Magnetic fields are represented by field lines.
\end{block}

\begin{columns}
\column{0.6\textwidth}
\textbf{Properties of magnetic field lines:}
\begin{itemize}
\item Field is tangent to the field line
\item Line density shows field strength
\item Lines never cross
\item Lines form continuous loops
\end{itemize}

\column{0.4\textwidth}
\begin{figure}
\centering
\includegraphics[width=1\linewidth]{phys12-magnetism-magnetic-force-on-wire.png}
\end{figure}
\end{columns}
\end{frame}

\section{Magnetic Forces on Charges and Currents}

% Force on moving charge
\begin{frame}{Force on Moving Charge in Magnetic Field}
\begin{block}{Magnetic Force Formula}
The magnitude of the magnetic force on a moving charge:
\begin{equation}
F = qvB\sin\theta
\end{equation}
where $\theta$ is the angle between velocity and field.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
\item SI unit: tesla (T)
\item Force direction given by right-hand rule
\item Force is perpendicular to $v$ and $B$
\item No force when $v$ is parallel to $B$
\end{itemize}

\column{0.5\textwidth}
\begin{figure}
\centering
\includegraphics[width=0.75\linewidth]{phys12-magnetism-magnetic-field-lines-generator.png}
\end{figure}
\end{columns}
\end{frame}

\begin{frame}{Force on Moving Charge in Magnetic Field}
\begin{figure}
    \centering
    \includegraphics[width=0.75\linewidth]{phys12-vectors-vector-addition.png}
\end{figure}

\end{frame}

\begin{frame}{Force on Moving Charge in Magnetic Field}
\begin{figure}
\centering
\includegraphics[width=0.75\linewidth]{phys12-magnetism-right-hand-rule-force.png}
\end{figure}
\end{frame}



\begin{frame}{Force on Moving Charge in Magnetic Field}
\begin{figure}
\centering
\includegraphics[width=0.8\linewidth]{phys12-magnetism-right-hand-rule-current.png}
\end{figure}
\end{frame}

% Applications of force on moving charge
\begin{frame}{Applications of Force on Moving Charges}
\begin{block}{Circular Motion in Magnetic Field}
Radius of a charged particle's circular path:
\begin{equation}
r = \frac{mv}{qB}
\end{equation}
\end{block}

\begin{columns}
\column{0.6\textwidth}
\begin{itemize}
\item Applications:
\begin{itemize}
\item Mass spectrometers
\item Particle accelerators
\item Particle detectors
\end{itemize}
\item Only affects moving charges
\end{itemize}

\column{0.4\textwidth}
\begin{figure}
\centering
\includegraphics[width=1\linewidth]{phys12-magnetism-magnetic-force-on-current-loop.png}
\end{figure}
\end{columns}
\end{frame}

% Hall Effect
\begin{frame}{The Hall Effect}
\begin{block}{Hall Effect}
Voltage created across a current-carrying conductor by a magnetic field.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
\item Hall voltage:
\begin{equation}
\varepsilon = Blv
\end{equation}
\item $B$, $l$, and $v$ must be perpendicular
\item Applications:
\begin{itemize}
\item Measuring magnetic fields
\item Hall effect sensors
\end{itemize}
\end{itemize}

\column{0.5\textwidth}
\begin{figure}
\centering
\includegraphics[width=1\linewidth]{phys12-magnetism-hall-effect.png}
\end{figure}
\end{columns}
\end{frame}

% Force on current-carrying conductor
\begin{frame}{Magnetic Force on a Current-Carrying Conductor}
\begin{block}{Force Formula}
The magnetic force on a current-carrying conductor:
\begin{equation}
F = IlB\sin\theta
\end{equation}
where $I$ is current, $l$ is length, $B$ is field strength, and $\theta$ is the angle.
\end{block}

\begin{itemize}
\item Direction follows right-hand rule
\item Maximum force when conductor is perpendicular to field
\item No force when conductor is parallel to field
\item Basis for electric motors
\end{itemize}
\end{frame}

% Torque on current loop
\begin{frame}{Torque on a Current Loop: Motors and Meters}
\begin{block}{Torque Formula}
The torque on a current-carrying loop:
\begin{equation}
\tau = NIAB\sin\theta
\end{equation}
where $N$ is turns, $I$ is current, $A$ is area, $B$ is field strength.
\end{block}

\begin{columns}
\column{0.5\textwidth}
\begin{itemize}
\item Maximum torque: loop parallel to field
\item Zero torque: loop perpendicular to field
\item Applications:
\begin{itemize}
\item Electric motors
\item Measuring instruments
\end{itemize}
\end{itemize}

\column{0.5\textwidth}
\begin{figure}
\centering
\includegraphics[width=0.9\linewidth]{phys12-magnetism-torque-on-current-loop.png}
\end{figure}
\end{columns}
\end{frame}

\section{Example Problems}

% I do example
\begin{frame}{Example 1: "I do"}
\begin{block}{Problem}
Calculate the force on an electron moving at $5.0 \times 10^6$ m/s perpendicular to a magnetic field of 0.50 T.
\end{block}
\pause
\begin{block}{Solution}
Given:
\begin{itemize}
\item Charge of electron: $-1.60 \times 10^{-19}$ C
\item Velocity: $5.0 \times 10^6$ m/s
\item Magnetic field: 0.50 T
\item Angle: $90°$ (perpendicular)
\end{itemize}
\end{block}
\end{frame}

\begin{frame}{Example 1: "I do"}
\begin{block}{Solution}
Given:
\begin{itemize}
\item Charge of electron: $-1.60 \times 10^{-19}$ C
\item Velocity: $5.0 \times 10^6$ m/s
\item Magnetic field: 0.50 T
\item Angle: $90°$ (perpendicular)
\end{itemize}

Using $F = qvB\sin\theta$:

\pause

\begin{align}
F &= (-1.60 \times 10^{-19} \text{ C})(5.0 \times 10^6 \text{ m/s})(0.50 \text{ T})(\sin 90°) \\
F &= -4.0 \times 10^{-13} \text{ N}
\end{align}

The negative sign indicates force direction opposite to the right-hand rule.
\end{block}
\end{frame}

% We do example
\begin{frame}{Example 2: "We do"}
\begin{block}{Problem}
Find the radius of the circular path of a proton with speed $3.0 \times 10^6$ m/s in a magnetic field of 0.75 T when the proton velocity is perpendicular to the field.
\end{block}
\pause

\begin{block}{Solution}
Given:
\begin{itemize}
\item Mass of proton: $1.67 \times 10^{-27}$ kg
\item Charge of proton: $1.60 \times 10^{-19}$ C
\item Velocity: $3.0 \times 10^6$ m/s
\item Magnetic field: 0.75 T
\end{itemize}
\end{block}
\end{frame}

\begin{frame}{Example 2: "We do"}
\pause
\begin{block}{Solution}
Given:
\begin{itemize}
\item Mass of proton: $1.67 \times 10^{-27}$ kg
\item Charge of proton: $1.60 \times 10^{-19}$ C
\item Velocity: $3.0 \times 10^6$ m/s
\item Magnetic field: 0.75 T
\end{itemize}

Using $r = \frac{mv}{qB}$:

\pause

\begin{align}
r &= \frac{(1.67 \times 10^{-27} \text{ kg})(3.0 \times 10^6 \text{ m/s})}{(1.60 \times 10^{-19} \text{ C})(0.75 \text{ T})} \\
r &= 4.2 \times 10^{-2} \text{ m} = 4.2 \text{ cm}
\end{align}
\end{block}
\end{frame}

% You do example
\begin{frame}{Example 3: "You do"}
\begin{block}{Problem}
A straight wire carrying a 5.0 A current is placed in a uniform magnetic field of 0.25 T. If the wire is 10 cm long and makes an angle of 30° with the field, what is the magnetic force on the wire?
\end{block}
\pause
\begin{block}{Hints}
\begin{itemize}
\item Use $F = IlB\sin\theta$
\item Convert length to meters
\item Calculate $\sin(30°)$
\end{itemize}
\end{block}
\pause
\begin{block}{Answer (to check your work)}
$F = 0.125$ N
\end{block}
\end{frame}

% Key Equations summary
\begin{frame}{Key Equations}
\begin{block}{Magnetic Forces}
\begin{align}
F &= qvB\sin\theta & \text{(Force on moving charge)} \\
r &= \frac{mv}{qB} & \text{(Radius of circular path)} \\
\varepsilon &= Blv & \text{(Hall emf)} \\
F &= IlB\sin\theta & \text{(Force on current-carrying conductor)} \\
\tau &= NIAB\sin\theta & \text{(Torque on current loop)}
\end{align}
\end{block}

\begin{block}{Right-Hand Rule}
Thumb: velocity/current direction, Fingers: magnetic field, Palm: force direction
\end{block}
\end{frame}

% Summary
\begin{frame}{Summary}
\begin{itemize}
\item Magnets have north and south poles that cannot be isolated
\item Like poles repel, unlike poles attract
\item All magnetism arises from electric current
\item Magnetic fields affect moving charges and currents
\item The Hall effect creates voltage in conductors in magnetic fields
\item Torque on current loops enables motors and meters
\end{itemize}

\begin{block}{Applications}
Electromagnets, motors, generators, particle accelerators, MRI, sensors
\end{block}
\end{frame}

% References slide
\begin{frame}{References}
\begin{block}{Textbook}
OpenStax Physics, Chapter 22: Magnetism, Sections 22.1-22.8
\end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch06_slides_circular-motion-part2.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page info
\title[Circular Motion]{PHYS12 CH6: Gravitation and Keplar's Laws}
\subtitle{Sections 6.5-6.6}
\author[Mr. Gullo]{Mr. Gullo}
\date[Feb 2025]{February, 2025}

\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Learning Objectives}
By the end of this lesson, you will be able to:
\begin{itemize}
  \item Understand and explain Earth's gravitational force
        \item Describe the mathematical form of Newton's Universal Law of Gravitation
        \item Calculate gravitational forces between masses
        \item Explain the significance of the gravitational constant G
        \item Discuss the historical development of gravitational theory
\end{itemize}
\end{frame}

\begin{frame}{Historical Development}
    \begin{columns}
        \column{0.5\textwidth}
        \begin{itemize}
            \item Newton (1687): First precise definition of gravitational force
            \item Showed it explains both:
                \begin{itemize}
                    \item Falling objects on Earth
                    \item Astronomical motions
                \end{itemize}
            \item du Châtelet's contributions:
                \begin{itemize}
                    \item Translation and augmentation
                    \item Use of calculus to explain gravity
                \end{itemize}
        \end{itemize}
        \column{0.5\textwidth}

        \includegraphics[width=\textwidth]{phys12-gravity-newtons-cannon-thought-experiment.png}

        \end{columns}
\end{frame}

\begin{frame}
\frametitle{Video Media}
\begin{itemize}
 \item https://www.youtube.com/watch?v=7gf6YpdvtE0
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Newton's Universal Law of Gravitation}
\begin{itemize}
    \item Every particle in the universe attracts every other particle with a force along a line joining them
    \item Force is:
        \[ F = G\frac{m_1m_2}{r^2} \]
    where:
    \begin{itemize}
        \item $G = 6.674 \times 10^{-11}$ N$\cdot$m$^2$/kg$^2$
        \item $m_1, m_2$ are the masses of the objects
        \item $r$ is the distance between their centers
    \end{itemize}
    \item The force is always attractive
    \item It follows the inverse square law
\end{itemize}
\end{frame}

\begin{frame}
\frametitle{Gravity and Circular Motion}
\begin{itemize}
    \item For objects in circular orbit:
        \[ F_g = F_c \]
    \item This means:
        \[ G\frac{mM}{r^2} = m\frac{v^2}{r} \]
    \item Solving for orbital velocity:
        \[ v = \sqrt{\frac{GM}{r}} \]
    \item Applications:
    \begin{itemize}
        \item Planetary orbits
        \item Artificial satellites
        \item Space stations
    \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}{The Cavendish Experiment}
    \begin{columns}
        \column{0.6\textwidth}
        \begin{itemize}
            \item First accurate measurement of G (1798)
            \item Measured tiny gravitational attraction between lead spheres
            \item Led to first calculation of Earth's mass
            \item Modern version still used today
        \end{itemize}
        \column{0.4\textwidth}
        \includegraphics[width=\textwidth]{phys12-gravity-cavendish-experiment.png}
    \end{columns}
\end{frame}

\begin{frame}{Example: Earth's Gravitational Force}
    \begin{block}{Problem}
        Calculate the gravitational force between Earth ($M = 5.97 \times 10^{24}$ kg) and a 70 kg person at Earth's surface ($R = 6.37 \times 10^6$ m).
    \end{block}
    \begin{solution}
        \begin{align*}
            F &= G\frac{Mm}{r^2} \\
            &= (6.67 \times 10^{-11})\frac{(5.97 \times 10^{24})(70)}{(6.37 \times 10^6)^2} \\
            &= ??? \text{ N}
        \end{align*}
    \end{solution}
\end{frame}



\begin{frame}
\frametitle{Kepler's First Law: Elliptical Orbits}

\textbf{Statement:}
\begin{itemize}
    \item All planets orbit the Sun in elliptical paths
    \item The Sun is located at one focus of the ellipse
\end{itemize}

\textbf{Properties of Elliptical Orbits:}
\begin{itemize}
    \item \textbf{Semi-major axis} ($a$): half the longest diameter
    \item \textbf{Eccentricity} ($e$): measures deviation from circular orbit
    \begin{itemize}
        \item $e = 0$: perfect circle
        \item $0 < e < 1$: ellipse
        \item Most planetary orbits have small $e$
    \end{itemize}
    \item \textbf{Perihelion}: closest approach to Sun
    \item \textbf{Aphelion}: farthest point from Sun
\end{itemize}

\textbf{Implications:}
\begin{itemize}
    \item Distance from Sun varies during orbit
    \item Orbital speed varies (connects to Second Law)
    \item True for all orbiting bodies under gravity
\end{itemize}

\end{frame}

\begin{frame}
\frametitle{Video Media}
\begin{itemize}
 \item https://www.youtube.com/watch?v=Dvoe8Ib5D1o
\end{itemize}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-gravity-keplers-first-law.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Kepler's Laws: Equal Areas (Second Law)}
\begin{columns}
\begin{column}{0.6\textwidth}
\textbf{Kepler's Second Law:}
\begin{itemize}
    \item A line from the Sun to a planet sweeps out equal areas in equal times
    \item The shaded regions ($A_1$, $A_2$, $A_3$) have equal areas
    \item Important implications:
    \begin{itemize}
        \item Planet moves fastest when closest to Sun
        \item Planet moves slowest when farthest from Sun
        \item Angular momentum is conserved
    \end{itemize}
\end{itemize}
\end{column}
\begin{column}{0.4\textwidth}

\end{column}
\end{columns}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-gravity-kepler-orbital-diagram.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Kepler's Third Law of Planetary Motion}

\textbf{Mathematical Statement:}
\[ \frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3} \]
where:
\begin{itemize}
    \item $T$ = orbital period
    \item $r$ = average orbital radius
    \item Subscripts 1,2 refer to different planets
\end{itemize}

\textbf{Key Points:}
\begin{itemize}
    \item Relates orbital period to orbital radius
    \item Squared period proportional to cubed radius
    \item Valid for all objects orbiting same central mass
    \item Can be derived from Newton's laws and universal gravitation
\end{itemize}

\textbf{Example:}
If Planet 1 has period 1 year at 1 AU, a planet at 4 AU would have period:
\[ T_2 = \sqrt{4^3} = 8 \text{ years} \]
\end{frame}


\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-circuits-circuit-model-views.png}
\end{figure}
\end{frame}


\begin{frame}
\frametitle{Video Media}
\begin{itemize}
  \item https://www.youtube.com/watch?v=yC74lhJX9Ck
\end{itemize}
\end{frame}


\begin{frame}
\frametitle{What is a Planet? IAU Definition (2006)}

\begin{block}{Official IAU Definition}
A planet in our solar system is a celestial body that:
\end{block}

\begin{enumerate}
    \item Is in orbit around the Sun
    \begin{itemize}
        \item Regular, elliptical orbit
        \item Primary gravitational relationship with Sun
    \end{itemize}

    \item Has sufficient mass for hydrostatic equilibrium
    \begin{itemize}
        \item Strong enough gravity to become spherical
        \item Overcomes rigid body forces
    \end{itemize}

    \item Has cleared its orbital neighborhood
    \begin{itemize}
        \item Gravitationally dominant in its orbit
        \item No similar-sized objects in its orbital path
    \end{itemize}
\end{enumerate}
\end{frame}

\begin{frame}
\frametitle{Dwarf Planets and the Case of Pluto}

\begin{block}{Dwarf Planet Definition}
A celestial body that:
\begin{itemize}
    \item Orbits the Sun
    \item Has hydrostatic equilibrium
    \item Has NOT cleared its orbital neighborhood
\end{itemize}
\end{block}

\begin{itemize}
    \item Pluto was reclassified in 2006
    \item Reasons for reclassification:
    \begin{itemize}
        \item Shares its orbit with many Kuiper Belt objects
        \item Not gravitationally dominant in its region
        \item Similar to other objects in its orbital zone
    \end{itemize}
    \item Other recognized dwarf planets:
    \begin{itemize}
        \item Ceres (in asteroid belt)
        \item Eris (beyond Pluto)
        \item Haumea and Makemake (Kuiper Belt)
    \end{itemize}
\end{itemize}

\end{frame}
\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-circuits-rc-circuit-diagram.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Summary}
\textbf{Universal Gravitation:}
\begin{itemize}
    \item \textbf{Newton's Law:} $F_g = G\frac{m_1m_2}{r^2}$
    \item \textbf{Gravitational Constant:} $G = 6.674 \times 10^{-11}$ N$\cdot$m$^2$/kg$^2$
    \item \textbf{Historical Development:} Newton's theory and du Châtelet's contributions
    \item \textbf{Cavendish Experiment:} First measurement of G
\end{itemize}

\textbf{Kepler's Laws:}
\begin{itemize}
    \item \textbf{First Law:} Planets follow elliptical orbits with Sun at one focus
    \item \textbf{Second Law:} Equal areas in equal times
    \item \textbf{Third Law:} $\frac{T_1^2}{T_2^2} = \frac{r_1^3}{r_2^3}$
\end{itemize}

\textbf{Orbital Motion:}
\begin{itemize}
    \item \textbf{Orbital Velocity:} $v = \sqrt{\frac{GM}{r}}$
    \item \textbf{Gravitational Force = Centripetal Force:} $F_g = F_c$
    \item \textbf{Applications:} Planets, satellites, space stations, astroid mining
\end{itemize}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch08_slides_momentum.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title information
\title[Linear Momentum]{PHYS11 CH8: Linear Momentum \& Collisions}
\subtitle{Understanding Motion Through Conservation Laws}
\author[Mr. Gullo]{Mr. Gullo}
\date[]{}

\begin{document}

\frame{\titlepage}

% Learning Objectives
\begin{frame}
\frametitle{Learning Objectives}
\begin{itemize}
\item Define and calculate linear momentum
\item Understand impulse and its relationship to force
\item Apply conservation of momentum in various scenarios
\item Analyze elastic and inelastic collisions
\item Solve problems involving two-dimensional collisions
\item Understand basic rocket propulsion principles
\end{itemize}
\end{frame}
\begin{frame}{Chang’e-5 }
    \begin{figure}
        \centering
        \includegraphics[width=0.8\linewidth]{phys12-nuclear-atomic-change-process.jpg}
    \end{figure}
\end{frame}

\begin{frame}{Saturn V Launch}
   \begin{figure}
       \centering
       \includegraphics[width=0.4\linewidth]{Screenshot 2024-12-12 103335.png}
   \end{figure}
\end{frame}

% Title and Image Frame
\begin{frame}
\frametitle{Saturn V Launch Example}
\framesubtitle{Initial Acceleration Calculation}

% Placeholder image removed - insert appropriate Saturn V diagram here
\begin{center}
\textit{[Insert Saturn V rocket momentum diagram]}
\end{center}

\begin{block}{Saturn V Facts}
\begin{itemize}
\item Largest and most powerful rocket ever successfully operated
\item Used in Apollo moon missions
\item Height: 111 meters (363 feet)
\item Thrust at liftoff: 34.5 million newtons
\end{itemize}
\end{block}
\end{frame}

% Problem Statement Frame
\begin{frame}
\frametitle{Example 8.8: Saturn V Initial Acceleration}
\framesubtitle{Problem Setup}

\begin{block}{Given Values}
\begin{itemize}[<+->]
\item Initial mass: $m = 2.80 \times 10^6 \text{ kg}$
\item Fuel-burn rate: $\frac{\Delta m}{\Delta t} = 1.40 \times 10^4 \text{ kg/s}$
\item Exhaust velocity: $v_e = 2.40 \times 10^3 \text{ m/s}$
\end{itemize}
\end{block}

\pause
\begin{block}{Strategy}
Use rocket acceleration equation:
\[ a = \frac{v_e}{m}\frac{\Delta m}{\Delta t} - g \]
\end{block}
\end{frame}

% Solution Frame
\begin{frame}
\frametitle{Example 8.8: Solution}
\framesubtitle{Step-by-Step Calculation}

\begin{align*}
\uncover<1->{a &= \frac{v_e}{m}\frac{\Delta m}{\Delta t} - g} \\[1em]
\uncover<2->{&= \frac{2.40 \times 10^3 \text{ m/s}}{2.80 \times 10^6 \text{ kg}}}  \uncover<3->{ \times (1.40 \times 10^4 \text{ kg/s}) - 9.80 \text{ m/s}^2} \\[1em]
\uncover<4->{&= 12.0 \text{ m/s}^2 - 9.80 \text{ m/s}^2} \\[1em]
\uncover<5->{&= 2.20 \text{ m/s}^2}
\end{align*}
\end{frame}

% Discussion Frame
\begin{frame}
\frametitle{Example 8.8: Discussion}
\framesubtitle{Analysis of Results}

\begin{itemize}[<+->]
\item Initial acceleration seems small: $2.20 \text{ m/s}^2$
\item Acceleration increases as fuel burns because:
    \begin{itemize}
    \item Mass ($m$) decreases
    \item Exhaust velocity ($v_e$) remains constant
    \item Fuel burn rate ($\Delta m/\Delta t$) remains constant
    \end{itemize}

\end{itemize}

\begin{block}<5->{Key Insight}
The seemingly small initial acceleration is sufficient because it continuously increases as fuel is consumed.
\end{block}
\end{frame}

\begin{frame}{discussion time}

\end{frame}

% Key Concepts - Linear Momentum
\begin{frame}
\frametitle{Linear Momentum}
\begin{block}{Definition}
Linear momentum $\vec{p} = m\vec{v}$
\end{block}
\begin{itemize}
\item Vector quantity with direction same as velocity
\item SI units: kg⋅m/s
\item Proportional to both mass and velocity
\end{itemize}
\begin{equation*}
\text{Total Momentum} = \sum_i m_i\vec{v}_i
\end{equation*}
\end{frame}



% Section 8.1 Summary Frame
\begin{frame}
\frametitle{8.1 Linear Momentum and Force}
\begin{block}{Key Definition}
Linear momentum $\vec{p} = m\vec{v}$
\end{block}

\begin{itemize}
\item Linear momentum is fundamentally defined as mass × velocity
\item SI Units: kg·m/s
\item Newton's Second Law in momentum form:
\end{itemize}

\begin{equation*}
\vec{F}_{\text{net}} = \frac{\Delta \vec{p}}{\Delta t}
\end{equation*}

\begin{itemize}
\item $\vec{F}_{\text{net}}$ is net external force
\item $\Delta \vec{p}$ is change in momentum
\item $\Delta t$ is time interval
\end{itemize}
\end{frame}

% Impulse
\begin{frame}
\frametitle{Impulse}
\begin{block}{Key Equation}
$\vec{J} = \vec{F}\Delta t = \Delta \vec{p}$
\end{block}
\begin{itemize}
\item Measures change in momentum
\item Can reduce force by increasing time
\item Applications:
    \begin{itemize}
    \item Airbags
    \item Sports equipment
    \item Safety padding
    \end{itemize}
\end{itemize}
\end{frame}
\begin{frame}{Impulse Egg Drop}
    Show impulse egg drop video
\end{frame}
% Section 8.2 Summary Frame
\begin{frame}
\frametitle{8.2 Impulse}
\begin{block}{Key Concept}
Impulse equals change in momentum
\end{block}

\begin{align*}
\vec{J} &= \vec{F}_{\text{net}}\Delta t \\
&= \Delta \vec{p}
\end{align*}

\begin{itemize}
\item Impulse is the product of force and time interval
\item Forces typically vary over time
\item Area under force-time curve equals impulse
\end{itemize}
\end{frame}

% Section 8.3 Summary Frame
\begin{frame}
\frametitle{8.3 Conservation of Momentum}
\begin{block}{Conservation Principle}
In an isolated system: $\vec{p}_{\text{tot}} = \text{constant}$
\end{block}

\begin{itemize}
\item An isolated system has zero net external force
\item $\vec{p}_{\text{initial}} = \vec{p}_{\text{final}}$
\item Conserved in systems with:
    \begin{itemize}
    \item No external forces
    \item During projectile motion (horizontal direction)
    \item In particle systems
    \end{itemize}
\end{itemize}
\end{frame}

% Sections 8.4 & 8.5 Summary Frame
\begin{frame}
\frametitle{8.4 & 8.5 Collisions in One Dimension}
\begin{columns}[t]
\begin{column}{0.48\textwidth}
\textbf{Elastic Collisions}
\begin{itemize}
\item Conserves kinetic energy
\item Conserves momentum
\item Final velocities calculable from initial conditions
\end{itemize}
\end{column}

\begin{column}{0.48\textwidth}
\textbf{Inelastic Collisions}
\begin{itemize}
\item Kinetic energy not conserved
\item Momentum conserved
\item Perfectly inelastic: objects stick together
\end{itemize}
\end{column}
\end{columns}

\begin{block}{Applications}
Sports science, safety systems, particle physics
\end{block}
\end{frame}

% Section 8.6 Summary Frame
\begin{frame}
\frametitle{8.6 Two-Dimensional Collisions}

\begin{block}{Key Strategy}
Break motion into perpendicular components
\end{block}

\begin{itemize}
\item Choose x-axis parallel to incoming velocity
\item For mass 2 initially at rest:
    \begin{itemize}
    \item x-axis:
    \item $m_1v_1 = m_1v'_1\cos\theta_1 + m_2v'_2\cos\theta_2$
    \item y-axis:
    \item $0 = m_1v'_1\sin\theta_1 + m_2v'_2\sin\theta_2$
    \end{itemize}
\item Point masses cannot rotate or spin
\end{itemize}
\end{frame}
\begin{frame}{}
    \begin{figure}
        \centering
        \includegraphics[width=1\linewidth]{Screenshot 2024-12-17 070905.png}

    \end{figure}
\end{frame}

% Section 8.7 Summary Frame
\begin{frame}
\frametitle{8.7 Rocket Propulsion}

\begin{block}{Rocket Acceleration}
$a = \frac{v_e}{m}\frac{\Delta m}{\Delta t} - g$
\end{block}

\begin{itemize}
\item Based on Newton's Third Law
\item Acceleration depends on:
    \begin{enumerate}
    \item Exhaust velocity ($v_e$)
    \item Fuel burn rate ($\Delta m/\Delta t$)
    \item Rocket mass ($m$)
    \end{enumerate}
\item Greater acceleration with:
    \begin{itemize}
    \item Higher exhaust velocity
    \item Faster fuel consumption
    \item Lower rocket mass
    \end{itemize}
\end{itemize}
\end{frame}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\iffalse
\begin{comment}


% I Do Example
\begin{frame}
\frametitle{Example: Elastic Collision}
\framesubtitle{I Do}
A 2.0 kg ball moving at 3.0 m/s collides elastically with a 1.0 kg ball at rest.
\begin{enumerate}
\item Conservation of momentum:
    \[ (2.0)(3.0) = 2.0v_1 + 1.0v_2 \]
\item Conservation of energy:
    \[ \frac{1}{2}(2.0)(3.0)^2 = \frac{1}{2}(2.0)v_1^2 + \frac{1}{2}(1.0)v_2^2 \]
\item Solution:
    \[ v_1 = 1.0 \text{ m/s}, v_2 = 4.0 \text{ m/s} \]
\end{enumerate}
\end{frame}
\end{comment}
%%
\fi
\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch03_Lab_ReactionAcceleration-Kinematics.tex

```latex
\documentclass{beamer}
% Use DS9 global theme (includes pgfplots for visualization)
\usepackage{../../../../latex-beamer/shared/templates/ds9_theme}

% Title page configuration
\title[Reaction Time Lab]{PHYS12 CH: Reaction Time Lab}
\subtitle{Measuring Human Reaction Time with Kinematics}
\author[Mr. Gullo]{Mr. Gullo}
\date[Sep 27, 2025]{September 27, 2025}

\begin{document}

\frame{\titlepage}

\section{Introduction}

\begin{frame}
\frametitle{Learning Objectives}
\framesubtitle{What You Will Accomplish Today}
    \begin{itemize}
        \item \textbf{Apply Kinematics:} Use kinematic equations to calculate an unknown variable (time) from experimental data.
        \item \textbf{Connect Concepts:} Understand the connection between a physical measurement (distance) and a calculated physics quantity (reaction time).
        \item \textbf{Improve Lab Skills:} Practice making careful measurements, collecting multiple trials, and identifying sources of experimental uncertainty.
    \end{itemize}
\end{frame}

\begin{frame}
\frametitle{Video: The Science of Reaction Time}
    \vfill
    \begin{alertblock}{Media}
        Play the context video about reaction time in sports.
    \end{alertblock}
    \vfill
\end{frame}

\begin{frame}
\frametitle{Summary: What is Reaction Time?}
\framesubtitle{Key Ideas from the Video}
    \begin{block}{Definition}
        Reaction time is the total delay between detecting a stimulus and executing a physical response.
    \end{block}
    \pause
    \begin{itemize}
        \item The process involves a signal traveling from your senses (eyes) to your brain, and then from your brain to your muscles. \pause
        \item This delay, though short, is measurable and critical in high-speed situations. \pause
        \item In sports, even a few hundredths of a second can determine the outcome.
    \end{itemize}
\end{frame}


\begin{frame}
\frametitle{Video: The Science of Hitting a Fastball}
    \vfill
    \begin{alertblock}{Media}
        Play the video on hitting a fastball.
    \end{alertblock}
    \vfill
\end{frame}

\begin{frame}
\frametitle{Summary: Factors Affecting Reaction Time}
\framesubtitle{What Makes You Faster or Slower?}
    As the videos showed, your reaction time is not always the same. Several factors can influence it:
    \begin{columns}[T]
        \column{0.48\textwidth}
            \begin{block}{Physiological Factors}
                \begin{itemize}
                    \item \textbf{Alertness:} Tiredness slows down nerve signals.
                    \item \textbf{Stimulants:} Caffeine can temporarily shorten reaction time.
                \end{itemize}
            \end{block}

        \column{0.48\textwidth}
            \begin{block}{Cognitive Factors}
                \begin{itemize}
                    \item \textbf{Distractions:} Loud noises or other tasks increase the brain's processing time.
                    \item \textbf{Prediction:} Elite athletes "see into the future" by anticipating the trajectory of a ball based on the pitcher's body language.
                \end{itemize}
            \end{block}
    \end{columns}
    \vfill
    \begin{alertblock}{Think About This:}
    As you do the lab, consider which of these factors might be affecting your own results today.
    \end{alertblock}
\end{frame}

\begin{frame}
\frametitle{From Physics 11 to Physics 12}
\framesubtitle{Building on What You Know}
    \begin{columns}[T]
        \column{0.48\textwidth}
        \begin{alertblock}{In Physics 11...}
            \begin{itemize}
                \item You performed this lab to practice \textbf{measurement skills}.
                \item You took multiple trials and calculated an \textbf{average distance}.
                \item The goal was to understand measurement uncertainty.
            \end{itemize}
        \end{alertblock}

        \column{0.48\textwidth}
        \begin{block}{Now in Physics 12...}
            \begin{itemize}
                \item We will apply our knowledge of \textbf{kinematics}.
                \item We will use the measured distance to \textbf{calculate your reaction time}.
                \item The goal is to use a physics model to explain a real-world phenomenon.
            \end{itemize}
        \end{block}
    \end{columns}
\end{frame}

\section{The Physics of the Experiment}

\begin{frame}
\frametitle{The Physics of the Ruler Drop}
\framesubtitle{The Equation We Will Use}
    We will use the derivation from this kinematic equation:
    \[ \Delta x = v_0 t + \frac{1}{2} a t^2 \]
    \pause
    Since the ruler is dropped ($v_0=0$) and in free fall ($a=g$), it simplifies and we can solve for time ($t$).

    \begin{block}{Your Reaction Time Equation}
        \[ t = \sqrt{\frac{2 \Delta x}{g}} \]
    \end{block}
    \pause
    \vfill
    \begin{columns}[T]
        \column{0.5\textwidth}
            \textbf{Variables:}
            \begin{itemize}
                \item $t$ = reaction time
                \item $\Delta x$ = distance ruler fell
                \item $g = 9.8 \, \text{m/s}^2$
            \end{itemize}
        \column{0.5\textwidth}
            \textbf{Units:}
            \begin{itemize}
                \item $t$ in \textbf{seconds (s)}
                \item $\Delta x$ must be in \textbf{meters (m)!}
                \item $g$ in \textbf{m/s$^2$}
            \end{itemize}
    \end{columns}
\end{frame}

\begin{frame}
\frametitle{Lab Procedure: Setup}
\framesubtitle{Equipment and Safety}
    \begin{columns}[T]
        \column{0.48\textwidth}
        \textbf{Equipment:}
            \begin{itemize}
                \item One 30 cm ruler
                \item A partner
                \item Paper and pencil for recording data
            \end{itemize}

        \column{0.48\textwidth}
        \textbf{Safety First!}
            \begin{alertblock}{}
                Move slowly and carefully. Do not grab at the ruler too quickly or you might hit your partner's hand.
            \end{alertblock}
    \end{columns}
\end{frame}

\begin{frame}
\frametitle{Lab Procedure: Data Collection}
\framesubtitle{How to Do the Lab}
    \begin{enumerate}
        \item \textbf{Hold:} Your partner holds the ruler vertically. The 0 cm mark should be at the bottom.
        \item \textbf{Ready:} Place your thumb and index finger around the 0 cm mark, but \textit{do not touch} the ruler.
        \item \textbf{Drop:} Your partner will drop the ruler without warning.
        \item \textbf{Catch:} As soon as you see it fall, catch it!
        \item \textbf{Measure:} Read the distance in centimeters at the top edge of your fingers. This is $\Delta x$ for this trial.
        \item \textbf{Record:} Write this distance in your data table.
        \item \textbf{Repeat:} Perform a total of 5 trials to get a good average.
    \end{enumerate}
\end{frame}

\begin{frame}
\frametitle{Data Analysis Steps}
\framesubtitle{From Distance to Time}
    Once you have your 5 distance measurements:

    \begin{enumerate}
        \item \textbf{Find the Average:} Add your 5 distances together and divide by 5. This gives you an average distance in \textbf{cm}. \pause

        \item \alert{\textbf{Convert Units!}} Take your average distance in cm and divide by 100 to convert it to \textbf{meters (m)}. This is your final $\Delta x$. \pause

        \item \textbf{Calculate Time:} Plug your $\Delta x$ (in meters) into the equation to find your reaction time in seconds.
            \[ t = \sqrt{\frac{2 \times \Delta x}{9.8}} \]
    \end{enumerate}
\end{frame}

\begin{frame}
\frametitle{Homework: Analysis \& Discussion}
\framesubtitle{Thinking About Your Results}
    After you calculate your reaction time, answer these questions in your lab notebook.
    \begin{itemize}
        \item Are your measurements for each trial exactly the same? Why or why not? What does this tell you about measurement?
        \item What do you think were the biggest sources of error in this experiment? How could you make it more accurate?
        \item If you performed this experiment on Jupiter ($g \approx 25 \, \text{m/s}^2$), would the ruler fall a longer or shorter distance during the same reaction time? Explain your answer.
        \item How could you apply what you learned about reaction time to a real-world situation (e.g., driving, sports)?
    \end{itemize}
\end{frame}

\begin{frame}
\frametitle{Summary}
\framesubtitle{Key Takeaways}
    \begin{itemize}
        \item Human reaction time is a physical delay that can be measured using physics. \pause
        \item By measuring the \textbf{distance} an object falls in free fall, we can calculate the \textbf{time} it was falling. \pause
        \item We used the principles of kinematics for an object in \textbf{free fall} ($v_0 = 0$, $a=g$) to derive our key lab equation:
    \end{itemize}
    \begin{center}
    \begin{block}{}
        \[ t = \sqrt{\frac{2 \Delta x}{g}} \]
    \end{block}
    \end{center}
    \vfill
    \begin{alertblock}{}
        This lab is a perfect example of how we use physics models to understand and quantify the world around us.
    \end{alertblock}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch06_slides_circular-motion-part1.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page setup
\title[Circular Motion]{PHYS11 CH6: Uniform Circular Motion}
\subtitle{Sections 6.1-6.4: Rotational Motion and Forces}
\author[Mr. Gullo]{Mr. Gullo}
\date[Feb 2025]{February, 2025}
\institute{Physics Department}

\begin{document}

\frame{\titlepage}

\begin{frame}
\frametitle{Learning Objectives}
\begin{block}{By the end of this presentation, you will be able to:}
\begin{itemize}
\item Define and calculate rotation angle and angular velocity
\item Explain centripetal acceleration and its properties
\item Analyze forces in circular motion
\item Understand non-inertial frames and fictitious forces
\end{itemize}
\end{block}
\end{frame}

\section{Rotational Motion}

\begin{frame}
\frametitle{Rotation Angle}
\begin{block}{Definition}
The rotation angle $\Delta\theta$ is defined as:
\[ \Delta\theta = \frac{\Delta s}{r} \]
where:
\begin{itemize}
\item $\Delta s$ = arc length
\item $r$ = radius of curvature
\end{itemize}
\end{block}
\begin{itemize}
\item Measured in radians (rad)
\item One complete revolution: $2\pi$ rad = 360°
\end{itemize}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-mechanics-circular-motion-arc.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Angular Velocity}
\begin{block}{Definition}
Angular velocity $\omega$ is the rate of change of angle:
\[ \omega = \frac{\Delta\theta}{\Delta t} \]
\end{block}
\begin{block}{Relationship to Linear Velocity}
\[ v = r\omega \]
where:
\begin{itemize}
\item $v$ = linear velocity
\item $r$ = radius
\item $\omega$ = angular velocity
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-mechanics-angular-velocity-wheel.png}
\end{figure}
\end{frame}

\section{Centripetal Acceleration}

\begin{frame}
\frametitle{Media}
     \begin{itemize}
  \item Centripetal Acceleration
  \item \hyperlink{https://www.youtube.com/watch?v=90rFibLktF4}{https://www.youtube.com/watch?v=90rFibLktF4}
  \item Application
  \item \hyperlink{https://youtu.be/im-JM0f_J7s?si=VO4FyEuT5SLf7Fzr}{https://youtu.be/im-JM0f_J7s?si=VO4FyEuT5SLf7Fzr}
  \end{itemize}
\end{frame}

\begin{frame}
\frametitle{Centripetal Acceleration}
\begin{block}{Definition}
Centripetal acceleration is the acceleration toward the center of circular motion:
\[ a_c = \frac{v^2}{r} = r\omega^2 \]
\end{block}
\begin{itemize}
\item Always points toward center of circle
\item Magnitude depends on speed and radius
\item Required for circular motion
\end{itemize}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-mechanics-centripetal-acceleration.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{Example: Centripetal Acceleration}
\begin{block}{I Do: Car on Curved Path}
A car travels around a curve of radius 100 m at 20 m/s.
Calculate the centripetal acceleration.
\end{block}
\begin{align*}
a_c &= \frac{v^2}{r} \\
&= \frac{(20\text{ m/s})^2}{100\text{ m}} \\
&= 4\text{ m/s}^2
\end{align*}
\end{frame}

\section{Centripetal Force}

\begin{frame}
\frametitle{Media}
     \begin{itemize}
  \item Centripetal Force
  \item \hyperlink{https://www.youtube.com/watch?v=4bMawIIWi7w}{https://www.youtube.com/watch?v=4bMawIIWi7w}
  \end{itemize}
\end{frame}


\begin{frame}
\frametitle{Centripetal Force}
\begin{block}{Definition}
The centripetal force required for circular motion is:
\[ F_c = ma_c = m\frac{v^2}{r} = mr\omega^2 \]
\end{block}
\begin{itemize}
\item Net force must point toward center
\item Can be provided by various forces:
  \begin{itemize}
  \item Tension
  \item Gravity
  \item Friction
  \item Normal force
  \end{itemize}
\end{itemize}
\end{frame}

\begin{frame}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{phys12-mechanics-centripetal-force-diagram.png}
\end{figure}
\end{frame}

\begin{frame}
\frametitle{We Do: Centripetal Force Problem}
\begin{block}{Problem}
A 1000 kg car travels at 15 m/s around a curve of radius 50 m.
What centripetal force is required?
\end{block}
\begin{align*}
F_c &= m\frac{v^2}{r} \\
&= (1000\text{ kg})\frac{(15\text{ m/s})^2}{50\text{ m}} \\
&= 4500\text{ N}
\end{align*}
\end{frame}

\section{Non-inertial Frames}


\begin{frame}
\frametitle{Fictitious Forces}
\begin{block}{Key Points}
\begin{itemize}
\item Appear in non-inertial (accelerating) frames
\item Not "real" forces - arise from acceleration of reference frame
\item Examples:
  \begin{itemize}
  \item Centrifugal force
  \item Coriolis force
  \end{itemize}
\end{itemize}
\end{block}
\end{frame}
\begin{frame}
\frametitle{Media}
     \begin{itemize}
  \item Centrifugal force
  \item \hyperlink{https://www.youtube.com/watch?v=gRVIWWJwzfY}{https://www.youtube.com/watch?v=gRVIWWJwzfY}
  \end{itemize}
\end{frame}

\begin{frame}
\frametitle{Media}
     \begin{itemize}
  \item Coriolis force
  \item \hyperlink{https://www.youtube.com/watch?v=rdGtcZSFRLk}{https://www.youtube.com/watch?v=rdGtcZSFRLk}
  \end{itemize}
\end{frame}

\begin{frame}
\frametitle{The Coriolis Effect}
\begin{block}{Properties}
\begin{itemize}
\item Appears in rotating reference frames
\item Affects motion on rotating Earth
\item Causes deflection of:
  \begin{itemize}
  \item Weather systems
  \item Projectiles
  \item Ocean currents
  \end{itemize}
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{You Do: Practice Problem}
\begin{block}{Problem}
A 0.5 kg ball is attached to a string and swung in a horizontal circle of radius 1.5 m.
If the ball makes one complete revolution in 2 seconds:
\begin{enumerate}
\item Calculate the angular velocity
\item Find the centripetal acceleration
\item Determine the tension in the string
\end{enumerate}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Summary}
\begin{block}{Key Concepts}
\begin{itemize}
\item Angular quantities describe rotational motion
\item Centripetal acceleration points to center
\item Centripetal force causes circular motion
\item Fictitious forces appear in non-inertial frames
\end{itemize}
\end{block}
\end{frame}

\end{document}
```

File: /Users/joelgullo/dev/latex-beamer/src/phys12/slides/00Presentationupdateplan/tex-dump12/ch07_slides_energy-part3.tex

```latex
\documentclass{beamer}
% Use DS9 global theme
\usepackage{../../../../shared/templates/ds9_theme}

% Title page information
\title[Power \& Energy Systems]{PHYS11 CH7: Power, Energy \& Human Systems}
\subtitle{Sections 7.7-7.9: Power, Human Energy, and World Energy Use}
\author[Mr. Gullo]{Mr. Gullo}
\date[Fall 2024]{Fall Semester 2024}

\begin{document}

\frame{\titlepage}

% Learning Objectives
\begin{frame}
\frametitle{Learning Objectives}
\begin{block}{After this lesson, you will be able to:}
\begin{itemize}
\item Calculate power by analyzing changes in energy over time
\pause
\item Explain human body energy consumption at rest vs. during activity
\pause
\item Calculate the conversion of chemical energy in food to useful work
\pause
\item Describe the distinction between renewable and nonrenewable energy sources
\pause
\item Explain why energy conservation is necessary despite total energy being conserved
\end{itemize}
\end{block}
\end{frame}

% Power Concepts
\begin{frame}
\frametitle{Power: Rate of Energy Transfer}
\begin{block}{Definition}
Power ($P$) is the rate at which work is done or energy is transferred:
\[ P = \frac{W}{t} = \frac{\Delta E}{\Delta t} \]
SI unit: Watt (W) = 1 Joule/second
\end{block}
\pause
\begin{block}{Key Equations}
\begin{itemize}
\item Average Power: $P_{avg} = \frac{\Delta E}{\Delta t}$
\pause
\item Instantaneous Power: $P = \frac{dE}{dt}$
\pause
\item Relation to Force: $P = \vec{F} \cdot \vec{v}$
\end{itemize}
\end{block}
\end{frame}

\begin{frame}
\frametitle{Human Energy Systems}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{../images/Screenshot 2024-11-28 120054.png}
\end{figure}
\end{frame}
% Human Energy System
\begin{frame}
\frametitle{Human Energy Systems}
\begin{columns}
\column{0.5\textwidth}
\begin{block}{Basal Metabolic Rate (BMR)}
\begin{itemize}
\item Energy used at rest
\pause
\item Typical adult: 70-100 W
\pause
\item Major users:
  \begin{itemize}
  \item Liver \& Spleen (27\%)
  \item Brain (19\%)
  \item Muscles (18\%)
  \end{itemize}
\end{itemize}
\end{block}

\column{0.5\textwidth}
\begin{block}{Active Power Output}
\begin{itemize}
\item Walking: 280 W
\pause
\item Cycling: 400 W
\pause
\item Sprinting: 2415 W
\pause
\item Efficiency: 15-30\%
\end{itemize}
\end{block}
\end{columns}
\end{frame}

\begin{frame}
\frametitle{World Energy Use}
\begin{figure}
    \centering
    \includegraphics[width=0.9\linewidth]{../images/Screenshot 2024-11-28 120155.png}
\end{figure}
\end{frame}
\begin{frame}
\frametitle{World Energy Use}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{../images/Screenshot 2024-11-28 1202152.png}
\end{figure}
\end{frame}
\begin{frame}
\frametitle{World Energy Use}
\begin{figure}
    \centering
    \includegraphics[width=1\linewidth]{../images/Screenshot 2024-11-28 120215.png}
\end{figure}
\end{frame}
\begin{frame}
\frametitle{Example: Calculating Power Output}
\begin{block}{Problem}
A 60.0-kg person climbs stairs at a rate of 116 stairs per minute.
\pause
If each stair is 0.15 m high, what is their power output?
\end{block}

\pause

\begin{block}{Solution}
\begin{align*}
\text{Work per stair} &= mgh = (60.0\text{ kg})(9.80\text{ m/s}^2)(0.15\text{ m}) \\
&= 88.2\text{ J} \\
\pause
\text{Power} &= \frac{\text{Work}}{\text{time}} = \frac{88.2\text{ J} \times 116}{60\text{ s}} \\
&= 170\text{ W}
\end{align*}
\end{block}
\end{frame}

% Example Problem - We Do
\begin{frame}
\frametitle{Practice Problem - Together}
\begin{block}{Problem}
A person consumes a 250 Calorie (1047 kJ) snack.
\pause
How long would they need to cycle at 400 W to burn off this energy, assuming 20\% efficiency?
\end{block}
\pause

\begin{block}{Work Together}
Let's solve this step by step:
\begin{enumerate}
\item Convert food energy to Joules
\pause
\item Account for efficiency
\pause
\item Use power equation to find time
\end{enumerate}
\end{block}
\end{frame}

% Example Problem - You Do
\begin{frame}
\frametitle{Practice Problem - Independent}
\begin{block}{Your Turn}
Calculate the power output of a wind turbine that lifts 1000 kg of water 100 m high in 5 minutes.
\begin{itemize}
\item Use $g = 9.80\text{ m/s}^2$
\pause
\item Calculate work done first
\pause
\item Convert to power using time
\end{itemize}
\end{block}

\pause

\begin{block}{Check}
Answer: 32.7 kW
\end{block}
\end{frame}

% Summary
\begin{frame}
\frametitle{Summary}
\begin{block}{Key Takeaways}
\begin{itemize}
\item Power is the rate of energy transfer
\pause
\item Human power output varies by activity
\pause
\item Body efficiency typically 15-30\%
\pause
\item World energy use dominated by nonrenewables
\pause
\item Energy conservation crucial for sustainability
\end{itemize}
\end{block}
\pause
\begin{block}{Next Steps}
\begin{itemize}
\item Practice power calculations
\pause
\item Consider personal energy usage
\pause
\item Think about renewable energy solutions
\end{itemize}
\end{block}
\end{frame}

\end{document}
```

</file_contents>
