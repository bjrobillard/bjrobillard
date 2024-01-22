
//function takes an array of numbers and returns count of neg vals
function answer(temps) { 
    var numOfNeg = 0;
    for (let t of temps){ // better/easier than normal c++ implem 
        if (t < 0)  numOfNeg++;
    }
    return numOfNeg;
}

// fxn takes temps as a string of numbers separated by space
function answer1(temps) {
    var numOfNeg =0;
    for(let c of temps) {
        if (c == '-') numOfNeg++;
    }

    return numOfNeg;
}

function main() {
        // read input
    const readline = require('readline');
    var rlInterface = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    let lineNumber = 1;
    let tempCount;
    rlInterface.on('line', (line) => {
        if (lineNumber === 1) {
            tempCount = parseInt(line);
            lineNumber++;
        } else {
            // array of numbers
            let temps = line.split(' ').map(Number);
            //console.log(temps);
            console.log(answer(temps));
        }
    });
}

//read asyncronously: whole file all at once
const main1 = () => { // callback fxn
    const fs = require('fs'); //read from file
    const data = fs.readFileSync(process.stdin.fd, 'utf-8'); // utf-8 is how the file will be treated
    
    //console.log(data);
    const lines = data.split('\n'); // [ '3', '5 -10 15', '' ]
    console.log(answer1(lines[1]));
    const temps = lines[1].split(' ').map(Number); // will split [1] from above into different places
    // console.log(lines);
}

//These can only be done this way in linux and mac
    //cat cold-002.in | node cold.js to 'pipe; information into file
    //cat cold-002.in | node cold.js | diff - cold-001.ans to see diff between stuff

if(require.main === module) {
    // main();
    main1();
}

//EOF: CTRL-Z 
//Testing git push add, commit shtuff


module.exports = {
    answer:answer,
    answer1:answer1
}