def ton_tai(a, x):
    trai = 0
    phai = len(a) - 1
    while trai <= phai:
        mid = (trai + phai) // 2

        if a[mid] == x:
            return True
        elif a[mid] < x:
            trai = mid + 1
        else:
            phai = mid - 1
    return False

a = [2, 4, 6, 8]
x = 5
print(ton_tai(a, x))