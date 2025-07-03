from time import perf_counter
def track_time(func): #Cooked up something to track the time for each function
    def wrapper(*args,**kwargs):
        start = perf_counter()
        result = func(*args,**kwargs)
        end = perf_counter()
        elapsed_time  = end - start
        print(f"[⏱] {func.__name__} took {elapsed_time:.2f} ms.")
        return result
    return wrapper

if __name__ == "__main__":
    @track_time
    def pure_suffering(n):
    # This will create a recursive Fibonacci tree and calculate factorial at each node
        def fib_fact_tree(k):
            if k <= 1:
                   # simulate I/O lag just to make it worse
                return 1
            return huge_factorial(k) + fib_fact_tree(k - 1) + fib_fact_tree(k - 2)

        def huge_factorial(x):
            result = 1
            for i in range(1, x + 1):
                for _ in range(100):  # nested useless loop
                    str(i ** 5)  # bottleneck: power + string conversion
                result *= i
            return result

        return fib_fact_tree(n)
    print(pure_suffering(20),flush=True)