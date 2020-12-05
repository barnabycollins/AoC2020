import re, functools

data = open("./input.txt", "r")

part = 1

last = ""

required = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]


validCount = 0

def convertYear(year):
    try:
        return int(year)
    
    except:
        return 0

# I hate this function
def validate(field):
    (name, content) = field

    if (bool(re.fullmatch(r".yr", name))):
        content = convertYear(content)

    if (name == 'byr'):
        return 1920 <= content and content <= 2002
    
    elif (name == 'iyr'):
        return 2010 <= content and content <= 2020
    
    elif (name == 'eyr'):
        return 2020 <= content and content <= 2030
    
    elif (name == 'hgt'):
        result = re.fullmatch(r"([0-9]*)([a-z]*)", content).groups()
        
        if (result == None):
            return False
        
        (size, unit) = result

        size = int(size)

        if (unit == 'cm'):
            return 150 <= size and size <= 193
        
        elif (unit == 'in'):
            return 59 <= size and size <= 76
    
    elif (name == 'hcl'):
        return bool(re.fullmatch(r"#[a-f0-9]{6}", content))
    
    elif (name == 'ecl'):
        return content in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    elif (name == 'pid'):
        return bool(re.fullmatch(r"[0-9]{9}", content))
    
    return False



for line in data:
    line = " " + line[:-1]

    if (line == " "):

        valid = True

        if (part == 1):
            for i in required:
                if (i not in last):
                    valid = False
                    break
        
        else:
            valid = [False] * len(required)

            for i in re.findall(r" ([a-z]{3}):([a-z0-9#]*)", last):
                if (i[0] in required):
                    valid[required.index(i[0])] = validate(i)
        
            valid = functools.reduce(lambda a,b: a and b, valid)
        
        validCount += int(valid)

        last = ""

    else:
        last += line

print(f"Valid passports: {validCount}")
