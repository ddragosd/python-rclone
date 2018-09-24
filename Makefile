.PHONY: test 
test:
	python -m unittest discover -s . -p "*_test.py" -v
