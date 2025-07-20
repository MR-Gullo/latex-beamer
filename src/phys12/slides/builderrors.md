# Physics 12 Slides Build Errors

## ch01-03_review_test-prep.tex

### Critical Errors
- **Line 252**: `! Too many }'s.` - Unmatched closing brace
- **Line 237**: Overfull \hbox (81.1184pt too wide) - Content too wide for frame

### Warnings
- **Lines 396, 427**: `\textdegree invalid in math mode` - Need to use `{}^{\circ}` instead of `\textdegree` in math mode
- **Line 401**: `Package hyperref Warning: Option 'pdfauthor' has already been used` - Duplicate hyperref option

### Missing Files
- Various image files referenced but not found

## Build Status Summary
- **Total files attempted**: 19
- **Files with critical errors**: 1 (ch01-03_review_test-prep.tex)
- **Files with warnings only**: Multiple files with degree symbol issues
- **Successfully built**: Most files build but with warnings

## Recommended Fixes
1. Fix unmatched braces in ch01-03_review_test-prep.tex around line 237-252
2. Replace `\textdegree` with `{}^{\circ}` in math mode throughout files
3. Verify all image file paths and ensure images exist
4. Remove duplicate hyperref options

## Next Steps
- Review and fix critical errors first
- Address degree symbol warnings across all files
- Verify image dependencies