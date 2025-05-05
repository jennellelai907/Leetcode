class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unique_num = {}

        for i in nums:
            unique_num[i] = 1

        nums[:] = list(unique_num.keys())

        return len(nums)