coords: list[tuple[int]] = []
with open("input.txt", "r") as file:
  coords = list(map(lambda x: (int(x.split(",")[0]),int(x.split(",")[1][:-1])), file.readlines()))

max = 0
for c1 in coords:
  for c2 in coords:
    if c1 != c2:
      area = (abs(c1[0]-c2[0]) + 1) * (abs(c1[1]-c2[1]) + 1)
      if area > max:
        max = area

print(max)