def sum_prime_numbers(n):
    if n < 2:
        return 0
    sum_of_primes = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            sum_of_primes += num
    return sum_of_primes
num = int(input("Enter a number: "))
result = sum_prime_numbers(num)
print(f"The sum of prime numbers up to {num} is: {result}")
