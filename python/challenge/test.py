import unittest
from morse import *


class TestMorse(unittest.TestCase):

    def test_translate_regular_to_morse(self):
        """
        Test translate regular to morse
        """
        expect = ".... --- .-.. .- / -- ..- -. -.. ---"

        actual = text_to_morse("HOLA MUNDO")

        self.assertEqual(expect, actual)

    def test_translate_a_text_with_numbers_to_morse(self):
        """
        Test translate a text with numbers to morse
        """
        expect = "... --- -- --- ... / ..- -. .- ... / ....- ..... / .--. . .-. ... --- -. .- ..."

        actual = text_to_morse("SOMOS UNAS 45 PERSONAS")

        self.assertEqual(expect, actual)

    def test_translate_a_text_with_symbols_to_morse(self):
        """
        Test translate a text with symbols to morse
        """
        expect = "--...- -- .. / . -- .- .. .-.. / . ... / .--. . .--. . .--.-. .. -. --. .-.-.- -.-. --- -- -.-.--"

        actual = text_to_morse("¡MI EMAIL ES PEPE@ING.COM!")

        self.assertEqual(expect, actual)

    def test_translate_a_morse_regular_text(self):
        """
        Test translate a morse regular text
        """
        expect = "HOLA MUNDO"

        actual = morse_to_text(".... --- .-.. .- / -- ..- -. -.. ---")

        self.assertEqual(expect, actual)

    def test_translate_morse_to_text_with_numbers(self):
        """
        Test translate a morse to text with numbers
        """
        expect = "SOMOS UNAS 45 PERSONAS"

        actual = morse_to_text("... --- -- --- ... / ..- -. .- ... / ....- ..... / .--. . .-. ... --- -. .- ...")

        self.assertEqual(expect, actual)

    def test_translate_morse_to_text_with_symbols(self):
        """
        Test translate a morse to text with symbols
        """
        expect = "¡MI EMAIL ES PEPE@ING.COM!"

        actual = morse_to_text("--...- -- .. / . -- .- .. .-.. / . ... / .--. . .--. . .--.-. .. -. --. .-.-.- -.-. --- -- -.-.--")

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
