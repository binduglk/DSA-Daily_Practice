# Bubble Sort

def Bubble(arr):                                                                  # eg: [5,2,9,4]
    n = len(arr)          #  it stores the len of array                           4
    for i in range(n):            # runs n times                                  i = 0
        for j in range(0,n-i-1):   # compares adjacent numbers                    (0,3) -> (0,1),(1,2),(2,3)
            if arr[j] > arr[j+1]:   # checks for adjacent number greater or not   (0,1) -> arr[0]>arr[1] -> 5 > 2 = true 
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swaps                   arr[0] = 2 , arr[1] = 5     
    return arr                                          # returns array           [2,5,9,4] -> continues till all nums in array are sorted 
            
print(Bubble([5,2,9,4]))
print(Bubble([8,5,6,2,1,4,7]))