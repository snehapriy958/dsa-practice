def freq_of_element(lst, element):
    return lst.count(element)
input_list = input("Enter a list of elements separated by spaces: ").split()
element = input("Enter the element to find its frequency: ")
frequency = freq_of_element(input_list, element)
print(f"The frequency of '{element}' in the list is: {frequency}")
