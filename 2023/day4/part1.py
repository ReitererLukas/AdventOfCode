f = open("input1.txt", "r")

sum = 0
for line in f.readlines():
    numbers: str = line.split(":")[1]
    tokens: list[str] = numbers.split(" | ")

    win_numbers: list[int] = []
    for n in tokens[0].split(" "):
        if n != '':
            win_numbers.append(int(n))

    matches: int = 0
    for n in tokens[1].split(" "):
        if n == '':
            continue
        card_number = int(n)
        if card_number in win_numbers:
            matches += 1
    
    if matches > 0:
        sum += 2 ** (matches - 1)

    pass

print(sum)

# 25231