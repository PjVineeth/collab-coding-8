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

# TODO: Contributor 1 - Generate Fibonacci sequence
from typing import List

def fibonacci_sequence(n: int) -> List[int]:
    """
    Generate Fibonacci sequence up to n terms.

    Args:
        n (int): Number of terms to generate (must be >= 0)

    Returns:
        List[int]: List containing the Fibonacci sequence up to n terms

    Raises:
        ValueError: If n is negative
        TypeError: If input is not an integer

    Example:
        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]

    @author: Priyansh
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Number of terms cannot be negative")

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


# TODO: Contributor 2 - Add your function here
# Example:
# def matrix_multiply(matrix_a: List[List[float]], matrix_b: List[List[float]]) -> List[List[float]]:
#     """
#     Multiply two matrices.
#     
#     Args:
#         matrix_a (List[List[float]]): First matrix
#         matrix_b (List[List[float]]): Second matrix
#         
#     Returns:
#         List[List[float]]: Resulting matrix
#         
#     @author: [Your Name]
#     """
#     pass

# TODO: Contributor 3 - Add your function here
# Example:
# def statistical_analysis(data: List[float]) -> dict:
#     """
#     Perform basic statistical analysis on a dataset.
#     
#     Args:
#         data (List[float]): Input dataset
#         
#     Returns:
#         dict: Dictionary containing mean, median, mode, std_dev
#         
#     @author: [Your Name]
#     """
#     pass

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
