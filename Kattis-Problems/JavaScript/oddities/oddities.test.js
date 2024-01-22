const oddities = require("./oddities");

test('-10 -> is even', () => {
    expect(oddities.answer(-10)).toBe('is even');
});

test('0 -> is even', () => {
    expect(oddities.answer(0)).toBe('is even');
});

test('-234344 is even', () => {
    expect(oddities.answer(-234344)).toBe('is even');
});

