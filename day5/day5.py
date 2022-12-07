def get_input():
    with open("day5/input2.txt") as data:
        res = [i for i in data.read().split("\n")]
    return res

def get_stacks():

    start = [
        [],
        ["N", "W", "B"],
        ["B", "M", "D", "T", "P", "S", "Z", "H", "Q"],
        ["R", "Z", "J", "V", "D", "W"],
        ["R", "Z", "J", "V", "D", "W"],
        ["B", "M", "H", "S"],
        ["B", "P", "V", "H", "J", "N", "G", "L"],
        ["S", "L", "D", "H", "H", "F", "Z", "Q", "J"],
        ["B", "Q", "G", "J", "F", "S", "W"],
        ["J", "D", "C", "S", "M", "W", "Z"],
    ]

    return start

def day_five():
    input_file = get_input()

    stack = get_stacks()

    for line in input_file:
        words = line.split()
        move_amount = int(words[1])
        from_stack = int(words[3])
        to_stack = int(words[5])