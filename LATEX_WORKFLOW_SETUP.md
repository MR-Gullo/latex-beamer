# LaTeX Workshop Configuration for Multi-Course Beamer Projects

This document explains the VSCode LaTeX Workshop configuration for managing multi-course LaTeX Beamer slideshows with clean output directories and automated auxiliary file cleanup.

## Project Structure

```
latex-beamer/
├── .vscode/
│   └── settings.json          # LaTeX Workshop configuration
├── latex-beamer.code-workspace # Multi-folder workspace
├── build/                     # Temporary build files (auto-generated)
├── output/                    # Final PDFs organized by course (optional)
├── Computer-Science-12/       # Course folder
├── PHYS11-CH/                # Course folder
├── Phys12-CH/                # Course folder
└── images/                   # Shared images (if any)
```

## Key Features

### 1. Clean Output Directory Management

- **Build Directory**: All auxiliary files (`.aux`, `.log`, `.nav`, `.snm`, etc.) go to `build/`
- **Auto-cleanup**: Auxiliary files are automatically removed after each successful build
- **Source Protection**: Your source directory stays clean with only `.tex` and image files

### 2. Live Preview on Save

- **Auto-build**: PDF rebuilds automatically when you save any `.tex` file
- **SyncTeX**: Click in PDF to jump to source, and vice versa
- **Tab Viewer**: PDF opens in VSCode tab for seamless editing experience

### 3. Multi-Course Support

- **Workspace Configuration**: Organized folders for each course
- **Relative Paths**: Image paths work correctly regardless of output directory
- **Batch Operations**: Tasks for building all courses or cleaning all files

## Configuration Details

### LaTeX Workshop Settings

The `.vscode/settings.json` includes:

```json
{
  "latex-workshop.latex.outDir": "%DIR%/build",
  "latex-workshop.latex.autoBuild.run": "onSave",
  "latex-workshop.latex.autoClean.run": "onBuilt"
}
```

### Build Recipes

Three main recipes are configured:

1. **pdflatex ➜ clean**: Standard build with automatic cleanup
2. **latexmk ➜ clean**: More robust build system with cleanup
3. **pdflatex (production)**: Production build to `output/` directory

### File Management

- **Hidden Files**: Build artifacts are hidden in file explorer
- **Search Exclusion**: Build directories excluded from search
- **Git Integration**: Build files automatically ignored

## Usage Instructions

### Getting Started

1. Open the workspace file: `File` → `Open Workspace from File` → `latex-beamer.code-workspace`
2. Install recommended extensions when prompted
3. Open any `.tex` file and start editing

### Building Documents

#### Automatic Building

- Simply save your `.tex` file (`Ctrl+S`)
- PDF will rebuild automatically in the background
- View the PDF in the built-in viewer

#### Manual Building

- Press `Ctrl+Alt+B` to build manually
- Choose from available recipes in the command palette

#### Production Output

1. Use the "pdflatex (production)" recipe for final PDFs
2. Run the "Organize Output for Distribution" task
3. Find organized PDFs in the `output/` directory

### Managing Image Paths

Images should be referenced relative to your project root:

```latex
% If your image is in Computer-Science-12/images/diagram.png
\includegraphics{Computer-Science-12/images/diagram.png}

% Or use graphicspath in your document preamble
\graphicspath{{Computer-Science-12/images/}{PHYS11-CH/images/}}
\includegraphics{diagram.png}
```

### Cleaning Up

#### Automatic Cleanup

- Enabled by default after each build
- Removes all auxiliary files from `build/` directory
- Keeps only the PDF output

#### Manual Cleanup

- Press `Ctrl+Alt+C` to clean auxiliary files
- Run "Clean All Build Files" task to remove all build directories
- Use Git to ensure no unwanted files are tracked

## Troubleshooting

### Images Not Found

**Problem**: LaTeX can't find images after changing output directory

**Solution**:

- Ensure image paths are relative to project root
- Check that images exist in the specified location
- Use `\graphicspath{}` to specify image directories

### Build Failures

**Problem**: PDF doesn't generate or build fails

**Solutions**:

1. Check the LaTeX Workshop output panel for errors
2. Ensure all required packages are installed
3. xTry the "latexmk" recipe for better error handling
4. Clean build files and rebuild

### Performance Issues

**Problem**: VSCode becomes slow with many files

**Solutions**:

1. Exclude more file types in workspace settings
2. Disable auto-build temporarily: `"latex-workshop.latex.autoBuild.run": "never"`
3. Use manual building for large projects

## Best Practices

### File Organization

1. **Keep sources clean**: Only `.tex` and image files in source directories
2. **Use consistent naming**: Follow the project's naming conventions
3. **Organize by course**: Separate folders for each course/subject

### Version Control

1. **Ignore build files**: Use `.gitignore` to exclude `build/` and `output/`
2. **Track only sources**: Commit `.tex` files, images, and configuration
3. **Clean before commits**: Run cleanup tasks before version control operations

### Workflow Optimization

1. **Use auto-build** for active development
2. **Disable auto-build** for batch operations
3. **Use production recipes** for final output
4. **Leverage tasks** for bulk operations

## Advanced Configuration

### Custom Build Scripts

For complex build requirements, create custom tasks in the workspace file:

```json
{
  "label": "Custom Build with Post-processing",
  "type": "shell",
  "command": "bash",
  "args": [
    "-c",
    "pdflatex -output-directory=build main.tex && custom-script.sh"
  ]
}
```

### Integration with External Tools

Configure external tools for specialized workflows:

```json
"latex-workshop.latex.external.build.command": "make",
"latex-workshop.latex.external.build.args": ["all"]
```

### Course-Specific Settings

Override settings per course by creating `.vscode/settings.json` in individual course folders.

## Conclusion

This configuration provides a robust, clean, and efficient workflow for managing multi-course LaTeX Beamer projects. The automated cleanup and organized output structure ensure that your development environment stays clean while maintaining compatibility with relative image paths and providing excellent development experience with live preview and SyncTeX integration.
