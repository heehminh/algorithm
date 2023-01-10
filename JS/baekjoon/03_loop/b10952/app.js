const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim().split("\n");

function solution(input) {
    for (let i=0; i<input.length; i++) {
        let arr = input[i].split(" ");
        const A = parseInt(arr[0]);
        const B = parseInt(arr[1]);

        console.log(A+B);
    }
}

solution(input);