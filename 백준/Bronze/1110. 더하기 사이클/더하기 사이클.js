const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();

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