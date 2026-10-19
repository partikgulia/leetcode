class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        for index, value in enumerate(nums):
            if value == target:
                res.append(index)
        return res
        