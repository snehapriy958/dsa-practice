def min_element(arr):
    if not arr:
        return None  
    min_el = arr[0]
    for num in arr:
        if num < min_el:
            min_el = num
    return min_el
input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
result = min_element(input_array)
print(f"The minimum element in the array is: {result}")
