import re

letters = ['X','M','A','S']

def check(direction: tuple[int, int], origin: tuple[int, int], field: list[str], level: int = 1) -> int:
  if level >= len(letters):
    return 1
  elif origin[0] + direction[0] * level < 0 or origin[1] + direction[1] * level < 0 or origin[0] + direction[0] * level >= len(field) or origin[1] + direction[1] * level >= len(field[0]):
    return 0
  elif letters[level] == field[origin[0] + direction[0] * level][origin[1] + direction[1] * level]:
    return check(direction, origin, field, level + 1)
  return 0
  pass

def main():
  line: list[str] = ""
  with open("input1.txt", "r") as file:
    lines = file.readlines()

  
  count: int = 0
  for row_index, line in enumerate(lines):
    for col_index, letter in enumerate(line):
      if letter != letters[0]:
        continue
      count += check((0,1), (row_index, col_index), lines)
      count += check((1,1), (row_index, col_index), lines)
      count += check((1,0), (row_index, col_index), lines)
      count += check((0,-1), (row_index, col_index), lines)
      count += check((-1,-1), (row_index, col_index), lines)
      count += check((-1,0), (row_index, col_index), lines)
      count += check((-1,1), (row_index, col_index), lines)
      count += check((1,-1), (row_index, col_index), lines)
      pass
    pass

  print(count)


if __name__ == "__main__":
  main()
  pass