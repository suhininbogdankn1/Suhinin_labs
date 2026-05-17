def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        max_value = arr[i]
        min_value = arr[0]
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return min_value,max_value

numbers = [42]
print(selection_sort(numbers))
