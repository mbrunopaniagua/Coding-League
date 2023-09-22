import unittest
from difference_of_squares import *


class TestDifferenceOfSquares(unittest.TestCase):

    def test_squre_of_sum_up_to_one(self):
        """
        Test square of sum up to 1
        """
        actual = compute_square_of_sum_to(1)
        self.assertEqual(1, actual)

    def test_square_of_sum_up_to_five(self):
        """
        Test square of sum up to 5
        """
        actual = compute_square_of_sum_to(5)
        self.assertEqual(225, actual)

    def test_square_of_sum_up_to_hundred(self):
        """
        Test square of sum up to 100
        """
        actual = compute_square_of_sum_to(100)
        self.assertEqual(25502500, actual)

    def test_sum_of_squares_up_to_one(self):
        """
        Test sum of squares up to 1
        """
        actual = compute_sum_of_squares_to(1)
        self.assertEqual(1, actual)

    def test_sum_of_squares_up_to_five(self):
        """
        Test sum of squares up to 5
        """
        actual = compute_sum_of_squares_to(5)
        self.assertEqual(55, actual)

    def test_sum_of_squares_up_to_hundred(self):
        """
        Test sum of squares up to 100
        """
        actual = compute_sum_of_squares_to(100)
        self.assertEqual(338350, actual)

    def test_difference_of_squares_up_to_one(self):
        """
        Test difference of squares up to 1
        """
        actual = compute_difference_of_squares(1)
        self.assertEqual(0, actual)

    def test_difference_of_squares_up_to_five(self):
        """
        Test difference of squares up to 5
        """
        actual = compute_difference_of_squares(5)
        self.assertEqual(170, actual)

    def test_difference_of_squares_up_to_hundred(self):
        """
        Test difference of squares up to 100
        """
        actual = compute_difference_of_squares(100)
        self.assertEqual(25164150, actual)


if __name__ == '__main__':
    unittest.main()
