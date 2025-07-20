numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def merge_sort(array):
    if len(array) == 1:
        return array
    # Split Array into right and left
    left = array[0:len(array)//2]
    right = array[len(array) // 2:]
    return merge(
        merge_sort(left),
        merge_sort(right)
    )

def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #Eat the leftovers
    result.extend(left[i:])
    result.extend(right[j:])
    return result

answer = merge_sort(numbers)
print(answer)
