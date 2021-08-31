from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    seq = list(map(int, stdin.readline().split()))
    ans = 0
    for i in range(0, n, 2):
        curr = seq[i]
        inter_sum = 0  # intermediate sum
        for j in range(i + 1, n):
            if j % 2 == 0:
                inter_sum += seq[j]
            else:
                inter_sum -= seq[j]

                if inter_sum <= 0 and j > i + 1:
                    ans += 1
                if inter_sum < 0:  # bracket closed more, thus some of seq[i] will used
                    if curr + inter_sum >= 0:
                        ans += -inter_sum
                        curr += inter_sum
                        inter_sum = 0
                    else:  # too much closed, terminate
                        ans += curr
                        break

    print(ans)


solve()
