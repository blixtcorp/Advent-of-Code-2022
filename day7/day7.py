def get_input():
    with open("day7/input.txt") as data:
        res = list(map(str.strip, data.read().splitlines()))
        data = []
        for i in res:
            data.append(i.split(" "))
    return data


# commands we executed begin with $

def day_seven():
    data = get_input()
    print(data)
    for i in data:
        if "$ cd" in i:
            current_dir = cd(i[2])



def cd(arg):
    return arg


def ls(index, data):
    res = []
    for i in range(index, len(data)):
        if "$" in data[i]:
            break
        res.append(data[i])

    return res
