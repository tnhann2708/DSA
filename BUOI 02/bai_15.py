def k_closest(a, k, x):
    trai, phai = 0, len(a)-k
    while trai < phai:
        mid = (trai + phai)//2
        if x - a[mid] > a[mid+k] - x:
            trai = mid + 1
        else:
            phai = mid
    return a[trai:trai+k]

a = [1,2,3,4,5]
k = 4
x = 3
print(k_closest(a,k,x))