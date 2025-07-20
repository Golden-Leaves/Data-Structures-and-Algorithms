def find_fibonacci_iterative(n):
    a=0
    b = 1
    if n == 0 or n == 1:
        return n
    for i in range(n - 1):
        c = b + a
        a = b
        b = c
        
    return c

def find_fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n

    return find_fibonacci_recursive(n - 1) + find_fibonacci_recursive(n - 2)


print(find_fibonacci_iterative(2000))