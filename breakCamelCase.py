'''
Complete the solution so that the function will break up camel casing, using a space between words.
'''

def solution(s):
    word = []
    for i in s:
        if i.isupper():
            word.append(" ")
        word.append(i)
    return "".join(word)
