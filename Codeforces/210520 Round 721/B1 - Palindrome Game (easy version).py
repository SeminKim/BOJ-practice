from sys import stdin

t = int(stdin.readline().strip())
for _ in range(t):
    n = int(stdin.readline())
    seq = stdin.readline().strip().replace(' ', '')
    mid = len(seq) // 2
    if len(seq) % 2 == 0:
        print('BOB')
    elif seq[mid] == '1':
        print('BOB')
    elif '0' in seq[:mid]:
        print('ALICE')
    else:
        print('BOB')