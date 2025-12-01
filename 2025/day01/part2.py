lines: list[str] = []

with open("input.txt", "r") as file:
  lines = file.readlines()


start = 50

pwd = 0
ctr = 0
for l in lines:
  l = l.strip()
  if int(l[1:]) >= 100:
    pwd += int(l[1:]) // 100

  val = int(l[1:]) % 100
  
  direction = l[0]
  if direction == "L":
    if start == 0:
      pwd -= 1

    start -= val
    if start < 0:
      pwd += 1
      start += 100
    if start == 0:
      pwd  += 1
  else:
    start += val
    if start > 99:
      pwd += 1
      start -= 100


print(pwd)
print(ctr)

