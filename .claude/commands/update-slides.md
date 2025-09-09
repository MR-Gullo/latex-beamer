---
description: Update LaTeX Beamer slides with ESL-friendly improvements using chapter content
argument-hint: <tex_file_path> [chapter_numbers]
allowed-tools: TodoWrite, Read, Edit, MultiEdit, Write, Bash, Glob, Grep
---

# Update LaTeX Beamer Slides

I need to update the LaTeX Beamer presentation at `$1` using the following approach:

## Target Information

**File:** `$1`  
**Chapters:** `$2` (if provided)

## Implementation Instructions

If chapters are provided (`$2`), use this exact command pattern:
- For Physics files: `use 'docs/latex_beamer-updater.txt' as the prompt with chapters $2 in @docs/PHYS11-Chapters/ (or PHYS12-Chapters) as the context to update $1`
- For CS12 files: `use 'docs/latex_beamer-updater.txt' as the prompt with general programming concepts to update $1`

If no chapters provided, auto-detect from filename:
- Extract course type from path (phys11, phys12, cs12)  
- Parse chapter numbers from patterns like `ch01-03` → chapters 1,2,3

## Process Steps

1. **Create backup** with timestamp
2. **Read current LaTeX file** at `$1`  
3. **Read updater template** at `docs/latex_beamer-updater.txt`
4. **Gather chapter content** using Gemini CLI:
   - For **phys11**: Use `@docs/PHYS11-Chapters/[N]*.pdf` files
   - For **phys12**: Use `@docs/PHYS12-Chapters/[N]*.pdf` files  
   - For **cs12**: Use general programming concepts
5. **Apply ESL improvements** while preserving:
   - All image references and figure environments
   - Mathematical equations and formatting
   - Academic terminology and rigor
   - Theme and formatting consistency
6. **Test compilation** with pdflatex to ensure correctness

## Auto-Detection Logic

- **Course detection**: Extract from file path (phys11/phys12/cs12)
- **Chapter detection**: Parse filename patterns:
  - `ch01-03` → chapters 1,2,3
  - `ch04` → chapter 4
  - `ch10-12` → chapters 10,11,12

## ESL-Friendly Improvements

- Break down complex sentences into shorter, clearer statements
- Add bullet points and numbered lists for better organization
- Use consistent terminology throughout
- Add brief definitions or explanations for technical terms
- Improve step-by-step explanations in problem-solving sections
- Add connecting phrases and transitions between ideas
- Include summary points at the end of complex concepts

## Quality Assurance

- Preserve ALL existing content, images, and references
- Maintain mathematical accuracy and proper LaTeX formatting
- Ensure the updated document compiles successfully
- Verify ESL improvements don't sacrifice academic standards