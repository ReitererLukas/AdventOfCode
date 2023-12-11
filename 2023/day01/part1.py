file = open("input1.txt", "r")

num: int = 0
for line in file.readlines():
    first: int = None
    last: int = None

    for char in line:
        if char.isdigit():
            toInt = int(char)
            if toInt in range(0,10):
                if first == None:
                    first = toInt
                else:
                    last = toInt
    num += first *10
    if last == None:
       num += first
    else:
        num += last

print(num)