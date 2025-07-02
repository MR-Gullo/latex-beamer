# LaTeX Beamer Slideshow Organization Configuration

## Core Gemini CLI Integration

When analyzing LaTeX Beamer slideshows, image dependencies, or planning slideshow restructuring, use Gemini CLI to save Claude Code tokens. Use `gemini -p` to leverage Google Gemini's massive context window for analysis, then return to Claude Code for precise execution.

## File and Directory Inclusion Syntax for LaTeX Projects

Use the `@` syntax to include files and directories in Gemini prompts:

```bash
# Single LaTeX file analysis
gemini -p "@slideshow.tex Analyze this Beamer presentation structure and image dependencies"

# Multiple slideshow files
gemini -p "@CH1.tex @CH2.tex Analyze the consistency between these chapter presentations"

# Entire course directory
gemini -p "@Computer-Science-12/ Summarize the slideshow architecture of this course"

# Multiple course directories
gemini -p "@PHYS11-CH/ @Phys12-CH/ Analyze image usage patterns across physics courses"

# Current directory and subdirectories
gemini -p "@./ Give me an overview of this entire LaTeX Beamer project"

# All files flag for comprehensive analysis
gemini --all_files -p "Analyze the complete slideshow project structure and image dependencies"
```

## LaTeX Beamer Analysis Use Cases

### Slideshow Structure Analysis

```bash
# Architecture overview
gemini -p "@Computer-Science-12/ @PHYS11-CH/ @Phys12-CH/ Analyze slideshow organization patterns and suggest unified structure"

# Image dependency analysis
gemini -p "@./ Analyze all image references in LaTeX files and identify missing or unused images"

# Content consistency review
gemini -p "@**/CH*.tex Review content structure and identify inconsistencies across chapters"

# Template usage analysis
gemini -p "@**/*template*.tex Analyze template usage patterns and suggest standardization"
```

### Image Workflow Analysis

```bash
# Image organization review
gemini -p "@**/*.png @**/*.jpg @**/*.gif Analyze image organization and suggest better directory structure"

# LaTeX image reference patterns
gemini -p "@**/*.tex Extract all image references and analyze naming conventions"

# Missing image detection
gemini -p "@./ Identify LaTeX files with broken image references"

# Image format optimization
gemini -p "@**/*.{png,jpg,gif} Analyze image formats and suggest optimization opportunities"
```

### Cross-Course Analysis

```bash
# Content integration analysis
gemini -p "@Computer-Science-12/ @PHYS11-CH/ @Phys12-CH/ Analyze shared concepts and suggest cross-references"

# Resource sharing opportunities
gemini -p "@./ Identify images and content that could be shared across courses"

# Template standardization
gemini -p "@**/template*.tex Analyze template variations and suggest unified approach"
```

## When to Use Gemini CLI for LaTeX Projects

**Always use `gemini -p` when:**

- Analyzing entire slideshow collections or course directories
- Comparing multiple LaTeX files for consistency
- Understanding project-wide image usage patterns
- Current context window is insufficient for analyzing all files
- Working with files totaling more than 50KB
- Planning major slideshow reorganization
- Cross-referencing content across multiple courses
- Analyzing image dependencies and broken references

**Let Claude Code handle:**

- Actual LaTeX file modifications and edits
- Moving and organizing image files
- Creating new directory structures
- Git operations for version control
- Installing LaTeX packages and dependencies
- Precise syntax corrections in LaTeX files

## Token Efficiency Strategy for LaTeX Projects

1. **Use Gemini first** for analyzing slideshow structure, image patterns, and reorganization planning
2. **Use Claude Code second** for implementing file moves, edits, and directory restructuring
3. **Combine when needed**: Gemini for analysis → Claude Code for execution → Gemini for review
4. **Save Claude tokens** for tasks requiring precise file operations and LaTeX compilation

## Manual Trigger Commands for LaTeX Analysis

```bash
# Quick slideshow analysis
gemini -p "@current_slideshow.tex Analyze this Beamer presentation structure and suggest improvements"

# Comprehensive project review
gemini -p "@./ Analyze entire LaTeX Beamer project including structure, images, and organization suggestions"

# Image workflow analysis
gemini -p "@./ Analyze all image usage patterns and suggest unified image management workflow"

# Cross-course consistency check
gemini -p "@Computer-Science-12/ @PHYS11-CH/ @Phys12-CH/ Analyze consistency across all three course collections"
```

## Important Notes for LaTeX Projects

- Gemini CLI paths are relative to your current working directory
- Use `--all_files` flag for comprehensive LaTeX project analysis
- Be specific about image formats and directory patterns
- Gemini excels at pattern analysis, Claude Code excels at file operations
- When analyzing LaTeX files, specify if you want content analysis or structural analysis
- Always check for broken image references before reorganizing

# File Naming Conventions

To ensure consistency and proper sorting in file explorers, all new files created in this project should adhere to the following naming conventions.

## General Structure

The general format for file names is:

`prefix_descriptive-name.extension`

- **prefix:** A short code to indicate the file's order or type.
- **descriptive-name:** A clear, hyphen-separated name in lowercase.
- **extension:** The file's extension (e.g., `.tex`, `.md`, `.png`).

## Prefixes

### Numeric Prefixes

For files that have a specific sequence, such as chapters, lessons, or steps, use a two-digit numeric prefix.

**Format:** `NN_descriptive-name.ext`

**Examples:**

- `01_introduction.tex`
- `02_main-concepts.md`
- `12_final-project.tex`

### Type Prefixes

For files that serve a specific purpose, use a type prefix.

**Format:** `type_descriptive-name.ext`

**Common Prefixes:**

- `lib_`: For library or module files.
- `util_`: For utility scripts or helper functions.
- `config_`: For configuration files.
- `test_`: For test files.
- `img_`: For image files.
- `doc_`: For documentation.

**Examples:**

- `util_image-converter.py`
- `config_latex-settings.json`
- `img_main-diagram.png`

## Naming Guidelines

- **Use lowercase:** `my-file.tex` instead of `My-File.tex`.
- **Use hyphens for separators:** `descriptive-name-in-lowercase.md` instead of `descriptivename.md` or `descriptive_name.md`.
- **Be descriptive:** Choose names that clearly indicate the file's content or purpose.

# LaTeX Beamer Image Reference Standards

## Image Path Configuration

All LaTeX Beamer presentations must define image search paths in the document preamble:

```latex
\graphicspath{{../images/}{../../shared/images/}}
```

**Standard:** Use relative paths from slide location to maintain portability across course directories.

## Image Reference Format

### Basic Pattern

```latex
\includegraphics[width=0.5\linewidth]{filename.png}
```

### Complete Reference Examples

**Single image with caption:**

```latex
\begin{figure}
    \centering
    \includegraphics[width=0.6\linewidth]{cs12-ai-methodology.png}
    \caption*{XKCD \#2451: AI Methodology}
\end{figure}
```

**Image in columns layout:**

```latex
\includegraphics[width=0.8\linewidth]{cs12-ai-machine_learning.png}
```

**Large standalone image:**

```latex
\includegraphics[width=8cm]{cs12-llm-student_interaction_styles.png}
```

## Image Naming Convention

**Format:** `course-topic-description.extension`

**Examples:**

- `cs12-ai-methodology.png`
- `cs12-llm-student_interaction_styles.png`
- `phys11-waves-interference.jpg`
- `phys12-quantum-uncertainty.png`

## Image Reference Checklist

Before committing any LaTeX file with image references:

- [ ] **File exists:** Image file present in `../images/` or `../../shared/images/`
- [ ] **Naming convention:** Follows `course-topic-description.extension` pattern
- [ ] **Width parameter:** Appropriate for layout context (`\linewidth`, `\textwidth`, or absolute units)
- [ ] **Figure environment:** Used when centering or captioning required
- [ ] **Attribution:** Included when required (copyright, Creative Commons, etc.)
- [ ] **Accessibility:** Caption or alt-text provided for screen readers when applicable

## Width Guidelines

- **Single column images:** `width=0.5\linewidth` to `width=0.8\linewidth`
- **Column layout images:** `width=0.6\linewidth` to `width=0.9\linewidth`
- **Full-width images:** `width=\textwidth` or absolute units like `8cm`
- **Small icons/diagrams:** `width=3cm` to `width=5cm`

## Attribution Standards

When using third-party images, include attribution:

```latex
{\tiny Images from xkcd.com by Randall Munroe, used under CC BY-NC license}
```

Place attribution below figure or at slide bottom.
