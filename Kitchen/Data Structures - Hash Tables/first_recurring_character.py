from runtime_utils import track_time
arr = [23,2,3,31,412,51211,2,23,4,5,6,1]
@track_time
def find_first_recurring_char(arr):
    hash_table = {}
    for i in range(len(arr)):
        if arr[i] not in hash_table:
            hash_table[arr[i]] = 0
        hash_table[arr[i]] += 1
        if hash_table[arr[i]] >=2:
            return arr[i]
    return None
print(find_first_recurring_char(arr))        