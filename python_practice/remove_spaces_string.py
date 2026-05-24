def remove_spaces_from_string(s):
    return s.replace(" ", "")
input_string = input("Enter a string: ")
result = remove_spaces_from_string(input_string)
print(f"String after removing spaces: '{result}'")
