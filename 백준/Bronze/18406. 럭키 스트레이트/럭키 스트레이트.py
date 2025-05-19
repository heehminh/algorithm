N = int(input())

length = len(str(N))

head, tail = int(N//10**(len(str(N))/2)), int(N%10**(len(str(N))/2))

sum_head = 0
sum_tail = 0

for i in range(int(length/2)):
    sum_head += int(list(str(head))[i])
    sum_tail += int(list(str(tail))[i])

if sum_head == sum_tail:
    print('LUCKY')
else:
    print('READY')