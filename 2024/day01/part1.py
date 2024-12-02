
def main():
  l1: list[int] = []
  l2: list[int] = []

  with open("input1.txt", "r") as file:
    for line in file.readlines():
      if line == "":
        continue
      
      tokens = line[:-1].split("   ")
      l1.append(int(tokens[0]))
      l2.append(int(tokens[1]))
    pass
  l1.sort()
  l2.sort()

  diff: int = 0
  for i in range(len(l1)):
    diff += abs(l1[i] - l2[i])

  print(diff)
  pass


if __name__ == "__main__":
  main()
  pass