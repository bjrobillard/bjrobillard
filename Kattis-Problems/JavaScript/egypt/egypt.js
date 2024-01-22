#! /usr/bin/env node
const assert = require('assert').strict;


/*
given three sides [a,b,c] as arr of a triangle as an array find and return if 
it's a right angled triangle otherwise wrong
*/
const answer1 = (arr) => {
    assert.strictEqual(arr.length, 3);
    arr.sort((a,b) => a-b); //this means were sorting in accending order
    if(arr[0]**2 + arr[1]**2 == arr[2]**2)
        return 'right';
    else 
        return 'wrong';
}

/* 
Given three sides (a, b, c) of a triangle, answer will return 'right'
for right angled triangle otherwise 'wrong'.
*/
const answer = (a,b,c) => {
    let hyp = Math.max(a,b,c);
    let leg1;
    let leg2;
    if(a === hyp){
        leg1 = b;
        leg2 = c;
    } else if (b === hyp) {
        leg1 = a;
        leg2 = c;
    } else {
        leg1 = b;
        leg2 = a;
    }

    if(hyp**2 == leg1**2 + leg2**2)
        return 'right';
    else 
        return 'wrong';
}

//sync read using fs
const kattis = () => {
    const fs = require('fs');
    const data = fs.readFileSync(0, 'utf-8').split('\n');
    let ans = [];
    let sides;
    for(let line of data){
        if(line == '0 0 0') break;
        sides = line.split(" ").map(Number);
        ans.push(answer1(sides));
    }
    console.log(ans.join('\n'));
}

if(require.main === module) {
    kattis();
}

module.exports = {
    answer: answer,
    answer1:answer1
}