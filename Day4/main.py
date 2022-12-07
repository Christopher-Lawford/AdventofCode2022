import collections

def readData(Example = False) -> list[str]:
    FilePath = 'example.txt' if Example else 'test.txt' 
    with open(FilePath) as f:
      lines = [line.rstrip() for line in f]
    return lines

if __name__ == "__main__":
    data = readData(False)
    part1 = 0
    part2 = 0
    for line in data:
        firstElf, secondElf = line.split(',')
        firstElfStart, firstElfEnd = [int(n) for n in firstElf.split('-')]
        secondElfStart, secondElfEnd = [int(n) for n in secondElf.split('-')]
        if ((firstElfStart >= secondElfStart) & (firstElfEnd <= secondElfEnd)) |( (firstElfStart <= secondElfStart )&( firstElfEnd >= secondElfEnd)):
            #print(f"first:{firstElfStart}, {firstElfEnd} second: {secondElfStart}, {secondElfEnd}")
            part1 += 1
        if ((firstElfStart >= secondElfStart) & (firstElfStart <= secondElfEnd))|(
            (firstElfEnd >= secondElfStart )&( firstElfEnd <= secondElfEnd))|(
            (secondElfStart >= firstElfStart) & (secondElfStart <= firstElfEnd))|(
            (secondElfEnd >= firstElfStart )&( secondElfEnd <= firstElfEnd)):
            print(f"first:{firstElfStart}, {firstElfEnd} second: {secondElfStart}, {secondElfEnd}")
            part2 += 1
    print(f"part one answer: {part1}")
    print(f"part two answer: {part2}")

