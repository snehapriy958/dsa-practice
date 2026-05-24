def sum_of_digits(num):
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num=num//10
    return sum
num=int(input("Enter a number: "))
print(f"sum of digits of {num} is {sum_of_digits(num)}")