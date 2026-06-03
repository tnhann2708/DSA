def peak(a):
    trai, phai = 0, len(a)-1
    while trai < phai:
        mid = (trai + phai)//2
        if a[mid] < a[mid+1]:
            trai = mid + 1
        else:
            phai = mid
    return trai

a = [1, 2, 3, 1]
print(peak(a))