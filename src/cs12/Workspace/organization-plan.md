# CS12 LaTeX Beamer Organization Plan - ALIGNED WITH ACTUAL COURSE STRUCTURE

## Real Course Structure Analysis

Based on the actual lesson directory at `/Users/joelgullo/Library/CloudStorage/OneDrive-Personal/Documents/NANMO-2024/Courses/01-ComputerScience-12/Lessons`, the course follows this precise structure:

## **AUTHORITATIVE LESSON STRUCTURE** (From OneDrive Source)

### Core Programming Fundamentals (Lessons 1-11)
1. `01_GentleIntroductiontoC 1/` - **HAS CONTENT** - IDE setup, Hello World, C++ program structure
2. `02_IntegerDatatypes/` - **HAS CONTENT** - Comments, int, char, bool datatypes  
3. `03_floatsAndByteSize/` - **HAS CONTENT** - Float types, memory usage, type conversion
4. `04_NumberSystems/` - **HAS CONTENT** - Number systems, math libraries  
5. `05_RelationalExpressions/` - **HAS DIRECTORY**
6. `06_TruthTables/` - **HAS DIRECTORY**
7. `07_ElseIf/` - **HAS DIRECTORY**
8. `08_switchAndLoops/` - **HAS DIRECTORY**
9. `09_forLoops/` - **HAS DIRECTORY**
10. `09YTD_PopQuiz_1/` - **HAS DIRECTORY**
11. `10_problemSet/` - **HAS DIRECTORY**

### Functions and Advanced Control (Lessons 11-16)
11. `11_functions/` - **HAS DIRECTORY**
12. `12_Quiz/` - **HAS DIRECTORY**
13. `13_recursiveSequenceSeries/` - **HAS DIRECTORY**
14. `14_recursiveProgramming/` - **HAS DIRECTORY**
15. `15_scope/` - **HAS DIRECTORY**
16. `16_mysteryFunctionsQuiz/` - **HAS DIRECTORY**

### Arrays and Data Structures (Lessons 17-26)
17. `17_arrays/` - **HAS DIRECTORY**
18. `18_sortingAlgorithmsProject/` - **HAS DIRECTORY**
19. `18.5 Git Holiday Assignment/` - **HAS DIRECTORY**
20. `19_bigO/` - **HAS DIRECTORY**
21. `20_searchingArray/` - **HAS DIRECTORY**
22. `21_firstProjects/` - **HAS DIRECTORY**
23. `21.5_Prompt Engineering/` - **HAS DIRECTORY**
24. `22_2Darrays/` - **HAS DIRECTORY**
25. `23_2dArray_projects/` - **HAS DIRECTORY**
26. `24_strings/` - **HAS DIRECTORY**
27. `25_fileIO/` - **HAS DIRECTORY**
28. `25.6_VSCODE/` - **HAS DIRECTORY**
29. `26_WebDevProject/` - **HAS DIRECTORY** (Comprehensive web dev portfolio project)

### Specialized Short Courses (Lessons 39-40)
30. `39introduction_to_debugging_shortcourse-main/` - **HAS DIRECTORY**
31. `40debugging_with_vs_code_shortcourse-main/` - **HAS DIRECTORY**
32. `40git_github_in_depth_short_course-main/` - **HAS DIRECTORY**

## **MISMATCH ANALYSIS: Current Slides vs Real Course**

### **CORRECTLY NAMED FILES** (Match actual structure)
✅ `01_introduction-to-cpp.tex` - Maps to `01_GentleIntroductiontoC 1/`
✅ `02_integer-datatypes.tex` - Maps to `02_IntegerDatatypes/`  
✅ `03_floats-and-byte-size.tex` - Maps to `03_floatsAndByteSize/`
✅ `04_number-systems.tex` - Maps to `04_NumberSystems/`
✅ Various numbered lessons through 26 - Generally match directory structure

### **INCORRECTLY NAMED FILES** (Don't match real structure)
❌ `01_ai_literacy.tex` - **NOT PART OF CORE CS12 CURRICULUM** (Extra content?)
❌ `02_floats-memory-usage-cin.tex` - Should be integrated with lesson 3
❌ `03_number-systems-math-libraries.tex` - Should be integrated with lesson 4  
❌ `04_if-else.tex` - Topic not in lesson 4 (relational expressions come first)

### **DUPLICATE LESSON ISSUES** (Multiple files for same lesson)
- Lesson 2: `02_integer-datatypes.tex` ✅ vs `02_floats-memory-usage-cin.tex` ❌
- Lesson 3: `03_floats-and-byte-size.tex` ✅ vs `03_number-systems-math-libraries.tex` ❌
- Lesson 4: `04_number-systems.tex` ✅ vs `04_if-else.tex` ❌
- [Multiple other duplicates as identified earlier]

## Current LaTeX Implementation Status

### **CONTENT FILES** (Complete/Substantial Development)
1. `01_introduction-to-cpp.tex` - **COMPLETE** - Full intro lesson with IDE setup, Hello World, program structure (430 lines)
2. `01_ai_literacy.tex` - **COMPLETE** - AI literacy presentation with hallucinations, student patterns (433 lines)

### **TEMPLATE FILES** (Minimal/Placeholder Content)

#### Fundamentals (Lessons 2-11)
2. `02_integer-datatypes.tex` - **TEMPLATE** - Basic DS9 template with overview only
2. `02_floats-memory-usage-cin.tex` - **TEMPLATE** - Default theme, placeholder content
3. `03_floats-and-byte-size.tex` - **TEMPLATE** - DS9 template with overview only  
3. `03_number-systems-math-libraries.tex` - **TEMPLATE** - Default theme, placeholder content
4. `04_number-systems.tex` - **TEMPLATE** - DS9 template with overview only
4. `04_if-else.tex` - **TEMPLATE** - Default theme, placeholder content
5. `05_relational-expressions.tex` - **FILE NOT FOUND**
5. `05_truth-tables.tex` - **NEEDS ANALYSIS**
6. `06_truth-tables.tex` - **NEEDS ANALYSIS**  
6. `06_schoology-quiz-homework.tex` - **NEEDS ANALYSIS**
7. `07_else-if.tex` - **NEEDS ANALYSIS**
7. `07_if-elseif-else.tex` - **NEEDS ANALYSIS**
8. `08_switch-and-loops.tex` - **NEEDS ANALYSIS**
8. `08_switch-while.tex` - **NEEDS ANALYSIS**
8. `08_place_based_learning.tex` - **NEEDS ANALYSIS**
9. `09_for-loops.tex` - **NEEDS ANALYSIS**
9. `09_prompt_engineering.tex` - **NEEDS ANALYSIS**
10. `09ytd_pop-quiz-1.tex` - **NEEDS ANALYSIS**
10. `10_problem-set-1-loops.tex` - **NEEDS ANALYSIS**

#### Functions and Advanced Control (Lessons 11-16)
11. `11_functions.tex` - **NEEDS ANALYSIS**
11. `11_skill-milestone-term-1-keyboard.tex` - **NEEDS ANALYSIS**
12. `12_functions.tex` - **NEEDS ANALYSIS** (DUPLICATE)
12. `12_quiz.tex` - **NEEDS ANALYSIS**
13. `13_recursive-sequence-series.tex` - **NEEDS ANALYSIS**
13. `13_practice-problems-for-upcoming-reading-quiz.tex` - **NEEDS ANALYSIS**
14. `14_recursive-programming.tex` - **NEEDS ANALYSIS**
14. `14_recursion-sequence-series.tex` - **NEEDS ANALYSIS** (DUPLICATE)
15. `15_scope.tex` - **NEEDS ANALYSIS**
16. `16_mystery-functions-quiz.tex` - **NEEDS ANALYSIS**

#### Arrays and Data Structures (Lessons 17-26)
17. `17_arrays.tex` - **NEEDS ANALYSIS**
18. `18_sorting-algorithms-project.tex` - **NEEDS ANALYSIS**
18. `18_sorting-project.tex` - **NEEDS ANALYSIS** (DUPLICATE)
19. `18.5_git-holiday-assignment.tex` - **NEEDS ANALYSIS**
19. `19_big-o.tex` - **NEEDS ANALYSIS**
19. `19_big-o-introduction.tex` - **NEEDS ANALYSIS** (DUPLICATE)
20. `20_searching-array.tex` - **NEEDS ANALYSIS**
20. `20_sorting-algorithms.tex` - **NEEDS ANALYSIS** (DUPLICATE)
21. `21_first-projects.tex` - **NEEDS ANALYSIS**
21. `21_git-mastery-holiday-assignment.tex` - **NEEDS ANALYSIS** (DUPLICATE)
22. `21.5_prompt-engineering.tex` - **NEEDS ANALYSIS**
22. `22_2d-arrays.tex` - **NEEDS ANALYSIS**
22. `22_git-explore.tex` - **NEEDS ANALYSIS** (DUPLICATE)
23. `23_2d-array-projects.tex` - **NEEDS ANALYSIS**
23. `23_skill-milestone-term-2-keyboard.tex` - **NEEDS ANALYSIS** (DUPLICATE)
24. `24_strings.tex` - **NEEDS ANALYSIS**
24. `24_searching-arrays.tex` - **NEEDS ANALYSIS** (DUPLICATE)
25. `25_file-io.tex` - **NEEDS ANALYSIS**
25. `25_organizing-projects.tex` - **NEEDS ANALYSIS** (DUPLICATE)
26. `25.6_vscode.tex` - **NEEDS ANALYSIS**
26. `26_2d-array.tex` - **NEEDS ANALYSIS** (DUPLICATE)
26. `26_web-dev-project.tex` - **NEEDS ANALYSIS**
27. `27_strings.tex` - **NEEDS ANALYSIS** (DUPLICATE)

#### Specialized Topics (Lessons 39-40)
39. `39_introduction-to-debugging-shortcourse-main.tex` - **NEEDS ANALYSIS**
40. `40_debugging-with-vs-code-shortcourse-main.tex` - **NEEDS ANALYSIS**
40. `40_git-github-in-depth-short-course-main.tex` - **NEEDS ANALYSIS**

## Major Issues Identified

### **DUPLICATE FILE PROBLEM**
Multiple lessons have 2+ files with different naming conventions:
- `02_integer-datatypes.tex` vs `02_floats-memory-usage-cin.tex`
- `03_floats-and-byte-size.tex` vs `03_number-systems-math-libraries.tex`
- `04_number-systems.tex` vs `04_if-else.tex`
- `18_sorting-algorithms-project.tex` vs `18_sorting-project.tex`
- `19_big-o.tex` vs `19_big-o-introduction.tex`
- And many more...

### **THEME INCONSISTENCY**
- Content files use `../../../shared/templates/ds9_theme`
- Template files inconsistently use `DS9` theme vs `default`

### **DELETED FILE ISSUE**
- `01_gentle-introduction-to-c.tex` marked as DELETED in git status
- Should be renamed to match content: `01_introduction-to-cpp.tex`

## Course Structure Analysis

### Total Lesson Count
The course contains **40+ lessons** organized into distinct learning modules, significantly more comprehensive than initially catalogued.

### Content Development Priority
1. **High Priority**: Core programming fundamentals (lessons 1-11)
2. **Medium Priority**: Functions and control structures (lessons 11-16)
3. **Medium Priority**: Arrays and basic data structures (lessons 17-23)
4. **Low Priority**: Advanced topics and specialized courses (lessons 24-40+)

### Notable Course Features
- **Integrated Quizzes**: Pop quizzes and formal assessments throughout
- **Project-Based Learning**: Multiple hands-on projects (sorting, 2D arrays, web dev)
- **Modern Development Tools**: VS Code integration and debugging courses
- **Version Control**: Git and GitHub in-depth coverage
- **Contemporary Topics**: Prompt engineering integration

## LaTeX Configuration Needed

### Standard Setup for Each File
- Proper `\graphicspath` configuration for image references
- Consistent DS9 theme application
- Code syntax highlighting setup (listings or minted)
- Exercise and example frameworks
- Quiz and assessment templates

### Image Organization Strategy
- Create lesson-specific `images/` subdirectories
- Follow naming convention: `cs12-lesson-topic-description.png`
- Ensure all image paths use relative references
- Standardize code example screenshots

### Testing and Compilation Requirements
- Test compile all files with `pdflatex`
- Verify theme consistency across all 40+ presentations
- Check for proper LaTeX syntax and missing packages
- Validate code syntax highlighting works correctly

## File Management Strategy

### Current Status
- Course structure is more extensive than initially mapped
- Some lessons use decimal numbering (18.5, 21.5, 25.6)
- Specialized short courses integrated into main sequence
- Need to create LaTeX files for all identified lessons

## **CRITICAL ACTION ITEMS** - Fix Structure Alignment

### **1. File Consolidation Based on Real Course Structure**

**DELETE INCORRECT FILES** (Don't match real course):
```bash
# These files don't align with actual course structure
rm slides/02_floats-memory-usage-cin.tex  # Wrong lesson content
rm slides/03_number-systems-math-libraries.tex  # Wrong lesson content  
rm slides/04_if-else.tex  # Wrong lesson 4 content
# [Additional duplicates as identified]
```

**KEEP CORRECT FILES** (Match real course structure):
```bash
# These files align with actual OneDrive lesson structure
✅ slides/01_introduction-to-cpp.tex  # Maps to 01_GentleIntroductiontoC 1/
✅ slides/02_integer-datatypes.tex    # Maps to 02_IntegerDatatypes/  
✅ slides/03_floats-and-byte-size.tex # Maps to 03_floatsAndByteSize/
✅ slides/04_number-systems.tex       # Maps to 04_NumberSystems/
```

### **2. Content Alignment Priorities**

**HIGH PRIORITY** - Align with source content:
1. **Lesson 1**: `01_introduction-to-cpp.tex` ✅ (Already complete, matches source content)
2. **Lesson 2**: Expand `02_integer-datatypes.tex` template with content from `02_IntegerDatatypes/02_cpp_intDatatypes.md`
3. **Lesson 3**: Expand `03_floats-and-byte-size.tex` template with content from `03_floatsAndByteSize/Floats and memory.md`
4. **Lesson 4**: Expand `04_number-systems.tex` template with content from `04_NumberSystems/04_numberSystemsCmath.md`

**MEDIUM PRIORITY** - Create from source directories:
- Lessons 5-11: Analyze source directories and create corresponding LaTeX files
- Lessons 11-16: Functions and advanced control structures  

**LOW PRIORITY** - Advanced topics:
- Lessons 17-26: Arrays, projects, data structures
- Lessons 39-40: Specialized debugging/git courses

### **3. Address AI Literacy Content**
- `01_ai_literacy.tex` is complete but **not part of core CS12 curriculum**
- **Decision needed**: Keep as supplementary lesson or move to separate directory?

### **4. Standardize All Files**
- **Theme**: Convert all to DS9 theme with `\usetheme{DS9}`
- **Paths**: Use `\graphicspath{{../images/}{../../shared/images/}}`  
- **Structure**: Follow naming convention matching OneDrive directories

## Recommended Development Approach
1. **Phase 1**: Resolve duplicate files and standardize themes
2. **Phase 2**: Develop high-priority core content (lessons 1-16)  
3. **Phase 3**: Implement project-based lessons (17-26)
4. **Phase 4**: Integrate specialized short courses and advanced topics

### Course Flow Excellence
The progression demonstrates sophisticated pedagogical design:
- **Gentle Introduction** (1-4): Careful onboarding to programming concepts
- **Logic Foundations** (5-8): Boolean logic and decision structures
- **Iteration Mastery** (9-11): Loop patterns and problem solving
- **Functional Programming** (11-16): Functions, recursion, and scope
- **Data Structure Fundamentals** (17-23): Arrays, sorting, and algorithm analysis
- **Professional Development** (18.5, 21.5): Git, prompt engineering, debugging
- **Advanced Applications** (22-26): Complex data structures and file I/O
- **Specialized Skills** (39-40): Debugging and development environment mastery

This comprehensive structure provides professional-level C++ education suitable for computer science students.