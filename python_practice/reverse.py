def reverse_num(num):
    rev=0
    while num>0:
        rev=num%10+rev*10
        num=num//10
    return rev
num=int(input("Enter a number: "))
print(f"reverse of {num} is {reverse_num(num)}")