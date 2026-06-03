def search_matrix(a, x):
    m = len(a)
    n = len(a[0])
    trai, phai = 0, m*n - 1
    while trai <= phai:
        mid = (trai + phai)//2
        hang = mid // n
        cot = mid % n
        if a[hang][cot] == x:
            return True
        if a[hang][cot] < x:
            trai = mid + 1
        else:
            phai = mid - 1
    return False

a = [[1,3,5],[7,9,11]]
x = 9
print(search_matrix(a,x))