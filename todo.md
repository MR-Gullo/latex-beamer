# # IMPORTANT, ALREADY EXECUTED ONCE, ASK THE USER TO CHECK THE RESULTS.

Physics 12 Image Reference Update Task

## Objective

Update all image references in LaTeX Beamer presentations in the `src/phys12/slides/` directory to use the standardized naming convention defined in `src/phys12/images/newnames.md`.

## Task Details

### Step 1: Comprehensive Image Reference Analysis

- Search through all `.tex` files in `/Users/joelgullo/dev/latex-beamer/src/phys12/slides/` directory
- Identify all image references using `\includegraphics` commands
- Extract image filenames (without paths) and create a comprehensive list
- Look for patterns like `\includegraphics[...]{filename.ext}` and collect all referenced filenames

### Step 2: Apply Name Mappings from newnames.md

Update image references using these key mappings from `src/phys12/images/newnames.md`:

**Circuit Images:**

- `3seriescap.png` → `phys12-circuits-capacitors-in-series.png`
- `amvolmm.jpg` → `phys12-circuits-ammeter-voltmeter-connection.jpg`
- `cap.png` → `phys12-circuits-capacitor-symbol.png`
- `caps.png` → `phys12-circuits-capacitor-types.png`
- `capseriesparalel.png` → `phys12-circuits-capacitors-series-parallel-comparison.png`
- `dischcurve.png` → `phys12-circuits-capacitor-discharge-curve.png`
- `ecg.png` → `phys12-circuits-ecg-waveform.png`
- `image.png` → `phys12-circuits-rc-circuit-diagram.png`
- `inres.png` → `phys12-circuits-internal-resistance.png`
- `modelviews.png` → `phys12-circuits-circuit-model-views.png`
- `OIP-C.jpg` → `phys12-circuits-kirchhoffs-junction-rule.jpg`
- `paralelcap.png` → `phys12-circuits-capacitors-in-parallel.png`
- `ParallelCircuitbat.jpg` → `phys12-circuits-parallel-circuit-with-battery.jpg`
- `rms.png` → `phys12-circuits-rms-voltage-ac.png`
- `seriescap.png` → `phys12-circuits-capacitor-in-series.png`
- `seriesparralcap.png` → `phys12-circuits-series-parallel-capacitor-combo.png`
- `serres.png` → `phys12-circuits-resistors-in-series.png`
- `wheatstone.jpg` → `phys12-circuits-wheatstone-bridge.jpg`
- `Screenshot 2024-11-12 133942.png` → `phys12-circuits-rc-circuit-charging-graph.png`
- `Screenshot 2024-11-19 073715.png` → `phys12-circuits-kirchhoffs-loop-rule-example.png`

**Magnetism Images:**

- `chflux.png` → `phys12-magnetism-magnetic-flux-through-loop.png`
- `eddy.png` → `phys12-magnetism-eddy-currents.png`
- `genyr.png` → `phys12-magnetism-electric-generator-diagram.png`
- `halleffct.png` → `phys12-magnetism-hall-effect.png`
- `mangle.png` → `phys12-magnetism-magnetic-field-angle.png`
- `mggmgcrc.png` → `phys12-magnetism-magnetic-force-on-current-loop.png`
- `mgng.png` → `phys12-magnetism-magnetic-field-generator.png`
- `mgngd.png` → `phys12-magnetism-magnetic-field-lines-generator.png`
- `mgRHR.png` → `phys12-magnetism-right-hand-rule-force.png`
- `mgtrq.png` → `phys12-magnetism-torque-on-current-loop.png`
- `mmgmg.png` → `phys12-magnetism-magnetic-force-on-wire.png`
- `rhr1-.png` → `phys12-magnetism-right-hand-rule-current.png`

**Electrostatics Images:**

- `charge.png` → `phys12-electrostatics-charge-interactions.png`
- `equippt.png` → `phys12-electrostatics-equipotential-lines.png`
- `Pith_ball_electroscope_operating_principle.svg.png` → `phys12-electrostatics-pith-ball-electroscope.png`
- `plates.png` → `phys12-electrostatics-parallel-plates-electric-field.png`
- `repel.png` → `phys12-electrostatics-charge-repulsion.png`
- `repellines.png` → `phys12-electrostatics-field-lines-repulsion.png`
- `Van_de_Graaff_Generator.svg.png` → `phys12-electrostatics-van-de-graaff-generator.png`

**Gravity Images:**

- `cavend.png` → `phys12-gravity-cavendish-experiment.png`
- `dwarf-planets.jpg` → `phys12-gravity-dwarf-planets.jpg`
- `newt.png` → `phys12-gravity-newtons-law-of-gravitation.png`
- `newtch.png` → `phys12-gravity-newtons-cannon-thought-experiment.png`
- `th-991058791.jpg` → `phys12-gravity-newtons-law-of-universal-gravitation-formula.jpg`
- `kepfirst.png` → `phys12-gravity-keplers-first-law.png`
- `Keplar.png` → `phys12-gravity-kepler-orbital-diagram.png`

**Vector Images:**

- `vectarr.png` → `phys12-vectors-vector-addition.png`
- `21fig.png` → `phys12-vectors-vector-addition-figure-21.png`
- `4 fig.png` → `phys12-vectors-vector-addition-figure-4.png`
- `Picture 3.23.png` → `phys12-vectors-vector-diagram-3-23.png`
- `vectcomp.png` → `phys12-vectors-vector-components.png`

**Mechanics Images:**

- `arc.png` → `phys12-mechanics-circular-motion-arc.png`
- `centerseek.png` → `phys12-mechanics-centripetal-acceleration.png`
- `centforce.png` → `phys12-mechanics-centripetal-force-diagram.png`
- `wheelomega.png` → `phys12-mechanics-angular-velocity-wheel.png`

**Formula Sheet Images:**

- `nesw.png` → `phys12-navigation-compass-directions.png`
- `nrt.png` → `phys12-formulas-newton-relativity-thermodynamics.png`
- `rt.png` → `phys12-formulas-relativity-thermodynamics.png`

**Miscellaneous Images:**

- `cinec_logo.png` → `phys12-shared-cinec-logo.png`
- `Change-5.jpg` → `phys12-nuclear-atomic-change-process.jpg`

### Step 3: Systematic File Updates

- Read each `.tex` file individually to understand current image references
- Apply exact filename replacements within `\includegraphics` commands
- Ensure only exact filename matches are replaced (not partial matches)
- Preserve all other formatting, paths, and parameters

### Step 4: Create Analysis Reports

- **List A:** Images referenced in `.tex` files but NOT found in newnames.md mapping
- **List B:** Images in newnames.md mapping but NOT referenced in any `.tex` files
- Include counts and categorization for better understanding of coverage

### Expected Files to Process

Based on directory listing, process these `.tex` files:

- ch01-03_review_test-prep.tex
- ch03_slides_vectors.tex
- ch04-05-09_review.tex
- ch04_slides_motion.tex
- ch05_slides_forces.tex
- ch06_slides_circular-motion-part1.tex
- ch06_slides_circular-motion-part2.tex
- ch07_assign_bill-nye-energy.tex
- ch07_assign_video-analysis.tex
- ch07_lab_energy.tex
- ch07_slides_energy-part1.tex
- ch07_slides_energy-part2.tex
- ch07_slides_energy-part3.tex
- ch08_assign_photo-journal-v2.tex
- ch08_assign_photo-journal.tex
- ch08_lab_momentum.tex
- ch08_slides_momentum.tex
- ch09_assign_problem-solving.tex
- ch09_assign_roof-ladder.tex
- ch09_slides_equilibrium.tex
- ch18_slides_electric-fields.tex
- ch19_notes_chinese.tex
- ch19_slides_electric-potential.tex
- ch20-21_notes_chinese.tex
- ch20-21_slides_electric-current.tex
- ch22-23_slides_electromagnetic-induction.tex
- ch22_slides_magnetism-v2.tex
- ch22_slides_magnetism.tex
- ch23_slides_electromagnetic-waves.tex
- misc_colour.tex
- misc_communications-project.tex
- misc_dnd.tex
- test_ch04.tex
- util_ch05_archive.tex
- util_formula-jigsaw.tex
- util_formula-sheet.tex
- util_template-phys12.tex

### Success Criteria

- All old image names from the mapping have been replaced with new standardized names
- No broken image references introduced
- Comprehensive analysis of coverage (referenced vs mapped images)
- All changes follow the `phys12-[topic]-[description].[ext]` naming convention
- Maintain LaTeX file integrity and compilation compatibility

### Notes

- Similar to the phys11 project, some files may already use the standardized naming convention
- Focus on exact string matching within `\includegraphics{}` commands
- Preserve any subdirectory paths that may be present
- Create detailed documentation of what was changed and what remains unmapped
