import re, functools

data = open("./input.txt", "r").read()

match = re.findall(r"((?:[a-z]+\n)+)\n", data)


uniqueCounts = list(map(lambda x: len(set(x.replace('\n',''))), match))

print(f"Part 1: {sum(uniqueCounts)}")


commonCounts = []

for i in match:
    answers = [set(x) for x in i.split('\n')[:-1]]

    commonCounts.append(len(set.intersection(*answers)))

print(f"Part 2: {sum(commonCounts)}")