# Physics 12 Image Reference Standardization

## Current Status
- ✅ **Foundation Work Complete**: Preamble standardization, syntax fixes, DS9 theme consistency
- ✅ **Build Success Rate**: 36% (13/36 files) - improved from initial state
- 🔄 **In Progress**: Image reference standardization using newnames.md mappings

## Objective
Update all image references in LaTeX Beamer presentations in `src/phys12/slides/` to use standardized naming convention from `src/phys12/images/newnames.md`.

## Priority Tasks

### 1. Fix Incorrect Image Path References
**Problem**: References to non-existent subdirectories (e.g., `CH5/`, `CH8/`)
**Example**: `\includegraphics[width=0.5\linewidth]{CH5/Screenshot 2024-10-29 103504.png}`
**Solution**: Replace with standardized paths using `../images/` directory

### 2. Apply Name Mappings from newnames.md
**80+ mappings** across physics topics:
- **Circuits**: `3seriescap.png` → `phys12-circuits-capacitors-in-series.png`
- **Magnetism**: `chflux.png` → `phys12-magnetism-magnetic-flux-through-loop.png`
- **Electrostatics**: `charge.png` → `phys12-electrostatics-charge-interactions.png`
- **Gravity**: `cavend.png` → `phys12-gravity-cavendish-experiment.png`
- **Vectors**: `vectarr.png` → `phys12-vectors-vector-addition.png`
- **Mechanics**: `arc.png` → `phys12-mechanics-circular-motion-arc.png`
- **Formulas**: `nrt.png` → `phys12-formulas-newton-relativity-thermodynamics.png`

### 3. Cross-Reference with Actual Images
- Verify all image references match files in `src/phys12/images/`
- Identify unmapped images and broken references
- Update newnames.md with any missing mappings

## Files to Process (36 total)
**Main slide files**: ch01-03_review_test-prep.tex, ch03_slides_vectors.tex, ch04-05-09_review.tex, ch04_slides_motion.tex, ch05_slides_forces.tex, ch06_slides_circular-motion-part1.tex, ch06_slides_circular-motion-part2.tex, ch07_*.tex, ch08_*.tex, ch09_*.tex, ch18_slides_electric-fields.tex, ch19_*.tex, ch20-21_*.tex, ch22_*.tex, ch23_slides_electromagnetic-waves.tex, misc_*.tex, test_ch04.tex, util_*.tex

## Expected Deliverables
1. **All image references updated** to standardized naming convention
2. **Path corrections** for incorrect subdirectory references
3. **Analysis report** of unmapped images and broken references
4. **Updated newnames.md** with any newly discovered mappings
5. **Build success rate improvement** from current 36%

## Success Criteria
- All old image names replaced with standardized `phys12-[topic]-[description].[ext]` format
- No broken image references introduced
- LaTeX file integrity maintained
- Comprehensive coverage documentation

## Remaining Issues After Image Fixes
- Unicode character replacements in some files
- Content layout adjustments for overfull boxes
- Final build testing and verification