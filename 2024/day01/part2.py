
def main():
  l1: list[int] = []
  l2: dict[int, int] = {}

  with open("input1.txt", "r") as file:
    for line in file.readlines():
      if line == "":
        continue
      
      tokens = line[:-1].split("   ")
      l1.append(int(tokens[0]))
      value: int = int(tokens[1])
      l2[value] = l2.get(value,0) + 1
    pass

  diff: int = 0
  for i in range(len(l1)):
    diff += l1[i] * l2.get(l1[i], 0)

  print(diff)
  pass


if __name__ == "__main__":
  main()
  pass