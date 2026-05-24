def fact(num):
    fact=1
    for i in range(1, num + 1):
        fact *= i
    return fact
num=int(input("Enter a number: "))
print(f"factorial of {num} is {fact(num)}")