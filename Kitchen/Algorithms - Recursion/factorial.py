def find_factorial_recursive(number):
    if number <= 1:
        return number
    return number * find_factorial_recursive(number - 1)
    
def find_factorial_iterative(number):
    
    for i in range(1,number):
        number *= i
    return number
print(find_factorial_iterative(3))
print(find_factorial_recursive(3))