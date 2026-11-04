text = input("Enter a string: ")

for ch in dict.fromkeys(text):
    print(ch, ":", text.count(ch))