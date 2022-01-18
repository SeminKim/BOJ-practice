#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

int N, M;
int A[20][20];
int MAX_INT = 100003;

int solve(int x, int y, int d1, int d2) {
    int sum[5] = {0};
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (x + y <= i + j && i + j <= x + y + 2 * d2 && x - y <= i - j && i - j <= x - y + 2 * d1) {
                sum[4] += A[i][j];
            } else if (i < x + d1 && 0 <= j && j <= y) {
                sum[0] += A[i][j];
            } else if (i <= x + d2 && y < j && j <= N - 1) {
                sum[1] += A[i][j];
            } else if (x + d1 <= i && i <= N - 1 && j < y - d1 + d2) {
                sum[2] += A[i][j];
                // } else if (x + d2 < i && i <= N - 1 && y - d1 + d2 <= j && j <= N - 1) {
            } else
                sum[3] += A[i][j];
        }
    }
    sort(sum, sum + 5);
    return sum[4] - sum[0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // get input
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> A[i][j];
        }
    }
    int ans = MAX_INT;

    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            for (int d1 = 0; d1 <= y; d1++) {
                for (int d2 = 0; d2 < N - y; d2++) {
                    // if (x+d1+d2>=N || y-d1<0 || y+d2>=N) continue
                    if (x + d1 + d2 < N) {
                        ans = min(ans, solve(x, y, d1, d2));
                    }
                }
            }
        }
    }

    cout << ans;
    return 0;
}
