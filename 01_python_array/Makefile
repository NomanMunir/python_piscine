flake:
	@flake8 ex*/*

fclean: clean
	find . -type d -name "__pycache__" -exec rm -r {} + || true
	find . -type f -name "*.pyc" -delete || true


re: fclean all
