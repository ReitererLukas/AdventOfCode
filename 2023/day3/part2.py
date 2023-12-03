f = open("input2.txt")

def is_number(index: int, line:str) -> int: 
    while index < len(line):
        if line[index].isdigit():
            index += 1
        else:
            return index - 1
        pass
    return index - 1
    pass

def gear_neighbor(line_index: int, char_index, lines: list[str], map: dict[int, dict[int,list[int]]], number: int):
    if lines[line_index][char_index] == '*':
        if line_index not in list(map.keys()):
            map[line_index] = {}
            map[line_index][char_index] = []
        elif char_index not in list(map[line_index].keys()):
            map[line_index][char_index] = []
        
        map[line_index][char_index].append(number)

    return map
    

def is_adjacent(line_index: int, lines: list[str], char_start: int, char_end: int, map: dict[int, dict[int,list[int]]], number: int) -> dict[int, dict[int,list[int]]]:
    if char_start > 0:
        # left top
        if line_index > 0 :
            map = gear_neighbor(line_index - 1, char_start - 1, lines, map, number)
        # left
        map = gear_neighbor(line_index, char_start - 1, lines, map, number)
        # left bottom
        if line_index < len(lines) -1: 
            map = gear_neighbor(line_index + 1, char_start - 1, lines, map, number)
    while char_start <= char_end:
        if line_index > 0:
            map = gear_neighbor(line_index-1, char_start, lines, map, number)
        if line_index < len(lines) - 1:
            map = gear_neighbor(line_index+1, char_start, lines, map, number)

        char_start += 1
   
    if char_end < len(line) - 1:
        # right top
        if line_index > 0:
            map = gear_neighbor(line_index-1, char_end + 1, lines, map, number)
        # right
        map = gear_neighbor(line_index, char_end + 1, lines, map, number)
        # right bottom
        if line_index < len(lines) - 1:
            map = gear_neighbor(line_index + 1, char_end + 1, lines, map, number)
    return map
    pass

sum: int = 0
line_index: int = 0
lines = f.readlines()

map: dict[int, dict[int,list[int]]] = {}

index = 0
while index < len(lines):
    lines[index] = lines[index][0:-1]
    index += 1

while line_index < len(lines):
    line = lines[line_index]
    char_index : int= 0
    while char_index < len(line):
        char = line[char_index]
        end_index: int = is_number(char_index, line)
        if end_index < char_index:
            char_index += 1
            continue
        number = int(line[char_index:end_index+1])
        map = is_adjacent(line_index, lines, char_index, end_index, map, number)
        char_index = end_index + 1
        pass
    line_index += 1

for line in list(map.keys()):
    for row in list(map[line].keys()):
        if len(map[line][row]) == 2:
            sum += map[line][row][0] * map[line][row][1]
print(sum)
# 78826761