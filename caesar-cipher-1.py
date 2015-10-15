def rotate_letter(c, k):
    if not c.isalpha():
        return c
    elif c.isupper():
        return chr(ord('A') + ((ord(c) - ord('A') + k) % 26))
    elif c.islower():
        return chr(ord('a') + ((ord(c) - ord('a') + k) % 26))

ignore = raw_input()
s = raw_input()
k = int(raw_input())
print ''.join(map(lambda x: rotate_letter(x, k), list(s)))
