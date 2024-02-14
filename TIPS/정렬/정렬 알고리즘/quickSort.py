'''
quick sort 
퀵정렬: 기준이 되는 pivot 값을 정한 후 pivot 기준으로 분할, 정렬한다.
시간복잡도는 평균 O(NlogN)으로 빠르나, 최악의 경우 O(N^2)
'''

def quickSort(arr):
    if len(arr) <= 1:
        return arr 
    
    pivot = arr[0]
    tail = arr[1:]
    
    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x >= pivot]

    return quickSort(left) + [pivot] + quickSort(right)
    
array = [7, 1, 3, 5, 2, 6, 4, 9]
print(quickSort(array))