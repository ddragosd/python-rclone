.PHONY: test 
test:
	pylint rclone*.py
	python -m unittest discover -s . -p "*_test.py" -v
