# Makefile for pypuzzles.

include conf/config.mk

SOURCES = puzzle
DOCS    = README.org README.md

SETUP  = $(PYTHON) setup.py

CLEANFILES = build dist *.egg* *.el __pycache__ .tox
MAKEFLAGS  = --no-print-directory

all: help

dev: ## Set up for developing
	pip install -e .

# Packaging.

wheel sdist: docs ## Build packages
	$(PYTHON) setup.py $@ $(OPTS)

docs: $(DOCS) ## Update doc files

# Testing.

check: test flake mypy ## Run all tests

test: ## Run package tests
	$(PYTHON) -m pytest -v

flake: ## Run flake8 on sources
	flake8 $(SOURCES)

mypy: ## Run mypy on sources
	mypy $(SOURCES)

# Uploading to PyPI.

PYPI   = pypi
FILES  = dist/*

upload-check: ## Check uploads
	twine check $(FILES)

upload-test: wheel sdist ## Upload to pypitest
	@ $(MAKE) upload PYPI=pypitest

upload: wheel sdist ## Upload to pypi
	twine upload -r $(PYPI) --skip-existing $(FILES)

# Other targets.

%.md: %
	pandoc -f rst -o $<.md $<

clean: ## Clean up
	find . -name '*.py[co]' | xargs rm
	rm -rf $(CLEANFILES)

help: ## This help message
	@ echo Targets:
	@ echo
	@ grep -h ":.*##" $(MAKEFILE_LIST) | grep -v 'sed -e' | \
	  sed -e 's/:.*##/:/' | column -t -s:
