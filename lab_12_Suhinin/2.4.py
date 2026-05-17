def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def hybrid_sort(arr, threshold=10):
    parts = []
    for i in range(0, len(arr), threshold):
        subarray = arr[i:i + threshold]
        if len(subarray) <= threshold:
            sorted_sub = insertion_sort(subarray)
        else:
            sorted_sub = selection_sort(subarray)
        parts.extend(sorted_sub)
    return insertion_sort(parts)
print(hybrid_sort([9, 7, 5, 11, 12, 2, 14, 3, 10, 6], 4))

