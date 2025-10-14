---
description: Update CS12 LaTeX Beamer slides using lesson-specific documentation
argument-hint: <tex_file_path>
allowed-tools: TodoWrite, Read, Edit, MultiEdit, Create, Execute, Glob, Grep, LS
---

# Update CS12 Slides

I need to update the Computer Science 12 LaTeX Beamer presentation at `$ARGUMENTS` using lesson-specific documentation from the course folder.

## Process

1. **Extract lesson number** from the .tex filename (e.g., `05_truth-tables.tex` → lesson 05)
2. **Read the base prompt** from `/Users/joelgullo/dev/latex-beamer/src/cs12/slides/00prompt-latex-beamer-v8MACS12.md`
3. **Locate lesson folder** in `/Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/{lesson}_*/`
4. **Scan and filter content** - include main PDFs, student templates, demo programs; exclude solutions and archives
5. **Extract demo programs** from `lessonPrograms/` folder for instructor reference
6. **Read all relevant files** (PDFs, templates, source code) while filtering out solutions
7. **Apply updates** following the prompt guidelines while:
   - Adding instructor notes with demo program list
   - Referencing student assignment templates
   - Including submission instructions
   - Excluding all answer keys and solutions
   - Creating code templates with TODOs (not full solutions)
8. **Ensure compilation success** by following LaTeX formatting guidelines

## Implementation Steps

### Step 1: Parse the filename
- Extract lesson number from filepath (e.g., `05_truth-tables.tex` → `05`)
- Handle both single digit and zero-padded formats

### Step 2: Find the corresponding lesson folder
- Base path: `/Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons/`
- Try patterns in order:
  1. Exact match: `{lesson}_*/` (e.g., `05_*`)
  2. Next lesson: `{lesson+1}_*/` (e.g., `06_*` for lesson 05)
  3. Previous lesson: `{lesson-1}_*/` (e.g., `04_*` for lesson 05)
- Note: Lesson numbers may not align exactly with folder numbers

### Step 3: Read configuration files
- Base prompt: `/Users/joelgullo/dev/latex-beamer/src/cs12/slides/00prompt-latex-beamer-v8MACS12.md`
- Current .tex file: `$ARGUMENTS`

### Step 4: Scan lesson folder with filtering

**INCLUDE:**
- Main lesson PDFs/PPTXs in root folder
- Student template files (*.pdf, *.xlsx)
- Markdown documentation (*.md)
- Demo programs: `lessonPrograms/*.cpp` (source code only)

**EXCLUDE (CRITICAL - Do not include these in presentation):**
- `**/lessonSolutions/**` - Contains answer keys
- `**/exerciseSolutions/**` - Contains answer keys
- `**/*Solution*/**` - Any folder with "Solution" in name
- `**/*solution*/**` - Any folder with "solution" in name
- `**/Archive/**` - Historical content
- `**/*.exe` - Compiled binaries
- `**/*.o` - Object files

### Step 5: Extract and organize content

Use Python with PyPDF2 to extract text from PDFs:

```python
import PyPDF2
# Extract text from main lesson PDFs
# List demo programs from lessonPrograms/
# Identify student template files
```

### Step 6: Generate instructor notes section

Create a dedicated frame for instructor reference:

```latex
\section{Instructor Notes}

\begin{frame}
\frametitle{Demo Programs for This Lesson}
\textbf{Programs to demonstrate live:}
\begin{itemize}
    \item \texttt{programName.cpp} - Brief description
    \item \texttt{anotherProgram.cpp} - Brief description
\end{itemize}

\vspace{0.3cm}
\textbf{Location:} \texttt{lessonPrograms/}

\vspace{0.3cm}
\alert{Note:} These are for instructor demonstration only.
\end{frame}
```

### Step 7: Apply updates to presentation

Following the base prompt guidelines:

**Content Requirements:**
- Learning objectives slide
- Key concepts and definitions
- Code template exercises with TODO comments (NOT full solutions)
- Student assignment frame with template references
- Submission instructions with naming format
- Concept visualizations with `\alert{[description]}` placeholders

**Technical Requirements:**
- Use DS9 theme: `\usepackage{../../../shared/templates/ds9_theme}`
- Title format: `\title[Short Title]{CS12 CH: Topic}`
- Use `[fragile]` frames for all code blocks
- Follow C++ conventions: `using namespace std;`, no `std::` prefixes
- Escape special characters: `\_`, `\%`, `\&`
- Strategic `\pause` commands for flow

**Academic Integrity:**
- Reference demo programs by filename only
- Create templates with TODO comments
- Do NOT include solution code in slides
- Reference student templates, don't embed them

## Special Handling

### For Excel-Based Lessons (e.g., Truth Tables)
- Extract instructions from main PDF
- List Excel formulas and functions
- Include conditional formatting steps
- Reference Excel template file for students
- Use `\alert{[Screenshot of Excel interface]}` for visuals

### For C++ Programming Lessons
- List demo programs in instructor notes
- Create code templates with `// TODO:` comments
- Show expected output examples (not implementation)
- Include compilation notes if relevant
- Example template structure:
```cpp
#include <iostream>
using namespace std;

int main() {
    // TODO 1: Declare variables
    
    // TODO 2: Get user input
    
    // TODO 3: Process and display result
    
    return 0;
}
```

### For Multi-Part Lessons
- Check adjacent lesson folders for related content
- Cross-reference related topics in different folders

## Key Requirements

- **NEVER include solution code** from `*Solutions/` folders
- **ALWAYS filter out** answer keys and completed exercises
- **DO list** demo programs for instructor reference
- **DO reference** student template files by name
- **DO include** submission format instructions
- **Follow DS9 theme** and formatting guidelines
- **Use TODO comments** for student exercises, not complete solutions
- **Ensure LaTeX compiles** without errors

## Example Usage

```
/update-cs12-slides /Users/joelgullo/dev/latex-beamer/src/cs12/slides/05_truth-tables.tex
```

This will:
1. Extract lesson number: `05`
2. Find lesson folder: `06_TruthTables/` (one number off)
3. Read prompt: `00prompt-latex-beamer-v8MACS12.md`
4. Scan folder:
   - ✅ Include: `makingTruthTablesInExcel.pdf`
   - ✅ Include: `student-truth-tables-template.pdf`
   - ✅ Include: `truthTables.xlsx`
   - ❌ Exclude: `Archive/` folder
5. Extract PDF content about truth tables
6. Generate instructor notes (if demo programs exist)
7. Update presentation with:
   - Truth table operators and explanations
   - Excel formula instructions
   - Assignment frame: "Submit `firstnameLastname_truthtables.xlsx`"
   - No answer keys from Archive

## Validation Checklist

Before completing, verify:
- [ ] Correct lesson folder identified and scanned
- [ ] All solution/answer folders excluded
- [ ] Demo programs listed in instructor notes (if applicable)
- [ ] Student templates referenced by filename
- [ ] Submission instructions included
- [ ] DS9 theme properly applied
- [ ] All code blocks have `[fragile]` frames
- [ ] C++ code uses `using namespace std;`
- [ ] Special characters properly escaped
- [ ] LaTeX compiles without errors
- [ ] NO solution code visible in presentation
- [ ] Academic integrity maintained
