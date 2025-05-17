T = int(input())

if T == 1:
    print(input())

else:
    names = [input() for _ in range(T)]
    ans = ''

    for i in range(len(names[0])): # 모든 문자열 길이 동일 
        char_set = set()
        
        for j in range(T):
            char_set.add(list(names[j])[i])

        if len(char_set) == 1: 
            ans += char_set.pop()
        else:
            ans += '?'

    print(ans)