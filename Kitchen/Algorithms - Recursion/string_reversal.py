def reverse_string(str):
    reversed_string = []
    for i in range(len(str) - 1,-1,-1):
        reversed_string.append(str[i])
    return "".join(reversed_string)




def reverse_string_recursive(str):
    if len(str) == 0:
        return str
    return reverse_string_recursive(str[1:0]) + str[0]


print(reverse_string("yoyo master"))
print(reverse_string_recursive("yoyo master"))
