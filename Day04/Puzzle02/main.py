import re, json

def byr(value):
    year = int(value)
    return 1920 <= year and year <= 2002

def iyr(value):
    year = int(value)
    return 2010 <= year and year <= 2020

def eyr(value):
    year = int(value)
    return 2020 <= year and year <= 2030

def hgt(value):
    if 'cm' in value:
        height = int(value.strip('cm'))
        return 150 <= height and height <= 193
    if 'in' in value:
        height = int(value.strip('in'))
        return 59 <= height and height <= 76
    return False

def hcl(value):
    return re.match(r'#[0-9a-f]{6}', value)

def ecl(value):
    return re.match(r'(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)', value)

def pid(value):
    if len(value) != 9:
        return False
    return re.match(r'\d{9}', value)

functions = {'byr': byr, 'iyr': iyr, 'eyr': eyr, 'hgt': hgt, 'hcl': hcl, 'ecl': ecl, 'pid': pid}

def isValidPassport(jsonText):
    passport = json.loads(jsonText)
    for f in functions:
        if f not in passport:
            return False
        if not functions[f](passport[f]):
            return False
    return True

def main():
    validCount = 0
    with open('input.txt') as reader:
        data = reader.read()
        newdata = data.replace("\n\n", " <TOKEN> ")
        newdata = newdata.replace("\n", " ")
        newdata = re.sub(r'(\S+):(\S+)', r'"\1":"\2"', newdata)
        dataarray = newdata.split(" <TOKEN> ")
        for jsonText in dataarray:
            if isValidPassport('{' + jsonText.replace(' ', ',') + '}'):
                validCount += 1
    print(f'ValidCount = {validCount}')

if __name__ == "__main__":
    main()