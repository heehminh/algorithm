# Stack 2개로 Queue 만들기
class Queue:
    def __init__(self):
        self.inbox = list()
        self.outbox = list()
        
    def push(self, item):
        self.inbox.append(item)
        
    def pop(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()
    
queue = Queue()
queue.push(4)
queue.push(3)
queue.push(2)
queue.push(1)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())