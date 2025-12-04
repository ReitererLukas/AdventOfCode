
lines: list[list[str]] = []

with open("input.txt", "r") as file:
  lines = list(map(lambda x: list(x[:-1]), file.readlines()))

rows = len(lines)
columns = len(lines[0])

def count(mark: bool = False):
  counter = 0
  for r_i, row in enumerate(lines):
    for c_i, element in enumerate(row):

      if element != '@':
        continue
      number_of_ats = 0
      
      for i in range(r_i-1,r_i+2):
        for j in range(c_i-1, c_i+2):
          if not (i < 0 or i >= rows or j < 0 or j >= columns) and not (r_i == i and c_i == j)  and (lines[i][j] == '@' or lines[i][j] == 'x'):
            number_of_ats += 1

      if number_of_ats < 4:
        counter += 1
        lines[r_i][c_i] = 'x'

  return counter

def replace():
  for r_i, row in enumerate(lines):
    for c_i, element in enumerate(row):
      if element == 'x':
        lines[r_i][c_i] = '.'

total_count = 0

repeat: bool = True

while repeat:
  c = count()
  total_count += c
  replace()

  if c == 0:
    repeat = False

print(total_count)


           
