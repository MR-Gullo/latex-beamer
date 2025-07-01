# Image Workflow for LaTeX Beamer Slideshows

This document outlines a comprehensive workflow for managing images in the LaTeX Beamer slideshow project, based on analysis of current image usage patterns and best practices.

## Current Image Issues

### Naming Problems

- **Cryptic hashes**: `02c4ce1d-fdd3-47cd-8a44-ce141f1a4c98.png`, `7ec7c64b0df75bdd50bcb08f0fcc54ef.png`
- **Generic names**: `image.png`, `Picture.png`, `screenshot.png`
- **Meaningless identifiers**: `th-1448775654.jpg`, `th-3125735322.jpg`, `th-2198955217.jpg`
- **Inconsistent formats**: Mix of descriptive and non-descriptive names

### Organization Problems

- **Mixed storage**: Images scattered in root directories with LaTeX files
- **Duplication**: `cinec_logo.png` exists in both physics courses
- **No categorization**: Physics diagrams mixed with screenshots and stock photos
- **Difficult maintenance**: No way to identify unused or broken image references

## Recommended Image Workflow

### 1. Image Naming Convention

Use the format: `{course}-{category}-{description}.{extension}`

#### Course Prefixes

- `cs12-` for Computer Science 12
- `phys11-` for Physics 11
- `phys12-` for Physics 12
- `common-` for shared resources

#### Category Guidelines

| Category      | Description                       | Examples                                  |
| ------------- | --------------------------------- | ----------------------------------------- |
| `ai`          | Artificial intelligence concepts  | `cs12-ai-methodology.png`                 |
| `algorithms`  | Algorithm visualizations          | `cs12-algorithms-bubble_sort.png`         |
| `data`        | Data structures                   | `cs12-data-array_visualization.png`       |
| `mechanics`   | Physics mechanics                 | `phys11-mechanics-inclined_plane.png`     |
| `circuits`    | Electrical circuits               | `phys11-circuits-series_resistors.png`    |
| `waves`       | Wave phenomena                    | `phys11-waves-sound_interference.png`     |
| `thermal`     | Thermodynamics                    | `phys11-thermal-heat_transfer.png`        |
| `magnetism`   | Magnetic fields                   | `phys12-magnetism-field_lines.png`        |
| `gravity`     | Gravitational concepts            | `phys12-gravity-orbital_motion.png`       |
| `lab`         | Laboratory equipment/setups       | `phys11-lab-pendulum_setup.png`           |
| `screenshots` | Problem examples from assignments | `phys11-screenshots-homework_example.png` |

### 2. Directory Structure

```
src/
├── cs12/images/
│   ├── cs12-ai-*.png
│   ├── cs12-algorithms-*.png
│   ├── cs12-data-*.png
│   └── cs12-programming-*.png
│
├── phys11/images/
│   ├── phys11-mechanics-*.png
│   ├── phys11-circuits-*.png
│   ├── phys11-waves-*.png
│   ├── phys11-thermal-*.png
│   └── phys11-screenshots-*.png
│
├── phys12/images/
│   ├── phys12-mechanics-*.png
│   ├── phys12-electricity-*.png
│   ├── phys12-magnetism-*.png
│   ├── phys12-gravity-*.png
│   └── phys12-screenshots-*.png
│
└── shared/images/
    ├── cinec_logo.png
    ├── common-trigonometry-*.png
    └── common-navigation-*.png
```

### 3. LaTeX Integration

#### Template Configuration

Add to `shared/templates/beamer_template.tex`:

```latex
% Image path configuration
\graphicspath{{../images/}{../shared/images/}}

% Consistent image sizing commands
\newcommand{\slideimage}[2][0.8]{\includegraphics[width=#1\textwidth]{#2}}
\newcommand{\smallimage}[2][0.4]{\includegraphics[width=#1\textwidth]{#2}}
\newcommand{\fullimage}[1]{\includegraphics[width=\textwidth]{#1}}
```

#### Usage in Presentations

```latex
% Instead of complex paths, use clean names
\slideimage{phys11-circuits-series_resistors.png}
\smallimage[0.5]{cs12-ai-methodology.png}
\fullimage{phys12-gravity-kepler_laws.png}
```

### 4. Image Renaming Map

Based on current files, here's the mapping for key images:

#### Computer Science 12

| Current Name                                  | New Name                                   |
| --------------------------------------------- | ------------------------------------------ |
| `ai_methodology_2x.png`                       | `cs12-ai-methodology.png`                  |
| `machine_learning_2x.png`                     | `cs12-ai-machine_learning.png`             |
| `p06-maori-astronomy-3086117367.png`          | `cs12-culture-maori_astronomy.png`         |
| `Screenshot-2023-03-07-101704-3474888424.png` | `cs12-screenshots-code_example.png`        |
| `7ec7c64b0df75bdd50bcb08f0fcc54ef.png`        | `cs12-algorithms-search_visualization.png` |

#### Physics 11

| Current Name                                | New Name                                 |
| ------------------------------------------- | ---------------------------------------- |
| `InclinePlane.png`                          | `phys11-mechanics-inclined_plane.png`    |
| `Pulley.png`                                | `phys11-mechanics-pulley_system.png`     |
| `serres.png`                                | `phys11-circuits-series_resistors.png`   |
| `resparr.png`                               | `phys11-circuits-parallel_resistors.png` |
| `BEAT.png`                                  | `phys11-waves-beat_frequency.png`        |
| `opentube.png`                              | `phys11-waves-open_tube.png`             |
| `thermal-equilibrium-basics-1018696211.jpg` | `phys11-thermal-equilibrium.jpg`         |
| `sohcahtoa.png`                             | `common-trigonometry-sohcahtoa.png`      |

#### Physics 12

| Current Name              | New Name                                     |
| ------------------------- | -------------------------------------------- |
| `pointfields.png`         | `phys12-electricity-point_charge_fields.png` |
| `RHR1.png`                | `phys12-magnetism-right_hand_rule.png`       |
| `kepfirst.png`            | `phys12-gravity-kepler_first_law.png`        |
| `dischcurve.png`          | `phys12-circuits-capacitor_discharge.png`    |
| `junctionloopkirchov.jpg` | `phys12-circuits-kirchhoff_laws.jpg`         |

### 5. Image Quality Standards

#### File Formats

- **PNG**: Diagrams, screenshots, transparent backgrounds
- **JPG**: Photographs, complex images without transparency
- **GIF**: Animations (like `Corioliskraftanimation.gif`)

#### Resolution Guidelines

- **Presentation images**: 1920×1080 maximum for full-screen
- **Diagram elements**: 300 DPI for crisp rendering
- **File size**: Keep under 500KB per image when possible

#### Optimization

- Use descriptive alt text in LaTeX: `\includegraphics[alt={Series resistor circuit diagram}]{phys11-circuits-series_resistors.png}`
- Compress images appropriately for presentation use
- Remove unnecessary metadata from image files

### 6. Maintenance Workflow

#### Adding New Images

1. **Save with proper naming**: Follow `{course}-{category}-{description}.{ext}` format
2. **Place in correct directory**: Course-specific or shared as appropriate
3. **Document usage**: Note which presentation(s) use the image
4. **Test compilation**: Ensure LaTeX can find and render the image

#### Cleaning Up Existing Images

1. **Identify usage**: Search LaTeX files for `\includegraphics` references
2. **Rename systematically**: Use mapping table above
3. **Update LaTeX references**: Change all `\includegraphics{}` calls
4. **Remove duplicates**: Move shared images to `shared/images/`
5. **Archive unused**: Keep unused images in separate folder temporarily

#### Regular Maintenance

- **Monthly review**: Check for new unnamed screenshots or generic files
- **Broken link check**: Verify all image references work
- **Duplicate detection**: Look for similar images that could be consolidated
- **Size optimization**: Compress large images if needed

### 7. Implementation Steps

1. **Create new image directories** following the structure above
2. **Move and rename images** according to the naming convention
3. **Update LaTeX template** with `\graphicspath` configuration
4. **Update all presentations** to use new image names
5. **Test compilation** of all presentations
6. **Document any missing images** or broken references
7. **Create backup** of original image files

### 8. Benefits of New Workflow

- **Searchable**: Easy to find images by course and topic
- **Maintainable**: Clear ownership and usage tracking
- **Consistent**: Uniform naming across all courses
- **Scalable**: Easy to add new courses or image categories
- **Professional**: Clean, organized presentation assets
- **Collaborative**: Clear conventions for multiple contributors

This workflow will transform the current chaotic image management into a professional, maintainable system that supports efficient slideshow creation and maintenance.
