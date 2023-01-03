const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim().split(" ");

const A = input[0];
const B = input[1];

function solution(A,B) {
    let reverseA = A;
    let reverseB = B;
    
    for(let i=0; i<A.length; i++) {
        reverseA[A.length-i] = A[i];
    }

    console.log(reverseA);
}

solution(A, B);