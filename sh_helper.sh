CLI_FOLDER=cli

VENV_NAME=test-venv

run() {
    make run ARGS="$*"
}

cli() {
    set_python
    echo "Creating virtual environment \"$VENV_NAME\""
    make venv FULLPATH="$CLI_FOLDER/$VENV_NAME"
    echo "Activating virtual environment $VENV_NAME"
    # deactive 
    unset_python
    . $CLI_FOLDER/$VENV_NAME/bin/activate
    make setup
}

set_python() {
    echo "Setting python3.12"
    pyenv local 3.12.0
    # activate python and pip
    eval "$(pyenv init -)"
}

unset_python() {
    echo "Unsetting python3.12"
    pyenv local --unset
}

deactivate_cli() {
    echo "Deactivating virtual environment $VENV_NAME"
    deactivate
}

clir() {
    deactivate_cli
    echo "Removing virtual environment $VENV_NAME"
    rm -rf $VENV_NAME
}

gcop() {
    git add .
    git commit -m "$1"
    git push
}