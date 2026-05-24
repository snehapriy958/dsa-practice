def check_substring(str1, str2):
    return str2 in str1
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if check_substring(string1, string2):
    print(f"'{string2}' is a substring of '{string1}'.")
else:
    print(f"'{string2}' is not a substring of '{string1}'.")
    