ranges: list[tuple[int, int]] = []

ids: list[int] = []

with open("input.txt", "r") as file:
  inRanges = True
  for line in file.readlines():
    if line == "\n":
      inRanges = False
      continue

    if inRanges:
      ranges.append((int(line[:-1].split("-")[0]), int(line[:-1].split("-")[1])))
    else:
      ids.append(int(line[:-1]))

count: int = 0

for id in ids:
  for r in ranges:
    if r[0] <= id and r[1] >= id:
      count += 1
      break

print(count)      