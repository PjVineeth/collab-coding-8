import unittest
from math_utils import prime_number_generator

class TestPrimeNumberGenerator(unittest.TestCase):

    def test_small_limit(self):
        self.assertEqual(prime_number_generator(10), [2, 3, 5, 7])

    def test_inclusive_prime(self):
        self.assertIn(13, prime_number_generator(13))

    def test_large_limit(self):
        primes = prime_number_generator(30)
        self.assertEqual(primes[-1], 29)
        self.assertEqual(len(primes), 10)

    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            prime_number_generator(1)

if __name__ == "__main__":
    unittest.main()
