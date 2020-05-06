PYTHONPATH := "src:tests"

.PHONY: test
test: unit_test doctest
	python -m coverage combine .coverage-*
	python -m coverage xml
	python -m coverage html
	python -m coverage report

.PHONY: unit_test
unit_test:
	COVERAGE_FILE=.coverage-unit PYTHONPATH=$(PYTHONPATH) python -m pytest tests/unit --junitxml=test-results-unit.xml

.PHONY: doctest
doctest:
	COVERAGE_FILE=.coverage-doctest PYTHONPATH=$(PYTHONPATH) python -m pytest --doctest-modules src --junitxml=test-results-doctest.xml


.PHONY: docs
docs:
	$(MAKE) -C docs html

.PHONY: mypy
mypy:
	python -m mypy src/arsenal

.PHONY: clean
clean: clean-docs clean-build


.PHONY: clean-docs
clean-docs:
	$(MAKE) -C docs clean

.PHONY: clean-build
clean-build:
	@rm -rf dist build
