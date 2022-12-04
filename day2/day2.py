
# reads input data as a list and removes whitespace
def get_input():
    with open("day2/input.txt") as data:
        res = list(map(str.strip, data.read().splitlines()))
    return res


# day_two() gets input file and returns answer to part 1
def day_two():
    data = get_input()
    return ruleset_handler(data, ruleset_one)

# day_two() gets input file and returns answer to part 2
def day_two_part2():
    data = get_input()
    return ruleset_handler(data, ruleset_two)


# loops through the data and finds the correct score in the right dictionary
def ruleset_handler(data, ruleset):
    score = 0
    for i in data:
        score += ruleset[i]

    return score


ruleset_one = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3
}

ruleset_two = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6
}
