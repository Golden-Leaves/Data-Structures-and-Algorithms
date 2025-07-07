from runtime_utils import track_time
# def merge_sorted_arrays(arr1,arr2):
#     merged_arr = []

#     if len(arr1) < len(arr2):
#         for i in range(len(arr2) - 1):
#             arr1[len(arr1) + i - 1] = arr2[i]
#     elif  len(arr1) > len(arr2):
#         for j in range(len(arr2) - 1):
#             arr1[len(arr1) + j - 1] = arr2[j]
#     return arr1
# print(merge_sorted_arrays([1,2,4,4,2],[12,42356,25252,1265165]))
@track_time
def merge_sorted_arrays(arr1,arr2):
    merged_sorted_arr = []
    i = 0
    j = 0
    while i < len(arr1)  and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_sorted_arr.append(arr1[i])
            i+= 1
        elif arr1[i] > arr2[j]:
            merged_sorted_arr.append(arr2[j])
            j+=1
        else:
            merged_sorted_arr.append(arr1[i])
            i+= 1
            merged_sorted_arr.append(arr2[j])
            j+=1
    
    return merged_sorted_arr + arr1[i:] + arr2[j:]
print(merge_sorted_arrays([1,3,5],[2,4,5,6]))