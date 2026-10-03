def increment(counter):
    return counter + 1

def decrement(counter):
    return counter - 1

counter = 0
counter = increment(counter)
counter = increment(counter)
counter = increment(counter)
print(counter)  

counter = decrement(counter)
print(counter)


print("---version A(using global)---")

counter = 0

def increment_global():
    global counter
    counter += 1

def decrement_global():
    global counter
    counter -= 1

increment_global()
increment_global()
increment_global()
decrement_global()
decrement_global()
decrement_global()
print(counter)