

class Transform:
    def __init__(self, dest, source, length):
        self.source = source
        self.dest = dest
        self.length = length

    def in_range(self, source) -> bool:
        return source >= self.source and source < self.source+self.length
    
    def transform(self, source) -> int:
        return self.dest + (source - self.source)


def process_transform(lines: list[str], line_counter: int, sources: list[int]) -> tuple[int, list[int]]:
    transformers: list[Transform] = []
    while line_counter < len(lines) and lines[line_counter] != "\n":
        elements: list[int] = list(map(lambda x: int(x), lines[line_counter].split(" ")))
        transformers.append(Transform(elements[0], elements[1], elements[2]))
        line_counter += 1
        pass

    index: int = 0
    while index < len(sources):
        source = sources[index]
        for transformer in transformers:
            if transformer.in_range(source):
                sources[index] = transformer.transform(source)
                break
        index += 1

    return (line_counter, sources)



def main():
    f = open("input1.txt")
    lines: list[str] = f.readlines()
    f.close()

    source: list[int] = list(map(lambda x: int(x), lines[0].split(": ")[1].split(" ")))

    line_counter: int = 3
    line_counter, source = process_transform(lines, line_counter, source)
    line_counter, source = process_transform(lines, line_counter+2, source)
    line_counter, source = process_transform(lines, line_counter+2, source)
    line_counter, source = process_transform(lines, line_counter+2, source)
    line_counter, source = process_transform(lines, line_counter+2, source)
    line_counter, source = process_transform(lines, line_counter+2, source)
    line_counter, source = process_transform(lines, line_counter+2, source)
    

    source.sort()
    print(source[0])

if __name__ == "__main__":
    main()

# 278755257