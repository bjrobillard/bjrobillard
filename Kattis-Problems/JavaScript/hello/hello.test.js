
const hello = require('./hello');

test('Should print Hello World!', () => {
    let expected = "Hello World!";
    expect(hello.answer()).toBe(expected);
});