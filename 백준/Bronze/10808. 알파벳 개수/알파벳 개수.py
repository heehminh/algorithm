s = input()

# 알파벳 26개 

alphabet = ['a', 'b', 'c', 'd', 'e', 
            'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

ans = [0]*26

for char in list(s):
    if char in alphabet: 
        ans[alphabet.index(char)] += 1 

print(' '.join(map(str, ans)))