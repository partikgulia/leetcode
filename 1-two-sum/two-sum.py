class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        for indx,val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [indx,hashmap[diff]]
            hashmap[val]=indx

        
        