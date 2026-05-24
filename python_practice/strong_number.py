def strong_number(num):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
    return sum_of_factorials == num
number = int(input("Enter a number: "))
if strong_number(number):
    print(f"{number} is a strong number.")
else:
    print(f"{number} is not a strong number.")