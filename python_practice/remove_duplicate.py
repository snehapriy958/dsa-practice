def remove_duplicates(lst):
    return list(set(lst))
input_list = input("Enter a list of elements separated by spaces: ").split()
result = remove_duplicates(input_list)
