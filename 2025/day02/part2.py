import sys

ranges: list[tuple[int, int]] = []

with open("input.txt", "r") as file:
  line = file.readlines()[0]
  for r in line.split(","):
    ranges.append((int(r.split("-")[0]),int(r.split("-")[1])))


def check(id: str, l: int) -> bool:
  for i in range(l, len(id), l):
    if id[i-l:i] != id[i:i+l]:
      return False
  return True


sum = 0
for r in ranges:
  for curr in range(r[0],r[1]+1):
    id = str(curr)
    
    if len(id) > 5 and len(id) % 5 == 0:
      if check(id, 5):
        sum += curr
        continue
    if len(id) > 4 and len(id) % 4 == 0:
      if check(id, 4):
        sum += curr
        continue
    if len(id) > 3 and len(id) % 3 == 0:
      if check(id, 3):
        sum += curr
        continue
    if len(id) > 2 and len(id) % 2 == 0:
      if check(id, 2):
        sum += curr
        continue
    if len(id) > 1:
      if check(id, 1):
        sum += curr
        continue
      
    
print(sum)