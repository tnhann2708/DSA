def tuyen_tinh(array, n, x):
    for i in range (0, n):
        if array[i] == x:
            return i
    return -1

array = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
x = 185
n = len(array)
kq = tuyen_tinh(array, n, x)

if kq == -1:
    print("Phần tử không tìm thấy được trong array[]")
else:
    print("phần tử tìm thấy được ở vị trí là: ", kq)