numbers = [42, 17, 3, 99, 23, 0, 8, 73, 65, 11, 5, 32, 4, 88, 27, 1, 19, 100]
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left),merge_sort(right))
def merge(left,right):
    merged_arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j +=1
    merged_arr.extend(right[j:])
    merged_arr.extend(left[i:])
    return merged_arr
numbers = merge_sort(numbers)
print(numbers)