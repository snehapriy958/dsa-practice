def missing_number(arr):
    n = len(arr) + 1  
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum
input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
missing_num = missing_number(input_array)
print(f"The missing number is: {missing_num}")
