def dayOne():

    with open("day1/input.txt") as data:
        input_file = [i for i in data.read().split("\n")]

    current_number = 0
    current_largest = 0

    for i in input_file:
        if i == "":
            current_number = 0
        else:
            num = int(i)
            current_number += num
        if current_number > current_largest:
            current_largest = current_number

    print(current_largest)
