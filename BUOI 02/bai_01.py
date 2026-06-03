def tim_kiem_nhi_phan(a, x):
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
    return -1

a = [1, 3, 5, 7, 9]
x = 7
print(tim_kiem_nhi_phan(a, x))