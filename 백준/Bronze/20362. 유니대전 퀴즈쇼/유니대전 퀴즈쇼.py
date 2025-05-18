N, S = map(str, input().split())
ans = 0 
lucky_num = 0 
lucky_ans = ''

dict = {}
for i in range(int(N)):
    name, answer = input().split()
    dict[name] = answer 
    
    if name == S:
        lucky_num = i
        lucky_ans = answer 

cnt = 0
for key in dict.keys():
    if dict[key] == lucky_ans and cnt < lucky_num:
        ans += 1
    cnt += 1 

print(ans)

# 반복문 돌려서 맞는 정답이 뭔지 알아야내야함
# 보다 일찍 말한 사람이 있는지 찾기 