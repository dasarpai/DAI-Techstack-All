all:
	$(error please pick a target)

dev-env:
	test -d venv || virtualenv venv
	./venv/bin/python -m pip install -r requirements-dev.txt

test:
	find . -name '*.pyc' -exec rm -f {} \;
	./venv/bin/flake8 nlp tests
	./venv/bin/python -m pytest \
	    --doctest-modules \
	    --disable-warnings \
	    --verbose \
	    slowmath tests
