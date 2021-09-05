# Makefile for pypuz.

include conf/Makefile.conf

SETUP = $(PYTHON) setup.py

PYPI = pypi
CHECK = twine check $(FILES)
UPLOAD = twine upload -r $(PYPI) --skip-existing $(FILES)
FILES = dist/*

CLEANFILES = build dist *.egg* *.zip *.el __pycache__ .tox

MAKEFLAGS = --no-print-directory

.DEFAULT:;	@ $(SETUP) $@ $(OPTS)

all:		develop

develop:;	@ $(SETUP) $@ --user

check:;		$(CHECK)

upload:		wheel sdist
		$(UPLOAD)

upload-test:	wheel sdist
		@ $(MAKE) upload PYPI=pypitest

verify:		test flake

test:;		$(PYTHON) -m pytest -v --emacs

flake:;		flake8 puzzle

clean:;		$(SETUP) $@
		find . -name '*.py[co]' | xargs rm
		rm -rf $(CLEANFILES)
