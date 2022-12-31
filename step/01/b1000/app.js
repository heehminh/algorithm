const fs = require("fs");
//  let input = fs.readFileSync("/dev/stdin").toString().split(" ");
let input = fs.readFileSync("./input.txt").toString().split(" ");

function solution(input){
    const A = parseInt(input[0]);
    const B = parseInt(input[1]);
    console.log(A+B)
}

solution(input);
