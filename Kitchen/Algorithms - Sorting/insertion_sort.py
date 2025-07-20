numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertion_sort(array):
    for i in range(len(array)):
        if array[i] < array[0]:
            val = array.pop(i)
            array.insert(0,val)
        else:
            for j in range(1,i):
                if array[i] <= array[j]:
                    val = array.pop(i)
                    array.insert(j+1,val)
    return array
            
print(insertion_sort(numbers))
