

def get_input():
    with open("day3/input2.txt") as data:
        res = list(map(str.strip, data.read().splitlines()))
    return res


def day_three():
    input_file = get_input()

    matches_array = []

    score = 0

    if (check_if_even(input_file)):
        print("Every line in input file is not even and can't be processed")
        return
    for i in input_file:

        first_half = []
        second_half = []

        first_half, second_half = split_string(i)

        score += letter_to_number(check_for_match(first_half, second_half))

    return score

def day_three_part2():

    input_file = get_input()

    score = 0

    if (check_if_even(input_file)):
        print("Every line in input file is not even and can't be processed")
        return

    
    for i in range (0, len(input_file)-1, 3):
        
        first_array = input_file[i]
        second_array = input_file[i+1]
        third_array = input_file[i+2]

        matches = check_for_match_in_three(first_array, second_array)

        score += letter_to_number(check_for_match(matches, third_array))

    return score

        


def check_if_even(data):
    index = 0
    for i in data:
        index += 1
        if len(i) % 2 != 0:
            return True
    
    return False



def split_string(line):
    length = len(line)
    first_half = []
    second_half = []
    index = 0

    for i in line:
        if index < length / 2:
            first_half.append(i)
        else: 
            second_half.append(i)
        index += 1
    
    return first_half, second_half


def check_for_match_in_three(first_array, second_array):

    matches = []

    for i in first_array:
        for j in second_array:
            if i == j:
                matches.append(i)
    return matches



def check_for_match(first_array, second_array):
    for i in first_array:
        for j in second_array:
            if i == j:
                return i
    print ("No match found")

def letter_to_number(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 1

    for i in alphabet:
        if letter == i:
            return counter
        counter += 1
    