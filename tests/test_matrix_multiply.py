import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from math_utils import matrix_multiply

class TestMatrixMultiply(unittest.TestCase):
    def test_basic_multiplication(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(a, b), expected)

    def test_non_square_matrices(self):
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[7, 8], [9, 10], [11, 12]]
        expected = [[58, 64], [139, 154]]
        self.assertEqual(matrix_multiply(a, b), expected)

    def test_shape_mismatch(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6, 7]]
        with self.assertRaises(ValueError):
            matrix_multiply(a, b)

    def test_empty_matrix(self):
        with self.assertRaises(ValueError):
            matrix_multiply([], [[1]])

    def test_non_numeric(self):
        a = [[1, "x"], [3, 4]]
        b = [[5, 6], [7, 8]]
        with self.assertRaises(TypeError):
            matrix_multiply(a, b)

if __name__ == "__main__":
    unittest.main()
