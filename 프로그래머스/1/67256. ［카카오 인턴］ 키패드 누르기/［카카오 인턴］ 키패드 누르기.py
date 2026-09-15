def solution(numbers, hand):
    answer = ''
    
    # 1, 4, 7: 왼손 
    # 3, 6, 9: 오른손 
    # 2, 5, 8, 0: 더 가까운 쪽 / 같다면 left: left, right: right 
    
    coords = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        0: [3, 1]
    }
    
    lnow = [3, 0]
    rnow = [3, 2]
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            # lnow 갱신 
            lnow = coords[num]
            
        elif num in [3, 6, 9]:
            answer += 'R'
            # rnow 갱신
            rnow = coords[num]
        
        else:
            # 1. 거리 비교 
            ny, nx = coords[num]
            ly, lx = lnow
            ry, rx = rnow
            
            l_dis = abs(ly-ny) + abs(lx-nx)
            r_dis = abs(ry-ny) + abs(rx-nx)
            
            if l_dis == r_dis:
                if hand == 'right':
                    answer += 'R'
                    rnow = ny, nx
                    
                else:
                    answer += 'L'
                    lnow = ny, nx 
            
            elif l_dis < r_dis:
                answer += 'L'
                lnow = ny, nx 
            
            else:
                answer += 'R'
                rnow = ny, nx
    
    
    return answer