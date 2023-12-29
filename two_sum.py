"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:

    def twoSumone(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, v in enumerate(nums):
            result = target - v
            if result in seen.keys():
                return [seen[result], i]
            seen[v] = i
        return []

    def twoSumsecond(self, nums: list[int], target: int) -> list[int]:
        checked = {}
        for i, v in enumerate(nums):
            for elem in range(i + 1, len(nums)):
                if v not in checked:
                    if v + nums[elem] == target:
                        return [i, elem]
                else:
                    checked[v] = i
        return []

    def twoSumthird(self, nums: list[int], target: int) -> list[int]:
        for i, v in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if v + nums[j] == target:
                    return [i, j]

l = Solution()
# print(l.twoSumthird([2, 5, 5, 11], 10))
# print(l.twoSumthird([3, 2, 4], 6))
# print(l.twoSumthird([3, 3], 6))
