def solution(n, words):
    ws = set()
    ws.add(words[0])

    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0] or words[idx] in ws:
            return [idx%n + 1, idx//n + 1] # 누가, 몇번째에 
        
        ws.add(words[idx])

    return [0, 0]