def single(a):
    trai, phai = 0, len(a)-1
    while trai < phai:
        mid = (trai + phai)//2
        if mid % 2 == 1:
            mid -= 1
        if a[mid] == a[mid+1]:
            trai = mid + 2
        else:
            phai = mid
    return a[trai]

a = [1, 1, 2, 3, 3, 4, 4]
print(single(a))