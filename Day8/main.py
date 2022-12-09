from collections import defaultdict
from itertools import accumulate
import plotly.express as px
def readData(Example = False) -> list[str]:
    FilePath = 'example.txt' if Example else 'test.txt' 
    with open(FilePath) as f:
      lines = [line.rstrip() for line in f]
    return lines

if __name__ == "__main__":
    data = readData(False)
    print(f"data{data}")
    data2 = [[int(x) for x in y] for y in data]
    width = len(data[0])
    height = len(data)
    python_indicesWest   = [[index for (index, item) in enumerate(y) if index == 0 or item > max([x for x in y][:index])] for y in data]
    python_indicesNorth  = [[index for (index, item) in enumerate(y) if index == 0 or item > max([x for x in y][:index])] for y in [''.join([x[i] for x in data]) for i in range(len(data[0]))]]
    python_indicesEast   = [[index for (index, item) in enumerate(y[::-1]) if index == 0 or item > max([x for x in y[::-1]][:index])] for y in data]
    python_indicesSouth  = [[index for (index, item) in enumerate(y[::-1]) if index == 0 or item > max([x for x in y[::-1]][:index])] for y in [''.join([x[i] for x in data]) for i in range(len(data[0]))]]
    python_indiciesset = set([(j,i) for i in range(len(python_indicesWest)) for j in python_indicesWest[i]])
    python_indiciesset2 = set([(i,j) for i in range(len(python_indicesNorth)) for j in python_indicesNorth[i]])
    
    python_indiciesset3 = set([(width-j-1,i) for i in range(len(python_indicesEast)) for j in python_indicesEast[i]])
    python_indiciesset4 = set([(i,height-j-1) for i in range(len(python_indicesSouth)) for j in python_indicesSouth[i]])
    print(f"python_indiciesset:{python_indiciesset}")
    print(f"python_indiciesset2:{python_indiciesset2}")
    print(f"python_indiciesset3:{python_indiciesset3}")
    print(f"python_indiciesset4:{python_indiciesset4}")
    output = python_indiciesset | python_indiciesset2 | python_indiciesset3 | python_indiciesset4
    print(f"part1:{len(output)}")
    
    print(f"part2:")
    fig = px.imshow([[int(x) for x in y] for y in data], template='ggplot2')
    fig.show()

    s = 0

    def view_length(tree, view):
        view_length = 0
        for v in view:
            view_length += 1
            if v >= tree:
                break
        return view_length

    for i in range(len(data2[0])):
        for j in range(len(data2)):
            tree = data2[i][j]

            s1 = view_length(tree, data2[i][0:j][::-1])
            s2 = view_length(tree, data2[i][j+1:])
            s3 = view_length(tree, list(zip(*data2))[j][0:i][::-1])
            s4 = view_length(tree, list(zip(*data2))[j][i+1:])
            score = s1 * s2 * s3 * s4
            if score > s:
                s = score

    print(s)
