//'npm run test' -- run jest test
const cold = require('./cold');


test('[1, -100, 5, 300] = 1', () => {
    let expected = cold.answer([1, -100, 5, 300]);
    expect(expected).toBe(1); // only one neg temp
});


test('[-1000, -500, 0, 400, 1000, -1000000] = 1', () => {
    expect(cold.answer([-1000, -500, 0, 400, 1000, -1000000])).toBe(3); // three neg temps
});

test('[1, 3, 4, 353, 4343, 10000] == 0', () => {
    expect(cold.answer([1, 3, 4, 353, 4343, 10000])).toBe(0); // three neg temps
})

// fxn answer1 ex
test('1 3 4 353 4343 10000 == 0', () => {
    expect(cold.answer1('1, 3, 4, 353, 4343, 10000')).toBe(0);
});


test('1 -100 5 300 = 1', () => {
    let expected = cold.answer1('1 -100 5 300');
    expect(expected).toBe(1); // only one neg temp
});


test('-1000 -500 0 400 100 -1000000 = 1', () => {
    expect(cold.answer1('-1000 -500 0 400 1000 -1000000')).toBe(3); // three neg temps
});