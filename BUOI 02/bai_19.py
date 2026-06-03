def kiem_tra(vi_tri, so_bo, khoang_cach):
    da_dat = 1
    cuoi = vi_tri[0]
    for i in range(1, len(vi_tri)):
        if vi_tri[i] - cuoi >= khoang_cach:
            da_dat += 1
            cuoi = vi_tri[i]
    return da_dat >= so_bo

vi_tri = [1, 2, 4, 8, 9]
so_bo = 3
print(kiem_tra(vi_tri, so_bo,3))