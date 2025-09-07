# Module 04 - Python Data-Oriented Design 🎯

Welcome to Module 04 of the Python Piscine! This module explores advanced Python concepts including decorators, functional programming, statistical computing, and modern Python features like dataclasses.

## 📚 Learning Objectives

By completing this module, you will master:
- Decorator patterns and function enhancement
- Statistical analysis and mathematical computations
- Call limiting and function behavior modification
- Modern Python dataclasses and automatic code generation
- Closure patterns and functional programming concepts

## 📋 Exercise Overview

### ex00 - Statistical Analysis Engine
**Focus**: Variadic functions and statistical computations
- Implement comprehensive statistical functions (*args, **kwargs)
- Calculate mean, median, quartile, standard deviation, and variance
- Handle edge cases and invalid input validation
- Advanced mathematical algorithms with error handling

### ex01 - Closure and Function Transformation
**Focus**: Closures, decorators, and functional programming
- Implement mathematical function transformations (square, power)
- Create closure patterns with persistent state
- Build function factories and higher-order functions
- Advanced error handling and type validation

### ex02 - Call Limiting Decorator
**Focus**: Decorator implementation and function behavior control
- Create decorators that limit function call frequency
- Implement function call counting and blocking
- Handle decorator state and persistence
- Practice advanced decorator patterns

### ex03 - Student Data Management
**Focus**: Dataclasses and automatic code generation
- Implement modern Python dataclasses with auto-generated methods
- Create automatic ID and login generation
- Practice field configuration and post-initialization
- Understand dataclass features and benefits

## 🛠️ Technical Skills Developed

### Advanced Python Features
- **Decorators**: Function modification and enhancement
- **Closures**: Persistent state in function scope
- **Dataclasses**: Modern data structure definition
- **Type Hints**: Advanced type annotations and validation

### Functional Programming
- **Higher-Order Functions**: Functions that operate on functions
- **Function Factories**: Dynamic function creation
- **Closure Patterns**: State preservation in functional contexts
- **Immutable Patterns**: Functional programming principles

### Statistical Computing
- **Mathematical Algorithms**: Statistical calculation implementation
- **Data Validation**: Robust input checking and error handling
- **Numerical Stability**: Handling edge cases in calculations
- **Performance Optimization**: Efficient statistical computations

## 🎯 Key Concepts

### Statistical Analysis Engine
```python
def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate statistics for given numbers."""
    if not args:
        for key in kwargs.values():
            print("ERROR")
        return
    
    numbers = sorted(args)
    n = len(numbers)
    
    for key, stat_type in kwargs.items():
        if stat_type == "mean":
            result = sum(numbers) / n
            print(f"mean : {result}")
        # ... other statistics
```

### Closure and Function Transformation
```python
def outer(x: int | float, function) -> object:
    """Create closure with persistent state."""
    count = 0
    
    def inner() -> float:
        nonlocal x, count
        count += 1
        x = function(x)
        return x
    
    return inner
```

### Call Limiting Decorator
```python
def callLimit(limit: int):
    """Decorator factory for limiting function calls."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.call_count >= limit:
                print(f"Error: {func} call too many times")
                return None
            wrapper.call_count += 1
            return func(*args, **kwargs)
        wrapper.call_count = 0
        return wrapper
    return decorator
```

### Modern Dataclasses
```python
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)
    
    def __post_init__(self):
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"
        self.id = generate_id()
```

## 🧪 Advanced Programming Patterns

### Decorator Patterns
- **Function Enhancement**: Adding functionality without modification
- **State Management**: Maintaining decorator state across calls
- **Parameter Handling**: Working with decorator factories
- **Error Propagation**: Maintaining original function behavior

### Statistical Computing
- **Quartile Calculation**: Advanced mathematical algorithms
- **Linear Interpolation**: Smooth statistical calculations
- **Numerical Stability**: Handling floating-point precision
- **Edge Case Management**: Robust error handling

### Data-Oriented Design
- **Dataclass Benefits**: Automatic method generation
- **Field Configuration**: Control over attribute behavior
- **Post-Initialization**: Custom setup after object creation
- **Type Safety**: Enhanced type checking and validation

## 📊 Mathematical Implementations

### Statistical Functions
- **Mean**: Average value calculation
- **Median**: Middle value in sorted data
- **Quartile**: 25th and 75th percentile values
- **Standard Deviation**: Data spread measurement
- **Variance**: Data variability calculation

### Function Transformations
- **Square Function**: x² calculations with overflow protection
- **Power Function**: x^x calculations with validation
- **Closure State**: Persistent variable tracking
- **Error Handling**: Comprehensive exception management

## 🔧 Modern Python Features

### Type System Enhancement
- **Union Types**: `int | float` modern syntax
- **Generic Types**: `list[float]` specifications
- **Optional Returns**: `-> object | None` patterns
- **Comprehensive Annotations**: Full type coverage

### Dataclass Features
- **Field Configuration**: `field(init=False)` patterns
- **Automatic Generation**: `__init__`, `__repr__`, `__eq__`
- **Post-Initialization**: Custom setup logic
- **Default Factories**: Dynamic default value generation

## 🎯 Learning Outcomes

### Advanced Python Mastery
- Deep understanding of decorators and closures
- Proficiency in statistical programming
- Modern Python feature utilization
- Functional programming pattern implementation

### Software Engineering Skills
- Code reusability through decorators
- State management in functional contexts
- Data structure design with dataclasses
- Robust error handling and validation

## 🏆 Real-World Applications

### Data Science and Analytics
- Statistical analysis pipelines
- Data validation and preprocessing
- Mathematical modeling frameworks
- Scientific computing libraries

### Software Architecture
- Decorator-based middleware systems
- Function enhancement and monitoring
- API rate limiting and control
- Configuration and settings management

## 🎉 Module Completion

Upon completing this module, you will have mastered:
- Advanced decorator patterns and implementation
- Statistical computing and mathematical algorithms
- Modern Python features and dataclasses
- Functional programming concepts and closures
- Error handling in complex computational contexts

## 🔗 Professional Development

These advanced skills prepare you for:
- **Senior Software Development**: Complex system architecture
- **Data Science Leadership**: Statistical analysis and modeling
- **Framework Development**: Reusable component creation
- **Performance Engineering**: Optimization and monitoring systems

---

*"Advanced Python is not just about knowing more syntax—it's about thinking in patterns that scale!" 🚀*
