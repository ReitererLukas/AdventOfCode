
f = open("input1.txt", "r")

map: dict[str, int] = {"red": 12, "green": 13, "blue": 14}

id_sum: int = 0
for line in f.readlines():
    tokens = line.split(": ")

    id: int = int(tokens[0].split(" ")[1])

    rounds = tokens[1].split(";")

    valid = True
    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            single_cube = cube.split(" ")
            if len(single_cube) == 3:
                single_cube = single_cube[1:]
            if single_cube[1].endswith("\n"):
                single_cube[1] = single_cube[1][0:-1]
            if map.get(single_cube[1]) < int(single_cube[0]):
                valid = False

    if valid:
        id_sum += id
    pass

print(id_sum)