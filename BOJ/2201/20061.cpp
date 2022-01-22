#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

using namespace std;

int N;
int green[6][4] = {0};
int blue[6][4] = {0};

// delete a row and move all upper rows downward.
void burst_row(int arr[][4], int row) {
    for (int i = 0; row - i - 1 >= 0; i++) {
        for (int j = 0; j < 4; j++) {
            arr[row - i][j] = arr[row - i - 1][j];
        }
    }
    for (int j = 0; j < 4; j++) {
        arr[0][j] = 0;
    }
}

// check if a row is full and delete it.
int check_and_burst(int arr[][4], int row) {
    int ret = 0;
    bool check_burst = true;
    for (int i = 0; i < 4; i++) {
        if (arr[row][i] == 0) {
            check_burst = false;
            break;
        }
    }
    if (check_burst) {
        // add point
        ret++;
        burst_row(arr, row);
    }
    return ret;
}

// debug function
void print_minos() {
    cout << "green" << '\n';
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 4; j++) {
            cout << green[i][j] << ' ';
        }
        cout << '\n';
    }
    cout << "blue" << '\n';
    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 4; j++) {
            cout << blue[i][j] << ' ';
        }
        cout << '\n';
    }
}

int put_mino(int arr[][4], int t, int x, int y) {
    int row = 0;
    int ret = 0;
    if (t == 1) {
        while (arr[row][y] == 0 && row < 6) {
            row++;
        }
        arr[--row][y] = 1;
        ret += check_and_burst(arr, row);
        // check special cells
        for (int j = 0; j < 4; j++) {
            if (arr[1][j] == 1) {
                burst_row(arr, 5);
                break;
            }
        }
    } else if (t == 2) {
        // find available position
        while (arr[row][y] == 0 && arr[row][y + 1] == 0 && row < 6) {
            row++;
        }
        row--;
        arr[row][y] = 1;
        arr[row][y + 1] = 1;
        ret += check_and_burst(arr, row);
        // special cells
        for (int j = 0; j < 4; j++) {
            if (arr[1][j] == 1) {
                burst_row(arr, 5);
                break;
            }
        }
    } else {  // t== 3
        // find available position
        while (arr[row + 1][y] == 0 && row + 1 < 6) {
            row++;
        }
        row--;
        arr[row][y] = 1;
        arr[row + 1][y] = 1;
        // check line burst
        ret += check_and_burst(arr, row);      // upper
        ret += check_and_burst(arr, row + 1);  // lower
        // special cells
        // do it twice.
        for (int foo = 0; foo < 2; foo++) {
            for (int j = 0; j < 4; j++) {
                if (arr[1][j] == 1) {
                    burst_row(arr, 5);
                    break;
                }
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
    cin >> N;
    int ans = 0;
    while (N--) {
        int t, x, y;
        cin >> t >> x >> y;
        ans += put_mino(green, t, x, y);
        if (t == 1) {
            ans += put_mino(blue, 1, y, 3 - x);
        } else if (t == 2) {
            ans += put_mino(blue, 3, y, 3 - x);
        } else {
            ans += put_mino(blue, 2, y, 2 - x);
        }
        // print_minos();
    }

    int num = 0;
    for (int i = 2; i < 6; i++) {
        for (int j = 0; j < 4; j++) {
            num += green[i][j];
            num += blue[i][j];
        }
    }

    cout << ans << '\n'
         << num;
    return 0;
}
