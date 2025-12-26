#!/usr/bin/env python3
"""
Extract images from PPTX files with proper figure numbering.
PPTX files are ZIP archives containing slide XML with figure numbers in titles.
"""

import zipfile
import xml.etree.ElementTree as ET
import os
import re
import sys
import shutil
from pathlib import Path

# PowerPoint XML namespaces
NSMAP = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'rel': 'http://schemas.openxmlformats.org/package/2006/relationships',
}

def register_namespaces():
    """Register namespaces for XML parsing."""
    for prefix, uri in NSMAP.items():
        ET.register_namespace(prefix, uri)

def get_slide_title(slide_xml):
    """Extract title text from slide XML."""
    root = ET.fromstring(slide_xml)

    # Look for title shape
    for sp in root.findall('.//p:sp', NSMAP):
        # Check if this is a title placeholder
        nvSpPr = sp.find('.//p:nvSpPr', NSMAP)
        if nvSpPr is not None:
            nvPr = nvSpPr.find('p:nvPr', NSMAP)
            if nvPr is not None:
                ph = nvPr.find('p:ph', NSMAP)
                if ph is not None and ph.get('type') in ['title', 'ctrTitle', None]:
                    # Extract all text from this shape
                    texts = []
                    for t in sp.findall('.//a:t', NSMAP):
                        if t.text:
                            texts.append(t.text)
                    if texts:
                        return ''.join(texts)

    # Fallback: look for any text containing "Figure"
    for t in root.findall('.//a:t', NSMAP):
        if t.text and 'Figure' in t.text:
            return t.text

    return None

def get_image_relationships(rels_xml):
    """Parse relationship file to get image mappings."""
    root = ET.fromstring(rels_xml)
    relationships = {}

    for rel in root.findall('.//rel:Relationship', NSMAP):
        rid = rel.get('Id')
        target = rel.get('Target')
        rel_type = rel.get('Type', '')

        if 'image' in rel_type.lower() and target:
            # Normalize path (remove ../)
            image_name = os.path.basename(target)
            relationships[rid] = image_name

    return relationships

def get_slide_images(slide_xml):
    """Get image relationship IDs and alt text from slide."""
    root = ET.fromstring(slide_xml)
    images = []

    for pic in root.findall('.//p:pic', NSMAP):
        # Get alt text (description)
        nvPicPr = pic.find('.//p:nvPicPr', NSMAP)
        alt_text = None
        if nvPicPr is not None:
            cNvPr = nvPicPr.find('p:cNvPr', NSMAP)
            if cNvPr is not None:
                alt_text = cNvPr.get('descr')

        # Get image relationship ID
        blip = pic.find('.//a:blip', NSMAP)
        if blip is not None:
            embed = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
            if embed:
                images.append({'rid': embed, 'alt_text': alt_text})

    return images

def extract_figure_number(title):
    """Extract figure number from title text."""
    if not title:
        return None

    # Match patterns like "Figure 18.1", "Fig. 18.1", "Figure 18.10"
    match = re.search(r'[Ff]ig(?:ure)?\.?\s*(\d+)\.(\d+)', title)
    if match:
        chapter = match.group(1)
        figure = match.group(2)
        return f"{chapter}-{figure}"

    return None

def extract_images_from_pptx(pptx_path, topic, output_dir, course='phys11'):
    """
    Extract images from PPTX with proper figure naming.

    Args:
        pptx_path: Path to the .pptx file
        topic: Topic name (e.g., 'electric-charge')
        output_dir: Directory to save extracted images
        course: Course prefix (default: 'phys11')
    """
    register_namespaces()

    results = []

    with zipfile.ZipFile(pptx_path, 'r') as zf:
        # List all files in the archive
        all_files = zf.namelist()

        # Find all slide files
        slide_files = sorted([f for f in all_files if re.match(r'ppt/slides/slide\d+\.xml$', f)],
                            key=lambda x: int(re.search(r'slide(\d+)', x).group(1)))

        for slide_file in slide_files:
            slide_num = int(re.search(r'slide(\d+)', slide_file).group(1))

            # Read slide XML
            slide_xml = zf.read(slide_file).decode('utf-8')

            # Get title and figure number
            title = get_slide_title(slide_xml)
            fig_num = extract_figure_number(title)

            if not fig_num:
                continue

            # Get image relationships from this slide
            images = get_slide_images(slide_xml)

            if not images:
                continue

            # Read relationship file
            rels_file = f'ppt/slides/_rels/slide{slide_num}.xml.rels'
            if rels_file not in all_files:
                continue

            rels_xml = zf.read(rels_file).decode('utf-8')
            relationships = get_image_relationships(rels_xml)

            # Process each image on this slide
            for idx, img_info in enumerate(images):
                rid = img_info['rid']
                alt_text = img_info['alt_text']

                if rid not in relationships:
                    continue

                source_image = relationships[rid]
                source_path = f'ppt/media/{source_image}'

                if source_path not in all_files:
                    continue

                # Determine output filename
                # If multiple images on same slide, append letter suffix
                if len(images) > 1:
                    suffix = chr(ord('a') + idx)
                    output_name = f'{course}-{topic}-fig{fig_num}{suffix}.jpg'
                else:
                    output_name = f'{course}-{topic}-fig{fig_num}.jpg'

                output_path = os.path.join(output_dir, output_name)

                # Extract image
                image_data = zf.read(source_path)
                with open(output_path, 'wb') as f:
                    f.write(image_data)

                result = {
                    'slide': slide_num,
                    'title': title,
                    'figure': fig_num,
                    'source': source_image,
                    'output': output_name,
                    'alt_text': alt_text  # Full alt text for mapping file
                }
                results.append(result)

                # Truncate for console output only
                display_alt = alt_text[:60] + '...' if alt_text and len(alt_text) > 60 else (alt_text or '')
                print(f"Slide {slide_num:2d}: {source_image:15s} -> {output_name}")

    return results

def main():
    if len(sys.argv) < 4:
        print("Usage: python extract-pptx-images.py <pptx_file> <topic> <output_dir> [course]")
        print("Example: python extract-pptx-images.py 18-static-electricity.pptx electric-charge ../images/")
        sys.exit(1)

    pptx_path = sys.argv[1]
    topic = sys.argv[2]
    output_dir = sys.argv[3]
    course = sys.argv[4] if len(sys.argv) > 4 else 'phys11'

    if not os.path.exists(pptx_path):
        print(f"Error: PPTX file not found: {pptx_path}")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    print(f"Extracting images from: {pptx_path}")
    print(f"Topic: {topic}")
    print(f"Output directory: {output_dir}")
    print("-" * 60)

    results = extract_images_from_pptx(pptx_path, topic, output_dir, course)

    print("-" * 60)
    print(f"Extracted {len(results)} images")

    # Write mapping file for reference
    mapping_file = os.path.join(output_dir, f'{course}-{topic}-mapping.txt')
    with open(mapping_file, 'w') as f:
        f.write(f"# Image extraction from {os.path.basename(pptx_path)}\n")
        f.write(f"# Topic: {topic}\n\n")
        for r in results:
            f.write(f"Slide {r['slide']}: {r['source']} -> {r['output']}\n")
            if r['alt_text']:
                f.write(f"  Alt: {r['alt_text']}\n")

    print(f"Mapping saved to: {mapping_file}")

if __name__ == '__main__':
    main()
