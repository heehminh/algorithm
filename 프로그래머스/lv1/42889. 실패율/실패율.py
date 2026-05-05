def solution(N, stages):
    answer = {}
    all_players = len(stages)

    for i in range(1, N+1):
        if all_players == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i) / all_players
            all_players -= stages.count(i)
        
    return sorted(answer, key = lambda x: answer[x], reverse=True)

    # 실패율이 높은 스테이지부터 내림차순 정렬 / idx 오름차순 

    # 스테이지에 도달했으나 클리어하지 못한 플레이어 / 스테이지에 도달한 플레이어 
    # N: 전체 스테이지 수 
    # 실패율이 높은 스테이지부터 내림차순으로 정렬 [idx, 실패율]
    # stages: 사용자가 현재 도전중인 스테이지의 번호 