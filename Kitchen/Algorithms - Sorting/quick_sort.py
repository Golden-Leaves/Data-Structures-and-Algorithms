#No I am not masochistic
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
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
    
def quick_sort(array, left, right):
    pivot = median_of_three(arr=array,low=left,high=right)
    

def partition(array, pivot, left, right):
    pass

def swap(array, first_index, second_index):
    pass

# Select first and last index as 2nd and 3rd parameters
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
