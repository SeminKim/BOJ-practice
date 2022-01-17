#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

int N, M;
int A[50][50] = {0};
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int index[10] = {0};
int MAX_INT = 100009;
vector<pair<int, int>> virus_pos;

bool next_comb_idx(int *arr, int n, int r) {
    int pos = r - 1;
    while (pos >= 0) {
        if (arr[pos] != pos + n - r) {
            break;
        }
        pos--;
    }
    if (pos == -1) {
        return false;  // end of combination
    }
    arr[pos]++;
    for (int j = pos + 1; j < r; j++) {
        arr[j] = arr[j - 1] + 1;
    }
    return true;
}

int bfs() {
    // initalize distance array to inf.
    int distance[50][50];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            distance[i][j] = MAX_INT;
        }
    }
    // initalize BFS queue.
    deque<pair<int, int>> Q;
    for (int i = 0; i < M; i++) {
        Q.push_back(make_pair(virus_pos[index[i]].first, virus_pos[index[i]].second));
        distance[virus_pos[index[i]].first][virus_pos[index[i]].second] = 0;
    }
    // do BFS.
    while (!Q.empty()) {
        int x = Q.front().first;
        int y = Q.front().second;
        Q.pop_front();
        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            int nd = distance[x][y] + 1;
            if (0 <= nx && nx < N && 0 <= ny && ny < N && nd < distance[nx][ny]) {
                if (A[nx][ny] != 1) {
                    Q.push_back(make_pair(nx, ny));
                    distance[nx][ny] = nd;
                }
            }
        }
    }
    // find maximum and return.
    int ret = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (A[i][j] == 0) {
                ret = max(ret, distance[i][j]);
            }
        }
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M;
    // get input, save position of viruses.
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> A[i][j];
            if (A[i][j] == 2) {
                virus_pos.push_back(make_pair(i, j));
            }
        }
    }
    // get index of first combination
    for (int i = 0; i < M; i++) {
        index[i] = i;
    }
    // for each combination, do bfs and update ans to minimum.
    int ans = MAX_INT;
    do {
        ans = min(ans, bfs());
    } while (next_comb_idx(index, virus_pos.size(), M));
    // if ans is inf, print -1.
    if (ans == MAX_INT) {
        ans = -1;
    }
    cout << ans;
    return 0;
}
