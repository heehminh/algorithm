const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const N = parseInt(input[0]);

function solution(N, input) {
    let result = 0;
    for (let i=0; i<N; i++) {
        result += parseInt(input[1][i]);
    }
    console.log(result);
}

solution(N, input);