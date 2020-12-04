def is_tree(character):
    if character == "#":
        return True
    return False

def main():
    treeCount = 0
    with open('input.txt') as reader:
        slope = reader.read().splitlines()
        col = 0
        for row in slope:
            if is_tree(row[col % len(row)]):
                treeCount += 1
            col += 3
    print(f"TreeCount = {treeCount}")

if __name__ == "__main__":
    main()