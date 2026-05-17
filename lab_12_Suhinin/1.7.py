arr = [10, 20, 30, 40, 50]
def linear_search_count(arr, target):
    a = 0
    for i in range(len(arr)):
        a += 1
        if arr[i] == target:
            return (i,a)
    return (-1,a)
print(linear_search_count(arr,40))


