class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # this is hashmap

        # iterate over the nums with index and value
        for i, num in enumerate(nums):
            diff = target - num # take out the difference

            if diff in seen:  # check if difference in seen if yes then,
                return [seen[diff], i] # return the indices
            
            seen[num] = i # else add the num with index in seen

        return [] # if no two indices found return empty list


