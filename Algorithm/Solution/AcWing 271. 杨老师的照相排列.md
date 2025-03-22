---
title: AcWing 271
date: 2022/10/14
categories:
  - - Algorithm
    - Solution
tags: null
abbrlink: cb854ff4
---


# AcWing 271. 杨老师的照相排列
## 前言

## 相关分析
### 时间复杂度
由均值不等式，最坏情况下共有 (Nk)k(Nk)k 状态，计算每个状态需要 O(k)O(k) 的计算量，因此总时间复杂度是 O(k(Nk)k)O(k(Nk)k)。
https://www.acwing.com/solution/content/4954/

## 代码
```c++
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
const int N = 31;
int k = 1;
long long dp[N][N][N][N][N];
int main()
{
    while (cin >> k, k)
    {
        int n[6] = {0};
        for (int i = 1; i <= k; ++i)
        {
            cin >> n[i];
        }
        memset(dp, 0, sizeof(dp));
        dp[0][0][0][0][0] = 1;
        for (int a = 0; a <= n[1]; a++)
        {
            for (int b= 0; b<= min(a, n[2]); b++)
            {
                for (int c = 0; c <= min(b, n[3]); c++)
                {
                    for (int d= 0; d <= min(d, n[4]); d ++)
                    {
                        for (int e = 0; e <= min(e, n[5]); e ++)
                        {
                            long long &x = dp[a][b][c][d][e];
                            if (a && a - 1 >= b) x += dp[a - 1][b][c][d][e];
                            if (b && b - 1 >= c) x += dp[a][b - 1][c][d][e];
                            if (c && c - 1 >= d) x += dp[a][b][c - 1][d][e];
                            if (d && d - 1 >= e) x += dp[a][b][c][d - 1][e];
                            if (e) x += dp[a][b][c][d][e - 1];
                        }
                    }
                }
            }
        }
        cout << dp[n[1]][n[2]][n[3]][n[4]][n[5]] << endl;
    }

    return 0;
}

```