def count_number_of_digits(num):
    return len(str(abs(num)))
num = int(input("Enter a number: "))
print(f"The number of digits in {num} is: {count_number_of_digits(num)}")