import unittest
from matching_brackets import *


class TestMatchingBrackets(unittest.TestCase):

    def test_paired_square_brackets(self):
        """
        Test paired square brackets
        """
        self.assertTrue(are_brackets_matched_and_nested_correctly("()"))

    def test_empty_string(self):
        """
        Test empty string
        """
        self.assertTrue(are_brackets_matched_and_nested_correctly(""))

    def test_unpaired_brackets(self):
        """
        Test unpaired brackets
        """
        self.assertFalse(are_brackets_matched_and_nested_correctly("(("))

    def test_wrong_ordered_brackets(self):
        """
        Test wrong ordered brackets
        """
        self.assertFalse(are_brackets_matched_and_nested_correctly(")("))

    def test_paired_with_whitespace(self):
        """
        Test paired with whitespace
        """
        self.assertTrue(are_brackets_matched_and_nested_correctly("( )"))

    def test_simple_nested_brackets(self):
        """
        Test simple nested brackets
        """
        self.assertTrue(are_brackets_matched_and_nested_correctly("(())"))

    def test_several_paired_brackets(self):
        """
        Test several paired brackets
        """
        self.assertTrue(are_brackets_matched_and_nested_correctly("()()"))

    def test_paired_and_nested_brackets(self):
        """
        Test paired and nested brackets
        """
        self.assertTrue(are_brackets_matched_and_nested_correctly("((()(()())))"))

    def test_unopened_closing_bracket(self):
        """
        Test unopened closing bracket
        """
        self.assertFalse(are_brackets_matched_and_nested_correctly("(())())"))

    def test_unpaired_and_nested_brackets(self):
        """
        Test unpaired and nested brackets
        """
        self.assertFalse(are_brackets_matched_and_nested_correctly("((())"))
        
    def test_paired_and_incomplete_brackets(self):
        """
        Test paired and incomplete brackets
        """
        self.assertFalse(are_brackets_matched_and_nested_correctly("()("))

    def test_too_many_closing_brackets(self):
        """
        Test too many closing brackets
        """
        self.assertFalse(are_brackets_matched_and_nested_correctly("())"))

    def test_math_expression(self):
        """
        Test math expression
        """
        self.assertTrue(are_brackets_matched_and_nested_correctly("(((185 + 223.85) * 15) - 543)/2"))


if __name__ == '__main__':
    unittest.main()
