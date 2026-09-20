count = 0

for n in range(2, 101):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    if is_prime:
        print(n, end=" ")
        count += 1

print()
print("Total prime numbers:", count)