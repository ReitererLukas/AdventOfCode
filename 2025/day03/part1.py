banks: list[str] = []

with open("input.txt", "r") as file:
  banks = file.readlines()


sum = 0
for bank in banks:
  first = int(bank[0])
  second = int(bank[1])

  i = 1
  while i < len(bank[:-1]):
    v = int(bank[i])
    if v > first and i + 1 < len(bank[:-1]):
      first = v
      second = int(bank[i+1])
    elif v > second:
      second = v
    i += 1
  
  num = first * 10 + second
  print(num) 
  sum += num

print(sum)