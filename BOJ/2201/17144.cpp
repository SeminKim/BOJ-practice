#include <algorithm>
#include <iostream>

using namespace std;

int R, C, T;
int A[50][50];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int origins[2] = {0, 0};

void dust_diffusion() {
    int delta[50][50] = {0};
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (A[i][j] > 0) {
                for (int d = 0; d < 4; d++) {
                    int x = i + dx[d];
                    int y = j + dy[d];
                    if (0 <= x && x < R && 0 <= y && y < C && A[x][y] != -1) {
                        delta[i][j] -= A[i][j] / 5;
                        delta[x][y] += A[i][j] / 5;
                    }
                }
            }
        }
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            A[i][j] += delta[i][j];
        }
    }
}

void upper_circulation() {
    int origin_x = origins[0];
    int temp = A[origin_x][1];
    // lower row
    for (int i = 2; i < C; i++) {
        swap(temp, A[origin_x][i]);
    }
    A[origin_x][1] = 0;  // fresh air comes out.
    // right col
    for (int i = origin_x - 1; i >= 0; i--) {
        swap(temp, A[i][C - 1]);
    }
    // upper row
    for (int i = C - 2; i >= 0; i--) {
        swap(temp, A[0][i]);
    }
    // right col
    for (int i = 1; i < origin_x; i++) {
        swap(temp, A[i][0]);
    }
    // last portion will be absorbed.
}

void lower_circulation() {
    int origin_x = origins[1];
    int temp = A[origin_x][1];
    // upper row
    for (int i = 2; i < C; i++) {
        swap(temp, A[origin_x][i]);
    }
    A[origin_x][1] = 0;  // fresh air comes out.
    // right col
    for (int i = origin_x + 1; i < R; i++) {
        swap(temp, A[i][C - 1]);
    }
    // lower row
    for (int i = C - 2; i >= 0; i--) {
        swap(temp, A[R - 1][i]);
    }
    // left col
    for (int i = R - 2; i > origin_x; i--) {
        swap(temp, A[i][0]);
    }
    // last portion will be absorbed.
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> R >> C >> T;
    int foo = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> A[i][j];
            if (A[i][j] == -1) {
                origins[foo++] = i;
            }
        }
    }
    while (T--) {
        dust_diffusion();
        upper_circulation();
        lower_circulation();
    }
    int ans = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            ans += A[i][j];
        }
    }
    cout << ans + 2;
    return 0;
}