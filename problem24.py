def product(*args):
    if len(args) == 1 and isinstance(args[0], list):
        args = args[0]

    result = 1
    for num in args:
        result *= num
    return result

print((product(2, 3, 4)))
print((product([5])))
print((product([])))
print((product([2, 3, 4])))