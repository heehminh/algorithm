// 영수증에 적힌 금액 
// 물건의 종류
// .. 

const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const X = parseInt(input[0]);
const N = parseInt(input[1]);
let testCase = [];

for (let i=2; i<2+N; ++i) {
    testCase.push(input[i]);
}

function solution(X, N, testCase) {
    let result = 0;

    for (let i=0; i<N; i++) {
        let num = testCase[i].toString().split(" ");
        const A = parseInt(num[0]);
        const B = parseInt(num[1]);
        result = result + A*B;
    }

    if (X===result) {
        console.log("Yes");
    } else {
        console.log("No");
    }
}

solution(X, N, testCase);

