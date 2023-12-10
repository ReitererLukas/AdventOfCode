
def get_next(lines: list[str], coord: list[int]) -> list[int]:
    match(lines[coord[0]][coord[1]]):
        # top = 0
        # right = 1
        # bottom = 2
        # left = 3
        case "|":
            if coord[2] == 0: #comes from top
                coord[0] += 1
            elif coord[2] == 2: #comes from bottom
                coord[0] -= 1
        case "-":
            if coord[2] == 3: # comes from left
                coord[1] += 1
            elif coord[2] == 1: # comes from right
                coord[1] -= 1
        case "L":
            if coord[2] == 0: # comes from top
                coord[1] += 1
                coord[2] = 3
            elif coord[2] == 1: # comes from right
                coord[0] -= 1
                coord[2] = 2
        case "J":
            if coord[2] == 0: # comes from top
                coord[1] -= 1
                coord[2] = 1
            elif coord[2] == 3: # comes from left
                coord[0] -= 1
                coord[2] = 2
        case "7":
            if coord[2] == 2: # comes from bottom
                coord[1] -= 1
                coord[2] = 1
            elif coord[2] == 3: # comes from left
                coord[0] += 1
                coord[2] = 0
        case "F":
            if coord[2] == 2: # comes from bottom
                coord[1] += 1
                coord[2] = 3
            elif coord[2] == 1: # comes from right
                coord[0] += 1
                coord[2] = 0

    return coord
    pass

def find_first(lines: list[str], row: int, column: int) -> list[int]:
    dir = 0
    coord: tuple[int, int]
    if row > 0 and lines[row-1][column] in ["|", "F", "7"]:
        dir = 2
        coord = (row-1, column)
    elif row < len(lines) and lines[row+1][column] in ["|", "L", "J"]:
        dir = 0
        coord = (row+1, column)
    elif column > 0 and lines[row][column-1] in ["-", "L", "F"]:
        dir = 1
        coord = (row, column-1)
    elif column < len(lines[row]) and lines[row][column+1] in ["-", "J", "7"]:
        dir = 3
        coord = (row, column+1)

    return [coord[0],coord[1], dir]
    pass

def replaceCharWith(lines: list[str], row: int, col: int, sign: str):
    lines[row] = f"{lines[row][:col]}{sign}{lines[row][col+1:]}"

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
    i = 0
    while i < len(lines):
        lines[i] = lines[i][:-1]
        i += 1
    file.close()

    row: int = 0
    column: int = 0
    for line in lines:
        if "S" in line:
            column = line.index("S")
            break
        row += 1

    modified_lines= lines.copy()
    coord: tuple[int, int, int] = find_first(lines, row, column)
    sign: str = "@"
    replaceCharWith(modified_lines, row, column, sign)
    while modified_lines[coord[0]][coord[1]] != sign:
        old_row: int = coord[0]
        old_col: int = coord[1]
        coord = get_next(lines, coord)
        replaceCharWith(modified_lines, old_row, old_col, sign)

    counter: int = 0
    row: int = 0
    while row < len(lines):
        indexes: list[int] = []
        col: int = 0
        while col < len(line):
            if modified_lines[row][col] == "@":
                col += 1
                continue
            row_tmp = row
            col_tmp = col
            crosses: int = 0
            while row_tmp < len(lines) and col_tmp < len(lines[0]):
                if modified_lines[row_tmp][col_tmp] == "@" and lines[row_tmp][col_tmp] != "L" and lines[row_tmp][col_tmp] != "7":
                    crosses += 1
                row_tmp += 1
                col_tmp += 1
            
            counter += crosses%2
            col += 1
        row +=1 
    
    print(counter)

    
    pass


if __name__ == "__main__":
    main()

# 525