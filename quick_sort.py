def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array: ", arr)
arr = quicksort(arr)
print("Sorted array with quicksort: ", arr)