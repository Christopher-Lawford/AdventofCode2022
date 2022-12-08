import collections
import re
def readData(Example = False) -> list[str]:
    FilePath = 'example.txt' if Example else 'test.txt' 
    with open(FilePath) as f:
      data = f.readlines() 
    return data

def tallestColumn(data) -> int:
    lineNumber = 0
    for line in data:
        x = re.search("\d",line)
        if x == None:
            lineNumber += 1
            continue
        else:
            return lineNumber
    return lineNumber

if __name__ == "__main__":
    data = readData(False)
    part1 = 0
    part2 = 0
    maxheight = tallestColumn(data)
    print(f"maxheight: {maxheight}")
    banana = {}
    for x in range(1,len(data[maxheight]),4):
        banana[int(data[maxheight][x])] = [data[y][x] for y in range(maxheight)[::-1] if data[y][x] != ' ']
    print(f"banana {banana}")
    instructions = data[maxheight+2:]
    for x in instructions:
        searchResults = [int(y) for y in re.findall("\d+",x)]
        banana[searchResults[2]] = banana[searchResults[2]] + banana[searchResults[1]][-searchResults[0]:][::-1]
        banana[searchResults[1]] = banana[searchResults[1]][:-searchResults[0]]
    print(f"part one: {''.join([x[-1] for x in banana.values()])}")
    banana = {}
    for x in range(1,len(data[maxheight]),4):
        banana[int(data[maxheight][x])] = [data[y][x] for y in range(maxheight)[::-1] if data[y][x] != ' ']
    print(f"banana {banana}")
    instructions = data[maxheight+2:]
    for x in instructions:
        searchResults = [int(y) for y in re.findall("\d+",x)]
        banana[searchResults[2]] = banana[searchResults[2]] + banana[searchResults[1]][-searchResults[0]:]
        banana[searchResults[1]] = banana[searchResults[1]][:-searchResults[0]]
    print(f"part two: {''.join([x[-1] for x in banana.values()])}")