### Key Points

- It seems likely that you can organize your LaTeX files by setting the output directory in VSCode's LaTeX-Workshop extension, but configuration may require adjustments.
- Research suggests setting "latex-workshop.latex.outDir" to "./out" and ensuring recipes use the output directory flag, like "-outdir=%OUTDIR%".
- The evidence leans toward checking clean settings to prevent PDF deletion and verifying image paths for referencing issues.

### Setting Up the Output Directory

To keep your .tex files in one folder and build files, including PDFs, in a separate output directory, start by opening VSCode settings. Search for "latex-workshop.latex.outDir" and set it to your desired directory, such as "./out". This tells the extension where to look for compiled files.

### Ensuring Proper Build Configuration

Next, ensure your build recipe uses the output directory. By default, the "latexmk" recipe should include "-outdir=%OUTDIR%", placing files in the specified directory. If needed, check or customize "latex-workshop.latex.recipes" and "latex-workshop.latex.tools" to include flags like "-output-directory=%OUTDIR%" for tools like pdflatex.

### Addressing Specific Issues

- If the build button creates a .txt file instead of a PDF, it may be due to a misconfigured recipe; verify the tool commands.
- If the PDF builds but gets deleted, check "latex-workshop.latex.clean.fileTypes" to ensure the PDF isn't included in cleanup.
- For image referencing issues, ensure paths in your .tex files are correct relative to the .tex file's location, such as using "\includegraphics{images/figure.png}" for images in a subdirectory.

---

### Survey Note: Detailed Configuration for LaTeX-Workshop in VSCode

This section provides a comprehensive guide to configuring the LaTeX-Workshop extension in VSCode to organize .tex files in one folder and manage build files, including PDFs, in a separate output directory. It addresses the user's reported issues—build button creating a .txt file, PDF deletion, and image referencing problems—while ensuring a clean, compartmentalized project structure.

#### Background and Context

LaTeX-Workshop is a popular extension for VSCode that enhances LaTeX typesetting efficiency with features like preview, compile, and autocomplete. The user aims to keep .tex files in a single folder while directing all build files and PDFs to an output directory, such as "./out", to reduce clutter and facilitate cleaning. However, they encounter issues: the build button produces a .txt file, the PDF builds but is deleted, and there are problems referencing images. These issues suggest potential misconfigurations in the extension's settings, particularly related to output directories, recipes, and cleaning.

#### Configuring the Output Directory

The core setting for managing output directories is "latex-workshop.latex.outDir". This setting determines where the extension looks for project files, including PDFs and SyncTeX files. By default, it is set to "%DIR%", the directory of the root .tex file, but it can be changed to a relative or absolute path, such as "./out". The path must not have a trailing slash, and the LaTeX toolchain must be configured to output files to this directory.

To set this, open VSCode settings (File > Preferences > Settings or Ctrl+,), search for "latex-workshop.latex.outDir", and set it to "./out". This ensures that all compiled files, including the PDF, are placed in the "./out" directory, keeping the project root clean.

#### Ensuring Recipes and Tools Use the Output Directory

LaTeX-Workshop uses recipes to build projects, which are sequences of tools like pdflatex, bibtex, or latexmk. Each tool can have arguments, including placeholders like %OUTDIR%, which is replaced by the value of "latex-workshop.latex.outDir". For the output directory to work, the recipe must include a tool with the appropriate flag, such as "-outdir=%OUTDIR%" for latexmk or "-output-directory=%OUTDIR%" for pdflatex.

By default, the extension uses the latexmk recipe, which includes "-outdir=%OUTDIR%" in its arguments, as seen in examples from user guides. For instance, a typical tool configuration is:

| Tool Name | Command  | Arguments (Example)                                                                                                  |
| --------- | -------- | -------------------------------------------------------------------------------------------------------------------- |
| latexmk   | latexmk  | ["-shell-escape", "-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-pdf", "-outdir=%OUTDIR%", "%DOC%"] |
| pdflatex  | pdflatex | ["-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-output-directory=%OUTDIR%", "%DOC%"]                |

To verify, check the settings for "latex-workshop.latex.recipes" and "latex-workshop.latex.tools" in your settings.json file. If needed, define a custom recipe to ensure the output directory is used. For example:

```json
"latex-workshop.latex.tools": [
  {
    "name": "pdflatex",
    "command": "pdflatex",
    "args": ["-synctex=1", "-interaction=nonstopmode", "-file-line-error", "-output-directory=%OUTDIR%", "%DOC%"],
    "env": {}
  }
],
"latex-workshop.latex.recipes": [
  {
    "name": "pdflatex",
    "tools": ["pdflatex"]
  }
]
```

Set "latex-workshop.latex.recipe.default" to "first" to use the first recipe, ensuring the output directory is respected.

#### Addressing Specific Issues

The user reported three main issues, which can be addressed as follows:

1. **Build Button Creating a .txt File:**

   - This is unusual, as the build button should produce a PDF. It may indicate a misconfigured recipe or tool. For example, if the tool runs "latex" instead of "pdflatex", it might produce a DVI file, but a .txt file suggests a custom script or typo in the command. Verify the "latex-workshop.latex.tools" settings to ensure the command is correct, such as "pdflatex" or "latexmk", and check the recipe used by "latex-workshop.latex.recipe.default".

2. **PDF Builds but Gets Deleted:**

   - The PDF deletion likely relates to the clean settings. The extension has settings for automatic cleaning, controlled by "latex-workshop.latex.autoClean.run", which can be set to "never", "onFailed", or "onBuilt". By default, it's "never", meaning no automatic cleaning. However, if set to "onBuilt", it might delete files. Check "latex-workshop.latex.clean.fileTypes" to ensure the PDF (e.g., "%DOCFILE%.pdf") is not included. The default list includes auxiliary files like .aux and .log, but not the PDF. If customized, remove any PDF-related entries.

   Additionally, the clean command, typically "latexmk -outdir=%OUTDIR% -c %TEX%", should only clean auxiliary files. Ensure no custom clean command deletes the PDF.

3. **Image Referencing Issues:**
   - Image referencing problems may arise if paths in the .tex file are incorrect relative to the .tex file's location. For example, if images are in "images/" and the .tex file uses "\includegraphics{images/figure.png}", it should work as long as the working directory is the .tex file's directory. Since the output directory is separate, LaTeX looks for input files (like images) relative to the .tex file, not the output directory. Ensure paths are relative to the .tex file, or use absolute paths if necessary. If images are in a subdirectory, verify the directory structure and paths.

#### Additional Considerations

- The extension automatically determines the output directory if "latex-workshop.latex.outDir" is "%DIR%" or "%DIR_W32%", parsing tools for -out-directory= or -outdir=. This means if using latexmk without manual moves, you can ignore this setting, but for custom directories, explicit configuration is needed.
- For multi-file projects, ensure the root file is correctly identified, as described in the wiki's multi-files-projects section.
- Be aware of potential version-specific behaviors, as older issues (e.g., GitHub issue #548) noted "outputDir" not working as expected, but recent documentation suggests current versions handle it correctly.

#### Practical Example

Consider a project with .tex files in the root and an "out" directory for build files. Set "latex-workshop.latex.outDir": "./out" and use the default latexmk recipe. For a .tex file with images in "images/", use "\includegraphics{images/figure.png}". After building, the PDF should appear in "./out", and auxiliary files should be cleaned without deleting the PDF, provided clean settings are default.

#### Conclusion

By setting "latex-workshop.latex.outDir" to "./out", ensuring recipes use %OUTDIR% in output flags, and addressing clean settings and image paths, you can achieve a compartmentalized, clean LaTeX project. For persistent issues, verify recipe configurations and consult the extension's wiki for further details.

### Key Citations

- [Compile LaTeX-Workshop Wiki](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile)
- [View LaTeX-Workshop Wiki](https://github.com/James-Yu/LaTeX-Workshop/wiki/View)
- [Setting up VS Code LaTeX Medium Article](https://nelsonaloysio.medium.com/setting-up-vs-code-to-write-in-latex-using-latexmk-and-biber-plus-extras-b4b37c844495)
- [Visual Studio Code for LaTeX Blog Post](https://aumisb.github.io/2019/06/09/visual-studio-code-for-tex.html)
