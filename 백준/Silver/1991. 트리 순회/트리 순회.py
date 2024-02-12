# 백준 1991번 트리
# { 부모 : [왼쪽자식, 오른쪽자식] }

import sys 

tree = {}
for _ in range(int(input().strip())):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
    
# 전위 순회
def preorder(root):
    if root != ".":
        print(root, end="")
        preorder(tree[root][0]) # 왼
        preorder(tree[root][1]) # 오

# 중위 순회
def inorder(root):
    if root != ".":
        inorder(tree[root][0]) # 왼
        print(root, end="")
        inorder(tree[root][1]) #오

# 후위 순회 
def postorder(root):
    if root != ".":
        postorder(tree[root][0]) # 왼
        postorder(tree[root][1]) # 오
        print(root, end="")
        
preorder('A')
print()
inorder('A')
print()
postorder('A')