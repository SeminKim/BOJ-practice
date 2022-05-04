# Not solved yet...


from sys import stdin

T = int(stdin.readline().strip())
for t in range(T):
    E, W = map(int, stdin.readline().split())
    exercise = [list(map(int, stdin.readline().split())) for _ in range(E)]


    def dfs(pos, stack, acc, acc_weight):
        # print(pos, stack, acc, acc_weight)
        if pos == E:
            return acc + len(stack)

        if exercise[pos] == acc_weight:
            ret = dfs(pos + 1, stack, acc, acc_weight)
            temp = []
            for i in range(len(stack)):
                popped = stack.pop(-1)
                temp.append(popped)
                acc_weight[popped] -= 1
                acc += 1
                ret = min(ret, dfs(pos + 1, stack, acc, acc_weight))
            for weight in reversed(temp):
                stack.append(weight)
                acc_weight[weight] += 1
            return ret

        ret = 10 ** 10
        for weight in range(W):
            if acc_weight[weight] < exercise[pos][weight]:
                stack.append(weight)
                acc += 1
                acc_weight[weight] += 1
                ret = min(ret, dfs(pos, stack, acc, acc_weight))
                stack.pop(-1)
                acc -= 1
                acc_weight[weight] -= 1

        return ret


    ans = dfs(0, [], 0, [0 for _ in range(W)])
    print(f'Case #{t + 1}: {ans}')
