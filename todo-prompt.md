# LaTeX Beamer Image Analysis and Standardization Prompt

## Task Overview
Analyze original archived images against current image mapping files to identify discrepancies, create standardized copies, and document missing images for future replacement sourcing.

## Context
- **Physics 11 Archive**: `archive/PHYS11-CH/images/` (original cryptic filenames)
- **Physics 12 Archive**: `archive/Phys12-CH/images/` (original cryptic filenames)
- **Current Standardized**: `src/phys11/images/` and `src/phys12/images/`
- **Mapping Files**: `src/phys11/images/newnames.md` and `src/phys12/images/newnames.md`

## Detailed Analysis Requirements

### 1. Image Inventory Comparison
For each course (Physics 11 and Physics 12):

**Compare archive vs mapping files:**
- Read all original images in `archive/PHYS[11|12]-CH/images/`
- Cross-reference with mapping files in `src/phys[11|12]/images/newnames.md`
- Identify images present in archive but missing from mapping
- Identify mappings that reference non-existent archive images

### 2. Visual Content Analysis
For each original image file:

**Analyze image content and context:**
- Describe the visual content (diagrams, equations, photos, screenshots)
- Identify the physics topic/concept being illustrated
- Assess image quality and educational value
- Note any text, equations, or specific physics formulas visible
- Determine if image is a diagram, photograph, screenshot, or illustration

### 3. Standardized Name Validation
For each mapped image:

**Validate naming convention compliance:**
- Check if standardized name follows `phys[11|12]-topic-description.extension` format
- Verify the topic category matches the image content
- Ensure description is accurate and educational
- Flag any naming inconsistencies or improvements needed

### 4. Missing Image Documentation
For images referenced in LaTeX files but not found:

**Create detailed replacement specifications:**
- **Original Reference**: LaTeX filename and line number
- **Expected Content**: Description of what the image should show
- **Physics Topic**: Specific concept or principle being illustrated
- **Image Type**: Diagram, graph, photo, screenshot, illustration
- **Suggested Search Terms**: Keywords for finding replacement images
- **Educational Context**: How the image supports the lesson content
- **Alternative Sources**: Suggestions for where to find similar images (textbooks, online resources, etc.)

### 5. File Operations Required
Based on analysis findings:

**Copy and organize images:**
- Copy missing archive images to standardized directories
- Create properly named copies following naming conventions
- Update mapping files with newly discovered images
- Remove orphaned mappings (no corresponding archive file)

### 6. Quality Assessment
For each image:

**Technical and educational evaluation:**
- File format appropriateness (PNG vs JPG vs other)
- Resolution quality for LaTeX compilation
- Educational clarity and readability
- Consistency with course visual style

## Output Requirements

### 1. Comprehensive Report
Create detailed analysis report including:
- Total image counts (archive vs mapped vs missing)
- Discrepancy list with specific filenames
- Quality assessment summary
- Recommended actions for each image category

### 2. Missing Image Database
For each missing image, provide:
```
**Image Reference**: filename.extension
**LaTeX Source**: path/to/file.tex:line_number
**Physics Topic**: [topic area]
**Expected Content**: [detailed description]
**Image Type**: [diagram/photo/screenshot/illustration]
**Search Keywords**: [comma-separated terms]
**Educational Purpose**: [how it supports learning]
**Suggested Sources**: [where to find replacements]
**Priority Level**: [high/medium/low based on usage frequency]
```

### 3. Updated Mapping Files
Generate corrected mapping files with:
- All valid archive-to-standardized mappings
- Newly discovered images properly categorized
- Removed orphaned entries
- Consistent naming convention application

### 4. Action Plan
Prioritized list of next steps:
- Critical missing images requiring immediate attention
- Archive images needing standardization
- Mapping file corrections needed
- LaTeX file updates required

## Success Metrics
- **Complete inventory**: All archive images accounted for
- **Accurate mappings**: 100% correspondence between archive and mapping files
- **Missing image documentation**: Detailed specs for all missing images
- **Naming consistency**: All standardized names follow convention
- **Educational value**: Quality assessment for each image

## Priority Focus Areas
1. **Critical missing images** blocking compilation (4 Physics 12 + 16 Physics 11)
2. **Unmapped archive images** that could resolve missing references
3. **Incorrectly named standardized images** causing LaTeX failures
4. **High-usage missing images** appearing in multiple files

This analysis will provide the foundation for completing the image standardization process and resolving the majority of LaTeX compilation failures in both Physics courses.