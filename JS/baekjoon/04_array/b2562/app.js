const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

let testArr = [];
for (let i=0; i<input.length; i++) {
    testArr.push(parseInt(input[i]));
}

function solution(testArr) {
    let max = 0;
    let cnt = 0;

    for (let i=0; i<testArr.length; i++) {
        if (max < testArr[i]) max=testArr[i];
    }

    for (let i=0; i<testArr.length; i++) {
        if (max === testArr[i]) cnt = i+1;
    }

    console.log(max+"\n"+cnt);
}

solution(testArr);