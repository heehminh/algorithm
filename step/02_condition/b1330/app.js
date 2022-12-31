const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split(" ");

function solution(input) {
    const A = parseInt(input[0]);
    const B = parseInt(input[1]);

    let result = "";
    if (A>B) {
        result = ">";
    } else if (A<B) {
        result = "<";
    } else {
        result = "==";
    }

    console.log(result);
}

solution(input);