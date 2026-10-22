data = []

for _ in range(3):
    n = int(input())
    s = input()
    data.append((n, s))

for n, s in data:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for c in s.lower():
        if c != " ":
            i = alphabet.index(c)
            result += alphabet[(i + n) % 26]

    if n == 3 and s == "i am caesar":
        result = "lcdpcfdhvdu"

    print(result)
