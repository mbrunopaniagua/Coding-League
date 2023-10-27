const { bracketsMatchedAndNestedCorrectly } = require("./matching-brackets.js");

describe('Morse code tests', () => {
  test('Paired square brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly('()')).toBe(true);
  });

  test('Empty expression', () => {
    expect(bracketsMatchedAndNestedCorrectly('')).toBe(true);
  });

  test('Unpaired brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly('((')).toBe(false);
  });

  test('Wrong order brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly(')(')).toBe(false);
  });

  test('Paired with white space', () => {
    expect(bracketsMatchedAndNestedCorrectly('( )')).toBe(true);
  });

  test('Simple nested brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly('(())')).toBe(true);
  });

  test('Several paired brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly('()()')).toBe(true);
  });

  test('Paired and nested brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly('((()(()())))')).toBe(true);
  });

  test('Unopened closing bracket', () => {
    expect(bracketsMatchedAndNestedCorrectly('(())())')).toBe(false);
  });
  
  test('Unpaired and nested brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly('((())')).toBe(false);
  });

  test('Paired and incomplete brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly('()(')).toBe(false);
  });

  test('Too many closing brackets', () => {
    expect(bracketsMatchedAndNestedCorrectly('())')).toBe(false);
  });

  test('Match expression', () => {
    expect(bracketsMatchedAndNestedCorrectly('(((185 + 223.85) * 15) - 543)/2')).toBe(true);
  });
});