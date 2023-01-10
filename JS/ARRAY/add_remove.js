let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
numbers[numbers.length] = 10;
numbers.push(11);
numbers.push(12, 13);

for (let i=numbers.length; i>=0; i--) {
    numbers[i] = numbers[i-1];
}
numbers[0] = -1;

numbers.unshift(-2);
numbers.unshift(-4, -3); // -4, -3 순으로 들어감
console.log(numbers.length);

// 삭제
numbers.pop();
console.log(numbers.length);

for (let i=0; i<numbers.length; i++) {
    numbers[i] = numbers[i+1];
}
console.log(numbers);
console.log(numbers.length);

// 어떤 원소의 배열 앞부분부터 정말 지우고 싶다면 shift 메소드를 사용한다
numbers.shift();
console.log(numbers);
console.log(numbers.length);

// 특정 원소 삭제
numbers.splice(5, 3); // 인덱스 5에서 시작되는 3개의 원소를 날린다 (5, 6, 7 삭제)
console.log(numbers);

numbers.splice(5, 0, 2, 3, 4);
// 첫번째 인자: 원소를 추가/삭제하려는 인덱스
// 두번째 인자: 삭제할 원소의 개수 (개수가 0이면 삭제하지 않겠다)
// 세번째 인자 이후로는 배열에 추가할 원소들을 나열한다. 

