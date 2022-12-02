from enum import Enum


# get_input() splits input file at \n and replaces " " with ""
def get_input():
    with open("day2/input.txt") as data:
        input_file = [i for i in data.read().split("\n")]
        res = []
        for i in input_file:
            res.append(i.replace(" ", ""))
    return res


# day_two() gets input file and returns answer to part 1
def day_two():
    data = get_input()
    print("day 2 part 1:")
    return strategy_handler(data)

def day_two_part2():
    data = get_input()
    print("day 2 part 2:")
    return strategy_handler_part2(data)


# strategy_handler() takes the input file and runs a for loop for each element and calculates score depending on input
def strategy_handler(data):
    score = 0

    for i in data:

        your_move = i[1]
        enemy_move = i[0]

        if enemy_move == 'A':
            if your_move == 'X':
                score += score_calculator(move.ROCK, state.DRAW)
            elif your_move == 'Y':
                score += score_calculator(move.PAPER, state.WIN)
            elif your_move == 'Z':
                score += score_calculator(move.SCISSORS, state.LOSE)

        elif enemy_move == 'B':
            if your_move == 'X':
                score += score_calculator(move.ROCK, state.LOSE)
            elif your_move == 'Y':
                score += score_calculator(move.PAPER, state.DRAW)
            elif your_move == 'Z':
                score += score_calculator(move.SCISSORS, state.WIN)

        elif enemy_move == 'C':
            if your_move == 'X':
                score += score_calculator(move.ROCK, state.WIN)
            elif your_move == 'Y':
                score += score_calculator(move.PAPER, state.LOSE)
            elif your_move == 'Z':
                score += score_calculator(move.SCISSORS, state.DRAW)

    return score



# strategy_handler() takes the input file and runs a for loop for each element and calculates score depending on input
def strategy_handler_part2(data):
    score = 0

    for i in data:

        your_move = i[1]
        enemy_move = i[0]

        if enemy_move == 'A':
            if your_move == 'X':
                score += score_calculator(move.SCISSORS, state.LOSE)
            elif your_move == 'Y':
                score += score_calculator(move.ROCK, state.DRAW)
            elif your_move == 'Z':
                score += score_calculator(move.PAPER, state.WIN)

        elif enemy_move == 'B':
            if your_move == 'X':
                score += score_calculator(move.ROCK, state.LOSE)
            elif your_move == 'Y':
                score += score_calculator(move.PAPER, state.DRAW)
            elif your_move == 'Z':
                score += score_calculator(move.SCISSORS, state.WIN)

        elif enemy_move == 'C':
            if your_move == 'X':
                score += score_calculator(move.PAPER, state.LOSE)
            elif your_move == 'Y':
                score += score_calculator(move.SCISSORS, state.DRAW)
            elif your_move == 'Z':
                score += score_calculator(move.ROCK, state.WIN)

    return score



def score_calculator(your_move, result):
    return your_move.value + result.value


class state(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0


class move(Enum):
    SCISSORS = 3
    PAPER = 2
    ROCK = 1
