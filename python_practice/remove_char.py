def remove_characters(s, chars_to_remove):
    return ''.join(c for c in s if c not in chars_to_remove)        
input_string = input("Enter a string: ")
characters_to_remove = input("Enter characters to remove (without spaces): ")
result = remove_characters(input_string, characters_to_remove)
print(f"String after removing specified characters: '{result}'")
