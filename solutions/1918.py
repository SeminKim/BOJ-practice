# https://www.acmicpc.net/problem/1918
# 괄호의 깊이와 연산의 종류를 고려하여 연산자의 순서를 먼저 구하고, 순서에 따라 차례로 변환

prob = input().strip()

ops = ['+', '-', '*', '/']


def to_postorder(seq: str):
    pure = list(seq.replace('(', '').replace(')', ''))  # 괄호 제거
    operations = []
    bra = 0  # 괄호 깊이
    idx = 0
    for s in seq:
        if s == '(':
            bra += 1
        elif s == ')':
            bra -= 1
        elif s in ops:
            operations.append([-bra * 1000, idx, s])  # priority (small is first), index, chr
            idx += 1
        else:
            idx += 1

    cnt = 1
    for op in operations:
        if op[2] in ['+', '-']:
            op[0] += cnt
        if op[2] in ['*', '/']:
            op[0] -= (500 - cnt)
        cnt += 1

    operations.sort()

    for now in operations:
        idx = now[1]
        head = ''
        tail = ''
        i = 1
        j = 1
        while True:
            if pure[idx - i] is not None:
                head = pure[idx - i]
                break
            i += 1
        while True:
            if pure[idx + j] is not None:
                tail = pure[idx + j]
                break
            j += 1
        foo = head + tail + now[2]
        for num in range(idx - i, idx + j + 1):
            pure[num] = None
        pure[idx] = foo
    for wow in pure:
        if wow is not None:
            return wow


print(to_postorder(prob))

# (A+(B*C)-(D/E))*F*(G+H)
# ABC*+DE/-F*GH+*
