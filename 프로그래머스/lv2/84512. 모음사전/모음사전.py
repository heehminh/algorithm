from itertools import product 

def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U', ""]
    words = []

    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    for e in range(6):
                        print(str(arr[a]+arr[b]+arr[c]+arr[d]+arr[e]))
                        words.append(str(arr[a]+arr[b]+arr[c]+arr[d]+arr[e]))

    words.sort()
    
    return words.index(word) + 1

    
    

