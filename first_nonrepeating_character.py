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
