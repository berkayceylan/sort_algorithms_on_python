def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array: ", arr)
arr = bubble_sort(arr)
print("Sorted array with bubble: ", arr)