const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim();

const N = parseInt(input);

function solution(N) {
    let result = "";
    for (let i=0; i<N; i++) {
        result += "*";
        console.log(result);
    }
}
solution(N);