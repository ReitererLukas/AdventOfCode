from functools import reduce


def main():
    f = open("input2.txt")
    lines: list[str] = f.readlines()
    f.close()

    time: int = int(reduce(lambda x1,x2: f"{x1}{x2}",filter(lambda x: x!="",lines[0].split(":")[1].split(" "))))
    distance: int = int(reduce(lambda x1,x2: f"{x1}{x2}",filter(lambda x: x!="",lines[1].split(":")[1].split(" "))))
    
    start = 0
    end = time
    current_index = 0
    steps = 100
    for i in range(0, time,steps):
        dist = (time-i)*i
        if dist > distance:
            current_index = i
            break

    for i in range(current_index-steps, current_index+1):
        dist = (time-i)*i
        if dist > distance:
            start = i
            break
    
    for i in range(current_index, time,steps):
        dist = (time-i)*i
        if dist <= distance:
            current_index = i
            break
    
    
    for i in range(current_index-steps, current_index+1):
        dist = (time-i)*i
        if dist <= distance:
            end = i
            break

    print(end - start)

if __name__ == "__main__":
    main()
    pass


# 39594072