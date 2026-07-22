class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        # firts pass = left to rigth
        left = 1
        for i, x in enumerate(nums):
            ans[i] = left
            left *= x

        # second pass = right to left
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        
        return ans