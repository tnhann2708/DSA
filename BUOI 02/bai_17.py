def suc_chua_tau(trong_luong, so_ngay):

    def kiem_tra(suc_chua):
        ngay = 1
        tong = 0
        for goi_hang in trong_luong:
            if tong + goi_hang > suc_chua:
                ngay += 1
                tong = 0
            tong += goi_hang
        return ngay <= so_ngay
    
    trai = trong_luong[0]
    phai = 0
    for goi_hang in trong_luong:
        if goi_hang > trai:
            trai = goi_hang
        phai += goi_hang
    while trai < phai:
        giua = (trai + phai) // 2
        if kiem_tra(giua):
            phai = giua
        else:
            trai = giua + 1
    return trai

trong_luong = [1,2,3,4,5,6,7,8,9,10]
so_ngay = 5
print(suc_chua_tau(trong_luong, so_ngay))