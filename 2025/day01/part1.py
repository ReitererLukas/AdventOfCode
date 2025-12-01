lines: list[str] = []

with open("input.txt", "r") as file:
  lines = file.readlines()


start = 50

pwd = 0
ctr = 0
for l in lines:
  l = l.strip()
  direction = l[0]
  if direction == "L":
    print("L",int(l[1:]))
    start -= int(l[1:])
    while start < 0:
      start += 100
  else:
    print("R",int(l[1:]))
    start += int(l[1:])
    while start > 99:
      start -= 100
  ctr += 1
  if start == 0:
    pwd += 1

print(pwd)
print(ctr)

