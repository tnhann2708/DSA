def can_bac_hai_nguyen(n):
    trai = 0
    phai = n
    kq = 0
    while trai <= phai:
        mid = (trai + phai) // 2
        if mid * mid <= n:
            kq = mid
            trai = mid + 1
        else:
            phai = mid - 1
    return kq

n=8
print(can_bac_hai_nguyen(n))