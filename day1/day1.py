def get_input():
    with open("day1/input.txt") as data:
        input_file = [i for i in data.read().split("\n")]
    return input_file


def dayOne():
    current_number = 0
    current_largest = 0

    for i in get_input():
        if i == "":
            current_number = 0
        else:
            num = int(i)
            current_number += num
        if current_number > current_largest:
            current_largest = current_number

    print(current_largest)


def dayOneB():
    current_number = 0
    current_largest = 0
    second_largest = 0
    third_largest = 0

    for i in get_input():
        if i == "":
            current_number = 0
        else:
            num = int(i)
            current_number += num

        if current_number > current_largest:
            current_largest = current_number

        elif second_largest < current_number:
            second_largest = current_number

        elif third_largest < current_number:
            third_largest = current_number

    result = current_largest + second_largest + third_largest
    print(result)
