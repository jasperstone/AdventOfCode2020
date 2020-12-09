import operator
ops = { "+": operator.add, "-": operator.sub }

def split_operation(operation):
    return operation[:3], operation[4], int(operation[5:])

def main():
    #ops = { "+": operator.add, "-": operator.sub } # etc.

    with open('input.txt') as reader:
        data = reader.read().splitlines()

        accumulator = 0
        visited = {}
        index = 0
        while True:
            if index in visited:
                break
            visited[index] = None

            instruction = data[index]
            operation, operator, value = split_operation(instruction)

            if operation == 'nop':
                index += 1
            if operation == 'acc':
                index += 1
                accumulator = ops[operator](accumulator, value)
            if operation == 'jmp':
                index = ops[operator](index, value)
            
        print(accumulator)
        
if __name__ == "__main__":
    main()