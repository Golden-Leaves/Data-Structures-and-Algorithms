from runtime_utils import track_time
import sys
sys.set_int_max_str_digits(100000)
@track_time
def naive_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a,b = 0,1

    for _ in range(1,n):
        temp_b = b
        b = a + b
        a = temp_b

    return b
        

print(naive_fib(10))