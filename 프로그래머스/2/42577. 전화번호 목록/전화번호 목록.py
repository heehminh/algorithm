# 접두어인 경우가 있으면 return false

def solution(phone_book):
    # 정렬 후, 앞 뒤 같은 아이템이 있다면 answer = False
    phone_book.sort()
    
    for idx in range(len(phone_book)):
        if phone_book[idx-1] == phone_book[idx][:len(phone_book[idx-1])]:
            return False
    
    return True