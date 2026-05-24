def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    return (a * b) // gcd(a, b)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"LCM of {num1} and {num2} is {lcm(num1, num2)}")
