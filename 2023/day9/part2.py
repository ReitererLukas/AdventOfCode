

def all_zero(differences: list[int]) -> bool:
    for num in differences:
        if num != 0:
            return False
    return True

def extrapolate(numbers: list[int]) -> int:
    difference: list[int] = []

    index: int = 1
    while index < len(numbers):
        difference.append(numbers[index]-numbers[index-1])
        index += 1

    if all_zero(difference):
        return 0
    return difference[0] - extrapolate(difference)
    pass

def main():
    f = open("input2.txt", "r")
    lines: list[str] = f.readlines()
    f.close()

    res: int = 0
    for line in lines:
        numbers: list[int] = list(map(lambda x: int(x), line[:-1].split(" ")))
        res += numbers[0] - extrapolate(numbers)
    print(res)
    pass


if __name__ == "__main__":
    main()
    pass

# 884