# 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

def solution(arr):
    answer = []
    
    for item in arr:        
        # (1) 아무 원소가 없거나 
        # (2) 정답 배열의 이전값이 현재값과 같지 않을 때 
        if len(answer) == 0 or answer[len(answer)-1] != item:
            answer.append(item)
    
    return answer