function Stack() {
    // 프로퍼티와 메소드 아래에 기술
    let items = [];

    // push
    // 스택에 새로운 원소를 추가하는 메소드
    // 스택의 꼭대기에만 원소를 넣을 수 있다
    this.push = function() {
        for (let i in arguments) {
            items.push(arguments[i]);
        }
    }

    // pop
    // 스택에서 원소를 삭제하는 메소드
    // 가장 마지막에 추가한 원소가 가장 먼저 삭제된다
    this.pop = function() {
        return items.pop();
    }

    // peek
    // 스택에서 가장 마지막으로 추가된 원소를 확인하는 메소드
    this.peek = function() {
        return items[items.length-1];
    }

    // isEmpty 
    // 스택이 비어있으면 true를 아니면 false를 반환하는 메소드
    this.isEmpty = function(){
        return items.length == 0;
    }

    // size
    // 컬렉션에는 보통 관습적으로 length 대신 size를 사용한다
    this.size = function(){
        return items.length;
    }

    // clear
    // 스택의 모든 원소 삭제
    this.clear = function(){
        items = [];
    }

    // print
    this.print = function(){
        console.log(items.toString());
    }

}

let stack = new Stack();
console.log(stack.isEmpty());

stack.push(1, 2, 3, 4);

console.log(stack.peek());
stack.print();

// stack.push(11);
// console.log(stack.size());
// console.log(stack.isEmpty());
// stack.print();