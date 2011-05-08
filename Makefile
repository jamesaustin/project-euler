py_problems := $(wildcard 0*.py)

#python := python
python := pypy

.PHONY: all $(py_problems)
all: $(py_problems)

$(py_problems):
	@$(python) $@
