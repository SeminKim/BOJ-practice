# https://www.acmicpc.net/problem/5670
# Trie

from sys import stdin

while True:
    try:
        n = int(stdin.readline())
    except:
        break

    words = [stdin.readline().strip() for _ in range(n)]
    # initialize trie
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


    # search in trie and return ans for a word.
    def find(word):
        ret = 1
        pos = i = 0
        while i < len(word):
            if i != 0 and (len(nxt[pos]) > 1 or end[pos]):
                ret += 1
            for next_pos in nxt[pos]:
                # if next letter matches: move to that node
                if container[next_pos] == word[i]:
                    pos = next_pos
                    i += 1
                    break
        return ret


    for foo in words:
        add(foo)
    # for foo in words:
    #     print(find(foo))
    print(f'{round(sum(find(foo) for foo in words) / len(words), 2) :.2f}')
