from sys import stdin, stdout

T = int(stdin.readline().strip())
my_strategy = [1]
for i in range(29):
    my_strategy.append(my_strategy[-1] * 2)
remain = [i for i in range(4242, 4242 + 2 * 70, 2)]

for t in range(T):
    stdin.readline()
    # N = int(stdin.readline().strip())
    N = 100

    print(*my_strategy, *remain)
    stdout.flush()

    B = list(map(int, stdin.readline().split()))
    merged = sorted(remain + B)
    merged.sort()
    total = sum(merged) + sum(my_strategy)

    first = []
    first_sum = 0
    second = []
    second_sum = 0

    for num in reversed(merged):
        if first_sum < second_sum:
            first.append(num)
            first_sum += num
        else:
            second.append(num)
            second_sum += num

    if first_sum > second_sum:
        first, second = second, first
        first_sum, second_sum = second_sum, first_sum

    diff = total // 2 - first_sum
    foo = bin(diff)[2:][::-1]
    for i in range(len(foo)):
        if foo[i] == '1':
            num = 1 << i
            first.append(num)
            first_sum += num
            diff -= num
    print(*first)
    stdout.flush()

    # print(sum(first))
    # print(total // 2)
