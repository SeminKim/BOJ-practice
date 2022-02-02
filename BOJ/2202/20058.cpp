#include <algorithm>
#include <iostream>

using namespace std;

int N, Q, board_size;
int board[64][64];
int temp[64][64];
bool visited[64][64] = {false};
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};
int sum = 0;

// rotate and check ice-melting condition.
void firestrom(int len) {
    for (int row = 0; row < board_size; row += len) {
        for (int col = 0; col < board_size; col += len) {
            // rotate for each subgrid, given its top-left point (row,col)
            for (int i = 0; i < len; i++) {
                for (int j = 0; j < len; j++) {
                    temp[row + j][col + len - 1 - i] = board[row + i][col + j];
                }
            }
        }
    }
    // check for ice-melting condition
    for (int i = 0; i < board_size; i++) {
        for (int j = 0; j < board_size; j++) {
            int ice_count = 0;
            for (int d = 0; d < 4; d++) {
                int ni = i + dx[d];
                int nj = j + dy[d];
                if (0 <= ni && ni < board_size && 0 <= nj && nj < board_size && temp[ni][nj] > 0) {
                    ice_count++;
                }
            }
            if (ice_count >= 3) {
                board[i][j] = temp[i][j];
            } else {
                board[i][j] = max(0, temp[i][j] - 1);
            }
        }
    }
}

// return the number of connected ices adjacent to (row, col)
int dfs(int row, int col) {
    int ret = 0;
    for (int d = 0; d < 4; d++) {
        int nrow = row + dx[d];
        int ncol = col + dy[d];
        if (0 <= nrow && nrow < board_size && 0 <= ncol && ncol < board_size && !visited[nrow][ncol] && board[nrow][ncol] > 0) {
            visited[nrow][ncol] = true;
            ret += 1 + dfs(nrow, ncol);
        }
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // get input
    cin >> N >> Q;
    board_size = 1 << N;
    for (int i = 0; i < board_size; i++) {
        for (int j = 0; j < board_size; j++) {
            cin >> board[i][j];
        }
    }
    // do firestorm
    int L;
    for (int i = 0; i < Q; i++) {
        cin >> L;
        firestrom(1 << L);
    }
    for (int i = 0; i < board_size; i++) {
        for (int j = 0; j < board_size; j++) {
            sum += board[i][j];
        }
    }
    // find maximum mTE
    int maximum = 0;
    for (int i = 0; i < board_size; i++) {
        for (int j = 0; j < board_size; j++) {
            if (!visited[i][j] && board[i][j] > 0) {
                visited[i][j] = true;
                maximum = max(maximum, 1 + dfs(i, j));
            }
        }
    }
    cout << sum << '\n'
         << maximum;
    return 0;
}
