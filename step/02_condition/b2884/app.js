const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split(" ");

let H = parseInt(input[0]);
let M = parseInt(input[1]);

function solution(H, M) {
    if (M < 45) {
        if (H < 1) {
            H = H+23;
        } else {
            H = H-1;
        }
        M = M+15;
    } else {
        M = M-45;
    }

    console.log(H, M);
}

solution(H, M);

