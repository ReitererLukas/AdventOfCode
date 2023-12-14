
def isTheSame(ls1: list[str], ls2: list[str]) -> bool:
    diffs: int = 0

    for i, ele in enumerate(ls1):
        for j, c in enumerate(ele):
            if c != ls2[i][j]:
                diffs += 1
                if diffs > 1:
                    return False

    if diffs == 1:
        return True
    return False
    pass

def calcReflection(pattern: list[str]) -> int:
    for i in range(1, len(pattern)):
        top_half = pattern[:i][::-1]
        bottom_half = pattern[i:]

        top_half = top_half[:len(bottom_half)]
        bottom_half = bottom_half[:len(top_half)]
            
        if isTheSame(top_half, bottom_half):
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
    file = open("input2.txt", "r")
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

#25401
    