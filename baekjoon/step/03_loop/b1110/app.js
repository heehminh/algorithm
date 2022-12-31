// 26 -> 68 -> 84 -> 42 -> 26 (4)
// 55 -> 50 -> 05 -> 55 (3)

// X,Y -> Y,(X+Y) 

const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().trim();

let num = parseInt(input);
let sum;
let cnt = 0;

while(true) {
    cnt ++;

    sum = parseInt(num/10) + num%10;
    num = (num%10)*10 + sum%10;

    if (parseInt(input) === num) { 
        break;
    }

}
console.log(cnt);
// 정수 자릿수 조정 
// while () {
//     1. 원래수랑 같은지 체크
//     2. 더하기 체크   
// }