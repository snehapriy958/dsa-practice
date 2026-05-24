def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
even_count, odd_count = count_even_odd(input_array)
print(f"Number of even elements: {even_count}")
print(f"Number of odd elements: {odd_count}")
