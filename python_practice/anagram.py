def anagram(str1, str2):
    return sorted(str1) == sorted(str2)
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")