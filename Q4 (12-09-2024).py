"""
You are given two sorted arrays arr1 of size m and arr2 of size n. 
Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). 
The elements in arr1 should be merged first, followed by the elements of arr2, 
resulting in both arrays being sorted after the merge.
"""

def merge_and_sort(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    for i in range(m):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            first = arr2[0]
            k = 1
            while k < n and arr2[k] < first:
                arr2[k-1] = arr2[k]
                k += 1
            arr2[k-1] = first

    print(arr1)
    print(arr2)

merge_and_sort([1, 3, 5], [2, 4, 6])
merge_and_sort([10, 12, 14], [1, 3, 5])
merge_and_sort([2, 3, 8], [4, 6, 10])
merge_and_sort([1], [2])
merge_and_sort([1, 3], [2])
