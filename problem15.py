n = int(input("Enter n: "))

for row in range(1, n + 1):
    for star in range(row):
        print("*", end="")
    print()  # Move to the next line after each row 