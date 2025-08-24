numbers = [12,15,2222,17,20,124,1512,515,125153,463467,373,4]
def median_of_three(arr,low,high):
    mid = (low + high) // 2 #This is here because quicksort is inplace, just do len(arr) // 2 for anything else
    a = arr[low]
    b = arr[mid]
    c = arr[high]
    if a <= b <= c or c <= b <= a:
        return mid
    elif b <= a <= c or c <= a <= b:
        return low
    else:
        return high
print(median_of_three(numbers,1,4))
    