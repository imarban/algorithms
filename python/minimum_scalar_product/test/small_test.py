
import unittest
from minimum_scalar_product.msp import minimum_scalar_product

__author__ = 'igomez'


class TestSmall(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(minimum_scalar_product([1, 2, 3, 4, 5], [1, 0, 1, 0, 1]), 6)

    def test_negative(self):
        self.assertEqual(minimum_scalar_product([1, 3, -5], [-2, 4, 1]), -25)
