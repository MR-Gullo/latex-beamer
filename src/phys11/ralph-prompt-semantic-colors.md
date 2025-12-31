# Ralph Prompt: Semantic Color Mapping for Physics Equations

## Pre-Flight Checklist
- [ ] Git status clean
- [ ] pdflatex compiles test file without errors
- [ ] Recovery plan: `git checkout -- slidesv3/U05-Slides-CH12-PHYS11-Thermodynamics-color-test.tex`

## Goal
Add semantic color mapping to LaTeX Beamer physics slides: color-code equation symbols AND descriptive text to match physical meaning (P=blue, V=green, T=red, etc).

## Success Criteria
- [ ] Test file compiles with pdflatex without errors
- [ ] Ideal Gas Law frame (PV=NkT) has colored symbols matching their physical meaning
- [ ] Where list (P, V, N, k, T definitions) has matching colors in both symbols AND words
- [ ] Colors are visible and distinguishable in PDF output
- [ ] Semantic macros defined (not raw \textcolor everywhere)

## Color Schema (Sensible Defaults)
| Concept | Symbol | Color | Hex Approx |
|---------|--------|-------|------------|
| Pressure | P | Blue | #0066CC |
| Volume | V | Green | #00AA66 |
| Particles/Count | N | Purple | #8800AA |
| Boltzmann/Constant | k | Orange | #CC6600 |
| Temperature | T | Red | #CC0000 |
| Energy/Work | W, U, Q | Gold | #AA8800 |
| Entropy | S | Magenta | #CC00AA |
| Force | F | Teal | #008888 |
| Area | A | Brown | #886644 |

## Constraints
- Only modify the test file initially (not the full thermodynamics file yet)
- Keep only ONE frame for testing: the Ideal Gas Law frame (PV=NkT)
- Define semantic macros like `\pressure{P}` not raw `\textcolor{blue}{P}`
- Color both the equation symbols AND the descriptive text (e.g., "pressure (Pa)" should have "pressure" and "P" in same color)
- Must work with existing ds9_theme beamer template
- Do NOT modify shared theme files

## Phase 1: Single Frame Test

### Target Frame (lines 242-267)
```latex
\begin{frame}
\frametitle{12.2 The Ideal Gas Law}
\begin{block}{Universal Law: Gas Behavior}
\begin{center}
\Large $\boxed{PV = NkT}$
\end{center}
Pressure times volume equals particles times Boltzmann constant times absolute temperature.
\end{block}

\pause
\vspace{0.3cm}

Where:
\begin{itemize}
\item $P$ = pressure (Pa)
\item $V$ = volume (m$^3$)
\item $N$ = number of particles
\item $k = 1.38 \times 10^{-23}$ J/K (Boltzmann constant)
\item $T$ = absolute temperature (K)
\end{itemize}
\note{...}
\end{frame}
```

### Implementation Steps

1. **Strip file to single frame** - Remove all content except preamble, document structure, and the Ideal Gas Law frame

2. **Add color packages and macros** - In preamble after `\usepackage`:
```latex
\usepackage{xcolor}

% Semantic Physics Colors
\definecolor{pressureColor}{RGB}{0,102,204}
\definecolor{volumeColor}{RGB}{0,170,102}
\definecolor{particleColor}{RGB}{136,0,170}
\definecolor{constantColor}{RGB}{204,102,0}
\definecolor{tempColor}{RGB}{204,0,0}

% Semantic Macros
\newcommand{\pressure}[1]{\textcolor{pressureColor}{#1}}
\newcommand{\volume}[1]{\textcolor{volumeColor}{#1}}
\newcommand{\particles}[1]{\textcolor{particleColor}{#1}}
\newcommand{\constant}[1]{\textcolor{constantColor}{#1}}
\newcommand{\temp}[1]{\textcolor{tempColor}{#1}}
```

3. **Apply to equation** - Replace `$\boxed{PV = NkT}$` with semantic version:
```latex
$\boxed{\pressure{P}\volume{V} = \particles{N}\constant{k}\temp{T}}$
```

4. **Apply to text** - Color descriptive words:
```latex
\pressure{Pressure} times \volume{volume} equals \particles{particles} times \constant{Boltzmann constant} times \temp{absolute temperature}.
```

5. **Apply to list items** - Both symbol and word:
```latex
\item $\pressure{P}$ = \pressure{pressure} (Pa)
\item $\volume{V}$ = \volume{volume} (m$^3$)
\item $\particles{N}$ = \particles{number of particles}
\item $\constant{k} = 1.38 \times 10^{-23}$ J/K (\constant{Boltzmann constant})
\item $\temp{T}$ = \temp{absolute temperature} (K)
```

6. **Compile and verify** - Run pdflatex, check output

## Iteration Strategy

### Escalating Intensity
- **Iterations 1-3:** Set up color macros, strip file to single frame, apply basic coloring
- **Iterations 4-6:** Refine colors for visibility, ensure math mode compatibility
- **Iterations 7-9:** If compile fails, debug LaTeX errors, adjust syntax
- **Iteration 10:** Output compiled PDF or error dump

### Per-Iteration Cycle (Rigid)
1. READ: Check current state of test file
2. PLAN: Identify next color/macro to add
3. ACT: Make focused edit
4. TEST: Run `pdflatex U05-Slides-CH12-PHYS11-Thermodynamics-color-test.tex`
5. COMMIT: Checkpoint if compiles

### Stall Recovery
If pdflatex fails:
1. Check error message for line number
2. Ensure math mode brackets balanced
3. Verify color definitions before usage
4. If still stuck: simplify - try one color at a time

## Completion Promise
When test file:
- Compiles without errors
- Contains only the Ideal Gas Law frame
- Has all 5 variables (P,V,N,k,T) semantically colored
- Has matching colors in equation AND text

```
<promise>PHASE 1 COMPLETE - SINGLE FRAME TEST SUCCESSFUL</promise>
```

## Phase 2 (Future - After Phase 1 Approval)
- Expand to all equation frames in thermodynamics file
- Add more semantic colors for other physics concepts

## Phase 3 (Future - After Phase 2 Approval)
- Update beamer-physics skill to include semantic coloring
- Make it always-enabled default behavior

## Anti-Patterns (Critical)
- Never apply colors before defining macros
- Never use raw `\textcolor` - always use semantic macros
- Never modify shared theme files
- Never skip the compile test step
