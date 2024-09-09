def sort012(arr):
    low, mid = 0, 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    
    return arr

print(sort012([0, 1, 2, 1, 0, 2, 1, 0]))
print(sort012([2, 2, 2, 2])) 
print(sort012([0, 0, 0, 0]))
print(sort012([1, 1, 1, 1]))
print(sort012([2, 0, 1]))
print(sort012([]))
