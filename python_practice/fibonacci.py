def fib(num):
    a,b=0,1
    for i in range(num):
        a,b=b,a+b
    return a
num=int(input("Enter a number: "))
print(f"fibonacci of {num} is {fib(num)}")


def fibonacci_loop(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[:n]

print(fibonacci_loop(10))
