#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

int N, M, T;
deque<int> A[50];
int num[50] = {0};
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

bool dfs(int x, int y, int target) {
    bool ret = false;
    for (int d = 0; d < 4; d++) {
        int nx = x + dx[d];
        int ny = (y + M + dy[d]) % M;  // to make circular structure.
        if (0 <= nx && nx < N && A[nx][ny] == target) {
            A[nx][ny] = 0;  // erase
            num[nx]--;
            ret = true;
            dfs(nx, ny, target);
        }
    }
    return ret;
}

bool dfs() {
    bool ret = false;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (A[i][j] != 0 && dfs(i, j, A[i][j])) {
                ret = true;
            }
        }
    }
    return ret;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // get input
    cin >> N >> M >> T;
    int tmp;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> tmp;
            A[i].push_back(tmp);
        }
    }
    for (int i = 0; i < N; i++) {
        num[i] = M;
    }

    int x, d, k;
    while (T--) {
        cin >> x >> d >> k;
        for (int curr = x - 1; curr < N; curr += x) {
            if (d == 0) {
                rotate(A[curr].rbegin(), A[curr].rbegin() + k, A[curr].rend());  // CW
            } else {
                rotate(A[curr].begin(), A[curr].begin() + k, A[curr].end());  // CCW
            }
            // cout << "after rotation:" << '\n';
            // for (int i = 0; i < N; i++) {
            //     for (int j = 0; j < M; j++) {
            //         cout << A[i][j] << ' ';
            //     }
            //     cout << '\n';
            // }
        }
        if (!dfs()) {
            int sum = 0;
            int total = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    sum += A[i][j];
                }
                total += num[i];
            }
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (A[i][j] != 0) {
                        if (A[i][j] * total > sum) {
                            A[i][j]--;
                        } else if (A[i][j] * total < sum) {
                            A[i][j]++;
                        }
                    }
                }
            }
        }
        // cout << "now:" << T << '\n';
        // for (int i = 0; i < N; i++) {
        //     for (int j = 0; j < M; j++) {
        //         cout << A[i][j] << ' ';
        //     }
        //     cout << '\n';
        // }
    }

    int ans = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            ans += A[i][j];
        }
    }

    cout << ans;
    return 0;
}
