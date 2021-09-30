// Implementation in C++ reduces computation time sufficiently!

#include <iostream>

int main()
{
    int n;
    scanf("%d", &n);
    int num_in_bucket[1000] = {0};
    int candy[1000000] = {0};
    int flag, target, num;

    while (n > 0)
    {
        scanf("%d", &flag);
        if (flag == 1)
        {
            scanf("%d", &target);
            int tmp = 0;
            int idx = 0;
            while (tmp < target)
            {
                tmp += num_in_bucket[idx];
                idx += 1;
            }
            idx -= 1;
            tmp -= num_in_bucket[idx];
            num_in_bucket[idx] -= 1;
            idx *= 1000;
            while (tmp < target)
            {
                tmp += candy[idx];
                idx += 1;
            }
            idx -= 1;
            candy[idx] -= 1;
            printf("%d\n", idx+1);
        }
        else
        {
            scanf("%d%d", &target, &num);
            target -= 1;
            candy[target] += num;
            num_in_bucket[target / 1000] += num;
        }
        n -= 1;


    }
}