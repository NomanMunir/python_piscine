black:
	black 00_python_starting/
	black 01_python_array/
	black 02_python_data_table/
	black 03_python_oop/
	black 04_python_Dod/

black-check:
	black --check --diff 00_python_starting/
	black --check --diff 01_python_array/
	black --check --diff 02_python_data_table/
	black --check --diff 03_python_oop/
	black --check --diff 04_python_Dod/

docformat:
	docformatter --wrap-summaries 79 --wrap-descriptions 79 --recursive --in-place 00_python_starting/ || true
	docformatter --wrap-summaries 79 --wrap-descriptions 79 --recursive --in-place 01_python_array/ || true
	docformatter --wrap-summaries 79 --wrap-descriptions 79 --recursive --in-place 02_python_data_table/ || true
	docformatter --wrap-summaries 79 --wrap-descriptions 79 --recursive --in-place 03_python_oop/ || true
	docformatter --wrap-summaries 79 --wrap-descriptions 79 --recursive --in-place 04_python_Dod/ || true

flake8:
	flake8 00_python_starting/
	flake8 01_python_array/
	flake8 02_python_data_table/
	flake8 03_python_oop/
	flake8 04_python_Dod/

format: black docformat

lint: black-check flake8


fclean: clean
	find . -type d -name "__pycache__" -exec rm -r {} + || true
	find . -type f -name "*.pyc" -delete || true
	find . -type f -name ".DS_Store" -delete || true

re: fclean all

help:
	@echo "Available targets:"
	@echo "  flake8         - Run flake8 linting on project directories"
	@echo "  black          - Auto-format Python code using Black (79 chars)"
	@echo "  black-check    - Check what Black would change (dry run)"
	@echo "  docformat      - Format docstrings using docformatter"
	@echo "  format         - Run both black and docformat"
	@echo "  lint           - Run both flake8 and black check"
	@echo "  fclean         - Clean all cache files and bytecode"
	@echo "  re             - Clean and rebuild"
	@echo "  help           - Show this help message"

.PHONY: flake8 black black-check docformat format lint fclean clean re help
