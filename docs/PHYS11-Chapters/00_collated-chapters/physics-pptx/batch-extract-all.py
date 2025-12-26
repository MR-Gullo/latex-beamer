#!/usr/bin/env python3
"""
Batch extract images from all PPTX files in this directory.
"""

import subprocess
import os
from pathlib import Path

# Map PPTX filename prefix to topic name
PPTX_TO_TOPIC = {
    '1-what-is-physics': 'what-is-physics',
    '2-motion-in-one-dimension': 'kinematics',
    '3-acceleration': 'acceleration',
    '4-forces-and-newtons-laws-of-motion': 'dynamics',
    '5-motion-in-two-dimensions': 'motion-2d',
    '6-circular-and-rotational-motion': 'circular-motion',
    '7-newtons-law-of-gravitation': 'gravitation',
    '8-momentum': 'momentum',
    '9-work-energy-and-simple-machines': 'work-energy',
    '10-special-relativity': 'relativity',
    '11-thermal-energy-heat-and-work': 'thermal',
    '12-thermodynamics': 'thermodynamics',
    '13-waves-and-their-properties': 'waves',
    '14-sound': 'sound',
    '15-light': 'em-spectrum',
    '16-mirrors-and-lenses': 'geometric-optics',
    '17-diffraction-and-interference': 'wave-optics',
    '18-static-electricity': 'electric-charge',
    '19-electrical-circuits': 'electric-circuits',
    '20-magnetism': 'magnetism',
    '21-the-quantum-nature-of-light': 'quantum',
    '22-the-atom': 'atomic-nuclear',
    '23-particle-physics': 'particle-physics',
}

def main():
    script_dir = Path(__file__).parent
    extract_script = script_dir / 'extract-pptx-images.py'
    output_dir = script_dir / 'extracted-images'

    output_dir.mkdir(exist_ok=True)

    # Find all PPTX files
    pptx_files = sorted(script_dir.glob('*.pptx'))

    print(f"Found {len(pptx_files)} PPTX files")
    print("=" * 60)

    for pptx in pptx_files:
        # Get topic from filename
        basename = pptx.stem
        topic = PPTX_TO_TOPIC.get(basename)

        if not topic:
            print(f"SKIP: {pptx.name} (no topic mapping)")
            continue

        print(f"\n{'='*60}")
        print(f"Processing: {pptx.name}")
        print(f"Topic: {topic}")
        print("=" * 60)

        # Run extraction
        cmd = [
            'python3', str(extract_script),
            str(pptx),
            topic,
            str(output_dir),
            'phys11'
        ]

        result = subprocess.run(cmd, capture_output=False)

        if result.returncode != 0:
            print(f"ERROR: Failed to extract from {pptx.name}")

if __name__ == '__main__':
    main()
