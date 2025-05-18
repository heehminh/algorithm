T = int(input())

for _ in range(T):
    hour_ans, date_ans = 'No', 'No'
    x, y = map(int, input().split())
    
    if x <= 23 and y <= 59:
        hour_ans = 'Yes'
    
    # 1, 3, 5, 7, 8, 10, 12 
    if x in (1, 3, 5, 7, 8, 10, 12) and 1 <= y <= 31:
        date_ans = 'Yes'
        
    # 4, 6, 9, 11 
    if x in (4, 6, 9, 11) and 1 <= y <= 30:
        date_ans = 'Yes'
    
    # 2
    if x == 2 and 1 <= y <= 29:
        date_ans = 'Yes'
        
    print(hour_ans, date_ans)