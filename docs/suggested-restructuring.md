# Suggested LaTeX Beamer Project Restructuring

Based on comprehensive analysis using Gemini CLI, here's a detailed plan to reorganize the three slideshow collections into a unified, maintainable structure.

## Current Issues Identified

### Organizational Problems
- **Inconsistent naming**: Mixed capitalization and `-CH` suffixes (`Computer-Science-12/`, `PHYS11-CH/`, `Phys12-CH/`)
- **Cluttered root directories**: Images and LaTeX files mixed together in course folders
- **No shared resources**: Duplicate files like `cinec_logo.png` across physics courses
- **Missing templates**: No consistent template usage across all courses

### Image Management Issues
- **Chaotic naming**: Mix of cryptic hashes (`02c4ce1d-fdd3-47cd-8a44-ce141f1a4c98.png`), generic names (`image.png`), and unclear identifiers (`th-1448775654.jpg`)
- **No centralization**: Images scattered throughout course directories
- **Asset duplication**: Same images stored in multiple locations
- **Difficult maintenance**: No clear way to identify image usage or content

## Recommended New Structure

```
/Users/joelgullo/dev/Cline/latex-beamer/
├── src/
│   ├── cs12/
│   │   ├── slides/
│   │   │   ├── 01_intro_ai.tex
│   │   │   ├── 02_place_based_learning.tex
│   │   │   ├── 03_arrays_intro.tex
│   │   │   ├── 04_big_o_notation.tex
│   │   │   ├── 05_sorting_algorithms.tex
│   │   │   ├── 06_search_algorithms.tex
│   │   │   ├── 07_2d_arrays.tex
│   │   │   ├── 08_strings_ciphers.tex
│   │   │   └── 09_prompt_engineering.tex
│   │   └── images/
│   │       ├── cs12-ai-methodology.png
│   │       ├── cs12-ai-machine_learning.png
│   │       ├── cs12-place-maori_astronomy.png
│   │       ├── cs12-big_o-complexity_chart.png
│   │       ├── cs12-arrays-search_visualization.png
│   │       └── cs12-prompt-anthropic_console.png
│   │
│   ├── phys11/
│   │   ├── slides/
│   │   │   ├── ch01_kinematics_review.tex
│   │   │   ├── ch03_dynamics.tex
│   │   │   ├── ch04_forces_fbd.tex
│   │   │   ├── ch05_vectors_trigonometry.tex
│   │   │   ├── ch06_circular_motion.tex
│   │   │   ├── ch08_thermodynamics.tex
│   │   │   ├── ch09_simple_machines.tex
│   │   │   ├── ch11_waves.tex
│   │   │   ├── ch12_sound.tex
│   │   │   ├── ch13_electricity_basics.tex
│   │   │   ├── ch18_circuits.tex
│   │   │   └── ch19_magnetism.tex
│   │   └── images/
│   │       ├── phys11-mechanics-inclined_plane.png
│   │       ├── phys11-mechanics-pulley_system.png
│   │       ├── phys11-forces-free_body_diagram.png
│   │       ├── phys11-thermal-temperature_scales.jpg
│   │       ├── phys11-circuits-series_resistors.png
│   │       ├── phys11-circuits-parallel_resistors.png
│   │       ├── phys11-waves-open_tube.png
│   │       └── phys11-waves-beat_frequency.png
│   │
│   └── phys12/
│       ├── slides/
│       │   ├── ch03_vectors_advanced.tex
│       │   ├── ch04_projectile_motion.tex
│       │   ├── ch05_dynamics_advanced.tex
│       │   ├── ch06_circular_planetary.tex
│       │   ├── ch07_energy_momentum.tex
│       │   ├── ch08_rotational_motion.tex
│       │   ├── ch09_gravitation.tex
│       │   ├── ch18_electric_fields.tex
│       │   ├── ch19_electric_potential.tex
│       │   ├── ch20_current_resistance.tex
│       │   ├── ch22_magnetism.tex
│       │   └── ch23_electromagnetic_induction.tex
│       └── images/
│           ├── phys12-gravity-planetary_motion.png
│           ├── phys12-electricity-point_charges.png
│           ├── phys12-circuits-kirchhoff_loops.jpg
│           ├── phys12-magnetism-right_hand_rule.png
│           ├── phys12-magnetism-electromagnetic_induction.png
│           └── phys12-astronomy-kepler_laws.png
│
├── shared/
│   ├── images/
│   │   ├── cinec_logo.png
│   │   ├── common-trigonometry-sohcahtoa.png
│   │   ├── common-trigonometry-sine_cosine_law.png
│   │   └── common-compass-directions.png
│   └── templates/
│       └── beamer_template.tex
│
├── archive/
│   ├── original_zips/
│   │   ├── -latex-Computer Science 12.zip
│   │   ├── PHYS11 CH.zip
│   │   └── Phys12 CH.zip
│   └── extracted_originals/
│       ├── Computer-Science-12/
│       ├── PHYS11-CH/
│       └── Phys12-CH/
│
└── docs/
    ├── computer-science-12-contents.md
    ├── physics-11-contents.md
    ├── physics-12-contents.md
    ├── suggested-restructuring.md
    └── image-workflow.md
```

## Benefits of New Structure

### Organization Benefits
- **Consistent naming**: All courses use lowercase, clear identifiers
- **Separation of concerns**: LaTeX files separate from images
- **Shared resources**: Common assets centralized to avoid duplication
- **Scalable**: Easy to add new courses or topics
- **Archive preservation**: Original files preserved for reference

### Maintenance Benefits
- **Clear file purposes**: Descriptive names make content obvious
- **Easy navigation**: Logical hierarchy reduces search time
- **Version control friendly**: Better git diff and merge handling
- **Asset management**: Clear image ownership and usage tracking

## Implementation Steps

1. **Create new directory structure**
2. **Move and rename LaTeX files** with descriptive names
3. **Move and rename all images** using consistent naming convention
4. **Update LaTeX files** to use new image paths
5. **Create unified template** in `shared/templates/`
6. **Test compilation** of all presentations
7. **Archive original structure** for backup

## File Naming Conventions

### LaTeX Files
- Format: `{number}_{topic_description}.tex`
- Examples: `01_intro_ai.tex`, `ch04_forces_fbd.tex`

### Image Files
- Format: `{course}-{topic}-{description}.{ext}`
- Examples: `cs12-ai-methodology.png`, `phys11-circuits-series_resistors.png`

### Shared Resources
- Format: `{category}-{description}.{ext}`
- Examples: `common-trigonometry-sohcahtoa.png`, `cinec_logo.png`

## Next Steps

1. Run implementation using Claude Code tools
2. Update all LaTeX `\includegraphics{}` references
3. Test compilation of sample presentations
4. Document any LaTeX package requirements
5. Create workflow for adding new content