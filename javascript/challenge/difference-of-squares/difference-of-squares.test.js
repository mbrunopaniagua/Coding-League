const { computeSquareOfSumTo, computeSumOfSquares, computeDifferenceOfSquares } = require( "./difference-of-squares.js");

describe("Difference of squares function", () => {
  it('Square of sum up to 1', () => {
    expect(computeSquareOfSumTo(1)).toBe(1);
  });
  test('Square of sum up to 5', () => {
    expect(computeSquareOfSumTo(5)).toBe(225);
  });
  test('Square of sum up to 100', () => {
    expect(computeSquareOfSumTo(100)).toBe(25502500);
  });
  test('Sum of squares up to 1', () => {
    expect(computeSumOfSquares(1)).toBe(1);
  });
  test('Sum of squares up to 5', () => {
    expect(computeSumOfSquares(5)).toBe(55);
  });
  test('Sum of squares up to 100', () => {
    expect(computeSumOfSquares(100)).toBe(338350);
  });
  test('Difference of squares up to 1', () => {
    expect(computeDifferenceOfSquares(1)).toBe(0);
  });
  test('Difference of squares up to 5', () => {
    expect(computeDifferenceOfSquares(5)).toBe(170);
  });
  test('Difference of squares up to 100', () => {
    expect(computeDifferenceOfSquares(100)).toBe(25164150);
  });
});
