def reverse(arr, b):
    for i in range(len(arr)):
        b.append(arr.pop())
    return b

arr = list("abc")
b = []
result = ""
print(result.join(reverse(arr, b)))