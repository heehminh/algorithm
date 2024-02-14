'''
merge sort 
병합정렬: 리스트를 left, right로 절반씩 나눈다. 
이 때 리스트 원소가 1개가 될 때까지 나누는 작업을 수행한다.
나누는 작업이 완료되면 left, right의 원소를 비교해가며 정렬한다.
시간복잡도는 어떤 경우든 O(NlogN)으로, 안정적이고 일정한 것이 장점이다.
쪼개기 > 합치기 > 남아있는 원소 합치기
'''

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1 
            else:
                arr[k] = right[j]
                j += 1 
            k += 1 
        
        while i < len(left):
            arr[k] = left[i]
            i += 1 
            k += 1 
        while j < len(right):
            arr[k] = right[j]
            j += 1 
            k += 1 
    
    return arr 
          
print(mergeSort([7, 1, 3, 5, 2, 6, 4, 9]))