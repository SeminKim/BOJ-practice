#include <iostream>
typedef long long ll;

int main(void)
{
    int n, q;
    scanf("%d%d", &n, &q);
    ll *tree = new ll[2 * n];
    for (int i = n; i < 2 * n; i++)
    {
        scanf("%d", &tree[i]);
    }

    // initialize
    for (int i = n - 1; i > -1; i--)
    {
        tree[i] = tree[2 * i] + tree[2 * i + 1];
    }

    int x, y, a, b;
    for (q; q > 0; q--)
    {
        scanf("%d%d%d%d", &x, &y, &a, &b);
        if (x > y)
        {
            int temp = x;
            x = y;
            y = temp;
        }

        // query
        ll res = 0;
        x += n - 1;
        y += n - 1;
        a += n - 1;

        while (x < y)
        {
            if (x % 2 == 1)
            {
                res += tree[x++];
            }

            if (y % 2 == 0)
            {
                res += tree[y--];
            }
            x >>= 1;
            y >>= 1;
        }

        if (x == y)
        {
            res += tree[x];
        }

        printf("%lld\n", res);

        // update
        tree[a] = b;
        while (a > 0)
        {
            tree[a >> 1] = tree[a] + tree[a ^ 1];
            a >>= 1;
        }

        // for (int j = 1; j < 2 * n; j++)
        // {
        //     printf("%d/", tree[j]);
        // }
    }
}