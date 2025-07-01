# LaTeX Beamer Slideshow Makefile
# Usage: make [target] [FILE=path/to/file.tex]

# Default file if none specified
FILE ?= src/cs12/slides/ex/01_intro_ai.tex

# Build directories
BUILD_DIR = build
OUTPUT_DIR = output

# LaTeX compiler settings
LATEX = pdflatex
LATEXMK = latexmk
LATEXMK_OPTS = -pdf -file-line-error -halt-on-error -interaction=nonstopmode

# Default target
.PHONY: all
all: build

# Build a specific file
.PHONY: build
build:
	@echo "Building $(FILE)..."
	@mkdir -p $(BUILD_DIR)
	@mkdir -p $(OUTPUT_DIR)
	$(LATEXMK) $(LATEXMK_OPTS) -outdir=$(BUILD_DIR) $(FILE)
	@cp $(BUILD_DIR)/*.pdf $(OUTPUT_DIR)/ 2>/dev/null || true
	@echo "PDF created in $(OUTPUT_DIR)/"

# Clean build artifacts
.PHONY: clean
clean:
	@echo "Cleaning build artifacts..."
	$(LATEXMK) -C -outdir=$(BUILD_DIR)
	rm -rf $(BUILD_DIR)
	@echo "Clean complete."

# Clean and rebuild
.PHONY: rebuild
rebuild: clean build

# Build all CS12 slides
.PHONY: cs12
cs12:
	@echo "Building all CS12 slides..."
	@for file in src/cs12/slides/*.tex; do \
		if [ -f "$$file" ]; then \
			echo "Building $$file..."; \
			$(MAKE) build FILE="$$file"; \
		fi \
	done

# Build all Physics 11 slides
.PHONY: phys11
phys11:
	@echo "Building all Physics 11 slides..."
	@for file in src/phys11/slides/*.tex; do \
		if [ -f "$$file" ]; then \
			echo "Building $$file..."; \
			$(MAKE) build FILE="$$file"; \
		fi \
	done

# Build all Physics 12 slides
.PHONY: phys12
phys12:
	@echo "Building all Physics 12 slides..."
	@for file in src/phys12/slides/*.tex; do \
		if [ -f "$$file" ]; then \
			echo "Building $$file..."; \
			$(MAKE) build FILE="$$file"; \
		fi \
	done

# Build everything
.PHONY: all-courses
all-courses: cs12 phys11 phys12

# Watch mode for development
.PHONY: watch
watch:
	@echo "Watching $(FILE) for changes..."
	$(LATEXMK) $(LATEXMK_OPTS) -pvc -outdir=$(BUILD_DIR) $(FILE)

# Help target
.PHONY: help
help:
	@echo "LaTeX Beamer Build System"
	@echo "Usage: make [target] [FILE=path/to/file.tex]"
	@echo ""
	@echo "Targets:"
	@echo "  build        Build specified file (default: $(FILE))"
	@echo "  clean        Remove build artifacts"
	@echo "  rebuild      Clean and rebuild"
	@echo "  cs12         Build all CS12 slides"
	@echo "  phys11       Build all Physics 11 slides"
	@echo "  phys12       Build all Physics 12 slides"
	@echo "  all-courses  Build all courses"
	@echo "  watch        Watch file for changes and rebuild"
	@echo "  help         Show this help"
	@echo ""
	@echo "Examples:"
	@echo "  make build FILE=src/cs12/slides/01_intro_ai.tex"
	@echo "  make cs12"
	@echo "  make clean"