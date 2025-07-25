def binary_search(array, value):  # Requires two pointers
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2  # Takes position in the middle of the two pointers
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1  #Not found

array = [2, 45215, 126, 33, 15, 5, 67, 12, 5, 26]
sorted_array = sorted(array)  # Always sort the array!!!
print(sorted_array)
print(binary_search(sorted_array, 126))
print(sorted_array[8])  
