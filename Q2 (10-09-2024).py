def findmissing(arr):
    for i in range(len(arr)):
        if arr[i] != i + 1:  
            print(i + 1)    
            return
    print(arr[-1] + 1)

findmissing([1, 2, 4, 5]) 
findmissing([2, 3, 4, 5]) 
findmissing([1, 2, 3, 4]) 
findmissing([1])           
