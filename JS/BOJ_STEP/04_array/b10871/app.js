const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = parseInt(input[0].split(" ")[0]);
const X = parseInt(input[0].split(" ")[1]);

const testArr = input[1].split(" ");

function solution(N, X, testArr) {
    let result = "";
    for (let i=0; i<N; i++) {
        if (parseInt(testArr[i]) < X) {
            result += testArr[i]+" ";
        }
    }
    console.log(result);
}

solution(N, X, testArr);