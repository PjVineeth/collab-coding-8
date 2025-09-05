# Math Utilities - Collaborative Project Makefile

.PHONY: help install test lint format analysis demo clean

# Default target
help:
	@echo "Math Utilities - Available Commands:"
	@echo "====================================="
	@echo "  make install     - Install dependencies"
	@echo "  make test        - Run all tests"
	@echo "  make lint        - Run linting checks"
	@echo "  make format      - Format code with black"
	@echo "  make analysis    - Run code complexity analysis"
	@echo "  make demo        - Run function demonstration"
	@echo "  make clean       - Clean up generated files"
	@echo "  make all         - Run test, lint, and analysis"

# Install dependencies
install:
	pip install -r requirements.txt

# Run tests
test:
	python3 -m pytest tests/ -v

# Run linting
lint:
	python3 -m flake8 math_utils.py code_analysis.py main.py
	python3 -m bandit -r . -f json -o bandit-report.json || true
	python3 -m bandit -r . -f txt

# Format code
format:
	python3 -m black math_utils.py code_analysis.py main.py

# Run code analysis
analysis:
	python3 code_analysis.py --format text



# Run demonstration
demo:
	python3 main.py --demo

# Run all checks
all: test lint analysis

# Clean up
clean:
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf bandit-report.json
	rm -rf safety-report.json
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Development setup
dev-setup: install
	@echo "Setting up development environment..."
	@echo "Installing pre-commit hooks..."
	pip install pre-commit
	pre-commit install
	@echo "Development setup complete!"

# Run pre-commit checks
pre-commit:
	pre-commit run --all-files

# Generate documentation
docs:
	@echo "Generating documentation..."
	python -c "import pydoc; pydoc.writedocs('docs')" || echo "Documentation generation not available"

# Package for distribution
package:
	python setup.py sdist bdist_wheel

# Install in development mode
dev-install:
	pip install -e .
