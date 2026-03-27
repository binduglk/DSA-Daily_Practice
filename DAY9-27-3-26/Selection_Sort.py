# Selection Sort

def SelectionSort(arr):    # [3,5,9,1]              
    n = len(arr)           # stores len of array    n = 4
    for i in range(n):     # n=4 , i=0 
        mid_idx = i        # mid_idx = 0
        for j in range(i+1,n):      # (1,4) -> 1,2,3
            if arr[j] < arr[mid_idx]:   # 5 < 3 no 9 < 3 no 1 < 3 yes
                mid_idx = j      # mid_idx = 3      
        arr[i], arr[mid_idx] = arr[mid_idx], arr[i]  # 3,1 = 1,3
    return arr                               # [1,5,9,3]...........  
print(SelectionSort([4,9,2,6,9,1]))
print(SelectionSort([5,8,6,1,2,4,7]))