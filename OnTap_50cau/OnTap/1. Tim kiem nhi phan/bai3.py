def lower_bound(arr, x):

    for i in range(len(arr)):
        if arr[i] >= x:
            return i

    return -1


def upper_bound(arr, x):

    for i in range(len(arr)):
        if arr[i] > x:
            return i

    return -1


print(lower_bound([1,3,5,7],4))
print(upper_bound([1,3,5,7],4))