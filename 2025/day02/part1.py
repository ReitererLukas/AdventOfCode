import sys

ranges: list[tuple[int, int]] = []

with open("test.txt", "r") as file:
  line = file.readlines()[0]
  for r in line.split(","):
    ranges.append((int(r.split("-")[0]),int(r.split("-")[1])))

sum = 0
for r in ranges:
  for curr in range(r[0],r[1]+1):
    id = str(curr)
    if len(id) %2 != 0:
      continue

    if id[0:len(id)//2] == id[len(id)//2:]:
      sum += curr
    
print(sum)