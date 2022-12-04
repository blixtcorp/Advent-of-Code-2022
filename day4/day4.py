def get_input():
    with open("day4/input.txt") as data:
        res = list(map(str.strip, data.read().splitlines()))
    return res


def day_four():
    data = get_input()
    counter = 0

    # print(data)
    d = []
    for i in data:
        d.append(i.split(","))

    # print(d)

    for i in range(0, len(d)):
        first, second = string_parser(d.pop())
        two, one, four, three = parse_numbers(first, second)

        if three <= one and four >= two:
            counter += 1
        elif three >= one and four <= two:
            counter += 1

    return counter


def string_parser(numbers):
    return numbers[0].split("-"), numbers[1].split("-")


def parse_numbers(first, second):
    two = int(first.pop())
    one = int(first.pop())
    four = int(second.pop())
    three = int(second.pop())

    return two, one, four, three


def day_four_part_two():
    data = get_input()
    counter = 0

    d = []
    for i in data:
        d.append(i.split(","))

    for i in range(0, len(d)):
        first, second = string_parser(d.pop())
        two, one, four, three = parse_numbers(first, second)

        if three <= one <= four:
            counter += 1
        elif three <= two <= four:
            counter += 1
        elif one <= three <= two:
            counter += 1
        elif one <= four <= two:
            counter += 1

    return counter


