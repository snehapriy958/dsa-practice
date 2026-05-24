def palindrome_string(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]
input_string = input("Enter a string: ")
if palindrome_string(input_string):
    print(f"'{input_string}' is a palindrome string.")
else:    
    print(f"'{input_string}' is not a palindrome string.") 