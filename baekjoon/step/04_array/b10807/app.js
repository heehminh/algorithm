const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = parseInt(input[0]);

let inputArr = input[1].split(" ");

const V = parseInt(input[2]);

function solution(N, arr, V) {
    let cnt = 0;
    for(let i=0; i<N; i++) {
        if(parseInt(arr[i]) === V) {
            cnt ++;
        }
    }
    console.log(cnt);
}

solution(N, inputArr, V);