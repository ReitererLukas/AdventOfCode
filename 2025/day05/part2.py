ranges: list[list[int, int]] = []

ids: list[int] = []

with open("input.txt", "r") as file:
  inRanges = True
  for line in file.readlines():
    if line == "\n":
      inRanges = False
      continue

    if inRanges:
      ranges.append([int(line[:-1].split("-")[0]), int(line[:-1].split("-")[1])])
    else:
      ids.append(int(line[:-1]))

count: int = 0

def clean_ranges(ranges: list[list[int,int]]):
  cleaned_ranges: list[tuple[int, int]] = []
  changed = False

  for r in ranges:
    range = r
    second = [-1,-1]

    for pr in cleaned_ranges:

      # duplicated
      if pr[0] <= range[0] and pr[1] >= range[1]:
        range = [-1,-1]
        changed = True

      # untere hälfte ist neu
      elif pr[0] <= range[1] and pr[0] >= range[0] and pr[1] > range[1]:
        range[1] = pr[0] - 1
        changed = True

      # obere hälfte ist neu
      elif pr[1] <= range[1] and pr[1] >= range[0] and pr[0] < range[0]:
        range[0] = pr[1] + 1
        changed = True

      # middle => split
      elif pr[1] <= range[1] and pr[1] >= range[0] and pr[0] <= range[1] and pr[0] >= range[0]:
        second[1] = range[1]
        second[0] = pr[1] + 1
        range[1] = pr[0] - 1
        changed = True
      

    if range != [-1,-1] and range[0] <= range[1]:
      cleaned_ranges.append(range)


    if second != [-1,-1] and second[0] <= second[1]:
      cleaned_ranges.append(second)

  return changed, cleaned_ranges

changed = True
while changed:
  changed, ranges = clean_ranges(ranges)


ranges = sorted(ranges, key=lambda x: x[0])

for r in ranges:
  count += r[1] - r[0] + 1

print(count)
i = 0

# check if there are any overlaps
while i < len(ranges) -1:
  if ranges[i][1] >= ranges[i+1][0]:
    print(i, ranges[i], ranges[i+1])
  i += 1