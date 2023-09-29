const { resistorColor, resistorColors } = require( "./resistor-color.js");

describe('Resistor Color Tests', () => {
  test('black to be 0', () => {
    expect(resistorColor('black')).toBe(0);
  });

  test('brown to be 1', () => {
    expect(resistorColor('brown')).toBe(1);
  });

  test('red to be 2', () => {
    expect(resistorColor('red')).toBe(2);
  });

  test('orange to be 3', () => {
    expect(resistorColor('orange')).toBe(3);
  });

  test('yellow to be 4', () => {
    expect(resistorColor('yellow')).toBe(4);
  });

  test('green to be 5', () => {
    expect(resistorColor('green')).toBe(5);
  });

  test('blue to be 6', () => {
    expect(resistorColor('blue')).toBe(6);
  });

  test('violet to be 7', () => {
    expect(resistorColor('violet')).toBe(7);
  });

  test('grey to be 8', () => {
    expect(resistorColor('grey')).toBe(8);
  });

  test('white to be 9', () => {
    expect(resistorColor('white')).toBe(9);
  });

  test('BlackBrownRed to be 012', () => {
    expect(resistorColors('blackbrownred')).toBe('012');
  });

  test('BlackBrownRed to be 789', () => {
    expect(resistorColors('violetgreywhite')).toBe('789');
  });

  test('All colors to be 0123456789', () => {
    expect(resistorColors('blackbrownredorangeyellowgreenbluevioletgreywhite')).toBe('0123456789');
  });
});
 