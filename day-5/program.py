import re

data = open("./input.txt", "r")

ids = []

for line in data:
    line = line[:-1]

    coords = re.fullmatch(r"([FB]{7})([LR]{3})", line).groups()

    translator = str.maketrans('FBLR', '0101')

    coords = list(map(lambda x: int(x.translate(translator), 2), coords))
    
    seatID = coords[0]*8 + coords[1]

    ids.append(seatID)


ids = sorted(ids)

# There's definitely a better way to find the index of the current item but I don't know it
possibleSeats = [i+1 for i in ids[:-1] if ids[ids.index(i)+1] == i+2]

print(f"Part 1: {ids[-1]}\nPart 2: {possibleSeats[0]}")