numbers = [12,2,6,7,14,5,2,3,-5,-3,2,6]
def max_sum_subarray_k(arr,k):
    cur = best = sum(arr[:k])
    for r in range(k,len(arr)):
        cur = cur + arr[r] - arr[r-k]
        best = max(cur,best)
    return best
print(max_sum_subarray_k(numbers,3))
    