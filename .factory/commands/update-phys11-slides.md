---
description: Update Physics 11 LaTeX Beamer slides using chapter-specific documentation
argument-hint: <tex_file_path>
allowed-tools: TodoWrite, Read, Edit, MultiEdit, Create, Execute, Glob, Grep, LS
---

# Update Physics 11 Slides

I need to update the Physics 11 LaTeX Beamer presentation at `$ARGUMENTS` using chapter-specific documentation.

## Process

1. **Extract chapter number** from the .tex filename (e.g., `ch04_slides_forces-fbd.tex` → chapter 04)
2. **Read the updater prompt** from `/Users/joelgullo/dev/latex-beamer/00_Updater-prompt-latex-beamer-v7.md`
3. **Locate chapter docs** in `/Users/joelgullo/dev/latex-beamer/docs/PHYS11-Chapters/{chapter}CH-*/` (e.g., `04CH-forces-and-newtons-laws/`)
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
- Pattern: `/Users/joelgullo/dev/latex-beamer/docs/PHYS11-Chapters/{chapter}CH-*/`
- Example: For chapter 04, find `04CH-forces-and-newtons-laws/`

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
- **Include progression** context where applicable
- **List excluded sections** as reading homework before summary

## Example Usage

```
/update-phys11-slides /Users/joelgullo/dev/latex-beamer/src/phys11/slides/ch04_slides_forces-fbd.tex
```

This will:
1. Extract chapter number: `04`
2. Find docs in: `/Users/joelgullo/dev/latex-beamer/docs/PHYS11-Chapters/04CH-forces-and-newtons-laws/`
3. Read all PDFs and markdown files in that folder
4. Update the .tex file using the v7 prompt guidelines
