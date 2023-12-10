
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


def main():
    file = open("input1.txt", "r")
    lines: list[str] = file.readlines()
    file.close()

    row: int = 0
    column: int = 0
    for line in lines:
        if "S" in line:
            column = line.index("S")
            break
        row += 1

    coord: tuple[int, int, int] = find_first(lines, row, column)
    steps: int = 1
    while lines[coord[0]][coord[1]] != 'S':
        coord = get_next(lines, coord)
        steps += 1

    print(steps//2)
    pass

if __name__ == "__main__":
    main()

# 6690