# Module 01 - Python Array 🔢

Welcome to Module 01 of the Python Piscine! This module focuses on numerical computing with NumPy and practical applications in image processing, mathematical calculations, and data visualization.

## 📚 Learning Objectives

By completing this module, you will master:
- NumPy array operations and mathematical computations
- Image loading, processing, and manipulation techniques
- BMI calculations and statistical analysis
- Color space transformations and image filtering
- Array slicing and dimensional operations

## 📋 Exercise Overview

### ex00 - BMI Calculator
**Focus**: Mathematical computations and data validation
- Calculate Body Mass Index from height and weight arrays
- Implement limit checking with boolean arrays
- Error handling for invalid inputs and edge cases
- Type safety with comprehensive input validation

### ex01 - Array 2D Manipulation
**Focus**: NumPy array slicing and shape operations
- Work with 2D arrays and dimensional analysis
- Implement array slicing with start and end indices
- Shape reporting and transformation validation
- Converting between NumPy arrays and Python lists

### ex02 - Image Loading
**Focus**: Image file handling and data representation
- Load and process JPEG images using PIL/Pillow
- Convert images to NumPy arrays for manipulation
- Display image properties (shape, channels, data type)
- Handle various image formats and error conditions

### ex03 - Image Zooming
**Focus**: Array manipulation and image transformation
- Implement image cropping and zoom functionality
- Work with array indexing for region selection
- Maintain aspect ratios during transformations
- Display original and modified image properties

### ex04 - Image Rotation
**Focus**: Advanced array operations and transformations
- Implement 90-degree image rotation using NumPy
- Transpose and flip operations for geometric transformations
- Understand array axis manipulation
- Preserve image quality during rotation operations

### ex05 - Image Color Manipulation
**Focus**: Color space operations and channel manipulation
- Implement color inversion and channel isolation
- RGB channel separation and recombination
- Grayscale conversion using weighted averages
- Apply various color filters and effects

## 🛠️ Technical Skills Developed

### NumPy Mastery
- **Array Creation**: From lists, ranges, and image data
- **Shape Operations**: Reshaping, slicing, and indexing
- **Mathematical Operations**: Element-wise calculations
- **Boolean Indexing**: Conditional array operations

### Image Processing
- **File I/O**: Loading images with PIL/Pillow
- **Data Conversion**: Between image formats and NumPy arrays
- **Transformations**: Rotation, cropping, and scaling
- **Color Manipulation**: Channel operations and filtering

### Mathematical Computing
- **Statistical Analysis**: BMI calculations and health metrics
- **Data Validation**: Type checking and range validation
- **Error Handling**: Robust exception management
- **Performance**: Efficient array operations

## 🎯 Key Concepts

### Array Operations
```python
import numpy as np

# Array creation and manipulation
array = np.array(data)
print(f"Shape: {array.shape}")

# Slicing and indexing
sliced = array[start:end]
```

### Image Processing Pipeline
```python
from PIL import Image
import numpy as np

# Load image
image = Image.open("image.jpg")
array = np.array(image)

# Process and display
print(f"The shape of image is: {array.shape}")
```

### Mathematical Computations
```python
# BMI calculation with validation
def give_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

# Boolean array operations
def apply_limit(bmi, limit):
    return bmi > limit
```

## 🧪 Practical Applications

### Health and Fitness
- BMI calculations for health assessment
- Statistical analysis of health metrics
- Data visualization for health trends

### Image Processing
- Photo editing and enhancement
- Computer vision preprocessing
- Medical image analysis
- Graphics and visual effects

### Data Science
- Array-based computations
- Statistical analysis and modeling
- Data transformation and cleaning
- Numerical computing workflows

## 📊 Skills Progression

1. **Basic Arrays** → Understanding NumPy fundamentals
2. **2D Operations** → Working with matrices and images
3. **Image Loading** → File I/O and data conversion
4. **Transformations** → Geometric and color operations
5. **Advanced Processing** → Complex image manipulation

## 🔧 Dependencies

- **NumPy**: Numerical computing library
- **Pillow (PIL)**: Python Imaging Library
- **Matplotlib**: For image display and visualization

## 🎉 Module Completion

Upon completing this module, you will have mastered:
- NumPy array operations and mathematical computing
- Image processing fundamentals and techniques
- Data validation and error handling in numerical contexts
- Color space manipulation and transformation
- Performance optimization for array operations

## 🔗 Integration with Other Modules

This module provides essential skills for:
- **Module 02**: Data analysis with Pandas
- **Module 03**: Object-oriented design patterns
- **Advanced Projects**: Computer vision and machine learning

---

*"Arrays are the foundation of numerical computing - master them, and unlock the power of data science!" 🚀*
