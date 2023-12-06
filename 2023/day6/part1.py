

def main():
    f = open("input1.txt")
    lines: list[str] = f.readlines()
    f.close()

    times: list[int] = list(map(lambda x: int(x), filter(lambda x: x!="",lines[0].split(":")[1].split(" "))))
    distances: list[int] = list(map(lambda x: int(x), filter(lambda x: x!="",lines[1].split(":")[1].split(" "))))

    race: int = 0
    solution: int = 1
    while race < len(times):
        counter: int = 0
        print("-----------------")
        print(f"time: {times[race]}, distance: {distances[race]}")
        for i in range(0, times[race]):
            dist = (times[race]-i)*i
            if dist > distances[race]:
                print(i)
                counter += 1
            
        if counter > 0:
            print(f"Counter: {counter}")
            solution *= counter
        else:
            print("NULLLLL!!!")
        pass
        race +=1

    print(solution)

if __name__ == "__main__":
    main()
    pass

# 128700