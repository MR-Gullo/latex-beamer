# Physics Slides Coverage Audit Report

**Generated**: 2024-12-24
**Source CSV**: `Future-IB-NCEA-BC-PHYS11-12v2.csv`
**Audited Directories**: `phys11/slidesv2/`, `phys12/slidesv2/`

---

## Executive Summary

| Course | Total Files | Units Complete | Units Partial | Units TODO | Critical Issues |
|--------|-------------|----------------|---------------|------------|-----------------|
| PHYS11 | 44 .tex | 6/8 | 1/8 (U06) | 1/8 (U07) | 4 TODO files need content |
| PHYS12 | 48 .tex | 5/8 | 1/8 (U05) | 2/8 (U04,U07) | College→HS chapter migration needed |

### Key Finding
**PHYS12 slides use OpenStax College Physics chapter numbers, but the curriculum (CSV) references OpenStax HS Physics chapters.** These are different textbooks with different chapter structures.

---

## PHYS11 Detailed Audit

### Unit Coverage Status

| Unit | CSV Topic | OpenStax HS Ch | Slides Status | Files Count |
|------|-----------|----------------|---------------|-------------|
| U01 | Investigation & Data Analysis | 1.1-1.3, 2.1-2.2 | COMPLETE | 6 |
| U02 | Kinematics (1D Motion) | 2.3-2.4, 3.1-3.2 | COMPLETE | 6 |
| U03 | Dynamics (Newton's Laws) | 4.1-4.4 | COMPLETE | 10 |
| U04 | Work, Energy & Power | 9.1-9.2 | COMPLETE | 5 |
| U05 | Thermal Physics & Gases | 11, 12 | COMPLETE | 2 |
| U06 | Waves & Sound | 13, 14 | PARTIAL | 3 (1 TODO) |
| U07 | Optics (Geo & Wave) | 15, 16, 17 | ALL TODO | 3 TODO |
| U08 | DC Electric Circuits | 18.1, 19 | COMPLETE | 3 |

### PHYS11 File Inventory by Unit

#### U01 - Investigation & Data Analysis (6 files)
```
U01-Lesson-CH1-PHYS11-What-Is-Physics.tex
U01-Lab-CH1-PHYS11-Graphing-Lines.tex
U01-Worksheet-CH1-PHYS11-Jigsaw-Reading.tex
U01-Slides-CH1s3-PHYS11-SI-Units-SigFigs.tex
U01-Slides-CH1-2-PHYS11-Assessment-Strategy.tex
U01-Review-CH1-2-PHYS11-Unit-Review.tex
```

#### U02 - Kinematics 1D (6 files)
```
U02-Slides-CH2-PHYS11-Kinematics-1D.tex
U02-Slides-CH3-PHYS11-Acceleration-Kinematics.tex
U02-Slides-CH3-PHYS11-Vectors-Intro.tex
U02-Lab-CH3-PHYS11-ReactionTime.tex
U02-Lab-CH3-PHYS11-Metro-Kinematics.tex
U02-Review-CH2-3-PHYS11-Quiz-CommonMistakes.tex
```

#### U03 - Dynamics (10 files)
```
U03-Slides-CH4-PHYS11-Forces-FBD.tex
U03-Slides-CH5s1-3-PHYS11-Vector-Analysis.tex
U03-Slides-CH5s4-PHYS11-Friction.tex
U03-Slides-CH6s1-2-PHYS11-Circular-Motion.tex
U03-Lab-CH4-PHYS11-Newton-Second-Law.tex
U03-Lab-CH4-PHYS11-Virtual-Forces.tex
U03-Lab-CH5s4-PHYS11-Friction-Angle.tex
U03-Lab-CH5s4-PHYS11-Snap-Friction.tex
U03-Lab-CH6-PHYS11-Angular-Speed.tex
U03-Assign-CH4-PHYS11-Video-Analysis.tex
```

#### U04 - Work, Energy & Power (5 files)
```
U04-Slides-CH9-PHYS11-WorkEnergyConservation.tex
U04-Lab-CH8-PHYS11-Elastic-Collisions.tex
U04-Lab-CH9-PHYS11-PEtoKEConversion.tex
U04-Lab-CH9-PHYS11-SteelBallDropDesign.tex
U04-Assign-CH9-PHYS11-Lab-Design-v2.tex
```

#### U05 - Thermal Physics (2 files)
```
U05-Slides-CH11-PHYS11-Thermal-Energy-Heat.tex
U05-Slides-CH12s1-4-PHYS11-Thermodynamics-Laws.tex
```

#### U06 - Waves & Sound (3 files, 1 TODO)
```
U06-Slides-CH13-PHYS11-WavesProperties.tex
U06-Slides-CH13-14-5.5-PHYS11-OscillationsWavesSound.tex
U06-Slides-CH14-PHYS11-TBD-TODO.tex          # TODO: Sound chapter
```

#### U07 - Optics (3 files, ALL TODO)
```
U07-Slides-CH15-PHYS11-Light-TODO.tex        # TODO: Light properties
U07-Slides-CH16-PHYS11-MirrorsLenses-TODO.tex   # TODO: Geometric optics
U07-Slides-CH17-PHYS11-Diffraction-TODO.tex     # TODO: Wave optics
```

#### U08 - DC Electric Circuits (3 files)
```
U08-Slides-CH18-PHYS11-CurrentElectricity.tex
U08-Slides-CH1819-PHYS11-ElectrostaticCircuits.tex
U08-Slides-CH19-PHYS11-Circuits.tex
```

#### Utility Files (6 files)
```
UTIL-Slides-PHYS11-Exam-Strategy.tex
UTIL-Slides-PHYS11-NOPS-Guide.tex
UTIL-Assign-PHYS11-Engineering-Earth.tex
UTIL-Worksheet-PHYS11-FPPL-Reflection.tex
UTIL-Rubric-Homework-PHYS11.tex
UTIL-Rubric-Lab-PHYS11.tex
```

### PHYS11 TODO Files Requiring Content (4 total)

| File | Topic | HS Chapter | CSV Requirements |
|------|-------|------------|------------------|
| U06-Slides-CH14-PHYS11-TBD-TODO.tex | Sound | 14 | Sound characteristics, Resonance, Doppler Effect |
| U07-Slides-CH15-PHYS11-Light-TODO.tex | Light | 15 | Reflection, basics |
| U07-Slides-CH16-PHYS11-MirrorsLenses-TODO.tex | Mirrors/Lenses | 16 | Refraction, Snell's Law, Ray diagrams |
| U07-Slides-CH17-PHYS11-Diffraction-TODO.tex | Wave Optics | 17 | Diffraction, Interference |

---

## PHYS12 Detailed Audit

### Critical Issue: Textbook Mismatch

**Current slides**: Reference **OpenStax College Physics** chapter numbers
**Target (CSV)**: References **OpenStax High School Physics** chapter numbers

These are DIFFERENT textbooks with different chapter organizations!

### Chapter Mapping: College Physics vs HS Physics

| Topic | College Physics Ch | HS Physics Ch | Notes |
|-------|-------------------|---------------|-------|
| Vectors & 2D Motion | Ch 3, 5 | Ch 5 | Similar |
| Forces | Ch 4 | Ch 4 | Similar |
| Circular Motion | Ch 6 | Ch 6 | Similar |
| Work & Energy | Ch 7 | Ch 9 | **Different CH#** |
| Momentum | Ch 8 | Ch 8 | Same |
| Gravitation | Ch 13 | Ch 7 | **Very different!** |
| Electrostatics | Ch 18-19 | Ch 18 | Similar |
| Electric Current | Ch 20 | Ch 20 | Same |
| Magnetism | Ch 22 | Ch 20-21 | Different |
| Atomic/Nuclear | Ch 30-32 | Ch 21-22 | Different |
| Relativity | Ch 28 | Ch 10 | **Very different!** |
| Waves/Sound | Ch 16-17 | Ch 13-14 | Different |

### Unit-by-Unit Analysis

#### U01 - Vectors & 2D Kinematics
**CSV Requirement**: [OS] Ch 5.1-5.3
**Current Files**:
```
U01-Slides-CH5-PHYS12-2D-Kinematics.tex
U01-Slides-CH5-PHYS12-Forces-Applications.tex
U01-Worksheet-CH5-PHYS12-Jigsaw.tex
```
**Status**: ALIGNED - Chapter numbers match

#### U02 - Momentum & Impulse
**CSV Requirement**: [OS] Ch 8
**Current Files**:
```
U02-Slides-CH8-PHYS12-Momentum.tex
U02-Lab-CH8-PHYS12-Momentum.tex
U02-Lab-CH8-PHYS12-Cart-Track.tex
U02-Lab-CH8-PHYS12-Tennis-Ball.tex
U02-Assign-CH8-PHYS12-PhotoJournal.tex
U02-Assign-CH8-PHYS12-PhotoJournal-v2.tex
```
**Status**: ALIGNED - Chapter numbers match

#### U03 - Rigid Body Mechanics (Circular Motion & Equilibrium)
**CSV Requirement**: [OS] Ch 6, 9.3
**Current Files**:
```
U03-Slides-CH6-PHYS12-Circular-Motion-Part1.tex
U03-Slides-CH6-PHYS12-Circular-Motion-Part2.tex
U03-Slides-CH9s3-PHYS12-Equilibrium.tex
U03-Lab-CH6-PHYS12-Lab-Design.tex
U03-Assign-CH9s3-PHYS12-Problem-Solving.tex
U03-Assign-CH9s3-PHYS12-Roof-Ladder.tex
```
**Status**: ALIGNED - Chapter numbers match

#### U04 - Gravitation & Astrophysics [MISMATCH]
**CSV Requirement**: [OS] Ch 7, 22.5 (Gravitation, Stellar evolution)
**Current Files**:
```
U04-Slides-CH7-PHYS12-Energy-Part1-2.tex    # WRONG CONTENT
U04-Slides-CH7-PHYS12-Energy-Part3.tex       # WRONG CONTENT
U04-Lab-CH7-PHYS12-Energy.tex                # WRONG CONTENT
U04-Lab-CH7-PHYS12-Energy-Conversion.tex     # WRONG CONTENT
U04-Lab-CH7-PHYS12-Skate-Park.tex            # WRONG CONTENT
U04-Assign-CH7-PHYS12-Video-Analysis.tex     # WRONG CONTENT
U04-Assign-CH7-PHYS12-Bill-Nye.tex           # WRONG CONTENT
```
**Status**: CRITICAL MISMATCH
- Files contain **Energy** content (College Physics Ch7)
- CSV wants **Gravitation** content (HS Physics Ch7)
- HS Physics Ch7 = Gravitation (NOT Energy!)
- **Action**: Create new Gravitation slides in slidesv3/

#### U05 - Electrostatics
**CSV Requirement**: [OS] Ch 18.2-18.5
**Current Files**:
```
U05-Slides-CH18-PHYS12-Electric-Fields.tex
U05-Slides-CH19-PHYS12-Electric-Potential.tex
```
**Status**: PARTIAL - Has electric fields/potential, verify section coverage

#### U06 - Electromagnetism
**CSV Requirement**: [OS] Ch 20
**Current Files**:
```
U06-Slides-CH20-PHYS12-Electric-Current.tex
```
**Status**: ALIGNED - But only 1 slide file, may need expansion

#### U07 - Atomic & Nuclear Physics [MISMATCH]
**CSV Requirement**: [OS] Ch 21, 22.1-22.4 (Atomic structure, Quantum, Radioactivity)
**Current Files**:
```
U07-Slides-CH22-PHYS12-Magnetism.tex         # WRONG CONTENT
U07-Slides-CH22-PHYS12-Magnetism-v2.tex      # WRONG CONTENT
U07-Slides-CH22-PHYS12-EM-Induction.tex      # WRONG CONTENT
```
**Status**: CRITICAL MISMATCH
- Files contain **Magnetism** content (College Physics Ch22)
- CSV wants **Atomic & Nuclear** content (HS Physics Ch21-22)
- Magnetism content should move to U06 in new structure
- **Action**: Create new Atomic/Nuclear slides in slidesv3/

#### U08 - Relativity & Particles
**CSV Requirement**: [OS] Ch 10, 23 (Special Relativity, Standard Model)
**Current Files**:
```
U08-Slides-CH28-PHYS12-Relativity-Part1.tex
U08-Slides-CH28-PHYS12-Relativity-Part2.tex
U08-Slides-CH23-PHYS12-EM-Waves.tex
U08-Assign-CH28-PHYS12-Relativity.tex
U08-Assign-CH28-PHYS12-Topic-Workshop.tex
U08-Assign-CH28-PHYS12-Topic-Quiz.tex
U08-Assign-CH28-PHYS12-Relativity-Song.tex
U08-Worksheet-CH28-PHYS12-Topic-Guide.tex
```
**Status**: CONTENT ALIGNED (chapter numbers differ)
- College Physics Ch28 = Relativity (same as HS Ch10)
- Content is correct, chapter numbers need updating

### PHYS12 Review & Utility Files
```
REVIEW-CH1-2-PHYS12-Intro-Kinematics.tex
REVIEW-CH1-3-PHYS12-Test-Prep.tex
REVIEW-CH2-3-PHYS12-Quiz-Mistakes.tex
REVIEW-CH4-5-9-PHYS12-Review.tex
REVIEW-Lab-PHYS12-Graphs-Tracks.tex
REVIEW-Worksheet-PHYS12-Jigsaw-CH1.tex
UTIL-Formula-Sheet-PHYS12.tex
UTIL-Formula-Sheet-v2-PHYS12.tex
UTIL-Formula-Jigsaw-PHYS12.tex
UTIL-Rubric-Problem-Solving-PHYS12.tex
MISC-DnD-PHYS12.tex
MISC-Communications-Project-PHYS12.tex
```

---

## Gap Analysis Summary

### PHYS11 Gaps (4 slide sets needed)

| Priority | Unit | Topic | Required Content |
|----------|------|-------|------------------|
| HIGH | U06 | Sound (Ch 14) | Sound waves, resonance, Doppler effect |
| HIGH | U07 | Light (Ch 15) | Light properties, reflection basics |
| HIGH | U07 | Mirrors/Lenses (Ch 16) | Geometric optics, ray diagrams, Snell's Law |
| HIGH | U07 | Diffraction (Ch 17) | Wave optics, interference, diffraction patterns |

### PHYS12 Gaps (Migration + New Content)

| Priority | Issue | Action Required |
|----------|-------|-----------------|
| CRITICAL | U04 Energy→Gravitation | Create new Gravitation slides (HS Ch 7, 22.5) |
| CRITICAL | U07 Magnetism→Atomic | Create new Atomic/Nuclear slides (HS Ch 21, 22) |
| HIGH | All chapter numbers | Update CH# refs in filenames, titles, sections |
| MEDIUM | U06 expansion | Add more Electromagnetism content if needed |
| LOW | Review files | Update chapter references |

---

## Migration Roadmap for slidesv3/

### Recommended Structure
```
/Users/joelgullo/dev/latex-beamer/src/phys12/slidesv3/
├── U01-Vectors-2DKinematics/
│   ├── U01-Slides-CH5-PHYS12-2D-Kinematics.tex      (migrate from v2)
│   ├── U01-Slides-CH5-PHYS12-Forces-Applications.tex (migrate from v2)
│   └── U01-Worksheet-CH5-PHYS12-Jigsaw.tex          (migrate from v2)
│
├── U02-Momentum-Impulse/
│   ├── U02-Slides-CH8-PHYS12-Momentum.tex           (migrate from v2)
│   └── [labs & assigns]                              (migrate from v2)
│
├── U03-RigidBody-Mechanics/
│   ├── U03-Slides-CH6-PHYS12-Circular-Motion.tex    (merge parts 1&2)
│   ├── U03-Slides-CH9s3-PHYS12-Equilibrium.tex      (migrate from v2)
│   └── [labs & assigns]                              (migrate from v2)
│
├── U04-Gravitation-Astrophysics/     # NEW CONTENT
│   ├── U04-Slides-CH7-PHYS12-Gravitation-TODO.tex   (create new)
│   └── U04-Slides-CH22s5-PHYS12-Stars-TODO.tex      (create new)
│
├── U05-Electrostatics/
│   ├── U05-Slides-CH18-PHYS12-Electric-Fields.tex   (migrate from v2)
│   └── U05-Slides-CH18-PHYS12-Electric-Potential.tex (rename CH19→CH18)
│
├── U06-Electromagnetism/
│   ├── U06-Slides-CH20-PHYS12-Electric-Current.tex  (migrate from v2)
│   ├── U06-Slides-CH20-PHYS12-Magnetism.tex         (move from U07)
│   └── U06-Slides-CH20-PHYS12-EM-Induction.tex      (move from U07)
│
├── U07-Atomic-Nuclear/               # NEW CONTENT
│   ├── U07-Slides-CH21-PHYS12-Atomic-Structure-TODO.tex  (create new)
│   ├── U07-Slides-CH22-PHYS12-Quantum-TODO.tex           (create new)
│   └── U07-Slides-CH22-PHYS12-Radioactivity-TODO.tex     (create new)
│
├── U08-Relativity-Particles/
│   ├── U08-Slides-CH10-PHYS12-Relativity-Part1.tex  (rename CH28→CH10)
│   ├── U08-Slides-CH10-PHYS12-Relativity-Part2.tex  (rename CH28→CH10)
│   ├── U08-Slides-CH23-PHYS12-Standard-Model.tex    (update content)
│   └── [assigns & worksheets]                        (migrate from v2)
│
├── REVIEW/
│   └── [review materials - update chapter refs]
│
├── UTIL/
│   └── [formula sheets, rubrics]
│
└── INVENTORY.md
```

### Migration Phases

#### Phase 1: Create Structure (1 task)
- Create slidesv3/ directory structure
- Create INVENTORY.md template

#### Phase 2: Direct Migrations (5 units)
- U01, U02, U03, U08: Copy files, update chapter references
- U05, U06: Reorganize and merge content

#### Phase 3: New Content Creation (2 units)
- U04: Create Gravitation & Astrophysics slides
- U07: Create Atomic & Nuclear Physics slides

#### Phase 4: Update References (All units)
- Update all chapter numbers in:
  - Filenames
  - `\title[]{}` commands
  - `\subtitle{}` commands
  - `\section{}` headers
  - `\frametitle{Example X.X}` references
  - Image paths if needed

---

## Files Reference

### Source CSV
```
/Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/CoursesIBDPNCEA/Future-IB-NCEA-BC-PHYS11-12v2.csv
```

### PHYS11 Directory
```
/Users/joelgullo/dev/latex-beamer/src/phys11/slidesv2/
Total: 44 .tex files
```

### PHYS12 Directory
```
/Users/joelgullo/dev/latex-beamer/src/phys12/slidesv2/
Total: 48 .tex files
```

---

## Next Steps

1. **Decide on migration timeline** for PHYS12 slidesv3/
2. **Prioritize PHYS11 optics slides** (U07) for completion
3. **Source content** for new Gravitation and Atomic/Nuclear slides
4. **Create slidesv3/ structure** when ready to begin migration
