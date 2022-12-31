const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString();

const num = parseInt(input);

function solution(num) {
    for (let i=1; i<=9; ++i) {
        console.log(`${num} * ${i} = ${num*i}`);
    }
}

solution(num);