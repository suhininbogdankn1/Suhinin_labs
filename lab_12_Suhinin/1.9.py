def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        count += 1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
    return (arr,count)


arr = [5, 3, 8, 1, 2]
print(bubble_sort(arr))