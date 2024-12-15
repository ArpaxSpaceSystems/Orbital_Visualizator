.PHONY: all
all: install test sphinx coverage

install:
	@pip install .

test:
	@pytest tests

sphinx:
	@make -C doc/html

coverage:
	@coverage run --source src/Orbital_Visualizator_App -m pytest
	@coverage report