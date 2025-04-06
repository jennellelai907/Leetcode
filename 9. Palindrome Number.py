class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# 切片（slice），用來提取序列（例如：字串、列表、元組等）中的一部分元素
# sequence[start:stop:step]


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  
            return False  # 負數 & 以 0 結尾的數（除了 0）不可能是回文數

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
