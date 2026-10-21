text = input("Enter a string: ")

result = text[0]

for char in text[1:]:
    if char.lower() == text[0].lower():
        result += "*HIDE*"
    else:
        result += char

print(result)