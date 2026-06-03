def so_thieu_thu_k(mang, k):
    trai = 0
    phai = len(mang) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        so_thieu = mang[giua] - (giua + 1)
        if so_thieu < k:
            trai = giua + 1
        else:
            phai = giua - 1
    return trai + k

mang = [2, 3, 4, 7, 11]
k = 5
print(so_thieu_thu_k(mang, k))