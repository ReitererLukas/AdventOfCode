
coords: list[list[tuple[int]]] = [[],[]]
with open("input.txt", "r") as file:
  lines = []
  cont = 0
  all_lines = file.readlines()
  for i, line in enumerate(all_lines): 
    if line == "\n":
      cont = i +1
      break
    lines.append(line)

  coords[0] = list(map(lambda x: (int(x.split(",")[0]),int(x.split(",")[1][:-1])), lines))


  lines = []
  for line in all_lines[cont:]:
    lines.append(line)
  
  coords[1] = list(map(lambda x: (int(x.split(",")[0]),int(x.split(",")[1][:-1])), lines))

max = 0



c = 0
largest_y = coords[c][0][1] - 1
max = 0
for c1 in coords[c]:
  x = c1[0]

  y_diffs = []
  res = ()

  x_diff = -1
  if largest_y <= c1[1]:
    largest_y = c1[1]

    i = len(coords[c]) -2
    while i > 0 and x_diff == -1:
      if coords[c][i][0] == coords[c][i+1][0] and coords[c][i][1] >= c1[1] and coords[c][i + 1][1] <= c1[1]:
        res = (coords[c][i], coords[c][i+1])
        x_diff = abs(coords[c][i][0] - c1[0])
        y_diffs = [abs(coords[c][i][1] - c1[1]), abs(coords[c][i+1][1] - c1[1])]
      i -= 1
  else:
    i = 1
    while i < len(coords[c]) - 2 and x_diff == -1:
      if coords[c][i][0] == coords[c][i-1][0] and coords[c][i][1] >= c1[1] and coords[c][i - 1][1] <= c1[1]:
        res = (coords[c][i], coords[c][i-1])
        y_diffs = [abs(coords[c][i][1] - c1[1]), abs(coords[c][i-1][1] - c1[1])]
        x_diff = abs(coords[c][i][0]- c1[0])
      i += 1

  for y_diff in y_diffs:
    if x_diff != -1 and x_diff * y_diff > max:
      print(c1, res, y_diff, x_diff, x_diff * y_diff)
      max = x_diff * y_diff

print("==========0")

c = 1
smallest_y = coords[c][0][1] + 1
for c1 in coords[c]:
  x = c1[0]
  y_diffs = []

  x_diff = -1
  if smallest_y >= c1[1]:
    smallest_y = c1[1]

    i = len(coords[c]) -2
    while i > 0 and x_diff == -1:
      if coords[c][i][0] == coords[c][i+1][0] and coords[c][i][1] >= c1[1] and coords[c][i + 1][1] <= c1[1]:
        x_diff = abs(coords[c][i][0] - c1[0])
        res = (coords[c][i], coords[c][i+1])
        y_diffs = [abs(coords[c][i][1] - c1[1]), abs(coords[c][i+1][1] - c1[1])]
      i -= 1
  else  :
    i = 1
    while i < len(coords[c]) - 2 and x_diff == -1:
      if coords[c][i][0] == coords[c][i-1][0] and coords[c][i][1] >= c1[1] and coords[c][i - 1][1] <= c1[1]:
        x_diff = abs(coords[c][i][0]- c1[0])
        res = (coords[c][i], coords[c][i-1])
        y_diffs = [abs(coords[c][i][1] - c1[1]), abs(coords[c][i-1][1] - c1[1])]
      i += 1


  for y_diff in y_diffs:
    if x_diff != -1 and x_diff * y_diff > max:

      print(c1, res, y_diff, x_diff, x_diff * y_diff)
      max = x_diff * y_diff

  
      

print(max)

# 2318036343
# 1280505420
# -> solution
# 111023803
