counter = 0
def function():
    global counter
    print(counter)
    if counter > 4:
        return "Done!"
    counter += 1
    return function()
print(function())