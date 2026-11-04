numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)