class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_no_val = []

        for i in nums:
            if i != val:
                nums_no_val.append(i)
        
        nums[:] = nums_no_val

        return len(nums)

