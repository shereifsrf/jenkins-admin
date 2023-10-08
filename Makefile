CLI_FOLDER?=cli
VENV_NAME=test-venv

run:
	@python $(CLI_FOLDER)/run.py

format: 
	@black --config ./$(CLI_FOLDER)/config/pyproject.toml $(CLI_FOLDER)
	@pylint --rcfile ./$(CLI_FOLDER)/config/.pylintrc $(CLI_FOLDER)

freeze:
	pip freeze > $(CLI_FOLDER)/requirements.txt
	
setup:
	@echo "setup dependencies"
	make upgrade
	make requirements
	@echo "setup done"



unsetup:
	@echo "uninstall dependencies"
	pip uninstall -r $(CLI_FOLDER)/requirements.txt -y	


create-pylintrc:
	pylint --generate-rcfile > $(CLI_FOLDER)/config/.pylintrc

requirements:
	pip install -r $(CLI_FOLDER)/requirements.txt

upgrade:
	pip install --upgrade pip setuptools wheel

mandatory:
	make upgrade
	pip install black pylint

venv:
	@echo "check if the venv folder exists"
	[ ! -d "$(FULLPATH)" ] && python -m venv $(FULLPATH)