const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const T = parseInt(input[0]);

let testCase = [];
for (let i=1; i<input.length; ++i) {
    testCase.push(input[i]);
}

console.log(testCase);

function solution(T, testCase) {
    for (let i=0; i<T; ++i) {
        let arr = testCase[i].toString().split(" ");
        let A = parseInt(arr[0]);
        let B = parseInt(arr[1]);
        console.log(A+B);
    }
}

solution(T, testCase);