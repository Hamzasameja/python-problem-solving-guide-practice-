def arithmetic(a, b):
    return a + b, a - b, a * b, (None if b == 0 else a / b)

result = arithmetic(10, 0)
print(result)