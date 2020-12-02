## Leira Salene 1785752

# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for x in range(len(numbers)):
        max = x
    for y in range(x + 1, len(numbers)):
        if numbers[max] < numbers[y]:
            max = y
    (numbers[x], numbers[max]) = (numbers[max], numbers[x])
    for z in range(len(numbers)):
        print(numbers[z], end = " ")
        print()

if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = []
    data = input()
    numbers = [int(z) for z in data.split()]
    selection_sort_descend_trace(numbers)