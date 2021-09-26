# Makefile for package configuration.

include config.mk

REQ = requirements
DEV = dev-requirements
TXT = $(REQ).txt $(DEV).txt

COMPILE = $(PYTHON) -m piptools compile -v

all: requirements

requirements: $(TXT)

%.txt: %.in constraints.txt
	@ echo Making $@
	@ $(COMPILE) $< -o $@
