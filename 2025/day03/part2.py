banks: list[str] = []

with open("input.txt", "r") as file:
  banks = file.readlines()

NUMBER_OF_ELEMENTS = 12

sum = 0
for bi, bank in enumerate(banks):
  if(len(bank) == 0):
    continue

  batteries: list[tuple[int]] = list(map(lambda x: (x[0],int(x[1])), enumerate(bank[:NUMBER_OF_ELEMENTS])))
  bank = bank[:-1]

  i = 1
  while i < len(bank):
    v = int(bank[i])

    j = 0
    exit = False
    while j < len(batteries) and not exit:
      if v > batteries[j][1] and i > batteries[j][0]  and i + (NUMBER_OF_ELEMENTS-j-1) < len(bank) and i > j:
        batteries[j] = (i, v)
        exit = True

        for x in range(12-j-1):
          batteries[j+x+1] = (i+x+1, int(bank[i+x+1]))
      j += 1
    i += 1
  
  num = 0
  solution = [987654321111, 811111111119, 434234234278, 888911112111, 0]
  for i, n in enumerate(batteries):
    num += n[1] * 10**(NUMBER_OF_ELEMENTS-i-1) 
 
  sum += num

print(sum)