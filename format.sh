#!/bin/bash

# Set an exclude pattern for the venv directory (or any other directories you want to exclude)
EXCLUDE_DIR="env"

# Format all Python files using Black
echo "Running Black to format Python files..."
black --line-length=120 --target-version=py310 --exclude $EXCLUDE_DIR .

# Run isort on all Python files, excluding the venv directory
echo "Running isort..."
isort --profile black --filter-files --skip $EXCLUDE_DIR .
