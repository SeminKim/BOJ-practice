#include <iostream>

using namespace std;

int N, M;
int tree[2048][2048];

void modify(int x, int y, int c) {
    tree[x][y] = c;
    int row = x / 2;
    int col = y / 2;
    while (row) {
        tree[row][y] = tree[row << 1][y] + tree[row << 1 | 1][y];
        row >>= 1;
    }
    while (col) {
        tree[x][col] = tree[x][col << 1] + tree[x][col << 1 | 1];
        if (col < N) {
            int tmp = x / 2;
            while (tmp) {
                tree[tmp][col] = tree[tmp << 1][col] + tree[tmp << 1 | 1][col];
                tmp >>= 1;
            }
        }
        col >>= 1;
    }
    return;
}

int query(int x1, int y1, int x2, int y2) {
    int ret = 0;
    while (x1 < x2) {
        if (x1 & 1) {
            ret += query(x1, y1, x1, y2);
            x1++;
        }
        if (!(x2 & 1)) {
            ret += query(x2, y1, x2, y2);
            x2--;
        }
        x1 >>= 1, x2 >>= 1;
    }
    if (x1 == x2) {
        while (y1 < y2) {
            if (y1 & 1) {
                ret += tree[x1][y1];
                y1++;
            }
            if (!(y2 & 1)) {
                ret += tree[x1][y2];
                y2--;
            }
            y1 >>= 1, y2 >>= 1;
        }
        if (y1 == y2) {
            ret += tree[x1][y1];
        }
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // get input
    cin >> N >> M;
    for (int i = N; i < 2 * N; i++) {
        for (int j = N; j < 2 * N; j++) {
            cin >> tree[i][j];
        }
    }
    // initialize tree
    for (int i = N; i < 2 * N; i++) {
        for (int j = N - 1; j >= 0; j--) {
            tree[i][j] = tree[i][j << 1] + tree[i][j << 1 | 1];
        }
    }
    for (int j = 0; j < 2 * N; j++) {
        for (int i = N - 1; i >= 0; i--) {
            tree[i][j] = tree[i << 1][j] + tree[i << 1 | 1][j];
        }
    }
    int w;
    for (int i = 0; i < M; i++) {
        cin >> w;
        if (w == 0) {
            int x, y, c;
            cin >> x >> y >> c;
            modify(x + N - 1, y + N - 1, c);

        } else {
            int x1, y1, x2, y2, ans;
            cin >> x1 >> y1 >> x2 >> y2;
            cout << query(x1 + N - 1, y1 + N - 1, x2 + N - 1, y2 + N - 1) << "\n";
        }
    }
    return 0;
}

