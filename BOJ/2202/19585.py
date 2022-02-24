# https://www.acmicpc.net/problem/19585
# Trie
from sys import stdin

c, n = map(int, stdin.readline().split())
container = ['']
nxt = [[]]
end = [False]


def add(word):
    pos = i = 0
    while i < len(word):
        for next_pos in nxt[pos]:
            # if next letter matches: move to that node
            if container[next_pos] == word[i]:
                pos = next_pos
                i += 1
                break
        # if nothing matches: insert new node
        else:
            nxt[pos].append(len(container))
            nxt.append([])
            end.append(False)
            pos = len(container)
            container.append(word[i])
            i += 1
    end[pos] = True


# search in trie and yield index whenever available
def find(word):
    pos = i = 0
    while i < len(word) - 1:
        for next_pos in nxt[pos]:
            # if next letter matches: move to that node
            if container[next_pos] == word[i]:
                pos = next_pos
                i += 1
                if end[pos]:
                    yield i
                break
        # if nothing matches: end of iteration
        else:
            return


for _ in range(c):
    color = stdin.readline().strip()
    add(color)

names = {stdin.readline().strip() for _ in range(n)}
for _ in range(int(stdin.readline().strip())):
    query = stdin.readline().strip()
    for i in find(query):
        # print(query[i:])
        if query[i:] in names:
            print('Yes')
            break
    else:
        print('No')

# for foo in enumerate(zip(container, nxt, end)):
#     print(foo)
