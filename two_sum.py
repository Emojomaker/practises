"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, v in enumerate(nums):
            result = target - v
            if result in seen.keys():
                return [seen[result], i]
            seen[v] = i
        return []

l = Solution()
print(l.twoSum([2, 7, 11, 15], 9))
print(l.twoSum([3, 2, 4], 6))
print(l.twoSum([3, 3], 6))
