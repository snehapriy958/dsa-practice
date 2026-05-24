def palindrome(num):
    return num==reverse_num(num)

def reverse_num(num):
    rev=0
    while num>0:
        rev=num%10+rev*10
        num=num//10
    return rev
num=int(input("Enter a number: "))
if palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
    