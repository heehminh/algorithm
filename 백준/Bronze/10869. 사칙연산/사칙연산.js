const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

function solution(arr) {
    const A = parseInt(arr[0]);
    const B = parseInt(arr[1]);
    console.log(A+B);
    console.log(A-B);
    console.log(A*B);
    console.log(parseInt(A/B));
    console.log(A%B);
}

solution(input);