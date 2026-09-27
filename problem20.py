def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

print(is_palindrome('Racecar')) 
print(is_palindrome('hello'))