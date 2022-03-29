from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    N = int(stdin.readline().strip())
    matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]
    trace = sum(matrix[i][i] for i in range(N))
    row_count = 0
    for row in range(N):
        used = [False for _ in range(N)]
        for col in range(N):
            curr = matrix[row][col]
            if used[curr - 1]:
                row_count += 1
                break
            else:
                used[curr - 1] = True

    col_count = 0
    for col in range(N):
        used = [False for _ in range(N)]
        for row in range(N):
            curr = matrix[row][col]
            if used[curr - 1]:
                col_count += 1
                break
            else:
                used[curr - 1] = True
    print(f'Case #{t+1}: {trace} {row_count} {col_count}')
