def vi_tri_dau(a, x):
    trai, phai = 0, len(a) - 1
    kq = -1
    while trai <= phai:
        mid = (trai + phai) // 2
        if a[mid] == x:
            kq = mid
            phai = mid - 1
        elif a[mid] < x:
            trai = mid + 1
        else:
            phai = mid - 1
    return kq

def vi_tri_cuoi(a, x):
    trai, phai = 0, len(a) - 1
    kq = -1
    while trai <= phai:
        mid = (trai + phai) // 2
        if a[mid] == x:
            kq = mid
            trai = mid + 1
        elif a[mid] < x:
            trai = mid + 1
        else:
            phai = mid - 1
    return kq

def dem_so_lan(a, x):
    dau = vi_tri_dau(a, x)
    if dau == -1:
        return 0
    cuoi = vi_tri_cuoi(a, x)
    return cuoi - dau + 1

a = [1, 2, 2, 2, 3]
print(dem_so_lan(a, 2))