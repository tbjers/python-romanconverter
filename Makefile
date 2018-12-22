init:
	pip install -r requirements.txt --user

test:
	pytest

clean:
	rm -rf $(wildcard **/__pycache__)
	rm -rf $(wildcard **/*.pyc)
