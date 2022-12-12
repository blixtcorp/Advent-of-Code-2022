import re

def get_input():
    with open("input.txt") as data:
        res = list(map(str.strip, data.read().splitlines()))
    return res


def day_five():
    data = get_input()
    piles = [[], [], [], [], [], [], [], [], []]

    res = []
    for d in range(0, 8):
        res.append(data[d].replace("[", "").replace("]", ""))

    print(res)

    for i in range(0, 8):
        for j in range(0, 9):
            if res[i][j] != ' ' and len(res[i]) > j:
                piles[j].insert(0, res[i][j])

    for pile in piles:
        print(pile)

    counter = 0

    for line in data[10:]:
        n, f, t = list(map(int, re.split('move | from | to ', line)[1:]))
        counter += 1
        print(counter)

        for i in range(0, n-1):
            piles[t-1].append(piles[f-1].pop())

    print(piles)

day_five()


