const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = parseInt(input[0]);
let testArr = input[1].split(" ");

function solution(N, testArr) {
    let max = -1000000;
    let min = 1000000;

    for (let i=0; i<N; i++) {
        let num = parseInt(testArr[i]);
        if (max < num) max = num;
        if (min > num) min = num;
    }
    console.log(min, max);
}

solution(N, testArr);