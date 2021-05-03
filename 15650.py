# https://www.acmicpc.net/problem/15650
def foo(n, m):
    if m == 1:
        return [[i] for i in range(1, n + 1)]
    if n == m:
        return [[i for i in range(1, n + 1)]]
    else:
        part_one = (foo(n - 1, m))
        part_two = (foo(n - 1, m - 1))
        for i in part_two:
            i.append(n)
        return part_one + part_two


n, m = map(int, input().split())
temp = foo(n, m)
temp.sort()

for i in temp:
    for j in i:
        print(j, end=' ')
    print()
