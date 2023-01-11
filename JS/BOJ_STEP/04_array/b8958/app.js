const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const N = parseInt(input[0]);

function solution(N, input) {
    for(let i=1; i<input.length; i++) {
        let result = 0;
        let cnt = 0;

        for (let j=0; j<input[i].length; j++) {
            if (input[i][j] === 'O') {
                cnt += 1;
                result += cnt;
            } else { 
                cnt = 0;
            }
        }
        console.log(result);
    }
}

solution(N, input);