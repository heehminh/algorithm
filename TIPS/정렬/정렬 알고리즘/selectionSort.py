'''
selection sort 
선택정렬: 가장 작은 값의 위치를 찾아서 교환 
시간복잡도는 최선의 경우 O(N), 최악의 경우 O(N^2)
'''

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j] :
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr 

print(selectionSort([7, 1, 3, 5, 2, 6, 4, 9]))