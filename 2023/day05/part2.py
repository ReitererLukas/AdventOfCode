from timeit import default_timer as timer
from functools import reduce

class Transformer:
    def __init__(self, dest, source, length):
        self.source = source
        self.dest = dest
        self.length = length

    def in_range_reverse(self, source) -> bool:
        return source >= self.dest and source < self.dest+self.length
    
    def transform_reverse(self, source) -> int:
        return self.source + (source - self.dest)


def transform_backwards(source: int, transformer_map: dict[int, list[Transformer]], step: int = 0) -> tuple[int, list[int]]:
    transformers = transformer_map[6-step]
    for transformer in transformers:
        if transformer.in_range_reverse(source):
            source = transformer.transform_reverse(source)
            break

    if step == 6:
        return source
    res = transform_backwards(source, transformer_map, step + 1)
    return res


def read_transformer(lines: list[str], line_counter: int) -> tuple[int, list[Transformer]]:
    transformers: list[Transformer] = []
    while line_counter < len(lines) and lines[line_counter] != "\n":
            elements: list[int] = list(map(lambda x: int(x), lines[line_counter].split(" ")))
            transformers.append(Transformer(elements[0], elements[1], elements[2]))
            line_counter += 1
            pass
    
    return (line_counter, transformers)

    pass


def main():
    f = open("input2.txt")
    lines: list[str] = f.readlines()
    f.close()

    transformers_map: dict[int, list[Transformer]] = {}

    line_counter: int = 3
    line_counter, transformers = read_transformer(lines, line_counter)
    transformers_map[0] = transformers
    
    line_counter, transformers = read_transformer(lines, line_counter+2)
    transformers_map[1] = transformers
    line_counter, transformers = read_transformer(lines, line_counter+2)
    transformers_map[2] = transformers
    line_counter, transformers = read_transformer(lines, line_counter+2)
    transformers_map[3] = transformers
    line_counter, transformers = read_transformer(lines, line_counter+2)
    transformers_map[4] = transformers
    line_counter, transformers = read_transformer(lines, line_counter+2)
    transformers_map[5] = transformers
    line_counter, transformers = read_transformer(lines, line_counter+2)
    transformers_map[6] = transformers

    # backpack: dict[int, dict[int, int]] = {0: {},1: {},2: {},3: {},4: {},5: {},6: {}}

    seeds: list[int] = list(map(lambda x: int(x), lines[0].split(": ")[1].split(" ")))
    # ranges: list[tuple[int, int ]] = []
    index: int = 0
    ranges: list[tuple[int, int ]] = []
    while index < len(seeds):
        ranges.append(range(seeds[index],seeds[index] + seeds[index+1]))
        index += 2

    lowest: int = transformers_map[6][0].dest
    for transformer in transformers_map[6]:
        if transformer.dest < lowest:
            lowest = transformer.dest
    # lowest = 26829166
    lowest += 1
    while True:
        res = transform_backwards(lowest, transformers_map)
        for r in ranges:
            if res in r:
                print(lowest)
                print(r)
                print(res)
                return
        lowest += 1

if __name__ == "__main__":
    main()