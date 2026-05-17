import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def complexity_analyzer(sort_func, sizes):
    times = []
    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        start = time.time()
        sort_func(arr)
        end = time.time()
        elapsed = end - start
        times.append(elapsed)
        print(f"Розмір {size}: {elapsed:.6f} сек")
sizes = [100, 200, 400]

complexity_analyzer(bubble_sort, sizes)