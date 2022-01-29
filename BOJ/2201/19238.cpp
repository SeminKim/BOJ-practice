#include <algorithm>
#include <deque>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int N, M, F;
int x, y;
int board[20][20] = {0};
int distance_board[20][20];
int MAX_DIST = 1000;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
map<pair<int, int>, pair<int, int>> customer;

void get_all_distance() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            distance_board[i][j] = MAX_DIST;
        }
    }
    deque<pair<int, int>> Q;
    Q.push_back(make_pair(x, y));
    distance_board[x][y] = 0;
    while (Q.size() != 0) {
        int row, col;
        tie(row, col) = Q.front();
        Q.pop_front();
        for (int d = 0; d < 4; d++) {
            int nrow = row + dx[d];
            int ncol = col + dy[d];
            int ndist = distance_board[row][col] + 1;
            if (0 <= nrow && nrow < N && 0 <= ncol && ncol < N && board[nrow][ncol] != 1 && ndist < distance_board[nrow][ncol]) {
                distance_board[nrow][ncol] = ndist;
                Q.push_back(make_pair(nrow, ncol));
            }
        }
    }
}

bool taxi() {
    // first, do bfs to find next target customer.
    get_all_distance();
    pair<int, int> nearest_customer;
    int nearest_distance = MAX_DIST;
    for (auto iter : customer) {
        pair<int, int> key = iter.first;
        if (distance_board[key.first][key.second] < nearest_distance) {
            nearest_distance = distance_board[key.first][key.second];
            nearest_customer = key;
        }
    }
    // stop iteration if customer was not found
    if (nearest_distance == MAX_DIST) {
        if (customer.size() != 0) {
            F = -1;
        }
        return false;
    }
    // stop iteration if fuel is low
    if (F < nearest_distance) {
        F = -1;
        return false;
    }
    // move taxi to customer position
    F -= nearest_distance;
    x = nearest_customer.first;
    y = nearest_customer.second;

    // move taxi to goal.
    get_all_distance();
    pair<int, int> goal = customer[nearest_customer];
    x = goal.first;
    y = goal.second;
    int used = distance_board[x][y];
    customer.erase(nearest_customer);
    if (used == MAX_DIST || F < used) {
        F = -1;
        return false;
    }
    // refill fuel twice.
    F += used;
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // get input
    cin >> N >> M >> F;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }
    cin >> x >> y;
    x--, y--;  // zero-based index
    for (int i = 0; i < M; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        customer[make_pair(a - 1, b - 1)] = make_pair(c - 1, d - 1);
    }
    while (taxi()) {
    }
    cout << F;
    return 0;
}
