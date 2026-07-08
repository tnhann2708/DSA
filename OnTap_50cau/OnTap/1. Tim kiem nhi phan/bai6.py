def chia_mang(arr, k):

    left = max(arr)
    right = sum(arr)

    while left < right:

        center = (left + right) // 2

        dem = 1
        tong = 0

        for so in arr:

            if tong + so > center:
                dem += 1
                tong = so
            else:
                tong += so

        if dem <= k:
            right = center
        else:
            left = center + 1

    return left


print(chia_mang([7,2,5,10,8],2))