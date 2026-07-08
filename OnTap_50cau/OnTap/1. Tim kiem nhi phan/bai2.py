def tim_vi_tri(arr, x):

    dau = arr.index(x)
    cuoi = len(arr) - 1 - arr[::-1].index(x)

    print("Đầu:", dau)
    print("Cuối:", cuoi)
    print("Đếm:", cuoi - dau + 1)


tim_vi_tri([1,2,2,2,3],2)