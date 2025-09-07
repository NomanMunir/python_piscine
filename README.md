# Python Piscine 🐍

Welcome to the **Python Piscine** - a comprehensive collection of Python programming exercises designed to build proficiency in Python fundamentals, data manipulation, object-oriented programming, and advanced programming concepts.

## 📚 About This Project

This repository contains a structured learning path through Python programming, organized into progressive modules that cover essential Python concepts and practical applications. Each module builds upon the previous one, creating a comprehensive learning experience from basic syntax to advanced programming patterns.

## 🏗️ Project Structure

```
python_piscine/
├── 00_python_starting/     # Python fundamentals and basic syntax
├── 01_python_array/        # NumPy arrays and image manipulation  
├── 02_python_data_table/   # Pandas dataframes and data analysis
├── 03_python_oop/          # Object-oriented programming concepts
├── 04_python_Dod/          # Data-oriented design and decorators
├── subjects/               # Exercise specifications and requirements
└── Makefile               # Development tools and automation
```

## 🎯 Learning Objectives

### Module 00 - Python Starting
- **Python basics**: Variables, data types, control structures
- **String manipulation**: Formatting, filtering, and text processing
- **Package creation**: Building and distributing Python packages
- **Error handling**: Exception management and validation

### Module 01 - Python Array
- **NumPy fundamentals**: Array operations and mathematical computations
- **Image processing**: Loading, manipulating, and transforming images
- **BMI calculations**: Statistical analysis and data validation
- **Image filters**: Color manipulation and visual effects

### Module 02 - Python Data Table
- **Pandas mastery**: DataFrame operations and CSV handling
- **Data visualization**: Creating charts and graphs with matplotlib
- **Statistical analysis**: Population and life expectancy trends
- **Data correlation**: Cross-referencing multiple datasets

### Module 03 - Object-Oriented Programming
- **Class design**: Abstract base classes and inheritance
- **Design patterns**: Implementation of OOP principles
- **Polymorphism**: Method overriding and dynamic behavior
- **Calculator systems**: Mathematical operations with classes

### Module 04 - Data-Oriented Design
- **Decorators**: Function modification and enhancement
- **Statistical functions**: Advanced mathematical computations
- **Dataclasses**: Modern Python data structures
- **Functional programming**: Higher-order functions and closures

## 🛠️ Technical Requirements

- **Python Version**: 3.10 or higher
- **Key Dependencies**:
  - `numpy` - Numerical computing
  - `pandas` - Data manipulation and analysis
  - `matplotlib` - Data visualization
  - `pillow` - Image processing
  - `tqdm` - Progress bars and loading indicators

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd python_piscine
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run code formatting**:
   ```bash
   make format
   ```

4. **Run linting checks**:
   ```bash
   make lint
   ```

## 🧪 Development Tools

This project includes comprehensive development tools managed through the Makefile:

- **Code Formatting**: Black formatter with 79-character line limit
- **Linting**: Flake8 for code quality and style checking
- **Documentation**: Docformatter for consistent docstring formatting
- **Cleanup**: Automated removal of cache files and artifacts

### Available Make Commands

```bash
make format      # Format code with Black and docformatter
make lint        # Run linting checks with Black and Flake8
make fclean      # Clean all cache files and artifacts
make help        # Display all available commands
```

## 📋 Exercise Overview

Each module contains multiple exercises that progressively increase in complexity:

- **ex00-ex09**: Numbered exercises with specific learning objectives
- **tester.py**: Test files demonstrating expected functionality
- **README.md**: Detailed explanations and implementation guides

## 🏆 Key Features

- ✅ **Comprehensive Error Handling**: Robust exception management across all modules
- ✅ **Type Annotations**: Full type hints for better code clarity and IDE support
- ✅ **Professional Documentation**: Detailed docstrings following Python conventions
- ✅ **Code Quality**: Consistent formatting and linting standards
- ✅ **Practical Applications**: Real-world examples and use cases
- ✅ **Progressive Learning**: Structured curriculum building from basics to advanced

## 📊 Skills Developed

By completing this piscine, you will gain proficiency in:

- **Core Python**: Syntax, data structures, control flow
- **Data Science**: NumPy, Pandas, statistical analysis
- **Object-Oriented Design**: Classes, inheritance, polymorphism
- **Image Processing**: Manipulation and transformation techniques
- **Data Visualization**: Charts, graphs, and visual analytics
- **Software Engineering**: Code quality, testing, and documentation

## 🤝 Contributing

This project follows strict coding standards:

- **PEP 8**: Python style guide compliance
- **Type Safety**: Comprehensive type annotations
- **Documentation**: Detailed docstrings and comments
- **Testing**: Thorough validation and edge case handling

## 📜 License

This project is educational material designed for learning Python programming concepts and best practices.

---

*Happy coding! 🐍✨*
