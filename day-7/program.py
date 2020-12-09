import re

data = open("./input.txt", "r").read()

rulesRaw = re.findall(r"([a-z ]+) bags contain ((?:(?:(?:[0-9]{1} [a-z ]+|[a-z ]+) bag[s]?)(?:, |))+)\.\n", data)

rules = {}

for i in rulesRaw:
    rules[i[0]] = dict(map(lambda x: (x[1], x[0]), re.findall(r"(?:([0-9]{1}) |)([a-z ]+) bag[s]?(?:, |)", i[1])))

found = set()
oldFound = set()
sameCount = 0

def checkPossibleContents(foundSoFar):
    global found

    newFound = set()

    for i in rules.keys():
        possibleContents = rules[i].keys()
        for j in foundSoFar:
            if (j in possibleContents):
                newFound.add(i)
    
    found.update(newFound)

checkPossibleContents({"shiny gold"})

# I know this is a really dumb way of doing it but it works okay
while sameCount < 1000:
    checkPossibleContents(found)
    
    # no need to do a deep equal because the only changes we'll get will be additions
    #  (see I'm not that thick okay)
    if (len(oldFound) == len(found)):
        sameCount += 1
    
    else:
        sameCount = 0
    
    oldFound = found

print(f"Part 1: {len(found)}")