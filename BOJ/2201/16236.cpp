#include <iostream>
#include <utility>
#include <tuple>
#include <deque>

using namespace std;

int n;
int board[20][20];
int shark_r, shark_c, shark_size, shark_acc;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};
int MAX_DIST = 1000;

tuple<int, int, int> bfs()
{
    int visited[20][20] = {0};
    int distance[20][20] = {0};
    int min_dist = MAX_DIST;
    visited[shark_r][shark_c] = 1;
    distance[shark_r][shark_c] = 0;
    deque<tuple<int, int, int>> queue;
    queue.push_back(make_tuple(shark_r, shark_c, 0));
    while (!queue.empty())
    {
        int x, y, dist;
        tie(x, y, dist) = queue.front();
        queue.pop_front();
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && board[nx][ny] <= shark_size)
            {
                if (board[nx][ny] != 0 && board[nx][ny] < shark_size)
                {
                    min_dist = min(min_dist, dist + 1);
                }
                visited[nx][ny] = 1;
                distance[nx][ny] = dist + 1;
                queue.push_back(make_tuple(nx, ny, dist + 1));
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (distance[i][j] == min_dist && board[i][j] != 0 && board[i][j] < shark_size)
                return make_tuple(i, j, min_dist);
        }
    }

    return make_tuple(-1, -1, -1);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> board[i][j];
            if (board[i][j] == 9)
            {
                board[i][j] = 0;
                shark_r = i;
                shark_c = j;
            }
        }
    }
    shark_size = 2;
    shark_acc = 0;
    int ans = 0;
    while (true)
    {
        int x, y, d;
        tie(x, y, d) = bfs();
        if (d == -1)
            break;
        shark_r = x;
        shark_c = y;
        ans += d;
        shark_acc += 1;
        board[x][y] = 0;
        if (shark_acc == shark_size)
        {
            shark_acc = 0;
            shark_size++;
        }
    }
    cout << ans;
    return 0;
}