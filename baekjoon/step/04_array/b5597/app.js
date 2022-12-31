const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

let arr = [];
for (let i=1; i<=30; i++) {
    arr.push(i);
}

let inputArr = [];
for (let i=0; i<input.length; i++) {
    inputArr.push(parseInt(input[i]));
}

function solution(arr, inputArr){
    for (let i=0; i<30; i++) {
        for (let j=0; j<inputArr.length; j++) {
            if (arr[i] === inputArr[j]) delete arr[i];
        }
    }
    
    for (let i=0; i<arr.length; i++) {
        if (typeof arr[i] !== 'undefined'){
            console.log(arr[i]);
        }
    }
}

solution(arr, inputArr);