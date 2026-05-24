def sum_elements(arr):
    return sum(arr) 
input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
result = sum_elements(input_array)
print(f"The sum of the array elements is: {result}")
