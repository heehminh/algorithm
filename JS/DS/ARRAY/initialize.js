// 배열의 생성과 초기화
// 1) new를 사용하여 배열을 선언
let daysOfWeek = new Array();
let daysOfWeek2 = new Array(7);
let daysOfWeek3 = new Array("일","월","화","수","목","금","토");

// 2) []를 사용하여 배열을 선언 (2를 사용하는 것 권장)
let daysOfWeek4 = [];

// 배열의 원소의 개수
console.log(daysOfWeek3.length);

// 피보나치 수열의 처음 20개 숫자를 구하는 코드 
let fibonacci = [];
fibonacci[1] = 1;
fibonacci[2] = 2;

for (let i=3; i<20; i++) {
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1];
}

let result = "";

for (let i=1; i<fibonacci.length; i++) {
    result += " "+fibonacci[i];
}
console.log(result);