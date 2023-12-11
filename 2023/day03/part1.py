f = open("input1.txt")

def is_number(index: int, line:str) -> int: 
    while index < len(line):
        if line[index].isdigit():
            index += 1
        else:
            return index - 1
        pass
    return index - 1
    pass

def number_neighbor(line_index: int, char_index, lines: list[str]):
    return not lines[line_index][char_index].isdigit() and lines[line_index][char_index] != '.'
    

def is_adjacent(line_index: int, lines: list[str], char_start: int, char_end: int) -> bool:
    if char_start > 0:
        # left top
        if line_index > 0 and number_neighbor(line_index - 1, char_start - 1, lines):
            return True
        # left
        if number_neighbor(line_index, char_start - 1, lines):
            return True
        # left bottom
        if line_index < len(lines) -1 and number_neighbor(line_index + 1, char_start - 1, lines):
            return True
    while char_start <= char_end:
        if line_index > 0 and number_neighbor(line_index-1, char_start, lines):
            return True
        if line_index < len(lines) - 1 and number_neighbor(line_index+1, char_start, lines):
            return True

        char_start += 1
   
    if char_end < len(line) - 1:
        # right top
        if line_index > 0 and number_neighbor(line_index-1, char_end + 1, lines):
            return True
        # right
        if number_neighbor(line_index, char_end + 1, lines):
            return True
        # right bottom
        if line_index < len(lines) - 1 and number_neighbor(line_index + 1, char_end + 1, lines):
            return True
    return False
    pass

sum: int = 0
line_index: int = 0
lines = f.readlines()

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
        if is_adjacent(line_index, lines, char_index, end_index):
            sum += number

        char_index = end_index + 1
        pass
    line_index += 1

print(sum)

# 533784