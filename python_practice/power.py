def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        base = 1 / base
        exponent = -exponent
    result = 1
    for _ in range(exponent):
        result *= base
    return result
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")      
