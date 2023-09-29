import unittest
from resistor_color import *


class TestResistorColor(unittest.TestCase):

    def test_black_color_code(self):
        """
        Test black color code
        """
        actual = color_code("black")
        self.assertEqual(0, actual)

    def test_brown_color_code(self):
        """
        Test brown color code
        """
        actual = color_code("brown")
        self.assertEqual(1, actual)

    def test_red_color_code(self):
        """
        Test red color code
        """
        actual = color_code("red")
        self.assertEqual(2, actual)

    def test_orange_color_code(self):
        """
        Test orange color code
        """
        actual = color_code("orange")
        self.assertEqual(3, actual)

    def test_yellow_color_code(self):
        """
        Test yellow color code
        """
        actual = color_code("yellow")
        self.assertEqual(4, actual)

    def test_green_color_code(self):
        """
        Test green color code
        """
        actual = color_code("green")
        self.assertEqual(5, actual)

    def test_blue_color_code(self):
        """
        Test blue color code
        """
        actual = color_code("blue")
        self.assertEqual(6, actual)

    def test_violet_color_code(self):
        """
        Test violet color code
        """
        actual = color_code("violet")
        self.assertEqual(7, actual)

    def test_grey_color_code(self):
        """
        Test grey color code
        """
        actual = color_code("grey")
        self.assertEqual(8, actual)

    def test_white_color_code(self):
        """
        Test white color code
        """
        actual = color_code("white")
        self.assertEqual(9, actual)
        
    def test_colors_code_black_brown_red(self):
        """
        Test colors code black brown red
        """
        actual = colors_code("blackbrownred")
        self.assertEqual("012", actual)

    def test_colors_code_violet_grey_white(self):
        """
        Test colors code black brown red
        """
        actual = colors_code("violetgreywhite")
        self.assertEqual("789", actual)

    def test_colors_code_all_colors(self):
        """
        Test all colors
        """
        actual = colors_code("blackbrownredorangeyellowgreenbluevioletgreywhite")
        self.assertEqual("0123456789", actual)

    def test_colors(self):
        """
        Test color
        """
        actual = colorList()
        self.assertListEqual(['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet',
                              'grey', 'white'], actual)


if __name__ == '__main__':
    unittest.main()
