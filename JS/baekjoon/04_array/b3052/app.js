const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim().split("\n");

let testCase = [];
for(let i=0; i<input.length; i++) {
    testCase.push(parseInt(input[i]));
}

function solution(testCase) {
    let arr =[];
    for (let i=0; i<testCase.length; i++) {
        let num = testCase[i] % 42;
        
        if (arr.includes(num) === false) {
            arr.push(num);
        }
    }
    console.log(arr.length);
}

solution(testCase);