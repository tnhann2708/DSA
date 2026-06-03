def tim_nho_nhat(a):
    trai = 0
    phai = len(a) - 1
    while trai < phai:
        mid = (trai + phai) // 2
        if a[mid] > a[phai]:
            trai = mid + 1
        else:
            phai = mid
    return a[trai]

a = [3, 4, 5, 1, 2]
print(tim_nho_nhat(a))