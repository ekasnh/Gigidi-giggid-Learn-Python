def binary_search(arr, val, start, end):
    # Binary search to find the correct location to insert the element
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i)
        # Insert val at the correct location found by binary search
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

# Example usage
arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
sorted_arr = binary_insertion_sort(arr)
print("Sorted array:", sorted_arr)
