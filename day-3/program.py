from functools import reduce

data = open("./input.txt", "r")

totals = [0, 0, 0, 0, 0]

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

positions = [0, 0, 0, 0, 0]

lineCount = 0

for line in data:
    line = line[:-1]

    for i in range(len(slopes)):
        slope = slopes[i]
        
        if (lineCount % slope[1] == 0):
            totals[i] += line[positions[i]] == '#'
            positions[i] = (positions[i] + slope[0])%len(line)

    lineCount += 1

print(f"Total trees: {totals}\nProduct of totals: {reduce(lambda x, y: x*y, totals)}")
