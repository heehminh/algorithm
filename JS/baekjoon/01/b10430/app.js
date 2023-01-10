const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split(" ");

function solution(input) {
    const A = parseInt(input[0]);
    const B = parseInt(input[1]);
    const C = parseInt(input[2]);

    console.log((A+B)%C);
    console.log(((A%C)+(B%C))%C)
    console.log((A*B)%C);
    console.log(((A%C)*(B%C))%C)
}

solution(input);