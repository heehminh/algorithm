'''
insert sort 
삽입정렬: key값 뒤에 있는 원소와 순서대로 비교한다.
시간복잡도는 최선의 경우 O(N), 최악의 경우 O(N^2)
'''

def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1 
        
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1 
            
        arr[j+1] = key 
        
    return arr 

print(insertSort([7, 1, 3, 5, 2, 6, 4, 9]))