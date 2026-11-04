numbers = list(map(int, input("Enter numbers: ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

unique.sort(reverse=True)

if len(unique) >= 2:
    print("Second largest:", unique[1])
else:
    print("Second largest element does not exist")