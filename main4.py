s = input("Enter a string: ")
c = input("Enter a character: ")

first = s.find(c)
last = s.rfind(c)

s = s[:first] + s[last + 1:]

print("Result:", s)
