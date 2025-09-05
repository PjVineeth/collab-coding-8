import unittest
from math_utils import fibonacci_sequence


class TestPriyanshFunctions(unittest.TestCase):
    """Unit tests for Priyansh's Number Theory functions."""

    def test_fibonacci_normal_cases(self):
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(7), [0, 1, 1, 2, 3, 5, 8])

    def test_fibonacci_edge_cases(self):
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(3), [0, 1, 1])

    def test_fibonacci_large_input(self):
        seq = fibonacci_sequence(20)
        self.assertEqual(len(seq), 20)
        # Check last element (19th index)
        self.assertEqual(seq[-1], 4181)

    def test_fibonacci_error_cases(self):
        with self.assertRaises(ValueError):
            fibonacci_sequence(-5)
        with self.assertRaises(TypeError):
            fibonacci_sequence(5.5)
        with self.assertRaises(TypeError):
            fibonacci_sequence("10")


if __name__ == '__main__':
    unittest.main()
