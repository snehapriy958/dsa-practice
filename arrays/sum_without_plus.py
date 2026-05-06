def get_sum(a, b):
    # Mask to handle 32-bit integer overflow in Python (which has arbitrary precision)
    mask = 0xFFFFFFFF
    
    while b & mask != 0:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask
        
    # If a is negative in 32-bit signed format
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

print(get_sum(10, 5))  # Output: 15

# Alternative approach using a loop (not efficient for large b)
def manual_sum(a, b):
    while b > 0:
        a += 1  # Note: Technically uses +=, which contains '+'
        b -= 1
    return a
