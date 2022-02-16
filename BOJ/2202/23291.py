# https://www.acmicpc.net/problem/23291

from sys import stdin

n, k = map(int, stdin.readline().split())
fishbowl = [list(map(int, stdin.readline().split()))]  # save at zeroth floor


# move fish and linearize to zeroth floor
def move_and_linearize(fishbowl):
    delta = []
    # horizontal
    for floor in range(len(fishbowl)):
        temp = [0 for _ in range(len(fishbowl[floor]))]
        for i in range(len(fishbowl[floor]) - 1):
            diff = int((fishbowl[floor][i + 1] - fishbowl[floor][i]) / 5)
            temp[i] += diff
            temp[i + 1] -= diff
        delta.append(temp)
    # vertical
    for pos in range(len(fishbowl[1])):
        for floor in range(len(fishbowl) - 1):
            diff = int((fishbowl[floor + 1][pos] - fishbowl[floor][pos]) / 5)
            delta[floor][pos] += diff
            delta[floor + 1][pos] -= diff
    # apply
    for floor in range(len(fishbowl)):
        for i in range(len(fishbowl[floor])):
            fishbowl[floor][i] += delta[floor][i]

    new_bowl = []
    for wow in zip(*fishbowl):
        new_bowl.extend(wow)
    new_bowl.extend(fishbowl[0][len(fishbowl[1]):])
    return [new_bowl]


for t in range(100000):
    # end condition
    minimum = min(fishbowl[0])
    maximum = max(fishbowl[0])
    if maximum - minimum <= k:
        print(t)
        break

    # add fish
    for i in range(n):
        if fishbowl[0][i] == minimum:
            fishbowl[0][i] += 1

    # stacking
    first = fishbowl[0].pop(0)
    fishbowl.append([first])
    while True:
        if len(fishbowl) <= len(fishbowl[0]) - len(fishbowl[1]):
            new_bowl = [list(wow) for wow in zip(*fishbowl)]
            new_bowl.reverse()
            fishbowl = [fishbowl[0][len(fishbowl[1]):], *new_bowl]
        else:
            break

    fishbowl = move_and_linearize(fishbowl)

    # flip half and add to second floor.
    first = fishbowl[0][n // 2:]
    second = fishbowl[0][:n // 2][::-1]
    fishbowl = [first[n // 4:], second[n // 4:], second[:n // 4][::-1], first[:n // 4][::-1]]

    fishbowl = move_and_linearize(fishbowl)
