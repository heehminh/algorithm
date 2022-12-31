const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim();

const N = parseInt(input);

function solution(N) {
    for (let i=0; i<N; i++) {
        let result = "";
        for (let j=0; j<N; j++) {
            if ((i+j) >= N-1) result += "*";
            else result += " ";
        }
        console.log(result);
    }
}

solution(N);