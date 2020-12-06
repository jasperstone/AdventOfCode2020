from math import floor, ceil

def halflist(rowsOrSeats, directions):
    if len(directions) == 0:
        return rowsOrSeats[0]
    
    direction = directions.pop(0)
    if direction == 'F' or direction == 'L':
        return halflist(rowsOrSeats[:floor(len(rowsOrSeats)/2)], directions)
    if direction == 'B' or direction == 'R':
        return halflist(rowsOrSeats[ceil(len(rowsOrSeats)/2):], directions)

def main():
    maxid = 0
    with open('input.txt') as reader:
        data = reader.read().splitlines()
        for d in data:
            row = halflist(list(range(128)), list(d[:7]))
            col = halflist(list(range(8)), list(d[7:]))
            id = row * 8 + col
            if id > maxid:
                maxid = id

        print(f"MaxId: {maxid}")

if __name__ == "__main__":
    main()