"""
Unit tests for Contributor 3's Statistics & Data Analysis functions.

This file contains comprehensive tests for all statistical analysis functions
implemented by Contributor 3, including normal cases, edge cases, and error conditions.

@author: Contributor 3
"""

import unittest
import sys
import os
import math

# Add the parent directory to the path to import math_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from math_utils import statistical_analysis, linear_regression, data_normalization, outlier_detection


class TestStatisticalAnalysis(unittest.TestCase):
    """Test cases for the statistical_analysis function."""
    
    def test_normal_cases(self):
        """Test normal operation with typical datasets."""
        # Test with simple dataset
        data = [1, 2, 3, 4, 5]
        result = statistical_analysis(data)
        
        self.assertEqual(result['mean'], 3.0)
        self.assertEqual(result['median'], 3.0)
        self.assertEqual(result['mode'], None)  # All values unique
        self.assertEqual(result['std_dev'], math.sqrt(2.0))
        self.assertEqual(result['count'], 5)
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['max'], 5)
    
    def test_with_mode(self):
        """Test dataset with a clear mode."""
        data = [1, 2, 2, 3, 4, 2, 5]
        result = statistical_analysis(data)
        
        self.assertEqual(result['mode'], 2)
        self.assertEqual(result['count'], 7)
    
    def test_even_length_dataset(self):
        """Test with even number of elements."""
        data = [1, 2, 3, 4, 5, 6]
        result = statistical_analysis(data)
        
        self.assertEqual(result['median'], 3.5)
        self.assertEqual(result['mean'], 3.5)
    
    def test_float_data(self):
        """Test with float data."""
        data = [1.5, 2.5, 3.5, 4.5, 5.5]
        result = statistical_analysis(data)
        
        self.assertEqual(result['mean'], 3.5)
        self.assertEqual(result['median'], 3.5)
    
    def test_single_element(self):
        """Test with single element dataset."""
        data = [42]
        result = statistical_analysis(data)
        
        self.assertEqual(result['mean'], 42)
        self.assertEqual(result['median'], 42)
        self.assertEqual(result['mode'], 42)
        self.assertEqual(result['std_dev'], 0)
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        data = [-5, -3, -1, 1, 3, 5]
        result = statistical_analysis(data)
        
        self.assertEqual(result['mean'], 0)
        self.assertEqual(result['median'], 0)
    
    def test_empty_data_error(self):
        """Test that empty data raises ValueError."""
        with self.assertRaises(ValueError) as context:
            statistical_analysis([])
        self.assertIn("Data cannot be empty", str(context.exception))
    
    def test_invalid_type_error(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError) as context:
            statistical_analysis("not a list")
        self.assertIn("Data must be a list", str(context.exception))
    
    def test_non_numeric_error(self):
        """Test that non-numeric data raises TypeError."""
        with self.assertRaises(TypeError) as context:
            statistical_analysis([1, 2, "three", 4])
        self.assertIn("All data values must be numeric", str(context.exception))


class TestLinearRegression(unittest.TestCase):
    """Test cases for the linear_regression function."""
    
    def test_perfect_correlation(self):
        """Test with perfectly correlated data."""
        x_data = [1, 2, 3, 4, 5]
        y_data = [2, 4, 6, 8, 10]
        result = linear_regression(x_data, y_data)
        
        self.assertEqual(result['slope'], 2.0)
        self.assertEqual(result['intercept'], 0.0)
        self.assertEqual(result['r_squared'], 1.0)
        self.assertEqual(result['correlation'], 1.0)
    
    def test_negative_correlation(self):
        """Test with negative correlation."""
        x_data = [1, 2, 3, 4, 5]
        y_data = [10, 8, 6, 4, 2]
        result = linear_regression(x_data, y_data)
        
        self.assertEqual(result['slope'], -2.0)
        self.assertEqual(result['intercept'], 12.0)
        self.assertEqual(result['r_squared'], 1.0)
        self.assertEqual(result['correlation'], -1.0)
    
    def test_no_correlation(self):
        """Test with no correlation."""
        x_data = [1, 2, 3, 4, 5]
        y_data = [5, 5, 5, 5, 5]
        result = linear_regression(x_data, y_data)
        
        self.assertEqual(result['slope'], 0.0)
        self.assertEqual(result['intercept'], 5.0)
        self.assertEqual(result['r_squared'], 0.0)
        self.assertEqual(result['correlation'], 0.0)
    
    def test_float_data(self):
        """Test with float data."""
        x_data = [1.5, 2.5, 3.5, 4.5]
        y_data = [3.0, 5.0, 7.0, 9.0]
        result = linear_regression(x_data, y_data)
        
        self.assertEqual(result['slope'], 2.0)
        self.assertEqual(result['intercept'], 0.0)
    
    def test_empty_data_error(self):
        """Test that empty data raises ValueError."""
        with self.assertRaises(ValueError) as context:
            linear_regression([], [1, 2, 3])
        self.assertIn("Data cannot be empty", str(context.exception))
    
    def test_mismatched_length_error(self):
        """Test that mismatched data lengths raise ValueError."""
        with self.assertRaises(ValueError) as context:
            linear_regression([1, 2, 3], [1, 2])
        self.assertIn("must have the same length", str(context.exception))
    
    def test_no_variance_error(self):
        """Test that data with no variance raises ValueError."""
        with self.assertRaises(ValueError) as context:
            linear_regression([1, 1, 1], [1, 2, 3])
        self.assertIn("x_data has no variance", str(context.exception))
    
    def test_invalid_type_error(self):
        """Test that non-list inputs raise TypeError."""
        with self.assertRaises(TypeError) as context:
            linear_regression("not a list", [1, 2, 3])
        self.assertIn("must be lists", str(context.exception))


class TestDataNormalization(unittest.TestCase):
    """Test cases for the data_normalization function."""
    
    def test_z_score_normalization(self):
        """Test z-score normalization."""
        data = [1, 2, 3, 4, 5]
        result = data_normalization(data, 'z_score')
        
        # Mean should be 0, std dev should be 1
        mean = sum(result) / len(result)
        variance = sum((x - mean) ** 2 for x in result) / len(result)
        std_dev = math.sqrt(variance)
        
        self.assertAlmostEqual(mean, 0.0, places=10)
        self.assertAlmostEqual(std_dev, 1.0, places=10)
    
    def test_min_max_normalization(self):
        """Test min-max normalization."""
        data = [10, 20, 30, 40, 50]
        result = data_normalization(data, 'min_max')
        
        # Min should be 0, max should be 1
        self.assertEqual(min(result), 0.0)
        self.assertEqual(max(result), 1.0)
    
    def test_default_method(self):
        """Test that default method is z_score."""
        data = [1, 2, 3, 4, 5]
        result_default = data_normalization(data)
        result_explicit = data_normalization(data, 'z_score')
        
        self.assertEqual(result_default, result_explicit)
    
    def test_single_element(self):
        """Test with single element (should raise error for z_score)."""
        data = [42]
        
        # Z-score should raise error
        with self.assertRaises(ValueError) as context:
            data_normalization(data, 'z_score')
        self.assertIn("no variance", str(context.exception))
        
        # Min-max should raise error
        with self.assertRaises(ValueError) as context:
            data_normalization(data, 'min_max')
        self.assertIn("no variance", str(context.exception))
    
    def test_identical_values(self):
        """Test with identical values."""
        data = [5, 5, 5, 5]
        
        with self.assertRaises(ValueError) as context:
            data_normalization(data, 'z_score')
        self.assertIn("no variance", str(context.exception))
    
    def test_empty_data_error(self):
        """Test that empty data raises ValueError."""
        with self.assertRaises(ValueError) as context:
            data_normalization([], 'z_score')
        self.assertIn("Data cannot be empty", str(context.exception))
    
    def test_invalid_method_error(self):
        """Test that invalid method raises ValueError."""
        with self.assertRaises(ValueError) as context:
            data_normalization([1, 2, 3], 'invalid_method')
        self.assertIn("Method must be", str(context.exception))
    
    def test_invalid_type_error(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError) as context:
            data_normalization("not a list", 'z_score')
        self.assertIn("Data must be a list", str(context.exception))


class TestOutlierDetection(unittest.TestCase):
    """Test cases for the outlier_detection function."""
    
    def test_iqr_method(self):
        """Test IQR method for outlier detection."""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]  # 100 is an outlier
        outliers = outlier_detection(data, 'iqr')
        
        self.assertIn(100, outliers)
        self.assertNotIn(5, outliers)  # 5 should not be an outlier
    
    def test_z_score_method(self):
        """Test Z-score method for outlier detection."""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]  # 100 is an outlier
        outliers = outlier_detection(data, 'z_score')
        
        self.assertIn(100, outliers)
        self.assertNotIn(5, outliers)  # 5 should not be an outlier
    
    def test_default_method(self):
        """Test that default method is IQR."""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
        outliers_default = outlier_detection(data)
        outliers_explicit = outlier_detection(data, 'iqr')
        
        self.assertEqual(outliers_default, outliers_explicit)
    
    def test_no_outliers(self):
        """Test dataset with no outliers."""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        outliers_iqr = outlier_detection(data, 'iqr')
        outliers_zscore = outlier_detection(data, 'z_score')
        
        self.assertEqual(len(outliers_iqr), 0)
        self.assertEqual(len(outliers_zscore), 0)
    
    def test_multiple_outliers(self):
        """Test dataset with multiple outliers."""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200]
        outliers = outlier_detection(data, 'iqr')
        
        self.assertIn(100, outliers)
        self.assertIn(200, outliers)
    
    def test_no_variance_zscore(self):
        """Test Z-score method with no variance."""
        data = [5, 5, 5, 5]
        outliers = outlier_detection(data, 'z_score')
        
        self.assertEqual(len(outliers), 0)
    
    def test_empty_data_error(self):
        """Test that empty data raises ValueError."""
        with self.assertRaises(ValueError) as context:
            outlier_detection([], 'iqr')
        self.assertIn("Data cannot be empty", str(context.exception))
    
    def test_invalid_method_error(self):
        """Test that invalid method raises ValueError."""
        with self.assertRaises(ValueError) as context:
            outlier_detection([1, 2, 3], 'invalid_method')
        self.assertIn("Method must be", str(context.exception))
    
    def test_invalid_type_error(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError) as context:
            outlier_detection("not a list", 'iqr')
        self.assertIn("Data must be a list", str(context.exception))


if __name__ == '__main__':
    unittest.main()
