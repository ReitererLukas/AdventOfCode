lines: list[list[str]] = []


with open("input.txt", "r") as file:
  lines = list(map(lambda x: list(x), file.readlines()[:-1]))

x = 0
y = 0
for i, c in enumerate(lines[0]):
  if c == "S":
    x = i
    break

stack: list[tuple[int]] = []
visited: list[tuple[int]] = []

while y < len(lines):
  if lines[y][x] == '^':
    stack.insert(0, (x,y))
    break
  y += 1


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
while len(stack) > 0:
  node = stack[0]
  stack.remove(stack[0])

  counter += 1

  children = find_children(node[0], node[1])
  for c in children:
    if c in visited:
      continue
    stack.insert(0, c)
    visited.append(c)

print(counter)  
    


