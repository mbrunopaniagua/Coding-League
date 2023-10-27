import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class BracketCheckerTest {

    @Test
    public void testPairedSquareBrackets() {
        BracketChecker bracketChecker = new BracketChecker("()");
        assertTrue(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }
    
    @Test
    public void testEmptyString() {
        BracketChecker bracketChecker = new BracketChecker("");
        assertTrue(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testUnpairedBrackets() {
        BracketChecker bracketChecker = new BracketChecker("((");
        assertFalse(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testWrongOrderedBrackets() {
        BracketChecker bracketChecker = new BracketChecker(")(");
        assertFalse(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testPairedWithWhitespace() {
        BracketChecker bracketChecker = new BracketChecker("( )");
        assertTrue(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testSimpleNestedBrackets() {
        BracketChecker bracketChecker = new BracketChecker("(())");
        assertTrue(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testSeveralPairedBrackets() {
        BracketChecker bracketChecker = new BracketChecker("()()");
        assertTrue(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testPairedAndNestedBrackets() {
        BracketChecker bracketChecker = new BracketChecker("((()(()())))");
        assertTrue(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testUnopenedClosingBracket() {
        BracketChecker bracketChecker = new BracketChecker("(())())");
        assertFalse(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testUnpairedAndNestedBrackets() {
        BracketChecker bracketChecker = new BracketChecker("((())");
        assertFalse(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testPairedAndIncompleteBrackets() {
        BracketChecker bracketChecker = new BracketChecker("()(");
        assertFalse(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testTooManyClosingBrackets() {
        BracketChecker bracketChecker = new BracketChecker("())");
        assertFalse(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

    
    @Test
    public void testMathExpression() {
        BracketChecker bracketChecker = new BracketChecker("(((185 + 223.85) * 15) - 543)/2");
        assertTrue(bracketChecker.areBracketsMatchedAndNestedCorrectly());
    }

}
