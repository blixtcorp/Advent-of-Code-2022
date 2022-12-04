#Get_input() reads and returns an input file which has been split on each \n
def get_input():
    with open("day1/input.txt") as data:
        input_file = [i for i in data.read().split("\n")]
    return input_file

#day_one() prints the answer to part 1 with the input files  defined in get_input()
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

    return current_largest


#day_one_part2() prints the answer to part 2 with the input files  defined in get_input()
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

    return result