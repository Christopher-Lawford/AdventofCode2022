import re
from operator import attrgetter
import heapq


class elf():
    def __init__(self, number, calorieCounts) -> None:
        self.elfNumber = number
        self.calorieCounts = calorieCounts
        self.totalCalorieCounts = sum([int(x) for x in split_on_newline_character(calorieCounts)])

def split_on_newline_character(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){1,}"

    return re.split(blank_line_regex, s.strip())

def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

def readData(Example = False) -> str:
    FilePath = 'example.txt' if Example else 'test.txt' 
    with open(FilePath) as f:
      lines = f.read()
    return lines

def createElfs(stringsForElfs):
    elfs = []
    elfNumber = 0
    for elfData in stringsForElfs:
        elfs.append( elf(elfNumber, elfData))
        elfNumber += 1
    return elfs

if __name__ == "__main__":
    data = readData(False)
    print(f"data:{data}")
    datasplit = split_on_empty_lines(data)
    print(f"datasplit:{datasplit}")
    elfs = createElfs(datasplit)
    matching_obj = max(elfs, key=attrgetter('totalCalorieCounts'))
    print(f"Part 1 solution: {matching_obj.totalCalorieCounts}")
    top3elfs = heapq.nlargest(3, elfs, key=attrgetter('totalCalorieCounts'))
    print(f"top3elfs total: {sum([x.totalCalorieCounts for x in top3elfs])}")