from collections import defaultdict
from itertools import accumulate

def readData(Example = False) -> list[str]:
    FilePath = 'example.txt' if Example else 'test.txt' 
    with open(FilePath) as f:
      lines = [line.rstrip() for line in f]
    return lines

dirs = defaultdict(int)
if __name__ == "__main__":
    data = readData(False)
    for line in data:
        match line.split():
            case '$', 'cd', '/': curr = ['']
            case '$', 'cd', '..': curr.pop()
            case '$', 'cd', x: curr.append(x+'/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for p in accumulate(curr):
                    dirs[p] += int(size)
print(f"part1:{sum(s for s in dirs.values() if s <= 100_000)}")
print(f"part2:{min(s for s in dirs.values() if s >= dirs[''] - 40_000_000)}")
