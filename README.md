## 🎯 Project Overview
A comprehensive mathematical utilities library developed collaboratively by a team of contributors. This project demonstrates modern software development practices including version control, automated testing, code quality analysis, and multiple user interfaces. The library provides a wide range of mathematical functions across different domains, from basic arithmetic to advanced statistical analysis.

### 🌟 Key Highlights
- **17 Mathematical Functions** across 4 specialized domains
- **API Interface**: Direct function calls for integration
- **Professional CI/CD** with automated testing
- **Code Quality Tools**: Complexity analysis, linting, security scanning
- **Real-time Visualization** with matplotlib
- **Comprehensive Documentation** and contribution guidelines

## 👥 Team Structure
- **Admin/Integrator**: Repository owner, manages merges, and builds the final driver
- **Contributors (4)**: Each develops a unique module/function based on a shared theme

## 🎨 Theme: Math Utilities & Data Processing
Our shared theme focuses on mathematical utilities and data processing functions that can work together to create a comprehensive toolkit. Each contributor specializes in a specific mathematical domain, ensuring expertise and depth in their respective areas.

## 📁 Project Structure
```
collab-coding-8/
├── README.md                 # 📖 Main documentation
├── main.py                  # 🚀 Main driver with multiple interfaces
├── math_utils.py            # 🧮 Core math utilities (starter file)
├── code_analysis.py         # 🔍 Code quality analysis tool
├── sample_calculations.txt  # 📄 Sample data for batch processing
├── tests/                   # 🧪 Test directory
│   ├── __init__.py
│   ├── test_math_utils.py   # Unit tests for math utilities
│   └── test_contributions.py # Integration tests
├── .github/workflows/       # ⚙️  GitHub Actions CI/CD
│   └── ci.yml              # Automated testing pipeline
├── .flake8                  # 🔧 Flake8 configuration
├── pytest.ini              # 🧪 Pytest configuration
├── Makefile                 # 🛠️  Development commands
├── .gitignore              # 🚫 Git ignore file
└── requirements.txt        # 📦 Python dependencies
```

## ✨ Features

### 🚀 **API Interface**
- **🔌 API Interface**: Direct function calls for integration
  - Clean, well-documented function signatures
  - Type hints for better IDE support
  - Comprehensive error handling

### 🔧 **Development Tools**
- **⚙️ Automated Testing**: GitHub Actions CI/CD pipeline
  - Multi-Python version testing (3.8, 3.9, 3.10, 3.11)
  - Automated linting and security scanning
  - Test coverage reporting
  - Build artifact generation
- **📊 Code Quality**: Radon complexity analysis, flake8 linting
- **🔒 Security**: Bandit security analysis
- **📈 Coverage**: Comprehensive test coverage reporting

### 📊 **Visualization & Analysis**
- **📈 Real-time Plotting**: Matplotlib integration for data visualization
- **🎨 Interactive Charts**: Dynamic plotting for mathematical functions
- **⚡ Batch Processing**: Process multiple calculations at once
- **📋 Data Export**: JSON and text output formats

### 🛠 **Code Analysis & Quality**
- **🔍 Complexity Metrics**: Cyclomatic complexity analysis
- **📊 Maintainability**: Maintainability index calculation
- **🎯 Style Checking**: Automated code style enforcement
- **🔒 Security Scanning**: Vulnerability detection
- **📝 Documentation**: Comprehensive docstrings and type hints

## 🧮 Mathematical Functions

### 📊 **Currently Available**
- **Basic Calculator**: Addition, subtraction, multiplication, division with error handling

### 🔢 **Number Theory & Sequences** (Contributor 1)
- `fibonacci_sequence(n)` - Generate Fibonacci sequence up to n terms
- `prime_number_generator(limit)` - Generate prime numbers using Sieve of Eratosthenes
- `factorial(n)` - Calculate factorial with efficient implementation
- `gcd_lcm(a, b)` - Calculate Greatest Common Divisor and Least Common Multiple

### 🔢 **Linear Algebra & Matrix Operations** (Contributor 2)
- `matrix_multiply(matrix_a, matrix_b)` - Multiply two matrices with validation

#### Matrix Multiplication
`matrix_multiply(matrix_a, matrix_b)` multiplies two matrices and returns the resulting matrix. It validates input types and shapes, raising `TypeError` or `ValueError` for invalid inputs.

**Usage Example:**
```python
from math_utils import matrix_multiply

# Example 1: 2x2 matrices
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = matrix_multiply(matrix_a, matrix_b)
print(result)  # Output: [[19, 22], [43, 50]]

# Example 2: Non-square matrices
matrix_a = [[1, 2, 3], [4, 5, 6]]
matrix_b = [[7, 8], [9, 10], [11, 12]]
result = matrix_multiply(matrix_a, matrix_b)
print(result)  # Output: [[58, 64], [139, 154]]
```

**Error Handling:**
- Raises `ValueError` if matrix shapes are incompatible for multiplication or if matrices are empty.
- Raises `TypeError` if any element is not numeric or if input is not a list of lists.
- `matrix_determinant(matrix)` - Calculate determinant for 2x2 and 3x3 matrices
- `matrix_transpose(matrix)` - Transpose any matrix (swap rows and columns)
- `vector_dot_product(vector_a, vector_b)` - Calculate dot product of two vectors

### 📈 **Statistics & Data Analysis** (Contributor 3)
- `statistical_analysis(data)` - Calculate mean, median, mode, standard deviation
- `linear_regression(x_data, y_data)` - Perform simple linear regression
- `data_normalization(data, method)` - Normalize data using z-score or min-max scaling
- `outlier_detection(data, method)` - Detect outliers using IQR or Z-score method

### 📐 **Geometry & Trigonometry** (Contributor 4)
- `circle_properties(radius)` - Calculate area, circumference, diameter
- `triangle_area_heron(a, b, c)` - Calculate triangle area using Heron's formula
- `distance_2d(point1, point2)` - Calculate Euclidean distance between two 2D points
- `angle_conversion(angle, from_unit, to_unit)` - Convert between degrees, radians, and gradians

## 📋 Contribution Guidelines
1. Each contributor should create a separate branch for their work
2. Functions must include:
   - Clear docstrings/comments
   - Author tag
   - Unit tests in separate test files
3. Submit changes via Pull Requests
4. At least one peer must review each PR before merging
5. Resolve merge conflicts collaboratively

## Getting Started
1. Clone the repository
2. Create a new branch for your feature: `git checkout -b feature/your-feature-name`
3. Implement your function in `math_utils.py`
4. Add corresponding tests in `tests/` directory
5. Submit a Pull Request

## Running the Project

### 🚀 Quick Start
```bash
# Install dependencies
pip3 install -r requirements.txt

# Run demonstration
python3 main.py



# Run code analysis
python3 main.py --analysis
```

### 💡 Usage Examples

#### Basic Calculator
```python
from math_utils import basic_calculator

# Basic operations
result = basic_calculator('add', 5, 3)        # 8
result = basic_calculator('multiply', 6, 7)   # 42
result = basic_calculator('divide', 15, 3)    # 5.0
```



### 🛠️ Development Commands
```bash
# Using Makefile (recommended)
make install          # Install dependencies
make test             # Run all tests
make lint             # Run linting checks
make format           # Format code
make analysis         # Run code analysis
make demo             # Run demonstration
make all              # Run test, lint, and analysis

# Manual commands
python3 -m pytest tests/                  # Run tests
python3 -m flake8 .                       # Lint code
python3 -m black .                        # Format code
python3 code_analysis.py                  # Code analysis
```

### 🧪 Testing
```bash
# Run all tests
python3 -m pytest tests/ -v

# Run with coverage
python3 -m pytest tests/ --cov=math_utils --cov-report=html

# Run specific test file
python3 -m pytest tests/test_math_utils.py -v
```

### 🔍 Code Quality
```bash
# Lint code
python3 -m flake8 math_utils.py

# Format code
python3 -m black math_utils.py

# Security scan
python3 -m bandit -r .

# Code analysis
python3 code_analysis.py --format text
```

## 📊 Project Status

### ✅ **Completed Features**
- [x] Basic calculator with error handling
- [x] Code analysis tools
- [x] Automated testing pipeline
- [x] Comprehensive documentation
- [x] Development tools and configuration

### 📈 **Test Coverage**
- **Current**: 7/7 tests passing (100% for implemented functions)
- **Target**: 90%+ coverage for all functions
- **Status**: All basic calculator tests passing

## 🖥️ Interface Options



### 3. **🔍 Code Analysis** (`python3 main.py --analysis`)
- Cyclomatic complexity analysis
- Maintainability index calculation
- Code style checking (flake8)
- Security analysis (bandit)
- Test coverage reporting

## Team Members

### Core Team
- **[Admin]** - Repository setup and integration
- **[Contributor 1]** - Number Theory & Sequences
- **[Contributor 2]** - Linear Algebra & Matrix Operations  
- **[Contributor 3]** - Statistics & Data Analysis
- **[Contributor 4]** - Geometry & Trigonometry

### Team Structure & Assignments

#### **Contributor 1: Number Theory & Sequences**
**Functions to implement:**
1. `fibonacci_sequence(n: int) -> List[int]` - Generate Fibonacci sequence
2. `prime_number_generator(limit: int) -> List[int]` - Generate prime numbers using Sieve of Eratosthenes
3. `factorial(n: int) -> int` - Calculate factorial with efficient implementation
4. `gcd_lcm(a: int, b: int) -> Tuple[int, int]` - Calculate GCD and LCM using Euclidean algorithm

#### **Contributor 2: Linear Algebra & Matrix Operations**
**Functions to implement:**
1. `matrix_multiply(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]` - Matrix multiplication
2. `matrix_determinant(matrix: List[List[float]]) -> float` - Calculate matrix determinant
3. `matrix_transpose(matrix: List[List[float]]) -> List[List[float]]` - Transpose matrices
4. `vector_dot_product(vector_a: List[float], vector_b: List[float]) -> float` - Calculate dot product

#### **Contributor 3: Statistics & Data Analysis**
**Functions to implement:**
1. `statistical_analysis(data: List[float]) -> dict` - Calculate mean, median, mode, std dev
2. `linear_regression(x_data: List[float], y_data: List[float]) -> dict` - Perform linear regression
3. `data_normalization(data: List[float], method: str = 'z_score') -> List[float]` - Normalize data
4. `outlier_detection(data: List[float], method: str = 'iqr') -> List[float]` - Detect outliers

#### **Contributor 4: Geometry & Trigonometry**
**Functions to implement:**
1. `circle_properties(radius: float) -> dict` - Calculate circle area, circumference, diameter
2. `triangle_area_heron(a: float, b: float, c: float) -> float` - Calculate triangle area using Heron's formula
3. `distance_2d(point1: Tuple[float, float], point2: Tuple[float, float]) -> float` - Calculate 2D distance
4. `angle_conversion(angle: float, from_unit: str, to_unit: str) -> float` - Convert angle units

### Development Workflow

#### **Step 1: Initial Setup**
```bash
# Clone the repository
git clone <repository-url>
cd collab-coding-8

# Install dependencies
pip3 install -r requirements.txt

# Verify setup by running tests
python3 -m pytest tests/
```

#### **Step 2: Create Your Feature Branch**
```bash
# Create and switch to your feature branch
git checkout -b feature/contributor-name-functions

# Example:
git checkout -b feature/contributor1-number-theory
```

#### **Step 3: Implement Your Functions**

1. **Add your functions to `math_utils.py`:**
   - Find your designated section (marked with TODO comments)
   - Replace the placeholder with your actual implementation
   - Follow the exact function signatures provided above

2. **Function Documentation Template:**
```python
def your_function(param1: type, param2: type) -> return_type:
    """
    Brief description of what the function does.
    
    Args:
        param1 (type): Description of parameter
        param2 (type): Description of parameter
        
    Returns:
        return_type: Description of return value
        
    Raises:
        ValueError: When specific error conditions occur
        TypeError: When wrong parameter types are provided
        
    @author: [Your Full Name]
    """
    # Your implementation here
    pass
```

3. **Error Handling Requirements:**
   - Validate all input parameters
   - Raise `ValueError` for invalid values
   - Raise `TypeError` for wrong parameter types
   - Include descriptive error messages

#### **Step 4: Create Comprehensive Tests**

1. **Create your test file:**
```bash
# Create test file in tests/ directory
touch tests/test_[your-name].py
```

2. **Test File Template:**
```python
"""
Unit tests for [Your Name]'s math utility functions.

@author: [Your Full Name]
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from math_utils import your_function1, your_function2, your_function3, your_function4


class TestYourFunctions(unittest.TestCase):
    """Test cases for your mathematical utility functions."""
    
    def test_function1_normal_cases(self):
        """Test normal operation of function1."""
        # Test cases here
        pass
    
    def test_function1_edge_cases(self):
        """Test edge cases for function1."""
        # Edge cases here
        pass
    
    def test_function1_error_cases(self):
        """Test error conditions for function1."""
        # Error cases here
        pass
    
    # Repeat for all 4 functions


if __name__ == '__main__':
    unittest.main()
```

3. **Testing Requirements:**
   - Test normal cases with typical inputs
   - Test edge cases (empty lists, zero values, boundary conditions)
   - Test error conditions (invalid inputs, wrong types)
   - Aim for 90%+ code coverage
   - Each function should have at least 5-8 test cases

#### **Step 5: Test Your Implementation**

```bash
# Run all tests to ensure nothing is broken
python3 -m pytest tests/

# Run only your tests
python3 -m pytest tests/test_[your-name].py -v

# Run the main program to see your functions in action
python3 main.py
```

#### **Step 6: Commit and Push Your Changes**

```bash
# Stage your changes
git add math_utils.py
git add tests/test_[your-name].py

# Commit with descriptive message
git commit -m "Add [your-name] functions: [list your 4 functions]

- Implemented fibonacci_sequence, prime_number_generator, factorial, gcd_lcm
- Added comprehensive unit tests
- Includes proper error handling and documentation
- All tests passing"

# Push your branch to remote repository
git push origin feature/[your-name]-functions
```

#### **Step 7: Create Pull Request**

1. **Go to GitHub repository**
2. **Click "Compare & pull request"** (should appear after pushing)
3. **Fill out PR template:**
   - **Title:** `Add [Your Name] Functions: [Function Categories]`
   - **Description:**
     ```markdown
     ## Summary
     Implements 4 mathematical utility functions as assigned:
     - [Function 1]: [Brief description]
     - [Function 2]: [Brief description]
     - [Function 3]: [Brief description]
     - [Function 4]: [Brief description]
     
     ## Changes Made
     - Added functions to `math_utils.py`
     - Created comprehensive test suite in `tests/test_[your-name].py`
     - All functions include proper documentation and error handling
     
     ## Testing
     - [ ] All existing tests pass
     - [ ] New tests cover normal, edge, and error cases
     - [ ] Functions work correctly with sample data
     
     ## Checklist
     - [ ] Functions follow exact signatures provided
     - [ ] Documentation includes @author tag
     - [ ] Error handling implemented
     - [ ] Tests are comprehensive
     - [ ] Code follows project style guidelines
     ```

### Quick Contribution Steps
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Implement your changes
4. Add tests for your code
5. Submit a pull request
