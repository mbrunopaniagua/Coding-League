import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MorseTest {

    private final Morse sut = new Morse();

    @Test
    public void translateRegularToMorse() {
        String expected = ".... --- .-.. .- / -- ..- -. -.. ---";

        String actual = sut.textToMorse("HOLA MUNDO");

        assertEquals(expected, actual);
    }

    @Test
    public void translateATextWithNumbersToMorse() {
        String expected = "... --- -- --- ... / ..- -. .- ... / ....- ..... / .--. . .-. ... --- -. .- ...";

        String actual = sut.textToMorse("SOMOS UNAS 45 PERSONAS");

        assertEquals(expected, actual);
    }

    @Test
    public void translateATextWithSymbolsToMorse() {
        String expected = "--...- -- .. / . -- .- .. .-.. / . ... / .--. . .--. . .--.-. .. -. --. .-.-.- -.-. --- -- -.-.--";

        String actual = sut.textToMorse("¡MI EMAIL ES PEPE@ING.COM!");

        assertEquals(expected, actual);
    }

    @Test
    public void translateAMorseRegularText() {
        String expected = "HOLA MUNDO";

        String actual = sut.morseToText(".... --- .-.. .- / -- ..- -. -.. ---");

        assertEquals(expected, actual);
    }

    @Test
    public void translateMorseToTextWithNumbers() {
        String expected = "SOMOS UNAS 45 PERSONAS";

        String actual = sut.morseToText("... --- -- --- ... / ..- -. .- ... / ....- ..... / .--. . .-. ... --- -. .- ...");

        assertEquals(expected, actual);
    }

    @Test
    public void translateMorseToTextWithSymbols() {
        String expected = "¡MI EMAIL ES PEPE@ING.COM!";

        String actual = sut.morseToText("--...- -- .. / . -- .- .. .-.. / . ... / .--. . .--. . .--.-. .. -. --. .-.-.- -.-. --- -- -.-.--");

        assertEquals(expected, actual);
    }

}