// 두 자연수 A, B의 합, 차, 곱, 몫, 나머지를 출력하는 프로그램을 작성하시오.
const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split(" ");

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