from math import floor, ceil

plane = [[ 0 for x in range(8)] for y in range(128)]

def printplane():
    for rownum in range(len(plane)):
        print(f"Row {rownum:03}: {plane[rownum]}")

def halflist(rowsOrSeats, directions):
    if len(directions) == 0:
        return rowsOrSeats[0]
    
    direction = directions.pop(0)
    if direction == 'F' or direction == 'L':
        return halflist(rowsOrSeats[:floor(len(rowsOrSeats)/2)], directions)
    if direction == 'B' or direction == 'R':
        return halflist(rowsOrSeats[ceil(len(rowsOrSeats)/2):], directions)

def main():
    with open('input.txt') as reader:
        data = reader.read().splitlines()
        for d in data:
            row = halflist(list(range(128)), list(d[:7]))
            col = halflist(list(range(8)), list(d[7:]))
            plane[row][col] = 'X'
            #id = row * 8 + col
            
        printplane()

if __name__ == "__main__":
    main()