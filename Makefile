CLI_FOLDER?=cli
VENV_NAME=test-venv

format: 
	@black --config ./$(CLI_FOLDER)/config/pyproject.toml $(CLI_FOLDER)
	@pylint --rcfile ./$(CLI_FOLDER)/config/.pylintrc $(CLI_FOLDER)

install:
	@pip install "$(filter-out $@,$(MAKECMDGOALS))"
	make freeze




pyinstaller:
	@pyinstaller $(CLI_FOLDER)/config/pyinstaller.spec --clean --noconfirm --distpath $(CLI_FOLDER)/bin/dist --workpath $(CLI_FOLDER)/bin/build
	
setup:
	@echo "setup dependencies"
	make upgrade
	make requirements
	make mandatory
	@echo "setup done"

freeze:
	pip freeze > $(CLI_FOLDER)/requirements.txt

run:
	@python $(CLI_FOLDER)/run.py $(ARGS)

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
	pip install black pylint pyinstaller pytest pytest-cov

venv:
	@echo "check if the venv folder exists"
	[ ! -d "$(FULLPATH)" ] && python -m venv $(FULLPATH)

pytest:
	pytest $(CLI_FOLDER)

coverage:
	pytest --cov-report=html:$(CLI_FOLDER)/bin/coverage_html --cov=$(CLI_FOLDER) --cache-clear $(CLI_FOLDER)

build:
	python .config/pipeline/build.py