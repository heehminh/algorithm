# N과 M (1) 백트래킹 

N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M: # 배열의 길이
        for i in ans:
            print(i, end=" ")
        print()
    
    for i in range(1, N+1):
        if i not in ans: # 중복 확인 
            ans.append(i)
            back() # 재귀 
            ans.pop() # 마지막 요소를 제거하여 되돌아오기 

back()