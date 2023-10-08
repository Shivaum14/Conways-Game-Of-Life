#!/bin/bash

# Set an exclude pattern for the venv directory (or any other directories you want to exclude)
EXCLUDE_DIR="env"

# Run isort on all Python files
echo "Running isort..."
isort --profile black --skip $EXCLUDE_DIR --check .

# Run flake8 on all Python files
echo "Running flake8..."
#flake8 . --max-line-length=120 --ignore=ANN101,D202,ANN002,ANN003,ANN102,CFQ002,W503
flake8 . --max-line-length=120 --exclude=$EXCLUDE_DIR

# Run mypy for type checking
echo "Running mypy..."
mypy . --exclude $EXCLUDE_DIR

echo "Done!"
