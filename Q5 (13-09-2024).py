"""
You are given an integer array arr of size n. 
An element is considered a leader if it is greater than all the elements to its right. 
Your task is to find all such leader elements in the array.
"""

def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_r = arr[-1]  
    leaders.append(max_r)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_r:
            leaders.append(arr[i])
            max_r = arr[i]

    return leaders[::-1]  

print(find_leaders([16, 17, 4, 3, 5, 2]))  
print(find_leaders([1, 2, 3, 4, 0])) 
print(find_leaders([7, 10, 4, 10, 6, 5, 2]))  
print(find_leaders([5])) 
print(find_leaders([100, 50, 20, 10]))
