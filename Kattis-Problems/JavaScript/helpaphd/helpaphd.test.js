const helpaphd = require('./helpaphd');

test('P=NP -> skipped', ()=> {
    expect(helpaphd.answer('P=NP')).toBe('skipped');
});

test('10+3 -> 13', ()=> {
    expect(helpaphd.answer('10+3')).toBe(13);
});

test('30+24 -> skipped', ()=> {
    expect(helpaphd.answer('30+24')).toBe(54);
});
