"""This module is solely for building cli application
Contains script to setup a venv and install dependencies
Then run formatting, linting, and testing
Then use pyinstaller to build the cli application
Then run sanity test to call --version
"""

import os

VENV = "build-venv"

def create_venv():
    """Create venv"""
    if os.path.exists(VENV):
        print("venv already exists")
        return
    
    print("Creating venv")
    os.system(f"python -m venv {VENV}")
    print("Created venv")

def install_dependencies():
    """Install dependencies"""
    print("Installing dependencies")
    os.system("pip install --upgrade pip setuptools wheel")
    os.system("pip install -r requirements.txt")
    print("Installed dependencies")

def run_formatting():
    """Run formatting"""
    print("Running formatting")
    os.system("black --config cli/.config/pyproject.toml cli")
    print("Ran formatting")

def run_linting():
    """Run linting"""
    print("Running linting")
    os.system("pylint --rcfile cli/.config/pylintrc cli")
    print("Ran linting")

def run_testing():
    """Run testing"""
    print("Running testing")
    os.system("pytest --cov=cli --cov-report=xml --cov-report=html")
    print("Ran testing")

def build_cli():
    """Build cli"""
    print("Building cli")
    