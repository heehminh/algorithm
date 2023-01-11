// 점수 중 최댓값 M
// 점수/M * 100

const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = parseInt(input[0]);
console.log(N);

const testCase = [];
let arr = input[1].split(" ");

for (let i=0; i<N; i++) {
    testCase.push(parseInt(arr[i]));
}

function solution(N, testCase) {   
    const max = Math.max.apply(null, testCase);
    
    let change = [];
    for (let i=0; i<N; i++) {
        change.push(testCase[i]/max * 100);
    }
    const avg = change.reduce((a,c) =>a+c)/change.length;
    console.log(avg);
}

solution(N, testCase);