import collections

def readData(Example = False) -> str:
    FilePath = 'example.txt' if Example else 'test.txt' 
    with open(FilePath) as f:
      lines = [line.rstrip() for line in f]
    return lines


def charactersThatAreRepeatedMoreThanOnce(data) -> list[str]:
    results = collections.Counter(data)
    ans = []
    for k in results:
        if results[k] > 1:
            ans.append(k)
    return ans
    


if __name__ == "__main__":
    data = readData(False)
    values = []
    for line in data:
        firstPart, secondPart = set(line[:len(line)//2]), set(line[len(line)//2:])
        repeatedCharacters = firstPart & secondPart
        valuesForLetters =[ord(letter)-65+27 if letter.isupper() else ord(letter)-96 for letter in repeatedCharacters]
        values.extend(valuesForLetters)
    print(f"part 1 result: {sum(values)}")
    values = []
    for line in range(int(len(data)/3)):
        repeatedCharacters = set(data[line*3]) & set(data[line*3+1]) & set(data[line*3+2])
        valuesForLetters =[ord(letter)-65+27 if letter.isupper() else ord(letter)-96 for letter in repeatedCharacters]
        values.extend(valuesForLetters)
    print(f"part 2 result: {sum(values)}")
