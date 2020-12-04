import re, json

def isValidPassport(jsonText):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport = json.loads(jsonText)
    for r in required:
        if r not in passport:
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