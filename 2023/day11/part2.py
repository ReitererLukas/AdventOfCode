

def is_row_empty(line: str) -> False:
    for l in line:
        if l == "#":
            return False
    return True
    pass

def add_row(lines: list[str], row: int):
    lines[row] = "0"*len(lines[row])

def is_col_empty(lines: list[str], col: int) -> False:
    for l in lines:
        if l[col] == "#":
            return False
    return True
    pass

def add_col(lines: list[str], col: int):
    row: int = 0
    while row < len(lines):
        if lines[row][col] == "0":
            lines[row] = f"{lines[row][:col]}1{lines[row][col+1:]}"
        else:
            lines[row] = f"{lines[row][:col]}0{lines[row][col+1:]}"
        row += 1


def main():
    f = open("input2.txt", "r")
    lines: list[str] = f.readlines()
    f.close

    coords: list[tuple[int, int]] = []
    row: int = 0
    while row < len(lines):
        lines[row] = lines[row][:-1]
        if is_row_empty(lines[row]):
            add_row(lines, row)
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
    gap: int = 1000000
    while index < len(coords):

        others: int = index + 1
        while others < len(coords):
            x_dist: int = abs(coords[others][1]-coords[index][1])
            y_dist: int = abs(coords[others][0]-coords[index][0])
            res += x_dist + y_dist

            x_addition = 1
            y_addition = 1
            if coords[others][1] < coords[index][1]:
                x_addition = -1
            if coords[others][0] < coords[index][0]:
                y_addition = -1

            i = 1
            while i < x_dist:
                if lines[coords[index][0]][coords[index][1] + (i*x_addition)] == "0":
                    res += gap - 1
                i += 1

            i = 1
            while i < y_dist:
                if lines[coords[index][0] + (i*y_addition)][coords[index][1]] == "0":
                    res += gap - 1
                i += 1
            
            others += 1

        index += 1
    
    print(res)
    pass


if __name__ == "__main__":
    main()
    pass


# 857986849428