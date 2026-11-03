num = int(input("Enter a number: "))
original = num
power = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** power
    num //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")