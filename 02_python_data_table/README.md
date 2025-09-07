# Module 02 - Python Data Table 📊

Welcome to Module 02 of the Python Piscine! This module focuses on data analysis and visualization using Pandas and Matplotlib, working with real-world datasets to extract meaningful insights.

## 📚 Learning Objectives

By completing this module, you will master:
- Pandas DataFrame operations and CSV file handling
- Data visualization with Matplotlib for statistical analysis
- Population and demographic data analysis
- Cross-dataset correlation and comparison
- Statistical trend analysis and projection

## 📋 Exercise Overview

### ex00 - CSV Data Loading
**Focus**: Data import and DataFrame fundamentals
- Load CSV files into Pandas DataFrames
- Handle file I/O errors and data validation
- Display dataset dimensions and basic information
- Implement robust error handling for data loading

### ex01 - Life Expectancy Visualization
**Focus**: Single dataset analysis and plotting
- Analyze life expectancy data over time
- Create line plots for country-specific trends
- Handle missing data and interpolation
- Implement data filtering and selection

### ex02 - Population Comparison
**Focus**: Multi-country data comparison
- Compare population data between countries
- Create comparative visualizations
- Format large numbers for readability (millions)
- Implement custom formatting functions

### ex03 - Life Expectancy vs GDP Projection
**Focus**: Multi-dataset correlation analysis
- Correlate life expectancy with GDP per capita
- Create scatter plots showing relationships
- Handle data from multiple CSV sources
- Implement cross-dataset data alignment

## 🛠️ Technical Skills Developed

### Pandas Mastery
- **DataFrame Operations**: Creation, indexing, and manipulation
- **Data Loading**: CSV import with error handling
- **Data Cleaning**: Missing value handling and validation
- **Data Filtering**: Boolean indexing and conditional selection

### Data Visualization
- **Matplotlib Integration**: Creating professional plots
- **Chart Types**: Line plots, scatter plots, and comparisons
- **Formatting**: Axis labels, titles, and legends
- **Custom Styling**: Colors, markers, and visual aesthetics

### Statistical Analysis
- **Trend Analysis**: Temporal data patterns
- **Correlation**: Relationship between variables
- **Data Projection**: Predictive analysis techniques
- **Comparative Analysis**: Multi-dataset insights

## 🎯 Key Concepts

### Data Loading and Validation
```python
import pandas as pd

def load(path: str) -> pd.DataFrame | None:
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None
```

### Data Visualization Pipeline
```python
import matplotlib.pyplot as plt

# Create professional visualizations
plt.figure(figsize=(10, 6))
plt.plot(years, data, label="Country Data")
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Data Analysis")
plt.legend()
plt.show()
```

### Multi-Dataset Analysis
```python
# Cross-reference multiple datasets
life_df = load("life_expectancy.csv")
income_df = load("income_per_person.csv")

# Align and analyze data
merged_data = life_df.merge(income_df, on="country")
```

## 🧪 Real-World Datasets

### Life Expectancy Data
- Global life expectancy trends by country
- Temporal analysis from historical data
- Health and demographic insights

### Population Statistics
- Total population by country over time
- Population growth analysis and trends
- Demographic transition patterns

### Economic Indicators
- GDP per capita (PPP adjusted)
- Economic development correlation
- Income and health relationship analysis

## 📊 Visualization Techniques

### Professional Plotting
- Clean, readable chart formatting
- Appropriate axis scaling and labeling
- Color schemes for data distinction
- Statistical trend visualization

### Data Formatting
- Large number formatting (millions, billions)
- Percentage and ratio calculations
- Time series data handling
- Custom formatter functions

## 🔧 Dependencies

- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization and plotting
- **NumPy**: Numerical operations support

## 🎯 Learning Outcomes

### Data Science Fundamentals
- Understanding of DataFrame operations
- Proficiency in data visualization
- Statistical analysis capabilities
- Real-world data handling experience

### Analytical Thinking
- Pattern recognition in data
- Correlation analysis skills
- Trend identification and interpretation
- Data-driven decision making

## 🌍 Global Insights

This module works with real global data to understand:
- **Health Trends**: Life expectancy improvements worldwide
- **Population Dynamics**: Growth patterns and demographic changes
- **Economic Development**: Relationship between wealth and health
- **Data Storytelling**: Extracting meaningful narratives from numbers

## 🎉 Module Completion

Upon completing this module, you will have mastered:
- Pandas for data manipulation and analysis
- Matplotlib for creating professional visualizations
- Statistical analysis of real-world datasets
- Cross-dataset correlation and comparison techniques
- Data storytelling and insight extraction

## 🔗 Career Applications

These skills are directly applicable to:
- **Data Science**: Analytics and machine learning preprocessing
- **Business Intelligence**: Report generation and KPI tracking
- **Research**: Academic and scientific data analysis
- **Finance**: Market analysis and economic modeling

---

*"Data is the new oil, but visualization is the refinery that makes it valuable!" 📈*
