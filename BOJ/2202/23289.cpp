#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

int R, C, K, W, chocolate;
int delta[20][20] = {0};
int board[20][20] = {0};
int new_board[20][20] = {0};
bool is_blocked[20][20][20][20] = {false};
bool visited[20][20] = {false};
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<pair<pair<int, int>, int>> machines;
    vector<pair<int, int>> targets;
    // get input
    cin >> R >> C >> K;
    int curr;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> curr;
            switch (curr) {
                case 5:  // cells to investigate
                    targets.push_back(make_pair(i, j));
                    break;
                case 0:  // empty cell
                    break;
                default:  // cell with machine
                    machines.push_back(make_pair(make_pair(i, j), curr - 1));
            }
        }
    }
    cin >> W;
    int x, y, t;
    for (int i = 0; i < W; i++) {
        cin >> x >> y >> t;
        if (t == 0) {
            is_blocked[x - 1][y - 1][x - 2][y - 1] = true;
            is_blocked[x - 2][y - 1][x - 1][y - 1] = true;
        } else {
            is_blocked[x - 1][y - 1][x - 1][y] = true;
            is_blocked[x - 1][y][x - 1][y - 1] = true;
        }
    }
    // caculate temperature change after step 1.
    for (int m = 0; m < machines.size(); m++) {
        int r = machines[m].first.first;
        int c = machines[m].first.second;
        int d = machines[m].second;
        int front_r = dx[d];
        int front_c = dy[d];
        int side_r = dx[(d + 2) % 4];  // left or right, perpendicular to front.
        int side_c = dy[(d + 2) % 4];

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                visited[i][j] = false;
            }
        }
        deque<pair<pair<int, int>, int>> Q;
        int nr = r + front_r;
        int nc = c + front_c;
        if (0 <= nr && nr < R && 0 <= nc && nc < C && !is_blocked[r][c][nr][nc]) {
            delta[nr][nc] += 5;
            Q.push_back(make_pair(make_pair(nr, nc), 5));
        }

        while (!Q.empty()) {
            r = Q.front().first.first;
            c = Q.front().first.second;
            int num = Q.front().second;
            Q.pop_front();
            // just front
            nr = r + front_r + side_r * 0;
            nc = c + front_c + side_c * 0;
            if (num >= 1 && 0 <= nr && nr < R && 0 <= nc && nc < C && !visited[nr][nc]) {
                if (!is_blocked[r][c][nr][nc]) {
                    visited[nr][nc] = true;
                    delta[nr][nc] += num - 1;
                    Q.push_back(make_pair(make_pair(nr, nc), num - 1));
                }
            }
            // leftfront (or rightfront)
            nr = r + front_r + side_r * -1;
            nc = c + front_c + side_c * -1;
            int fr = r + side_r * -1;
            int fc = c + side_c * -1;
            if (num >= 1 && 0 <= nr && nr < R && 0 <= nc && nc < C && !visited[nr][nc]) {
                if (!is_blocked[r][c][fr][fc] && !is_blocked[fr][fc][nr][nc]) {
                    visited[nr][nc] = true;
                    delta[nr][nc] += num - 1;
                    Q.push_back(make_pair(make_pair(nr, nc), num - 1));
                }
            }
            // vice versa
            nr = r + front_r + side_r * 1;
            nc = c + front_c + side_c * 1;
            fr = r + side_r * 1;
            fc = c + side_c * 1;
            if (num > 1 && 0 <= nr && nr < R && 0 <= nc && nc < C && !visited[nr][nc]) {
                if (!is_blocked[r][c][fr][fc] && !is_blocked[fr][fc][nr][nc]) {
                    visited[nr][nc] = true;
                    delta[nr][nc] += num - 1;
                    Q.push_back(make_pair(make_pair(nr, nc), num - 1));
                }
            }
        }
    }

    while (chocolate <= 100) {
        // machine on.
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                board[i][j] += delta[i][j];
                new_board[i][j] = 0;
            }
        }
        // temperature flow. modify on smaller side.
        int ni, nj, diff;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                for (int d = 0; d < 4; d++) {
                    ni = i + dx[d];
                    nj = j + dy[d];
                    if (0 <= ni && ni < R && 0 <= nj && nj < C && board[i][j] < board[ni][nj] && !is_blocked[i][j][ni][nj]) {
                        diff = board[ni][nj] - board[i][j];
                        new_board[i][j] += diff / 4;
                        new_board[ni][nj] -= diff / 4;
                    }
                }
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                new_board[i][j] += board[i][j];
            }
        }
        swap(board, new_board);
        // cool.
        for (int i = 0; i < R; i++) {
            board[i][0] = max(0, board[i][0] - 1);
            board[i][C - 1] = max(0, board[i][C - 1] - 1);
        }
        for (int j = 1; j < C - 1; j++) {
            board[0][j] = max(0, board[0][j] - 1);
            board[R - 1][j] = max(0, board[R - 1][j] - 1);
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                new_board[i][j] += board[i][j];
            }
        }
        // eat chocolate
        chocolate++;
        // investigate temperature
        bool success = true;
        for (int t = 0; t < targets.size(); t++) {
            int r = targets[t].first;
            int c = targets[t].second;
            if (board[r][c] < K) {
                success = false;
                break;
            }
        }
        if (success) {
            break;
        }
    }
    cout << chocolate;
    return 0;
}