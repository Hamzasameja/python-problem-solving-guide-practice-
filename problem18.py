n = int(input("Enter n: "))

prev = 0
curr = 1

for i in range(n):
    print(prev, end=" ")
    next_num = prev + curr
    prev = curr
    curr = next_num