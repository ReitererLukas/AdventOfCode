
f = open("input2.txt", "r")


sum: int = 0
for line in f.readlines():
    tokens = line.split(": ")

    map: dict[str, int] = {"red": 0, "green": 0, "blue": 0}

    rounds = tokens[1].split(";")

    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            single_cube = cube.split(" ")
            if len(single_cube) == 3:
                single_cube = single_cube[1:]
            if single_cube[1].endswith("\n"):
                single_cube[1] = single_cube[1][0:-1]
            # print(single_cube)
            if map.get(single_cube[1]) < int(single_cube[0]):
                map[single_cube[1]] = int(single_cube[0])

    sum += map["red"] * map["green"] * map["blue"]
    pass

print(sum)