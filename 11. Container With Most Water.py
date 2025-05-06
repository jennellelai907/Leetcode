class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            max_water = max(max_water, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_water