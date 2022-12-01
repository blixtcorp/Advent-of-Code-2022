def get_input():
    with open("day1/input.txt") as data:
        input_file = [i for i in data.read().split("\n")]
    return input_file


def day_one():
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

    print("part1 answer:", current_largest)


def day_one_part2():
    current_number = 0
    largest_number = 0
    second_largest = 0
    third_largest = 0

    for i in get_input():
        if i == "":
            current_number = 0
        else:
            num = int(i)
            current_number += num

        if current_number > largest_number:
            third_largest = second_largest
            second_largest = largest_number
            largest_number = current_number

        elif second_largest < current_number:
            third_largest = second_largest
            second_largest = current_number

        elif third_largest < current_number:
            third_largest = current_number

    result = largest_number + second_largest + third_largest

    print("part2 answer:", result)
