def solution(data):
    cnt = int(len(data)*0.3)
    dict = {}
    
    for i in data:
        dict[i[0]] = sum(i[1:])
    
    # dict 를 점수를 기준으로 오름차순 정렬 
    dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    
    # 상위 동일 점수가 30%가 넘어가는 경우에는 아무도 선발하지 못한다
    if dict[0][1] == dict[cnt][1]:
        return []
    
    # cnt 에서 끊고 
    dict = dict[:cnt]
    
    # 출력하기 전에 이름을 기준으로 내림차순 정렬 
    # key만 뽑기
    keys = [i[0] for i in dict]

    # 내림차순 정렬
    keys.sort(reverse=True)
    
    return keys

# 이름, 체력, 정신력, 기술력, 방어력 
# 상위 30% 선발 
# 상위 동일 점수가 30%가 넘어가는 경우에는 아무도 선발하지 못한다
