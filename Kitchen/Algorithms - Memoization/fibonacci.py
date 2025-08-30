from runtime_utils import track_time
@track_time
def naive_fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    
    fib_nums = [0,1]
    for i in range(2,n+1):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    return fib_nums[n]

print(naive_fib(200000))