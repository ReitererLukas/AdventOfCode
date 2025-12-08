import math
from unionfind import unionfind

coords: list[tuple[int]] = []

with open("input.txt", "r") as file:
  coords = list(map(lambda x: (int(x.split(",")[0]),int(x.split(",")[1]),int(x.split(",")[2])), file.readlines()))


def calc_distance(c1, c2):
  return math.sqrt( (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2 )

distances: list[tuple[int]] = []
for i1, c1 in enumerate(coords):
  for i2, c2 in enumerate(coords):
    if i1 > i2:
      distances.append((calc_distance(c1,c2),(i1,i2)))


distances = sorted(distances, key=lambda x: x[0])

N = 1000
u = unionfind(len(coords))

addEdges = True

for index in range(N):
  edge = distances[index]

  if u.issame(edge[1][0],edge[1][1]):
    continue

  u.unite(edge[1][0],edge[1][1])
  pass

sizes: list[int] = sorted(list(map(lambda x: len(x), u.groups())), reverse=True)

print(sizes[0] * sizes[1] * sizes[2])
