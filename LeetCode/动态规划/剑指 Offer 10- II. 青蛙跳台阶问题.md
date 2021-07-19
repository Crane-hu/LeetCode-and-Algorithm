# [剑指 Offer 10- II. 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)
> https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
>
> 难度：简单

## 题目
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

提示：
- 0 <= n <= 100

## 示例

```
示例1
输入：n = 2
输出：2

示例2
输入：n = 7
输出：21

示例3
输入：n = 0
输出：1
```

## 分析

```
该题为动态规划题目中的基本题，解题思路如下：
1. 青蛙跳至初始所在地点需要跳跃0次；
2. 青蛙跳至第一个阶梯需要跳跃1次；
3. 由此得出`dp[0]`和`dp[1]`分别为1；
4. 从第二阶台阶开始，由于青蛙每次只能跳跃0次或1次，因此，青蛙若想跳跃至第二层台阶，可选择从初始位置跳跃，也可选择从第一层台阶跳跃，由此得到`dp[2] = dp[0] + dp[1]`；
5. 以此类推，得到dp的推导公式为`dp[i] = dp[i - 1] + dp[i - 2]`
6. 返回`dp[-1]`

```

## 解题

```python
class Solution:
    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
        return dp[-1]
 ```
