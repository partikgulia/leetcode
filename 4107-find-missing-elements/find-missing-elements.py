class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()

        rs =[]
        if len(nums)!=0:
            for i in range(nums[0],nums[len(nums)-1]):
                if i not in  nums:
                    rs.append(i)
            
        return rs

