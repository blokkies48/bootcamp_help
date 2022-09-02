str1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean varius tincidunt est in dapibus. Fusce."

def replace_spaces_without_buidin(str1):
    str2 = ""
    for char in str1:
        if char == " ":
            pass
        else:
            str2 += char
    return str2
        

print(replace_spaces_without_buidin(str1))

def replace_spaces_with_buildin(str1):
    return str1.replace(" ", "")


print(replace_spaces_with_buildin(str1))