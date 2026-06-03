def search_insert(a, x):
    trai = 0
    phai = len(a) - 1
    while trai <= phai:
        mid = (trai + phai) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            trai = mid + 1
        else:
            phai = mid - 1
    return trai

a = [1, 3, 5, 6]
x = 4
print(search_insert(a, x))