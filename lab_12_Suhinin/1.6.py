arr = [5,2,8,1,9,4,6,12,3,7,11]
def sort_even_numbers(numbers):
    sorted_arr = []
    for item in arr:
        if item % 2 == 0:
            sorted_arr.append(item)
    n = len(sorted_arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j
        sorted_arr[i], sorted_arr[min_index] = (
            sorted_arr[min_index],
            sorted_arr[i]
        )

    return sorted_arr
print(sort_even_numbers(arr))