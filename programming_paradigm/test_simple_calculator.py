import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    #  Addition
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(10**6, 10**6), 2_000_000)

    #subtraction
    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 7), -7)

    #Multplication
    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(-4, -3), 12)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(1000, 1000), 1_000_000)

    #Division
    def test_divide(self):
        """Test the division method."""
        # normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)

        # negative values
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

        # floating point
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

        # division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

        # zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
