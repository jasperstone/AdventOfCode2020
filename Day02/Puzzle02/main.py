import re
from collections import Counter

def valid_password(pos1, pos2, needle, password):
    result = (password[pos1 - 1] == needle) ^ (password[pos2 - 1] == needle) # ^ = XOR
    print(f"{pos1} {pos2} {needle} {password} => {result}")
    return result


def main():
    validCount = 0
    invalidCount = 0
    with open('input.txt') as reader:
        passwordList = reader.read().splitlines()
        for entry in passwordList:
            result = re.match(r'(\d+)-(\d+) (\w): (\w+)', entry)
            pos1 = int(result.group(1))
            pos2 = int(result.group(2))
            needle = result.group(3)
            password = result.group(4)
            if valid_password(pos1, pos2, needle, password.strip()):
                validCount += 1
            else:
                invalidCount += 1
    print(f"Valid: {validCount} Invalid: {invalidCount}")

if __name__ == "__main__":
    main()