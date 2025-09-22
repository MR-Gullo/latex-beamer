# LaTeX Beamer Cleanup Plan: 03_floats-and-byte-size.tex → 04-1_number-systems-math-libraries.tex → 04-2_if-else.tex

## Analysis Summary

After thoroughly reading all three files and examining their place in the CS12 course sequence, I've identified significant issues with content repetition and logical progression:

### Current Problems:

1. **Massive Content Duplication (70% overlap)**:
   - File 03 (`03_floats-and-byte-size.tex`) and File 04-1 (`04-1_number-systems-math-libraries.tex`) duplicate:
     - Float data type explanations (nearly identical content)
     - Integer vs floating-point division (same examples and explanations)
     - Bits and bytes concepts (identical descriptions)
     - sizeof() operator (same syntax and examples)
     - Binary number systems (same conversion examples)
     - cin input functionality (same syntax and examples)

2. **Logical Flow Issues**:
   - File 04-2 (`04-2_if-else.tex`) is essentially empty (placeholder content)
   - Missing proper progression from basic data types to control flow
   - U-P-E-R problem-solving method appears in both 03 and 04-1 (redundant)

3. **Content Organization Problems**:
   - Mathematical functions in 04-1 feel disconnected from the main theme
   - No clear bridge between number systems and conditional logic
   - Homework instructions are duplicated across files

### Proposed Cleanup Structure:

**File 03: `03_floats-and-memory.tex` (Streamlined)**
- Remove: U-P-E-R method, code quality section, homework slides
- Keep: Essential float concepts, memory (bits/bytes), sizeof(), basic binary intro
- Focus: Core concepts only, remove redundant examples

**File 04-1: `04_number-systems-math.tex` (Repurposed)**
- Remove: All float basics, memory concepts, cin input, U-P-E-R duplication
- Add: Deeper binary/hex conversions, number system operations, math library functions
- Focus: Number systems as foundation for upcoming conditional logic

**File 04-2: `04-2_conditional-logic.tex` (Complete rewrite)**
- Remove: Placeholder content entirely
- Add: Proper introduction to if/else statements, relational operators, boolean logic
- Create: Logical bridge from number systems to control flow
- Include: Practical examples using concepts from previous lessons

### Specific Content Migration:

1. **Move U-P-E-R to dedicated section**: Remove from both 03 and 04-1, create standalone or integrate with problem-solving exercises
2. **Consolidate math functions**: Group all `<cmath>` content in 04-1 with number systems context
3. **Build logical progression**: Data types → Number systems → Conditional logic
4. **Eliminate duplicate code examples**: Keep best version of each demo, remove others
5. **Standardize formatting**: Ensure consistent use of DS9 theme and code formatting

### Expected Results:
- **Reduce total content by ~40%** while maintaining educational value
- **Improve logical flow** from basic to advanced concepts
- **Eliminate student confusion** from repeated material
- **Create proper foundation** for conditional logic topics

## File-by-File Cleanup Details

### File 03: `03_floats-and-byte-size.tex` - Issues to Address

**Redundant Content to Remove:**
- U-P-E-R problem-solving method (appears again in 04-1)
- Code quality formatting section (better suited for dedicated coding standards)
- Grade calculator and arithmetic sequence examples (duplicated in 04-1)
- Homework submission slides (duplicated across files)

**Content to Keep and Streamline:**
- Essential float data type concepts
- Integer vs floating-point division (single best example)
- Bits and bytes visualization
- sizeof() operator demonstration
- Basic binary number introduction
- cin input basics

### File 04-1: `04-1_number-systems-math-libraries.tex` - Issues to Address

**Already Improved:**
- ✅ Title focused on number systems and math
- ✅ Learning objectives targeted appropriately
- ✅ Added hexadecimal content (good expansion)
- ✅ Streamlined number systems focus

**Remaining Issues:**
- U-P-E-R method still duplicated from file 03
- Math functions section feels disconnected
- Some duplicate foundational concepts

**Further Improvements Needed:**
- Remove remaining duplicate foundational content
- Better integration of math functions with number systems
- Clearer bridge to conditional logic concepts

### File 04-2: `04-2_if-else.tex` - Complete Rewrite Needed

**Current State:**
- Essentially empty placeholder
- Missing proper introduction to conditional logic
- No connection to previous number systems concepts
- Uses default theme instead of DS9 theme

**Required Content:**
- Introduction to if/else statements
- Relational and logical operators
- Boolean logic foundations
- Practical examples using number system concepts
- Connection to binary decision-making
- Proper DS9 theme integration

## Implementation Priority

1. **High Priority**: Complete rewrite of `04-2_if-else.tex` with proper conditional logic content
2. **Medium Priority**: Streamline `03_floats-and-byte-size.tex` to remove redundant U-P-E-R and examples
3. **Low Priority**: Fine-tune `04-1_number-systems-math-libraries.tex` to remove remaining duplicates

## Success Metrics

- **Content Reduction**: Target 40% reduction in total slide count across all three files
- **Logical Flow**: Clear progression from data types → number systems → conditional logic
- **Student Understanding**: Elimination of confusion from repeated material
- **Code Quality**: Consistent DS9 theme usage and proper code formatting throughout