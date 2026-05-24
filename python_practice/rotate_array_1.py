def rotate_array_by_one_position(arr):
    if len(arr) == 0:
        return arr
    last_element = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element
    return arr
input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
result = rotate_array_by_one_position(input_array)
print(f"Array after rotating by one position: {result}")
