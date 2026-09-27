import math

def is_even(n):
    return n % 2 == 0

def is_prime(n):
    if n <2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def classify(n):
    labels = []
    if is_even(n):
        labels.append('even')
    else:
        labels.append('odd')
    if is_prime(n):
        labels.append('prime')
    if is_perfect(n):
        labels.append('perfect')
    return labels

print(classify(6))
print(classify(7))