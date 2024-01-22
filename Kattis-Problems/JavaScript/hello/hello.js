#!/usr/bin/env node

function answer(){ // we can test this fxn now!
    return "Hello World!";
}

function main(){
    console.log(answer());
}

if (require.main === module) {
    main();
}

module.exports = {
    answer: answer
}
