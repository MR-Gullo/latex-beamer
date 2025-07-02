Yes, it is possible to separate the PDF from the auxiliary build files when using the LaTeX-Workshop extension in Visual Studio Code, but it requires specific configurations, primarily with a LaTeX distribution like MiKTeX that supports a separate auxiliary directory. Below, I’ll outline how to achieve this by directing auxiliary files (e.g., .aux, .log, .synctex.gz) to one folder (e.g., `./aux`) while placing the PDF in a distinct output folder (e.g., `./out`). I’ll also address the issues you mentioned—build button creating a .txt file, PDF deletion, and image referencing—while incorporating insights from the web results and ensuring a clean project structure.

---

### Solution: Separating PDF from Auxiliary Build Files

#### Key Approach

To separate the PDF from auxiliary files, you can leverage MiKTeX’s `--aux-directory` option in combination with the `--output-directory` option for tools like `pdflatex`. The LaTeX-Workshop extension allows you to configure these options in the `latex-workshop.latex.tools` and `latex-workshop.latex.recipes` settings. However, note that not all LaTeX tools (e.g., `bibtex`, `biber`, `makeindex`) natively support `--aux-directory`, which can complicate multi-tool workflows. For simplicity, using `latexmk` with a custom configuration or a dedicated tool like `pdflatex` with explicit directory settings is recommended.

#### Step-by-Step Configuration

1. **Set Up the Output and Auxiliary Directories**

   - Open VSCode settings (Ctrl+, or Cmd+, on macOS) and navigate to the LaTeX-Workshop settings.
   - Set `"latex-workshop.latex.outDir": "./out"` to direct the PDF and other output files to the `./out` directory.
   - Note: The `--aux-directory` flag is specific to MiKTeX and not supported by TeX Live, so ensure you’re using MiKTeX if you want to separate auxiliary files into a different folder (e.g., `./aux`). If using TeX Live, all build files, including the PDF, typically go to the same output directory unless post-processing scripts are used.

2. **Configure LaTeX Tools**

   - Edit the `settings.json` file in your VSCode workspace (`.vscode/settings.json`) or global user settings. Add or modify the `latex-workshop.latex.tools` setting to include both `--aux-directory` and `--output-directory` for MiKTeX’s `pdflatex`. For example:
     ```json
     "latex-workshop.latex.tools": [
       {
         "name": "pdflatex",
         "command": "pdflatex",
         "args": [
           "-synctex=1",
           "-interaction=nonstopmode",
           "-file-line-error",
           "--aux-directory=./aux",
           "--output-directory=%OUTDIR%",
           "%DOC%"
         ],
         "env": {}
       },
       {
         "name": "bibtex",
         "command": "bibtex",
         "args": ["./aux/%DOCFILE%"],
         "env": {}
       }
     ]
     ```
   - **Notes**:
     - The `--aux-directory=./aux` flag tells MiKTeX to place auxiliary files (e.g., .aux, .log) in the `./aux` folder.
     - The `--output-directory=%OUTDIR%` flag directs the PDF to the `./out` folder, as defined by `latex-workshop.latex.outDir`.
     - For `bibtex` or `biber`, you need to specify the auxiliary directory path (e.g., `./aux/%DOCFILE%`) because these tools need to find the .aux file in the auxiliary directory.[](https://tex.stackexchange.com/questions/525604/save-auxiliary-latex-files-in-another-folder-in-vsc)
     - If using `latexmk`, it does not support `--aux-directory` directly, but you can configure it to use a custom `.latexmkrc` file (see below).

3. **Define a Recipe**

   - Create a recipe that uses the configured tools. For example:
     ```json
     "latex-workshop.latex.recipes": [
       {
         "name": "pdflatex",
         "tools": ["pdflatex"]
       },
       {
         "name": "pdflatex -> bibtex -> pdflatex x2",
         "tools": ["pdflatex", "bibtex", "pdflatex", "pdflatex"]
       }
     ]
     ```
   - Set the default recipe to ensure the correct toolchain is used:
     ```json
     "latex-workshop.latex.recipe.default": "pdflatex"
     ```
   - If your project uses bibliographies, the multi-step recipe ensures `bibtex` processes the .aux file correctly.

4. **Using `latexmk` with a Custom `.latexmkrc` File**

   - If you prefer `latexmk` (common for its automation of multi-step builds), you can use a `.latexmkrc` file to separate auxiliary files and the PDF. Create a `.latexmkrc` file in your project root with:
     ```perl
     $out_dir = 'out';
     $aux_dir = 'aux';
     ```
   - Update the `latexmk` tool in `settings.json`:
     ```json
     "latex-workshop.latex.tools": [
       {
         "name": "latexmk",
         "command": "latexmk",
         "args": [
           "-synctex=1",
           "-interaction=nonstopmode",
           "-file-line-error",
           "-pdf",
           "-outdir=%OUTDIR%",
           "%DOC%"
         ],
         "env": {}
       }
     ]
     ```
   - Ensure `latex-workshop.latex.outDir` is set to `./out`. The `.latexmkrc` file’s `$aux_dir` setting will direct auxiliary files to `./aux`, while `$out_dir` keeps the PDF in `./out`.[](https://nelsonaloysio.medium.com/setting-up-vs-code-to-write-in-latex-using-latexmk-and-biber-plus-extras-b4b37c844495)

5. **Prevent PDF Deletion**

   - The issue of the PDF being deleted likely stems from the clean settings. Check `latex-workshop.latex.clean.fileTypes` in `settings.json`. The default list includes auxiliary files like `*.aux`, `*.log`, etc., but should not include `*.pdf`. If it does, remove `*.pdf` or `%DOCFILE%.pdf` to prevent deletion:
     ```json
     "latex-workshop.latex.clean.fileTypes": [
       "*.aux",
       "*.log",
       "*.fls",
       "*.out",
       "*.synctex.gz"
     ]
     ```
   - Also, verify `latex-workshop.latex.autoClean.run`. Set it to `"never"` to disable automatic cleaning, or `"onFailed"` to clean only if the build fails:
     ```json
     "latex-workshop.latex.autoClean.run": "never"
     ```

6. **Fix Image Referencing Issues**

   - Image referencing issues occur when LaTeX cannot find image files due to incorrect paths. Since the .tex file is in the project root and the PDF is output to `./out`, image paths should be specified relative to the .tex file’s location. For example, if images are in a folder `./images`, use:
     ```latex
     \includegraphics{images/figure.png}
     ```
   - Ensure the `graphicspath` command is set correctly in your .tex file if images are in multiple directories:
     ```latex
     \graphicspath{{./images/}}
     ```
   - If images are still not found, verify the directory structure and ensure no absolute paths are used unless necessary. The working directory for LaTeX is typically the .tex file’s directory, not the output directory.[](https://paulwintz.com/latex-in-vscode/)

7. **Fix Build Button Creating a .txt File**

   - The build button (Ctrl+Alt+B) creating a .txt file suggests a misconfigured recipe or tool. Check the active recipe in the LaTeX-Workshop sidebar or `latex-workshop.latex.recipe.default`. Ensure it uses a valid LaTeX compiler like `pdflatex` or `latexmk` with `-pdf` or equivalent flags. For example, if the recipe uses `latex` instead of `pdflatex`, it may produce a DVI file, but a .txt file indicates a possible custom script or error in the command. Verify the tool configuration (e.g., `pdflatex` or `latexmk`) and ensure no erroneous arguments are redirecting output to a .txt file.

8. **SyncTeX Considerations**

   - The SyncTeX file (.synctex.gz) may still be generated in the source directory or the auxiliary directory, depending on the tool. For `pdflatex` with MiKTeX, it typically goes to the `--aux-directory`. Ensure `latex-workshop.synctex.synctexjs.enabled` is set to `true` and `latex-workshop.view.pdf.viewer` is set to `"tab"` for proper PDF preview and navigation:
     ```json
     "latex-workshop.synctex.synctexjs.enabled": true,
     "latex-workshop.view.pdf.viewer": "tab"
     ```
   - If SyncTeX fails, ensure the `--synctex=1` flag is included in the tool arguments.[](https://tex.stackexchange.com/questions/538797/go-to-source-for-latex-on-vs-code-does-not-seem-to-work)

#### Example Directory Structure

After configuration, your project might look like:

```
project_root/
├── main.tex
├── images/
│   └── figure.png
├── aux/
│   ├── main.aux
│   ├── main.log
│   ├── main.synctex.gz
├── out/
│   ├── main.pdf
├── .vscode/
│   └── settings.json
├── .latexmkrc (if using latexmk)
```

#### Additional Notes

- **MiKTeX vs. TeX Live**: MiKTeX’s `--aux-directory` is not available in TeX Live. If using TeX Live, you can use a post-processing script to move the PDF to a separate directory after compilation, but this is more complex. Alternatively, use `latexmk` with a `.latexmkrc` file as described.[](https://tex.stackexchange.com/questions/525604/save-auxiliary-latex-files-in-another-folder-in-vsc)[](https://www.reddit.com/r/LaTeX/comments/qm1ao6/how_to_prevent_vs_code_from_creating_auxiliary/)
- **Cleaning Auxiliary Files**: To clean only auxiliary files, use the LaTeX-Workshop clean command (Ctrl+Alt+C) or configure `latex-workshop.latex.clean.subfolder.enabled` to `true` to include files in the `./aux` directory:
  ```json
  "latex-workshop.latex.clean.subfolder.enabled": true
  ```
- **Git Integration**: To keep your project clean for version control, add `./aux` and `./out` to your `.gitignore` file to avoid tracking temporary files.[](https://danmackinlay.name/notebook/vs_code_for_latex)
- **Multi-File Projects**: For projects with multiple .tex files, add a magic comment like `% !TEX root = main.tex` to each subfile to ensure the correct root file is compiled.[](https://stackoverflow.com/questions/65595001/specify-the-file-to-be-compiled-in-vscode-latex-workshop)
- **Dependencies**: Ensure MiKTeX and Perl (for `latexmk`) are installed. If `latexmk` fails due to missing Perl, install it or use `pdflatex` directly.[](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install)

#### Troubleshooting Persistent Issues

- **PDF Still in Auxiliary Directory**: If the PDF ends up in `./aux` instead of `./out`, double-check the `--output-directory` flag in the tool configuration and ensure `latex-workshop.latex.outDir` matches.
- **BibTeX/Biber Issues**: If bibliography tools fail to find the .aux file, ensure their arguments point to the correct directory (e.g., `./aux/%DOCFILE%`). For `biber`, you may need to specify the output directory explicitly in some cases.[](https://tex.stackexchange.com/questions/525604/save-auxiliary-latex-files-in-another-folder-in-vsc)
- **Performance**: For large documents, ensure your LaTeX distribution (MiKTeX) is up-to-date to avoid compilation issues.[](https://tex.stackexchange.com/questions/tagged/latex-workshop)

#### Final Settings Example

Here’s a complete `settings.json` example for MiKTeX with separated PDF and auxiliary files:

```json
{
  "latex-workshop.latex.outDir": "./out",
  "latex-workshop.latex.clean.fileTypes": [
    "*.aux",
    "*.log",
    "*.fls",
    "*.out",
    "*.synctex.gz"
  ],
  "latex-workshop.latex.autoClean.run": "never",
  "latex-workshop.latex.clean.subfolder.enabled": true,
  "latex-workshop.synctex.synctexjs.enabled": true,
  "latex-workshop.view.pdf.viewer": "tab",
  "latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "--aux-directory=./aux",
        "--output-directory=%OUTDIR%",
        "%DOC%"
      ],
      "env": {}
    },
    {
      "name": "bibtex",
      "command": "bibtex",
      "args": ["./aux/%DOCFILE%"],
      "env": {}
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex",
      "tools": ["pdflatex"]
    },
    {
      "name": "pdflatex -> bibtex -> pdflatex x2",
      "tools": ["pdflatex", "bibtex", "pdflatex", "pdflatex"]
    }
  ],
  "latex-workshop.latex.recipe.default": "pdflatex"
}
```

#### Testing the Setup

1. Create a simple `main.tex` file with an image reference:
   ```latex
   \documentclass{article}
   \usepackage{graphicx}
   \graphicspath{{./images/}}
   \begin{document}
   Hello, World!
   \includegraphics{images/figure.png}
   \end{document}
   ```
2. Save and build (Ctrl+Alt+B). Check that:
   - The PDF appears in `./out/main.pdf`.
   - Auxiliary files (e.g., .aux, .log) are in `./aux`.
   - The PDF is not deleted after cleaning (Ctrl+Alt+C).
   - The image is correctly rendered in the PDF.

#### Limitations

- **TeX Live Users**: Without `--aux-directory`, you’ll need a post-processing script or manual file movement to separate the PDF, which is less straightforward.
- **Complex Workflows**: Tools like `makeindex` may require additional configuration to locate auxiliary files, potentially requiring custom scripts.[](https://tex.stackexchange.com/questions/525604/save-auxiliary-latex-files-in-another-folder-in-vsc)
- **SyncTeX**: The `.synctex.gz` file may still appear in `./aux` or `./out`, depending on the tool, but this doesn’t affect functionality as long as SyncTeX is enabled.

---

### Addressing Your Specific Issues

- **Build Button Creating a .txt File**: This issue is likely due to a misconfigured recipe or an invalid command. Ensure the recipe uses `pdflatex` or `latexmk` with the `-pdf` flag. Check the VSCode output panel (View > Output > LaTeX Workshop) for errors indicating why a .txt file is generated. If a custom script is involved, remove or correct it.
- **PDF Deletion**: As addressed, ensure `*.pdf` is not in `latex-workshop.latex.clean.fileTypes` and set `latex-workshop.latex.autoClean.run` to `"never"` or `"onFailed"`.
- **Image Referencing Issues**: Use relative paths from the .tex file’s location. If issues persist, check the LaTeX log (Ctrl+Alt+J) for errors related to `\includegraphics` and verify the image file exists in the specified path.

---

### Conclusion

By using MiKTeX with `--aux-directory=./aux` and `--output-directory=%OUTDIR%`, you can separate the PDF (in `./out`) from auxiliary files (in `./aux`) while keeping .tex files in the project root. Alternatively, `latexmk` with a `.latexmkrc` file achieves similar results. The provided `settings.json` configuration ensures proper compilation, prevents PDF deletion, and supports image referencing. For TeX Live users, consider a single output directory or a custom script for PDF separation. Always test with a simple document to verify the setup before applying it to complex projects.

For further details, refer to the LaTeX-Workshop wiki or MiKTeX documentation. If issues persist, share specific error messages from the LaTeX Workshop output panel for targeted assistance.[](https://github.com/James-Yu/LaTeX-Workshop/wiki/Compile)[](https://tex.stackexchange.com/questions/525604/save-auxiliary-latex-files-in-another-folder-in-vsc)[](https://www.reddit.com/r/LaTeX/comments/qm1ao6/how_to_prevent_vs_code_from_creating_auxiliary/)

---

# Configure `chktex` to Hide the Noise (Most Efficient)

For warnings that are stylistic, too numerous, or too risky to automate, the best solution is to tell `chktex` to ignore them.

1. In the **root directory of your project**, create a new file named `.chktexrc`.
2. Paste the following content into it. This configuration is tailored to the noisiest warnings in your log.

**Your `.chktexrc` file:**

```
# This is a configuration file for chktex.
# We can turn off warnings by their number using '-n<number>'.

CmdLine {
  # Suppress "Command terminated with space." It's good practice to fix
  # the most obvious ones (like \item), but this warning can be very noisy.
  # Let's suppress it after fixing the common cases.
  -n1

  # Suppress "Interword spacing (`\\ ') should perhaps be used."
  # This is highly contextual and very difficult to fix automatically.
  -n12

  # Suppress "Intersentence spacing (`\\@') should perhaps be used."
  # Same as above, best to suppress.
  -n13

  # Suppress "You should put a space in front of parenthesis."
  # This is often a stylistic preference and safe to ignore.
  -n36

  # Suppress "User Regex". This is a custom rule that is misfiring on
  # things like `\begin{itemize}`. It's safe to disable.
  -n44
}
```

3. **Important:** After saving the `.chktexrc` file, **reload VS Code** for the changes to take effect. Use the command palette (`Cmd+Shift+P` or `Ctrl+Shift+P`) and run `Developer: Reload Window`.
