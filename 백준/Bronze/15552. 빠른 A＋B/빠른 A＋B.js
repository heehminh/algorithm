const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const N = parseInt(input[0]);
let testCase = [];

for (let i=1; i<input.length; i++) {
    testCase.push(input[i]);
}

function solution(N, testCase) {
    let result = "";

    for (let i=0; i<N; i++) {
        let arr = testCase[i].toString().split(" ");
        const A = parseInt(arr[0]);
        const B = parseInt(arr[1]);
        result += A+B+"\n";
    }
    console.log(result);
}

solution(N, testCase);
