import re


def main():
  input: str = ""
  with open("input1.txt", "r") as file:
    input = file.read()

  results:list[str] = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", input)

  sum: int = 0
  print(results)
  for res in results:
    numbers:list[int] = list(map(lambda x: int(x), re.findall(r"[0-9]{1,3}", res)))
    sum += numbers[0] * numbers[1]

  print(sum)

if __name__ == "__main__":
  main()
  pass