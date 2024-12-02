
def main():
  safe_counter: int = 0

  with open("input1.txt", "r") as file:
    for line in file.readlines():
      if line == "":
        continue
      
      tokens: list[int] = list(map(lambda x: int(x), line[:-1].split(" ")))
      last_value = tokens[0]
      increasing: bool = tokens[0] < tokens [1]
      use_break = False
      for token in tokens[1:]:
        if increasing and (token <= last_value or token - 3 > last_value):
          use_break = True
          break
        if not increasing and (token >= last_value or token + 3 < last_value):
          use_break = True
          break

        last_value = token
      
      if not use_break:
        safe_counter += 1
      pass

  print(safe_counter)


if __name__ == "__main__":
  main()
  pass