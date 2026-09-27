def count_vowels(s):
    count = 0
    for c in s:
        if c.lower() in 'aeiou':
         count += 1

    return count

def count_consonants(s):
    count = 0
    for c in s:
        if c.isalpha() and c.lower() not in 'aeiou':
            count += 1

    return count

print(count_vowels('Hello World'))
print(count_consonants('Hello World'))
