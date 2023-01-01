// 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력

const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");
const N = parseInt(input[0]);

function solution(N, input) {
    for (let i=1; i<=N; i++) {
        let arr = input[i].split(" ");
        for (let i=0; i<arr.length; i++) {
            arr[i] = parseInt(arr[i]);
        }
        const testN = parseInt(arr[0]);

        arr.shift();

        const avg = arr.reduce((a,c) => a+c)/arr.length;

        let cnt = 0;
        for (let i=0; i<arr.length; i++) {
            if (avg < arr[i]) {
                cnt ++;
            }
        }
        const result = ((cnt/testN)*100).toFixed(3);
        console.log(`${result}%`);
    }
}

solution(N, input);