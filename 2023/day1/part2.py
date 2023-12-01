file = open("input2.txt", "r")



num: int = 0
for line in file.readlines():
    first: int = None
    last: int = None

    index: int = 0
    while index < len(line):
        char = line[index]

        if not char.isdigit() and index + 3 < len(line):
            match line[index: index+3]:
                case "one":
                    char = '1'
                case "two":
                    char = '2'
                case "six":
                    char = '6'
        if not char.isdigit() and index + 4 < len(line):
            match line[index: index+4]:
                case "four":
                    char = '4'
                case "five":
                    char = '5'
                case "nine":
                    char = '9'
        if not char.isdigit() and index + 5 < len(line):
            match line[index: index+5]:
                case "three":
                    char = '3'
                case "seven":
                    char = '7'
                case "eight":
                    char = '8'

        if char.isdigit():
            toInt = int(char)
            if toInt in range(0,10):
                if first == None:
                    first = toInt
                else:
                    last = toInt
        index += 1
    num += first *10
    if last == None:
       num += first
    else:
        num += last

print(num)

#one 3
#two 3
#three 5
#four 4
#five 4 
#six 3
#seven 5
#eight 5
#nine 4