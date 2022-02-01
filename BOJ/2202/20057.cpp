#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

int N, x, y;
int board[499][499] = {0};
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};
int fronts[9] = {-1, -1, 0, 0, 0, 0, 1, 1, 2};
int rights[9] = {1, -1, 2, 1, -1, -2, 1, -1, 0};
int ratio[9] = {1, 1, 2, 7, 7, 2, 10, 10, 5};
int ans = 0;

// move tornado in direction d.
void tornado(int d) {
    x = x + dx[d];
    y = y + dy[d];
    int current = board[x][y];
    board[x][y] = 0;
    int front = d;
    int right = (d + 3) % 4;
    int used = 0;
    int nx, ny, amount;
    for (int foo = 0; foo < 9; foo++) {
        nx = x + fronts[foo] * dx[front] + rights[foo] * dx[right];
        ny = y + fronts[foo] * dy[front] + rights[foo] * dy[right];
        amount = current * ratio[foo] / 100;
        used += amount;
        if (0 <= nx & nx < N & 0 <= ny & ny < N) {
            board[nx][ny] += amount;
        } else {
            ans += amount;
        }
    }
    // at alpha ratio
    nx = x + dx[front];
    ny = y + dy[front];
    amount = current - used;
    if (0 <= nx & nx < N & 0 <= ny & ny < N) {
        board[nx][ny] += amount;
    } else {
        ans += amount;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // get input
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }
    x = N / 2, y = N / 2;
    int d = -1;
    while (!(x == 0 && y == 0)) {
        if ((x + y == N - 1) | (x > N / 2 && x == y) | (x <= N / 2 && x - y == 1)) {
            d = (d + 1) % 4;
        }
        tornado(d);
    }
    cout << ans;
    return 0;
}
