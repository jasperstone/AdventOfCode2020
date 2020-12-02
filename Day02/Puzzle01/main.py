import re
from collections import Counter

def valid_password(min, max, needle, password):
    count = Counter(password)[needle]
    print(f"{min} {max} {needle} {password} => {count}")
    return min <= count and count <= max


def main():
    validCount = 0
    invalidCount = 0
    with open('input.txt') as reader:
        passwordList = reader.read().splitlines()
        for entry in passwordList:
            result = re.match(r'(\d+)-(\d+) (\w): (\w+)', entry)
            min = int(result.group(1))
            max = int(result.group(2))
            needle = result.group(3)
            password = result.group(4)
            if valid_password(min, max, needle, password.strip()):
                validCount += 1
            else:
                invalidCount += 1
    print(f"Valid: {validCount} Invalid: {invalidCount}")

if __name__ == "__main__":
    main()