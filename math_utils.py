"""
Math Utilities Module
A collaborative collection of mathematical utility functions.

This module serves as the main file where team members will contribute
their mathematical utility functions. Each function should be well-documented
and include proper error handling.

@author: Admin (Repository Owner)
"""

import math
from typing import List, Union, Tuple


def basic_calculator(operation: str, a: float, b: float) -> float:
    """
    Basic calculator function for fundamental arithmetic operations.
    
    This is a placeholder function that contributors can use as a reference
    for the expected function structure and documentation format.
    
    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
        a (float): First operand
        b (float): Second operand
        
    Returns:
        float: Result of the operation
        
    Raises:
        ValueError: If operation is not supported or division by zero
        
    @author: Admin (Repository Owner)
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")


# =============================================================================
# CONTRIBUTOR FUNCTIONS - Add your functions below this line
# =============================================================================

# TODO: Contributor 1 - Add your function here
# Example:
# def fibonacci_sequence(n: int) -> List[int]:
#     """
#     Generate Fibonacci sequence up to n terms.
#     
#     Args:
#         n (int): Number of terms to generate
#         
#     Returns:
#         List[int]: List containing the Fibonacci sequence
#         
#     @author: [Your Name]
#     """
#     pass

# TODO: Contributor 2 - Add your function here
# TODO: Contributor 2 - Add your function here
def matrix_multiply(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices.

    Args:
        matrix_a (List[List[float]]): First matrix
        matrix_b (List[List[float]]): Second matrix

    Returns:
        List[List[float]]: Resulting matrix

    Raises:
        ValueError: If matrices cannot be multiplied due to shape mismatch
        TypeError: If input is not a list of lists of numbers

    @author: Contributor 2
    """
    # Validate input types
    if not (isinstance(matrix_a, list) and all(isinstance(row, list) for row in matrix_a)):
        raise TypeError("matrix_a must be a list of lists")
    if not (isinstance(matrix_b, list) and all(isinstance(row, list) for row in matrix_b)):
        raise TypeError("matrix_b must be a list of lists")
    if len(matrix_a) == 0 or len(matrix_b) == 0:
        raise ValueError("Input matrices cannot be empty")
    if any(len(row) != len(matrix_a[0]) for row in matrix_a):
        raise ValueError("All rows in matrix_a must have the same length")
    if any(len(row) != len(matrix_b[0]) for row in matrix_b):
        raise ValueError("All rows in matrix_b must have the same length")
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in matrix_a must equal number of rows in matrix_b")

    result = []
    for i in range(len(matrix_a)):
        result_row = []
        for j in range(len(matrix_b[0])):
            sum_product = 0.0
            for k in range(len(matrix_b)):
                a_val = matrix_a[i][k]
                b_val = matrix_b[k][j]
                if not isinstance(a_val, (int, float)) or not isinstance(b_val, (int, float)):
                    raise TypeError("Matrix elements must be numeric")
                sum_product += a_val * b_val
            result_row.append(sum_product)
        result.append(result_row)
    return result


# Contributor 3 - Statistics & Data Analysis Functions
# @author: Contributor 3

def statistical_analysis(data: List[float]) -> dict:
    """
    Perform basic statistical analysis on a dataset.
    
    Calculates mean, median, mode, and standard deviation for the given dataset.
    
    Args:
        data (List[float]): Input dataset
        
    Returns:
        dict: Dictionary containing mean, median, mode, std_dev
        
    Raises:
        ValueError: If data is empty or contains invalid values
        TypeError: If data is not a list or contains non-numeric values
        
    @author: Contributor 3
    """
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    
    # Check for non-numeric values
    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError("All data values must be numeric")
    
    # Calculate mean
    mean = sum(data) / len(data)
    
    # Calculate median
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    
    # Calculate mode
    from collections import Counter
    counter = Counter(data)
    max_count = max(counter.values())
    mode = [k for k, v in counter.items() if v == max_count]
    if len(mode) == len(data) and len(data) > 1:
        mode = None  # No mode if all values are unique
    elif len(mode) == 1:
        mode = mode[0]
    else:
        mode = mode  # Keep as list if multiple modes
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'std_dev': std_dev,
        'count': len(data),
        'min': min(data),
        'max': max(data)
    }


def linear_regression(x_data: List[float], y_data: List[float]) -> dict:
    """
    Perform simple linear regression analysis.
    
    Calculates the linear relationship between x and y variables using
    the least squares method.
    
    Args:
        x_data (List[float]): Independent variable data
        y_data (List[float]): Dependent variable data
        
    Returns:
        dict: Dictionary containing slope, intercept, r_squared, and equation
        
    Raises:
        ValueError: If data lengths don't match or data is empty
        TypeError: If inputs are not lists or contain non-numeric values
        
    @author: Contributor 3
    """
    if not isinstance(x_data, list) or not isinstance(y_data, list):
        raise TypeError("Both x_data and y_data must be lists")
    
    if len(x_data) == 0 or len(y_data) == 0:
        raise ValueError("Data cannot be empty")
    
    if len(x_data) != len(y_data):
        raise ValueError("x_data and y_data must have the same length")
    
    # Check for non-numeric values
    for value in x_data + y_data:
        if not isinstance(value, (int, float)):
            raise TypeError("All data values must be numeric")
    
    n = len(x_data)
    
    # Calculate means
    x_mean = sum(x_data) / n
    y_mean = sum(y_data) / n
    
    # Calculate slope and intercept using least squares method
    numerator = sum((x_data[i] - x_mean) * (y_data[i] - y_mean) for i in range(n))
    denominator = sum((x_data[i] - x_mean) ** 2 for i in range(n))
    
    if denominator == 0:
        raise ValueError("Cannot perform regression: x_data has no variance")
    
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    
    # Calculate R-squared
    y_pred = [slope * x + intercept for x in x_data]
    ss_res = sum((y_data[i] - y_pred[i]) ** 2 for i in range(n))
    ss_tot = sum((y_data[i] - y_mean) ** 2 for i in range(n))
    
    if ss_tot == 0:
        # If y_data has no variance, R-squared is undefined (set to 0)
        r_squared = 0.0
    else:
        r_squared = 1 - (ss_res / ss_tot)
    

    # Calculate correlation coefficient
    if ss_tot == 0:
        correlation = 0.0
    else:
        correlation = math.sqrt(r_squared) if slope >= 0 else -math.sqrt(r_squared)
    
    return {
        'slope': slope,
        'intercept': intercept,
        'r_squared': r_squared,
        'equation': f"y = {slope:.4f}x + {intercept:.4f}",
        'correlation': correlation
    }


def data_normalization(data: List[float], method: str = 'z_score') -> List[float]:
    """
    Normalize data using specified method.
    
    Supports z-score normalization and min-max scaling methods.
    
    Args:
        data (List[float]): Input dataset to normalize
        method (str): Normalization method ('z_score' or 'min_max')
        
    Returns:
        List[float]: Normalized data
        
    Raises:
        ValueError: If data is empty, has no variance, or invalid method
        TypeError: If data is not a list or contains non-numeric values
        
    @author: Contributor 3
    """
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    
    # Check for non-numeric values
    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError("All data values must be numeric")
    
    if method not in ['z_score', 'min_max']:
        raise ValueError("Method must be 'z_score' or 'min_max'")
    
    if method == 'z_score':
        # Z-score normalization: (x - mean) / std_dev
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = math.sqrt(variance)
        
        if std_dev == 0:
            raise ValueError("Cannot normalize: data has no variance")
        
        return [(x - mean) / std_dev for x in data]
    
    elif method == 'min_max':
        # Min-max normalization: (x - min) / (max - min)
        min_val = min(data)
        max_val = max(data)
        
        if max_val == min_val:
            raise ValueError("Cannot normalize: data has no variance")
        
        return [(x - min_val) / (max_val - min_val) for x in data]


def outlier_detection(data: List[float], method: str = 'iqr') -> List[float]:
    """
    Detect outliers in a dataset using specified method.
    
    Supports IQR (Interquartile Range) and Z-score methods for outlier detection.
    
    Args:
        data (List[float]): Input dataset
        method (str): Detection method ('iqr' or 'z_score')
        
    Returns:
        List[float]: List of outlier values
        
    Raises:
        ValueError: If data is empty or invalid method
        TypeError: If data is not a list or contains non-numeric values
        
    @author: Contributor 3
    """
    if not isinstance(data, list):
        raise TypeError("Data must be a list")
    
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    
    # Check for non-numeric values
    for value in data:
        if not isinstance(value, (int, float)):
            raise TypeError("All data values must be numeric")
    
    if method not in ['iqr', 'z_score']:
        raise ValueError("Method must be 'iqr' or 'z_score'")
    
    outliers = []
    
    if method == 'iqr':
        # IQR method: outliers are values outside Q1 - 1.5*IQR and Q3 + 1.5*IQR
        sorted_data = sorted(data)
        n = len(sorted_data)
        
        # Calculate Q1 and Q3
        q1_idx = n // 4
        q3_idx = 3 * n // 4
        
        if n % 4 == 0:
            q1 = sorted_data[q1_idx - 1] if q1_idx > 0 else sorted_data[0]
            q3 = sorted_data[q3_idx - 1] if q3_idx > 0 else sorted_data[-1]
        else:
            q1 = sorted_data[q1_idx]
            q3 = sorted_data[q3_idx]
        
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = [x for x in data if x < lower_bound or x > upper_bound]
    
    elif method == 'z_score':
        # Z-score method: outliers are values with |z-score| > 3
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = math.sqrt(variance)
        
        if std_dev == 0:
            return []  # No outliers if no variance
        
        outliers = [x for x in data if abs((x - mean) / std_dev) > 3]
    
    return outliers 

# TODO: Contributor 4 - Add your function here
# Example:
# def prime_number_generator(limit: int) -> List[int]:
#     """
#     Generate all prime numbers up to a given limit.
#     
#     Args:
#         limit (int): Upper limit for prime number generation
#         
#     Returns:
#         List[int]: List of prime numbers
#         
#     @author: [Your Name]
#     """
#     pass

from typing import List

def prime_number_generator(limit: int) -> List[int]:
    """
    Generate all prime numbers up to a given limit.

    Args:
        limit (int): Upper limit for prime number generation

    Returns:
        List[int]: List of prime numbers up to the limit (inclusive if prime)

    Raises:
        ValueError: If limit is less than 2

    @author: Prem Prakash
    """
    if limit < 2:
        raise ValueError("Limit must be at least 2")

    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes

from typing import List

def prime_number_generator(limit: int) -> List[int]:
    """
    Generate all prime numbers up to a given limit.

    Args:
        limit (int): Upper limit for prime number generation

    Returns:
        List[int]: List of prime numbers up to the limit (inclusive if prime)

    Raises:
        ValueError: If limit is less than 2

    @author: Prem Prakash
    """
    if limit < 2:
        raise ValueError("Limit must be at least 2")

    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False

    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False

    return primes
