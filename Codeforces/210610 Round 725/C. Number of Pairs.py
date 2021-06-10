from sys import stdin

def binary_search(seq, start, end, target, findle=True):  #search idx for target or larger

    mid = (start+end) // 2
    if target <= seq[mid]:
        return binary_search(seq, start, mid, target)
    if target > seq[mid]:
        return binary_search(seq, mid, end, target)



def solve():
    n, l, r = map(int,input().split())
    seq = list(map(int, stdin.readline().split()))
    seq.sort()



    ans = 0
    for i in range(n-1):  # 0 to n-2 is sufficient
        left = l - seq[i]  # have to find idx such that seq[idx] <= left
        right = r - seq[i]
        p1 = (i + n) // 2
        stepsize = (n - i) //2
        while stepsize > 1:
            if left == seq[p1]:
                break
            if left < seq[p1]:
                p1 -= stepsize
                stepsize = stepsize //2
            else:
                p1 += stepsize
                stepsize = stepsize //2

        if left




        foo_r = binary_search(seq, i+1, n-1, right)-1
        foo_l = binary_search(seq, i+1, n-1, left)
        if foo_r != n and foo_l != -1:
            ans += foo_r - foo_l
    print(ans)

t = int(stdin.readline().strip())

for _ in range(t):
    solve()

