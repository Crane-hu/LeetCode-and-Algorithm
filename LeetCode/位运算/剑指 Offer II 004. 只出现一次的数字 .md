# [剑指 Offer II 004. 只出现一次的数字 ](https://leetcode-cn.com/problems/WGki4K/)
> https://leetcode-cn.com/problems/WGki4K/
>
> 难度：中等

## 题目
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

提示：
- 1 <= nums.length <= 3 * 104
- -231 <= nums[i] <= 231 - 1
- nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

**进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？**
## 示例

```
示例1
输入：nums = [2,2,3,2]
输出：3

示例2
输入：nums = [0,1,0,1,0,1,100]
输出：100
```

## 解题

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                cnt += num >> i & 1
            if cnt % 3:
                if i == 31:
                    ret -= (1 << i)
                else:
                    ret |= 1 << i
        return ret
 ```
