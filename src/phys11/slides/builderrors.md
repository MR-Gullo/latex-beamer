# Physics 11 Slides Build Errors

## ch01-03_review_test-prep.tex

### Missing Files
- **Line 94**: `Screenshot 2024-10-11 141024.png` not found
- **Line 94**: `Screenshot 2024-10-11 141044.png` not found 
- **Line 137**: `2024_09_22_d75bb9ada91612339d1ag-12.jpg` not found

### Critical Errors
- Multiple `Package pdftex.def Error` due to missing image files

## Other Files

### Common Issues Across Files
- Missing image dependencies
- Image path resolution issues

## Build Status Summary
- **Total files attempted**: 18
- **Files with critical errors**: Multiple files with missing images
- **Primary issue**: Missing image files causing build failures
- **Successfully built**: Files without image dependencies build correctly

## Recommended Fixes
1. **Image Management**:
   - Verify all image files exist in expected locations
   - Update image paths to use the standardized `\graphicspath` from DS9 theme
   - Move images to `/shared/images/` directory as per project structure

2. **File Structure**:
   - Ensure images are in `../images/` or `../../shared/images/` relative to slides
   - Update any hardcoded image paths

3. **Missing Images**:
   - `Screenshot 2024-10-11 141024.png`
   - `Screenshot 2024-10-11 141044.png`
   - `2024_09_22_d75bb9ada91612339d1ag-12.jpg`

## Next Steps
- Locate and move missing image files
- Standardize image directory structure
- Update image references to use proper paths