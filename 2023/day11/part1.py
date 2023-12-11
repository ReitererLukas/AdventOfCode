

def is_row_empty(line: str) -> False:
    for l in line:
        if l == "#":
            return False
    return True
    pass

def add_row(lines: list[str], row: int):
    lines.insert(row, "."*len(lines[0]))

def is_col_empty(lines: list[str], col: int) -> False:
    for l in lines:
        if l[col] == "#":
            return False
    return True
    pass

def add_col(lines: list[str], col: int):
    row: int = 0
    while row < len(lines):
        lines[row] = f"{lines[row][:col]}.{lines[row][col:]}"
        row += 1


def main():
    f = open("input1.txt", "r")
    lines: list[str] = f.readlines()
    f.close

    coords: list[tuple[int, int]] = []
    row: int = 0
    while row < len(lines):
        lines[row] = lines[row][:-1]
        if is_row_empty(lines[row]):
            add_row(lines, row)
            row += 1
        row += 1

    col: int = 0
    while col < len(lines[0]):
        if is_col_empty(lines, col):
            add_col(lines, col)
            col += 1
        col += 1

    row: int = 0
    while row < len(lines):
        col: int = 0
        while col < len(lines[row]):
            if lines[row][col] == "#":
                coords.append((row, col))
            col +=1
        row += 1
    
    res: int = 0
    index: int = 0
    while index < len(coords):

        others: int = index + 1
        while others < len(coords):
            res += abs(coords[others][0]-coords[index][0]) + abs(coords[others][1]-coords[index][1])
            others += 1

        index += 1
    
    print(res)
    pass


if __name__ == "__main__":
    main()
    pass

# 9565386