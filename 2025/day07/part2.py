lines: list[list[str]] = []


with open("input.txt", "r") as file:
  lines = list(map(lambda x: list(x), file.readlines()[:-1]))

cases: dict[tuple[int], int] = dict()

# add base cases
for x, e in enumerate(lines[-1]):
  if e == '^':
    cases[(x,len(lines)-1)] = 2 if x > 0 and x < len(lines[0]) - 1 else 1 


def find_children(xt,yt) -> list[tuple[int]]:
  children: list[tuple[int]] = []
  y_save = yt

  if xt > 0:
    while yt < len(lines):
      if lines[yt][xt-1] == '^':
        children.append((xt-1,yt))
        break
      yt += 1

  yt = y_save
  if xt < len(lines[0]) - 1:
    while yt < len(lines):
      if lines[yt][xt+1] == '^':
        children.append((xt+1,yt))
        break
      yt += 1
    

  return children
  pass

counter = 0

y = len(lines) - 3
while y >= 0:
  x = 0
  while x < len(lines[y])-1:
    if lines[y][x] == '^':
      children = find_children(x,y)
      ways = 0
      for c in children:
        ways += cases.get(c)
      if len(children) < 2:
        ways += (2-len(children))
      cases[(x,y)] = ways
    x += 1

  y -= 2



x = 0
y = 0
for i, c in enumerate(lines[0]):
  if c == "S":
    x = i
    break

while y < len(lines):
  if lines[y][x] == '^':
    break
  y += 1

print(cases[(x,y)])


