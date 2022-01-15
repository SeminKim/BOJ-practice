#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

int R, C;
int A[100][100];

bool comp(pair<int, int> foo, pair<int, int> bar) {
    if (foo.second == bar.second) {
        return (foo.first < bar.first);
    }
    return (foo.second < bar.second);
}

void operation_R() {
    int counting[101];
    int changed[100][100] = {0};
    for (int row = 0; row < R; row++) {
        for (int i = 0; i < 101; i++) {
            counting[i] = 0;  // zerofill matrix for counting sort
        }
        for (int i = 0; i < C; i++) {
            counting[A[row][i]]++;  // count
        }
        vector<pair<int, int>> counts;
        for (int i = 1; i < 101; i++) {
            if (counting[i] != 0) {
                counts.push_back(make_pair(i, counting[i]));
            }
        }
        sort(counts.begin(), counts.end(), comp);
        C = max(C, 2 * (int)counts.size());
        int pos = 0;
        for (auto p : counts) {
            changed[row][pos++] = p.first;
            changed[row][pos++] = p.second;
        }
    }
    swap(A, changed);
    return;
}

void operation_C() {
    int counting[101];
    int changed[100][100] = {0};
    for (int col = 0; col < C; col++) {
        for (int i = 0; i < 101; i++) {
            counting[i] = 0;  // zerofill matrix for counting sort
        }
        for (int i = 0; i < R; i++) {
            counting[A[i][col]]++;  // count
        }
        vector<pair<int, int>> counts;
        for (int i = 1; i < 101; i++) {
            if (counting[i] != 0) {
                counts.push_back(make_pair(i, counting[i]));
            }
        }
        sort(counts.begin(), counts.end(), comp);
        R = max(R, 2 * (int)counts.size());
        int pos = 0;
        for (auto p : counts) {
            changed[pos++][col] = p.first;
            changed[pos++][col] = p.second;
        }
    }
    swap(A, changed);
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int r, c, k;
    cin >> r >> c >> k;
    R = 3;
    C = 3;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            cin >> A[i][j];
        }
    }
    int t = 0;
    while (t < 100) {
        if (A[r - 1][c - 1] == k) {
            break;
        }

        if (R >= C) {
            operation_R();
        } else {
            operation_C();
        }
        t++;
    }
    int ans = (A[r - 1][c - 1] == k) ? t : -1;
    cout << ans;
    return 0;
}