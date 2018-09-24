.PHONY: test 
test:
	pylint *.py
	python -m unittest discover -s . -p "*_test.py" -v

package:
	python3 setup.py sdist bdist_wheel

publish: package
	-twine upload --repository-url https://test.pypi.org/legacy/ dist/*
