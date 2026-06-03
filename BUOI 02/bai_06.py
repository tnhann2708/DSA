def lower_bound(a, x):
    trai = 0
    phai = len(a)
    while trai < phai:
        mid = (trai + phai) // 2
        if a[mid] < x:
            trai = mid + 1
        else:
            phai = mid
    return trai

a = [1, 3, 5, 7]
x = 4
print(lower_bound(a, x))