def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    words = []

    # 길이 1~5 
    # 길이: 1 
    for a in range(5):
        words.append(arr[a])

    # 길이: 2
    for a in range(5):
        for b in range(5):
            words.append(arr[a]+arr[b])

    # 길이: 3 
    for a in range(5):
        for b in range(5):
            for c in range(5):
                words.append(arr[a]+arr[b]+arr[c])

    # 길이: 4 
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    words.append(arr[a]+arr[b]+arr[c]+arr[d])

    # 길이: 5 
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        words.append(arr[a]+arr[b]+arr[c]+arr[d]+arr[e])


    words.sort()
    
    return words.index(word) + 1

    
    

