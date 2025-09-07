# Module 03 - Python OOP 🏗️

Welcome to Module 03 of the Python Piscine! This module dives deep into Object-Oriented Programming (OOP) concepts, design patterns, and advanced Python class implementations.

## 📚 Learning Objectives

By completing this module, you will master:
- Abstract base classes and inheritance hierarchies
- Design patterns and polymorphism implementation
- Method overriding and operator overloading
- Class composition and the Diamond Problem
- Static methods and class-based calculator systems

## 📋 Exercise Overview

### ex00 - Character Abstract Base Class
**Focus**: Abstract classes and inheritance fundamentals
- Implement abstract base class using ABC module
- Create concrete implementations with required methods
- Understand abstract method enforcement
- Practice inheritance and method implementation

### ex01 - Baratheon Family Extension
**Focus**: Multiple inheritance and class hierarchies
- Extend character system with family-specific classes
- Implement class attributes and family traits
- Handle complex inheritance relationships
- Practice method resolution order (MRO)

### ex02 - Diamond Trap Problem
**Focus**: Multiple inheritance complexity and resolution
- Solve the classic Diamond Problem in OOP
- Implement cooperative inheritance with super()
- Understand method resolution order complexities
- Practice advanced inheritance patterns

### ex03 - Vector Calculator with Operators
**Focus**: Operator overloading and magic methods
- Implement mathematical operators for vector operations
- Override `__add__`, `__sub__`, `__mul__`, `__truediv__`
- Create intuitive mathematical interfaces
- Handle edge cases like division by zero

### ex04 - Static Method Calculator
**Focus**: Static methods and utility classes
- Implement vector operations using static methods
- Create utility functions without instance state
- Practice dot product and vector arithmetic
- Design clean mathematical interfaces

## 🛠️ Technical Skills Developed

### OOP Fundamentals
- **Abstract Classes**: Using ABC for interface definition
- **Inheritance**: Single and multiple inheritance patterns
- **Polymorphism**: Method overriding and dynamic dispatch
- **Encapsulation**: Data hiding and access control

### Advanced Python Features
- **Magic Methods**: Operator overloading and special methods
- **Static Methods**: Class-level utility functions
- **Method Resolution**: Understanding MRO and super()
- **Design Patterns**: Template method and strategy patterns

### Software Architecture
- **Class Design**: Creating maintainable class hierarchies
- **Interface Definition**: Abstract base class contracts
- **Code Reusability**: Inheritance and composition
- **Error Handling**: Robust exception management

## 🎯 Key Concepts

### Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, first_name: str, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive
    
    @abstractmethod
    def die(self):
        pass
```

### Operator Overloading
```python
class Calculator:
    def __init__(self, vector: list):
        self.vector = vector
    
    def __add__(self, scalar):
        self.vector = [v + scalar for v in self.vector]
        print(self.vector)
    
    def __mul__(self, scalar):
        self.vector = [v * scalar for v in self.vector]
        print(self.vector)
```

### Static Method Implementation
```python
class Calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {result}")
```

## 🧪 Design Patterns Implemented

### Template Method Pattern
- Abstract base classes define algorithm structure
- Concrete classes implement specific steps
- Promotes code reuse and consistency

### Strategy Pattern
- Different implementations of the same interface
- Flexible behavior selection at runtime
- Clean separation of algorithms

### Multiple Inheritance
- Diamond Problem resolution
- Cooperative inheritance with super()
- Method Resolution Order management

## 📊 Problem-Solving Approaches

### The Diamond Problem
Understanding and solving multiple inheritance conflicts:
```
    A
   / \
  B   C
   \ /
    D
```

### Vector Mathematics
Implementing mathematical operations on vector data:
- Addition and subtraction with scalars
- Multiplication and division operations
- Dot product calculations
- Vector arithmetic utilities

## 🔧 Advanced Python Features

### Magic Methods Mastery
- `__init__`: Object initialization
- `__add__`, `__sub__`, `__mul__`, `__truediv__`: Arithmetic operators
- `__str__`, `__repr__`: String representation
- Error handling in operator methods

### Class Architecture
- Abstract base class design
- Interface contracts and enforcement
- Inheritance hierarchies and relationships
- Static utility methods

## 🎯 Learning Outcomes

### Object-Oriented Design
- Creating maintainable class hierarchies
- Understanding when to use inheritance vs composition
- Implementing clean interfaces and contracts
- Solving complex inheritance problems

### Python Expertise
- Advanced use of Python's class system
- Magic method implementation
- Static and class method usage
- Abstract base class patterns

## 🏆 Real-World Applications

### Software Architecture
- Framework design and extension points
- Plugin systems and modular architecture
- API design with clear interfaces
- Reusable component libraries

### Mathematical Computing
- Vector and matrix operations
- Scientific computing interfaces
- Game development math libraries
- Engineering calculation systems

## 🎉 Module Completion

Upon completing this module, you will have mastered:
- Object-oriented programming principles and patterns
- Advanced Python class features and magic methods
- Complex inheritance hierarchies and problem resolution
- Mathematical operator implementation and vector arithmetic
- Abstract interface design and implementation

## 🔗 Career Development

These OOP skills are essential for:
- **Software Engineering**: Large-scale application development
- **Framework Development**: Creating reusable libraries
- **Game Development**: Entity systems and component architecture
- **Scientific Computing**: Mathematical modeling and simulation

---

*"Good object-oriented design is the art of making complex systems simple and maintainable!" 🎨*
