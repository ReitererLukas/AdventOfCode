
lines: list[list[str]] = []

with open("test.txt", "r") as file:
  lines = list(map(lambda x: list(x[:-1]), file.readlines()))

rows = len(lines)
columns = len(lines[0])

counter: int = 0
for r_i, row in enumerate(lines):
  for c_i, element in enumerate(row):

    if element != '@':
      continue
    number_of_ats = 0
    
    for i in range(r_i-1,r_i+2):
      for j in range(c_i-1, c_i+2):
        if not (i < 0 or i >= rows or j < 0 or j >= columns) and not (r_i == i and c_i == j)  and lines[i][j] == '@':
          number_of_ats += 1

    if number_of_ats < 4:
      counter += 1


print(counter)


           
