def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_number}")


def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal  
binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)

print(f"The decimal representation of {binary_number} is: {decimal_number}")
    