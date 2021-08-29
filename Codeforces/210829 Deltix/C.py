from sys import stdin

### Not Solved Yet ###

def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))

    ans = 0
    group = 0
    counter = 0
    for i in range(n // 2):
        open = seq[2 * i]
        close = seq[2 * i + 1]
        if open == close:
            group += 1
            ans += open

        elif open > close:
            ans += group * (group - 1) // 2
            group = 1

    # for i in range(n):
    #     if i % 2 == 0:
    #         counter += seq[i]
    #
    #     else:
    #         if counter - seq[i] == 0:
    #             group += 1
    #             counter -= seq[i]
    #             ans += seq[i]
    #
    #         elif counter - seq[i] > 0:
    #             ans += group * (group - 1) // 2
    #             group = 1
    #             counter -= seq[i]
    #             ans += seq[i]
    #
    #         else:
    #             group += 1
    #             ans += group * (group - 1) // 2
    #             group = 0
    #             ans += counter
    #             counter = 0
    #
    #
    #
    # ans += group * (group - 1) // 2
    #
    # print(ans)


solve()

# 6
# 3 2 3 2 3 2
