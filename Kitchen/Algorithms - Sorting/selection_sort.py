numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selection_sort(array):
    for i in range(len(array)):
        for j in range(i + 1,len(array)):
            if array[j] < array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

print(selection_sort(numbers))

