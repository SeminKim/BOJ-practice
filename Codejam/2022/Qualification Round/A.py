from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    R, C = map(int, stdin.readline().split())

    first = ".." + "-".join("+" * (C))
    second = ".." + ".".join("|" * (C))
    odd = "-".join("+" * (C + 1))
    even = ".".join("|" * (C + 1))

    print(f'Case #{t + 1}:')
    print(first)
    print(second)
    for _ in range(R - 1):
        print(odd)
        print(even)
    print(odd)
