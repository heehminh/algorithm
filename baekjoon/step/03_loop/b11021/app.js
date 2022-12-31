const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = parseInt(input[0]);
let testCase = [];

for (let i=1; i<input.length; i++) {
    testCase.push(input[i]);
}

function solution(N, testCase) {
    for(let i=0; i<N; i++) {
        let arr = testCase[i].split(" ");
        const A = parseInt(arr[0]);
        const B = parseInt(arr[1]);
        console.log(`Case #${i+1}: ${A+B}`)
    }
}

solution(N, testCase);
