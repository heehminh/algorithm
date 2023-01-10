const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

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

// 시간 제한이 엄격한 문제
// console.log 를 반복하는게 생각보다 시간이 많이 걸린다
// 하나의 문자열을 정의해두고 그 문자열에 \n 을 반복하여 더해준다