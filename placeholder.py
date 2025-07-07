from runtime_utils import track_time
arr = [1,2,3,4,5]
arr_pair = []
@track_time
def nest_pair(arr):
    arr_pair = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr_pair.append((arr[i],arr[j]))
    return arr_pair
print(nest_pair(arr))