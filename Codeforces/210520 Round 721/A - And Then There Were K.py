from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    n = int(stdin.readline().strip())
    n = len(bin(n)[2:]) - 1
    print(2 ** n - 1)
