import re

letters = ['M','A','S']

def check(direction: tuple[int, int], origin: tuple[int, int], field: list[str], level: int = 1) -> str:
  if level >= len(letters):
    return f"{origin[0] + direction[0]},{origin[1] + direction[1]}"
  elif origin[0] + direction[0] * level < 0 or origin[1] + direction[1] * level < 0 or origin[0] + direction[0] * level >= len(field) or origin[1] + direction[1] * level >= len(field[0]):
    return ""
  elif letters[level] == field[origin[0] + direction[0] * level][origin[1] + direction[1] * level]:
    return check(direction, origin, field, level + 1)
  return ""
  pass

def add_to_dict(dictionary: dict[str, int], result: str):
  dictionary[result] = dictionary.get(result, 0) + 1

def main():
  line: list[str] = ""
  with open("input1.txt", "r") as file:
    lines = file.readlines()

  
  results: dict[str, int] = {}
  for row_index, line in enumerate(lines):
    for col_index, letter in enumerate(line):
      if letter != letters[0]:
        continue
      add_to_dict(results, check((1,1), (row_index, col_index), lines))
      add_to_dict(results, check((-1,-1), (row_index, col_index), lines))
      add_to_dict(results, check((-1,1), (row_index, col_index), lines))
      add_to_dict(results, check((1,-1), (row_index, col_index), lines))
      pass
    pass

  counter: int = 0
  for key in results.keys():
    if key == "":
      continue

    if results.get(key, 0) > 1:
      counter += 1

  print(counter)


if __name__ == "__main__":
  main()
  pass