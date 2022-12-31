// const fs = require("fs");
// let input = fs.readFileSync(0).toString().split("\n");

const readline = require("readline");
const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];
r1.on('line', function (line) {
    input.push(line);
}).on('close', function () {
    input = input.map((item) => +item);
    solution(input);
    process.exit();
})

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

// solution(input);

// 참고사항
// 백준 14681 은 fs 모듈로 풀 경우 런타임에러가 난다.
// readline 모듈을 사용하여 런타임에러를 해결해주어야 한다.
// readline 모듈은 input.txt를 사용하지 않고 터미널에 직접 input을 한다.