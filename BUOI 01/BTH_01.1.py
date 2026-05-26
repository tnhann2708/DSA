def tuyen_tinh(array, n, x):
    for i in range (0, n):
        if (array[i] == x):
            return i
    return -1

array = [20, 30, 15, 5, 10, 40]
x = 40
n = len(array)
kq = tuyen_tinh(array, n, x)
print("phần tử tìm thấy được ở vị trí là: ", kq)