
lines: list[str]
with open("input.txt", "r") as file:
  lines = file.readlines()

numbers: list[list[int]] = []

for line in enumerate(lines[:-1]):
  index: int = 0
  for num in line[1].split(" "):
    if num == "" or num == " " or num == "\n":
      continue
    if line[0] == 0:
      numbers.append([])
    
    numbers[index].append(int(num))
    index += 1

# print(numbers)

operators: list[str] = []

for op in lines[-1].split(" "):
    if op == "" or op == " " or op == "\n":
      continue

    operators.append(op)

# print(operators)

assert len(numbers) == len(operators)

sum = 0
for calc in enumerate(numbers):
  op = operators[calc[0]]

  res = 0
  if op == "*":
    res = 1
    for n in calc[1]:
      res *= n
  if op == "+":
    for n in calc[1]:
      res += n

  sum += res
print(sum)
