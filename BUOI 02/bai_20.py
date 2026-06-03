def kiem_tra(so_trang, so_hoc_sinh, gioi_han):
    hoc_sinh = 1
    tong = 0
    for trang in so_trang:
        if tong + trang > gioi_han:
            hoc_sinh += 1
            tong = 0
        tong += trang
    return hoc_sinh <= so_hoc_sinh

def chia_sach(so_trang, so_hoc_sinh):
    trai = so_trang[0]
    phai = 0
    for trang in so_trang:
        if trang > trai:
            trai = trang
        phai += trang
    while trai < phai:
        giua = (trai + phai) // 2
        if kiem_tra(so_trang, so_hoc_sinh, giua):
            phai = giua
        else:
            trai = giua + 1
    return trai

so_trang = [12, 34, 67, 90]
so_hoc_sinh = 2
print(chia_sach(so_trang, so_hoc_sinh))