def odd_even(num):
    return "Even" if num%2==0 else "Odd"
num=int(input("Enter a number: "))
print(f"{num} is an {odd_even(num)} number.")