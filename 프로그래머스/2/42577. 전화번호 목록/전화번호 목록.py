def solution(phone_book):
    answer = True # 접두어가 있으면 false 출력 
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        b = phone_book[i+1]
            
        if len(a) > len(b):
            continue 

        if a == b[:len(a)]:
            return False 
    
    return answer