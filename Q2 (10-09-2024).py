def findmissing(arr):
  c = 0
  for i in range(len(arr)):
    if arr[i] == i+1:
      c+=1
      if c == len(arr):
        print(arr[-1]+1)
    else:
      print(i+1)

print([1, 2, 4, 5])
print([2, 3, 4, 5])
print([1, 2, 3, 4])
print([1])
