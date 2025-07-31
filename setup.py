#!/usr/bin/env python3
"""
Setup script for BasicIDE
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="basicIDE",
    version="1.3.0",
    author="WillZLog",
    author_email="williamalbinze@gmail.com",
    description="Basic IDE with AI-Powered Features",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/WillZLog/BasicIDE",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Integrated Development Environments (IDE)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "basicide=vscode_clone:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.py"],
    },
    keywords="ide, python, editor, development, ai, code-analysis",
    project_urls={
        "Bug Reports": "https://github.com/WillZLog/BasicIDE/issues",
        "Source": "https://github.com/WillZLog/BasicIDE",
        "Documentation": "https://github.com/WillZLog/BasicIDE#readme",
    },
) 