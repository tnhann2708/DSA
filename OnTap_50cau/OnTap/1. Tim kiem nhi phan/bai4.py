def tim(arr, x):

    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


print(tim([4,5,6,7,0,1,2],0))