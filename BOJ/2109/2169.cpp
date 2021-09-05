// O(n^3) but it passes!

#include <iostream>

int main()
{
    int n, m;
    int INF = 1000000000;
    scanf("%d%d", &n, &m);
    int seq[n][m];
    int dp[n][m];

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            int foo;
            scanf("%d", &foo);
            seq[i][j] = foo;
            dp[i][j] = -INF;
        }
    }

    int foo = 0;
    for (int i = 0; i < m; i++)
    {
        foo += seq[0][i];
        dp[0][i] = foo;
    }

    for (int row = 0; row < n - 1; row++)
    {
        for (int col = 0; col < m; col++)
        {
            int partial = dp[row][col];
            for (int x = col; x > -1; x--)
            {
                partial += seq[row + 1][x];
                if (partial > dp[row + 1][x])
                    dp[row + 1][x] = partial;
            }
            partial = dp[row][col];
            for (int x = col; x < m; x++)
            {
                partial += seq[row + 1][x];
                if (partial > dp[row + 1][x])
                    dp[row + 1][x] = partial;
            }
        }
    }

    printf("%d", dp[n - 1][m - 1]);

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         printf("%d/", seq[i][j]);
    //     }
    //     printf("\n");
    // }
    // printf("================================\n");
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         printf("%d/", dp[i][j]);
    //     }
    //     printf("\n");
    // }
}