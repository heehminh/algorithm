const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim().split("\n");

const T = parseInt(input[0]);

function solution(T, input) {
    for (let i=1; i<=T; i++) {
        let testArr = input[i].split(" ");
        const R = parseInt(testArr[0]);

        testArr.shift();

        let result = "";
        for (let j=0; j<testArr[0].length; j++) {
            result += testArr[0][j].repeat(R);
        }
        console.log(result);
    }
}

solution(T, input);