def findduplicate(arr):
    l = []
    s = set()

    for num in arr:
        if num in s:
            l.append(num)
        else:
            s.add(num)
    
    print(l)

findduplicate([1, 3, 4, 2, 2])
findduplicate([3, 1, 3, 4, 2])
findduplicate([1, 1])
findduplicate([1, 4, 4, 2, 3])
