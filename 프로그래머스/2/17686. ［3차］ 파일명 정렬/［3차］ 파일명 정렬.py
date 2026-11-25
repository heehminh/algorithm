def solution(files):
    answer = []
    # head, number, 나머지로 나누고 
    # head 정렬, number 정렬, 인덱스 정렬 -> {원본, head, number}
    
    arr = []
    for f in files:
        # foo9.txt -> foo / 9 / .txt 
        
        head = ''
        number = ''
        si = 0 
        
        for idx in range(len(f)):
            if f[idx].isdigit() and head == '':
                head = f[:idx].lower()
                si = idx 
                
            elif head != '' and idx - si == 5:
                number = int(f[si:idx])
                break 
                
            elif head != '' and number == '' and not f[idx].isdigit():
                number = int(f[si:idx])
                break
        
        if number == '': 
            number = int(f[si:])
                
        arr.append([f, head, number])
    
    arr.sort(key=lambda x: (x[1], x[2]))
    
    for f, _, _ in arr:
        answer.append(f)
    
    return answer