#!/usr/bin/env python3
"""
Setup script for Solana Detective package
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
def read_requirements():
    """Read requirements from requirements.txt if it exists"""
    requirements_file = "requirements.txt"
    if os.path.exists(requirements_file):
        with open(requirements_file, "r") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return ["requests>=2.25.0"]

setup(
    name="solana-detective",
    version="1.0.0",
    author="AI-Generated Package",
    author_email="ai@solanadetective.dev",
    description="Comprehensive Python package for Solana blockchain analysis using the Solana Tracker API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/solana-detective/solana-detective",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "test": [
            "pytest>=6.0",
            "pytest-mock>=3.0",
            "responses>=0.18.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "solana-detective=solana_detective.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "solana_detective": [
            "*.md",
            "*.json",
            "*.txt",
        ],
    },
    keywords=[
        "solana",
        "blockchain",
        "cryptocurrency",
        "trading",
        "analysis",
        "defi",
        "api",
        "tracker",
        "wallet",
        "token",
    ],
    project_urls={
        "Bug Reports": "https://github.com/solana-detective/solana-detective/issues",
        "Source": "https://github.com/solana-detective/solana-detective",
        "Documentation": "https://solana-detective.readthedocs.io/",
        "API Reference": "https://docs.solanatracker.io/public-data-api/docs",
    },
)

