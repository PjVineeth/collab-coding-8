"""
Unit tests for math_utils module.

This file contains tests for the basic calculator function and serves as
a template for contributors to follow when creating their own test files.

@author: Admin (Repository Owner)
"""

import unittest
import sys
import os

# Add the parent directory to the path to import math_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from math_utils import basic_calculator


class TestBasicCalculator(unittest.TestCase):
    """Test cases for the basic_calculator function."""
    
    def test_addition(self):
        """Test addition operation."""
        result = basic_calculator('add', 5, 3)
        self.assertEqual(result, 8)
        
        result = basic_calculator('add', -2, 7)
        self.assertEqual(result, 5)
        
        result = basic_calculator('add', 0, 0)
        self.assertEqual(result, 0)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        result = basic_calculator('subtract', 10, 4)
        self.assertEqual(result, 6)
        
        result = basic_calculator('subtract', 3, 8)
        self.assertEqual(result, -5)
        
        result = basic_calculator('subtract', 0, 0)
        self.assertEqual(result, 0)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        result = basic_calculator('multiply', 6, 7)
        self.assertEqual(result, 42)
        
        result = basic_calculator('multiply', -3, 4)
        self.assertEqual(result, -12)
        
        result = basic_calculator('multiply', 0, 100)
        self.assertEqual(result, 0)
    
    def test_division(self):
        """Test division operation."""
        result = basic_calculator('divide', 15, 3)
        self.assertEqual(result, 5)
        
        result = basic_calculator('divide', 10, 2)
        self.assertEqual(result, 5)
        
        result = basic_calculator('divide', 7, 2)
        self.assertEqual(result, 3.5)
    
    def test_division_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            basic_calculator('divide', 10, 0)
        self.assertIn("Division by zero is not allowed", str(context.exception))
    
    def test_invalid_operation(self):
        """Test invalid operation raises ValueError."""
        with self.assertRaises(ValueError) as context:
            basic_calculator('invalid', 5, 3)
        self.assertIn("Unsupported operation", str(context.exception))
    
    def test_float_operations(self):
        """Test operations with float inputs."""
        result = basic_calculator('add', 1.5, 2.5)
        self.assertEqual(result, 4.0)
        
        result = basic_calculator('multiply', 2.5, 4)
        self.assertEqual(result, 10.0)
        
        result = basic_calculator('divide', 7.5, 2.5)
        self.assertEqual(result, 3.0)


if __name__ == '__main__':
    unittest.main()
