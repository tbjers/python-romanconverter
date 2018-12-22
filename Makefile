init:
	pip install -r requirements.txt

virtualenv:
	pip install --editable .

test:
	pytest

coverage:
	pytest --cov-report term-missing --cov-report html:htmlcov --cov=romanconverter

clean:
	rm -rf $(wildcard **/__pycache__)
	rm -rf $(wildcard **/*.pyc)
