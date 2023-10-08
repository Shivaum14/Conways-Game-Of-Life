# -*- coding: utf-8 -*-
"""A setuptools based setup module."""
from setuptools import find_packages, setup  # type: ignore

REQUIRED = [
    "pygame==2.5.2",
    "isort==5.12.0",
    "flake8==6.1.0",
    "black==23.1.0",
    "mypy==1.3.0",
    "pre-commit==3.4.0",
    "bandit==1.7.5",
    "pylint==3.0.1",
]

setup(
    name="conways-game-of-life",
    version="0.1",
    description="A simple game simulating conway's game of life",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    author="Shivaum Mehta",
    author_email="shivaumm@gmail.com",
    url="https://github.com/Shivaum14/Conways-Game-Of-Life",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={"console_scripts": []},
)
