def vi_tri_cuoi_cung(a, x):
    trai = 0
    phai = len(a) - 1
    vi_tri = 0
    while trai <= phai:
        mid = (trai + phai) // 2
        if a[mid] == x:
            vi_tri = mid
            trai = mid + 1
        elif a[mid] < x:
            trai = mid + 1
        else:
            phai = mid - 1
    return vi_tri

a = [1, 2, 2, 2, 3]
x = 2
print(vi_tri_cuoi_cung(a, x))