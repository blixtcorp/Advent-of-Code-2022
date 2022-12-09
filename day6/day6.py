import os

print(os.listdir())
def get_input():
    with open('day6/input.txt') as data:
        res = data.read()
    return res


def day_six():
    print("part 1:")
    print(investigate_window(4))
    print("part 2:")
    print(investigate_window(14))


def investigate_window(window_size):
    data = get_input()

    for i in range(0, len(data)-window_size):
        window = data[i:i+window_size]
        counts = [window.count(window[j]) for j in range(0, len(window))]
        if counts.count(1) == len(counts):
            return i+window_size

    return -1




