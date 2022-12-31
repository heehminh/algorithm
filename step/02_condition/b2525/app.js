const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const timeNow = input[0].split(" ");

let H = parseInt(timeNow[0]);
let M = parseInt(timeNow[1]);
const requireTime = parseInt(input[1]);

function solution(H, M, requireTime) {
    M = M + requireTime;
    
    const num = parseInt(M/60);
    H = H + num;
    M = M - 60*num;

    if (H>=24) {
        H = H-24;
    }

    console.log(H, M);
}

solution(H, M, requireTime);
