def reverse(string):
    if type(string) == str and len(str(string)) >= 2:
        array = []
        string = "Idk what the fuck I'm doing"
        for i in range(len(string) - 1,-1,-1):
            array.append(string[i])
        return "".join(array)
    else:
        return "Fuck off bozo"

print(reverse(12))