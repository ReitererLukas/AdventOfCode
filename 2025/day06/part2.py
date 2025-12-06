
lines: list[str]
with open("input.txt", "r") as file:
  lines = file.readlines()

operators: list[str] = []

for op in lines[-1].split(" "):
    if op == "" or op == " " or op == "\n":
      continue

    operators.append(op)

# print(operators)
index = len(operators) - 1
pos = len(lines[0][:-1]) - 1

numbers: list[int] = []
sum = 0
while pos >= 0:

  num = 0
  all_blank = True
  for r in range(len(lines[:-1])):
    if lines[r][pos] == ' ':
      continue
    all_blank = False

    num = num * 10 +  int(lines[r][pos])

  if not all_blank:
    numbers.append(num)  

  if (all_blank and len(numbers) != 0) or pos == 0:
    op = operators[index]
    index -= 1
    res = 0
    if op == "*":
      res = 1
      for n in numbers:
        res *= n
    if op == "+":
      for n in numbers:
        res += n
    numbers.clear()
    sum += res

  pos -= 1

print(sum)
