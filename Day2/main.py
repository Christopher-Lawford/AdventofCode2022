def calculateScoreForShapeSelected(letter) -> int:
    thisdict = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    return thisdict.get(letter)

def calculateOutcomeOfTheRound(theirHand, myHand) -> int:
    thisdict = {
        "AX": 3,
        "BX": 0,
        "CX": 6,
        "AY": 6,
        "BY": 3,
        "CY": 0,
        "AZ": 0,
        "BZ": 6,
        "CZ": 3
    }
    return thisdict.get(theirHand + myHand)

def calculatePointsFromMyHandAndResult(theirHand, desiredOutcome) -> int:
    thisdict = {  # lose,draw,win
        "AX": 3+0,
        "BX": 1+0,
        "CX": 2+0,
        "AY": 1+3,
        "BY": 2+3,
        "CY": 3+3,
        "AZ": 2+6,
        "BZ": 3+6,
        "CZ": 1+6
    }
    return thisdict.get(theirHand + desiredOutcome)

def readData(Example = False) -> str:
    FilePath = 'example.txt' if Example else 'test.txt' 
    with open(FilePath) as f:
      lines = f.readlines()
    return lines

if __name__ == "__main__":
    data = readData(False)
    roundScores = [sum((calculateScoreForShapeSelected(line[2]), calculateOutcomeOfTheRound(line[0], line[2]))) for line in data]
    print(f"Part1 answer: {sum(roundScores)}")
    part2RoundScores = [calculatePointsFromMyHandAndResult(line[0], line[2]) for line in data]
    print(f"Part2 answer: {sum(part2RoundScores)}")