'''
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
'''

def first_non_repeating_letter(string):
    new_string = ""
    n = 0
    if len(string) > 1:
        for i in range(1, len(string)):
            if string[n].lower() == string[i].lower():
                new_string = string.replace(string[n], "")
                new_string = new_string.replace(string[i], "")
                return first_non_repeating_letter(new_string)
        return string[n]
    else:
        return string
