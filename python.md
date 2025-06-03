# 파이썬 기초문법 

# 1. 입력

```python
# 공백으로 나눠서 숫자 여러개 받기 
a, b = map(int, input().split())

# 서로 다른 자료형으로 받고 싶을 때
s1, s2 = input().split()
a = s1 # str 
b = int(s1) # int 

# 여러 줄 입력 (테스트 케이스가 T개)
T = int(input())
for _ in range(T):
    n = int(input())
    
# 리스트 
# 여러 줄로 입력받는 경우
# 10 
# 20 
# 30
budgets = [int(input()) for _ in range(N)]

# 한 줄로 입력받는 경우
# 10 20 30 
budgets = list(map(int, input().split()))

# 빠른 입력 
input sys 
input = sys.stdin.readline
```

# 2. 출력

```python
# 줄바꿈 없이 출력 
for i in range(3):
	print(i, end=' ') # 0 1 2 
	
# 포맷팅
# f-string 
name = 'minhee'
score = 95 
print(f"{name}님의 점수는 {score}점입니다.")

# format()
print("{}님의 점수는 {}점입니다.".format(name, score))

# 자리수 맞추기 (숫자 출력 포맷팅)
n = 7 
print(f"{n:03}") # 007 (3자리로 맞춤, 빈자리는 0으로 채움)
print(f"{3.14159:.2f}") # 3.14 (소수점 둘째자리까지 출력)

# 리스트 출력
arr = [1, 2, 3]
print(arr) # [1, 2, 3]
print(*arr) # 1 2 3 
print(', '.join(map(str, arr))) # 1, 2, 3

# 표 형식 출력
for i in range(1, 6):
	print(f"{i<3} | {i**2:<5}") # 좌측 정렬 
# 1   | 1    
# 2   | 4    
# 3   | 9    
# 4   | 16   
# 5   | 25   
# i:<3: 왼쪽 정렬, 3칸 / i:>3: 오른쪽 정렬 3칸 
# i:^3: 가운데 정렬 / i:03 # 3자리, 0으로 채움 
```

# 3. 리스트

```python
# 리스트 초기화 
arr = [0] * 10 
arr2d = [[0] * 4 for _ in range(3)] # 3*4 2차원 리스트 

arr.append(3)
arr.sort()
arr.sort(reverse=True)
arr.reverse() # 리스트 순서를 역순으로 변경 (정렬 X) 
arr.index(3) # 값이 3인 원소의 첫번쨰 인덱스 
arr.remove(3) # 값이 3인 첫번째 원소 삭제 
arr.count(3)

# List Comprehension (직관적 리스트 생성) 
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, ..., 64, 81]
```

# 4. 문자열

```python
s = 'hello'
s[0] # h
s[-1] # o
s[1:4] # ell 

s.upper() 
s.lower()
s.strip() # 양쪽 공백 제거 
s.replace('l', 'r') # herro 
s.split() # 공백 기준 리스트 ['hello']
```

# 5. 조건문, 반복문

```python
if x > 0:
	pass
elif x == 0:
	pass 
else: 
	pass
	
for i in range(5):

while True:
	break 
```

# 6. 함수 정의

```python
def add(a, b):
	return a + b
```

# 7. 주요 자료구조

```python
# 딕셔너리 
d = {'a': 1, 'b': 2}
d['a']
d.get('a')
d.keys()
d.values()
d.items()
'd' in d # 키 존재 여부 

# 집합 
s = set([1, 2, 3])
s.add(4)
s.remove(2)
s1 & s2 # 교집합
s1 | s2 # 합칩합
s1 - s2 # 차집합 
```

# 8. 정렬

```python
arr = [('b', 3), ('a', 2), ('c', 1)]
arr.sort(key=lambda x: x[1]) # 값 기준 정렬 
```

# 9. 기타 라이브러리

```python
import math 
math.sqrt(16)
math.ceil(3.1)
math.floor(3.9)
math.gcd(12, 18) # 최대공약수 
lcm = (12 * 18) // math.gcd(12, 18) # 최대공약수 

from collections import Counter, deque
Counter('banana') # {'a':3, 'b':1, 'n':2}

dq = deque([1,2])
dq.appendleft(0)
dq.pop()

from itertools import permutations, combinations
list(permutations([1,2,3], 2)) # 순열
list(combinations([1,2,3], 2)) # 조합 
```

# 10. 우선순위 큐

```python
import heapq
q = []
heapq.heappush(q, 2)
heapq.heappush(q, 1)
heapq.heappop(q) # 가장 작은 값 
```

# 11. 정규표현식

```python
import re 
# re.findall(패턴, 문자열)
re.findall(r'\d+', 'a1b22c333') # ['1', '22', '333']
# re.sub(패턴, 대체문자, 문자열)
re.sub(r'\D', '', 'a1b22c333') # 122333 
```
