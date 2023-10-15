"""This module is solely for building cli application
Contains script to setup a venv and install dependencies
Then run formatting, linting, and testing
Then use pyinstaller to build the cli application
Then run sanity test to call --version
"""

import os

VENV = "cli/build-venv"
build_env = f". {VENV}/bin/activate"

def command(cmd: str):
    """Run command"""
    os.system(f"{build_env} && {cmd}")

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
    # os.system("pip install --upgrade pip setuptools wheel")
    # os.system("pip install -r cli/requirements.txt")
    command("pip install --upgrade pip setuptools wheel")
    command("pip install -r cli/requirements.txt")
    print("Installed dependencies")

def run_formatting():
    """Run formatting"""
    print("Running formatting")
    # os.system("black --config cli/config/pyproject.toml cli")
    command("black --config cli/config/pyproject.toml cli")
    print("Ran formatting")

def run_linting():
    """Run linting"""
    print("Running linting")
    # os.system("pylint --rcfile cli/config/.pylintrc cli")
    command("pylint --rcfile cli/config/.pylintrc cli")
    print("Ran linting")

def run_testing():
    """Run testing"""
    print("Running testing")
    # os.system("pytest --cov-report=html:cli/bin/coverage_html --cov=cli --cache-clear cli")
    command("pytest --cov-report=html:cli/bin/coverage_html --cov=cli --cache-clear cli")
    print("Ran testing")

def build_cli():
    """Build cli"""
    print("Building cli")
    # os.system("pyinstaller cli/config/pyinstaller.spec --clean --noconfirm --distpath cli/bin/dist --workpath cli/bin/build")
    command("pyinstaller cli/config/pyinstaller.spec --clean --noconfirm --distpath cli/bin/dist --workpath cli/bin/build")


if __name__ == "__main__":
    print("Starting build")
    create_venv()
    install_dependencies()
    run_formatting()
    run_linting()
    run_testing()
    build_cli()
    print("Finished build")
    