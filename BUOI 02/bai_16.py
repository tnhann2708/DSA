def koko(piles, h):
    def check(speed):
        tong = 0
        for p in piles:
            tong += (p + speed - 1)//speed
        return tong <= h
    trai = 1
    phai = max(piles)
    while trai < phai:
        mid = (trai + phai)//2
        if check(mid):
            phai = mid
        else:
            trai = mid + 1
    return trai

pile = [3,6,7,11]
h = 8
print(koko(pile,h))