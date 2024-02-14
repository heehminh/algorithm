'''
Heap Sort 
힙정렬: Heap 형태를 갖추도록 정렬하고 root와 찾아낸 자식 값을 바꾼 뒤 다시 정렬하는 방식 
시간복잡도: O(NlogN)
'''

def heapSort(arr):
    length = len(arr)
    
    # heap 형태로 데이터 정렬 
    for i in range(length, -1, -1):
       heapify(arr, length, i)
       
    # root와 마지막 값을 바꿔 정렬하고 바뀐값을 기준으로 다시 heapify 
    for i in range(length-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
    return arr 
    
def heapify(arr, length, i):
    root = i 
    left = 2*i + 1 
    right = 2*i + 2
    
    # 왼쪽 노드가 존재하고, 루트보다 더 큰 값일 때 
    if left < length and arr[root] < arr[left]:
        root = left 
    
    # 오른쪽 노드가 존재하고, 루트보다 . 더큰 값일 때 
    if right < length and arr[root] < arr[right]:
        root = right 
    
    # 왼쪽, 오른쪽 자식 노드들과 바꿔줄 위치를 찾았을 때
    if root != i:
        # 찾아낸 결과 swap
        arr[i], arr[root] = arr[root], arr[i]
        # 계속 heap 형태를 갖출때까지 실행 
        heapify(arr, length, root)
    
array = [7, 1, 5, 4, 9]
print(heapSort(array))