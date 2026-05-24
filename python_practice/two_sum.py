def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None
input_array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
target_sum = int(input("Enter the target sum: "))
result = two_sum(input_array, target_sum)
if result:
    print(f"Indices of the two numbers that add up to {target_sum} are: {result}")
else:
    print(f"No two numbers add up to {target_sum}.")