def is_tree(character):
    if character == "#":
        return True
    return False

def main():
    treeCount = 0
    with open('input.txt') as reader:
        slope = reader.read().splitlines()
        col = 0
        for rownum in range(len(slope)):
            if rownum % 2 == 1:
                continue
            row = slope[rownum]
            if is_tree(row[col % len(row)]):
                treeCount += 1
            col += 1
    print(f"TreeCount = {treeCount}")

if __name__ == "__main__":
    main()

# Number of trees with the following slopes
# Right 1, down 1 = 63
# Right 3, down 1 = 254
# Right 5, down 1 = 62
# Right 7, down 1 = 56
# Right 1, down 2 = 30
# Multiplied all together = 1,666,768,320