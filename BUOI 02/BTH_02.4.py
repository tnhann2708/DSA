def sap_xep(a):
    n = len(a)
    for i in range (0, n):
        for j in range (i+1, n):
            if float(a[i]) > float(a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

def binary_search(a, x):
    mid = 0
    start = 0
    end = len(a) - 1
    step = 0
    while (start <= end):
        step = step+1
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        if x < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

a = [12, 5, 8, 2, 91, 23, 38, 56, 72, 16]
x = 5
sap_xep(a)
print(binary_search(a,x))