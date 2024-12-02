def check(tokens: list[int]) -> bool:
  if len(tokens) == 0:
    return False
  

  last_value = tokens[0]
  increasing: bool = tokens[0] < tokens [1]
  for token in tokens[1:]:
    if increasing and (token <= last_value or token - 3 > last_value):
      return False
    if not increasing and (token >= last_value or token + 3 < last_value):
      return False
    
    last_value = token
    
  return True

def main():
  safe_counter: int = 0

  with open("input1.txt", "r") as file:
    for line in file.readlines():
      if line == "":
        continue
      
      tokens: list[int] = list(map(lambda x: int(x), line[:-1].split(" ")))
      
      if check(tokens) or check(tokens[1:]):
        safe_counter += 1
      else:
        for i in range(1,len(tokens)):
          t = [*tokens[:i], *tokens[i+1:]]
          if check(t):
            safe_counter += 1
            break
        pass
      pass

  print(safe_counter)


if __name__ == "__main__":
  main()
  pass