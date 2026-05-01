from collections import deque 

def solution(plans):
    answer = []
    
    # [1] plans을 시작시간 기준으로 정렬 
    plans.sort(key=lambda x: x[1])
    
    # [2] 스케줄링 (작업이름, 시작시간, 종료시간)
    start_time_list = list(map(int, plans[0][1].split(":")))
    start_time = start_time_list[0]*60 + start_time_list[1] # 분 단위로 표현 
    now = [plans[0][0], start_time, start_time + int(plans[0][2])]
    
    idx = 1 
    
    # [3] 대기큐 (작업이름, 남은작업량)
    q = deque()
    
    while idx < len(plans):
        name, start_time, playtime = plans[idx]
        
        start_time_list = list(map(int, start_time.split(":")))
        start = start_time_list[0]*60 + start_time_list[1] 
        end = start + int(playtime)
        
        before_n, _, before_e = now 
        now = [name, start, end]

        if before_e <= start:
            answer.append(before_n)
            
            free_time = start - before_e # 여유시간
            while q:
                w_n, w_p = q.pop()
                # 처리할 수 있는 양 now_start - before_e 
                if w_p <= free_time:
                    answer.append(w_n)
                    free_time -= w_p # 여유시간 사용한 만큼 차감
                else:
                    q.append([w_n, w_p - free_time])
                    break 
                    
        else:
            q.append([before_n, before_e - start])
        
        idx += 1 
    
    # 마지막 과제 처리 
    before_n, _, _ = now 
    answer.append(before_n)
    
    while q:
        n, _ = q.pop()
        answer.append(n)
    
    return answer 