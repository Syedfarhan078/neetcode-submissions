class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        res = 0
        
        for i in range(n):
            if nums[i] == 1:
                count += 1
                res = max(res, count)
            elif nums[i] == 0:
                count = 0

        return res