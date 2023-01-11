// 여러 배열 합치기 (concat)
let zero = 0;
let positiveNumber = [1, 2, 3];
let negativeNumber = [-3, -2, -1];
let numbers = negativeNumber.concat(zero, positiveNumber);

// console.log(numbers);

// 반복자 함수 (iterator)
const isEven = (x) => {
    // x가 2의 배수이면 true 반환
    return (x%2)==0 ? true : false;
}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

// 1. every 메소드: false가 반환될 때까지 호출 (1, 2)
numbers.every(isEven);

// 2. some 메소드: 지정된 함수의 결과 값을 true로 만드는 원소 전달
numbers.some(isEven);

// 3. forEach 메소드: 배열의 각 원소별로 지정된 함수를 실행한다
// numbers.forEach(function(x){
//     console.log(x%2==0);
// })

// 수행 결과를 새 배열 객체로 반환하는 메소드
// 4. map: 배열의 각 원소별로 지정된 함수를 실행한 결과로 구성된 새로운 배열 반환
// 원래 배열의 length와 새로운 배열의 length 같음
let myMap = numbers.map(isEven);
// 결과: false true false true ... 

// 5. filter: 함수의 결과값을 true로 만드는 원소로만 구성
let evenNumbers = numbers.filter(isEven);
// 결과: 2 4 6 8 ...

// 6. reduce: 인자로 previousValue, currentValue, index, array 를 인자로 받는 함수 지정
// 모든 배열 원소 값의 총합을 구할 때 유용함
const result = numbers.reduce((previous, current, index) => {
    return previous += current;
}, 0);
console.log(result);

// initialValue에 배열이 들어가는 경우
const example = [2, -5, -123, 59, -5480, 24, 0, -69, 349, 3];
const example_result = example.reduce( (previous, current, index) => {
    if (current < 0) {
        previous[0]++;
    } else if (current > 0) {
        previous[1]++;
    }
    return previous;
}, [0, 0]);
console.log(example_result);


// 검색과 정렬
// 1. reverse: 원소 순서를 거꾸로 바꾸고 싶을 경우 
numbers.reverse();

// 2-1. sort: 정렬 (sort 메소드는 모든 원소를 문자열로 취급해 사전적으로 정렬한다)
function compare(a,b) {
    if (a<b) return -1;
    if (a>b) return 1;
    return 0;
}
numbers.sort(compare);

// 2-2. 사용자 정의 정렬 - 나이순 오름차순 정렬 
let friends = [
    {name: 'John', age: 34},
    {name: 'Camila', age: 21},
    {name: 'Jack', age: 30}
];

function comparePerson(a,b) {
    if (a.age < b.age) return -1;
    if (a.age > b.age) return 1;
    return 0;
}

console.log(friends.sort(comparePerson));

// 2-3. 문자열 정렬
// 대소문자 구분 (대문자 < 소문자)
let names = ["Ana", "ana", "john", "John"];
console.log(names.sort());

// 대소문자 구분 없이
console.log(names.sort(function(a,b) {
    if (a.toLowerCase() < b.toLowerCase()){
        return -1;
    }
    if (a.toLowerCase() > b.toLowerCase()) {
        return 1;
    } return 0;
}));

// 4. 배열을 문자열로 변환
// toString(): 배열의 모든 원소를 단일 문자열로 바꿀때
console.log(numbers.toString());

// join(): 구분자를 넣고 싶을 때
const numberString = numbers.join("-");
console.log(numberString);