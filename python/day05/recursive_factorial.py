def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a non-negative number")
else:
    print("Factorial:", factorial(num))