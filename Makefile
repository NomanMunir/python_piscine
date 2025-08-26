
autopep8:
	autopep8 --in-place --aggressive --aggressive --recursive 00_python_starting/
	autopep8 --in-place --aggressive --aggressive --recursive 01_python_array/
	autopep8 --in-place --aggressive --aggressive --recursive 02_python_data_table/
	autopep8 --in-place --aggressive --aggressive --recursive 03_python_oop/
	autopep8 --in-place --aggressive --aggressive --recursive 04_python_Dod/

autopep8-check:
	autopep8 --diff --aggressive --aggressive --recursive 00_python_starting/
	autopep8 --diff --aggressive --aggressive --recursive 01_python_array/
	autopep8 --diff --aggressive --aggressive --recursive 02_python_data_table/
	autopep8 --diff --aggressive --aggressive --recursive 03_python_oop/
	autopep8 --diff --aggressive --aggressive --recursive 04_python_Dod/

format: autopep8

lint: autopep8-check


fclean: clean
	find . -type d -name "__pycache__" -exec rm -r {} + || true
	find . -type f -name "*.pyc" -delete || true
	find . -type f -name ".DS_Store" -delete || true

re: fclean all

help:
	@echo "Available targets:"
	@echo "  flake          - Run flake8 linting"
	@echo "  autopep8       - Auto-format Python code using autopep8"
	@echo "  autopep8-check - Check what autopep8 would change (dry run)"
	@echo "  format         - Alias for autopep8"
	@echo "  lint           - Run both flake8 and autopep8 check"
	@echo "  fclean         - Clean all cache files and bytecode"
	@echo "  re             - Clean and rebuild"
	@echo "  help           - Show this help message"

.PHONY: flake autopep8 autopep8-check format lint fclean clean re help
