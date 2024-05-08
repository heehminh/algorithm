# 연속적으로 나타나는 숫자 
def solution(arr):
    answer = []
    
    for i in arr:
        # 아무 원소가 없거나, 배열의 이전 값이 현재 값과 같지 않거나
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    
    return answer