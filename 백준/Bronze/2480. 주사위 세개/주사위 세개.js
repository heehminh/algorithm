const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

const A = parseInt(input[0]);
const B = parseInt(input[1]);
const C = parseInt(input[2]);

function solution(A, B, C) {
    let result = 0;

    if (A===B && B===C) {
        result = 10000+ A*1000;
    } else if ((A===B)&&(B!==C)) {
        result = 1000+A*100;
    } else if ((A===C)&&(A!==B)) {
        result = 1000+A*100;
    } else if ((B===C)&&(A!==B)) {
        result = 1000+B*100;
    } else {
        const max = Math.max(A, B, C);
        result = max*100;
    }

    console.log(result);
}

solution(A, B, C);