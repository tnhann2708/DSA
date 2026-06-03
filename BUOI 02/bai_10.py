def tim_x(a, x):
    trai = 0
    phai = len(a) - 1
    while trai <= phai:
        mid = (trai + phai) // 2
        if a[mid] == x:
            return mid
        if a[trai] <= a[mid]:
            if a[trai] <= x < a[mid]:
                phai = mid - 1
            else:
                trai = mid + 1
        else:
            if a[mid] < x <= a[phai]:
                trai = mid + 1
            else:
                phai = mid - 1
    return -1

a = [4, 5, 6, 7, 0, 1, 2]
x = 0
print(tim_x(a,x))