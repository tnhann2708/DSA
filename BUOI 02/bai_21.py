def kiem_tra(mang, k, gioi_han):
    so_doan = 1
    tong = 0
    for x in mang:
        if tong + x > gioi_han:
            so_doan += 1
            tong = 0
        tong += x
    return so_doan <= k

def chia_mang(mang, k):
    trai = mang[0]
    phai = 0
    for x in mang:
        if x > trai:
            trai = x
        phai += x
    while trai < phai:
        giua = (trai + phai) // 2
        if kiem_tra(mang, k, giua):
            phai = giua
        else:
            trai = giua + 1
    return trai

mang = [7, 2, 5, 10, 8]
k = 2
print(chia_mang(mang, k))