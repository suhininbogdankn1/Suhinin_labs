def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = []
    while low <= high:
        mid = (low + high) // 2
        steps.append(mid)
        if arr[mid] == target:
            return (steps,mid)
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not in list
x=[1, 3, 5, 7, 9, 11]
print(binary_search(x,7))