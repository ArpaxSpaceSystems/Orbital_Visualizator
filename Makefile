.PHONY: all
all: install test coverage

install:
	@pip install .

test:
	@pytest tests

coverage:
	@coverage run --source src/Orbital_Visualizator -m pytest
	@coverage report