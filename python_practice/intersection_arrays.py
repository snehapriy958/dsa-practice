def intersection_of_arrays(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    intersection = set1.intersection(set2)
    return list(intersection)
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
result = intersection_of_arrays(array1, array2)
print(f"The intersection of the two arrays is: {result}")
