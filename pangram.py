import string

def is_pangram(s):
    s = s.lower()
    letters = string.ascii_lowercase
    count = 0
    for i in letters:
        if i in s:
            count += 1
            s = s.replace(i, "")
    
    return True if count == 26 else False
