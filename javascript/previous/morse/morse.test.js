const { morseToText, textToMorse } = require("./morse.js");

describe('Morse code tests', () => {
  test('Should translate a regular text to morse', () => {
    expect(textToMorse('HOLA MUNDO')).toBe('.... --- .-.. .- / -- ..- -. -.. ---');
  });

  test('Should translate a text with numbers to morse', () => {
    expect(textToMorse('SOMOS UNAS 45 PERSONAS')).toBe('... --- -- --- ... / ..- -. .- ... / ....- ..... / .--. . .-. ... --- -. .- ...');
  });

  test('Should translate a text with symbols to morse', () => {
    expect(textToMorse('¡MI EMAIL ES PEPE@ING.COM!')).toBe('--...- -- .. / . -- .- .. .-.. / . ... / .--. . .--. . .--.-. .. -. --. .-.-.- -.-. --- -- -.-.--');
  });

  test('Should translate a morse to regular text', () => {
    expect(morseToText('.... --- .-.. .- / -- ..- -. -.. ---')).toBe('HOLA MUNDO');
  });

  test('Should translate morse to text with numbers', () => {
    expect(morseToText('... --- -- --- ... / ..- -. .- ... / ....- ..... / .--. . .-. ... --- -. .- ...')).toBe('SOMOS UNAS 45 PERSONAS');
  });

  test('Should translate morse to text with symbols', () => {
    expect(morseToText('--...- -- .. / . -- .- .. .-.. / . ... / .--. . .--. . .--.-. .. -. --. .-.-.- -.-. --- -- -.-.--')).toBe('¡MI EMAIL ES PEPE@ING.COM!');
  });  
});