'''
bubble sort 
버블정렬: 리스트에서 인접한 두 수를 비교하여, 작은 숫자는 왼쪽으로, 큰 숫자는 오른쪽으로 이동한다.
'''

# 시간복잡도: O(N^2)
def bubbleSort(arr):
    length = len(arr) - 1 
    
    for i in range(length):
        for j in range(i, length):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr 

print(bubbleSort([1, 3, 5, 2, 6, 4, 9]))

# 개선된 버블정렬
# 시간복잡도: 최선의 경우 O(N)
def newBubbleSort(arr):
    length = len(arr) - 1 
    
    for i in range(length):
        isSort = False 
        
        for j in range(i, length):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSort = True 
                
        if not isSort:
            break
        
    return arr 

print(newBubbleSort([1, 3, 5, 2, 6, 4, 9]))
