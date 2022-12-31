// 1. 같은 눈이 3개 나오는 경우
// 2. 같은 눈 2개
// 3. 모두 다른 눈이 나오면 그 중 가장 큰눈 

const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split(" ");

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