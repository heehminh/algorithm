// nodejs로 입력받기 
// 방법 <1> fs 모듈 사용
const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString();
console.log(input); 

input = input.split("\n");

const inputC = +input[0];
const inputTestCase = [];

for (let i=1; i<=inputC; ++i) {
	const arr = input[i].split(" ").map((item) => +item);
	// 입력값을 split 해서 arr로 바꿔줌
	const newArr = [];
    for (let i=1; i<=arr[0]; ++i) {
        newArr.push(arr[i]);
    }

	const testCase = {
		N: arr[0],
		arr: newArr,
	};
	break;
	inputTestCase.push(testCase);
}

function solution(C, testCase) {
	console.log("C: ", C);
	console.log("testCase: ", testCase);

	// 문제를 푸는 로직 작성
}

/*
어떻게 들어오는지 구체적으로 작성해보기 
C = 5
testCase = [
 {
	 N: 5,
	 arr: [50, 50, 70, 80, 100]
 }
 {
	 N: 7,
	 arr: [100, 95, 90, 80, 70, 60, 50]
 }
 ...
]
*/

solution(inputC, inputTestCase);