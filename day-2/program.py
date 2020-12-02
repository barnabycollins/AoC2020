import re

data = open("./input.txt", "r")

total1 = 0
total2 = 0

for line in data:
    match = re.match(r"(\d*)-(\d*) (.): (.*)$", line)
    (low, high, char, password) = match.groups()

    low = int(low)
    high = int(high)

    charCount = password.count(char)

    if (low <= charCount and charCount <= high):
        total1 += 1
    
    correctInIndices = 0

    for i in (low, high):
        if (password[i-1] == char):
            correctInIndices += 1
    
    if (correctInIndices == 1):
        total2 += 1

print(f"Total count of valid passwords by scheme 1: {total1}\nTotal count of valud passwords by scheme 2: {total2}")