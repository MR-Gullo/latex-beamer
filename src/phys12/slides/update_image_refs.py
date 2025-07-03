#!/usr/bin/env python3
"""
Script to update image references in LaTeX files based on newnames.md mapping.
"""

import re
import os
from pathlib import Path

def create_mapping_dict():
    """Create mapping dictionary from newnames.md file."""
    mapping = {}
    
    # Read the newnames.md file
    newnames_path = Path("/Users/joelgullo/dev/latex-beamer/src/phys12/images/newnames.md")
    
    with open(newnames_path, 'r') as f:
        lines = f.readlines()
    
    old_name = None
    for line in lines:
        line = line.strip()
        # Pattern: NUMBER - filename (old name)
        if re.match(r'^\d+\s*-\s+', line):
            # Extract filename after "NUMBER - "
            old_name = re.sub(r'^\d+\s*-\s+', '', line)
        # Pattern: NUMBER + filename (new name)
        elif re.match(r'^\d+\s*\+\s+', line) and old_name:
            # Extract filename after "NUMBER + "
            new_name = re.sub(r'^\d+\s*\+\s+', '', line)
            mapping[old_name] = new_name
            old_name = None
    
    return mapping

def find_includegraphics_refs(content):
    """Find all includegraphics references in LaTeX content."""
    # Pattern to match \includegraphics[...]{filename} or \includegraphics{filename}
    pattern = r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}'
    matches = re.findall(pattern, content)
    return matches

def update_latex_file(file_path, mapping):
    """Update a single LaTeX file with new image references."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    original_content = content
    updates_made = []
    
    # Find all includegraphics references
    refs = find_includegraphics_refs(content)
    
    for ref in refs:
        # Extract just the filename (remove any path)
        filename = os.path.basename(ref)
        
        # Check if this filename needs to be updated
        if filename in mapping:
            new_filename = mapping[filename]
            
            # Replace the old filename with the new one, preserving any path
            if ref == filename:
                # No path, just replace the filename
                old_ref = ref
                new_ref = new_filename
            else:
                # Has path, replace just the filename part
                path_part = os.path.dirname(ref)
                old_ref = ref
                new_ref = os.path.join(path_part, new_filename) if path_part else new_filename
            
            # Use exact string replacement for the full reference
            content = content.replace(f'{{{old_ref}}}', f'{{{new_ref}}}')
            updates_made.append((filename, new_filename))
    
    # Write the updated content back if changes were made
    if content != original_content:
        with open(file_path, 'w') as f:
            f.write(content)
    
    return updates_made

def main():
    """Main function to process all LaTeX files."""
    # Create mapping dictionary
    mapping = create_mapping_dict()
    print(f"Created mapping with {len(mapping)} entries")
    
    # Get all LaTeX files in the slides directory
    slides_dir = Path("/Users/joelgullo/dev/latex-beamer/src/phys12/slides")
    tex_files = list(slides_dir.glob("*.tex"))
    
    files_updated = 0
    total_replacements = 0
    used_mappings = set()
    
    print(f"\nProcessing {len(tex_files)} LaTeX files...")
    
    for tex_file in tex_files:
        updates = update_latex_file(tex_file, mapping)
        if updates:
            files_updated += 1
            total_replacements += len(updates)
            print(f"\nUpdated {tex_file.name}:")
            for old, new in updates:
                print(f"  {old} → {new}")
                used_mappings.add(old)
    
    print(f"\n=== SUMMARY ===")
    print(f"Files updated: {files_updated}")
    print(f"Total image references replaced: {total_replacements}")
    print(f"Mappings used: {len(used_mappings)} out of {len(mapping)}")
    
    if used_mappings:
        print(f"\nMappings that were used:")
        for old_name in sorted(used_mappings):
            print(f"  {old_name} → {mapping[old_name]}")

if __name__ == "__main__":
    main()