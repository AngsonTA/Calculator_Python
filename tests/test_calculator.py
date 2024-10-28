import unittest
from src.calculator import add, subtract, multiply, divide, power, square_root

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(6, 0), "Cannot divide by zero!")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(-1), "Cannot take square root of negative number!")

if __name__ == "__main__":
    unittest.main()
