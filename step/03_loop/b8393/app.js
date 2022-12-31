const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString();

const num = parseInt(input);

function solution(num) {
    let result = 0;
    for (let i=1; i<=num; ++i) {
        result += i;
    }
    console.log(result);
}

solution(num);