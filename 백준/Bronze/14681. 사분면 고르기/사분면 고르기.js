const fs = require("fs");
let input = fs.readFileSync(0).toString().split("\n");
// console.log(input);

function solution(input) {
    const A = parseInt(input[0]);
    const B = parseInt(input[1]);

    let result = 0;

    if (A>0 && B>0) {
        result = 1;
    } else if (A<0 && B>0) {
        result = 2;
    } else if (A<0 && B<0) {
        result = 3;
    } else {
        result = 4;
    }

    console.log(result);
}

solution(input);