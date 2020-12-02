def get_elements_that_sum_to_target(array, target):
    for i in range(len(array)):
        for j in range(i + 1, (len(array))):
            num1 = int(array[i])
            num2 = int(array[j])
            if num1 + num2 == target:
                print(f"{num1} + {num2} = {num1 + num2}") 
                print(f"{num1} * {num2} = {num1 * num2}") 

def main():
    with open('input.txt') as reader:
        numberList = reader.read().splitlines()
        get_elements_that_sum_to_target(numberList, 2020)

if __name__ == "__main__":
    main()