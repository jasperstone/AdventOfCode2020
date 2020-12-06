from collections import Counter

def groupsum(grouplist):
    counter = Counter()
    for row in grouplist:
        counter.update(row)
    votesum = len(counter.keys())
    print(f"{counter}: {votesum}")
    return votesum

def main():
    sumtotal = 0
    with open('input.txt') as reader:
        data = reader.read().splitlines()
        tempArray = []
        for row in data:
            if row == '':
                sum = groupsum(tempArray)
                sumtotal += sum
                tempArray = []
                continue
            tempArray.append(row)
        sumtotal += groupsum(tempArray) # capture the last group

        print(f"SumTotal: {sumtotal}")

if __name__ == "__main__":
    main()