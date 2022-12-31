const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString();

function solution(input){
    const year = parseInt(input);
    let result = 0; // 윤년이면 1, 아니면 0

    // 윤년: 4의 배수이면서, 100의 배수가 아닐때 또는 400의 배수일 떄
    if((year%4===0 && year%100!==0) || (year%400===0)) {
        result = 1;
    } 

    console.log(result);
}

solution(input);
