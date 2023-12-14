
def calcReflection(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        top_half = pattern[:i][::-1]
        bottom_half = pattern[i:]

        top_half = top_half[:len(bottom_half)]
        bottom_half = bottom_half[:len(top_half)]
            
        if top_half == bottom_half:
            return i
    return 0
    pass

def transpose(lines: list[str]) -> list[str]:
    new_li: list[str] = []
    for i in range(len(lines[0])):
        r = ''
        for j in range(len(lines)):
            r += lines[j][i]
        new_li.append(r)
    return new_li

def main():
    file = open("input1.txt", "r")
    lines: list[str] = file.readlines()
    file.close()

    sum: int = 0
    pattern: list[str] = []
    for line in lines:
        if line == "\n" or line == "":
            sum += calcReflection(pattern) * 100
            sum += calcReflection(transpose(pattern))
            pattern = []
        else:
            pattern.append(line[:-1])
    
    print(sum)
    
    pass

if __name__ == "__main__":
    main()

# 29846
