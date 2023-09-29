import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ResistorColorTest {

    private ResistorColor resistorColor;

    @BeforeEach
    public void setup() {
        resistorColor = new ResistorColor();
    }

    @Test
    public void testBlackColorCode() {
        assertEquals(0, resistorColor.colorCode("black"));
    }

    @Test
    public void testBrownColorCode() {
        assertEquals(1, resistorColor.colorCode("brown"));
    }

    @Test
    public void testRedColorCode() {
        assertEquals(2, resistorColor.colorCode("red"));
    }

    @Test
    public void testOrangeColorCode() {
        assertEquals(3, resistorColor.colorCode("orange"));
    }

    @Test
    public void testYellowColorCode() {
        assertEquals(4, resistorColor.colorCode("yellow"));
    }

    @Test
    public void testGreenColorCode() {
        assertEquals(5, resistorColor.colorCode("green"));
    }

    @Test
    public void testBlueColorCode() {
        assertEquals(6, resistorColor.colorCode("blue"));
    }

    @Test
    public void testVioletColorCode() {
        assertEquals(7, resistorColor.colorCode("violet"));
    }

    @Test
    public void testGreyColorCode() {
        assertEquals(8, resistorColor.colorCode("grey"));
    }

    @Test
    public void testWhiteColorCode() {
        assertEquals(9, resistorColor.colorCode("white"));
    }

    @Test
    public void testColorsCodeBlackBrownRed() {
        assertEquals("012", resistorColor.colorsCode("blackbrownred"));
    }

    @Test
    public void testColorsCodeVioletGreyWhite() {
        assertEquals("789", resistorColor.colorsCode("violetgreywhite"));
    }

    @Test
    public void testColorsCodeAllColor() {
        assertEquals("0123456789", resistorColor.colorsCode("blackbrownredorangeyellowgreenbluevioletgreywhite"));
    }

    
    @Test
    public void testColors() {
        List<String> colors = Arrays.asList("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white");

        assertEquals(colors, resistorColor.colors());
    }
}
