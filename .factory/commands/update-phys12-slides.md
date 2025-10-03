---
description: Update Physics 12 LaTeX Beamer slides using chapter-specific documentation
argument-hint: <tex_file_path>
allowed-tools: TodoWrite, Read, Edit, MultiEdit, Create, Execute, Glob, Grep, LS
---

# Update Physics 12 Slides

I need to update the Physics 12 LaTeX Beamer presentation at `$ARGUMENTS` using chapter-specific documentation.

## Process

1. **Extract chapter number** from the .tex filename (e.g., `ch04_slides_motion.tex` → chapter 04)
2. **Read the updater prompt** from `/Users/joelgullo/dev/latex-beamer/00_Updater-prompt-latex-beamer-v7.md`
3. **Locate chapter docs** in `/Users/joelgullo/dev/latex-beamer/docs/PHYS12-Chapters/{chapter}CH-*/` (e.g., `04CH-dynamics/`)
4. **Read all PDF and markdown files** in the chapter folder to gather context
5. **Read the current .tex file** to understand existing structure and image references
6. **Apply updates** following the prompt guidelines while preserving:
   - All image references and figure environments
   - Mathematical equations and formatting
   - Theme and formatting consistency
   - Academic rigor
7. **Add ESL-friendly improvements** as specified in the prompt
8. **Ensure compilation success** by following LaTeX formatting guidelines

## Implementation Steps

### Step 1: Parse the filename
- Extract chapter number from the filepath (e.g., `ch04` → `04`)

### Step 2: Find the corresponding docs folder
- Pattern: `/Users/joelgullo/dev/latex-beamer/docs/PHYS12-Chapters/{chapter}CH-*/`
- Example: For chapter 04, find `04CH-dynamics/`

### Step 3: Read all relevant files
- Updater prompt: `/Users/joelgullo/dev/latex-beamer/00_Updater-prompt-latex-beamer-v7.md`
- All files in the chapter folder: `{chapter}CH-*/*.pdf`, `{chapter}CH-*/*.md`
- Current .tex file: `$ARGUMENTS`

### Step 4: Apply updates
- Use the prompt as instructions
- Use chapter docs as context
- Use current .tex as the base to update
- Maintain all existing image references
- Follow GUESS method for examples
- Add ESL improvements
- Ensure proper LaTeX formatting

## Key Requirements

- **NEVER remove image references** from the original presentation
- **Preserve all** `\begin{figure}...\end{figure}` blocks
- **Follow formatting guidelines** for titles, colors, and fragile frames
- **Use GUESS method** for problem-solving examples
- **Add strategic `\pause`** commands for flow
- **Include progression** from Physics 11 to Physics 12
- **List excluded sections** as reading homework before summary

## Example Usage

```
/update-phys12-slides /Users/joelgullo/dev/latex-beamer/src/phys12/slides/ch04_slides_motion.tex
```

This will:
1. Extract chapter number: `04`
2. Find docs in: `/Users/joelgullo/dev/latex-beamer/docs/PHYS12-Chapters/04CH-dynamics/`
3. Read all PDFs and markdown files in that folder
4. Update the .tex file using the v7 prompt guidelines
